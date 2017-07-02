Title: Installazione e configurazione di Ubuntu Eee 8.04.1 su Asus EeePC 901
Date: 2008-10-05 14:44
Author: admin
Category: EeePC, HowTo, Linux
Tags: asus, EeePC, ubuntu-eee
Slug: installazione-e-configurazione-di-ubuntu-eee-8041-su-asus-eeepc-901
Status: published

![](http://www.andreagrandi.it/wp-content/uploads/2008/10/asus_ubuntueee.jpg "asus_ubuntueee"){.alignright
.size-full .wp-image-128 width="240" height="197"}La versione di Linux
che viene installata sugli EeePC (**Xandros** Linux) da Asus, sebbene
sia l'ideale per chi non ha mai utilizzato Linux e desidera un netbook
semplice da usare, tuttavia **non permette di sfruttare pienamente le
potenzialità** che l'EeePC ha.

Poco tempo dopo l'uscita dei primi modelli degli EeePC sono iniziate
quindi ad essere rilasciate distribuzioni alternative alla Xandros,
ottimizzate per il netbook di Asus. E' ovviamente possibile installare
una qualsiasi distribuzione Linux, ma ovviamente il lavoro da compiere
per far funzionare tutte le periferiche sarà maggiore rispetto a quello
necessario con una distribuzione realizzata ad hoc.

La distribuzione che ho deciso di installare sul mio **EeePC 901** è la
[Ubuntu Eee 8.04.1](http://www.ubuntu-eee.com).

Per installare la **Ubuntu Eee** è necessario scaricarla dal [sito web
dedicato](http://www.ubuntu-eee.com/wiki/index.php5?title=Get_Ubuntu_Eee)
e poi trasferirla su una chiavetta USB o su un disco USB esterno (visto
che l'EeePC non è dotato di lettore CD/DVD) utilizzando una utility
chiamata **Unetbootin** e seguendo le [istruzioni presenti sul
wiki](http://www.ubuntu-eee.com/wiki/index.php5?title=How_to:_Using_Unetbootin).

Dopo aver trasferito l'installazione sulla chiavetta USB dobbiamo
inserirla nell'EeePC ed avviare premendo piu' volte il tasto **Esc**.
Quando compare il menu di avvio, dobbiamo selezionare il disco USB dalla
lista e premere **Invio** per continuare.

Nel caso la Ubuntu Eee non si dovesse avviare, i motivi possono essere
diversi. Per prima cosa dobbiamo controllare nella sezione Boot del
**BIOS** se il disco USB è al primo posto nell'ordine dei dischi da cui
fare il boot. Se non dovesse avviarsi nemmeno in questo caso, è
possibile che la **chiavetta** USB **non sia compatibile**: a me è
successo di non essere in grado di utilizzare una chiavetta USB da 1 Gb
che avevo e sono dovuto ricorrere ad un disco esterno USB.

Se riusciamo ad avviare la Ubuntu Eee, saremo in grado di utilizzare
l'installer grafico senza alcun problema. Il mio consiglio è quello di
scegliere il **partizionamento manuale** e di utilizzare il primo
**disco SSD** da **4 Gb per la root /** ed il **disco SSD** da **16 Gb
per la /home**.

Le **caratteristiche** della **Ubuntu Eee** la rendono praticamente la
distribuzione perfetta per gli EeePC:

-   supporto per gli Asus EeePC 701, 900, 900A, 901, 1000 e 1000H
-   occupa 1.8 Gb di spazio
-   Kernel ottimizzato di [Adam](http://www.array.org/ubuntu/) con
    supporto per tutte le periferiche degli EeePC
-   interfaccia Notebook Remix predefinita (è possibile cambiarla
    tramite un'apposita utility)

Sebbene il setup e la configurazione predefiniti di Ubuntu Eee siano
quasi perfetti, tuttavia sono necessari ancora alcuni ritocchi per fare
in modo che tutto funzioni regolarmente.

Per prima cosa occorre **commentare** l'ultima riga di **/etc/fstab**,
quella relativa al cdrom, altrimenti si otterrà un errore durante la
fase di mount quando si inserisce una chiavetta USB.

Per ottenere il meglio dal **risparmio energetico**, consiglio di
installare gli **script ACPI** di **Murat** che potete trovare a questo
indirizzo:
<http://www.informatik.uni-bremen.de/~elmurato/EeePC/Hardy_ACPI_scripts-EeePC_900A_901_1000.tar.gz>

Gli script permettono di attivare/disattivare alcune periferiche come il
bluetooth, la webcam, la wifi ecc... consentendo alla batteria di durare
piu' a lungo. Per l'installazione sono sufficienti i seguenti passaggi:

`tar xfvz Ubuntu_ACPI_scripts-EeePC_900A_901_1000.tar.gz cd Ubuntu_ACPI_scripts-EeePC_900A_901_1000/ chmod +x install.sh sudo ./install.sh`

In particolare le funzionalità che vengono aggiunte sono le seguenti
(gli hotkey sono quei tasti hardware posizionati sopra ad i tasti F1,
F2, ecc...):

-   Fn+F1 Standby
-   Fn+F2 WLAN-toggle
-   Fn+F3/F4 Brightness
-   Fn+F5 VGA-toggle
-   Fn+F6 Taskmanager
-   Fn+F7/F8/F9 Volume
-   1\. new hotkey Display-toggle (internal)
-   2\. new hotkey Bluetooth-toggle
-   3\. new hotkey CPU frequency control or user-defined
-   4\. new hotkey Webcam-toggle or user-defined

Gli script di Murat purtroppo introducono un **piccolo bug**: viene
disattivata la funzionalità **"Dim when idle"** del display (in pratica
non viene abbuiato lo schermo quando non si usa l'EeePC). Per
ripristinare questa funzionalità è sufficiente eseguire questo comando:  
` sudo cp /etc/acpi/backup/hal-system-lcd-set-brightness-linux /usr/lib/hal/scripts/linux/`

A questo punto la configurazione dovrebbe essere al completo. Si
consiglia di **riavviare l'EeePC** per rendere effettive tutte le
modifiche. Per ulteriori trucchetti su come ottimizzare la
configurazione, vi consiglio di visitare direttamente il [wiki di Ubuntu
Eee](http://www.ubuntu-eee.com/wiki/index.php5?title=User_Guides) dove
potrete trovare articoli piu' approfonditi.
