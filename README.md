# Wireless Com Scripts

La repository offre una serie di script in python che ho utilizzando durante lo svolgimento degli esercizi sulle reti Wireless
In particolare:
## Link Budget
Lo script permette di risolvere esercizi di Link Budget, (supporta attualmente solamente il modello in spazio libero <b>free-space</b>). Tramite input si possono inserire tutti i parametri necessari per il calcolo delle perdite di percorso e ottenere così distanza massima tra trasmettitore (tx) e ricevitore (rx) e capacità di canale tenendo conto di eventuali attenuazioni / guadagni.

## ErlangB
L'erlangB è una formula applicabile ai sistemi di tipo LCC (Lost Call Cleared). Fissata una probabilità di blocco <b>Pb</b> e un numero di canali **N** è possibile ottenere l'utilizzazione in erlangs ricorsivamente. Utilizzando la formula:
![{\displaystyle E_{B}(m,A)={A^{m} \over m!}\left({\sum _{i=0}^{m}{A^{i} \over i!}}\right)^{-1}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8bfc2007e5e115dd255d299b117f598f8761b20f)

## ErlangC
WIP

# Dispositivi compatibili
E' possibile utilizzare qualsiasi sistema Linux / Windows / OSX. 

E' possibile installare gli script su calcolatrice grafica **NumWorks** seguendo questi passaggi.

### NumWorks

 - Accedere a https://my.numworks.com/
 -  Assicurarsi di aver collegato la calcolatrice correttamente tramite USB (preferibilmente utilizzando il cavetto originale)
 - Recarsi su "I miei script"
 - Cliccare su "Nuovo script"
 - Aggiungere il titolo, descrizione e incollare il codice dello script (sfortunatamente non è possibile uploadare un intero file)
 - Salvare e cliccare su "Invia alla calcolatrice"
 - Nella sezione "Python" è possibile visualizzare gli script

**NB**: Il calcolo dell'ErlangB potrebbe risultare lento per un numero elevato di canali a causa delle prestazioni limitate del device, quindi è normale se lo script non fornisce l'output immediatamente.

 

 
