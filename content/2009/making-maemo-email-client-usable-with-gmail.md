Title: Making Maemo email client usable with GMail
Date: 2009-08-08 13:34
Author: admin
Category: HowTo, Igalia, Linux, Maemo (EN)
Tags: client, email, gmail, maemo, modest, recent
Slug: making-maemo-email-client-usable-with-gmail
Status: published

I must admit, I wasn't using Maemo email client, because I did find it
was simply unusable, at least with my GMail account.

I tried both POP3 and IMAP, but having about 25.000+ messages in my
account, downloading just the headers was a job that the client simply
couldn't manage.

Yesterday I knew about "**recent mode**" support in **POP3**, a
functionality that **GMail** supports too. This mode allow you to
download **only last 30 days** messages (in my case, no more than 1000) 
so the client can manage them without any problem.

All you have to do to enable this mode is put the "**recent:**" string
before the username. For example: if your username is
"username@gmail.com" you have to write "**recent:username@gmail.com**".
Important: this mode only works with POP3, not with IMAP.

To conclude, let me say **thank you** to the kind guy who let me
discover this mode. Thank you
[**Sergio**](http://blogs.igalia.com/svillar/)! Now there is another
thing I can do with my tablet!
