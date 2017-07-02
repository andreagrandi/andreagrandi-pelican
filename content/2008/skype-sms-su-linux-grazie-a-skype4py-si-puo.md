Title: Skype SMS su Linux: grazie a Skype4Py si puo'!
Date: 2008-05-11 17:56
Author: admin
Category: Linux, Programmazione, Python, Skype
Tags: API, Linux, Python, Skype, skype4py, sms
Slug: skype-sms-su-linux-grazie-a-skype4py-si-puo
Status: published

![Skype
Logo](http://www.andreagrandi.it/wp-content/uploads/2008/05/skype_logo.thumbnail.jpg)Il
client di **Skype** per Linux **non supporta** al momento l'**invio
degli SMS**. Questa puo' essere per molti una grossa limitazione, visto
che è molto conveniente come metodo per inviare gli sms (costano 10
centesimi) rispetto a molte tariffe in circolazione al momento, con i
principali gestori italiani.La mancanza di questa funzionalità è però
soltanto apparente! Infatti è stata già implementata a livello di
librerie di Skype ed è già disponibile tramite le API.

Grazie alla libreria
[**Skype4Py**](https://developer.skype.com/wiki/Skype4Py), ufficialmente
supportata da **Skype** e sviluppata da **Arkadiusz Wahlig** (che ha
tenuto un talk proprio su questo argomento nella giornata di ieri del
[PyCon](http://www.pycon.it) Due), è possibile scrivere applicazioni
multipiattaforma (Windows, Linux, Mac) che interagiscano con Skype.

Una volta installata la libreria nel proprio sistema, dobbiamo soltanto
avviare il client Skype.

Le applicazioni che possiamo scrivere, per automatizzare alcune funzioni
di Skype, sono moltissime. In questo caso particolare farò vedere un
piccolo script Python che invia un SMS utilizzando il client (ed il
credito) dell'istanza di Skype che sta girando sulla vostra macchina:

\[sourcecode language='python'\]  
import Skype4Py

number = '+393\*\*\*\*\*\*\*\*\*'  
text= 'Messaggio di prova da PySms4Skype!'

skype = Skype4Py.Skype()  
skype.FriendlyName = 'PySms4Skype'

skype.Attach()

sms = skype.CreateSms(Skype4Py.smsMessageTypeOutgoing, number)  
sms.Body = text  
sms.Send()  
\[/sourcecode\]

Quando eseguite questo script, Skype vi chiedera' la **conferma** per
autorizzare la vostra applicazione ad utilizzare le API, basterà quindi
dare conferma per continuare. Nello script ovviamente dovrete sostituire
il numero di telefono con uno valido.
