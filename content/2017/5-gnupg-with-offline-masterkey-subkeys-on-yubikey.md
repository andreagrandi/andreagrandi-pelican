Title: Configuring an offline GnuPG master key and subkeys on YubiKey
Date: 2017-09-30 14:00
Author: Andrea Grandi
Category: HowTo
Tags: GnuPG, PGP, Security, YubiKey, Encryption
Slug: configuring-offline-gnupg-masterkey-subkeys-on-yubikey
Status: published

I've recently bought a [YubiKey 4](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605) and 
decided to use it for GnuPG too, other than using it as hardware 2FA.

I've also decided to make my GnuPG configuration much more safe, generating the **master key**
on an **offline** computer (in my case a simple RaspberryPi not connected to Internet) and **generating a subkey**
that will be moved to my [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605).

#### Disclaimer

Always think about what your **threat model** is before deciding something is 100% safe for you.
I'm not claiming this setup/configuration is bullet proof. If you want to protect your GnuPG key from most of the hackers,
keyloggers and if you want to use it on different computers without ever compromising your secret key, this setup
can be what you are looking for. If you think you may be victim of a targeted state sponsored attack, I'm not sure this
setup could be enough.

#### Why keeping offline the master key?

If you only use your master key on a computer that never connects to Internet (I reckon you will want to update/patch it
from time to time, that's why we are going to keep the master key on an external USB key) you are at least safe from remote attacks.

#### Why using subkeys?

Your GnuPG master key is also your "identity" among every PGP user. If you loose your master key or if your key is compromised
you need to rebuild your identity and reputation from scratch. Instead, if a subkey is compromised, you can revoke the subkey (using your
master key) and generate a new subkey.

#### How a YubiKey makes things safer?

If you always use your subkey from a [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605), it's very unlikely that your
private key can be stolen: it's impossible to read it from the [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605) and if you loose your YubiKey
or if it's physically stolen, the attacker will still need your passphrase and your YubiKey PIN.

### Requirements

- 1 [YubiKey 4](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605)
- 2 USB keys (in theory you only need one, but I strongly suggest you have another one as backup)
- 1 offline computer (a simple RaspberryPi with no Internet connection will be fine)

### Initial setup

From now on, I will assume that you have prepared a computer for offline use (in my case I'm using a RaspberryPi 2 with
Raspbian) and you will type the next commands there and only there.

Plug one of the **USB key** (you can format it with VFAT for simplicity) in the offline computer and wait for the system to mount it.
At this point it should be mounted in a path like this: **/media/AABB-BAAC**

Now set the GnuPG working directory and create it:

    :::text
    user@debian:~$ export GNUPGHOME=/media/AABB-BAAC/gnupghome
    user@debian:~$ mkdir $GNUPGHOME

#### Second disclaimer

If you think your threat model doesn't include someone can hack your computer from remote,
you can ignore my advice and type these commands on your main laptop (at your own risk).

#### Note

For my own convenience, to write this tutorial I reproduced all these steps on my MacBook because it was easier to copy/paste
commands and outputs but I've tested it with the exact setup I'm describing, and it
should be compatible with OSX and Linux.
When you see something has been masked it's just to hide (from spam) things like my email or to protect the serial number
of my [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605). Last but not least, the output shown here could not match exactly the one you get on your own PC and this also
depends on the GnuPG version you are using.

### Generating the master key

The master key must be generated using the advanced mode, because by default when a new master key is generated, also a new subkey
is created with all the capabilities (Authentication + Signing + Encryption), while we want something different.

**Note:** PGP keys up to **4096 bits** are only supported in **YubiKey 4** models. If you have a **YubiKey NEO** you must use
a **2048 bits** key because it's the maximum size supported. Here you will create a PGP key with **only
the Authentication capability**. If your GnuPG version doesn't allow this, choose "sign only", just don't
create the encryption capability at this time.

    :::text
    user@debian:~$ gpg --expert --gen-key
    gpg (GnuPG) 2.0.30; Copyright (C) 2015 Free Software Foundation, Inc.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    gpg: directory `/media/AABB-BAAC/gnupghome' created
    gpg: new configuration file `/media/AABB-BAAC/gnupghome/gpg.conf' created
    gpg: WARNING: options in `/media/AABB-BAAC/gnupghome/gpg.conf' are not yet active during this run
    gpg: keyring `/media/AABB-BAAC/gnupghome/secring.gpg' created
    gpg: keyring `/media/AABB-BAAC/gnupghome/pubring.gpg' created
    Please select what kind of key you want:
    (1) RSA and RSA (default)
    (2) DSA and Elgamal
    (3) DSA (sign only)
    (4) RSA (sign only)
    (7) DSA (set your own capabilities)
    (8) RSA (set your own capabilities)
    Your selection? 8

    Possible actions for a RSA key: Sign Certify Encrypt Authenticate
    Current allowed actions: Sign Certify Encrypt

    (S) Toggle the sign capability
    (E) Toggle the encrypt capability
    (A) Toggle the authenticate capability
    (Q) Finished

    Your selection? s

    Possible actions for a RSA key: Sign Certify Encrypt Authenticate
    Current allowed actions: Certify Encrypt

    (S) Toggle the sign capability
    (E) Toggle the encrypt capability
    (A) Toggle the authenticate capability
    (Q) Finished

    Your selection? e

    Possible actions for a RSA key: Sign Certify Encrypt Authenticate
    Current allowed actions: Certify

    (S) Toggle the sign capability
    (E) Toggle the encrypt capability
    (A) Toggle the authenticate capability
    (Q) Finished

    Your selection? q
    RSA keys may be between 1024 and 4096 bits long.
    What keysize do you want? (2048) 4096
    Requested keysize is 4096 bits
    Please specify how long the key should be valid.
            0 = key does not expire
        <n>  = key expires in n days
        <n>w = key expires in n weeks
        <n>m = key expires in n months
        <n>y = key expires in n years
    Key is valid for? (0) 2y
    Key expires at Wed 25 Sep 18:39:49 2019 BST
    Is this correct? (y/N) y

    GnuPG needs to construct a user ID to identify your key.

    Real name: Andrea Grandi
    Email address: user@email.com
    Comment:
    You selected this USER-ID:
        "Andrea Grandi <user@email.com>"

    Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o
    You need a Passphrase to protect your secret key.

    We need to generate a lot of random bytes. It is a good idea to perform
    some other action (type on the keyboard, move the mouse, utilize the
    disks) during the prime generation; this gives the random number
    generator a better chance to gain enough entropy.
    gpg: /media/AABB-BAAC/gnupghome/trustdb.gpg: trustdb created
    gpg: key 2240402E marked as ultimately trusted
    public and secret key created and signed.

    gpg: checking the trustdb
    gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
    gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
    gpg: next trustdb check due at 2019-09-25
    pub   4096R/2240402E 2017-09-25 [expires: 2019-09-25]
        Key fingerprint = 7D4C 4090 DB50 1693 4614  F6FC 6206 9DE9 2240 402E
    uid       [ultimate] Andrea Grandi <user@email.com>

**Note:** please remember to save your passphrase in a safe place. Choose something you
can remember because you will need it every time you need to sign, encrypt or decrypt something.

### Creating a revocation certificate

It's very important to create a revocation certificate to be used if and when 
in the future you want to change your master key and revoke the existing one:

    :::text
    user@debian:~$ gpg --gen-revoke 2240402E > 2240402E-revocation-certificate.asc

    sec  4096R/2240402E 2017-09-25 Andrea Grandi <user@email.com>

    Create a revocation certificate for this key? (y/N) y
    Please select the reason for the revocation:
    0 = No reason specified
    1 = Key has been compromised
    2 = Key is superseded
    3 = Key is no longer used
    Q = Cancel
    (Probably you want to select 1 here)
    Your decision? 3
    Enter an optional description; end it with an empty line:
    >
    Reason for revocation: Key is no longer used
    (No description given)
    Is this okay? (y/N) y

    You need a passphrase to unlock the secret key for
    user: "Andrea Grandi <user@email.com>"
    4096-bit RSA key, ID 2240402E, created 2017-09-25

    ASCII armored output forced.
    Revocation certificate created.

    Please move it to a medium which you can hide away; if Mallory gets
    access to this certificate he can use it to make your key unusable.
    It is smart to print this certificate and store it away, just in case
    your media become unreadable.  But have some caution:  The print system of
    your machine might store the data and make it available to others!

### Creating Encryption subkey

To create a subkey we need to edit the existing key (please note that **2240402E**
is the last 8 chars from the fingerprint of the previously generated master key)
and specify we want to create an Encryption only key.

    :::text
    user@debian:~$ gpg --edit-key 2240402E
    gpg (GnuPG) 2.0.30; Copyright (C) 2015 Free Software Foundation, Inc.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Secret key is available.

    pub  4096R/2240402E  created: 2017-09-25  expires: 2019-09-25  usage: C
                        trust: ultimate      validity: ultimate
    [ultimate] (1). Andrea Grandi <user@email.com>

    gpg> addkey
    Key is protected.

    You need a passphrase to unlock the secret key for
    user: "Andrea Grandi <user@email.com>"
    4096-bit RSA key, ID 2240402E, created 2017-09-25

    Please select what kind of key you want:
    (3) DSA (sign only)
    (4) RSA (sign only)
    (5) Elgamal (encrypt only)
    (6) RSA (encrypt only)
    Your selection? 6
    RSA keys may be between 1024 and 4096 bits long.
    What keysize do you want? (2048) 4096
    Requested keysize is 4096 bits
    Please specify how long the key should be valid.
            0 = key does not expire
        <n>  = key expires in n days
        <n>w = key expires in n weeks
        <n>m = key expires in n months
        <n>y = key expires in n years
    Key is valid for? (0) 2y
    Key expires at Wed 25 Sep 18:47:21 2019 BST
    Is this correct? (y/N) y
    Really create? (y/N) y
    We need to generate a lot of random bytes. It is a good idea to perform
    some other action (type on the keyboard, move the mouse, utilize the
    disks) during the prime generation; this gives the random number
    generator a better chance to gain enough entropy.

    pub  4096R/2240402E  created: 2017-09-25  expires: 2019-09-25  usage: C
                        trust: ultimate      validity: ultimate
    sub  4096R/01731555  created: 2017-09-25  expires: 2019-09-25  usage: E
    [ultimate] (1). Andrea Grandi <user@email.com>

    gpg> save

### Export a backup of the secret keys

It's very important to export a backup of the secret keys at this point.
Writing the secret subkey to the [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605) is a destructive process: keys are moved
to the [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605), they are not copied.

    :::text
    user@debian:~$ gpg --export-secret-key 2240402E > 2240402E-secret.pgp

**Note:** this backup includes both the secret master key and the secret subkey.
Please remember to **save a backup of this key** on a couple of separate USB keys: you will need
this keys to generate future subkeys and/or to revoke the existing ones.

###  Programming the YubiKey with all GnuPG keys

We have previously created the **master key** and the **encryption subkey**. Now we will
create the **authentication** and **signing** keys directly on the [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605) (we don't
need to have a copy of these keys) and we will move the secret encryption key
to the [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605).

    :::text
    user@debian:~$ gpg --edit-key 2240402E
    gpg (GnuPG) 2.0.30; Copyright (C) 2015 Free Software Foundation, Inc.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Secret key is available.

    pub  4096R/2240402E  created: 2017-09-25  expires: 2019-09-25  usage: C
                        trust: ultimate      validity: ultimate
    sub  4096R/01731555  created: 2017-09-25  expires: 2019-09-25  usage: E
    [ultimate] (1). Andrea Grandi <user@email.com>

    gpg> addcardkey
    Signature key ....: [none]
    Encryption key....: [none]
    Authentication key: [none]

    Please select the type of key to generate:
    (1) Signature key
    (2) Encryption key
    (3) Authentication key
    Your selection? 1

    What keysize do you want for the Signature key? (4096)
    Key is protected.

    You need a passphrase to unlock the secret key for
    user: "Andrea Grandi <user@email.com>"
    4096-bit RSA key, ID 2240402E, created 2017-09-25

    Please specify how long the key should be valid.
            0 = key does not expire
        <n>  = key expires in n days
        <n>w = key expires in n weeks
        <n>m = key expires in n months
        <n>y = key expires in n years
    Key is valid for? (0) 2y
    Key expires at Wed 25 Sep 18:50:42 2019 BST
    Is this correct? (y/N) y
    Really create? (y/N) y

    pub  4096R/2240402E  created: 2017-09-25  expires: 2019-09-25  usage: C
                        trust: ultimate      validity: ultimate
    sub  4096R/01731555  created: 2017-09-25  expires: 2019-09-25  usage: E
    sub  4096R/771B0554  created: 2017-09-25  expires: 2019-09-25  usage: S
    [ultimate] (1). Andrea Grandi <user@email.com>

    gpg> addcardkey
    Signature key ....: 6FAB DC46 1847 3550 3769  2D32 0DE1 36B4 771B 0554
    Encryption key....: [none]
    Authentication key: [none]

    Please select the type of key to generate:
    (1) Signature key
    (2) Encryption key
    (3) Authentication key
    Your selection? 3

    What keysize do you want for the Authentication key? (4096)
    Key is protected.

    You need a passphrase to unlock the secret key for
    user: "Andrea Grandi <user@email.com>"
    4096-bit RSA key, ID 2240402E, created 2017-09-25

    Please specify how long the key should be valid.
            0 = key does not expire
        <n>  = key expires in n days
        <n>w = key expires in n weeks
        <n>m = key expires in n months
        <n>y = key expires in n years
    Key is valid for? (0) 2y
    Key expires at Wed 25 Sep 18:54:51 2019 BST
    Is this correct? (y/N) y
    Really create? (y/N) y

    pub  4096R/2240402E  created: 2017-09-25  expires: 2019-09-25  usage: C
                        trust: ultimate      validity: ultimate
    sub  4096R/01731555  created: 2017-09-25  expires: 2019-09-25  usage: E
    sub  4096R/771B0554  created: 2017-09-25  expires: 2019-09-25  usage: S
    sub  4096R/A9B5334C  created: 2017-09-25  expires: 2019-09-25  usage: A
    [ultimate] (1). Andrea Grandi <user@email.com>

    gpg> toggle

    sec  4096R/2240402E  created: 2017-09-25  expires: 2019-09-25
    ssb  4096R/01731555  created: 2017-09-25  expires: never
    ssb  4096R/771B0554  created: 2017-09-25  expires: 2019-09-25
                        card-no: 0006 05672181
    ssb  4096R/A9B5334C  created: 2017-09-25  expires: 2019-09-25
                        card-no: 0006 05672181
    (1)  Andrea Grandi <user@email.com>

    gpg> key 1

    sec  4096R/2240402E  created: 2017-09-25  expires: 2019-09-25
    ssb* 4096R/01731555  created: 2017-09-25  expires: never
    ssb  4096R/771B0554  created: 2017-09-25  expires: 2019-09-25
                        card-no: 0006 05672181
    ssb  4096R/A9B5334C  created: 2017-09-25  expires: 2019-09-25
                        card-no: 0006 05672181
    (1)  Andrea Grandi <user@email.com>

    gpg> keytocard
    Signature key ....: 6FAB DC46 1847 3550 3769  2D32 0DE1 36B4 771B 0554
    Encryption key....: [none]
    Authentication key: BD26 3AD8 985E CAB0 9F32  7307 DF7C F7C0 A9B5 334C

    Please select where to store the key:
    (2) Encryption key
    Your selection? 2

    You need a passphrase to unlock the secret key for
    user: "Andrea Grandi <user@email.com>"
    4096-bit RSA key, ID 01731555, created 2017-09-25


    sec  4096R/2240402E  created: 2017-09-25  expires: 2019-09-25
    ssb* 4096R/01731555  created: 2017-09-25  expires: never
                        card-no: 0006 05672181
    ssb  4096R/771B0554  created: 2017-09-25  expires: 2019-09-25
                        card-no: 0006 05672181
    ssb  4096R/A9B5334C  created: 2017-09-25  expires: 2019-09-25
                        card-no: 0006 05672181
    (1)  Andrea Grandi <user@email.com>

    gpg> save

#### Check public keys

Just to verify everything has been created correctly, we check the public keys.
We should see one **pub** key and three **sub**:

    :::text
    user@debian:~$ gpg -k
    /media/AABB-BAAC/gnupghome/pubring.gpg
    --------------------------------
    pub   4096R/2240402E 2017-09-25 [expires: 2019-09-25]
    uid       [ultimate] Andrea Grandi <user@email.com>
    sub   4096R/01731555 2017-09-25 [expires: 2019-09-25]
    sub   4096R/771B0554 2017-09-25 [expires: 2019-09-25]
    sub   4096R/A9B5334C 2017-09-25 [expires: 2019-09-25]

#### Check private keys

When we check the private keys we should see that one key is still local, marked as **sec** (it's
the private key of the master key), while three other keys are marked as **ssb>**
which means they have been moved to the [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605):

    :::text
    user@debian:~$ gpg -K
    /media/AABB-BAAC/gnupghome/secring.gpg
    --------------------------------
    sec   4096R/2240402E 2017-09-25 [expires: 2019-09-25]
    uid                  Andrea Grandi <user@email.com>
    ssb>  4096R/01731555 2017-09-25
    ssb>  4096R/771B0554 2017-09-25
    ssb>  4096R/A9B5334C 2017-09-25

#### Import back secret keys from backup (only for multiple YubiKeys)

As previously said, when we write the encryption subkey to the [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605), the key
is **moved** and not just copied, so we need to import back the secret key into
the keyring. It's important to have a backup of the subkey too, not because we need it
in case the key is compromised etc... but because we need it in case we want to write
multiple YubiKeys with the same encryption key, so that we have a backup key to use.

    :::text
    user@debian:~$ gpg --import < 2240402E-secret.pgp

#### Completely remove secret keys from laptop

Once you have programmed the [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605) and you are sure the secret keys are
backed up on a couple of USB keys, you are ready to remove the secret keys from your laptop.

**Note:** you don't need to remove anything if you have conducted the whole setup
on a spare offline PC (or on a RaspberryPi) because that's not your every day computer.

    :::text
    user@debian:~$ gpg --delete-secret-key 2240402E

### Exporting the public PGP key

As you know, PGP keys are composed by a secret part and a public one. The public one
must be distributed publicly and it's the one people will use to encrypt messages directed
to you.

    :::text
    user@debian:~$ gpg --armor --export 2240402E > 2240402E.asc

If you have a personal blog/website I suggest to upload it there (for example mine
can be found here <https://www.andreagrandi.it/2240402E.asc>)

### Change YubiKey PINs and complete configuration

Every [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605) is sold with a certain default configuration: there is a **user PIN**
that is required every time we need to use the key to sign/decrypt something (in addition
to our passphrase) and there is an **admin PIN** that is required every time we change
certain settings on the [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605).

The default values are:

- user PIN: 123456
- admin PIN: 12345678

I strongly recommend you to change them following this example:

    :::text
    user@debian:~$ gpg --card-edit

    Reader ...........: Yubico Yubikey 4 OTP U2F CCID
    Application ID ...: D000000000000000000000000000000000
    Version ..........: 2.1
    Manufacturer .....: Yubico
    Serial number ....: 012345678
    Name of cardholder: [not set]
    Language prefs ...: [not set]
    Sex ..............: unspecified
    URL of public key : [not set]
    Login data .......: [not set]
    Signature PIN ....: not forced
    Key attributes ...: rsa4096 rsa4096 rsa4096
    Max. PIN lengths .: 127 127 127
    PIN retry counter : 3 0 3
    Signature counter : 3
    Signature key ....: 6FAB DC46 1847 3550 3769  2D32 0DE1 36B4 771B 0554
        created ....: 2017-09-25 17:50:37
    Encryption key....: FC6F 40BC 4173 8D13 2D7C  E958 BCDC EA84 0173 1555
        created ....: 2017-09-25 17:47:09
    Authentication key: BD26 3AD8 985E CAB0 9F32  7307 DF7C F7C0 A9B5 334C
        created ....: 2017-09-25 17:54:49
    General key info..: sub  rsa4096/0DE136B4771B0554 2017-09-25 Andrea Grandi <user@email.com>
    sec#  rsa4096/62069DE92240402E  created: 2017-09-25  expires: 2019-09-25
    ssb>  rsa4096/BCDCEA8401731555  created: 2017-09-25  expires: 2019-09-25
                                    card-no: 0006 05672181
    ssb>  rsa4096/0DE136B4771B0554  created: 2017-09-25  expires: 2019-09-25
                                    card-no: 0006 05672181
    ssb>  rsa4096/DF7CF7C0A9B5334C  created: 2017-09-25  expires: 2019-09-25
                                    card-no: 0006 05672181

    gpg/card> admin
    Admin commands are allowed

    # Change the PIN and Admin PINs
    gpg/card> passwd
    gpg: OpenPGP card no. D000000000000000000000000000000000 detected

    1 - change PIN
    2 - unblock PIN
    3 - change Admin PIN
    4 - set the Reset Code
    Q - quit

    Your selection? 1
    PIN changed.     

    1 - change PIN
    2 - unblock PIN
    3 - change Admin PIN
    4 - set the Reset Code
    Q - quit

    Your selection? 3
    PIN changed.     

    1 - change PIN
    2 - unblock PIN
    3 - change Admin PIN
    4 - set the Reset Code
    Q - quit

    Your selection? q

    # Make sure the PIN is entered before signing
    gpg/card> forcesig

    # Set the URL where the OpenPGP public key can be found.
    gpg/card> url
    URL to retrieve public key: https://www.andreagrandi.it/2240402E.asc

    # Fetch the public key into the local keyring
    gpg/card> fetch
                                                            
    gpg/card> quit

**Note:** when you want to use your [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605) on any computer (for example your work laptop)
you need to at least import your public PGP key into the keyring. If the key is not
read automatically, you may need to give it a refresh using this command:

    :::shell
    user@debian:~$ gpg --card-status

#### Careful with PINs

Please remember that you can only digit a wrong user PIN for a maximum of three times.
After three time you will need to edit the [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605) (with **gpg --card-edit**) become admin
and use the **unblock PIN** option. If you digit the wrong admin PIN for three time, you will have
to follow a quite complicated procedure (explained at this address: <https://developers.yubico.com/ykneo-openpgp/ResetApplet.html>)
and your [YubiKey](https://www.amazon.co.uk/Yubico-Y-158-YubiKey-4-Black/dp/B018Y1Q71M/ref=as_li_ss_tl?ie=UTF8&qid=1507054059&sr=8-1&keywords=yubico+4&linkCode=ll1&tag=andreagrandi-21&linkId=6da97357c6fe86ca94df918c172f6605) will be reset with factory settings, deleting your PGP keys from it.

### References

To write this tutorial I originally followed other articles online. The main ones are:

- <https://www.esev.com/blog/post/2015-01-pgp-ssh-key-on-yubikey-neo/>
- <https://blog.josefsson.org/2014/06/23/offline-gnupg-master-key-and-subkeys-on-yubikey-neo-smartcard/>
- <https://wiki.debian.org/Subkeys>
- <https://www.paulfurley.com/gpg-for-humans-preparing-an-offline-machine/>
- <https://spin.atomicobject.com/2013/11/24/secure-gpg-keys-guide/>
- <https://rnorth.org/gpg-and-ssh-with-yubikey-for-mac>
