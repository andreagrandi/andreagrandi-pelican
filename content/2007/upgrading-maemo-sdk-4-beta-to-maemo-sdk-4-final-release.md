Title: Upgrading Maemo SDK 4 Beta to Maemo SDK 4 final release
Date: 2007-11-11 16:22
Author: admin
Category: HowTo, Linux, Maemo (EN), Programmazione
Tags: maemo, SDK
Slug: upgrading-maemo-sdk-4-beta-to-maemo-sdk-4-final-release
Status: published

The final version of [Maemo SDK
4](http://maemo.org/development/sdks/maemo_4_0_chinook_sdk.html) is out.
Like most other people I couldn't wait for the final release and I
installed the beta version. The big question, when I did read about the
final version was "how can I upgrade to the final version without
installing it from scratch?!". Luckly one kind person helped me on
maemo-developer mailing list, and suggested me to do a dist-upgrade from
inside the Scratchbox environment. So, login into tour Scratchbox
environment and execute this:

`[sbox-SDK_BETA_X86: ~] > fakeroot apt-get update [sbox-SDK_BETA_X86: ~] > fakeroot apt-get dist-upgrade`

[[[That's all! I don't know if this is the official method to do the
upgrade, but it worked for me. I checked, after the upgrade, if I had
the right packages installed, using this page:
<http://tablets-dev.nokia.com/4.0/4.0b_vs_4.0_content_comparison.html>  
and they were
right.]{style="font-family: georgia;"}]{style="font-family: arial;"}]{style="font-family: verdana;"}</span>
