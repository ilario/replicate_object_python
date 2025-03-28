import mpmath
from replicate_object import replicate_object

def test_module_string():
    mp1 = mpmath.mp
    mp2 = mpmath.mp
    mp3 = replicate_object(mpmath, "mp")
    mp4 = replicate_object(mpmath, "mp")
    original_prec = mp1.prec
    mp1.prec = 123
    mp3.prec = 321
    # mp1 and mp2 have been created in the classic way, so they share the descriptors
    assert(mp2.prec == 123)
    # mp4 is independent from the others
    assert(mp4.prec == original_prec)

def test_module_list():
    mp1 = mpmath.mp
    mp2, mp3 = replicate_object(mpmath, ["mp","mp"])
    mp1.prec = 123
    mp2.prec = 321
    # mp3 has been taken from the same exec as mp2, so they share the descriptors
    assert(mp3.prec == 321)

# the test with the class is inspired by this question:
# https://stackoverflow.com/q/1004168/5033401
def test_class():
    from replicate_object import class_testing
    class1, descriptor1 = replicate_object(class_testing, ["MyClass","MyDescriptor"])
    class2, descriptor2 = replicate_object(class_testing, ["MyClass","MyDescriptor"])
    assert(class_testing.test1(class1, descriptor1))
    assert(class_testing.test1(class2, descriptor2))
    assert(class_testing.test2(class1, class2))



