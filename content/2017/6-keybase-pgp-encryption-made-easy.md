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

A few months ago Keybase introduced the encrypted chat. Messages between users
are **end to end encrypted** and cannot be read by anyone else, not even having access to Keybase
servers.

[![]({filename}/images/2017/10/keybase_chat.png){ width=100% }]({filename}/images/2017/10/keybase_chat.png)

#### A better address book

When we use services like WhatsApp or Signal, we are forced to share our telephone number if we want
the other person to be able to contact us.

On Keybase I don't need to share my telephone number. Anyone can reach me using one of my online
identities: **andreagrandi@twitter**, **andreagrandi@github** etc...

You can even send a message to a person who is **not on Keybase yet**: if you send a message to
randomuser@twitter, when randomuser joins Keybase and verify their Twitter account, the message
will be encrypted for them and will be safely delivered.

#### Security

Keybase doesn't use PGP to encrypt chat or files. Transmitting the key across all devices
wouldn't be safe so each message is encrypted using the public key of every device connected
to the account.

#### Command line

Keybase works from the command line too. There is no need to use the graphic
client to send a message to another user, you can do something like this:

    :::shell
    keybase chat send andreagrandi "Hello mate!"

You can integrate messages in any script and it's even available a JSON API:

    :::shell
    keybase chat help api

For more details you can have a look a this blog post on their website: <https://keybase.io/blog/keybase-chat>

### Teams

Keybase has recently introduced Teams feature. The Chat becomes more similar to Slack, but with the difference that
only team members can read the content of messages and files: the server only knows about team names and users, nobody else can
access the content.

[![]({filename}/images/2017/10/teams-splash-announcement.png){ width=100% }]({filename}/images/2017/10/teams-splash-announcement.png)

It's important to mention that in Keybase there aren't private channels like there are in Slack: if a team wants to have
channels accessible only from a restricted group of users, the admin needs to create a sub team. For example if you have a
team called **keybaselovers** you can create a sub team for admins only called **keybaselovers.admins**

Teams have a dedicated encrypter folder that you will find under **/keybase/team/keybaselovers**

At the moment the features available from the UI are quite limited and are only available from the command line. In the next
weeks these features will be available from the UI too. In the mean time you can have a look ad the commandline help:

    :::shell
    keybase team --help # for admin'ing teams
    keybase chat --help # for admin'ing chat channels

#### Create a Team

    :::shell
    keybase team create keybaselovers

#### Add a user to a Team

    :::shell
    keybase team add-member keybaselovers --user=alice --role=writer

For more information you can have a look at the official announcement page: <https://keybase.io/blog/introducing-keybase-teams>
