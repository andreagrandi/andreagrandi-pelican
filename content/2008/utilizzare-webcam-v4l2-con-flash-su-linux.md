Title: Utilizzare webcam V4L2 con Flash su Linux
Date: 2008-11-25 10:44
Author: admin
Category: HowTo, Linux
Tags: flash, V4L1, V4L2, webcam
Slug: utilizzare-webcam-v4l2-con-flash-su-linux
Status: published

![](http://www.andreagrandi.it/wp-content/uploads/2008/11/flash.png "flash"){.alignright .size-full .wp-image-174 width="134" height="130"}Introduzione
-------------------------------------------------------------------------------------------------------------------------------------------------------

Il supporto per le webcam su Linux non è mai stata una cosa molto
semplice. I motivi principali per cui le webcam non sono ben supportate
sono principalmente due: la **scarsa collaborazione dei produttori di
hardware**, che dovrebbero fornire almeno le specifiche a chi sviluppa i
driver per Linux e il quasi **completo disinteresse di chi scrive le
applicazioni** per l'utente finale (in particolare Microsoft con MSN e
Skype che utilizzano entrambi un protocollo proprietario e non
documentato).

Da diverso tempo si stanno diffondendo applicazioni scritte in **Flash**
che permettono di utilizzare la webcam: dalle videochat,
all'applicazione di
[**Youtube**](http://www.youtube.com/my_videos_quick_capture) che
permette di pubblicare un video registrandolo direttamente, fino ai
recenti servizi di streaming video come ad esempio
[**JustinTV**](http://www.justin.tv) e
[**UStream**](http://www.ustream.tv).

Il plugin Flash della Adobe, purtroppo ha iniziato a supportare le
webcam su Linux utilizzando il protocollo **V4L1** quando ormai la
maggior parte di esse funzionava solo con il nuovo protocollo **V4L2**.

A partire **dalla versione 10** di Flash, finalmente la Adobe ha
iniziato a supportare il protocollo V4L2, anche se il supporto non è
ancora completo. Modelli differenti di webcam infatti utilizzano
svariati formati di trasmissione video. Fortunatamente lo sviluppatore
che lavora per Adobe si è reso disponibile per ricevere il feedback da
parte degli utenti e per implementare questi formati in modo da
supportare il maggior numero possibile di webcam. Per chi volesse
contribuire è possibile seguire le istruzioni su questa pagina:
<http://blogs.adobe.com/penguin.swf/2008/07/paparazzi_v2_1.html>

gstfakevideo: un workaround per emulare V4L1
--------------------------------------------

Visto che il supporto per le webcam che utilizzano V4L1 è molto piu'
stabile, **l'ingegno della community Linux non è stato ad aspettare**
con le mani in mano. Il metodo utilizzato è basato su quello che veniva
usato su Skype per supportare un maggior numero di webcam: **in pratica
viene creato un device virtuale V4L1 sul quale viene redirezionato
l'output della webcam V4L2**.

Il [codice originale](http://code.google.com/p/gstfakevideo/) purtroppo
aveva bisogno di alcuni aggiustamenti, mi sono permesso quindi di
modificarlo e di applicarli. Potete trovare la nuova versione a questo
indirizzo:
<http://www.andreagrandi.it/download/gstfakevideo/gstfakevideo.tar.gz>

La compilazione non dovrebbe comportare particolari problemi: è
sufficiente eseguire **make** all'interno della cartella dei sorgenti.

Per testare il funzionamento della webcam è sufficiente esegurie lo
script che si trova all'interno della cartella. Verrà avviato **Firefox
con il supporto per le webcam V4L1**. Visitando uno dei siti web che
hanno un'applicazione Flash che utilizza la webcam citati all'inizio,
sara' possibile verificarne il corretto funzionamento.

***Riferimenti:** le istruzioni in questo post sono state in parte prese
da questo sito web (in inglese):
<http://www.jtolds.com/newsletter/2008/7/27/how-to-get-v4l2-devices-to-work-with-flash>*
