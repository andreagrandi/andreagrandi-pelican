Title: How to fix encfs installation on OSX 10.9 (Mavericks) and brew
Date: 2013-11-08 21:17
Author: admin
Category: HowTo, OSX, Sicurezza
Tags: cloud, encfs, encryption, fuse4x, OSX, security
Slug: how-to-fix-encfs-installation-on-osx-10-9-mavericks-and-brew
Status: published

After upgrading from OSX 10.8.x to 10.9 (Mavericks), **encfs** recipe is
broken. First of all you have to fix a problem with a library header:

    sudo ln -s /usr/include/sys/_endian.h /usr/include/sys/endian.h

then you can install encfs using this remote brew recipe:

    brew reinstall https://gist.github.com/ghibble/7297078/raw/cae1ff000a5e1cfc670f5b7a611279ed494b63af/encfs.rb

It's also possible that you have to fix fuse4x installation before being
able to use encfs (I had to do it):

    sudo /bin/cp -rfX /usr/local/Cellar/fuse4x-kext/0.9.2/Library/Extensions/fuse4x.kext /Library/Extensions
    sudo chmod +s /Library/Extensions/fuse4x.kext/Support/load_fuse4x

That's it! Please note that this is just a workaround (thanks to
**Giovanni Bajo** for suggesting me the symlink fix). Please also note
that this recipe uses fuse4x library and not the most updated osxfuse
(but it works, anyway). Some other users reported me that there is a fix
for the original brew recipe, and this one uses osxfuse. You can find it
here <https://gist.github.com/defunctzombie/7324625> but I haven't
tested it yet.

**Update:** to fully integrate encfs with OSX, I also suggest to follow
this nice guide <http://www.maketecheasier.com/install-encfs-mac/>
