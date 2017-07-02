Title: Applicazioni Ruby On Rails che non utilizzano database
Date: 2008-05-26 17:38
Author: admin
Category: Linux, Programmazione, Ruby, Ruby on Rails
Tags: activerecord, errore, MySQL, ror, Ruby, Ruby on Rails
Slug: applicazioni-ruby-on-rails-che-non-utilizzano-database
Status: published

Se a qualcuno fosse capitato di recente di creare una semplice
applicazione "*Hello World*" utilizzando il framework [**Ruby on
Rails**](http://www.rubyonrails.org), avrà notato che in fase di
esecuzione si ottiene un errore di questo tipo:

`Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)`

Perchè un errore relativo a **MySQL** in un'applicazione che stampa
semplicemente una stringa di testo? Nelle nuove versioni di **RoR**
vengono caricati per default i moduli **ActiveRecord**,
**ActiveResource** e **ActionMailer**. ActiveRecord in particolare si
aspetta di trovare (per le impostazioni di default) un database MySQL
funzionante.

Per evitare questo errore è sufficiente decommentare una riga
all'interno di environment.rb che si trova in
**\$PATH\_APPLICAZIONE/config/environment.rb**:

\[sourcecode language='ruby'\]  
\# Skip frameworks you're not going to use (only works if using
vendor/rails).  
\# To use Rails without a database, you must remove the Active Record
framework  
config.frameworks -= \[ :active\_record, :active\_resource,
:action\_mailer \]  
\[/sourcecode\]

*Fonte:*
<http://www.swards.net/2008/02/ruby-on-rails-application-with-no.html>
