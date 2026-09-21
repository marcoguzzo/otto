<!-- OTTO · P0 — Contratto di stile — iniettato in B, C e D -->
<!-- Versionare insieme al codice: cambiare questo file cambia il comportamento del sistema. -->
<!-- Rev. 4 settembre 2026 — regole 3, 7, 11, 12 e l'antipattern "spiegare il noto" vengono dal post-mortem G01188. -->

# Contratto di stile — Offerta Tecnica

Chi legge è un commissario di gara che valuta da sei a dodici offerte in poche
settimane e cerca, per ogni criterio, la risposta a una domanda sola: questo
fornitore ha capito il mio problema e mi dimostra di saperlo risolvere?

## Regole di scrittura

1. Ogni affermazione e' verificabile. Porta un numero, una fonte, un riferimento
   contrattuale, una certificazione. Cio' che non e' verificabile si taglia.
2. Prima il bisogno della stazione appaltante come risulta dal capitolato, poi
   cosa facciamo, poi con quale metodo, poi con quale misura.
3. INDICATIVO PRESENTE. Si scrive cosa l'azienda ha e fa, mai cosa andrebbe fatto
   o cosa si fara'. Sono vietati: "deve essere", "dovra'", "occorre", "sara'",
   "verra'", "puo' essere", "potrebbe", "si prevede di", e ogni costruzione
   condizionale su cio' che offriamo. "Il connettore e' certificato nello Store",
   non "il collegamento puo' essere realizzato tramite un connettore
   certificato". La differenza fra le due frasi, su un criterio tabellare, e'
   tre punti.
4. Frasi affermative. Nessuna costruzione "non X ma Y".
5. Lunghezza media delle frasi fra 18 e 22 parole. Nessuna frase oltre 35 parole.
6. Voce attiva, con il soggetto che esegue: "il Service Manager valida il piano",
   mai "il piano viene validato".
7. Il lessico e' quello del capitolato. Se la stazione appaltante scrive "presa
   in carico", si scrive "presa in carico" e non "onboarding". Il lessico tecnico
   e' quello corretto: "human in the loop", non "human in the middle" — che non
   esiste, e assomiglia al nome di un attacco informatico.
8. Ogni paragrafo apre con la frase-tesi che risponde al criterio. Nessuna
   introduzione di contesto prima della risposta.
9. Acronimi sciolti alla prima occorrenza, poi usati.
10. Le tabelle portano dati, non elenchi di aggettivi. Ogni tabella ha una riga
    di didascalia che dice cosa il lettore deve concludere guardandola.
11. Un nome proprio di uno strumento nostro si usa solo se accompagnato da cosa
    e' costruito sopra, da quando e' in esercizio e presso quale committente. Un
    nome commerciale senza queste tre cose il commissario lo legge come
    un'etichetta su software di mercato, e ha ragione.
12. Sugli asset dell'azienda non si usano diminutivi ne' minimizzatori: "software
    factory", non "mini software factory". E non si usano verbi dubitativi: "i
    tre use case coprono i processi di Control Room", non "appaiono coerenti".

## Antipattern — rigetto automatico

- "soluzione all'avanguardia", "partner strategico", "approccio olistico",
  "know-how consolidato", "best practice di settore" senza indicare quale
- aggettivi valutativi sull'offerente: eccellente, leader, innovativo
- paragrafi che descrivono l'azienda invece del servizio richiesto
- promesse senza metrica: "elevata qualita'", "tempi rapidi", "massima attenzione"
- riformulazione del capitolato senza contenuto aggiunto
- SPIEGARE AL COMMITTENTE CIO' CHE IL COMMITTENTE GIA' POSSIEDE O CONOSCE: come
  funziona un protocollo pubblico, come funziona la piattaforma che la stazione
  appaltante ha comprato, cosa sia una metodologia nota. Ogni riga deve dire cosa
  facciamo noi. La didattica occupa spazio che vale punti e non ne porta.
- elenchi puntati di sostantivi senza verbo
- riferimenti a prezzi, sconti o corrispettivi: nell'offerta tecnica non entrano
