Title: Alternative way to generate .deb packages for Maemo
Date: 2007-11-20 15:46
Author: admin
Category: HowTo, Linux, Maemo (EN), Programmazione, Ubuntu (EN)
Tags: debian, maemo, nokia, package
Slug: alternative-way-to-generate-deb-packages-for-maemo
Status: published

Thanks to [Mohammed Hassan]{style="font-weight: bold;"} now I know an
alternative (alternative to the [official
howto](http://maemo.org/development/documentation/how-tos/4-x/creating_a_debian_package.html))
way to generate a [.deb]{style="font-weight: bold;"} package for Maemo.

If the package already exist in the Debian repositories, you can get the
.dsc file (for example in an ftp like this:
<http://ftp.debian.org/debian/pool/non-free/s/spim/> ) and execute the
following commands:

`dget -x DSC_FILE_URL`

It will download the package and will unpack it in the current folder.
You have to enter in the created folder and edit the debian/\* files to
personalize settings, mantainer data, add deps ecc...

When you're done, you can generate the package with the usual command:

`dpkg-buildpackage -rfakeroot`
