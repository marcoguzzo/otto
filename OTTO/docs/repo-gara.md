# Il repository di gara — alberatura e convenzioni

*Ogni procedura vive in un repository git dedicato. Questo documento definisce come è
fatto, come si chiama, cosa entra in ogni cartella e chi la riempie. Lo scheletro
pronto da copiare sta in `template-gara/`.*

---

## Perché un repo per gara

Un'offerta tecnica è un documento con conseguenze giuridiche, e la domanda che gli si
farà fra sei mesi è sempre la stessa: perché dice questo, da quale versione del
disciplinare nasce, su quale evidenza si regge, chi lo ha firmato. Git risponde a tutte
e quattro senza che si debba costruire niente — contenuto indirizzato per hash, storia
completa, diff, tag.

Un repo per gara e non un monorepo, perché i cicli di vita sono indipendenti: una gara
si apre, si chiude e si archivia intera; una gara sotto NDA ha permessi propri; e il
diritto di accesso al fascicolo di una procedura non implica quello alle altre.

---

## Nome del repository

    gara-<AAAAMMGG>-<ente-slug>-<id-procedura>

`AAAAMMGG` è la data del termine di presentazione, che è l'unica data che tutti
ricordano. Lo slug dell'ente è minuscolo e senza spazi. L'id della procedura è quello
della stazione appaltante — CIG, numero di gara, riferimento RFQ.

    gara-20260513-gse-g01188
    gara-20261015-aslba-cup-2026
    gara-20260930-windtre-rfq10050

La cartella su disco porta lo stesso nome. La corrispondenza con la vecchia convenzione
Nextcloud (`LUO/Gare/20260513 - GSE/`) si tiene in `gara.yaml`, campo
`archivio_precedente`, finché la migrazione non è completa.

---

## Alberatura

```
gara-20260513-gse-g01188/
├── gara.yaml                    manifesto: identità, stato, owner, riservatezza
├── README.md                    scheda leggibile, rigenerata dal manifesto
│
├── 00-fonte/                    IMMUTABILE — nessun file qui si modifica, mai
│   ├── disciplinare.pdf
│   ├── capitolato-tecnico.pdf
│   ├── allegati/
│   ├── chiarimenti/             001-20260420.pdf, 002-20260428.pdf …
│   └── MANIFEST.sha256          cosa è stato scaricato, quando, con quale hash
│
├── 01-analisi/
│   ├── corpus.jsonl             output dell'ingest, un frammento per articolo
│   ├── bando-analizzato.json     BandoAnalizzato
│   ├── griglia-criteri.md        vista umana — si firma al cancello 1
│   ├── tabellari.md              ChecklistTabellari: livelli, decisione, costo in punti
│   └── bid-no-bid.md             decisione di partecipazione, con motivazione
│
├── 02-impianto/
│   ├── scaletta.json             ScalettaOT
│   ├── schede/                   4.2.json … una SchedaParagrafo per file
│   ├── posizionamento.md         nota di posizionamento — si firma al cancello 2
│   └── evidenze.md               asset Knowledge Farm selezionati, lacune iniziali
│
├── 03-offerta/
│   ├── paragrafi/                4.2.md … è qui che si scrive
│   ├── metriche/                 4.2.json — output del grader deterministico
│   ├── valutazioni/              4.2.giro-1.json — tre voci del collegio + dispersione
│   ├── lacune.md                 coda aperta, con owner e domanda esatta
│   └── build/                    offerta assemblata, DOCX/PDF
│
├── 04-consegna/
│   ├── depositato/               copia bit-a-bit di ciò che è stato caricato
│   ├── ricevute/                 ricevute della piattaforma telematica
│   └── checklist-consegna.md     firme, formati, dimensioni, marche temporali
│
├── 05-esito/
│   ├── verbali/                  verbali di gara pubblicati
│   ├── punteggi.json             coefficienti per sub-criterio, nostri e dei concorrenti
│   ├── graduatoria.md
│   └── post-mortem.md            scarto previsto/reale, rilievi, regole derivate
│
└── .otto/                        stato della macchina — non si edita a mano
    ├── stato.json                macchina a stati e storia delle transizioni
    ├── piano.json                PianoGara: milestone, percorso critico, buffer
    ├── alert.jsonl               storico degli alert, uno per riga
    └── run/                      log per nodo del grafo, un file per esecuzione
```

