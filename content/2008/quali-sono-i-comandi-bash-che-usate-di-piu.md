Title: Quali sono i comandi bash che usate di piu'?
Date: 2008-08-05 00:19
Author: admin
Category: Linux, Ubuntu (IT)
Tags: bash, Linux
Slug: quali-sono-i-comandi-bash-che-usate-di-piu
Status: published

Prendendo spunto da alcuni post apparsi sulla versione inglese di Planet
Ubuntu, ho deciso di provare questo comando:

` history | awk '{a[$2]++ } END{for(i in a){print a[i] " " i}}' | sort -rn | head`

che dovrebbe stampare la lista dei comandi piu' digitati nella bash
della vostra macchina Linux. Il risultato è stato il seguente:

` andy80@noteboontu:~$ history | awk '{a[$2]++ } END{for(i in a){print a[i] " " i}}' | sort -rn | head 89 vim 70 cd 50 ruby 41 ls 29 sudo 25 su 20 rails 16 mc 14 cat 11 telnet`

interessante, non trovate?!
