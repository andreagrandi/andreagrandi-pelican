Title: Il crivello di Eratostene
Date: 2008-01-30 17:56
Author: Andrea Grandi
Category: Python
Tags: crivello, eratostene, numeri primi, Python
Slug: il-crivello-di-eratostene
Status: published

Questo codice Python di esempio, genera una lista di numeri primi che
vanno da 2 fino al numero passato come parametro.

    :::python
    def eratostene(x):  
        primi = range(3, x + 1, 2)  
        for i in primi:  
            if(pow(i, 2) > x):  
                break  
            for j in primi:  
                if(i != j) and (j % i == 0):  
                    primi.remove(j)  
                    primi.insert(0, 2)
        return primi  
