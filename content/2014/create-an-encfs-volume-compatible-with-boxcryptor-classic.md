Title: Create an EncFS volume compatible with BoxCryptor Classic
Date: 2014-09-12 15:27
Author: admin
Category: HowTo, Linux, Sicurezza
Tags: boxcryptor, dropbox, encfs
Slug: create-an-encfs-volume-compatible-with-boxcryptor-classic
Status: published

If you are planning to share an encrypted volume between Linux/OSX and
Windows (I will assume you are sharing it on Dropbox, but you could use
any similar service) and you are using
[**EncFS**](http://www.arg0.net/encfs) under Linux/OSX and
[**BoxCryptor**](https://www.boxcryptor.com) under Windows, there are
some specifig settings to use when you create the EncFS volume. Infact
even if BoxCryptor claims to be "encfs compatible", it's not 100%.

Suppose you want to create an encrypted volume located at
**\$HOME/.TestTmpEncrypted** and mounted at **\$HOME/TestTmp** you need
the following command:

    andrea-Inspiron-660:~ andrea $ encfs ~/.TestTmpEncrypted ~/TestTmp

answer "Y" when you are asked if you want to create the folders:

    The directory "/home/andrea/.TestTmpEncrypted/" does not exist. Should it be created? (y,n) y
    The directory "/home/andrea/TestTmp" does not exist. Should it be created? (y,n) y

At this point you will need to select between default paranoia mode or
advanced mode. Please choose the **advanced** one (x):

    Creating new encrypted volume.
    Please choose from one of the following options:
     enter "x" for expert configuration mode,
     enter "p" for pre-configured paranoia mode,
     anything else, or an empty line will select standard mode.
    ?> x

Manual configuration mode selected.

    Select AES as cypher algorithm:

    The following cypher algorithms are available:
    1. AES : 16 byte block cipher
    -- Supports key lengths of 128 to 256 bits
    -- Supports block sizes of 64 to 4096 bytes
    2. Blowfish : 8 byte block cypher
    -- Supports key lengths of 128 to 256 bits
    -- Supports block sizes of 64 to 4096 bytes

    Enter the number corresponding to your choice: 1

    Selected algorithm "AES"

Select **256** as key size:

    Please select a key size in bits. The cypher you have chosen
    supports sizes from 128 to 256 bits in increments of 64 bits.
    For example:
    128, 192, 256
    Selected key size: 256

    Using key size of 256 bits

Choose **1024** as block size:

    Select a block size in bytes. The cypher you have chosen
    supports sizes from 64 to 4096 bytes in increments of 16.
    Alternatively, just press enter for the default (1024 bytes)

    filesystem block size:

    Using filesystem block size of 1024 bytes

Select **Stream** as filename encoding:

    The following filename encoding algorithms are available:
    1. Block : Block encoding, hides file name size somewhat
    2. Null : No encryption of filenames
    3. Stream : Stream encoding, keeps filenames as short as possible

    Enter the number corresponding to your choice: 3

    Selected algorithm "Stream""

Do **NOT** enable **filename initialization vector chaining**:

    Enable filename initialization vector chaining?
    This makes filename encoding dependent on the complete path,
    rather then encoding each path element individually.
    The default here is Yes.
    Any response that does not begin with 'n' will mean Yes: no

Do **NOT** enable **per-file initialization vectors**:

    Enable per-file initialization vectors?
    This adds about 8 bytes per file to the storage requirements.
    It should not affect performance except possibly with applications
    which rely on block-aligned file io for performance.
    The default here is Yes.
    Any response that does not begin with 'n' will mean Yes: no

Do **NOT** enable **external chained IV**:

    External chained IV disabled, as both 'IV chaining'
    and 'unique IV' features are required for this option.
    Enable block authentication code headers
    on every block in a file? This adds about 12 bytes per block
    to the storage requirements for a file, and significantly affects
    performance but it also means [almost] any modifications or errors
    within a block will be caught and will cause a read error.
    The default here is No.
    Any response that does not begin with 'y' will mean No: no

Do **NOT** enable **random bytes to each block header**:

    Add random bytes to each block header?
    This adds a performance penalty, but ensures that blocks
    have different authentication codes. Note that you can
    have the same benefits by enabling per-file initialisation
    vectors, which does not come with as great a performance
    penalty.
    Select a number of bytes, from 0 (no random bytes) to 8: 0

Enable **file-hole pass-through**:

    Enable file-hole pass-through?
    This avoids writing encrypted blocks when file holes are created.
    The default here is Yes.
    Any response that does not begin with 'n' will mean Yes: yes

Finally you will see:

    Configuration finished. The filesystem to be created has
    the following properties:
    Filesystem cypher: "ssl/aes", version 3:0:2
    Filename encoding: "nameio/stream", version 2:1:2
    Key Size: 256 bits
    Block Size: 1024 bytes
    File holes passed through to ciphertext.

At this point set a passphrase for your new volume:

    Now you will need to enter a password for your filesystem.
    You will need to remember this password, as there is absolutely
    no recovery mechanism. However, the password can be changed
    later using encfsctl.

    New Encfs Password:
    Verify Encfs Password:

You should be able to mount this volume using BoxCryptor.
