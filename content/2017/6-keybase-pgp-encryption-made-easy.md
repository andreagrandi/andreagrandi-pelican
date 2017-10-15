Title: Keybase: PGP encryption made easy
Date: 2017-10-11 22:00
Author: Andrea Grandi
Category: HowTo
Tags: GnuPG, PGP, Security, Encryption, Keybase
Slug: keybase-pgp-encryption-made-easy
Status: published

Using PGP can be quite hard, even if you have a lot of experience with computers.
By the way encryption is what gives us privacy and permits us to safely transmit information
and for this reason it should be easy to use, for everyone.

[Keybase](https://keybase.io) really makes encryption easy to use.

### PGP identity

When Keybase was launched it was mainly a wrapper for PGP commands
to encrypt and decrypt a message for a certain user, but it also introduced a very nice
chain of trust.

In Keybase it's possible to either generate a new PGP key or import an existing one
but the most important thing is being able to verify our own identity using multiple proofs.

Many of us have a personal blog, a Twitter or Facebook accounts, a GitHub account etc...
All these accounts combined together make our online identity.

Every Keybase account can be verified by other online identities. In Keybase
you don't just say "I'm Andrea Grandi, this is my PGP key...". In Keybase you
can link your existing online accounts to your Keybase account and show additional
proofs of your identity.

Unless an attacker controls all your social accounts, they cannot impersonate and verify
themselves as if they were you.

[![]({filename}/images/2017/10/keybase_identity.png){ width=100% }]({filename}/images/2017/10/keybase_identity.png)

Once you are on Keybase, other users can look for you even using your GitHub or Twitter username
without having to know your email address or Keybase username. This concept can be
very useful in some situations, we will see it later.

### Encrypted Filesystem

One of the first features launched by Keybase was their encrypted filesystem.
There is a virtual folder located at **/keybase** (on OSX/Linux or k:\keybase on Windows)
where you will find at least three other folders: **public**, **private**, **team**.

#### Public folders

Anything you place inside the /public folde can be accessed by any Keybase user and it's
automatically signed. Every user public folder/file can be accessed using their Keybase username,
like for example **/keybase/public/andreagrandi/hello.txt** but you can also use any other identity like
**/keybase/public/andreagrandi@github/hello.txt** or **/keybase/public/andreagrandi@twitter/hello.txt**

**Note:** This is very useful if you only know a person on Twitter (or GitHub etc...) and you want to
share a file with them (or send a message, as we will see later) but you don't follow each other
and you can't reach them privately.

This is a public folder example of one of the Keybase developers:

[![]({filename}/images/2017/10/keybase_chris_folder.png){ width=60% }]({filename}/images/2017/10/keybase_chris_folder.png)

You can put whatever you want in these folders: your public PGP key, your official avatar,
your Signal fingerprint etc... the other users will access these files with the assurance they
haven't been changed by anyone else in the middle.

**Note:** please keep in mind that Keybase doesn't work like Dropbox or similar. Files are not
synced between your devices and Keybase servers. Files are streamed on demand, so **you won't be able to access these files without a working Internet connection**.

#### Private folders

Hey but... where is the encryption here?! Whatever you put inside your **private**
folder can only be read by you and only you. **Not even Keybase employees can access the content of your files**,
because they are encrypted before leaving your devices and decrypted on demand
when you want to access them.

Do you want to share files with **anotheruser**? No problem. Just create a file inside **/keybase/private/andreagrandi,anotheruser**
(the folder **andreagrandi,anotheruser** will implicitely exist already) and that file will only be readable by you and **anotheruser**.

#### Security and other information

Keybase employes only have access to: 1) your top level folder names (like: "andreagrandi,anotheruser"),
2) when and for how long you are reading/writing, 3) how much space you are using.

They won't be able to access the content of your files and not even the files or folders names.

Every user initially had 10GB quota available, but a few hints (including one of their [recent screenshots]({filename}/images/2017/10/teams-splash-announcement.png))
say that now **users have 250GB available** to store their files.

You can find more technical information about Keybase encrypted folders in this article: <https://keybase.io/docs/kbfs>

### Encrypted Chat

...
