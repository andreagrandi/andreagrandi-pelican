Title: Evitare che Wordpress modifichi il codice da copia-incollare
Date: 2009-02-14 23:51
Author: admin
Category: HowTo, WordPress
Tags: WordPress
Slug: evitare-che-wordpress-modifichi-il-codice-da-copia-incollare
Status: published

![](http://www.andreagrandi.it/wp-content/uploads/2008/02/wordpress-logo.jpg "wordpress_logo"){.alignright
.size-full .wp-image-19 width="134" height="134"}Il precedente post che
ho fatto mi aveva fatto veramente disperare. Come potete leggere dai
comandi, è necessario passare alcuni parametri utilizzando il doppio
trattino.

**Wordpress trasformava automaticamente il doppio trattino in un
trattino singolo**, facendo si che se qualcuno provava a fare il
**copia-incolla** di quel comando ricevesse un errore di sintassi dal
sistema.

Poco dopo aver risolto un po' alla peggio, mi sono imbattuto in [questo
utilissimo post](http://www.imbrandon.com/?p=97). In pratica si piega
**come evitare che Wordpress modifichi in automatico i caratteri**
all'interno dei blocchi di codice.

E' sufficiente modificare il file **functions.php** del tema Wordpress
che stiamo utilizzando ed aggiungere questa riga in fondo al file:

\[sourcecode language='php'\]  
<?php remove_filter('the_content', "wptexturize" ); ?>  
\[/sourcecode\]