---

## Le regole che la tengono in piedi

**Le cartelle numerate sono le fasi.** L'ordine alfabetico coincide con l'ordine del
tempo, quindi chi apre il repo capisce dove si trova il lavoro guardando quale cartella
è piena. Una cartella vuota porta un `.gitkeep`, così l'alberatura è sempre completa.

**`00-fonte/` è immutabile.** Un documento di gara non si modifica, non si rinomina, non
si converte sul posto. Il `MANIFEST.sha256` registra nome, hash e data di acquisizione
di ogni file; una rettifica o un chiarimento entra come file nuovo, numerato e datato,
dentro `chiarimenti/`. Il pianificatore legge quella cartella a ogni esecuzione e
confronta i chiarimenti con la griglia: è così che un chiarimento che ridefinisce un
sub-criterio diventa un alert bloccante invece di una scoperta tardiva.

**JSON per la macchina, Markdown per la firma.** Ogni artefatto tipizzato è un JSON
conforme ai modelli in `schema/models.py`. Dove serve che una persona legga e firmi —
griglia dei criteri, tabellari, posizionamento — accanto al JSON vive una vista Markdown
rigenerabile. Il JSON è la verità; il Markdown si rigenera e non si edita a mano.

**Ogni cancello è un tag git.**

| Tag | Quando | Cosa attesta |
|---|---|---|
| `gate-1-griglia` | Fine analisi | Griglia, scadenze e decisioni sui tabellari validate |
| `gate-2-impianto` | Fine impianto | Scaletta, budget di spazio e posizionamento approvati |
| `gate-3-firma` | Prima del deposito | Offerta completa, zero segnaposto, vincoli formali verificati |
| `depositata` | Dopo il caricamento | Ricevuta acquisita |

Il diff fra `gate-2-impianto` e `depositata` è la storia della stesura, e si legge senza
chiedere niente a nessuno.

**Un commit per evento.** Un chiarimento acquisito, una decisione su un tabellare con il
suo costo in punti, un giro di riscrittura, una lacuna chiusa. Il messaggio dice cosa è
successo e chi lo ha deciso; gli agenti committano come `otto[bot]` con il nodo del
grafo nel trailer, così una modifica automatica si distingue sempre da una umana.

**`05-esito/` non è archivio, è il set di calibrazione.** Senza i coefficienti reali per
sub-criterio il collegio giudicante produce numeri plausibili e il loop di riscrittura
ottimizza verso un bersaglio immaginario. Regola operativa: **una gara non passa in
`chiusa` finché `post-mortem.md` non è scritto**, e il post-mortem si chiude elencando
quali rilievi diventano regole nei prompt o vincoli nello schema.

---

## Il manifesto `gara.yaml`

È l'unico file che si edita a mano all'apertura, ed è la fonte da cui `README.md` si
rigenera.

```yaml
id: gara-20260513-gse-g01188
oggetto: "Servizi di contact center e back office — Lotti I e III"
stazione_appaltante: "Gestore dei Servizi Energetici S.p.A."
riferimento: "G01188"
cig: "…"
importo_base: 4820000.00
lotti: [I, III]

criterio: OEPV                 # OEPV | prezzo | qualita
punteggio_tecnico_max: 70
punteggio_economico_max: 30
soglia_sbarramento: 40         # null se non prevista

stato: chiusa                  # vedi macchina a stati
owner: "…"                     # responsabile di gara
firmatario: "…"                # chi firma al cancello 3

riservatezza: interna          # pubblica | interna | nda
instradamento_modelli: cloud   # cloud | self-hosted  (nda => self-hosted)

piattaforma: "Portale Acquisti GSE"
buffer_caricamento_ore: 6      # non comprimibile

archivio_precedente: "LUO/Gare/20260513 - GSE"
```

`riservatezza: nda` impone `instradamento_modelli: self-hosted` e rende il repo privato:
è un vincolo verificato all'apertura, non una raccomandazione.

---

## La macchina a stati

```
individuata → in valutazione → in analisi → in impianto → in stesura
            → in revisione → depositata → in commissione → esito → chiusa
                                   ↘ sospesa        ↘ abbandonata
```

