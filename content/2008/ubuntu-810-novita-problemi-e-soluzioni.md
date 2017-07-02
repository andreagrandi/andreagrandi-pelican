Title: Ubuntu 8.10: novità, problemi e soluzioni
Date: 2008-11-07 19:19
Author: admin
Category: Recensione, Ubuntu (IT)
Tags: Ubuntu (EN)
Slug: ubuntu-810-novita-problemi-e-soluzioni
Status: published

![](http://www.andreagrandi.it/wp-content/uploads/2008/11/countdown_8_10_a_00_days_a_here.png "countdown_8_10_a_00_days_a_here"){.alignright
.size-full .wp-image-151 width="180" height="150"}Il **30 ottobre 2008**
è stata rilasciata la versione **8.10** di
[**Ubuntu**](http://www.ubuntu.com). Questa release presenta come al
solito **moltissime novità** per l'utente finale, **ma non è esente da
alcuni problemi** che solitamente riguardano le distribuzioni appena
uscite.

Questo articolo vuole essere un riferimento per chi sta utilizzando una
versione precedente di Ubuntu Linux o per chi ci si avvicina per la
prima volta, in modo che possa essere fatta una scelta in base agli
effettivi vantaggi e svantaggi.

Novità per l'utilizzo desktop
-----------------------------

Per l'utente desktop di, sono state introdotte alcune caratteristiche
che possono facilitarne l'utilizzo in particolare a chi utilizza Ubuntu
sui notebook, migliorando anche la sicurezza dei propri dati personali.

**Supporto alle connessioni 3G:** la versione 0.7 del **NetworkManager**
inclusa in questa release permette di gestire anche le connessioni
**GPRS/UMTS/HSDPA** in maniera piu' semplice, sia che si utilizzi un
modem interno, un dongle USB oppure che ci si connetta utilizzando il
proprio cellulare tramite il bluetooth.

**Installazione ed avvio da dischi USB:** è stato incluso un comodo tool
che permette di installare Ubuntu su una chiavetta o un disco USB
tramite una semplicissima interfaccia grafica. In questo modo sarà
possibile portarsi dietro la propria copia di Ubuntu ovunque si vada e
avendo anche la possibilità di salvare le impostazioni ed i propri
documenti.

**Utente Guest:** adesso è possibile lasciare in sospeso la propria
sessione utente avviando temporaneamente una seconda sessione **ospite**
per permettere ad esempio ad un nostro amico o collega di controllare la
propria posta elettronica o di navigare sul web **senza che questo possa
curiosare nei nostri documenti** o memorizzare file in maniera
permanente.

**Contenuti BBC:** grazie ad un accordo fra la **Canonical** e la
**BBC** è stato sviluppato un **plugin** che permette agli utenti di
accedere ai contenuti online della BBC tramite **Totem Movie Player** o
**Rhythmbox**.

**Gnome 2.24:** questa versione di Gnome incorpora un **nuovo client di
instant-messaging**, migliora il file manger Nautilus introducendo i
**tab** come su Firefox, migliora il supporto ai **monitor multipli** ed
aggiunge alcuni **nuovi formati** al gestore degli archivi compressi.

**Cartella privata cifrata:** è possibile creare in maniera molto
semplice una cartella privata che viene montata soltanto quando l'utente
è loggato nella propria sessione ed il cui contenuto viene cifrato.
Questa funzionalità è molto utile per chi ad esempio utilizza Linux in
un portatile: in caso di smarrimento del portatile nessuno sarebbe in
grado di accedere al contenuto di tale cartella.

**X.Org 7.4:** questa nuova versione di X.Org consente il riconoscimento
di mouse, tastiere e tavolette grafiche a caldo (nel senso che vengono
riconosciute non appena si inseriscono, quando il sistema è già
avviato).

**DKMS:** si tratta di un tool sviluppato dalla Dell. Quando una nuova
versione del kernel viene rilasciata, tutti moduli vengono
automaticamente ricompilati.

Novità per l'utilizzo server
----------------------------

Le novità non mancano anche per chi utilizza Ubuntu come server. Sono
stati introdotti sostanziali miglioramenti nel campo della
virtualizzazione, per chi sviluppa in Java e nei tool della gestione di
sistema.

**Virtualizzazione:** la versione
[**JeOS**](http://www.ubuntu.com/products/whatisubuntu/serveredition/jeos)
di Ubuntu è stata integrata in Ubuntu Server. Si tratta di una versione
ridotta di Ubuntu, adatta a girare all'interno delle macchine virtuali.
Ubuntu Server è anche ufficialmente supportata come sistema guest su
**Xen**.

**Java:** **Apache Tomcat 6.0** e **OpenJDK 6** sono completamente
supportati ed incusi nel repository principale di Ubuntu.

**Mail Server:** sono stati integrati nel repository principale sia
**ClamAV** che **SpamAssassin**. Questi due programmi permettono di
integrare nel server di posta sia il controllo anti-virus che
l'anti-spam.

**Supporto RAID:** dalla versione 8.10 è stato **aggiunto il supporto**
che permette di fare il **boot anche da un RAID degradato**. Questo
significa che se si dovesse rompere uno dei due dischi, verrà chiesto
all'utente se si vuole procedere ugualmente al boot, in modo da non
dover per forza bloccare quella macchina.

**Uncomplicated Firewall:** è stato migliorato il supporto al firewall
semplificato. Adesso è possibile specificare direttamente il nome del
servizio che si vuole aprire o chiudere, senza dover specificare il
numero della porta.

I problemi della nuova Ubuntu 8.10
----------------------------------

Come ho anticipato all'inizio, puo' capitare che una nuova release,
oltre ad introdurre nuove funzionalità, abbia anche dei **problemi** sia
perchè viene distribuita con versioni piu' recenti dei vari pacchetti,
sia **perchè non è stata sufficientemente testata** prima di essere
rilasciata.

Cerchero' di riassumere quelli che sono i problemi principali di questa
versione, in modo che ogni persona possa capire, a seconda dell'uso che
ne fa del PC e a seconda dell'hardware sul quale andra' ad installare
Ubuntu, se questi saranno o no un problema per l'utilizzo quotidiano.

**Il lettore CD/DVD mangia le dita ([bug
\#283316](https://bugs.launchpad.net/bugs/283316)):** non allarmatevi!
Non esce alcun mostro dal lettore a mangiare le vostre dita... Si tratta
semplicemente di un bug che fa si che il **carrellino** del lettore CD
venga **reinserito troppo velocemente** quando si richiede che un CD
venga fatto uscire. In pratica si ha meno di un secondo a disposizione
per togliere il CD, in caso contrario il carrello verra' chiuso e
dovremo premere manualmente il pulsante di eject.

**La sessione di Gnome non viene memorizzata ([bug
\#249373](https://bugs.launchpad.net/bugs/249373)):** a causa di un
cambiamento nel protocollo utilizzato per salvare la sessione, la
maggior parte delle applicazioni (come ad esempio Pidgin, Skype ecc...)
non sono piu' in grado di essere avviate automaticamente quando si salva
la sessione. E' necessario avviarle manualmente dopo ogni login.

**La ricezione e l'invio dei files tramite Bluetooth non funziona piu'
con i normali tool ([bug
\#290875](https://bugs.launchpad.net/bugs/290875)):** cercando di
connettersi ad un dispositivo esterno tramite Bluetooth, per lo scambio
dei files, si otterrà un errore. Sono stati introdotti nuovi tool (che
non sono ancora completi) ma non vengono installati di default.

**Le stampanti condivise con Samba non riescono a stampare quando non è
richiesta autenticazione ([bug
\#283811](https://bugs.launchpad.net/bugs/283811)):** un bug di CUPS
aggiunge ad ogni avvio una riga nel file di configurazione che obbliga a
richiedere l'autenticazione per poter stampare e questo impedisce alle
applicazioni di stampare.

**Il plugin UPnP di Rhythmbox non viene caricato ([bug
\#160592](https://bugs.launchpad.net/ubuntu/+source/rhythmbox/+bug/160592)):**
quando si tenta di abilitare questo plugin dentro Rhythmbox si ottiene
un errore e non è possibile quindi attivarlo. Per farlo funzionare
occorre installare il pacchetto **python-coherence**.

Questi sono solo alcuni dei problemi noti della Ubuntu 8.10. Potete
trovare la lista completa nella pagina delle release notes:
<http://www.ubuntu.com/getubuntu/releasenotes/810>

La maggior parte di questi problemi riguardano solo alcune particolari
configurazioni oppure hardware ben preciso, quindi se il vostro sistema
non rientra in uno dei casi che vengono elencati, potete installare la
nuova Ubuntu senza alcun timore.

Soluzioni ai problemi della nuova Ubuntu
----------------------------------------

La **maggior parte dei problemi** che ho citato sopra, **sono stati nel
frattempo corretti** e sono stati rilasciati i pacchetti aggiornati che
verranno inseriti poi nella prossima bug-fix release (presumibilmente la
**8.10.1**).

Per testare in anteprima le patch che vengono rilasciate, occorre
abilitare il repository **intrepid-proposed** tramite
**System-&gt;Administration-&gt;Software Sources-&gt;Updates**. E'
opportuno specificare che si tratta di patch che sono ancora sotto fase
di testing ma che nel 99% dei casi riescono a risolvere il problema.

Un suggerimento che vorrei dare agli utenti con un minimo di esperienza,
è quello di **non attendere che i bug vengano corretti standosene con le
braccia incrociate**. Esiste un comodissimo strumento che si chiama
[**Launchpad**](https://launchpad.net/ubuntu) che Ubuntu utilizza per
raccogliere le **segnalazioni dei bug** nei programmi.

E' fondamentale che piu' persone diano il loro feedback su un
particolare problema, in modo da aiutare gli sviluppatori a correggerlo
nel minor tempo possibile.

Conclusioni
-----------

Volendo fare il punto della situazione, la Ubuntu 8.10 introduce
**interessanti novità** per l'utente finale, ma **anche diversi bug**.

Se si utilizza Ubuntu in **ambienti critici**, il mio consiglio è quello
di **attendere** almeno un mesetto **prima di fare l'aggiornamento**, in
modo che almeno i problemi piu' gravi possano essere risolti.

Per tutti gli altri problemi ricordo quanto sia importante dare il
proprio contributo. Non è necessario avere competenze tecniche da
programmatori o hacker per migliorare una distribuzione. **Occorre**
solo armarsi di pazienza e saper dialogare con gli sviluppatori per
**segnalare in tempi brevi i problemi** ed attendere che vengano
corretti.

Riferimenti
-----------

La recensione delle novità e dei problemi della nuova Ubuntu 8.10 è
stata possibile sia grazie all'utilizzo diretto (è la distribuzione che
uso sul PC fisso) sia grazie alla lettura di alcuni post e alle release
notes ufficiali. Per approfondimenti:

-   **Avoiding feature regressions should be more important than (exact)
    time based releases:**
    <http://ernstfamily.ch/jonathan/2008/11/avoiding-feature-regressions/>
-   **Ubuntu 8.10 Release Notes:**
    <http://www.ubuntu.com/getubuntu/releasenotes/810>
-   **Ubuntu Desktop Edition:**
    <http://www.ubuntu.com/news/ubuntu-8.10-desktop>
-   **Ubuntu Server Edition:**
    <http://www.ubuntu.com/news/ubuntu-8.10-server>

