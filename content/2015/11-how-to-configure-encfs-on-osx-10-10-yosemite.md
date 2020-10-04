Title: How to configure EncFS on OSX 10.10 (Yosemite)
Date: 2015-10-11 19:44
Author: admin
Category: HowTo, OSX, Sicurezza
Tags: cloud, encfs, encryption, OSX, security
Slug: how-to-configure-encfs-on-osx-10-10-yosemite
Status: published

With **EncFS** it's possible to keep our data in almost any cloud
(Dropbox, OneDrive, etc...), having a good level of privacy and
security. Infact EncFS encrypt and decrypt our data automatically. It's
available for Linux as well and using a commercial solution (that is
currently unsupported) even on Windows.

Installing EncFS
----------------

EncFS can be installed from **brew**. If you don't have brew package
manager installed on OSX you can install it using this command:

``` {.lang:sh .decode:true}
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

After brew, you need to install **OSXFuse** from this
website <http://osxfuse.github.io>

Finally you can install **encfs** using this command:

``` {.lang:sh .decode:true}
brew install homebrew/fuse/encfs
```

Configuring the encrypted folder
--------------------------------

Now that EncFS is installed, you can either mount an existing EncFS
volume or create a new one. In both cases the command is the same:

``` {.lang:sh .decode:true}
encfs ~/Dropbox/Private ~/Private
```

If you are mounting an existing encrypted volume, you will be prompted
for the password. If you are creating a new encrypted volume you will be
asked some questions about EncFS parameters.

**Note:** if it's important for you to keep compatibility with
**[BoxCryptor Classic](https://www.boxcryptor.com/en/classic)** (in case
you want to use the same volume under Windows), please refer to this
other article I
wrote: <https://www.andreagrandi.it/2014/09/12/create-an-encfs-volume-compatible-with-boxcryptor-classic/>

Mount the encrypted volume on startup
-------------------------------------

First of all you need to save the volume's password inside the OSX
keychain. Open the app **Keychain Access** and create a new entry with
name **encfs** and account value **encfs**, then write your **password**
and click **Add**:

[![encfs\_keychain\_access](https://www.andreagrandi.it/wp-content/uploads/2015/10/encfs_keychain_access.png){.aligncenter
.size-full .wp-image-1052 width="428"
height="397"}](https://www.andreagrandi.it/wp-content/uploads/2015/10/encfs_keychain_access.png)

Once the password is saved, **open a text editor** and paste this script
and save it as **encfs\_mount.sh** inside your **\$HOME** folder:

``` {.lang:sh .decode:true}
#!/bin/bash
# Secure EncFS Dropbox mounter by Daniel Widerin <daniel@widerin.net>

SOURCE=~/Dropbox/Private
TARGET=~/Private
VOLUME_TITLE=Private
KEYCHAIN_PASSWORD='encfs'
ENCFS=/usr/local/bin/encfs

mount | grep $TARGET >/dev/null
[[ "$?" -eq "0" ]] && /usr/sbin/diskutil unmount $TARGET

if [ ! -d $TARGET ]; then
 echo "Create new mountpoint $TARGET"
 mkdir $TARGET
 chmod 0700 $TARGET
fi

$ENCFS $SOURCE $TARGET --extpass="security 2>&1 >/dev/null find-generic-password -gl '$KEYCHAIN_PASSWORD' |grep password|cut -d \\\" -f 2" -ovolname=$VOLUME_TITLE
```

Make it **executable**:

``` {.lang:sh .decode:true}
chmod +x ~/encfs_mount.sh
```

Open **AppleScript** editor and paste this text inside and save as an
app in the \$HOME folder:

[![Screenshot 2015-10-11
19.27.14](https://www.andreagrandi.it/wp-content/uploads/2015/10/Screenshot-2015-10-11-19.27.14.png){.aligncenter
.size-full .wp-image-1055 width="484"
height="392"}](https://www.andreagrandi.it/wp-content/uploads/2015/10/Screenshot-2015-10-11-19.27.14.png)

``` {.lang:sh .decode:true}
do shell script "$HOME/encfs_mount.sh"
```

Finally, open "**System Preferences**" -&gt; "**Users & Groups**" and
add the previously saved application.

[![Screenshot 2015-10-11
19.27.44](https://www.andreagrandi.it/wp-content/uploads/2015/10/Screenshot-2015-10-11-19.27.44.png){.aligncenter
.size-full .wp-image-1056 width="463"
height="380"}](https://www.andreagrandi.it/wp-content/uploads/2015/10/Screenshot-2015-10-11-19.27.44.png)

Final notes
-----------

At this point encfs is configured to be mounted at startup and to save
the encrypted files inside Dropbox. Please note: **do not save anything
directly on \~/Dropbox/Private**, only read and save your files from
\~/Private

References
----------

-   <https://www.maketecheasier.com/install-encfs-mac/>
-   <http://ninjatips.com/encrypt-dropbox-using-encfs/>

