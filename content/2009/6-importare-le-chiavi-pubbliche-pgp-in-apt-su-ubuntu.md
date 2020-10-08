Title: Importare le chiavi pubbliche PGP in apt su Ubuntu
Date: 2009-02-14 22:48
Author: Andrea Grandi
Category: HowTo, Linux, Sicurezza, Ubuntu (IT)
Tags: apt, pgp, Ubuntu (EN)
Slug: importare-le-chiavi-pubbliche-pgp-in-apt-su-ubuntu
Status: published

![]({static}/images/2009/02/pg2logo.png "pg2logo")

Utilizzando i repository esterni su **Ubuntu**, capita spesso di non avere una
procedura automatica per importare anche le relative **chiavi pubbliche
PGP**, che ci permettono di avere la garanzia che i pacchetti che stiamo
scaricando siano autentici e che quindi provengano dall'autore
originale.

Sul sito web dei progetti che mettono a disposizione un repository,
solitamente è indicato anche l'ID della chiave pubblica PGP. Ad esempio
sul sito del *Blueman Development Team* troviamo **6B15AB91951DC1E2**.

Per importare questa chiave pubblica dentro apt di Ubuntu, sono
sufficienti i seguenti comandi da terminale:

    :::shell
    gpg --keyserver keyserver.ubuntu.com --recv 6B15AB91951DC1E2
    gpg --export --armor 6B15AB91951DC1E2 | sudo apt-key add -

Ovviamente dovrete sostituire l'ID della chiave PGP con quello che vi
interessa aggiungere. Qui di seguito potete vedere un esempio completo
dei messaggi di conferma che si ricevono quando si aggiunge la chiave:

    :::shell
    gpg --keyserver keyserver.ubuntu.com --recv 6B15AB91951DC1E2
        gpg: requesting key 951DC1E2 from hkp server keyserver.ubuntu.com
        gpg: key 951DC1E2: public key "Launchpad PPA for Blueman Development Team" imported
        gpg: Total number processed: 1
        gpg:               imported: 1  (RSA: 1) 
    gpg --export --armor 6B15AB91951DC1E2 | sudo apt-key add - OK
