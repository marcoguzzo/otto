# OTTO — contratti dati fra gli agenti.
# Interfaccia del sistema: un agente che non riesce a riempire questi tipi
# sta fallendo in modo visibile, che e' l'unico modo accettabile di fallire.
#
# Revisione 4 settembre 2026 — post-mortem gara GSE G01188.
# Tre aggiunte strutturali: i tabellari diventano oggetti con i livelli
# testuali; il giudice diventa un collegio di tre e la dispersione e' un
# output; le schede a campi obbligatori sostituiscono la prosa dove il
# criterio valuta per slot.

from typing import Literal
from pydantic import BaseModel, Field

class Ancora(BaseModel):
    doc: str                       # "disciplinare.pdf"
    pagina: int
    articolo: str | None = None    # "art. 18.2, lett. c"

class Criterio(BaseModel):
    codice: str                    # "B.2"
    titolo: str
    punti_max: float
    tipo: Literal["discrezionale", "tabellare", "quantitativo"]
    criteri_motivazionali: str     # testo integrale, mai parafrasato
    metodo_attribuzione: str | None
    riparametrato: bool
    per_slot: int | None = None    # n. di slot valutati separatamente
                                   # ("Referenza n. 1, 2, 3"; "max 4 risorse").
                                   # Cambia il formato che il redattore produce.
    ancora: Ancora

# --- tabellari -------------------------------------------------------------
# Sul Lotto I della gara GSE, 4,00 punti su 12,97 di distacco dal vincitore
# venivano da due caselle tabellari. Nessuna delle due era una questione di
# scrittura: erano decisioni non prese, o prese senza sapere quanto costavano.

class LivelloTabellare(BaseModel):
    testo: str                     # integrale: "3 - connettore certificato nel
                                   # ServiceNow Store e supportato per almeno
                                   # le ultime 2 release"
    punti: float

class ElementoTabellare(BaseModel):
    codice: str                    # "a2"
    oggetto: str                   # cosa va dichiarato
    natura: Literal["possesso",             # si ha o non si ha
                    "dichiarazione",        # dato di fatto misurabile
                    "scelta_organizzativa"] # l'azienda delibera
    livelli: list[LivelloTabellare]         # tutti, alla lettera
    punti_max: float
    documento_probatorio: str | None        # cosa lo dimostra
    dicitura_richiesta: str | None          # stringa esatta (certificazioni)
    ancora: Ancora

class DecisioneTabellare(BaseModel):
    codice: str
    stato: Literal["posseduto", "non_posseduto",
                   "acquisibile_entro_termine", "da_deliberare"]
    livello_dichiarabile: str      # quale livello possiamo sostenere oggi
    punti_ottenuti: float
    punti_persi: float             # punti_max - punti_ottenuti
    evidenza_id: str | None        # asset KB che lo dimostra
    disallineamento: str | None    # dicitura posseduta != dicitura richiesta
    lead_time_giorni: int | None   # per acquisirlo, se acquisibile
    azione: str | None             # cosa fare per salire di livello
    decisione: str | None          # cosa si e' deciso
    approvata_da: str | None       # nome. Senza questo il cancello 1 non passa

class ChecklistTabellari(BaseModel):
    elementi: list[DecisioneTabellare]
    punti_in_gioco: float
    punti_rinunciati: float
    da_escalare: list[str]         # richiedono spesa o delibera
    bloccante: bool                # True finche' esiste una riga senza approvata_da

# --- bando -----------------------------------------------------------------

class VincoliFormali(BaseModel):
    pagine_max: int | None
    caratteri_max: int | None
    limiti_per_sezione: dict[str, int] = {}
    font: str | None
    corpo: str | None
    allegati_nel_conteggio: bool | None
    ancora: Ancora

class Ambiguita(BaseModel):
    citazione: str
    letture_alternative: list[str]
    domanda_per_chiarimenti: str
    ancora: Ancora

class BandoAnalizzato(BaseModel):
    oggetto: str
    stazione_appaltante: str
    criteri: list[Criterio]
    punteggio_tecnico_max: float
    soglia_sbarramento: float | None
    formula_economica: str | None
    vincoli: VincoliFormali
    requisiti_minimi: list[str]
    tabellari: list[ElementoTabellare]   # era list[str]: non bastava
    peso_tabellare: float                # somma punti T / punteggio tecnico max
    scadenze: dict[str, str]
    divieti: list[str]
    ambiguita: list[Ambiguita]
    mancanti: list[str]                  # cosa il corpus non contiene

