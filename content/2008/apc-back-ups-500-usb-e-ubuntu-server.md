Title: APC Back-UPS 500 USB e Ubuntu Server
Date: 2008-02-15 10:59
Author: admin
Category: Linux, Ubuntu (IT)
Tags: alimentazione, apc, apcupsd, back-ups, energetico, risparmio, server, shutdown, Ubuntu (EN), usb
Slug: apc-back-ups-500-usb-e-ubuntu-server
Status: published

![apc\_ups\_500](http://www.andreagrandi.it/wp-content/uploads/2008/02/apc500.thumbnail.jpg)L'utilizzo
di una unità UPS è certamente una delle cose piu' consigliate quando
vogliamo proteggere l'integrità di un computer da sbalzi di corrente o
interruzioni dell'alimentazione.

Cosa succede però quando la batteria dell'UPS si esaurisce? In casi
normali è molto semplice: la corrente viene a mancare del tutto ed il
nostro PC verrà spento bruscamente.

Alla mancanza di corrente non c'è modo di porre un rimedio definitivo,
però possiamo almeno fare in modo che il nostro computer venga spento in
maniera corretta, prima che la batteria dell'UPS si esaurisca del tutto.

Nel caso di una macchina Linux, ci viene in aiuto una utility chiamata
**apcupsd**. Installarla su Ubuntu è molto semplice:

\[code lang="bash"\]  
apt-get install apcupsd  
\[/code\]

A questo punto, dando per scontato che abbiate già connesso l'UPS al
PC/server, collegate il cavo USB a corredo in modo da far riconoscere
l'UPS a Linux, in modo da poter proseguire con la configurazione. Il
primo file da modificare è **/etc/apcupsd/apcupsd.conf** ed impostare i
seguenti parametri come segue:

\[code lang="bash"\]  
UPSCABLE usb  
UPSTYPE usb  
DEVICE  
\[/code\]

A questo punto non ci resta che modificare il file
**/etc/default/apcupsd** in modo da rendere effettive le modifiche:

\[code lang="bash"\]  
ISCONFIGURED=yes  
\[/code\]

Infine dobbiamo soltanto avviare il demone ed il gioco è fatto:

\[code lang="bash"\]  
/etc/init.d/apcupsd start  
\[/code\]

Per default **apcupsd** effettuerà lo **shutdown** nel PC quando la
batteria sarà arrivata al **5%** della sua capacità, consentendo così
uno shutdown controllato del sistema, ed evitando quindi possibili
perdite di dati.
