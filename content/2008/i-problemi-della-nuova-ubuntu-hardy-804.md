Title: I problemi della nuova Ubuntu Hardy 8.04
Date: 2008-04-29 19:05
Author: admin
Category: Linux, Ubuntu (IT)
Tags: 8.04, bluetooth, bugs, calendar, evolution, firefox 3, hardy, instabile, Linux, nvidia, problemi, tracker, Ubuntu (EN)
Slug: i-problemi-della-nuova-ubuntu-hardy-804
Status: published

[![ubuntu\_logo](http://www.andreagrandi.it/wp-content/uploads/2008/02/ubuntu-logo.thumbnail.png "ubuntu_logo")](javascript:void(0) "ubuntu_logo"){#file-link-14
.file-link .image}Il 24 aprile è uscita la tanto attesa **Ubuntu Hardy
8.04**, sicuramente una tra le distribuzioni piu' utilizzate al momento
dagli utenti Linux.

Trattandosi di una release LTS (long time support, ovvero supportata per
ben 3 anni dal rilascio) ci si aspettava che potesse trattarsi di una
distribuzione assai stabile. Dopo circa una decina di giorni di utilizzo
(avevo iniziato a fare l'upgrade pochi giorni prima dell'uscita
ufficiale), devo purtroppo confermare le lamentele che molti stanno
sollevando riguardo a questa versione.

Molti fattori, tra cui l'instabilità di alcuni applicativi che sono
stati distribuiti con questa versione, non ancora pronti al momento del
rilascio, hanno fatto si che questa versione risulti una delle piu'
instabili tra tutte quelle che sono state rilasciate fino ad ora.

Qui di seguito farò una panoramica dei problemi che ho personalmente
riscontrato, premettendo che si tratta ovviamente di una lista di
problemi non completa e relativa in particolare ai miei due PC sul quale
ho avuto modo di testarla:

**Firefox 3:** la versione di Firefox distribuita al momento del
rilascio della Ubuntu 8.04 è la versione **3.0 beta 5**. Pur trattandosi
di una versione "abbastanza stabile", non è del tutto esente da alcuni
fastidiosi bug, in particolare si riscontrano [frequenti crash del
browser](https://bugs.launchpad.net/ubuntu/+source/pulseaudio/+bug/192888)
quando si cerca di visualizzare video tramite il **plugin Flash**.

**PulseAudio:** il nuovo sistema di gestione audio adottato da Ubuntu,
sebbene abbia sulla carta ottime funzionalità, non è ancora compatibile
con la maggior parte dei programmi in circolazione. Questo fa si che, ad
esempio, anche programmi opensource come il client ufficiale di
**Last.Fm** abbiano problemi nel gestire la periferica audio, dando
spesso il seguente errore "The Alsa soundsystem is either busy or not
present".

**Bluetooth:** fino alla versione 7.10 di Ubuntu riuscivo ad inviare
correttamente le foto dal mio Nokia N73 al PC. Con la 8.04 non ci riesco
piu'. Il
[bug](https://bugs.launchpad.net/ubuntu/+source/bluez-utils/+bug/211252)
è già stato segnalato e riguarda anche altre persone oltre a me.

**Clock Applet:** cliccando sull'orologio per visualizzare il
calendario, va in crash gnome-panel. Anche [questo
bug](https://bugs.launchpad.net/ubuntu/+source/gnome-panel/+bug/203527)
è stato già segnalato ed era stato "fixato" prima del rilascio della
versione definitiva, ma ancora il problema non è risolto.

**Evolution e Google Calendar:** una delle funzioni tanto attese sarebbe
dovuta essere la possibilità di integrare Calendar di Google nel
calendario di Evolution. Purtroppo si tratta di un altro
[bug](https://bugs.launchpad.net/ubuntu/+source/evolution/+bug/220596)
ancora non risolto.

**Nvidia ed il driver proprietario:** sia a me che ad altre persone, non
viene installato correttamente il
drive[ ](javascript:void(0) "ubuntu_logo"){#file-link-14 .file-link
.image}r proprietario aggiornato, dopo aver aggiornato ad Ubuntu 8.04.
Io ho risolto disattivando il modulo e reinstallandolo da capo. Il
problema però non è ancora stato risolto.

**Tracker:** il tool di indicizzazione integrato nella Ubuntu, non
indicizza correttamente il contenuto di alcuni file. Cercando ad esempio
"Benedetta" vengono fuori anche i documenti che contengono "Benedetto".
Anche questo
[bug](https://bugs.launchpad.net/ubuntu/+source/tracker/+bug/222046) è
stato segnalato.

In conclusione, non mi sento proprio di consigliare, almeno per il
momento, l'aggiornamento alla Ubuntu 8.04 a meno che non si voglia
contribuire attivamente alla segnalazione dei bug, in modo che il team
di sviluppo di Ubuntu possa correggerli al piu' presto. Non ci resta che
attendere la versione **8.04.1** che uscirà prossimamente e conterrà i
principali fix dei bug che sono stati segnalati in questi giorni.
