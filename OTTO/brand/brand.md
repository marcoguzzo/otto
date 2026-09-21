# OTTO — identità visiva

## Il segno

Il marchio è un **fermaglio**. Tiene insieme e organizza: è il gesto che descrive quello
che OTTO fa a un fascicolo di gara — raccoglie disciplinare, capitolato, chiarimenti,
paragrafi, valutazioni e li tiene in un solo posto, in ordine, senza perderne nessuno.
È anche il segno che ogni ufficio gare riconosce senza spiegazioni.

La direzione arriva da un confronto fra sei proposte generate su ChatGPT a partire dal
brief di prodotto: il fermaglio ha vinto perché è l'unico che dice il mestiere senza
dover essere spiegato, e perché regge a 24 px dove le alternative più concettuali si
sciolgono.

Il disegno è un fermaglio vero, con la topologia giusta: un filo solo, quattro tratti
verticali e tre curve, spessore costante e terminali arrotondati. Inclinato di 25 gradi,
perché un fermaglio dritto sembra una graffetta da modulo e uno inclinato sembra usato.

## La mascotte

Otto è un personaggio che **porta il fermaglio addosso**, appuntato sul petto: la
mascotte non è il marchio con gli occhi, è qualcuno che quel marchio lo indossa. Tiene
un documento in una mano e ha tre espressioni, che nel prodotto non sono decorazione —
sono l'indicatore di salute della gara, agganciato al pianificatore.

| Stato | Quando | Colore |
|---|---|---|
| `sereno` | Nessun bloccante aperto, margine sul buffer positivo | Verde `#2F6141` |
| `attento` | Alert di livello attenzione, o margine dentro il buffer | Ambra `#B57A15` |
| `allarmato` | Alert bloccante o critico aperto | Rosso `#9C3323` |

`otto-mascotte.svg`, in blu inchiostro, è la versione neutra: si usa fuori dal prodotto —
presentazioni, documentazione, materiali — dove non c'è uno stato da dichiarare.

Otto non compare mai in un contesto in cui suggerirebbe che il sistema decide: non firma,
non spedisce, non prende il posto di una persona a un cancello.

## Colore

| Ruolo | Hex | Uso |
|---|---|---|
| Blu inchiostro | `#1B4B8F` | Colore primario: marchio, accento dell'interfaccia |
| Blu chiaro | `#3D74C4` | Dettagli e accento su fondo scuro (`#84B2E8`) |
| Carta | `#FBFBFA` | Occhi, superfici chiare, marchio in negativo |
| Inchiostro scuro | `#131C25` | Testo |
| Verde esito | `#2F6141` | Stato sereno, cancello attraversato |
| Ambra attenzione | `#B57A15` | Stato attento, alert non bloccanti |
| Rosso timbro | `#9C3323` | Stato allarmato, bloccanti, lacune aperte |

I tre colori di stato sono **riservati**: non si usano come colori decorativi né come
serie in un grafico, e viaggiano sempre con un'etichetta testuale, mai da soli.

## Tipografia

| Ruolo | Famiglia | Peso |
|---|---|---|
| Logotipo e numeri grandi | Archivo | 700 |
| Testo dell'interfaccia | IBM Plex Sans | 400 / 500 / 600 |
| Dati, percorsi, codici, ancore | IBM Plex Mono | 400 / 500 |

Il monospazio non è un vezzo: nel prodotto distingue a colpo d'occhio ciò che è
verificabile — un percorso di file, un id di Knowledge Farm, un'ancora di documento — da
ciò che è prosa.

## I file

| File | Quando si usa |
|---|---|
| `otto-mark.svg` | Marchio nudo, su fondo chiaro o scuro |
| `otto-icona.svg` | Tessera con angoli arrotondati: favicon, icona applicativa |
| `otto-logo.svg` | Logotipo orizzontale con payoff. Larghezza minima 180 px |
| `otto-mascotte.svg` | Mascotte neutra, blu inchiostro — fuori dal prodotto |
| `otto-mascotte-sereno.svg` · `-attento.svg` · `-allarmato.svg` | Mascotte a figura intera con badge di stato |
| `otto-badge.svg` e `otto-badge-<stato>.svg` | Solo testa, quadrata: è la versione per l'interfaccia, leggibile fino a 24 px |
| `prompt-immagini.md` | Il brief e i prompt usati per far proporre le direzioni ai modelli |

La regola è semplice: **sotto i 60 px si usa il badge, sopra la mascotte**. La figura
intera con documento e gambe smette di leggersi prima di quella soglia.

## Spazi di rispetto e limiti

Attorno al marchio si lascia uno spazio libero pari all'altezza dell'ansa grande. Il
marchio non si ruota oltre la sua inclinazione nativa, non si deforma, non si riempie di
gradienti e non cambia colore fuori dalla tavolozza — con l'unica eccezione dei tre stati
della mascotte, che il colore lo usano per dire qualcosa.

Il logotipo si compone, non si genera: marchio a sinistra alto quanto la "O" più il 40%,
spazio fra marchio e testo pari alla larghezza di una "O", payoff **OFFERTA TECNICA
ORCHESTRATA** in Archivo 500 al 20% del corpo, tracking +3, `#5A6976`.
