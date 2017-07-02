Title: Utilizzare WordPress da remoto grazie a XML-RPC
Date: 2008-02-01 23:47
Author: admin
Category: Python, WordPress
Slug: utilizzare-wordpress-da-remoto-grazie-a-xml-rpc
Status: published

Come molti utenti WordPress avranno già notato, esistono svariati client
per poter gestire il proprio blog, che possono essere utilizzati invece
della normale gestione via web. Gestire WordPress da un client nativo o
comunque da remoto, è possibile grazie ad
[XML-RPC](http://codex.wordpress.org/XML-RPC_Support).Questo semplice
script Python vi mostrerà quanto sia semplice connettersi al proprio
blog ed invocare un metodo:

\[sourcecode language='python'\]  
from xmlrpclib import Server  
server = Server("http://www.andreagrandi.it/xmlrpc.php")  
userinfo = server.blogger.getUserInfo('','admin','password')  
print userinfo  
\[/sourcecode\]

vi stamperà a video le informazioni sul vostro utente (ovviamente
dovrete sostituire l'URL con quello del vostro blog e mettere gli user e
password corretti.
