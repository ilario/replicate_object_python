# replicate_object
Create an identical but independent copy of an object in Python.

Inspired by [this answer by Nizam Mohamed](https://stackoverflow.com/a/35794584/5033401).

This code has been first proposed [here](https://stackoverflow.com/a/79539546/5033401).

## Rationale

Class descriptors are in common for all instances of that class. They are the variables defined outside the __init__() block of the class. This is by design, so that if you modify their value on one instance, you modify it on all of them.

If you don't want these variables to be shared by all instances, you should just rewrite the class.

If you don't want to rewrite a big class made by someone else, you need some alternative solution.

In my case, this originated with [this observation](https://github.com/adafruit/Adafruit_CircuitPython_INA219/issues/38), where I was using many instances of the same class, but setting and getting values from its descriptors differently for each instance.

## Concept

Takes an object or the module including that object, executes again the code that defines it, and returns the requested objects.

Providing the module as the first argument is convenient in cases where the object definition requires some other modules to be already imported.

It has been designed for having independent instances of the same class, without having the class descriptors being the same for all the instances.

The parameter wanted_objects_names can be either a string, with the name of the desired object to be returned, or a list containing the strings of the names of the objects

## Usage example

```
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
```
