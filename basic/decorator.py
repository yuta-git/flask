# def sample_decorator(myfunc):
#   print("I am the decorator!")
#   return 0

# @sample_decorator
# def myfunc():
#   pass

def my_decorator(func):
  def wapper():
    print("Before the function is called.")
    func()
    print("After the function is called.")
  return wapper

@my_decorator
def say_hello():
  print("Hello!")
  
say_hello()

def sample_decorator(myfunc):
  def inner_func(text):
    return "I am the decorator!"
  return inner_func

@sample_decorator
def myfunc(text):
  return text

print(myfunc("Blabla"))

class MyClass():
  @classmethod
  def myfunc(cls): #第一引数が必要
    print("I am a class method")
    
MyClass.myfunc()

class StaticMyClass:
  @staticmethod
  def myfunc():
    return "I am a static method"

print(StaticMyClass.myfunc())

class PropMyClass():
  def __init__(self):
    self._x = 12345
  @property
  def x(self):
    return self._x
  
instance = PropMyClass()
# instance.x = 1234  #エラー(read only)
print(instance.x)
    

class MethodMyClass():
  CONST = 10 #クラス変数
  
  def __init__(self, x):
    self.x = x #インスタンス変数
    
  def add0(self, y, z):  #インスタンスメソッド
    return self.x + y + z
  
  @classmethod #クラスメソッド
  def add1(cls, y, z):
    return cls.CONST + y + z
  
  @staticmethod #スタティックメソッド
  def add2(y, z):
    return y + z
  
  
