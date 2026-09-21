# OTTO

Sistema di agenti per la stesura dell'offerta tecnica di gara, per LUO. Il nome viene
da OT, offerta tecnica, e dall'orchestrazione che tiene insieme gli agenti. La mascotte
è un polpo: otto braccia che fanno otto cose insieme, e l'inchiostro con cui si scrive.

**Stato:** analisi chiusa, prototipo dimostrativo disponibile, sviluppo non avviato.
La revisione del 4 settembre recepisce il post-mortem della gara GSE G01188, che ha
fornito i primi dati reali su come una commissione italiana ha letto un'offerta LUO.

**Il punto di partenza:** ogni gara vive in un repository git dedicato. L'alberatura,
le convenzioni e la macchina a stati stanno in `docs/repo-gara.md`; lo scheletro pronto
da copiare in `template-gara/`.

## Da dove si comincia a leggere

| File | Cosa contiene | Per chi |
|---|---|---|
| `product.md` | Documento di prodotto: repo di gara, stati, cancelli e NBA, Knowledge Farm, copilota, confini | Chi decide |
| `docs/repo-gara.md` | Alberatura del fascicolo, naming, manifesto, macchina a stati, ciclo di vita degli artefatti | Chi lo costruisce |
| `docs/blueprint.md` | Architettura degli agenti, correzioni all'impianto, calibrazione, libreria prompt | Chi lo costruisce |
| `prototipo/otto-workspace.html` | Prototipo dimostrativo dell'interfaccia, su una gara inventata | Tutti |

## Alberatura

```
OTTO/
├── README.md              questo file
├── product.md             documento di prodotto
├── docs/
│   ├── blueprint.md       architettura, prompt, calibrazione
│   ├── blueprint.html     sorgente della pagina pubblicata — ferma al 2 settembre
│   └── repo-gara.md       il fascicolo di gara: alberatura e convenzioni
├── prompts/               un file per agente, versionati come codice
├── schema/models.py       contratti dati Pydantic fra gli agenti
├── template-gara/         scheletro da copiare per ogni nuova gara
├── brand/                 marchio, icona, logotipo, mascotte nei tre stati
└── prototipo/             prototipo HTML dell'interfaccia
```

## Gli agenti

| Prompt | Ruolo |
|---|---|
| `prompts/00-contratto-stile.md` | Regole di scrittura e antipattern, iniettati in architetto, redattore e collegio |
| `prompts/a-analista-gara.md` | Griglia dei criteri, tabellari con i livelli alla lettera, vincoli formali, scadenze |
| `prompts/t-checklist-tabellari.md` | Deterministico: incrocia i tabellari col registro certificazioni e blocca il cancello 1 |
| `prompts/b-architetto-ot.md` | Indice, formato dei paragrafi, budget di spazio, nota di posizionamento, schede |
| `prompts/c-redattore-paragrafo.md` | Scrive un paragrafo, o compila le schede se il criterio valuta per slot |
| `prompts/d1-grader-deterministico.md` | Controlli in Python: densità di evidenza, modo verbale, duplicazioni, sigle normative |
| `prompts/d-collegio-giudicante.md` | Tre commissari con profili distinti: rubrica, coefficiente atteso, dispersione |
| `prompts/e-triage-coordinatore.md` | Quali paragrafi riscrivere con il budget di giri rimasto |
| `prompts/f-pianificatore-gara.md` | Milestone a ritroso, impatto dei chiarimenti, lead time dei tabellari, alert |

I prompt si versionano come codice: cambiare un file sotto `prompts/` cambia il
comportamento del sistema, e la modifica va tracciata come una modifica di codice.

## Tre confini che non si spostano

Nessuna affermazione senza `fonte_id`: dove manca l'evidenza si emette una lacuna e un
segnaposto, mai un numero inventato. Nessun paragrafo si scrive prima che ogni elemento
tabellare abbia una decisione firmata, perché quei punti si vincono o si perdono prima
della scrittura. E OTTO non comunica con la stazione appaltante: chiarimenti,
sopralluogo, caricamento e trasmissione restano atti di una persona.

## La prossima cosa da fare

Calibrare il collegio su **G01188**, il primo set di validazione con etichette vere: 53
sub-criteri fra i due lotti, ciascuno con i coefficienti dei tre commissari riportati
singolarmente a verbale. Permette due misure invece di una — se il collegio prevede il
voto, e se riconosce l'evidenza fragile guardando la dispersione. Il fascicolo sta in
`nextcloud2/BIT/azienda/03. Projects/LUO/Gare/20260513 - GSE/esiti`.
