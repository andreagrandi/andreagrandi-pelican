Title: Creative Live Cam Notebook su Ubuntu Linux
Date: 2008-06-05 19:21
Author: admin
Category: Linux, Ubuntu (IT)
Tags: cam, creative, Linux, live, Ubuntu (EN), webcam
Slug: creative-live-cam-notebook-su-ubuntu-linux
Status: published

![Creative](http://www.andreagrandi.it/wp-content/uploads/2008/06/creative_live_cam_trasparente1.png)Finalmente
sono riuscito a trovare una webcam che funzioni (dopo qualche ricerca su
Google) abbastanza bene su Linux. Dopo aver provato una **[Logitech
Quickcam for
Notebook](http://www.logitech.com/index.cfm/webcam_communications/webcams/devices/2989&cl=it,it)**
mi ero quasi perso d'animo, poi ho deciso di fare un ultimo tentativo
con la [**Creative Live! Cam
Notebook**](http://it.europe.creative.com/products/product.asp?category=218&subcategory=219&product=16710).

Prima di proseguire nella lettura di questa guida, vi consiglio di
verificare che il modello di "Creative Live Cam" che state cercando di
installare, sia lo stesso che ho testato io. Potete verificarlo
scrivendo in un terminale il comando **lsusb**:  
` andy80@noteboontu:~$ lsusb Bus 003 Device 001: ID 0000:0000 Bus 002 Device 001: ID 0000:0000 Bus 001 Device 018: ID 041e:4068 Creative Technology, Ltd Bus 001 Device 001: ID 0000:0000`

Ovvero dovrete verificare che l'identificativo del vostro modello sia
esattamente **041e:4068**

Devo dire che al primo tentativo (ovvero inserendo il cavo USB nel mio
notebook e sperando che funzionasse) non ci sono riuscito, quindi mi
sono deciso a fare una piccola ricerca su Google. Ho notato che molte
persone hanno tentato (senza alcun successo) di far funzionare questa
webcam con i driver [**spca5xx**](http://mxhaard.free.fr/spca5xx.html)
che solitamente supportano un gran numero di webcam. Proseguendo nella
mia ricerca ho trovato i driver
**[ov51x-JPEG](http://www.rastageeks.org/ov51x-jpeg/index.php/Main_Page)**
che invece supportano il mio modello di webcam.

L'installazione non è difficile, dobbiamo però assicurarci di aver
installato sulla nostra macchina tutto il necessario per poter
ricompilare il modulo, quindi dovrete eseguire (da utente root oppure
utilizzando sudo) questo comando:

`apt-get install build-essential linux-headers-$(uname -r)`

A questo punto dovrete scaricare i sorgenti del driver, da questo
indirizzo: 
[**http://www.rastageeks.org/downloads/ov51x-jpeg/ov51x-jpeg-1.5.7.tar.gz**](http://www.rastageeks.org/downloads/ov51x-jpeg/ov51x-jpeg-1.5.7.tar.gz)

`root@noteboontu:~# wget http://www.rastageeks.org/downloads/ov51x-jpeg/ov51x-jpeg-1.5.7.tar.gz`

Dobbiamo poi scompattarli con il seguente comando:

`root@noteboontu:~# tar xfvz ov51x-jpeg-1.5.7.tar.gz`

Infine dobbiamo compilare il modulo ed installarlo:

`root@noteboontu:~# cd ov51x-jpeg-1.5.7 root@noteboontu:~/ov51x-jpeg-1.5.7# make root@noteboontu:~/ov51x-jpeg-1.5.7# make install`

Se la compilazione e l'installazione del modulo sono andati a buon fine,
possiamo finalmente caricare il modulo:

`root@noteboontu:~/ov51x-jpeg-1.5.7# modprobe ov51x-jpeg`  
Prima di poter utilizzare la webcam con Skype, c'è ancora una piccola
cosa da aggiustare, per evitare problemi di incompatibilità. Dobbiamo
modificare il file /etc/modprobe.d/options ed aggiungere la seguente
riga:  
` options ov51x-jpeg forceblock=1`

ovviamente prima di caricare il modulo. A questo punto l'installazione
dovrebbe essere completa. Se ci fossero problemi o difficoltà potete
scrivere lasciando un commento a questo post, in modo che anche altri
possano poi leggere la domanda/risposta.
