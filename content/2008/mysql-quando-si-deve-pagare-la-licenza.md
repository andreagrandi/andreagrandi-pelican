Title: MySQL: quando si deve pagare la licenza?
Date: 2008-02-05 15:47
Author: admin
Category: Linux, MySQL
Tags: commerciale, licenza, MySQL, opensource, pagamento, programma, programmi, vendita
Slug: mysql-quando-si-deve-pagare-la-licenza
Status: published

![mysql\_logo](http://www.andreagrandi.it/wp-content/uploads/2008/02/mysql_logo.thumbnail.jpg)Una
delle domande che mi vengono fatte piu' di frequente è "*MySQL si paga
per uso commerciale?*". La risposta non è delle piu' semplici.

Leggendo direttamente il sito web di **MySQL**, si possono trovare due
pagine dedicate alle licenze: una per chi fa sviluppo di [software
opensource](http://www.mysql.com/company/legal/licensing/opensource-license.html)
ed una per chi sviluppa [software
commerciale](http://www.mysql.com/company/legal/licensing/commercial-license.html).

Dopo una lettura superficiale delle due pagine, potremmo essere tratti
in inganno e pensare che sviluppando un'applicazione commerciale, si
debba per forza acquistare una licenza commerciale di MySQL. Questo non
è vero.

Tutto dipende dal tipo di librerie di interfacciamento che vogliamo
utilizzare. MySQL mette a disposizione due modi per interfacciarsi al
database: una propria **API** scritta in linguaggio C ed un **socket**
in ascolto che riceve comandi tramite una normale connessione TCP/IP.

E' chiaro che scrivendo un'applicazione che va a fare l'include di
(faccio un esempio) mysql.h poi io debba rilasciarne i sorgenti. La
licenza GPL con il quale è stato rilasciato MySQL (ed anche le sue
librerie client) dice chiaramente che quando si "*linka*" codice GPL ad
altro codice, il risultato deve essere per forza rilasciato sotto
licenza GPL.

La licenza GPL però non impone vincoli di utilizzo dell'applicazione
stessa. Utilizzare quindi una libreria client che al posto delle API,
usa il socket TCP/IP, ci permette di utilizzare MySQL anche da
un'applicazione closed-source, senza bisogno di ottenere una licenza
commerciale.

E' esattamente quello che fa la libreria di interfacciamento di
**Python** oppure di **PHP**. Esse utilizzando il metodo di connessione
al socket, senza fare l'include del codice di MySQL.

**Riassumendo:** se ci troviamo a scrivere un'applicazione commerciale
che sappiamo non verrà distribuita insieme al codice sorgente, dobbiamo
preoccuparci solo di utilizzare una libreria client che utilizzi il
metodo di connessione tramite socket al database.

C'è infine da aggiungere una cosa: se si utilizza codice opensource per
uso personale oppure interno alla propria azienda, senza distribuirlo in
giro, la GPL non ci impone di rilasciare le modifiche che abbiamo fatto
ai sorgenti GPL che stiamo utilizzando.

Il caso piu' lampante è quello di **Google**: essi utilizzano tonnellate
di codice GPL, però non distribuiscono un programma, offrono un
servizio. Questo gli permette di non dover rendere pubbliche le
modifiche fatte al codice originale.

*Credits: questo articolo è stato possibile in gran parte grazie
all'aiuto ed ai consigli di **Giovanni Bajo** (che pur chiedendomi di
specificare che non è un avvocato e che quindi potrebbe anche
sbagliarsi, ha senz'altro fatto un ottimo lavoro) .*
