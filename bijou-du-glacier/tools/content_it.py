# -*- coding: utf-8 -*-
"""
Italiano (uso svizzero).

REGOLA DELLA CASA: nessuna lineetta lunga «—» in questo file. Sa di testo
generato a macchina. Dove ce n'era una, la frase è stata ricostruita attorno a
un punto, a due punti o a una virgola. audit.py fa fallire il build se ne
ricompare una.

Intento di ricerca a cui è scritto il testo:
  appartamento saas-fee · casa vacanze saas-fee · appartamento 8 persone saas-fee ·
  appartamento vallese · settimana bianca saas-fee · chalet saas-fee
Scelte volontarie: «appartamento» e «casa vacanze», che sono i termini realmente
cercati; «autopostale» e «tassa di soggiorno», che sono l'uso svizzero.
"""

IT = {
    "lang": "it",
    "name": "Italiano",
    "locale": "it_CH",
    "dir_label": "IT",

    "ui": {
        "skip": "Vai al contenuto principale",
        "brand_sub": "Saas-Fee · Vallese · Svizzera",
        "home_label": "Home",
        "lang_label": "Scegli la lingua",
        "jump_label": "In questa pagina",
        "nav_label": "Navigazione principale",
        "crumb_label": "Percorso",
        "book_cta": "Prenota diretto alla miglior tariffa",
        "book_cta_short": "Prenota diretto",
        "note": "La tariffa a notte è identica a quella delle piattaforme. Prenotare con noi toglie semplicemente la loro commissione di servizio dal vostro totale, e vi mette in contatto dal primo messaggio con chi si prende cura dell'appartamento.",
        "book_block_title": "Prenota diretto",
        "or_label": "Oppure trovate lo stesso appartamento su",
        "next_label": "Prosegui",
        "gallery_note": "Fotografie dell'appartamento nello stato attuale, dopo la ristrutturazione.",
    },

    "nav": {
        "home": "Panoramica",
        "apartment": "L'appartamento",
        "resort": "Saas-Fee",
        "book": "Prenotare",
    },

    "amenities": [
        "Quattro camere doppie: due con letto king size, due con letti componibili",
        "Le due camere componibili a scelta come king size o due letti singoli",
        "Letti e materassi Hypnos in tutte le camere",
        "Otto posti letto",
        "Tre bagni: due vasche profonde e una doccia walk-in",
        "Soggiorno e cucina a vista",
        "Cucina completamente attrezzata",
        "Tavolo in noce per otto persone",
        "Forno, piano cottura, piano a induzione e microonde",
        "Lavastoviglie",
        "Macchina da caffè e bollitore",
        "Lavatrice e asciugatrice",
        "Internet ad alta velocità in tutto l'appartamento",
        "Televisore in soggiorno",
        "Grande balcone rivolto alle montagne",
        "Arredi da balcone per lunghi pomeriggi",
        "Ascensore fino all'appartamento",
        "Deposito sci nell'edificio",
        "Armadi a muro e spazio per l'attrezzatura",
        "Biancheria, asciugamani e asciugacapelli forniti",
        "Shampoo, balsamo, bagnoschiuma e sapone inclusi",
        "Tende oscuranti in ogni camera",
        "Grucce e spazio armadio in ogni camera",
        "Coperte calde in abbondanza",
        "Giochi per i bambini",
        "Prodotti per la pulizia a disposizione",
        "Parquet in rovere, caldo e silenzioso",
        "Rilevatori di fumo e di monossido di carbonio",
        "Non fumatori, animali non ammessi",
        "Quattro minuti a piedi dalle piste",
        "Nel villaggio senza auto",
        "Edificio interamente ristrutturato",
        "Niente aria condizionata: a 1800 metri non è mai mancata",
    ],

    "facts_table": {
        "caption": "Tutto ciò che si vuole confermato prima di dedicarci una settimana.",
        "rows": [
            ("Posti letto", "8 ospiti"),
            ("Camere", "4 doppie. Due con letto king size, due componibili come king size o letti singoli"),
            ("Bagni", "3: due con vasca profonda, uno con doccia walk-in"),
            ("Indirizzo", "Residence du Glacier, Blomattenstrasse 2, 3906 Saas-Fee, Vallese, Svizzera"),
            ("Distanza dalle piste", "Quattro minuti a piedi, attraverso il villaggio"),
            ("Supermercato più vicino", "A venti metri dalla porta"),
            ("Deposito sci", "Un locale sci nel seminterrato dell'edificio"),
            ("Ascensore", "Sì, fino alla porta dell'appartamento"),
            ("Parcheggio", "Nei parcheggi all'ingresso del villaggio. Saas-Fee è senza auto."),
            ("Stazione più vicina", "Visp, poi l'autopostale su per la valle (circa un'ora)"),
            ("Check-in / check-out", "Dalle 15; check-out flessibile"),
            ("Gestito da", "SaasFeeHolidays.com, in paese"),
            ("Stagioni", "Inverno ed estate"),
        ],
    },

    "faq": [
        ("Quante persone ospita l'appartamento?",
         "Otto, in quattro camere, tutte doppie. Due hanno un letto king size fisso. Le altre due hanno due letti singoli che si uniscono in un king size, a seconda di come serve al gruppo. Basta dirlo prima dell'arrivo e i letti saranno preparati di conseguenza. Tutti i materassi sono Hypnos. Niente divani letto, niente soppalchi, nessuna stanza che si rivela uno sgabuzzino con finestra."),
        ("L'appartamento è ski-in / ski-out?",
         "No, e preferiamo dirlo chiaramente. Bijou du Glacier si trova nel cuore stesso del villaggio, a quattro minuti a piedi dalle piste. Saas-Fee è senza auto, quindi ci si sposta comunque a piedi. Ma se cercate di allacciare gli scarponi davanti alla porta, questo non è l'appartamento giusto."),
        ("Dove si mettono gli sci?",
         "Nel seminterrato dell'edificio c'è un locale sci compreso con l'appartamento, e un ascensore che sale fino alla porta. Molti ospiti lasciano comunque gli sci in quota, alle piste: quattro minuti per tratta con gli scarponi ai piedi sono quattro minuti meglio spesi a colazione."),
        ("Dove si parcheggia?",
         "Nei parcheggi coperti all'ingresso del villaggio. Saas-Fee è senza auto da decenni: si lascia la macchina all'ingresso e si prosegue a piedi o con un taxi elettrico del paese."),
        ("C'è una cucina vera?",
         "Sì, completamente attrezzata. Forno e piano cottura, piano a induzione, microonde, lavastoviglie, macchina da caffè e bollitore, bicchieri e stoviglie per tutto il gruppo, e un tavolo in noce a bordo naturale dove gli otto siedono insieme."),
        ("È adatto ai bambini?",
         "Molto. Il villaggio è senza auto, quindi non c'è una strada da cui tenerli lontani. In appartamento ci sono giochi per i pomeriggi di pioggia, coperte calde in abbondanza e un ascensore che evita di portare qualcuno su per le scale a fine giornata."),
        ("È aperto anche d'estate?",
         "Sì. Il Metro Alpin sale al ghiacciaio dell'Allalin per tutta l'estate. Saas-Fee è uno dei pochi posti nelle Alpi dove si scia a luglio e nello stesso pomeriggio si cammina tra i larici."),
        ("Prenotare direttamente conviene davvero?",
         "La tariffa a notte è la stessa delle piattaforme. La differenza è ciò che si aggiunge sopra: le piattaforme addebitano all'ospite la propria commissione di servizio, la prenotazione diretta no. Già che ci siete, chiedete un check-out posticipato."),
    ],

    "pages": {

        "home": {
            "title": "Appartamento di lusso 4 camere, Saas-Fee | Bijou du Glacier",
            "desc": "Appartamento di quattro camere per otto nel cuore di Saas-Fee senza auto. King size o letti singoli, tre bagni, quattro minuti dalle piste.",
            "h1": "Un gioiello sotto il ghiacciaio di Saas-Fee",
            "lede": "Otto ospiti. Quattro camere doppie, preparate come king size o con letti singoli secondo il gruppo. Un tavolo in noce abbastanza lungo per tutti, in un villaggio dove il rumore più forte, fuori, sono gli scarponi sulla neve fresca.",
            "facts": ["8 persone", "4 camere doppie", "3 bagni", "4 min dalle piste"],
            "jump": [
                ("overview", "L'appartamento"),
                ("gallery", "Fotografie"),
                ("location", "Posizione"),
                ("resort", "Saas-Fee"),
                ("faq", "Domande"),
                ("book", "Prenotare"),
            ],
            "body": """
<section class="section" id="overview" aria-labelledby="overview-h">
  <div class="wrap">
    <p class="eyebrow reveal">L'appartamento</p>
    <h2 id="overview-h" class="reveal">Spazio a sufficienza perché nessuno debba cedere</h2>
    <div class="split">
      <div class="measure reveal">
        <p class="lede">Nella maggior parte degli appartamenti per otto qualcuno deve prendersi la stanza piccola. Qui la stanza piccola non c'è.</p>
        <p>Bijou du Glacier occupa l'estremità est del secondo piano della Residence du Glacier, un edificio ristrutturato da cima a fondo, nel cuore stesso del villaggio. Quattro camere, ognuna con il proprio letto king size su un materasso Hypnos, la propria finestra e la propria luce del mattino. Tre bagni in pietra chiara e ardesia scura: due con vasca profonda, il terzo con doccia walk-in.</p>
        <p>E un unico, lungo ambiente aperto. Cucina, soggiorno e un'asse di noce a bordo naturale dove tutti e otto siedono insieme, così il gruppo resta unito invece di disperdersi fra i piani.</p>
        <p>E poi c'è il balcone. Corre lungo tutta la facciata dell'appartamento, coperto e rivolto dritto verso le montagne. Sedute comode, il sole del pomeriggio finché la luce non lascia le cime, e tredici cime oltre i quattromila che pensano all'intrattenimento.</p>
        <p><a href="{apartment}">La visita, stanza per stanza</a>.</p>
      </div>
      {{fig|living-wide||(min-width: 900px) 46vw, 92vw}}
    </div>
    {{fig|floorplan|plan reveal|(min-width: 900px) 620px, 92vw}}
  </div>
</section>

<section class="section section-panel" id="gallery" aria-labelledby="gallery-h">
  <div class="wrap">
    <p class="eyebrow reveal">Gli ambienti</p>
    <h2 id="gallery-h" class="reveal">Bijou du Glacier dall'interno</h2>
    <p class="measure muted reveal">L'eleganza di un appartamento di chalet contemporaneo: materiali alpini caldi e comfort di oggi, molta luce, e la montagna da quasi ogni finestra.</p>
    <div class="gallery reveal">
      {{fig|dining-table|g-4|(max-width: 560px) 92vw, (max-width: 900px) 46vw, 60vw}}
      {{fig|kitchen|g-2|(max-width: 560px) 92vw, (max-width: 900px) 46vw, 30vw}}
      {{fig|bedroom-2|g-3|(max-width: 560px) 92vw, (max-width: 900px) 46vw, 45vw}}
      {{fig|bathroom|g-3|(max-width: 560px) 92vw, (max-width: 900px) 46vw, 45vw}}
      {{fig|balcony-view|g-2|(max-width: 560px) 92vw, (max-width: 900px) 46vw, 30vw}}
      {{fig|coffee-table|g-2|(max-width: 560px) 92vw, (max-width: 900px) 46vw, 30vw}}
      {{fig|village|g-2|(max-width: 560px) 92vw, (max-width: 900px) 46vw, 30vw}}
    </div>
  </div>
</section>

<section class="section" id="location" aria-labelledby="location-h">
  <div class="wrap">
    <p class="eyebrow reveal">L'indirizzo</p>
    <h2 id="location-h" class="reveal">A quattro minuti dalle piste. A un mondo dal traffico.</h2>
    <div class="cols">
      <div class="col reveal">
        <h3>Nel villaggio, non sopra di esso</h3>
        <p>Quattro minuti dalle piste. Venti metri dal supermercato. Il panificio, il noleggio sci e ogni ristorante che valga la passeggiata sono ancora più vicini. In una località dove si guida, stare in centro è una comodità; in un villaggio dove nessuno guida, disegna l'intera settimana. Si arriva, si lascia l'auto all'ingresso e non si pensa mai più a come spostarsi.</p>
      </div>
      <div class="col reveal">
        <h3>Tredici quattromila, dal proprio balcone</h3>
        <p>Il balcone guarda i Mischabel, il massiccio del Dom, la vetta più alta interamente in territorio svizzero. Al mattino la luce scende quella parete prima di raggiungere il paese. La sera le cime la trattengono venti minuti più a lungo della strada sotto, che è ragione sufficiente per essere ancora seduti fuori alle sette.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-panel" id="resort" aria-labelledby="resort-h">
  <div class="wrap">
    <p class="eyebrow reveal">Il villaggio</p>
    <h2 id="resort-h" class="reveal">Saas-Fee, la Perla delle Alpi</h2>
    <div class="split">
      {{fig|massif||(min-width: 900px) 46vw, 92vw}}
      <div class="measure reveal">
        <p class="lede">Niente auto. Niente motori. E un ghiacciaio proprio sopra, che si scia a luglio con la stessa naturalezza di gennaio.</p>
        <p>Saas-Fee sta a 1800 metri dentro un ferro di cavallo di tredici cime oltre i quattromila, ed è chiusa al traffico da decenni. Gli ospiti lasciano l'auto all'ingresso e proseguono a piedi. Quello che resta è un villaggio che suona come dovrebbero suonare i villaggi di montagna.</p>
        <p>Sopra, il Metro Alpin sale dentro la montagna fino al ghiacciaio dell'Allalin, a 3500 metri, dove la neve tiene tutto l'anno. È il motivo per cui ad agosto ci si allenano le squadre nazionali, e per cui la vostra stagione non finisce mai del tutto.</p>
        <p><a href="{resort}">Sci, estate e come arrivare</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="faq" aria-labelledby="faq-h">
  <div class="wrap">
    <p class="eyebrow reveal">Da sapere</p>
    <h2 id="faq-h" class="reveal">Tutto quello che vorrete chiedere</h2>
    <div class="reveal">{{faq}}</div>
  </div>
</section>

<section class="section section-panel" id="book" aria-labelledby="book-h">
  <div class="wrap">
    <p class="eyebrow reveal">Disponibilità</p>
    <h2 id="book-h" class="reveal">Prenotate il vostro soggiorno</h2>
    {{reservebox}}
  </div>
</section>
""",
        },

        "apartment": {
            "title": "Appartamento 4 camere, otto persone | Bijou du Glacier",
            "desc": "Stanza per stanza: quattro camere doppie su letti Hypnos, king size o letti singoli, cucina a vista, tavolo in noce per otto, tre bagni e un grande balcone.",
            "h1": "L'appartamento, stanza per stanza",
            "lede": "Rovere a doghe larghe, pietra chiara, ottone spazzolato. Alpino contemporaneo, non finto legno intagliato, e dimensionato perché otto persone vivano bene insieme, non semplicemente ci stiano.",
            "jump": [
                ("sleeping", "Camere"),
                ("living", "Soggiorno"),
                ("kitchen", "Cucina"),
                ("bathrooms", "Bagni"),
                ("balcony", "Balcone"),
                ("floorplan", "Pianta"),
                ("amenities", "Dotazione"),
                ("practical", "Pratica"),
                ("gallery", "Fotografie"),
            ],
            "body": """
<section class="section" id="sleeping" aria-labelledby="sleeping-h">
  <div class="wrap">
    <p class="eyebrow">Camere</p>
    <h2 id="sleeping-h">Quattro camere doppie. King size o letti singoli, come preferite.</h2>
    <div class="split">
      <div class="measure">
        <p>Tutte e quattro le camere sono doppie e ognuna ha la propria finestra e la propria luce naturale. Due hanno un letto king size fisso. Le altre due hanno due letti singoli che si uniscono in un king size.</p>
        <p>È più utile di quattro king size fissi. Quattro coppie hanno quattro king size. Due famiglie hanno due king size e quattro letti singoli per i bambini. Basta indicarlo al momento della prenotazione e i letti saranno pronti prima dell'arrivo. Così a nessuno tocca la parte peggiore.</p>
        <p>Ogni letto è un Hypnos, ed è il motivo per cui gli ospiti finiscono per scrivere di quanto hanno dormito bene più che dello sci. La camera principale è rivestita da pavimento a soffitto in rovere chiaro, con testiera imbottita. Le altre tre sono più chiare: pareti bianche, stampe alpine incorniciate, plaid di lana oliva, ruggine e ocra, e lampade da lettura su entrambi i lati.</p>
        <p>Armadi a muro in ogni stanza, con appenderia e ripiani, e un locale sci nel seminterrato dell'edificio, così l'attrezzatura di otto persone non finisce mai in corridoio.</p>
      </div>
      {{fig|bedroom-3||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="living" aria-labelledby="living-h">
  <div class="wrap">
    <p class="eyebrow">Soggiorno</p>
    <h2 id="living-h">Una stanza che tiene tutta la compagnia</h2>
    <div class="split">
      {{fig|living-corner||(min-width: 900px) 44vw, 92vw}}
      <div class="measure">
        <p>Il soggiorno prosegue nella cucina senza divisori e prende luce da due lati. Un divano profondo verde oliva, due tavolini rotondi in bronzo, un tappeto morbido a motivi su doghe larghe di rovere, e un televisore che c'è se lo si vuole ed è facile ignorare se non lo si vuole.</p>
        <p>La stanza è abbastanza grande perché metà del gruppo legga mentre l'altra metà cucina. Per il divano ci sono coperte calde in abbondanza, e in un armadio aspettano i giochi per il pomeriggio in cui passa una tempesta.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="kitchen" aria-labelledby="kitchen-h">
  <div class="wrap">
    <p class="eyebrow">Cucina e tavola</p>
    <h2 id="kitchen-h">Una cucina all'altezza di otto cene</h2>
    <div class="split">
      <div class="measure">
        <p>Completamente attrezzata e realizzata in tortora tenue con schienale in pietra e rubinetteria in ottone spazzolato: forno a incasso e piano cottura, piano a induzione, microonde, lavastoviglie, cappa, frigorifero, bollitore e macchina da caffè, con ripiani a vista per bicchieri, ciotole e piatti per tutto il gruppo.</p>
        <p>Il tavolo è un'unica asse di noce a bordo naturale con sedie nere cross-back. Otto posti, tutti allo stesso tavolo. Cucinare per un gruppo funziona solo se cucina e tavolo reggono il gruppo intero in una volta. Qui è così.</p>
        <p>Il supermercato è a venti metri dalla porta: fare la spesa è una commissione, non una spedizione.</p>
      </div>
      {{fig|kitchen-oven||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="bathrooms" aria-labelledby="bathrooms-h">
  <div class="wrap">
    <p class="eyebrow">Bagni</p>
    <h2 id="bathrooms-h">Tre bagni, pietra e ardesia</h2>
    <div class="split">
      {{fig|bathroom-shower||(min-width: 900px) 44vw, 92vw}}
      <div class="measure">
        <p>Tutti e tre sono rifiniti in pietra chiara di grande formato con una fascia di ardesia scura, mobili sospesi in rovere, lavabi in pietra e specchi retroilluminati. Due hanno una vasca profonda, che è quello che si desidera dopo una giornata intera sul ghiacciaio. Il terzo ha una doccia walk-in.</p>
        <p>Tre bagni per otto persone è il rapporto che fa funzionare una mattina sugli sci. Nessuna coda, e nessuno che contratta l'acqua calda alle otto. Accappatoi, asciugamani e asciugacapelli a disposizione, e una lavatrice con asciugatrice per l'attrezzatura della settimana.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="balcony" aria-labelledby="balcony-h">
  <div class="wrap">
    <p class="eyebrow">Fuori</p>
    <h2 id="balcony-h">Un balcone da cui non vorrete rientrare</h2>
    <div class="split">
      <div class="measure">
        <p>Un grande balcone coperto corre per tutta la lunghezza dell'appartamento, sopra i tetti del villaggio e rivolto dritto verso le montagne. È arredato per sedersi, non per stare in piedi, con poltrone lounge profonde in intreccio, tavolini bassi e riparo sufficiente per restare fuori mentre nevica. Che è poi il momento in cui dà il meglio.</p>
        <p>Guarda la parete dei Mischabel. Al mattino la luce scende lungo la faccia prima di arrivare al paese. La sera le vette la trattengono altri venti minuti quando la strada è già in ombra, e a quel punto nessuno ha fretta di rientrare.</p>
      </div>
      {{fig|balcony-view||(min-width: 900px) 44vw, 92vw}}
    </div>
    <div class="pair">
      {{fig|patio-seating||(min-width: 900px) 30vw, 45vw}}
      {{fig|patio-chair||(min-width: 900px) 30vw, 45vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="floorplan" aria-labelledby="floorplan-h">
  <div class="wrap">
    <p class="eyebrow">Pianta</p>
    <h2 id="floorplan-h">Come è distribuito l'appartamento</h2>
    <div class="measure">
      <p>Quattro camere, tre bagni e un lungo ambiente aperto, tutto sullo stesso livello all'estremità del piano. Il soggiorno sfiora i quaranta metri quadrati, le camere vanno dagli undici ai quattordici ciascuna, e il balcone coperto sulla facciata ne aggiunge altri venticinque.</p>
      <p>Qui sotto trovate il disegno originale dell'architetto per l'appartamento B4. È il modo più rapido per stabilire chi prende quale camera, prima ancora che qualcuno abbia fatto la valigia.</p>
    </div>
    {{fig|floorplan|plan|(min-width: 900px) 620px, 92vw}}
  </div>
</section>

<section class="section" id="amenities" aria-labelledby="amenities-h">
  <div class="wrap">
    <p class="eyebrow">Dotazione</p>
    <h2 id="amenities-h">Quello che vi aspetta</h2>
    {{amenities}}
  </div>
</section>

<section class="section section-panel" id="practical" aria-labelledby="practical-h">
  <div class="wrap">
    <p class="eyebrow">Pratica</p>
    <h2 id="practical-h">I dettagli</h2>
    {{facts}}
    <p class="fineprint">Check-in dalle 15, check-out flessibile. Chiavi e registrazione per la tassa di soggiorno sono gestite da SaasFeeHolidays.com, in paese, e confermate prima della partenza. <a href="{book}">Come si prenota</a>.</p>
  </div>
</section>

<section class="section" id="gallery" aria-labelledby="gallery-h">
  <div class="wrap">
    <p class="eyebrow">Fotografie</p>
    <h2 id="gallery-h">Ancora l'appartamento</h2>
    <div class="gallery">
      {{fig|dining-walnut|g-3|(max-width: 560px) 92vw, (max-width: 900px) 46vw, 45vw}}
      {{fig|kitchen-tap|g-3|(max-width: 560px) 92vw, (max-width: 900px) 46vw, 45vw}}
      {{fig|bedroom-4|g-2|(max-width: 560px) 92vw, (max-width: 900px) 46vw, 30vw}}
      {{fig|wardrobe|g-2|(max-width: 560px) 92vw, (max-width: 900px) 46vw, 30vw}}
      {{fig|blanket|g-2|(max-width: 560px) 92vw, (max-width: 900px) 46vw, 30vw}}
      {{fig|bathroom-bath|g-3|(max-width: 560px) 92vw, (max-width: 900px) 46vw, 45vw}}
      {{fig|robe-door|g-3|(max-width: 560px) 92vw, (max-width: 900px) 46vw, 45vw}}
    </div>
  </div>
</section>
""",
        },

        "resort": {
            "title": "Saas-Fee: senza auto, sci sul ghiacciaio | Bijou du Glacier",
            "desc": "Com'è soggiornare a Saas-Fee: villaggio senza auto a 1800 m, Metro Alpin fino al ghiacciaio dell'Allalin, neve tutto l'anno ed escursioni d'estate.",
            "h1": "Saas-Fee, la Perla delle Alpi",
            "lede": "Un villaggio senza auto a 1800 metri, circondato da tredici quattromila, sotto un ghiacciaio che si scia a luglio con la stessa naturalezza di gennaio.",
            "jump": [
                ("car-free", "Senza auto"),
                ("skiing", "Sci"),
                ("summer", "Estate"),
                ("eating", "Ristoranti"),
                ("getting-here", "Come arrivare"),
            ],
            "body": """
<section class="section" id="car-free" aria-labelledby="carfree-h">
  <div class="wrap">
    <p class="eyebrow">Il villaggio</p>
    <h2 id="carfree-h">Che cosa cambia davvero un villaggio senza auto</h2>
    <div class="split">
      <div class="measure">
        <p>Gli ospiti lasciano il veicolo nei parcheggi all'ingresso e proseguono a piedi. I pochi mezzi che circolano in paese sono piccoli veicoli elettrici: taxi, carrelli per le consegne, ogni tanto un mezzo di servizio.</p>
        <p>L'effetto è immediato e difficile da sopravvalutare. Nessun rumore di traffico, nessuno scarico, nessun bordo strada da cui tenere lontani i bambini. I gruppi si sparpagliano e si ritrovano senza che nessuno conti le teste davanti a una carreggiata. Quasi tutte le località alpine hanno smesso di essere così decenni fa. Saas-Fee mai.</p>
        <p>Cambia anche quanto vale la parola «centrale». Poiché ci si muove solo a piedi, un appartamento in mezzo al paese, <a href="{apartment}">come questo</a>, non è una comodità marginale. È la differenza tra una vacanza con logistica e una senza.</p>
      </div>
      {{fig|village||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="skiing" aria-labelledby="skiing-h">
  <div class="wrap">
    <p class="eyebrow">Inverno</p>
    <h2 id="skiing-h">Un ghiacciaio sopra il paese, una funicolare dentro la montagna</h2>
    <div class="split">
      {{fig|piste-dawn||(min-width: 900px) 44vw, 92vw}}
      <div class="measure">
        <p>Il comprensorio sale dal villaggio fino al ghiacciaio dell'Allalin. Il Metro Alpin, una funicolare sotterranea che corre dentro la montagna, porta gli sciatori a Mittelallalin, intorno ai 3500 metri, dove la neve tiene tutto l'anno.</p>
        <p>È quella quota a rendere Saas-Fee affidabile a inizio e fine stagione, quando i comprensori più bassi guardano le previsioni. Il terreno è ampio e aperto in alto e si restringe fra i larici sulla via del ritorno.</p>
        <p>Dalla porta dell'appartamento alle piste sono quattro minuti a piedi, attraverso il villaggio.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="summer" aria-labelledby="summer-h">
  <div class="wrap">
    <p class="eyebrow">Estate</p>
    <h2 id="summer-h">Sci prima di pranzo. A piedi dopo.</h2>
    <div class="split">
      <div class="measure">
        <p>Saas-Fee è uno dei pochi posti nelle Alpi in cui il ghiacciaio si scia per tutta l'estate, ed è il motivo per cui a luglio e agosto ci si accampano le squadre nazionali. Il Metro Alpin continua a funzionare: si è sulla neve prima di mezzogiorno senza un metro di dislivello a piedi.</p>
        <p>Sotto il ghiaccio comincia il territorio delle camminate: sentieri d'alta quota tra larici e roccia, alpeggi, e tutto il ferro di cavallo delle cime in vista. Giornate lunghe, notti fresche e il villaggio nella sua versione più rilassata e, per inciso, più conveniente.</p>
      </div>
      {{fig|glacier-view||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="eating" aria-labelledby="eating-h">
  <div class="wrap">
    <p class="eyebrow">Sere</p>
    <h2 id="eating-h">Cena, in un modo o nell'altro</h2>
    <div class="measure">
      <p>I ristoranti stanno sulla via principale e nei dintorni, tutti a distanza di passeggiata dall'appartamento. Poiché nulla dista più di qualche minuto, uscire a cena non richiede mai un piano. Si scende, si mangia, si risale, e nessuno deve restare sobrio per guidare.</p>
      <p>Mangiare a casa è l'altra metà dell'argomento a favore di un appartamento. Un gruppo di otto in albergo paga otto coperti a prezzo d'albergo tutte le sere. Qui <a href="{apartment}#kitchen">la cucina e il tavolo</a> reggono il gruppo intero, il supermercato è a venti metri, e si cucina quando se ne ha voglia.</p>
    </div>
  </div>
</section>

<section class="section" id="getting-here" aria-labelledby="getting-h">
  <div class="wrap">
    <p class="eyebrow">Come arrivare</p>
    <h2 id="getting-h">L'arrivo</h2>
    <div class="cols cols-3">
      <div class="col">
        <h3>In treno</h3>
        <p>Fino a Visp, sulla linea principale della valle del Rodano, poi l'autopostale su per la Saastal, circa un'ora. La fermata è all'ingresso del villaggio, a pochi minuti a piedi dall'appartamento.</p>
      </div>
      <div class="col">
        <h3>In auto</h3>
        <p>Da Visp si risale la valle fino ai parcheggi all'ingresso del paese. In Saas-Fee non si entra in auto; non lo fa nessuno. Da novembre le gomme invernali sono il minimo ragionevole.</p>
      </div>
      <div class="col">
        <h3>In aereo</h3>
        <p>Ginevra e Zurigo sono entrambe realistiche, circa tre ore e mezza fra treno e autopostale. D'estate Milano Malpensa è un'alternativa, passando dal Sempione.</p>
      </div>
    </div>
    <p class="fineprint">Le indicazioni precise per l'arrivo e la consegna delle chiavi arrivano dall'amministrazione locale una volta confermate le date. <a href="{book}">Condizioni di prenotazione</a>.</p>
  </div>
</section>
""",
        },

        "book": {
            "title": "Prenota diretto, senza commissioni | Bijou du Glacier",
            "desc": "Prenota Bijou du Glacier direttamente: stessa tariffa delle piattaforme, senza commissione di servizio. Quattro camere, otto persone, a Saas-Fee.",
            "h1": "Prenotare il soggiorno",
            "lede": "L'appartamento si prenota da più canali. Indichiamo per primo quello diretto, e la ragione è aritmetica più che sentimentale.",
            "jump": [
                ("direct", "Diretto"),
                ("platforms", "Piattaforme"),
                ("before-you-book", "Prima di prenotare"),
            ],
            "body": """
<section class="section" id="direct" aria-labelledby="direct-h">
  <div class="wrap">
    <p class="eyebrow">Diretto</p>
    <h2 id="direct-h">Prenotare direttamente presso l'appartamento</h2>
    <div class="measure">
      <p>La tariffa a notte è la stessa ovunque. Non pratichiamo prezzi inferiori a quelli delle piattaforme, e non ci è consentito farlo. Quello che cambia è ciò che si aggiunge sopra: le piattaforme addebitano all'ospite la propria commissione di servizio, la prenotazione diretta no.</p>
      <p>Chi prenota direttamente, inoltre, parla con SaasFeeHolidays.com in paese fin dal primo messaggio, invece che con una casella di posta di piattaforma. Sembra un dettaglio, e smette di sembrarlo quando serve un check-out posticipato o le chiavi in anticipo.</p>
    </div>
    {{bookblock}}
  </div>
</section>

<section class="section section-panel" id="platforms" aria-labelledby="platforms-h">
  <div class="wrap">
    <p class="eyebrow">Le alternative</p>
    <h2 id="platforms-h">Oppure trovateci sulle piattaforme</h2>
    <div class="measure">
      <p>Se preferite prenotare dove avete già un account, un metodo di pagamento e uno storico di cancellazioni, è del tutto ragionevole. Gli annunci qui sotto riguardano lo stesso appartamento.</p>
    </div>
    {{platforms}}
  </div>
</section>

<section class="section" id="before-you-book" aria-labelledby="before-h">
  <div class="wrap">
    <p class="eyebrow">Da sapere</p>
    <h2 id="before-h">Prima di prenotare</h2>
    <div class="cols">
      <div class="col">
        <h3>Con chi prenotate</h3>
        <p>Un appartamento di proprietà privata, seguito da Adam e dal team di SaasFeeHolidays.com, con sede in paese, in Untere Dorfstrasse. Non una catena, non un portafoglio immobiliare. Un appartamento, in un edificio, con un mazzo di chiavi.</p>
        <p>Non sono al primo inverno. Nove anni da host a Saas-Fee, status di Superhost su Airbnb e <strong>308 recensioni con una media di 4,76 su 5</strong> sugli appartamenti che seguono in paese. Vivono qui tutto l'anno, sanno quale ristorante vale la camminata a febbraio, e sono loro a rispondere ai vostri messaggi e a consegnarvi le chiavi.</p>
      </div>
      <div class="col">
        <h3>Pagamento e cancellazione</h3>
        <p>Il piano di pagamento e le condizioni di cancellazione vengono comunicati da SaasFeeHolidays.com alla conferma delle date, prima di qualsiasi versamento.</p>
        </div>
      <div class="col">
        <h3>Tassa di soggiorno e registrazione</h3>
        <p>I Comuni svizzeri richiedono la registrazione degli ospiti e riscuotono una tassa di soggiorno per persona e per notte, incassata sul posto. Non è compresa nella tariffa a notte e non è una commissione di prenotazione.</p>
      </div>
      <div class="col">
        </div>
      <div class="col">
        <h3>Ancora indecisi?</h3>
        <p>I due testi da leggere per primi sono <a href="{apartment}">la descrizione stanza per stanza</a> e <a href="{resort}">com'è davvero Saas-Fee</a>, soprattutto se non avete mai soggiornato in un villaggio senza auto.</p>
      </div>
    </div>
  </div>
</section>
""",
        },
    },

    "alt": {
        "patio-hero": "Una poltrona lounge in intreccio con cuscino malva sul balcone coperto dell'appartamento, nel sole del pomeriggio, sopra i larici della valle di Saas.",
        "patio-chair": "Una poltrona lounge rotonda in intreccio con un ampio cuscino malva e un tavolino rotondo basso sul balcone, accanto alle porte a vetri, con vista sui larici e sul tetto di uno chalet dall'altra parte della valle.",
        "patio-seating": "Il balcone coperto per tutta la lunghezza dell'appartamento, sotto un soffitto in legno scuro, con poltrone lounge in intreccio e cuscini malva lungo una ringhiera in ferro battuto, due tavolini rotondi bassi e i tetti di Saas-Fee più in basso.",
        "floorplan": "Pianta d'architetto dell'appartamento B4 al secondo piano della Residence du Glacier: quattro camere e tre bagni attorno a un ingresso centrale, soggiorno, zona pranzo e cucina a vista lungo la facciata, e un balcone coperto su tutta la larghezza.",
        "hero-video": "Una visita all'appartamento: la pista e la parete dei Mischabel sopra Saas-Fee, poi il soggiorno, la cucina, le quattro camere, i bagni e il balcone.",
        "piste-dawn": "Pista appena battuta che scende lungo un nevaio sopra Saas-Fee alle prime luci, con la roccia e il ghiaccio della parete dei Mischabel alle spalle.",
        "dining-band": "Il lungo tavolo in noce a bordo naturale apparecchiato per otto, visto per il lungo nell'ambiente aperto, con la cucina a un'estremità e una parete in pietra sul fondo.",
        "massif": "La parete glaciale del massiccio dei Mischabel sopra Saas-Fee, ampi nevai e creste dalle ombre azzurre sopra i tetti del villaggio.",
        "living-room": "Il soggiorno a vista dell'appartamento di Saas-Fee, con divano verde oliva, tavolini rotondi in bronzo, tappeto a motivi su doghe larghe di rovere e finestre su due lati.",
        "kitchen-shelves": "Ripiani a vista della cucina con stoviglie bianche e bicchieri sopra un piano in pietra, accanto a rubinetto in ottone spazzolato, bollitore e ceppo dei coltelli.",
        "master-bedroom": "La camera principale, letto king size contro una parete rivestita in rovere chiaro a tutta altezza, trapunta oliva, cuscini ruggine e stampa alpina incorniciata.",
        "balcony-view": "Il grande balcone coperto dell'appartamento, con ringhiera in ferro battuto, affacciato sui tetti innevati di Saas-Fee e sulle cime oltre.",
        "living-wide": "Soggiorno e zona pranzo dell'appartamento di quattro camere a Saas-Fee visti insieme, con alte finestre sul villaggio innevato e sulle montagne.",
        "coffee-table": "Due tavolini rotondi a doppio ripiano in bronzo su un tappeto color crema, davanti al divano verde oliva del soggiorno.",
        "living-corner": "Un angolo tranquillo del soggiorno con divano chiaro, cuscino senape, lampada ad arco e due specchi dal profilo organico alla parete.",
        "dining-table": "Il lungo tavolo in noce a bordo naturale con sedie nere cross-back, apparecchiato per otto davanti alla cucina a vista, con una parete in pietra sul fondo.",
        "dining-walnut": "Il tavolo in noce visto dal lato della cucina, con una ciotola chiara al centro e le finestre del soggiorno oltre.",
        "kitchen": "La cucina completamente attrezzata dell'appartamento di Saas-Fee in tortora tenue con schienale in pietra, forno a incasso e piano a induzione, tavolo in primo piano.",
        "kitchen-oven": "Il blocco cucina con forno a incasso e macchina da caffè sotto una calda luce a ripiano, affacciato direttamente sul tavolo.",
        "kitchen-tap": "Primo piano del rubinetto in ottone spazzolato e dello schienale in pietra, con bollitore di rame e utensili sul piano di lavoro.",
        "bedroom-2": "La seconda camera, letto king size in biancheria bianca, cuscini ocra e cioccolato, lampade da comodino accese e stampa incorniciata sopra la testiera.",
        "bedroom-3": "La terza camera, letto king size, alta testiera color crema a scanalature, cuscini marrone cioccolato e lampade accese su entrambi i lati.",
        "bedroom-4": "La quarta camera, letto king size, alto armadio in rovere scanalato, lampada da terra e finestra profonda affacciata sul villaggio.",
        "wardrobe": "Un armadio a muro in rovere aperto, con appenderia e ripiani, spazio per un gruppo di otto persone.",
        "blanket": "Una coperta di lana svizzera piegata, con banda rossa e croce, sul bracciolo di una poltrona in bouclé.",
        "bathroom": "Uno dei tre bagni, rifinito in pietra chiara di grande formato, con mobile sospeso in rovere, lavabo in pietra, rubinetto in ottone spazzolato e specchio retroilluminato.",
        "bathroom-shower": "La doccia walk-in dietro un vetro trasparente, ardesia scura contro pietra chiara, accanto allo specchio retroilluminato e al mobile in rovere.",
        "bathroom-bath": "Una delle due vasche profonde, davanti a una fascia di ardesia scura, con una porta a vetri affacciata sulla neve.",
        "robe-door": "Un accappatoio bianco appeso a una porta in rovere a spina di pesce dentro l'appartamento.",
        "village": "I tetti innevati di Saas-Fee, villaggio senza auto, al crepuscolo, con una pista che scende in paese e le cime alle spalle.",
        "glacier-view": "Le alte cime glaciali sopra Saas-Fee nella luce estiva, viste dalle finestre dell'appartamento oltre i tetti.",
        "share": "La parete glaciale dei Mischabel sopra il villaggio di Saas-Fee, in Vallese.",
    },

    "caption": {
        "patio-chair": "L'angolo vicino alle porte, dove il sole arriva per primo.",
        "patio-seating": "Tutta la sua lunghezza, al coperto, con il villaggio sotto.",
        "floorplan": "Il disegno originale dell'architetto per l'appartamento B4. Le diciture sono in tedesco: Zimmer una camera, Bad un bagno, Dusche la doccia, Küche la cucina, Wohnzimmer il soggiorno, Balkon il balcone.",
        "living-wide": "Soggiorno e cucina, aperti l'uno sull'altra.",
        "coffee-table": "Bronzo, rovere e lana, la palette della ristrutturazione.",
        "living-corner": "Un angolo per leggere mentre in cucina si lavora.",
        "dining-table": "Un tavolo, otto posti, e dietro una cucina completamente attrezzata: lavastoviglie, microonde, piano cottura e forno, macchina da caffè.",
        "dining-walnut": "Un'unica asse di noce a bordo naturale.",
        "kitchen": "Completamente attrezzata, e dimensionata per un gruppo.",
        "kitchen-oven": "Forno, piano e macchina da caffè sotto la luce a ripiano.",
        "kitchen-tap": "Ottone spazzolato sulla pietra.",
        "bedroom-2": "Seconda camera.",
        "bedroom-3": "Terza camera.",
        "bedroom-4": "Quarta camera.",
        "wardrobe": "Appenderia e ripiani in ogni stanza.",
        "blanket": "Lana, dove serve.",
        "bathroom": "Pietra, ardesia e rovere.",
        "bathroom-shower": "La doccia walk-in.",
        "bathroom-bath": "Una vasca profonda, con finestra sulla neve.",
        "robe-door": "Accappatoi a disposizione.",
        "village": "Saas-Fee al crepuscolo, con la pista che scende in paese.",
        "glacier-view": "Il ghiacciaio, dalle finestre.",
        "dining-band": "Un tavolo, otto posti, un ambiente.",
        "massif": "La parete dei Mischabel, dritta davanti al balcone.",
        "piste-dawn": "Prime luci sulla pista sopra il villaggio.",
        "balcony-view": "Il balcone, sopra i tetti del villaggio.",
    },

    "footer": {
        "explore": "Esplora",
        "book": "Prenotare",
        "contact": "L'immobile",
        "address": "Residence du Glacier · Blomattenstrasse 2 · 3906 Saas-Fee · Vallese · Svizzera",
        "fine": "Appartamento privato di quattro camere a Saas-Fee, gestito localmente.",
    },

    "next": {
        "apartment": ("L'appartamento, stanza per stanza", "Quattro camere, la cucina, i bagni e il balcone, con le informazioni pratiche in tabella."),
        "resort": ("Saas-Fee", "Un villaggio senza auto a 1800 m, il ghiacciaio sopra e come arrivarci."),
        "book": ("Prenota diretto", "Stessa tariffa a notte delle piattaforme, senza la loro commissione di servizio."),
        "home": ("Panoramica", "L'appartamento, il villaggio e le fotografie in una pagina."),
    },
}
