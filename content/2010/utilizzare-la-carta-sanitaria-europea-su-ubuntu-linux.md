Title: Utilizzare la Carta Sanitaria Europea su Ubuntu Linux
Date: 2010-11-11 14:32
Author: admin
Category: HowTo, Linux, Ubuntu (IT)
Tags: CSE, Firefox, Regione Toscana, SmartCard
Slug: utilizzare-la-carta-sanitaria-europea-su-ubuntu-linux
Status: published

![](http://www.andreagrandi.it/wp-content/uploads/2010/11/jpg_2056020.jpg "CSE_Toscana"){.alignright
.size-full .wp-image-426 width="149" height="118"}In questo periodo le
regioni stanno inviando a casa di ogni cittadino la nuova versione della
**Carta Sanitaria Europea**, simile a quella che potete vedere nella
foto. Questa nuova carta, oltre a conservare gli stessi utilizzi di
quella vecchia, comprende anche un micro chip che permette di
utilizzarla con i comuni lettori di smartcard.

Ma a cosa serve poter utilizzare la CSE con un lettore di smartcard? Ad
esempio ad accedere al proprio **fascicolo sanitario** tramite il sito
della regione, che ci permetterà di vedere alcuni nostri dati come ad
esempio: medicine prese, esenzioni, ricoveri in ospedale, ricoveri al
pronto soccorso, risultati delle analisi ecc...

Per accedere all'area riservata non viene utilizzato il classico metodo
di username/password, ma bensì l'autenticazione tramite smartcard.

Installazione del lettore di smartcard
--------------------------------------

![](http://www.andreagrandi.it/wp-content/uploads/2010/11/miniLectorBox.jpg "miniLectorBox"){.alignright
.size-full .wp-image-435 width="132" height="133"}

Prima di utilizzare la carta su **Ubuntu Linux** è necessario intanto
procurarsi un lettore di smartcard (**vi consiglio di acquistare il
kit** che vendono dove siete andati ad attivare la vostra CSE, poichè
viene venduto ad un prezzo vantaggioso di **4,20€** mentre se provate a
comprare il lettore altrove non lo troverete a meno di 15-20€) e poi
installare sul proprio sistema alcuni pacchetti necessari al suo
funzionamento.

Il lettore, una volta inserito nel proprio PC dovrebbe essere
identificabile tramite la seguente stringa:

\[sourcecode lang="text"\]  
andrea@centurion:\~\$ lsusb  
Bus 002 Device 004: ID 072f:90cc Advanced Card Systems, Ltd ACR38
SmartCard Reader  
\[/sourcecode\]

Per installare il software necessario, occorre eseguire il seguente
comando da terminale:

\[sourcecode lang="text"\]sudo apt-get install pcsc-tools pcscd
libccid\[/sourcecode\]

dopo di che dovrete procurarvi il driver del lettore, che potete trovare
a [questo
indirizzo](http://www.regione.toscana.it/Carta_sanitaria/software/linux/Installazione_lettore_LINUX/lettore/soft_lettore.zip)
ed installarlo con il seguente comando (dopo aver scompattato l'archivio
in una cartella a piacimento):

\[sourcecode lang="text"\]sudo dpkg -i
libminilector38u-bit4id.deb\[/sourcecode\]

Se tutto è stato eseguito correttamente, utilizzando il programma
**pcsc\_scan** da terminale, dovreste ottenere un output simile a
questo:

\[sourcecode lang="text"\]  
andrea@centurion:\~\$ pcsc\_scan  
PC/SC device scanner  
V 1.4.16 (c) 2001-2009, Ludovic Rousseau
&lt;ludovic.rousseau@free.fr&gt;  
Compiled with PC/SC lite version: 1.5.3  
Scanning present readers...  
0: ACS ACR 38U-CCID 00 00

Thu Nov 11 14:08:37 2010  
Reader 0: ACS ACR 38U-CCID 00 00  
Card state: Card inserted,  
ATR: 3B DF 18 00 81 31 FE 7D 00 6B 15 0C 01 81 01 11 01 43 4E 53 10 31
80 E8  
\[/sourcecode\]

Configurazione di Firefox
-------------------------

Prima di poter configurare Firefox è necessario installare un'ultima
libreria che permetterà al browser di poter interagire con il lettore di
smartcard. Dobbiamo scaricare l'archivio presente a [questo
indirizzo](http://www.regione.toscana.it/Carta_sanitaria/software/linux/Installazione_CSE_LINUX/Software/smart_card.zip),
scompattarlo e poi copiare uno dei due file presenti (a seconda che si
utilizzi un sistema a 32 o 64 bit) all'interno della cartella
**/usr/lib** ed infine digitare il comando **sudo ldconfig** per
aggiornare l'elenco delle librerie.

A questo punto bisogna aprire **Firefox** ed andare su
**Modifica--&gt;Preferenze--&gt;Avanzate--&gt;Cifratura--&gt;Dispositivi
di Sicurezza** cliccare su **Carica** e specificare come descrizione
**"CSE"** e come percorso quello dove avete copiato la libreria
installata nel passo precedente (che ad esempio potrà trovarsi in
**/usr/lib/libaseCnsP11.so** ).

Per verificare che tutto funzioni correttamente è sufficiente fare click
su **Accedi** e se ci verrà chiesto di inserire la "password" (che nel
nostro caso sarà il **PIN** della smartcard) vorrà dire che tutto sta
funzionando nel modo corretto.

Per avere maggiori informazioni sulla **Carta Sanitaria Europea** e per
conoscere tutti i servizi disponibili, vi consiglio di visitare la
seguente pagina presente sul sito della **Regione Toscana**:
<http://www.regione.toscana.it/cartasanitaria/cse/cose/index.html>
