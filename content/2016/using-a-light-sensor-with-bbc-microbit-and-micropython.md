Title: Using a light sensor with BBC micro:bit and MicroPython
Date: 2016-02-08 22:49
Author: Andrea Grandi
Category: Development
Tags: bbc, breadboard, embedded, microbit, micropython, howto, python
Slug: using-a-light-sensor-with-bbc-microbit-and-micropython
Status: published

A **[light sensor](https://en.wikipedia.org/wiki/Photoresistor)** is a
small component with a particular characteristic: it is basically a
resistor and its resistance decreases if the light is more intense. To
use it with micro:bit we need to use one of the **analogic ports**. To
build this circuit you will need a **breadboard**, **3 jumper wires**, a
**10k resistance** and possibly a **[Kitronik breadboard
kit](https://www.kitronik.co.uk/5609-prototyping-system-for-the-bbc-microbit.html)**.

### The project

I wanted to realise a simple project where, depending on the light
intensity captured by the light sensor, the **micro:bit** shows an image
of the **Sun** if the light is intense and an image of the **Moon** if
the light is less intense.

Here is the complete **circuit scheme**:

[![microbit\_breadboard\_schema\_light]({filename}/images/2016/02/microbit_breadboard_schema_light.png){ width=40% }]({filename}/images/2016/02/microbit_breadboard_schema_light.png)

###### "Image Copyright © Kitronik"

and here is a picture of the **finished project** I created:

[![microbit\_breadboard\_example\_2]({filename}/images/2016/02/microbit_breadboard_example_2.jpg){ width=40% }]({filename}/images/2016/02/microbit_breadboard_example_2.jpg)

The **source code** I needed is available here:

<p>
<script src="https://gist.github.com/andreagrandi/99a09be27c9626b1119d.js"></script>
</p>
and as a demo I realised this small **video**:

<iframe width="420" height="315" src="https://www.youtube.com/embed/6vLE_AQc4Bc" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
