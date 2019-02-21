Title: Skipping tests depending on the Python version
Date: 2019-02-21 20:00
Author: Andrea Grandi
Category: Python
Tags: python, test, programming, software, development, testing
Slug: skipping-tests-depending-python-version
Status: published

Sometimes we want to run certain tests only on a specific version of Python.

Suppose you are migrating a large project from Python 2 to Python 3 and you know in advance that certain tests won't run
under Python 3.

Chances are that during the migration you are already using the [six](https://pythonhosted.org/six/) library. The **six** libraries have
two boolean properties which are initialised to `True` depending on the Python version which is being used: `PY2` when running under Python 2
and `PY3` when running under Python 3.

This library, combined with the **skipIf** method of [unittest library](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures)
can be used to easily skip tests when using Python 3:

    :::python
    import six
    import unittest


    class MyTestCase(unittest.TestCase):


        @unittest.skipIf(six.PY3, "not compatible with Python 3")
        def test_example(self):
            # This test won't run under Python 3
            pass

## Credits

Thanks to my colleague **[Nicola](https://github.com/valnico)** for giving me the inspiration to write this post.
