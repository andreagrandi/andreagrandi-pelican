Title: Ubuntu 9.04 (Jaunty) su Asus EeePC 901
Date: 2009-04-26 15:20
Author: admin
Category: EeePC, HowTo, Linux, Recensione, Ubuntu (IT)
Tags: 9.04, 901, asus, EeePC, jaunty, Ubuntu (EN)
Slug: ubuntu-904-jaunty-su-asus-eeepc-901
Status: published

![eee-pc-901](http://www.andreagrandi.it/wp-content/uploads/2008/10/eee-pc-901.jpg "eee-pc-901"){.alignright
.size-full .wp-image-126 width="202" height="154"}Con l'uscita della
versione **9.04** di [Ubuntu Linux](http://www.ubuntu.com), questa
distribuzione ha veramente fatto passi da gigante per quanto riguarda il
supporto ai **netbook**. Oltre a rilasciare una versione
specificatamente pensata per i piccoli device (che integra di default
l'interfaccia [**Notebook
Remix**](http://www.canonical.com/projects/ubuntu/unr)), sono stati
inclusi nel kernel tutti i moduli necessari a far funzionare le
periferiche di questi device.

Per installare Ubuntu sull'EeePC dobbiamo per prima cosa procurarci la
ISO dell'ultima versione e poi utilizzare una delle seguenti utility per
preparare una chiavetta USB (da almeno 1 Gb) che ci permetterà di
effettuare l'installazione: **USB Startup Disk Creator**, disponibile a
partire dalle ultime versioni di Ubuntu (si trova in
System--&gt;Administration) oppure **Unetbootin**, che potete trovare a
questo indirizzo: <http://unetbootin.sourceforge.net/>

Nel caso vogliate installare la versione NBR (Notebook Remix) di Ubuntu,
che viene distribuita in formato .img dovete invece attenervi alle
istruzioni che trovate su questa pagina:
<https://help.ubuntu.com/community/Installation/FromImgFiles>

Una volta preparata la chiavetta USB (o in alternativa va bene anche una
memoria di tipo SD) dovrete utilizzarla per fare il boot (vi ricordo che
per fare il boot da USB dovete **premere ESC** nei primi secondi di
accensione dell'EeePC) e procedere all'installazione come se fosse un
normale PC. Se posso darvi un consiglio su come partizionare, vi
suggerisco di utilizzare il disco da **4 Gb** per la root **/** e quello
da **16 Gb** (o 12 Gb a seconda dei modelli) per la **/home**.

Completata l'installazione, al riavvio dell'EeePC avrete una piacevole
sorpresa: tutte le periferiche saranno perfettamente riconosciute!
Questo dimostra l'ottimo lavoro che è stato fatto per supportare questa
fascia di dispositivi. E' necessaria tuttavia qualche altra piccola
ottimizzazione per poter sfruttare al 100% il nostro netbook.

Per prima cosa vi consiglio di installare [gli
script](http://www.informatik.uni-bremen.de/~elmurato/EeePC/Jaunty_Eeeasy-Scripts.tar.gz)
di **elmurato** che vi permetteranno di utilizzare correttamente tutti i
tasti funzione (Fn+Fx). Perchè possano funzionare dovrete anche
installare sia un pacchetto presente nella Ubuntu, sia uno incluso nel
tar.gz, seguendo le seguenti istruzioni:

`sudo apt-get install dkms sudo apt-get remove --purge nvidia-common tar xzvf Jaunty_Eeeasy-Scripts.tar.gz cd Jaunty_Eeeasy-Scripts sudo dpkg --install asus-eee-dkms_3.0_all.deb sudo ./eeeasy-scripts.sh`

A questo punto non vi resta che riavviare il vostro EeePC e
l'installazione sarà completata. Se vogliamo essere precisi, ci sono
ancora un paio di piccole cose da migliorare. Noterete infatti che il
tasto per abilitare/disabilitare il **bluetooth** non funziona
correttamente. Si tratta di un bug del kernel **2.6.28** che viene
fortunatamente risolto con la versione **2.6.29** di cui **elmurato**
fornisce i pacchetti .deb già compilati:
<http://www.informatik.uni-bremen.de/~elmurato/EeePC/> (dovrete
installare **linux-headers-\*** e **linux-image-\*** ).

La versione 2.6.29 del kernel include anche una versione aggiornata del
modulo che fa funzionare la scheda **wireless**, permettendoci di avere
un **segnale piu' stabile**.

Consiglio infine di aggiungere la seguente stringa in fondo al file
**/etc/modprobe.d/options** (createlo se non esistesse): **options
psmouse proto=imps  
**questa opzione fa in modo che il touchpad funzioni meglio rispetto a
come viene configurato di default.**  
**
