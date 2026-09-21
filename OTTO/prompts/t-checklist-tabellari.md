<!-- OTTO · T — Checklist dei tabellari — componente deterministico, cancello 1 -->
<!-- Versionare insieme al codice. Non e' un agente: e' un join fra bando e knowledge base. -->
<!-- Nuovo, 4 settembre 2026 — post-mortem G01188. -->

# Che cosa fa

Unisce `BandoAnalizzato.tabellari` con il registro certificazioni e asset della
knowledge base e produce una `ChecklistTabellari`, che il cancello 1 mostra come
vista obbligatoria accanto alla griglia dei criteri.

Nessun LLM. Ogni riga e' un confronto fra due stringhe e un'aritmetica su punti.

# Perche' esiste

Sul Lotto I della gara GSE G01188, 4,00 punti su 12,97 di distacco dal vincitore
— il 31% — venivano da due caselle tabellari:

- **a2, connettore ServiceNow, 3,00 punti.** L'offerta scriveva «il collegamento
  puo' essere realizzato tramite OpenFrame, connettore certificato o adapter
  equivalente». Il livello massimo chiedeva «connettore certificato nel
  ServiceNow Store e supportato per almeno le ultime 2 release». Tutte le altre
  cinque offerte hanno preso 3,00; LUO e' l'unica a 0.
- **f2, quota di smart working, 1,00 punto.** Dichiarato 20–50% (1 punto) invece
  di oltre il 50% (2 punti), e motivato come preferenza organizzativa. Quattro
  concorrenti su cinque hanno dichiarato oltre il 50%.

Nessuna delle due e' una questione di scrittura. Sono decisioni non prese, o
prese senza sapere quanto costavano.

# Regole di composizione

| Natura | Come si risolve |
|---|---|
| `possesso` | Cerca in KB un asset con la `dicitura_richiesta`. Confronto sulla stringa normalizzata: norma, edizione, anno. Corrispondenza esatta → `posseduto`. Corrispondenza parziale → `posseduto` con `disallineamento` valorizzato e riga in `da_escalare`. Nessuna corrispondenza → `non_posseduto`. |
| `dichiarazione` | Il dato va cercato in KB (distanza sede, indirizzi, tempi). Se esiste, il livello si calcola; se non esiste, la riga resta aperta. |
| `scelta_organizzativa` | Stato sempre `da_deliberare`. Il sistema espone i livelli con i rispettivi punti e la domanda: quale livello siamo disposti a sostenere, e a che condizioni. **Nessun default.** |

- `punti_persi` = `punti_max` − `punti_ottenuti`, sommati in `punti_rinunciati`.
- `bloccante` resta `True` finche' esiste una riga senza `approvata_da`.

# La vista del cancello 1

Una tabella sola: codice, oggetto, livello massimo con i suoi punti, livello che
possiamo dichiarare oggi, punti che stiamo rinunciando, azione per salire, lead
time.

Sulla gara GSE quella tabella avrebbe mostrato, prima che qualcuno scrivesse una
riga di offerta:

| Cod. | Oggetto | Max | Dichiarabile oggi | Rinuncia | Azione | Lead time |
|---|---|---|---|---|---|---|
| a2 | Connettore ServiceNow certificato | 3,00 | «altri casi» — 0,00 | **3,00** | Certificare il connettore nello Store, o presentarsi con un vendor certificato | fuori perimetro gara |
| f2 | Quota operatori in smart working | 2,00 | «20% ≤ 50%» — 1,00 | **1,00** | Deliberare oltre il 50% | 0 giorni |
| d1–d8 | Otto certificazioni | 4,00 | 4,00 con 4 diciture disallineate | 0,00 (a rischio) | Allineare i certificati o motivare l'equivalenza in offerta | variabile |

# Il disallineamento delle certificazioni

Sul Lotto I la commissione ha accettato PAS 24000:2022 dove il capitolato
chiedeva SA 8000:2014, 45001:2023 per 45001:2018, 14064:2019 per 14064-1:2019 e
27001:2017 per 27001:2022 — quattro voci per due punti complessivi. La stessa
commissione ha pero' penalizzato un concorrente a 0,20 su tre certificazioni.
Due punti sono passati per benevolenza.

Il confronto e' quindi bloccante, non informativo: la persona sceglie fra
allineare il certificato e motivare l'equivalenza in offerta, ma la scelta va
fatta e va firmata.

# Effetto sul piano

Ogni riga con stato `acquisibile_entro_termine` genera una milestone con il suo
lead time. Se il lead time supera il tempo residuo, la milestone e'
`fuori_perimetro_gara`: non e' un ritardo di progetto, e' una decisione
industriale che va presa altrove e che, per questa procedura, si traduce in
punti rinunciati. Il pianificatore la riporta nella testata del cruscotto.