| Stato | Chi lavora | Uscita |
|---|---|---|
| `individuata` | Responsabile di gara | `00-fonte/` completo, hash registrati |
| `in valutazione` | Commerciale + responsabile | `bid-no-bid.md` firmato |
| `in analisi` | Ingest, analista, checklist tabellari | **`gate-1-griglia`** |
| `in impianto` | Architetto + commerciale | **`gate-2-impianto`** |
| `in stesura` | Redattore, grader, collegio | Zero segnaposto, densità sopra soglia |
| `in revisione` | Assemblatore, revisione redazionale | **`gate-3-firma`** |
| `depositata` | Persona sul portale | Ricevuta acquisita |
| `in commissione` | Nessuno — il pianificatore sorveglia | Verbali pubblicati |
| `esito` | Responsabile di gara | `post-mortem.md` scritto |
| `chiusa` | — | Regole derivate versionate nei prompt |

Le transizioni le scrive il grafo in `.otto/stato.json`, con timestamp e attore. Nessuna
transizione avviene senza il suo evento: un cancello si attraversa quando esiste il tag,
non quando qualcuno cambia un campo.

`sospesa` e `abbandonata` richiedono una motivazione nel manifesto, perché la ragione per
cui non si è partecipato è informazione commerciale che serve l'anno dopo.

---

## Aprire una gara nuova

```bash
# 1. scheletro
cp -R OTTO/template-gara gara-20261015-aslba-cup-2026
cd gara-20261015-aslba-cup-2026 && git init

# 2. manifesto
$EDITOR gara.yaml          # identità, criterio, riservatezza, piattaforma, buffer

# 3. documenti di gara — si scaricano, non si toccano
cp ~/Downloads/disciplinare.pdf 00-fonte/
shasum -a 256 00-fonte/**/*.pdf > 00-fonte/MANIFEST.sha256

git add -A && git commit -m "apertura gara: ASL BA — CUP e servizi al cittadino"
```

Da qui il repo è pronto: bitloop lo riceve come contesto di lavoro e il pianificatore
comincia a contare.

---

## Ciclo di vita degli artefatti

| Artefatto | Lo produce | Lo consuma | Si firma |
|---|---|---|---|
| `00-fonte/MANIFEST.sha256` | Responsabile di gara | Chiunque debba provare cosa c'era | no |
| `01-analisi/corpus.jsonl` | Ingest | Analista, copilota | no |
| `01-analisi/bando-analizzato.json` | Analista | Architetto, pianificatore | no |
| `01-analisi/griglia-criteri.md` | Analista, vista rigenerata | Cancello 1 | **sì** |
| `01-analisi/tabellari.md` | Checklist tabellari | Cancello 1, redattore | **sì** |
| `02-impianto/scaletta.json` | Architetto | Redattore, pianificatore | no |
| `02-impianto/posizionamento.md` | Architetto + commerciale | Cancello 2 | **sì** |
| `03-offerta/paragrafi/*.md` | Redattore | Grader, collegio, assemblatore | no |
| `03-offerta/valutazioni/*.json` | Collegio giudicante | Triage, cruscotto | no |
| `03-offerta/lacune.md` | Redattore | Coda NBA, team | no |
| `04-consegna/checklist-consegna.md` | Assemblatore | Cancello 3 | **sì** |
| `05-esito/punteggi.json` | Responsabile di gara | Calibrazione del collegio | no |
| `05-esito/post-mortem.md` | Responsabile + commerciale | Prompt e schema della gara dopo | **sì** |

---

## Riservatezza e conservazione

Un repo con `riservatezza: nda` è privato, instrada i modelli su self-hosted e non
esporta niente verso servizi esterni, copilota compreso. La marcatura sta nel manifesto
perché deve essere leggibile da una macchina prima che da una persona.

I fascicoli si conservano per la durata della prescrizione applicabile alla procedura e
per tutta la vita del contratto eventualmente aggiudicato. `00-fonte/` e `04-consegna/`
sono le due cartelle che non si potano mai: la prima prova cosa chiedeva la stazione
appaltante, la seconda cosa è stato effettivamente consegnato.
