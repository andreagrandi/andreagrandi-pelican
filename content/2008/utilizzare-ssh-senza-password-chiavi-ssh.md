Title: Utilizzare SSH senza password: chiavi SSH
Date: 2008-02-29 18:59
Author: Andrea Grandi
Category: HowTo
Tags: chiavi, connessione, Linux, openssh, password, Sicurezza, ssh, ssh2
Slug: utilizzare-ssh-senza-password-chiavi-ssh
Status: published

[![openssh\_logo]({filename}/images/2008/02/openssh_logo.thumbnail.png){ width=40% }]({filename}/images/2008/02/openssh_logo.thumbnail.png)

Quando vogliamo connetterci ad un server **SSH**, solitamente utilizziamo un
comando simile al seguente:

    :::shell
    ssh user@remotehost.com  

Una volta connessi ci viene richiesta la password di accesso e subito
dopo siamo connessi. Digitare ogni volta la password puo' essere
scomodo, ed in alcuni casi questo potrebbe addirittura impedirci di
creare uno script di automazione per velocizzare alcuni compiti.

Ci vengono in aiuto le **chiavi SSH**. Generando una coppia di chiavi
**pubblica/privata** di SSH sulla propria macchina, ed esportando la
chiave pubblica sul server remoto, possiamo fare in modo di autorizzare
la nostra chiave remota, facendo si che le connessioni successive
avvengano senza la richiesta di alcuna password.

Supponiamo (a scopo dimostrativo) che il server remoto si trovi
all'indirizzo IP **192.168.0.2** e supponiamo inoltre di avere un
account chiamato **user** sulla macchina remota.

Per prima cosa dobbiamo generare la coppia di chiavi sulla nostra
macchina locale (n.b: non utilizzo alcuna passphrase, altrimenti mi
verrebbe richiesta comunque al primo login di ogni sessione):

    :::shell
    andy80@noteboontu:~$ ssh-keygen -t dsa  
    Generating public/private dsa key pair.  
    Enter file in which to save the key (/home/andy80/.ssh/id_dsa):  
    Enter passphrase (empty for no passphrase):  
    Enter same passphrase again:  
    Your identification has been saved in /home/andy80/.ssh/id_dsa.  
    Your public key has been saved in /home/andy80/.ssh/id_dsa.pub.  
    The key fingerprint is:  
    22:99:69:d2:8d:8e:a5:f1:f4:dc:0f:d8:49:52:53:cd andy80@noteboontu  

A questo punto dobbiamo copiare la chiave pubblica appena generata, sul
server remoto:

    :::shell
    cd ~/.ssh/  
    scp id_dsa.pub user@192.168.0.2:./id_dsa.pub  

Ci verrà chiesta la nostra password remota, per poter effettuare la
copia del file. A questo punto dobbiamo connetterci via SSH al server
remoto:

    :::shell
    ssh user@192.168.0.2  

Quando abbiamo effettuato correttamente il login, dobbiamo procedere con
i seguenti comandi:

    :::shell
    cd .ssh  
    touch authorized_keys2  
    chmod 600 authorized_keys2  
    cat ../id_dsa.pub >> authorized_keys2  
    rm ../id_dsa.pub

Il gioco è fatto! Le successive connessioni SSH che effettueremo verso
il server remoto, avverranno senza la richiesta di alcuna password.
