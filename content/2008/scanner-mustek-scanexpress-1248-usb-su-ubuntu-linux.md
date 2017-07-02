Title: Scanner Mustek ScanExpress 1248 USB su Ubuntu Linux
Date: 2008-12-17 19:40
Author: admin
Category: HowTo, Linux
Tags: mustek, scanner
Slug: scanner-mustek-scanexpress-1248-usb-su-ubuntu-linux
Status: published

[![](http://www.andreagrandi.it/wp-content/uploads/2008/12/se1248ub.jpg "se1248ub"){.alignright
.size-full .wp-image-187 width="180"
height="134"}](http://www.mustek.de/eng_/html/produkte/se1248ub.htm)Lo
scanner [**Mustek ScanExpress 1248
USB**](http://www.mustek.de/eng_/html/produkte/se1248ub.htm) è
pienamente compatibile con Linux, però purtroppo non basta connetterlo
per farlo funzionare. **Ubuntu Linux 8.10** non distribuisce il firmware
necessario al suo funzionamento, però è possibile reperirlo ed
installarlo con molta facilità.

Per prima cosa dobbiamo assicurarci di avere il modello esatto di questo
scanner. Per scoprirlo è sufficiente dare il comando **lsusb** da
terminale. Dovremmo ottenere una stringa come la seguente:

`Bus 002 Device 003: ID 055f:021f Mustek Systems, Inc. SNAPSCAN e22`

A questo punto possiamo scaricare il suo firmware da [un
sito](http://www.meier-geinitz.de/sane/gt68xx-backend/) che li raccoglie
tutti (quelli che sono compatibili ovviamente):
[**http://www.meier-geinitz.de/sane/gt68xx-backend/firmware/SBSfw.usb**](http://www.meier-geinitz.de/sane/gt68xx-backend/firmware/SBSfw.usb)

Questo file va messo all'interno della cartella
**/usr/share/sane/gt68xx/** (occorrono i permessi di root per poterlo
fare, quindi il file andra' copiato tramite il comando **sudo cp
SBSfw.usb /usr/share/sane/gt68xx/** ).

Infine dobbiamo assicurarci di aver installato tutti i pacchetti
necessari a farlo funzionare:

`sudo apt-get install sane libsane sane-utils libsane-extras xsane xsane-common`

Lo scanner è adesso pronto per funzionare.

**Nota:** nella **Ubuntu 12.04** la
directory **/usr/share/sane/gt68xx/** non è presente di default e va
creata manualmente con **sudo mkdir **/usr/share/sane/gt68xx/****
