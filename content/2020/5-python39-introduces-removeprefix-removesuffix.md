Title: Python 3.9 introduces removeprefix and removesuffix
Date: 2020-10-11 19:00
Author: Andrea Grandi
Category: Development
Tags: python, development, python39, programming, version, language, strings, manipulation
Slug: python39-introduces-removeprefix-removesuffix
Status: published
Summary: A quick tutorial to removeprefix and removesuffix methods which have been introduced with Python 3.9.0

[Python 3.9.0](https://docs.python.org/3/whatsnew/3.9.html) has introduced two new methods to work with strings: `removeprefix` and `removesuffix`.
As their names suggest, one is used to remove a prefix from a string while the other one is used to remove a suffix.

## removeprefix

Given a string and a prefix, if the string begins with the prefix, the prefix is being removed, otherwise a copy of the original string is being returned:

    :::python
    In [5]: 'MyStringExample'.removeprefix('My')
    Out[5]: 'StringExample'

    In [6]: 'MyStringExample'.removeprefix('Foo')
    Out[6]: 'MyStringExample'

## removesuffix

Given a string and a suffix, if the string ends with the suffix, the suffix is being removed, otherwise a copy of the original string is being returned:

    :::python
    In [7]: 'ThisIsATest'.removesuffix('Test')
    Out[7]: 'ThisIsA'

    In [8]: 'ThisIsATest'.removesuffix('Foo')
    Out[8]: 'ThisIsATest'

Of course these are not the only features which have been added to **Python 3.9.0**, so I may cover more in the next days. If in the mean time you have **any preferences, please leave a comment below** and thanks for reading.

## References

- <https://docs.python.org/3/library/stdtypes.html#str.removeprefix>
- <https://docs.python.org/3/library/stdtypes.html#str.removesuffix>
