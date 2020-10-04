Title: Go: defining methods on struct types
Date: 2015-03-16 20:24
Author: admin
Category: Go
Tags: go, golang, programming, struct
Slug: go-defining-methods-on-struct-types
Status: published

In **Go** it's possible to define **methods** on **struct types**. The
syntax needed for it can be a bit strange for people that are used to
define classes and methods in Java, C\# etc... but once you learn it
it's quite easy to use.

In my case for example I needed something that could contain a Timer
object, a string and a method that could start the timer and call a
method at the end of the Timer execution. I implemented it in this way:

``` {.toolbar:2 .lang:go .decode:true}
type DeviceTimer struct {
    DeviceID    string
    DeviceTimer *time.Timer
}

func (timer DeviceTimer) startTimer() {
    <-timer.DeviceTimer.C
    notifyDeviceTimerExpired(timer.DeviceID)
}
```

The key point is **row 6** "*func (timer DeviceTimer) startTimer() { ...
}*" where I defined a method called **startTimer** and I specify timer
**DeviceTimer** inside the func definition. This basically "extends" the
struct DeviceTimer adding that method to it. This means that I can call
that method in this way:

``` {.toolbar:2 .lang:go .decode:true}
timer := time.NewTimer(time.Millisecond * 300)
device_timer := DeviceTimer{"abc123", timer}
go device_timer.startTimer()
```

This is all you need to do. If you want to read more about this subject,
I can suggest to read these two articles:

-   **Go by Example: Methods** <https://gobyexample.com/methods>
-   **Inheritance and subclassing in Go - or its near likeness**
    <http://golangtutorials.blogspot.co.uk/2011/06/inheritance-and-subclassing-in-go-or.html>

**Note:** I'm not a Go expert and these are just my personal notes I'm
taking during my learning experience. I'm very keen to share my notes
with everyone, but please don't take them as notes from an expert Go
developer.
