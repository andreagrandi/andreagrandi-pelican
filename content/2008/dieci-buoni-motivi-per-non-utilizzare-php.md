Title: Dieci buoni motivi per non utilizzare PHP
Date: 2008-10-09 14:08
Author: admin
Category: Programmazione
Tags: difetti, linguaggi, php, Programmazione
Slug: dieci-buoni-motivi-per-non-utilizzare-php
Status: published

![](http://www.andreagrandi.it/wp-content/uploads/2008/10/php-logo.jpg "php-logo"){.alignright
.size-full .wp-image-130 width="202" height="106"}Quando in questi
giorni ho appreso la triste notizia che il **progetto** da consegnare
per l'**esame** di **Laboratorio di Reti** avrebbe dovuto essere
realizzato in **PHP**, sono stato preso un po' dallo sconforto.

Per anni mi sono sempre rifiutato di imparare ed utilizzare questo
linguaggio ed ho persino declinato diverse offerte di lavoro, visto che
già sulla carta ne avevo sempre sentito parlare male. Adesso è arrivato
il momento di ingollare il rospo ed imparare almeno il minimo
indispensabile alla realizzazione del progetto.

Ho approfittato della situazione per documentarmi un po' sul PHP e per
ribadire alcuni motivi che per anni mi hanno tenuto lontano da questo
linguaggio. I punti che seguono prendono spunto sia da considerazioni
personali, sia da un [ottimo
articolo](http://www.bitstorm.org/edwin/en/php/) di **Edwin Martin**.

1. Ricorsione?! Chi era costei...
---------------------------------

La **[ricorsione](http://it.wikipedia.org/wiki/Ricorsione)**, come molti
di voi sapranno, è un meccanismo che permette ad una funzione di
chiamare se stessa. Viene impiegata nell'implementazione di moltissimi
algoritmi, come ad esempio il [**Quick
Sort**](http://it.wikipedia.org/wiki/Quick_sort). Se vengono generate
troppe chiamate ricorsive in PHP, il linguaggio va letteralmente in
palla e non funziona piu' correttamente. Questa cosa è stata [segnalata
come bug](http://bugs.php.net/bug.php?id=1901) e la motivazione che è
stata data dagli sviluppatori è che PHP utilizza lo stack al posto
dell'heap per le chiamate ricorsive. Questo cosa c'entra? Mi viene da
chiedere... eppure in altri linguaggi la ricorsione funziona benissimo!

2. Molti moduli PHP non sono thread safe
----------------------------------------

Anche se tutti i moduli del core di PHP sono garantiti **thread safe**,
la **maggior parte** degli altri moduli **non lo sono**. Questo rende
completamente inutile il fatto che Apache 2 supporti la modalità
multithreaded: gli sviluppatori di PHP
[sconsigliano](http://www.php.net/manual/en/install.unix.apache2.php)
pure di utilizzare questa versione di Apache.

3. PHP è azzoppato per motivi commerciali
-----------------------------------------

Vi sembra che **PHP** sia un po' **lento**? Non avete provato la
**versione commerciale** di **Zend PHP**, che garantisce maggiori
prestazioni! La versione gratuita di PHP infatti non ha alcuna
ottimizzazione e a meno di non utilizzare un qualche meccanismo di cache
(come ad esempio
[APC](http://pecl.php.net/package-info.php?package=APC)) le prestazioni
saranno basse.

4. Nessun supporto ai Namespace
-------------------------------

Se due moduli hanno una funzione che si chiama read, non possono essere
utilizzati contemporaneamente. Era stata proposta una soluzione a questo
problema in PHP5, ma alla fine [non è stata
inclusa](http://www.php.net/ChangeLog-5.php#5.0.0b2) nella release
definitiva. L'unico modo per evitare la collisione dei nomi dei metodi è
quello di nominarli aggiungendo il nome del modulo all'inizio. Ecco
perchè non è strano trovare metodi che ad esempio si chiamano
**xsl\_xsltprocessor\_transform\_to\_xml** che di sicuro non aumentano
la leggibilità del codice.

5. Caratteri di formattazione delle date non standard
-----------------------------------------------------

La maggior parte dei linguaggi di programmazione utilizza uno
[standard](http://unixhelp.ed.ac.uk/CGI/man-cgi?date) per quanto
riguarda i caratteri di formattazione delle date, che deriva da Unix e
dal linguaggio C. PHP utilizza un [proprio
formato](http://www.php.net/manual/en/function.date.php), completamente
incompatibile.

6. Inconsistenza nei nomi delle funzioni
----------------------------------------

Quando i nomi dei metodi contengono piu' di una parola, solitamente ci
sono tre modi diversi per poterli scrivere. Prendiamo ad esempio
un'ipotetica funzione che restituisce il numero dei file aperti.
Potremmo chiamarla **getnumberofopenfiles**,
**get\_number\_of\_open\_files** oppure **getNumberOfOpenFiles**.
**Quale** metodo utilizza **PHP**? **Tutti e tre** ovviamente! Oltre a
questo è opportuno far notare che i nomi dei metodi e delle funzioni
**non sono case sensitive**.

7. Assenza di un framework integrato
------------------------------------

Il modello piu' corretto per sviluppare un'applicazione web, sarebbe
quello chiamato **MVC**, dove la parte di **visualizzazione**, la
**business logic** e la validazione dei dati ed infine l'**interazione
con il database**, sono **parti separate** del progetto.

Nella maggior parte dei **siti scritti in PHP** è molto comune trovare
sorgenti che **includono tutti e tre questi aspetti in un unico file!**
Poche righe sopra viene fatta la connessione al database, poi c'è una
parte di visualizzazione di alcuni dati, verso la metà ci sono le
funzioni di validazione ed infine di nuovo altro codice html di
visualizzazione. Credo che questo sia il peggiore dei modi di realizzare
un'applicazione web. Pensate che sia facile per un grafico dover
apportare modifiche alla parte di visualizzazione senza toccare il
codice PHP? E viceversa... pensate che sia facile per un programmatore,
aggiungere codice PHP senza rischiare di scombinare il layout della
pagina?

Altri linguaggi con **Ruby** o **Python** ci hanno ormai abituati a
framework come [**Rails**](http://www.rubyonrails.org/) e
[**Django**](http://www.djangoproject.com/), rispettivamente. Per
fortuna le cose sono in miglioramento anche su PHP, grazie a framework
come [CakePHP](http://www.cakephp.org/) o
[Symfony](http://www.symfony-project.com/).

8. Mancanza del supporto Unicode
--------------------------------

Questa lacuna forse potra' non riguardarci da vicino, visto che il set
di caratteri che utilizziamo in Europa ed in America è ampiamente
supportato, ma non è certo così per **Cina**, **Giappone** ed altre
nazioni dove viene utilzzato un set di caratteri e di simboli molto
diverso dal nostro. Tramite
[**Unicode**](http://it.wikipedia.org/wiki/Unicode) è possibile
supportare anche questi caratteri. **PHP** avrà il **supporto per
Unicode** solo **nella futura versione 6**.

9. Lentezza
-----------

Pensate che il Java sia un linguaggio lento? Beh, niente a confronto di
PHP! Leggendo [questo
report](http://shootout.alioth.debian.org/debian/benchmark.php?test=all&lang=java&lang2=php)
si mettono in evidenza le scarse prestazioni di questo linguaggio.
Persino **Rasmus Lerdorf**, il creatore di PHP [ammette che non c'è modo
di migliorare le
prestazioni](http://www.sitepoint.com/blogs/2008/08/29/rasmus-lerdorf-php-frameworks-think-again/)
di PHP. Rasmus tra l'altro sconsiglia persino l'utilizzo dei frameworks
sopra citati (CakePHP e Symfony) perchè rallenterebbero inutilmente le
prestazioni dei siti web.

10. Estrema facilità di utilizzo
--------------------------------

Ammetto che questo ultimo punto **possa essere non condiviso da molte
persone**, si tratta infatti di una **mia personalissima opinione**. Il
fatto che un linguaggio di programmazione sia troppo facile da usare,
secondo me puo' presentare anche degli svantaggi. Permette infatti anche
a chi ha scarse conoscenze di programmazione, di cimentarsi in progetti,
con il rischio poi di far abbassare notevolmente la qualità del codice
che si trova in giro. Non è difficile infatti imbattersi in programmi
scritti in PHP che all'apparenza possono risultare gradevoli ed
accattivanti (magari perchè scritti da persone che principalmente si
occupano di web design), ma che sotto sotto sono dei veri e propri
pastoni di **codice mal scritto**.

Conclusioni
-----------

A favore di PHP possiamo sicuramente dire che si tratti di un linguaggio
**molto semplice da imparare** ed **ampiamente supportato** dalla
maggior parte dei **servizi di hosting** in tutto il mondo. A parte
queste due motivazioni però, non mi sentirei in alcun modo di
consigliarlo per sviluppare un'applicazione web.

Sicuramente qualcuno mi fara' notare che lo stesso blog sul quale sto
scrivendo è scritto in linguaggio PHP. Per l'utilizzo che ne devo fare,
Wordpress va piu' che bene, almeno per le mie esigenze. Questo non
toglie che PHP soffra ugualmente di tutti i problemi che sono stati
esposti sopra.

E' mia intenzione che questo articolo sia di avvertimento a chi si sta
per avvicinare per la prima volta al PHP o chi già lo utilizza. **Ci
tengo** però al fatto che **non contenga imprecisioni**, perchè credo
che servirebbero solo a screditare la natura stessa dell'articolo.
**Invito** quindi i lettori che rilevassero imprecisioni a
**segnalarmele**, indicandomi dove poter trovare maggiori informazioni
per verificare la validità di quanto riportato.
