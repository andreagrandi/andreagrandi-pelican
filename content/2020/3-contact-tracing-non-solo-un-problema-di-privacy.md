Title: Contact Tracing: non e' solo un problema di privacy o di sicurezza
Date: 2020-04-20 19:30
Author: Andrea Grandi
Category: Privacy
Tags: privacy, trasparenza, immuni, app, contact, tracing, covid, covid19
Slug: contact-tracing-non-solo-un-problema-di-privacy
Status: draft

## Contact Tracing in Italia

Negli ultimi giorni non si fa che parlare di **Immuni**, la app che il Governo Italiano avrebbe scelto, come soluzione di **contact tracing** per il **COVID-19**, e vengono sollevati molti dubbi (si va da quelli legittimi a quelli che rasentano il complottismo) al riguardo.

Per "contact tracing" si intende una soluzione che, mediante l'uso della tecnologia, ci permetta di creare una traccia di tutti i nostri contatti e fare in modo che quando uno di essi dichiarera' di essere positivo al COVID-19, le persone che sono entrate in contatto con lui/lei ricevano una notifica.

Prima che proseguiate nella lettura, mi sento in dovere di fare **una doverosa premessa**: da oltre 20 anni mi occupo di sviluppo software ed ho esperienza di utilizzo di svariate tecnologie anche in ambiti in cui di solito e' l'uomo a prendere una decisione. La cosa piu' importante pero' e' che **non sono ne' un virologo, ne' un epidemiologo, ne' un medico**. Mi limitero' quindi ad un'analisi dei fatti, rimanendo nell'ambito delle mie competenze.

La mia personale opinione (tuttavia irrilevante) e' che una soluzione tecnologica possa essere di aiuto nelle prossime fasi della pandemia, ma dovra' essere accompagnata da un'accurata verifica manuale dei risultati.

## I dubbi al momento

I maggiori dubbi al momento riguardando **l'efficacia** della soluzione scelta, la **sicurezza** dei dati sensibili che verranno raccolti e quelli sulla **privacy** delle persone.

Ritengo tutti questi punti molto importanti, ma sono dell'idea che prima di tutto questo si debba fare un punto sulla **trasparenza**.

### Il Governo e la task force

Alcune settimane fa il Governo ha annunciato la creazione di una [task force di tecnici](https://innovazione.gov.it/DM-task-force/), che avrebbe dovuto produrre un report con suggerimenti e linee guida, in modo che il governo potesse effettuare una scelta ragionata. Molti di questi nomi sono noti a chi e' del settore (ne conosco personalmente alcuni) e ritengo personalmente che fosse un ottimo punto di partenza.

Il problema pero' e' che **l'intera task force e' stata messa sotto Non Disclosure Agreement**, che tradotto in termini semplici significa che a nessuno di loro e' permesso di rilasciare commenti o dichiarazioni in pubblico, ne' di rivelare alcuna informazione su quanto prodotto.

### Il report della task force

Il **report**, ad oggi, **non e' stato reso pubblico**: in che modo possiamo valutare i criteri utilizzati per scegliere la soluzione, se non ci e' permesso di leggere il report? 

Come facciamo a verificare **che il Governo abbia effettivamente seguito le indicazioni** dei tecnici o se abbia preferito fare di testa propria? 

### La soluzione scelta: quali criteri?

Al momento non esiste un "white paper" che ci descriva la soluzione proposta e adottata. In base a **quali criteri** e' stata scelta proprio questa soluzione?

### Quali conseguenze dopo una notifica?

Supponiamo di ricevere una notifica che ci avvisa che il giorno X siamo stati per un certo periodo di tempo vicini ad un'altra persona che si e' poi dichiarata positiva. Quale sara' la diretta conseguenza?

- A) Qualcuno verra' a farci un tampone di verifica il prima possibile
- B) Ci verra' imposto un periodo di quarantena senza alcuna verifica
- C) Potremo ignorare la notifica

Se le conseguenze di questa importante notifica non vengono stabilite a priori, molti non vorranno rischiare di essere costretti in casa, magari per un falso negativo. 

**Nota**: le possibilita' di un falso positivo sono davvero molte. Basandosi sul raggio di azione del Bluetooth, in teoria potremmo essere a 1 metro di distanza da una persona infetta, ma essere nella stanza accanto (e quindi in totale sicurezza). Oppure potremmo passare accanto ad una persona infetta mentre siamo in macchina con il finestrino chiuso. Per non parlare poi degli operatori sanitari: in alcuni casi, loro hanno la certezza di trovarsi nei paraggi di persone infette. Verrebbero considerati infetti anche loro? E quando la sera tornano a casa dai loro coniugi e familiari, sarebbero anche essi considerati positivi dalla app?

### Closed Source

Nonostante le raccomandazioni della commissione Europea, pare che il codice sorgente della app non sara' pubblico (ma verra' rilasciato solo al Governo Italiano). Questo significa che non sara' possibile un controllo da parte di terze parti, e non ci sara' alcuna garanzia su quello che la app possa fare con i nostri dati (ne' sara' facile scovare e segnalare bug di sicurezza).

## Conclusioni

Qualsiasi strada si decida di prendere, e' fondamentale che il processo decisionale che ha portato a tale scelta sia quanto piu' **trasparente** possibile. Solo in questo modo si potra' ottenere la fiducia del maggior numero di persone e cercare di raggiungere l'effetto desiderato. Per il momento, tutta questa trasparenza non c'e' stata.
