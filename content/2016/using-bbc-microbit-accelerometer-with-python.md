Title: Using BBC MicroBit accelerometer with Python
Date: 2016-01-26 22:41
Author: Andrea Grandi
Category: Development
Tags: bbc, microbit, Python, howto
Slug: using-bbc-microbit-accelerometer-with-python
Status: published

In these days I'm having a bit of fun with **[BBC
MicroBit](https://www.microbit.co.uk/)** board and I'm learning how to
use the different sensors available. The latest one I wanted to try was
the accelerometer. The board can "sense" if you are moving it in any of
the 3 dimensional axes: X, Y, Z. According to the
[documentation](https://microbit-micropython.readthedocs.org/en/latest/accelerometer.html)
there are four methods available that can be used to get these
values: **microbit.accelerometer.get\_values()** will return you a tuple with all the 3 values, while 
**microbit.accelerometer.get\_x()**, **microbit.accelerometer.get\_y()**, **microbit.accelerometer.get\_z()**
will give you the single values.

The documentation on the official website doesn't explain much and for
example I didn't even know what was the range of the values I can get
back from these methods (by the way it's **between -1024** and
**1024**), so I decided to play with the code directly and write a very
simple example. The small example I wrote, shows a smile on the board
display if you keep it straight and shows a sad face if you bend it.

This is the result:

<iframe width="420" height="315" src="https://www.youtube.com/embed/LX8fYBsOxA0" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

and this is all the needed code of the application:

<p>
<script src="https://gist.github.com/andreagrandi/f4a7c8ee8597dde3070d.js"></script>
</p>

In the next days I will try to play with more sensors and to publish
other examples.
