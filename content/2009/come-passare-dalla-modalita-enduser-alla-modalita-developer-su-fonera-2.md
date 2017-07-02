Title: Come passare dalla modalità enduser alla modalità developer su Fonera 2
Date: 2009-05-05 13:10
Author: admin
Category: HowTo, Linux, Recensione
Tags: fon, fonera, router, ssh
Slug: come-passare-dalla-modalita-enduser-alla-modalita-developer-su-fonera-2
Status: published

Fino ad ora, i possessori di [**Fonera 2.0**](http://www.fon.com) che
volevano passare alla modalità "**developer**" (e quindi avere anche
l'accesso via **SSH**) dovevano flashare la fonera con un'apposita
immagine, facendo uso del cavo seriale oppure della procedura con il
cavo di rete che utilizza Redboot.

Da oggi è disponibile un nuovo plugin che permette di passare
automaticamente alla modalità developer, basta andare (ad esempio) su
questa pagina del router:
**http://192.168.0.105/luci/fon\_devices/fon\_plugins**

La Fonera passerà a questo punto in modalità developer e dovremo
effettuare due reboot affinchè SSH sia attivato. Non dimenticatevi
ovviamente di aprire l'accesso SSH nella configurazione del firewall
della Fonera. Accedendo via SSH, vi troverete davanti questi messaggi:

\[sourcecode language="text"\]andy80@andy80-jaunty:\~\$ ssh
root@192.168.0.105  
The authenticity of host '192.168.0.105 (192.168.0.105)' can't be
established.  
RSA key fingerprint is e5:6e:fc:70:73:44:f6:cd:30:bd:ac:2d:53:d2:ab:a9.  
Are you sure you want to continue connecting (yes/no)? yes  
Warning: Permanently added '192.168.0.105' (RSA) to the list of known
hosts.  
root@192.168.0.105's password:

BusyBox v1.11.1 (2009-04-17 12:45:57 CEST) built-in shell (ash)  
Enter 'help' for a list of built-in commands.

\_\_  
\_.-\~ )  
\_..--\~\~\~\~,' ,-/ \_  
.-'. . . .' ,-',' ,' )  
,'. . . \_ ,--\~,-'\_\_..-' ,'  
,'. . . (@)' ---\~\~\~\~ ,'  
/. . . . '\~\~ ,-'  
/. . . . . ,-'  
; . . . . - . ,'  
: . . . . \_ /  
. . . . . \`-.:  
. . . ./ - . )  
. . . | \_\_\_\_\_..---..\_/ \_\_\_\_ Seal \_  
\~---\~\~\~\~----\~\~\~\~ \~\~

Flipper

-------- Fonera 2.0 Firmware (v2.2.5.0) -----------  
\* Based on OpenWrt - http://openwrt.org  
\* Powered by FON - http://www.fon.com  
----------------------------------------------------  
root@Fonera:\~\# uname -a  
Linux Fonera 2.6.26.2 \#9 Tue Apr 21 11:32:31 CEST 2009 mips unknown  
root@Fonera:\~\#\[/sourcecode\]

Cercherò prossimamente, nel caso ci sia interesse, di scrivere qualche
post piu' approfondito su questa nuova Fonera, in modo da mostrare le
caratteristiche di questo dispositivo.
