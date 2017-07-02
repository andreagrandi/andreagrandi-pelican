Title: Convertire i file WMA in MP3 sotto Linux
Date: 2009-02-22 22:43
Author: admin
Category: HowTo, Linux, Programmazione
Tags: conversione, mp3, wma
Slug: convertire-i-file-wma-in-mp3-sotto-linux
Status: published

Se abbiamo dei file audio in formato **.wma** e li vogliamo convertire
in formato **.mp3** utilizzando Linux, è sufficiente creare un piccolo
script in **bash** che facendo uso di **mplayer** e **lame** provveda a
convertire tutti i file che si trovano all'interno di una certa
directory.

Creiamo un file chiamato **wma2mp3.sh** con all'interno il seguente
script:

`#!/bin/bash`

current\_directory=\$( pwd )

\#remove spaces  
for i in \*.wma; do mv "\$i" \`echo \$i | tr ' ' '\_'\`; done

\#remove uppercase  
for i in \*.\[Ww\]\[Mm\]\[Aa\]; do mv "\$i" \`echo \$i | tr '\[A-Z\]'
'\[a-z\]'\`; done

\#Rip with Mplayer / encode with LAME  
for i in \*.wma ; do mplayer -vo null -vc dummy -af resample=44100 -ao
pcm:waveheader \$i && lame -m s audiodump.wav -o \$i; done

\#convert file names  
for i in \*.wma; do mv "\$i" "\`basename "\$i" .wma\`.mp3"; done

rm audiodump.wav  
</code>

a questo punto basta mettere lo script nella cartella dove ci sono i
file .wma, dare i permessi di esecuzione a tale file (**chmod +x
wma2mp3.sh**) ed eseguirlo con **./wma2mp3.sh**

*Fonte:
<http://www.linuxquestions.org/linux/answers/Applications_GUI_Multimedia/Convert_WMA_to_MP3>*
