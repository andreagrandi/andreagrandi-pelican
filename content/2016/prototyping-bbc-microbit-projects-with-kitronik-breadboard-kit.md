Title: Prototyping BBC micro:bit projects with Kitronik breadboard kit
Date: 2016-02-07 21:47
Author: Andrea Grandi
Category: Development
Tags: bbc, embedded, microbit, micropython, python
Slug: prototyping-bbc-microbit-projects-with-kitronik-breadboard-kit
Status: published

**BBC micro:bit** has a few [IO
pins](http://microbit-micropython.readthedocs.org/en/latest/pin.html)
that can be used to interact with external devices. The problem with the
board is that it's not easy to connect the classic jumper wires (those
that we normally connect to a breadboard) to the **micro:bit**, unless
using a [crocodile clip](https://en.wikipedia.org/wiki/Crocodile_clip)
and being limited to just 3 pins.

[**Kitronik breadboard
kit**](https://www.kitronik.co.uk/5609-prototyping-system-for-the-bbc-microbit.html)
solves this problem, offering an interface where the micro:bit can be
plugged and all the pins are easily connectable to the breadboard using
normal [male/female jumper wires](https://www.adafruit.com/products/826).

I've built a very simple circuit following an example you can find on
this manual <https://www.kitronik.co.uk/pdf/5603_inventors_kit_for_the_bbc_microbit_tutorial_book.pdf>

[![microbit\_breadboard\_example\_1]({filename}/images/2016/02/microbit_breadboard_example_1.jpg){ width=40% }]({filename}/images/2016/02/microbit_breadboard_example_1.jpg)

To build the circuit you also need **4 male/female jumper wires** and
**two buttons**. All this circuit does is to connect the buttons to the
**micro:bit** pins that relate to those buttons. Basically pressing
those buttons is the same as pressing **button A** or **button B** on
the **micro:bit** board. Here you can see the schema in detail:

[![Screenshot 2016-02-0714.30.36]({filename}/images/2016/02/Screenshot-2016-02-07-14.30.36.png){ width=40% }]({filename}/images/2016/02/Screenshot-2016-02-07-14.30.36.png)

###### "Image Copyright © Kitronik" {#image-copyright-kitronik style="text-align: center;"}

I've also made a short **video** so that you can see it in action:

<iframe width="420" height="315" src="https://www.youtube.com/embed/0Zfa1sBP7yI" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

And of course the **source code** is available too:

<p>
<script src="https://gist.github.com/andreagrandi/9f66f6806d0ce577bada.js"></script>
</p>
