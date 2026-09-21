<!-- OTTO · D1 — Grader deterministico — controlli in Python, nessun LLM -->
<!-- Versionare insieme al codice. Specifica dei controlli, non un prompt. -->
<!-- Nuovo, 4 settembre 2026 — post-mortem G01188. -->

# Che cosa fa

Gira su ogni `ParagrafoRedatto` e produce `MetricheParagrafo`. Undici degli
diciotto rilievi del post-mortem G01188 sono difetti che questo componente
intercetta prima della consegna: non richiedono giudizio, richiedono un
controllo.

I controlli in **grassetto** sono nuovi con la revisione del 4 settembre.

# Controlli sul singolo paragrafo

| Controllo | Come | Esito |
|---|---|---|
| Limiti formali | caratteri, pagine, sezioni contro `VincoliFormali` | blocco se superati |
| Leggibilita' | Gulpease, lunghezza media frasi, frasi oltre 35 parole | segnale, non blocco |
| Passivi | quota sul totale dei verbi | segnale sopra 0,20 |
| Affermazioni senza fonte | affermazioni qualificanti senza `fonte_id` | blocco sopra soglia |
| **Densita' di evidenza** | affermazioni qualificanti ancorate / totale | **blocco sotto 0,80** |
| **Modo prospettico** | regex su «deve essere», «dovra'», «occorre», «sara'», «verra'», «puo' essere», «potrebbe», «si prevede di» | **blocco sopra 3 occorrenze per paragrafo** |
| **Dubitativi su asset propri** | «appare», «risulta», «sembra», «dovrebbe» in frasi il cui soggetto e' un nostro asset | **blocco** |
| **Diminutivi su asset propri** | «mini», «piccolo», «semplice», «basilare» come qualificatori di nostri asset | **blocco** |
| **Glossario** | termini fuori dal glossario approvato (es. «human in the middle») | **blocco** |
| **Sigle normative** | ogni «ISO / UNI / EN / IEC / PAS + numero» confrontata con il registro delle norme esistenti | **blocco su sigla non trovata** |
| **Duplicazioni** | similarita' coseno fra blocchi, dentro il paragrafo e verso gli altri | **blocco sopra 0,85** |
| **Campi scheda vuoti** | per formati a schede, ogni campo obbligatorio deve essere pieno | **blocco** |
| **Circolarita' use case** | `distinto_dalla_proposta == False` | **blocco** |
| Segnaposto | presenza di `[[DATO:` | blocco in consegna |
| Coerenza numerica | stessa metrica con valori diversi fra paragrafi | blocco |
| Riferimenti economici | prezzi, sconti, corrispettivi nell'offerta tecnica | blocco |

# Controllo redazionale sul documento assemblato

Gira sul PDF/DOCX finale, non sul singolo paragrafo, prima del cancello 3:

- coerenza di copertina e intestazioni con l'oggetto della procedura e del lotto;
- presenza di nomi di altri lotti o di altre procedure nel testo;
- duplicazioni fra sezioni;
- ortografia;
- conteggio pagine sul PDF finale.

E' il gate che avrebbe intercettato la copertina della relazione del Lotto III,
che riportava «LOTTO III_Supporto alla cabina di regia…» seguito da «LOTTO
1_Assistenza sui servizi piu' diffusi…» — residuo di copia-incolla dal Lotto I,
in prima pagina, davanti a una commissione che confrontava otto offerte.

# Come si tara la densita' di evidenza

La soglia 0,80 non e' arbitraria. Nella relazione del Lotto I la sezione
Cybersicurezza — SOC con sette analisti di primo livello, remediation PCI-DSS a
7/14/30/90 giorni, tassonomia ACN e Determinazione 379907/2025, tre data center
in topologia triangolare, Greenbone/OpenVAS e Qualys, RTO/RPO/MTD documentati
nella BIA — ha preso l'85% del massimo, a sei punti percentuali dal vincitore.
Le sezioni A e B, scritte con descrizioni di prodotto in modo prospettico e
referenze narrate senza cifre, si sono fermate al 55%.

Stessa azienda, stesso documento, stessa commissione. Cambia solo la densita' di
evidenza. La taratura definitiva si fa sul set G01188, verificando che l'indice
riproduca l'ordine noto dei criteri: D 100%, G 85%, C 78%, E 76%, F 67%, A 56%,
B 55%.
