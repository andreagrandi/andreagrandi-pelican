Title: Nokia N900: reboot loop after PR 1.1.1 upgrade is not a firmware bug
Date: 2010-02-20 02:50
Author: admin
Category: Linux, Maemo (EN), MeeGo
Tags: firmware, maemo, MeeGo, N900, nokia
Slug: nokia-n900-reboot-loop-after-pr-1-1-1-upgrade-is-not-a-firmware-bug
Status: published

Few days ago I published [some
notes](http://www.andreagrandi.it/2010/02/17/nokia-n900-some-problems-with-latest-pr-1-1-1-firmware/)
about my personal experience with **PR 1.1.1** firmware upgrade in Nokia
**N900**. In particular my device got an infinite reboot loop after
upgrading the firmware and I had to flash the firmware image from
scratch to fix the problem. Today I was kindly contacted by **Max
Waterman** (I suppose he works for Nokia) and he explained me what was
the problem. It was caused by a little bug in Harmattan UI demo and they
fixed it (the fix is already available in extras-devel).

No surprise for me: extras-devel contains unstable packages and if user
enables it, he does at his own risk. The most important thing is the
fact that the official firmware without any unstable application doesn't
suffer of this problem at all. The thing that really impressed me so
much (in a positive sense) it's that I was contacted privately by a
Nokia developer apologizing for the bug (no problem man, it's part of
the game if someone want to test extras-devel software) and explaining
that they already fixed it.

This is what I like of Maemo (or should I already call it MeeGo?), I
really feel to be a part of it!
