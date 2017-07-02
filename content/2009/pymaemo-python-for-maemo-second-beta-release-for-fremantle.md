Title: PyMaemo (Python for Maemo) second beta release for Fremantle
Date: 2009-08-10 09:20
Author: admin
Category: Igalia, Linux, Maemo (EN), Programmazione, Python
Tags: bindings, fremantle, maemo, nokia, pymaemo, Python, tablet
Slug: pymaemo-python-for-maemo-second-beta-release-for-fremantle
Status: published

The **PyMaemo** team is pleased to announce the second beta release of
PyMaemo for **Fremantle**!

This new release is available through the **extras-devel** repository,
see installation instructions in  
<http://pymaemo.garage.maemo.org/sdk_installation.html#fremantle>

What is it?
-----------

Python for Maemo (PyMaemo for short) main objective is to make possible
to use **Python** programming language as the scripting and development
language for Maemo Platform, providing a better alternative for fast
prototyping and programming in Maemo environment besides the C
programming language.

Python is for serious programming and to have fun. Python has a nice
syntax, it is easy to learn and powerful enough for a vast range of
applications, this is why we choose Python for Maemo.

What has changed?
-----------------

**New packages:**

-   **python-mafw** (0.1-1maemo1)
    -   Python bindings for the Media Application Framework \[1\]
    -   Supported API is very basic at the moment, and there are some
        bugs. Feedback is welcome!
-   **python-hildondesktop** (0.0.3-1maemo1)
    -   Python bindings for the home/status widgets API
-   **python-notify** (0.1.1-2maemo1)
    -   Python bindings for libnotify
-   **pyclutter** (0.8.0-1maemo2)
    -   Python bindings for the Clutter API \[2\]
    -   Experimental package, waiting for developer feedback

**Updated packages:**

-   **gnome-python** (2.26.1-1maemo1)
    -   major upgrade, matching current Debian testing release;
    -   feedback on this is welcome, as it replaces a fairly old version
        (2.18).
-   **pygtk** (2.12.1-6maemo7)
    -   Enable glade support.
-   **python2.5** (2.5.4-1maemo1)
    -   Updated to latest upstream 2.5.x release.
    -   add support to --install-layout=deb flag.
-   **python-central** (0.6.11.1maemo1)
    -   dependency needed by the new python-setuptools version.
-   **python-defaults** (2.5.2-3maemo3)
    -   Change PREVVER in debian/rules, avoiding old python2.5-minimal
        versions that had "/usr/bin/python" and thus conflicts with
        python-minimal.
-   **python-hildo**n (0.9.0-1maemo10)
    -   lots of bug fixes
-   **python-setuptools** (0.6c9-1maemo1)
    -   add support to --install-layout=deb flag.

**Bugs fixed:** MB\#4530 \[3\], MB\#4450 \[4\], MB\#4629 \[5\], MB\#4628
\[6\],  
MB\#4647 \[7\], MB\#4632 \[8\],  MB\#4646 \[9\],  MB\#4750 \[10\],
 MB\#4749 \[11\],  
MB\#4791 \[12\]

Known issues
------------

MB\#4782 \[13\]: osso.Context causes segmentation fault  
MB\#4821 \[14\]: Cannot create HildonTouchSelector with single text
column  
MB\#4824 \[15\]: python-mafw: source\_browsing.py example does not work  
MB\#4839 \[16\]: python-mafw: mafw.Registry lacks list\_plugins()
method  
MB\#4849 \[17\]: python-mafw: MafwPluginDescriptorPublic structure is
missing

We will not migrate to python2.6 in fremantle due to a (unresolved) bug
(MB\#4734 \[18\]), where a core SDK package explicitly conflicts with
python &gt;= 2.6, preventing any further upgrades from the 2.5.x series.

This release is supposed to be compatible with previous releases. If you
have any issues regarding building your Python application on Fremantle,
feel free to report it on the pymaemo-developers mailing list \[19\].

Acknowledgments
---------------

Thanks to everybody who helped making this release possible.

Bug reports, as always, should go to our Bugzilla \[20\]. Use the
**pymaemo-developers** mailing list for help, feedback or suggestions.

References
----------

\[1\] <https://garage.maemo.org/projects/mafw/>  
\[2\] <http://www.clutter-project.org/>  
\[3\] <https://bugs.maemo.org/show_bug.cgi?id=4530>  
\[4\] <https://bugs.maemo.org/show_bug.cgi?id=4450>  
\[5\] <https://bugs.maemo.org/show_bug.cgi?id=4629>  
\[6\] <https://bugs.maemo.org/show_bug.cgi?id=4628>  
\[7\] <https://bugs.maemo.org/show_bug.cgi?id=4647>  
\[8\] <https://bugs.maemo.org/show_bug.cgi?id=4632>  
\[9\] <https://bugs.maemo.org/show_bug.cgi?id=4646>  
\[10\] <https://bugs.maemo.org/show_bug.cgi?id=4750>  
\[11\] <https://bugs.maemo.org/show_bug.cgi?id=4749>  
\[12\] <https://bugs.maemo.org/show_bug.cgi?id=4791>  
\[13\] <https://bugs.maemo.org/show_bug.cgi?id=4782>  
\[14\] <https://bugs.maemo.org/show_bug.cgi?id=4821>  
\[15\] <https://bugs.maemo.org/show_bug.cgi?id=4824>  
\[16\] <https://bugs.maemo.org/show_bug.cgi?id=4839>  
\[17\] <https://bugs.maemo.org/show_bug.cgi?id=4849>  
\[18\] <https://bugs.maemo.org/show_bug.cgi?id=4734>  
\[19\] <https://garage.maemo.org/mailman/listinfo/pymaemo-developers>  
\[20\] <https://bugs.maemo.org/enter_bug.cgi?product=PyMaemo>

Credits
-------

This post was possible thanks to **Anderson Lizardo**, from PyMaemo
team, who posted these informations on pymaemo-developers mailing list.
