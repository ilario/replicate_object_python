def replicate_object(object_or_parent, wanted_objects_names):
    """
    Takes an object or the module including that object, executes again the
    code that defines it, and returns the requested objects.

    Providing the module as the first argument is convenient in cases where
    the object definition requires some other modules to be already imported.

    It has been designed for having independent instances of the same class,
    without having the class descriptors being the same for all the instances.

    wanted_objects_names can be either a string, with the name of the desired
    object to be returned, or a list containing the strings of the names of the objects

    Documented here:
    https://stackoverflow.com/a/79539546/5033401

    Usage example:
    >>> from replicate_object import replicate_object
    >>> import mpmath
    >>> mp1 = mpmath.mp
    >>> mp2 = mpmath.mp
    >>> mp3 = replicate_object(mpmath, "mp")
    >>> mp4, sin4 = replicate_object(mpmath, ["mp","sin"])
    >>> mp1.prec = 123
    >>> mp4.prec = 321
    >>> mp1.prec
    123
    >>> mp2.prec
    123
    >>> mp3.prec
    53
    >>> mp4.prec
    321
    """
    import sys, os, inspect
    source = inspect.getsource(object_or_parent)
    try:
        globals()["__package__"] = object_or_parent.__name__
        sys.path.append(os.path.dirname(inspect.getfile(object_or_parent)))
    except:
        pass
    exec(source, globals())
    if isinstance(wanted_objects_names, str):
        return globals()[wanted_objects_names]
    else:
        print(globals())
        return (globals()[key] for key in wanted_objects_names)

def class_test_functions():
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

