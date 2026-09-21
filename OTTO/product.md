# OTTO — documento di prodotto

*Versione 0.1 — 4 settembre 2026. Stato: prototipo dimostrativo. Il blueprint
architetturale sta in `docs/blueprint.md`, l'alberatura del fascicolo in
`docs/repo-gara.md`, il prototipo in `prototipo/otto-workspace.html`.*

---

## Ogni gara è un repository

Questa è la scelta che determina tutto il resto, quindi va detta per prima: **ogni
procedura vive in un repository git dedicato**, con la sua alberatura, la sua storia e i
suoi permessi. Non una cartella dentro un archivio condiviso, non righe in un
gestionale: un repo, uno per gara, che nasce quando la gara viene individuata e si
chiude quando il post-mortem è scritto.

La ragione è di sostanza. Un'offerta tecnica è un documento con conseguenze giuridiche:
può essere impugnata, può finire davanti a un TAR, e a distanza di mesi qualcuno deve
poter ricostruire perché il paragrafo 4.2 dice quello che dice, da quale versione del
disciplinare nasce, quale evidenza aziendale lo sostiene e chi lo ha firmato. Git fa
esattamente questo mestiere: contenuto immutabile indirizzato per hash, storia
completa, differenze fra due momenti, firme. Il fascicolo di gara diventa allora
l'artefatto centrale del prodotto, e OTTO è ciò che lo riempie.

Da questa scelta discendono tre proprietà che nessuna alternativa offre. La **prova**:
i documenti di gara scaricati restano bit-a-bit quelli scaricati, con un manifest di
hash, e la rettifica della stazione appaltante arriva come file nuovo e datato invece
di sostituire il precedente. L'**isolamento**: una gara sotto NDA è un repo privato con
i suoi permessi e il suo instradamento dei modelli, senza che questo condizioni le
altre. La **chiusura del ciclo**: gli esiti — verbali, coefficienti per sub-criterio,
scarto fra punteggio previsto e punteggio reale — vivono nello stesso repo del testo che
li ha prodotti, ed è questo che rende possibile calibrare il collegio giudicante invece
di sperare che indovini.

---

## Che cosa è OTTO

OTTO porta una gara dai documenti pubblicati dalla stazione appaltante fino all'offerta
tecnica firmata, e poi fino all'analisi di quello che è successo. Cinque agenti LLM —
analista, architetto, redattore, collegio giudicante, pianificatore — e quattro
componenti deterministici — ingest, checklist dei tabellari, grader di vincoli e
metriche, assemblatore — lavorano dentro un grafo di orchestrazione che si ferma in tre
punti dove una persona firma.

Il nome viene da OT, offerta tecnica, e dall'orchestrazione che tiene insieme gli
agenti. La mascotte è un polpo: otto braccia che fanno otto cose insieme, e l'inchiostro
con cui si scrive.

L'architettura degli agenti, i prompt e i contratti dati stanno nel blueprint. Questo
documento descrive il **prodotto**: come si presenta a chi lo usa, dove vivono i dati,
quali superfici esistono e quali confini non si attraversano.

---

## Chi lo usa, e cosa cambia per loro

Il **responsabile di gara** apre il fascicolo la mattina e vede la coda delle azioni,
non lo stato. Firma ai tre cancelli, decide sui tabellari, risponde alle lacune. Prima
teneva il piano in testa e le scadenze su un foglio; ora il piano è nel repo e le
scadenze sono nella barra.

Il **redattore di offerta** riceve schede eseguibili invece di una cartella di PDF, e
riceve la valutazione del collegio prima della commissione invece che dopo. Il suo
lavoro si sposta dalla produzione di prosa alla decisione su quale evidenza portare.

Il **responsabile commerciale** entra al cancello 2, dove si decide dove si spendono le
pagine e quale storia racconta l'offerta, e nel post-mortem, dove si legge quanto è
costata ogni scelta.

La **direzione** guarda la vista d'ufficio: quante gare aperte, quali stanno scivolando,
qual è il punteggio tecnico atteso su ciascuna. È la vista che esiste perché il
pianificatore è multi-gara per costruzione.

---

## Il fascicolo di gara

L'alberatura completa, con le convenzioni di naming e il ciclo di vita di ogni file,
sta in `docs/repo-gara.md`. Qui contano le quattro regole che la tengono in piedi.