# --- schede a campi obbligatori --------------------------------------------
# Dove il criterio assegna un punto per slot, la prosa continua vale meno
# della meta'. Sul Lotto I tre referenze da 1 punto hanno reso 1,56; sul
# Lotto III una risorsa descritta per soli aggettivi ha preso 0,43 su 1.

class SchedaReferenza(BaseModel):
    slot: str                      # "Referenza n. 1"
    committente: str
    periodo: str                   # "03/2021 - 06/2024"
    importo: str | None
    perimetro: str
    volumi: str                    # numeri, non aggettivi
    kpi_contrattuali: list[str]
    risultato_misurato: str        # esito, non attivita'
    trasferibilita: str            # perche' vale per questa stazione appaltante
    fonte_id: str

class SchedaProfilo(BaseModel):
    slot: str                      # "Risorsa n. 3"
    ruolo: str
    anni_esperienza: int
    committenti: list[str]
    volumi_governati: str
    certificazioni: list[str]
    cv_allegato: str               # riferimento all'allegato, obbligatorio
    fonte_id: str

class SchedaUseCase(BaseModel):
    slot: str
    committente: str               # mai "un servizio pubblico informativo"
    data_go_live: str
    problema: str
    soluzione: str
    baseline: str                  # il prima, con numeri
    risultato: str                 # il dopo, con numeri
    periodo_misurazione: str
    fonte_dato: str
    distinto_dalla_proposta: bool  # False = circolare, il grader blocca
    fonte_id: str

# --- scaletta e stesura ----------------------------------------------------

class SchedaParagrafo(BaseModel):
    id_par: str                    # "4.2"
    criterio: str                  # codice del criterio servito
    punti_max: float
    tesi: str                      # una frase, affermativa
    criteri_motivazionali_da_coprire: list[str]   # ordinati
    domanda_del_criterio: str      # la domanda a cui il paragrafo risponde,
                                   # in una riga. Il collegio ci misura la
                                   # copertura: un criterio che chiede quali
                                   # obiettivi sono stati raggiunti non e'
                                   # soddisfatto dall'elenco degli indicatori
                                   # che si misurerebbero.
    formato: Literal["prosa", "schede_referenza",
                     "schede_profilo", "schede_use_case",
                     "dichiarazione_tabellare"]
    n_slot: int | None             # se formato a schede
    evidenze_richieste: list[str]  # id di asset in knowledge base
    differenziatore: str | None
    metriche_obbligatorie: list[str]
    budget_caratteri: int
    tabelle_previste: int
    figure_previste: int
    da_evitare: list[str]
    lacune: list[str]              # evidenze che la KB non ha

class ScalettaOT(BaseModel):
    indice: list[SchedaParagrafo]
    vincoli_budget: list[str]
    saturazione_limite: float      # spazio allocato / limite.
                                   # Sotto 0.90 e' punteggio non preso.
    nota_posizionamento: str       # quali credenziali esibire per QUESTO lotto
    note_coerenza: list[str]

class Fonte(BaseModel):
    blocco: str
    fonte_id: str                  # id KB oppure ancora del capitolato
    affermazione: str

class ParagrafoRedatto(BaseModel):
    id_par: str
    testo: str
    schede: list[dict] = []        # SchedaReferenza/Profilo/UseCase serializzate
    fonti: list[Fonte]
    lacune: list[str]
    segnaposto: list[str]          # [[DATO: ...]] presenti nel testo
    caratteri: int
    copertura: dict[str, str]      # elemento motivazionale -> blocco

# --- grader deterministico (D1) --------------------------------------------

