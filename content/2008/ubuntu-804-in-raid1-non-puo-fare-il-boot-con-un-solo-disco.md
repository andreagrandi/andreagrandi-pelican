Title: Ubuntu 8.04 in RAID1 non può fare il boot con un solo disco
Date: 2008-09-25 14:05
Author: admin
Category: Linux, Sicurezza, Ubuntu (IT)
Tags: boot, mirror, RAID1
Slug: ubuntu-804-in-raid1-non-puo-fare-il-boot-con-un-solo-disco
Status: published

![](http://www.andreagrandi.it/wp-content/uploads/2008/09/raid1.jpg "raid1"){.alignright
.size-full .wp-image-122 width="157" height="179"}La modalità **RAID1**
(detta anche modalità **mirror**) è una particolare configurazione nella
quale vengono utilizzati due hard disk al posto di uno, per
leggere/scrivere gli stessi dati. Questo permette di avere **un'esatta
copia degli stessi dati su due dischi diversi**, facendo in modo che se
uno si dovesse rompere, l'altro conterrebbe una copia esatta dei dati,
permettendoci quindi di sostituire il disco rotto senza alcuna perdita.

Quello che **ci si aspetta** quando uno dei due dischi si rompe è **che
il sistema continui a funzionare normalmente**, magari avvisandoci della
rottura di uno dei due dischi.

Il comportamento di **Ubuntu 8.04** purtroppo **non segue questa
procedura**. Gli script di avvio sono infatti configurati in modo che
venga impedito il boot di sistema se il RAID risulta degradato. Questo
comportamento è stato inizialmente [segnalato come
bug](https://bugs.launchpad.net/initramfs-tools/+bug/120375) su
**launchpad.net** e successivamente confermato e marcato come "risolto"
per la prossima release di Ubuntu, la **8.10** che dovrebbe uscire alla
fine di ottobre.

Lo sviluppatore che si è occupato di risolvere il problema, [**Dustin
Kirkland**](https://launchpad.net/~kirkland), ha anche creato
un'apposita [pagina sul wiki](https://wiki.ubuntu.com/BootDegradedRaid)
di Ubuntu dove spiega uno scenario reale e come il problema è stato
risolto.

Ci saremmo aspettati di veder incluso questo fix anche nell'attuale
Ubuntu 8.04, visto che si tratta di una **LTS** (non tutti vorranno
abbandonare una versione la cui stabilità e gli aggiornamenti sono
mantenuti per almeno 3 anni) solo per risolvere un problema col RAID1,
ma per adesso non sembra rientrare nei piani degli sviluppatori.
