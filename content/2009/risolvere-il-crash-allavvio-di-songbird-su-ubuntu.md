Title: Risolvere il crash all'avvio di Songbird su Ubuntu
Date: 2009-06-24 16:00
Author: admin
Category: HowTo, Linux, Ubuntu (IT)
Tags: crash, libvisual, nvidia, songbird, Ubuntu (EN)
Slug: risolvere-il-crash-allavvio-di-songbird-su-ubuntu
Status: published

****![songbird\_screenshot\_0](http://www.andreagrandi.it/wp-content/uploads/2009/06/songbird_screenshot_0.jpg "songbird_screenshot_0"){.alignright
.size-full .wp-image-283 width="197" height="136"}****Se si prova a far
girare la versione di **Songbird** scaricabile [dal sito
ufficiale](http://getsongbird.com) su **Ubuntu** (ma il problema sembra
riguardare anche altre distribuzioni visto che si tratta di un bug del
driver Nvidia) si otterrà quasi sicuramente un crash dell'applicazione
stessa.

Per risolvere il problema è sufficiente disinstallare un plugin
(**libvisual-0.4-plugins**) utilizzando il seguente comando: **sudo
apt-get remove **libvisual-0.4-plugins****

Una nota negativa: questo bug è presente fin dalla versione 8.10 di
Ubuntu... che aspettano a correggerlo invece di far ricorrere gli utenti
a questi trucchetti?
