class MyDescriptor:
    def __set__(self, instance, value):
        print("__set__ called: ", value)

class MyClass:
    a = MyDescriptor()

def test1( class_in, descriptor ):
    o = class_in()
    o.a = "test"
    if isinstance(o.a, descriptor):
        return True # pass
    else:
        return False # fail

def test2( class_in1, class_in2 ):
    o1, o2 = class_in1(), class_in2()
    if o1.a is o2.a:
        return False # fail
    else:
        return True # pass

