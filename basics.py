'''
Python3 Basics and Important Concept Notes

https://realpython.com/instance-class-and-static-methods-demystified
https://realpython.com/list-comprehension-python/
timeit, filter, map, list comprehension,genrators,lambda fn, decorator, closure, unit testing, type checking in python
https://realpython.com/python-lambda/
docstrings, kwargs, vargs https://python.swaroopch.com/functions.html , closures: https://blog.bitsrc.io/closures-in-javascript-why-do-we-need-them-2097f5317daf 
memory profiling: sys.getsizeof() https://realpython.com/introduction-to-python-generators/#building-generators-with-generator-expressions
magic: dir(), dir(str) => gives all names and imports from curr module, importe module or data type
'''


class myclass:
    def __init__(self):
        self.x = 40

    def __repr__(self):
        return f'i am a class with x={self.x}'

    def instanceMethod(self, a=10):
        self.x=a
        return 'instance method called. has access to instance and class states', self

    @classmethod
    def classMethod(cls):
        '''helps add factory functions with many initializations + self-documenting in nature'''
        return 'class method called. has access to class state only', cls

    @staticmethod
    def staticMethod():
        return 'static method called. has access to nothing, only here for namespace'


if __name__=="__main__":
    obj= myclass()
    print(obj.instanceMethod())
    print(myclass.classMethod())
    print(obj.classMethod())
    print(myclass.staticMethod())
    print(obj.staticMethod())
    print(obj)
    print(myclass)
    print(myclass())
    obj.instanceMethod(100)
    print(obj)
    #filter map
    n=[1,2,3,4,5,6]
    print(list(map(lambda i:i*i, filter(lambda x:x%2==0, n))))
    #reduce
    from functools import reduce
    print(reduce(lambda x,y: x+y, n))
    #list comprehension
    print([a for a in n if a%2==1])
    #generator
    print((a for a in n if a%2==1))
    print(list(a for a in n if a%2==1))

    