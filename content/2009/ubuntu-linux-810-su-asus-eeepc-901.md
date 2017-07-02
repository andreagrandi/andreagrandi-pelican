Title: Ubuntu Linux 8.10 su Asus EeePC 901
Date: 2009-02-02 12:21
Author: admin
Category: EeePC, HowTo, Linux, Recensione
Tags: 901, asus, EeePC, Linux, Ubuntu (EN)
Slug: ubuntu-linux-810-su-asus-eeepc-901
Status: published

![](http://www.andreagrandi.it/wp-content/uploads/2008/10/eee-pc-901.jpg "eee-pc-901"){.alignright
.size-full .wp-image-126 width="275" height="209"}Dal momento in cui ho
acquistato l'**Asus EeePC 901**, ho rimosso la versione personalizzata
di **Xandros Linux** che viene installata su questi modelli, ed ho
installato una versione personalizzata di Ubuntu: [**Ubuntu-eee
8.04.1**](http://www.ubuntu-eee.com).

Questa versione, pensata appositamente per i netbook della Asus, è
davvero molto comoda perchè integra di default un kernel con tutte le
patch ed i driver per far funzionare l'EeePC, che invece non sono
contenuti nel kernel distribuito dalla Ubuntu 8.04 standard. Ubuntu-eee
installa anche l'interfaccia [Netbook
Remix](https://launchpad.net/netbook-remix) che è una particolare
interfaccia grafica adatta per i netbook con schermi di ridotte
dimensioni.

L'idea di avere una distribuzione basata su Ubuntu che integra già tutte
le patch necessarie per farla funzionare mi è sembrata subito una buona
idea, tanto che ho anche pensato di inviare un piccolo contributo in
denaro durante la campagna di raccolta fondi per finanziarne lo
sviluppo.

I problemi di Easy Peasy
------------------------

Dalla versione successiva alla 8.04.1, Ubuntu-eee ha dovuto cambiare
nome (per non violare le regole del marchio "Ubuntu" di proprietà di
Canonical), e fin qui nulla di male. Quello che non mi è affatto
piaciuto è che mentre per il logo è stato fatto un apposito concorso e
poi scelto il migliore, per il nome l'autore ha scelto a "gusto"
proprio: **Easy Peasy**.

Digerita la questione del nome, ho deciso di provarla sul mio EeePC.
L'impressione è stata a dir poco pessima. Tanto per cominciare si nota
da subito che la distribuzione non è stata minimamente testata: al primo
riavvio dopo l'installazione, si presenta di nuovo l'installer, come se
la dovessimo installare da zero. Il fix non è ancora stato rilasciato,
in compenso l'autore ha spiegato come risolverlo a mano.

Oltre a questo, [leggendo il
forum](http://www.ubuntu-eee.com/forum/viewtopic.php?f=12&t=543),
saltano fuori almeno un'altra decina di **problemi** con la Easy Peasy.
Tutti problemi che sarebbero stati facilmente risolvibili in fase di
creazione della distribuzione personalizzata, se solo fosse stata
minimamente testata. Che ci possano essere dei problemi su una
distribuzione generica come ad esempio la Ubuntu (che è pensata per
girare su qualsiasi configurazione) lo posso anche capire.

Non mi pare accettabile che possano esserci **così tanti problemi** su
una distribuzione che dovrebbe essere fatta appositamente per un certo
modello di netbook.

Ubuntu 8.10
-----------

Deluso dalla versione personalizzata, ho deciso di provare ad installare
la versione standardi di Ubuntu, sistemando a mano le cose che non
andavano.

### Installazione di base

L'installazione di **Ubuntu 8.10** è identica a quella di
Ubuntu-eee/EasyPeasy. E' sufficiente creare una versione di Ubuntu che
faccia il boot da una chiavetta USB oppure da una memoria SD,
utilizzando la **comoda utility** presente in Ubuntu 8.10
(System-&gt;Administration-&gt;Create a USB startup disk) oppure tramite
**[Unetbootin](http://unetbootin.sourceforge.net)**.

Completata l'installazione, come già accennato, molte periferiche (come
ad esempio la webcam, la scheda wireless o i tasti funzione) non saranno
riconosciuti, ma questo già lo sapevamo. La scheda ethernet è invece
riconosciuta e configurata perfettamente da Ubuntu 8.10, quindi è
possibile utilizzare provvisoriamente il cavo per connettersi e
completare l'installazione delle componenti mancanti.

### Il kernel ottimizzato per EeePC

La prima cosa da installare è il [kernel personalizzato di
Adam](http://array.org/ubuntu/). Questo kernel integra tutte le patch
necessarie al funzionamento di tutte le periferiche dell'EeePC. Non mi
dilungherò in questo post nella spiegazione di come si installa,
rimandandovi invece all'howto originale, presente sul sito dell'autore:
<http://array.org/ubuntu/setup-intrepid.html>

### eee-control

Questa utility ci permette di far funzionare tutti i **tasti funzione**
del nostro EeePC (Fn+F\*) e di tenere sotto controllo alcuni parametri
di sistema come ad esempio la temperatura, la velocità della ventolina
ed infine di disabilitare le periferiche che non utilizziamo sul momento
(come ad esempio il bluetooth o la wifi) in modo da **prolungare la
durata della batteria**.

Per installarla è sufficiente seguire le [istruzioni sul
sito](http://greg.geekmind.org/eee-control/) dell'autore oppure
scaricarla direttamente da questo indirizzo:
<http://greg.geekmind.org/eee-control/deb/eee-control_0.8.3_all.deb>

### Altre ottimizzazioni

Per ottenere il massimo dal proprio EeePC è necessario effettuare ancora
qualche piccolo aggiustamento. I consigli che seguono potrebbero
applicarsi anche ad altri modelli di EeePC anche se personalmente ho
avuto modo di testarli solo con l'EeePC 901.

#### laptop-mode

Per abilitare alcune ottimizzazioni per i notebook, dobbiamo abilitare
il laptop-mode all'interno del file **/etc/default/acpi-support**  
`ENABLE_LAPTOP_MODE=true`  
infine dobbiamo modificare il file
**/etc/laptop-mode/laptop-mode.conf**  
`ENABLE_LAPTOP_MODE_ON_BATTERY=1`

#### noatime

E' consigliabile utilizzare l'opzione **noatime** al posto di
**relatime** per fare il mount delle partizioni ext3. In questo modo si
evita che vengano scritte su disco le informazioni relative all'ultimo
accesso (anche in lettura) di un file. Dobbiamo modificare /etc/fstab in
questo modo:  
`UUID=dce586c1-db13-43c3-8e12-9e1aec67afce / ext3 noatime,errors=remount-ro 0 1`

**N.B:** questa riga non va copiata così com'è, va soltanto sostituito
**relatime** con **noatime** in quella del proprio file.

Altre ottimizzazioni possono essere trovate sul **wiki** di Ubuntu-eee:
<http://www.ubuntu-eee.com/wiki/index.php5?title=User_Guides>

Conclusioni
-----------

Ammetto che avere una distribuzione che integri di suo tutte queste
modifiche potrebbe far risparmiare del tempo. Se questa distribuzione
però non viene rilasciata con già tutti i fix necessari a far funzionare
il modello di netbook per cui è stata fatta, a che serve? A quel punto
tanto vale installare una distribuzione normale e cogliere l'occasione
per imparare qualcosa, effettuando a mano le modifiche necessarie per
farla funzionare.