class MetricheParagrafo(BaseModel):
    id_par: str
    caratteri: int
    gulpease: float
    lunghezza_media_frasi: float
    frasi_oltre_35_parole: int
    quota_passivi: float
    densita_evidenza: float             # affermazioni qualificanti ancorate
                                        # sul totale. Soglia di consegna 0.80.
    occorrenze_prospettico: list[str]   # "deve essere", "occorre", "sara'",
                                        # "verra'", "puo' essere", "potrebbe"
    occorrenze_dubitative: list[str]    # "appare", "risulta", "sembra"
    occorrenze_diminutivi: list[str]    # "mini", "piccolo", "semplice"
    termini_fuori_glossario: list[str]  # es. "human in the middle"
    sigle_normative_non_verificate: list[str]   # es. "ISO 18195"
    duplicazioni: list[str]             # similarita' > 0.85 fra blocchi
    campi_scheda_vuoti: list[str]
    blocchi: list[str]                  # violazioni che impediscono la consegna

# --- collegio giudicante (D2) ----------------------------------------------
# Tre voci, non una. Nei verbali GSE i coefficienti dei tre commissari sono
# pubblicati uno per uno: sul sub-criterio c1 del Lotto III hanno dato
# 0,6 / 1,0 / 0,7 sullo stesso testo. La media nasconde il segnale;
# lo scarto lo espone.

class Livello(BaseModel):
    dimensione: str
    valore: int = Field(ge=0, le=4)
    citazioni: list[str]

class Intervento(BaseModel):
    testo_da_cambiare: str
    riformulazione: str
    dimensione: str
    punti_recuperabili: float

class VotoCommissario(BaseModel):
    profilo: Literal["tecnico", "operativo", "amministrativo"]
    livelli: list[Livello]
    coefficiente: float = Field(ge=0, le=1)
    verbale: str
    interventi: list[Intervento]
    blocchi: list[str]

class Valutazione(BaseModel):
    id_par: str
    voti: list[VotoCommissario]          # sempre tre
    coefficiente_atteso: float           # media
    dispersione: float                   # max - min.
                                         # Sopra 0.25 si riscrive comunque.
    causa_dispersione: str | None        # su quale dimensione divergono
    punti_a_rischio: float
    punti_a_rischio_da_fragilita: float  # punti_max * dispersione
    interventi: list[Intervento]         # uniti e riordinati
    verbale: str                         # sintesi delle tre motivazioni
    blocchi: list[str]                   # unione dei blocchi delle tre voci

# --- tempo di gara ---------------------------------------------------------

class Scadenza(BaseModel):
    codice: Literal["chiarimenti", "risposte_chiarimenti", "sopralluogo",
                    "presentazione", "apertura", "validita_offerta"]
    data: str                      # ISO 8601
    ora: str | None
    inderogabile: bool
    ancora: Ancora | None          # None = data ipotizzata, non estratta

class Milestone(BaseModel):
    codice: str                    # "chiusura_paragrafi", "decisione_tabellari"
    titolo: str
    scadenza_interna: str          # calcolata a ritroso dal termine
    dipende_da: list[str]
    owner: str
    su_percorso_critico: bool
    fuori_perimetro_gara: bool = False   # lead time industriale:
                                         # una certificazione che richiede otto
                                         # settimane non e' un ritardo di
                                         # progetto, e' una decisione che va
                                         # presa altrove.
    stato: Literal["aperta", "in_corso", "chiusa", "a_rischio"]

class PianoGara(BaseModel):
    scadenze: list[Scadenza]
    milestone: list[Milestone]
    buffer_caricamento_ore: float  # non comprimibile
    ore_residue: float
    lavoro_residuo_stimato_ore: float
    capienza: Literal["ampia", "stretta", "insufficiente"]
    percorso_critico: list[str]

class Alert(BaseModel):
    livello: Literal["informativo", "attenzione", "critico", "bloccante"]
    titolo: str                    # una riga, leggibile su notifica
    oggetto: str                   # id_par, codice criterio o milestone
    punti_in_gioco: float | None
    azione: str                    # eseguibile, non "monitorare"
    owner: str
    entro: str
    motivo_scatto: str             # quale cambio di stato lo ha generato

class ChiarimentoRegistrato(BaseModel):
    riferimento: str
    pubblicato_il: str
    tocca: list[str]               # codici criterio, vincoli o scadenze
    paragrafi_invalidati: list[str]

class AggiornamentoPiano(BaseModel):
    piano: PianoGara
    alert: list[Alert]
    chiarimenti: list[ChiarimentoRegistrato]
    da_tagliare: list[str]         # se capienza == "insufficiente"
    intoccabili: list[str]         # sbarramento o requisito minimo
    testata: list[str]             # tre righe per la testata del cruscotto
