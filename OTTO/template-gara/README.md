# <oggetto della gara>

> Scheda rigenerata da `gara.yaml`. Non editare a mano.

| | |
|---|---|
| Stazione appaltante | — |
| Riferimento / CIG | — |
| Termine di presentazione | — |
| Stato | `individuata` |
| Responsabile | — |
| Riservatezza | `interna` |

## Dove sta cosa

- `00-fonte/` — documenti di gara, **immutabili**. Hash in `MANIFEST.sha256`.
- `01-analisi/` — corpus ancorato, griglia dei criteri, tabellari, bid/no-bid.
- `02-impianto/` — scaletta, schede di paragrafo, nota di posizionamento.
- `03-offerta/` — paragrafi, metriche, valutazioni del collegio, lacune, build.
- `04-consegna/` — ciò che è stato caricato e le ricevute.
- `05-esito/` — verbali, punteggi reali, post-mortem.
- `.otto/` — stato della macchina. Non si edita a mano.

## Regole

1. Nessun file di `00-fonte/` si modifica. Rettifiche e chiarimenti entrano come file
   nuovi, numerati e datati, in `00-fonte/chiarimenti/`.
2. Ogni cancello è un tag: `gate-1-griglia`, `gate-2-impianto`, `gate-3-firma`,
   `depositata`.
3. La gara non passa in `chiusa` finché `05-esito/post-mortem.md` non è scritto.
