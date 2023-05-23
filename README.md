# Cosmo-II

Ciao bellaggente!
 In questo repo ho messo quello che ho combinato ce soir. In pratica ci sono i risultati dell'integrazione dell'orizzonte visibile di particella per 150 valori di omega k distribuiti seconda una gaussiana (con valore medio -0.011 e stddev 0.013).
 I files sono in binario! Per leggerli basta integrare questa roba in python https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html in python.  Occhio che appunto sono in binario non txt!
 Nei files ci sono i valori numerici, sono salvati in ordine, sicché significa che al primo valore di d_VH corrisponde il primo valore di O_k e di d_PH e così via. Per maneggiarli quindi potrebbe essere comodo caricare i dati da file in un array numpy.
Trovate anche il programmino in python che ho usato per integrare (l'ho un po' velocizzato).
 Ci sono anche degli istogrammi delle varie distribuzioni
