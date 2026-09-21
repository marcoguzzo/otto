# CAPITOLATO TECNICO DI GARA
**Servizi Applicativi, Manutenzione Evolutiva e Soluzioni di Intelligenza Artificiale per la Pubblica Amministrazione**
*CIG: A09F823B12 — CUP: J59I24000120001*

---

## 1. REQUISITI ED ARCHITETTURA DI SISTEMA
[Doc: Capitolato | Pagina: 4 | Articolo: 1.1]
L'aggiudicatario dovrà realizzare ed erogare un'infrastruttura software modulare basata su architettura a microservizi integrata con moduli di AI Generativa e Agenti Cognitivi.

### 1.1 Specifiche Tecniche Obbligatorie
- **Interfacce Applicative:** Esposizione di API conformi alle Linee Guida di Interoperabilità AgID (RESTful e OpenAPI 3.0+).
- **Orchestrazione Multi-Agente:** Implementazione di workflow agenziali per l'estrazione dati, l'analisi automatica delle gare, la generazione di report e la verifica di conformità.
- **Ambiente di Esecuzione:** Deploy su infrastruttura Cloud qualificata ACN (Agenzia per la Cybersicurezza Nazionale) in conformità con la strategia Cloud Italia.

---

## 2. REQUISITI DI QUALITÀ E LIVELLI DI SERVIZIO (SLA)
[Doc: Capitolato | Pagina: 8 | Articolo: 2.3]

L'erogazione dei servizi deve rispettare i seguenti Livelli Minimi di Servizio (SLA):

1. **Disponibilità del Servizio (Uptime):** $\ge 99,9\%$ su base mensile calcolato h24 7/7.
2. **Tempo di Risposta API:** $\le 200\text{ ms}$ per l'85% delle chiamate HTTP a riposo.
3. **Presidio ed Assistenza Tecnica:**
   - **Ticket Bloccanti (Gravità 1):** Presa in carico entro 15 minuti; risoluzione o workaround entro 2 ore.
   - **Ticket Gravi (Gravità 2):** Presa in carico entro 60 minuti; risoluzione entro 6 ore.
   - **Ticket Minori (Gravità 3):** Presa in carico entro 4 ore; risoluzione entro 24 ore.

---

## 3. NORMATIVE E CERTIFICAZIONI DI SICUREZZA
[Doc: Capitolato | Pagina: 14 | Articolo: 3.1]

Per la corretta esecuzione del servizio e la tutela del patrimonio informativo, l'operatore economico deve garantire il possesso delle seguenti certificazioni ufficiali:

- **UNI CEI EN ISO/IEC 27001:2022** — Sistema di Gestione della Sicurezza delle Informazioni (SGSI) esteso alle estensioni Cloud ISO/IEC 27017 e ISO/IEC 27018.
- **UNI EN ISO 9001:2015** — Sistema di Gestione della Qualità per le attività di progettazione, sviluppo e manutenzione di software informatici.
- **UNI EN ISO 14001:2015** — Gestione Ambientale (criterio di premialità sostenibilità Green ICT).

---

## 4. METODOLOGIA DI SVILUPPO E DOCUMENTAZIONE
[Doc: Capitolato | Pagina: 19 | Articolo: 4.2]
Il processo di sviluppo dovrà seguire la metodologia Agile Scrum con sprint bisettimanali, rilascio continuo (CI/CD) e copertura di test automatici (Unit & Integration Test) non inferiore all'80% del codice fonte.
Tutta la documentazione tecnica, i file OpenAPI e i diagrammi di sequenza dovranno essere rilasciati nel repository dedicato dell'Amministrazione.