**Le cartelle numerate sono le fasi, e l'ordine alfabetico è l'ordine del tempo.** Da
`00-fonte/` a `05-esito/` si legge il processo senza doverlo spiegare. Chi apre il repo
per la prima volta capisce dove si trova il lavoro guardando quale cartella è piena.

**`00-fonte/` è immutabile.** Nessuno modifica un documento di gara, mai. Un
`MANIFEST.sha256` registra cosa è stato scaricato e quando; un chiarimento o una
rettifica entra come file nuovo, numerato e datato, dentro `00-fonte/chiarimenti/`. Il
pianificatore legge quella cartella per capire se un chiarimento invalida lavoro già
fatto.

**JSON per la macchina, Markdown per la firma.** Ogni artefatto tipizzato — la griglia
dei criteri, la scaletta, le valutazioni — vive come JSON conforme ai modelli in
`schema/models.py`, e ha una vista Markdown dove serve che una persona legga e firmi. Il
JSON è la verità, il Markdown è la vista: rigenerarlo è sempre possibile, editarlo a
mano non serve a niente.

**Ogni cancello è un tag git.** `gate-1-griglia`, `gate-2-impianto`, `gate-3-firma`,
`depositata`. Il diff fra `gate-2-impianto` e `depositata` è la storia della stesura,
leggibile senza chiedere niente a nessuno. Un chiarimento è un commit; una decisione su
un tabellare è un commit con dentro il costo in punti.

---

## Gli stati, e la barra che li mostra

Una gara attraversa dieci stati, più due uscite laterali. La barra orizzontale in testa
al workspace li mostra tutti, sempre, e ogni stato è navigabile: cliccarlo apre la vista
di quella fase, anche a fase conclusa, perché tornare indietro a leggere come è stata
decisa una cosa è metà del lavoro.

| Stato | Cosa succede | Come si esce |
|---|---|---|
| `individuata` | Il repo nasce, `00-fonte/` si popola | Documenti completi e hash registrati |
| `in valutazione` | Bid / no-bid | Decisione firmata in `01-analisi/bid-no-bid.md` |
| `in analisi` | Ingest, analista, checklist tabellari | **Cancello 1** — griglia, scadenze e tabellari validati |
| `in impianto` | Architetto: indice, budget, schede | **Cancello 2** — scaletta e posizionamento approvati |
| `in stesura` | Redattore, grader, collegio, riscritture | Nessun segnaposto aperto, densità sopra soglia |
| `in revisione` | Assemblatore e revisione redazionale | **Cancello 3** — firma |
| `depositata` | Caricata sulla piattaforma, ricevuta acquisita | Ricevuta in `04-consegna/ricevute/` |
| `in commissione` | Attesa | Pubblicazione dei verbali |
| `esito` | Verbali e punteggi caricati | Post-mortem scritto |
| `chiusa` | Le regole derivate sono versionate nei prompt | — |

`sospesa` e `abbandonata` sono le due uscite laterali, e portano la motivazione con sé.

La barra è **agganciata al pianificatore**: sotto lo stato corrente mostra le scadenze
vive con il countdown al netto del buffer di caricamento, e il badge di Otto cambia
colore con la salute della gara — sereno, attento, allarmato. Cliccando il badge si apre
il copilota già in contesto sul piano, così la domanda «perché sono in giallo» ha una
risposta invece di un'occhiata.

---

## Come bitloop esegue la gara

bitloop è il motore: Pydantic AI per l'agent loop e gli output tipizzati, LiteLLM come
gateway dei modelli, MCP per gli strumenti. Gli agenti di OTTO sono **ingestati in
bitloop come definizioni versionate** — un file di prompt sotto `prompts/`, un tipo di
output in `schema/models.py`, un nodo nel grafo — e bitloop li esegue contro il repo
della gara passato come contesto di lavoro.

Il gateway serve tre cose concrete. Le tre voci del collegio girano su modelli diversi
da quello del redattore, altrimenti il testo si valuta da solo. Una gara marcata
riservata nel manifesto viene instradata su modelli self-hosted sull'infrastruttura
bit-brain senza che il codice se ne accorga. E il costo per gara è misurabile per nodo,
il che serve quando si deve dire se OTTO conviene.

Il coordinatore resta codice: un grafo `pydantic_graph` con stato persistito in
`.otto/stato.json`, ripartenza da qualunque nodo e log per nodo in `.otto/run/`. Nessun
LLM decide quale agente chiamare.

