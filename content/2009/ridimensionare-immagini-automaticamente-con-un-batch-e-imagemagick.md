Title: Ridimensionare immagini automaticamente con un batch e ImageMagick
Date: 2009-07-05 17:56
Author: admin
Category: HowTo, Linux
Tags: batch, foto, fotoritocco, image, imagemagick, immagini, magick, ridimensionare, script
Slug: ridimensionare-immagini-automaticamente-con-un-batch-e-imagemagick
Status: published

Spesso capita di dover compiere azioni noiose e ripetitive su delle
immagini, come ad esempio ridimensionarle o salvarle in formati diversi
da quello originale. Queste operazioni possono richiedere moltissimo
tempo, soprattutto se abbiamo a che fare con una grande quantità di
immagini.

Per chi usa **Linux** è disponibile però l'utility **ImageMagick**, che
unita ad un pizzico di script in **bash** ci permette di risolvere
agevolmente il problema.

Per prima cosa è necessario installare il tool sulla propria
distribuzione. Su **Ubuntu** (o in qualsiasi altra distribuzione basata
su Debian) procedere nella seguente maniera:

`sudo apt-get install imagemagick`

A questo punto basta posizionarsi nella cartella dove si trovano le
immagini (vi consiglio di crearvi una copia a parte delle immagini da
modificare, visto che lo script andra' a lavorare direttamente su quelle
originali) ed eseguire un comando come questo:

`find ./ -iname '*.JPG' -exec convert '{}' -resize '1024' '{}' \;`

Questo comando convertirà tutte le immagini .JPG che trova in un formato
di 1024 pixel di larghezza, mantenendo ovviamente le proporzioni
dell'immagine originale.
