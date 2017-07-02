Title: Un bug del Kernel Linux 2.6.27 potrebbe danneggiare le schede ethernet con driver e1000e
Date: 2008-09-24 21:36
Author: admin
Category: Linux, Sicurezza
Tags: bug, e1000e, kernel
Slug: un-bug-del-kernel-linux-2627-potrebbe-danneggiare-le-schede-ethernet-con-driver-e1000e
Status: published

[![](http://www.andreagrandi.it/wp-content/uploads/2008/09/ethernet.jpg "ethernet"){.alignright
.size-full .wp-image-119 width="130"
height="130"}](https://lists.ubuntu.com/archives/ubuntu-devel-announce/2008-September/000488.html)Secondo
quanto [riportato sulla mailing
list](https://lists.ubuntu.com/archives/ubuntu-devel-announce/2008-September/000488.html)
di sviluppo di Ubuntu, un **bug** presente nella versione **2.6.27** del
**kernel Linux** potrebbe **danneggiare irreparabilmente** le schede
ethernet dotate di chipset **Intel GigE** che utilizzano il driver
**e1000e**.

Secondo le prime analisi, il bug andrebbe a sovrascrivere la eprom di
queste schede di rete, rendendole inutilizzabili.

L'attuale alpha 6 di Ubuntu contiene questo bug, si consiglia quindi di
non utilizzarla se si possiede tale scheda, ma di attendere almeno la
prossima release (la beta dovrebbe uscire il 2 ottobre), dove il bug è
già stato corretto.