---

## Cancelli, avvisi e next best action

Il cruscotto non mostra lo stato: mostra **la prossima cosa da fare**. Lo stato è quello
che si deduce quando la coda è corta.

Le Next Best Action sono una coda unica alimentata da quattro sorgenti che nel sistema
esistono già separate: gli **interventi** proposti dal collegio, ciascuno con i punti
recuperabili stimati; gli **alert** del pianificatore, con il loro livello; le
**decisioni sui tabellari** ancora aperte, con il costo in punti di ogni livello; le
**lacune** dichiarate dal redattore, con la domanda esatta da girare al team.

L'ordinamento è la parte che conta, e segue questa precedenza:

1. Tutto ciò che è **bloccante** — segnaposto aperti, vincolo formale superato,
   tabellare non deciso, chiarimento che invalida testo già scritto. Non ha prezzo:
   senza, l'offerta non è presentabile.
2. Ciò che avvicina alla **soglia di sbarramento**, quando il punteggio tecnico stimato
   è sotto.
3. Il resto per **punti recuperabili per ora di lavoro**, che è l'unica metrica onesta
   quando il tempo è la risorsa scarsa.
4. A parità, la **scadenza più vicina**.

Ogni azione porta con sé cosa fare, perché conta (i punti in gioco), chi la deve fare,
entro quando, e da quale agente viene la proposta. Un'azione senza proprietario non
entra in coda, e «monitorare la situazione» non è un'azione.

I **cancelli** vivono nella stessa coda, con un trattamento visivo distinto: sono le
uniche voci che fermano il flusso, e mostrano chi deve firmare. Un cancello aperto da
più di ventiquattr'ore alza un avviso, perché il modo tipico in cui un cancello
fallisce è che nessuno sa che tocca a lui.

---

## Knowledge Farm: da dove viene l'evidenza

Knowledge Farm è la RAG di BIT, ed è la fonte di tutto ciò che OTTO afferma. Il
collegamento è architetturale, non accessorio: il redattore può citare **solo** ciò che
risolve a un `fonte_id` di Knowledge Farm o a un'ancora del capitolato, e dove l'evidenza
manca emette una lacuna con un segnaposto invece di un numero inventato.

OTTO parla con Knowledge Farm attraverso strumenti MCP — `kf_search`, `kf_get`,
`kf_cita` — e le usa in quattro momenti. L'**architetto** interroga l'inventario per
capire quali referenze esistono prima di promettere un paragrafo. Il **redattore**
recupera gli asset che la scheda gli assegna e ne cita i campi. La **checklist dei
tabellari** interroga il registro delle certificazioni, perché una casella tabellare si
vince dimostrando un possesso e la domanda «ce l'abbiamo?» ha una risposta documentale.
Il **copilota** cerca lì quando la domanda esce dal fascicolo.

Il flusso torna indietro, ed è la parte che rende OTTO un sistema che migliora. Alla
chiusura di una gara, `05-esito/` alimenta Knowledge Farm: i verbali con i coefficienti
per sub-criterio, i paragrafi che hanno preso il punteggio pieno con il testo del
criterio che li ha premiati, il post-mortem con i rilievi verificati. La gara successiva
parte da un archivio più ricco, e il collegio giudicante ha più etichette vere su cui
calibrarsi.

---

## Il copilota del fascicolo

Ogni fascicolo ha un assistente che risponde su quel fascicolo e su Knowledge Farm.
Serve a domande che oggi costano mezz'ora di scorrimento di PDF: «dove dice che il
sopralluogo è obbligatorio», «quali referenze abbiamo su CUP sanitario negli ultimi tre
anni», «cosa cambia il chiarimento 3 rispetto al criterio B.2», «perché il collegio ha
dato 0,6 sul c1». Ogni risposta porta l'ancora — documento, pagina, articolo — o l'id
dell'asset di Knowledge Farm, e senza ancora la risposta non si dà.

Il copilota **legge e non scrive**. Non modifica paragrafi, non decide tabellari, non
avanza stati. La ragione è la tracciabilità: se il testo dell'offerta potesse essere
modificato da una conversazione, la catena che lega ogni affermazione alla sua scheda,
alla sua evidenza e alla sua valutazione si spezzerebbe al primo «sistemami questo
paragrafo». Le modifiche passano dalla pipeline, che le registra.

