Title: Soma.fm + Spotify + import.io + Python mashup: automatically create a Spotify playlist with Soma.fm tracks
Date: 2015-07-12 10:10
Author: admin
Category: Python
Tags: import.io, music, Python, soma.fm, spotify
Slug: soma-fm-spotify-import-io-python-mashup
Status: published

I'm a big fan of [Soma.fm](http://somafm.com) (a 25+ channels streaming
radio based in San Francisco) and during the years I've been writing
clients for this radio for different mobile platforms (Maemo, MeeGo,
Harmattan, Windows Phone, BlackBerry 10, Jolla). I love in particular
their "[**Indie Pop Rock**](http://somafm.com/indiepop/)" channel that
during these years made me discover some very good artists.

When **Spotify** finally was available in Italy (I'm still using it
right now that I live in the UK), something that I always missed was a
radio with the same good music. Why not just listening to Soma.fm?
Because I like to listen to the music while I commute and in the London
Underground it's nearly impossible to have signal.

So I was thinking: it would be nice to have **a Spotify playlist with
Soma.fm tracks**. Wait a moment.... **I can do it!**

[![Frankenstein\_Jr\_Mel\_Brooks\_1974](https://www.andreagrandi.it/wp-content/uploads/2015/07/Frankenstein_Jr_Mel_Brooks_1974.jpg){.aligncenter
.size-full .wp-image-981 width="542"
height="422"}](https://www.andreagrandi.it/wp-content/uploads/2015/07/Frankenstein_Jr_Mel_Brooks_1974.jpg)

Soma.fm publishes the tracks history with all the tracks streamed during
the last hour <http://somafm.com/indiepop/songhistory.html> so I just
needed something to parse this list for me and return me a well
formatted version.

Thanks to [**import.io**](https://import.io) (it's a service that takes
a web page as input, parse the data and generates a RESTful API to
access this data) I was able to easily get the data I needed. At this
point I only needed to be able to loop through the list, search each
track on Spotify and add it to my playlist.

The **source code is fully available** here
<https://github.com/andreagrandi/spotisoma>

**Note:** you can't just get the code and run it. You will need to get
your own **import.io api key**, generate your import.io api url, get a
[**Spotify application
key**](https://developer.spotify.com/technologies/libspotify/keys/) (the
old/deprecated one, since it was nearly impossible for me to use oauth
in a simple Python script due to the fact I didn't have an endpoint to
receive the token back. You can get more informations here:
<https://pyspotify.mopidy.com/en/latest/quickstart/#application-keys>)
and set your env variables with your Spotify username and password. Last
but not least: the **old Spotify library** only works with **Premium**
accounts.
