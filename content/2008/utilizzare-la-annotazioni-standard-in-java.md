Title: Utilizzare le annotazioni standard in Java
Date: 2008-07-10 00:26
Author: admin
Category: Java, Programmazione
Tags: annotazioni, compilatore, Java, jdk
Slug: utilizzare-la-annotazioni-standard-in-java
Status: published

![](http://www.andreagrandi.it/wp-content/uploads/2008/07/java_logo.jpg "java_logo"){.alignright
.size-full .wp-image-80 width="109" height="223"}Premetto di non aver
certo scoperto l'acqua calda, visto che si tratta di una feature di
**Java 5**. Pochi giorni fa mi sono imbattuto in una funzionalità di
Java che non avevo mai avuto modo di utilizzare. Si tratta della
annotazioni standard.

Grazie alla segnalazione di un amico ed al
[post](http://www.javalobby.org/java/forums/t17297) che mi ha passato,
ho potuto fare chiarezza su questo argomento.

Si tratta di tre annotazioni che possiamo utilizzare nel codice Java:
**@Deprecated**, **@Override**, **@SuppressWarnings**.

**@Deprecated:** come il nome ci suggerisce, se utilizzato prima della
definizione di un metodo o di una classe, fara' stampare un messaggio di
avviso al compilatore Java che ci avviserà che il metodo è appunto
obsoleto. Un esempio del suo utilizzo:

\[sourcecode language='java'\]  
// class  
@Deprecated  
public class SomeClass {

// field  
@Deprecated  
public int field;

// constructor  
@Deprecated  
public SomeClass() {

}

// method  
@Deprecated  
public void method() {

}  
}  
\[/sourcecode\]

**@Override:** si utilizza per avvisare esplicitamente il compilatore
che stiamo ridefinendo un metodo. Nel caso commettessimo un errore di
digitazione nel scrivere il nome del metodo, il compilatore ci
avviserebbe che nella classe padre non esiste un nome con quel metodo
che abbiamo specificato. Un esempio del suo utilizzo:

\[sourcecode language='java'\]  
public class MyClass {

// Won't compile - there is no toStirng method on java.lang.Object.  
@Override  
public String toStirng() {  
return "MyClass toString implementation";  
}  
}  
\[/sourcecode\]

**@SuppressWarnings:** quest'ultima notazione invece, viene utilizzata
per fare in modo che il compilatore "chiuda un occhio" su eventuali
warnings rilevati nel codice.
