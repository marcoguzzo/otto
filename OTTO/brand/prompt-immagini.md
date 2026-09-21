# OTTO — prompt per far proporre marchio e mascotte

L'idea di questo prompt: non dettare il concetto, ma raccontare il progetto e chiedere
al modello di proporre lui la direzione visiva, spiegando perché. Lo stile resta libero
— dei vincoli si danno solo quelli tecnici, che servono a ottenere un marchio invece di
un'illustrazione.

Si lancia identico su Gemini, ChatGPT e Grok. Tre letture diverse dello stesso progetto
sono già di per sé il primo confronto utile.

---

## Prompt — da incollare

```
Sei un direttore creativo specializzato in identità visiva per prodotti software B2B.
Ti do il brief di un progetto. Voglio che sia tu a decidere che cosa rappresentare.

═══ BRIEF ═══

CHE COS'È OTTO
OTTO è un sistema di agenti AI che scrive l'offerta tecnica delle gare d'appalto
pubbliche italiane. Lo usa LUO, un'azienda di contact center e BPO che si sta
trasformando in fornitore di servizi digitali.

COME FUNZIONA
Legge il disciplinare e il capitolato pubblicati dall'ente appaltante ed estrae la
griglia dei criteri di valutazione, i punteggi e le scadenze. Costruisce l'impianto
dell'offerta decidendo quanto spazio dare a ogni criterio in base ai punti che vale.
Scrive i paragrafi uno per uno. Li fa valutare da un collegio di tre commissari
simulati, che prevedono il punteggio prima della commissione vera. Un pianificatore
tiene il tempo: programma a ritroso dal termine di presentazione e avvisa quando
qualcosa sta scivolando.

Cinque agenti lavorano in parallelo sullo stesso fascicolo, coordinati da un programma
deterministico. Ogni gara vive in un archivio con la sua storia completa: si può sempre
ricostruire perché un paragrafo dice quello che dice e chi lo ha approvato.

IL NOME
OTTO viene da OT — offerta tecnica — e dall'orchestrazione che tiene insieme gli agenti.
In italiano "otto" è anche il numero 8.

I CONFINI, CHE SONO PARTE DELL'IDENTITÀ
Non inventa: ogni affermazione dell'offerta deve avere una fonte verificabile, e dove
l'evidenza manca il sistema si ferma invece di riempire il vuoto. Non firma: in tre
punti del percorso una persona deve approvare e il flusso si blocca fino ad allora. Non
comunica con l'ente: caricare l'offerta, prenotare il sopralluogo e chiedere chiarimenti
restano atti di una persona.

CHI LO USA
Il responsabile di gara, che decide e firma. Il redattore dell'offerta, che scrive. La
direzione, che guarda quante gare sono aperte e quali stanno scivolando. Il contesto è
quello degli appalti pubblici italiani: scadenze con valore legale, documenti che
possono finire davanti a un giudice amministrativo, punteggi assegnati da una
commissione.

COSA DEVE SENTIRE CHI GUARDA
Precisione, affidabilità, tempo sotto controllo, un collega competente che non si
distrae. Non magia, non futuro, non potenza di calcolo.

═══ COSA TI CHIEDO ═══

1. Leggi il brief e proponimi TRE direzioni concettuali per il marchio, una riga
   ciascuna: che cosa rappresenta e perché è pertinente a OTTO in particolare, non a un
   software qualsiasi. Non generare ancora immagini.

2. Scegli quella che difenderesti davanti al cliente e spiega in tre righe perché batte
   le altre due.

3. Genera l'ICONA DI PROGETTO su quella direzione: il segno che vive nella barra del
   titolo, nella favicon e sull'icona applicativa.

4. Genera la MASCOTTE, coerente con la stessa direzione: la figura che nel prodotto fa
   da indicatore di salute della gara e da volto dell'assistente che risponde alle
   domande. Deve poter assumere tre stati riconoscibili — tutto in ordine, attenzione,
   problema bloccante — quindi serve qualcosa che possa cambiare espressione o postura.

Lo stile lo scegli tu. Non ti do riferimenti né palette: voglio vedere che cosa ti
suggerisce il progetto.

═══ VINCOLI TECNICI — questi sì, non negoziabili ═══

- Nessun testo, lettera o numero dentro le immagini.
- Sfondo bianco pieno. Soggetto unico, centrato, senza scena né oggetti di contorno.
- Icona quadrata 1:1. Mascotte verticale 4:5.
- L'icona deve restare leggibile a 24 pixel e reggere la riduzione a un solo colore
  pieno. Se il segno vive solo grazie a sfumature o dettagli sottili, è sbagliato.
- Evita i segni che ogni prodotto AI usa da tre anni: cervelli, circuiti stampati, reti
  neurali, robot umanoidi, ingranaggi, sfere luminose, mani che si sfiorano, gradienti
  viola-blu.
```

---

## Secondo giro — dopo che ha generato

```
Ora genera anche le altre due direzioni che avevi proposto: icona e mascotte per
ciascuna, stesso trattamento e stessi vincoli. Poi mettile a confronto in tre righe —
quale regge meglio a 24 pixel, quale si ricorda di più a distanza di un'ora, quale
rischia di somigliare a qualcos'altro di già visto.
```

---

## Note per i tre modelli

**ChatGPT e Gemini** — si incolla tutto in un messaggio solo. Se partono a generare
saltando il ragionamento, basta un «fermati, prima le tre direzioni scritte».

**Grok** — tende a generare subito e a saltare i passaggi. Conviene spezzare: prima il
brief fino al punto 2, si aspettano le tre direzioni scritte, poi «genera icona e
mascotte sulla direzione che hai scelto, rispettando i vincoli tecnici».

Su tutti e tre: quattro varianti per immagine, e per correggere si rilancia il vincitore
(`stesso segno, tratto più spesso, più aria fra gli elementi`) invece di rigenerare da
capo, altrimenti la coerenza si perde a ogni giro.

---

## Come si sceglie, dopo

Tre prove, in quest'ordine.

**A 24 px.** Riduci ogni candidato alla dimensione in cui vivrà per il novanta per cento
del tempo. Quello che sparisce è fuori, per quanto bello sia grande.

**A un colore.** Riduci a un solo riempimento pieno. Se il segno non si legge, si rifà —
non si aggiusta con un secondo colore.

**Ad alta voce.** Fallo vedere a qualcuno del team senza dire cosa rappresenta e chiedi
cosa vede. Se la risposta non è il concetto, il concetto non è passato.

---

## Dopo la scelta

L'output dei modelli è raster. Per arrivare all'asset: scontorna, vettorizza (Illustrator
Image Trace a 6 colori, oppure vectorizer.ai), riduci a pochi colori piatti.

Il logotipo non si fa generare — i modelli sbagliano le lettere. Si compone a mano: il
marchio a sinistra, alto quanto la "O" più il 40%; lo spazio fra marchio e testo pari
alla larghezza di una "O"; il payoff sotto, corpo al 20% del logotipo.