---

## Le quattro viste del workspace

Il prodotto ha una sola pagina e quattro zone, ed è così che il prototipo la mostra.

**In testa**, l'identità della gara e la barra degli stati con le scadenze vive: si
capisce dove si è e quanto manca senza cliccare niente.

**A sinistra**, il fascicolo navigabile: l'albero del repo con i badge di stato per
cartella. È il modo in cui una persona verifica con i propri occhi che il documento
citato esiste davvero.

**Al centro**, la vista della fase corrente. In stesura è la griglia dei criteri con
punti a rischio, coefficiente atteso e dispersione del collegio; su un file selezionato è
il contenuto, con le fonti evidenziate.

**A destra**, la coda delle azioni e i cancelli. È la zona che si guarda per prima e che
determina cosa succede oggi.

Il copilota apre da un pannello a comparsa, sopra tutto, con il contesto già impostato su
ciò che si sta guardando.

---

## Che cosa OTTO non fa

**Non comunica con la stazione appaltante.** Richieste di chiarimenti, prenotazione del
sopralluogo, caricamento e trasmissione dell'offerta sono atti dell'operatore economico
con effetti giuridici, e restano azioni di una persona sul portale. OTTO li mette in
scadenza, li ricorda, prepara i testi. Non li invia.

**Non decide i tabellari.** Un tabellare è una decisione aziendale con un prezzo in
punti — dichiarare una quota di smart working, impegnarsi su una certificazione — e la
prende una persona al cancello 1. OTTO la mette in evidenza con il suo costo, la registra
firmata, e la trascrive nella dichiarazione senza sfumarla.

**Non inventa evidenza.** Dove la Knowledge Farm non ha l'asset, esce una lacuna e un
segnaposto, e la consegna resta bloccata. Un numero inventato in un'offerta pubblica è
una dichiarazione non veritiera, con esclusione e segnalazione ANAC.

**Non firma.** I tre cancelli sono passaggi umani. La responsabilità del contenuto resta
integralmente dell'operatore economico, e questo vale anche là dove l'uso dell'AI è
pacificamente legittimo: il TAR Lazio, con la sentenza n. 4546 del 3 marzo 2025, ha
stabilito che l'impiego dell'intelligenza artificiale non rende di per sé l'offerta
aleatoria e non impone alcun obbligo di dichiararlo.

---

## Stato: prototipo dimostrativo

Quello che esiste oggi è `prototipo/otto-workspace.html`: una pagina HTML autonoma che
mostra le quattro viste, la barra degli stati, la coda delle NBA, la navigazione del
fascicolo e il copilota, su una **gara dimostrativa costruita apposta**. I dati sono
inventati e la pagina lo dichiara: serve a decidere la forma del prodotto prima di
scrivere il backend, non a gestire una gara vera.

Quello che il prototipo non ha, e che va costruito nell'ordine: l'ingest ancorato e il
primo nucleo di Knowledge Farm; l'analista con il cancello 1 e la checklist dei
tabellari; architetto e redattore su un singolo sub-criterio; il collegio con la
calibrazione su G01188; e infine il grafo, il pianificatore e il cruscotto vero.

---

## Decisioni aperte

| Decisione | Perché blocca |
|---|---|
| **Dove vivono i repo**: GitLab self-hosted su bit-brain, GitHub privato, o git nudo su Nextcloud | Determina permessi, CI e come il copilota accede al fascicolo |
| **Perimetro**: solo procedure pubbliche con disciplinare, o anche RFQ private | Una RFQ privata non pubblica criteri motivazionali e richiede un analista costruito diversamente |
| **Una gara o l'ufficio gare**: workspace su singola procedura o vista su tutte | Condiziona da subito come si modella lo stato |
| **Dove arrivano gli alert**: email, Teams, Slack o solo cruscotto | Determina se il pianificatore invia o si limita a esporre |
| **Knowledge Farm**: cosa ci si mette per prima, e chi la cura | È il tetto di qualità di tutto il resto |
| **Chi presidia i cancelli**: responsabile di gara attuale o figura nuova LuoLab | Senza un ruolo assegnato i cancelli diventano ostacoli e vengono aggirati |
| **Gara pilota** | Serve una procedura con scadenza abbastanza lontana da tollerare un pilota |
