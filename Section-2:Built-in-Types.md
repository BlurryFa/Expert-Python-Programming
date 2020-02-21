# 一、python的built-in types
## Strings and bytes

* **str** ：存储文本信息

  * 对字符串进行编码
  
    > str.encode(encoding, errors)
     
    > bytes(source, encoding, errors)
  * 字符串拼接
  
    > str.join() 比 '+' 更高效
    
    > "".join(substrings) 或者 str.join("", substrings)
   
  * 字符串formatting with f-strings
  
    * Using % formatting. for example:  "Some string with included % value" % "other"
    
    * Using the  str.format() method. for example:  "Some string with included {other} value".format(other="other")
    
    * Using f-strings. for example:  f"This is Python {version_info.major}.{version_info.minor}"
    

* **bytes** ：存储元二进制数据，必须要加b前缀
  * 对字节进行解码
  
    >  bytes.decode(encoding, errors)
    
    >  str(source, encoding, error)
    
## Containers

* **Lists**

  |Operations         |Complexity        |
  |-------------------|------------------|
  |Copy               |O(n)              |
  |Append             |O(1)              |
  |Insert             |O(n)              |
  |Get item           |O(1)              |
  |Set item           |O(1)              |
  |Delete item        |O(n)              |
  |Iteration          |O(n)              |
  |Get slice of length k|O(k)            |
  |Del slice          |O(n)              |
  |Set slice of length k|O(k+n)          |
  |Extend             |O(k)              |
  |Multiply by k      |O(nk)             |
  |Test existence ( element in list ) |O(n)|
  |min() / max()      |O(n)              |
  |Get length         |O(1)              |
  
* **Tuples**
  
* **Dictionaries** (自3.6后，Dict按插入顺序存储key，或者可以使用collections.OrderedDict)

  * 三个关键methods
  
    > keys() : This returns the  dict_keys object which provides a view on all keys of the dictionary
  
    > values() : This returns the  dict_values object which provides a view on all values of the dictionary
  
    > items() : This returns the  dict_items object, providing views on all  (key, value) two-tuples of the dictionary
  
  * 只有hashable的objects才可以作为dictionary key
  
    hashable协议有两个methods组成
  
      * \_\_hash\_\_ : This provides the hash value (as an integer) that is needed by the internal  dict implementation. For objects that are instances of user-defined classes, it is derived from their  id() 
      * \_\_eq\_\_ : This compares if two objects have the same value. All objects that are instances of user-defined classes compare as unequal by default, except for themselves.
  
  |Operation|Average complexity| Amortized worst case complexity|
  |-|-|-|
  |Get item |O(1) |O(n)|
  |Set item |O(1) |O(n)|
  |Delete item |O(1) |O(n)|
  |Copy |O(n) |O(n)|
  |Iteration |O(n) |O(n)|
  
* **Sets**
  > set() : This is a mutable, non-ordered, finite collection of unique, immutable (hashable) objects
  
  > frozenset() : This is an immutable, hashable, non-ordered collection of unique, immutable (hashable) objects
  
  |Operation|Average complexity| Amortized worst case complexity|
  |-|-|-|
  |Add item|O(1)|O(n)|
  |Delete item|O(1)|O(n)|
  |Test for existense|O(1)|O(n)|
  
## Supplemental data types and containers(from collections)

* **namedtuple** : This is a factory function for creating tuple subclasses whose indexes can be accessed as named attributes
  
* **deque** : This is a double-ended queue—a list-like generalization of stacks and queues with fast appends and pops on both ends
  
* **ChainMap** : This is a dictionary-like class to create a single view of multiple mappings
  
* **Counter** : This is a dictionary subclass for counting hashable objects
  
* **OrderedDict** : This is a dictionary subclass that preserves the order that the entries were added in
  
* **defaultdict** : This is a dictionary subclass that can supply missing values using a user-defined factory function
  
## Symbolic enumeration with the enum module

``` Python

from enum import Enum, auto


class OrderStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    PROCESSED = auto()
    
    
class Order:
    def __init__(self):
        self.status = OrderStatus.PENDING
        
    def process(self):
        if self.status == OrderStatus.PROCESSED:
            raise RuntimeError(
                "Can't process order that has "
                "been already processed"
            )
        self.status = OrderStatus.PROCESSING
        ...
        self.status = OrderStatus.PROCESSED
```

Store selections of non-exclusive choices.

``` Python
from enum import Flag, auto


class Side(Flag):
    GUACAMOLE = auto()
    TORTILLA = auto()
    FRIES = auto()
    BEER = auto()
    POTATO_SALAD = auto()
```
