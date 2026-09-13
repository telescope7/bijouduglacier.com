# -*- coding: utf-8 -*-
"""
Deutsch (Schweizer Rechtschreibung: durchgehend "ss", kein "ß").

HAUSREGEL: keine Gedankenstriche vom Typ "—" in diesem File. Sie lesen sich
maschinell. Wo einer stand, wurde der Satz mit Punkt, Doppelpunkt oder Komma
neu gebaut. audit.py bricht den Build ab, wenn wieder einer auftaucht.

Suchintention, gegen die getextet wurde:
  ferienwohnung saas-fee · ferienwohnung saas-fee 8 personen ·
  ferienwohnung saas-fee 4 schlafzimmer · unterkunft saas-fee ·
  skiferien saas-fee wohnung · chalet saas-fee · wohnung mieten saas-fee
Bewusst NICHT wörtlich aus dem Englischen übersetzt: im deutschsprachigen
Suchverhalten dominiert "Ferienwohnung", nicht "Apartment".
"""

DE = {
    "lang": "de",
    "name": "Deutsch",
    "locale": "de_CH",
    "dir_label": "DE",

    "ui": {
        "skip": "Direkt zum Inhalt",
        "brand_sub": "Saas-Fee · Wallis · Schweiz",
        "home_label": "Startseite",
        "lang_label": "Sprache wählen",
        "jump_label": "Auf dieser Seite",
        "nav_label": "Hauptnavigation",
        "crumb_label": "Sie befinden sich hier",
        "book_cta": "Direkt buchen zum Bestpreis",
        "book_cta_short": "Direkt buchen",
        "note": "Der Übernachtungspreis ist derselbe wie auf den Plattformen. Bei einer Direktbuchung entfällt lediglich deren Servicegebühr, und Sie sprechen von der ersten Nachricht an mit den Menschen, die die Wohnung betreuen.",
        "book_block_title": "Direkt buchen",
        "or_label": "Oder Sie finden dieselbe Wohnung auf",
        "next_label": "Weiter",
        "gallery_note": "Aufnahmen der Wohnung im heutigen Zustand, nach der Renovation.",
    },

    "nav": {
        "home": "Übersicht",
        "apartment": "Die Wohnung",
        "resort": "Saas-Fee",
        "book": "Buchen",
    },

    "amenities": [
        "Vier Schlafzimmer mit je einem Kingsize-Bett",
        "Betten und Matratzen von Hypnos",
        "Platz für acht Personen",
        "Drei Badezimmer: zwei tiefe Wannen und eine Walk-in-Dusche",
        "Offener Wohn- und Küchenbereich",
        "Vollständig ausgestattete Küche",
        "Nussbaumtisch für acht Personen",
        "Backofen, Herd, Induktionskochfeld und Mikrowelle",
        "Geschirrspüler",
        "Kaffeemaschine und Wasserkocher",
        "Waschmaschine und Tumbler",
        "Schnelles Internet in der ganzen Wohnung",
        "Fernseher im Wohnzimmer",
        "Grosser Balkon mit Blick auf die Berge",
        "Balkonmöbel für lange Nachmittage",
        "Lift bis zur Wohnung",
        "Skidepot im Haus",
        "Einbauschränke und Stauraum für die Ausrüstung",
        "Bettwäsche, Handtücher und Haartrockner vorhanden",
        "Reichlich warme Wolldecken",
        "Spiele für die Kinder",
        "Reinigungsmittel vorhanden",
        "Eichenparkett, warm und ruhig",
        "Rauch- und Kohlenmonoxidmelder",
        "Nichtraucherwohnung, keine Haustiere",
        "Vier Gehminuten zu den Pisten",
        "Im autofreien Dorf gelegen",
        "Das ganze Haus neu saniert",
    ],

    "facts_table": {
        "caption": "Alles, was man bestätigt haben möchte, bevor man eine Woche darauf verwendet.",
        "rows": [
            ("Personen", "8 Gäste"),
            ("Schlafzimmer", "4, je mit einem Kingsize-Bett"),
            ("Badezimmer", "3: zwei mit tiefer Wanne, eines mit Walk-in-Dusche"),
            ("Adresse", "Residence du Glacier, Blomattenstrasse 2, 3906 Saas-Fee, Wallis, Schweiz"),
            ("Weg zu den Pisten", "Vier Gehminuten durch das Dorf"),
            ("Nächster Supermarkt", "Zwanzig Meter vor der Tür"),
            ("Skidepot", "Im Untergeschoss des Hauses"),
            ("Lift", "Ja, bis zur Wohnungstür"),
            ("Parkieren", "In den Parkhäusern am Dorfeingang. Saas-Fee ist autofrei."),
            ("Nächster Bahnhof", "Visp, danach mit dem Postauto ins Saastal (rund eine Stunde)"),
            ("Check-in / Check-out", "Ab 15 Uhr; Check-out flexibel"),
            ("Betreut von", "SaasFeeHolidays.com, im Dorf"),
            ("Saison", "Winter und Sommer"),
        ],
    },

    "faq": [
        ("Für wie viele Personen ist die Ferienwohnung?",
         "Für acht, in vier Schlafzimmern. In jedem steht ein Kingsize-Bett auf einer Hypnos-Matratze. Keine Schlafsofas, keine Galerie, kein Zimmer, das sich als Kammer mit Fenster entpuppt."),
        ("Ist die Wohnung Ski-in/Ski-out?",
         "Nein, und das sagen wir lieber offen. Bijou du Glacier liegt mitten im Dorf, vier Gehminuten von den Pisten entfernt. Saas-Fee ist autofrei, man geht ohnehin überall zu Fuss hin. Wer aber unbedingt direkt vor der Tür einsteigen will, ist hier falsch."),
        ("Wohin mit den Skiern?",
         "Im Untergeschoss des Hauses gibt es ein Skidepot, das zur Wohnung gehört, und einen Lift bis zur Tür. Viele Gäste lassen die Ski trotzdem oben an der Piste, denn vier Minuten pro Weg in Skischuhen sind vier Minuten, die man besser beim Frühstück verbringt."),
        ("Wo können wir parkieren?",
         "In den gedeckten Parkhäusern am Dorfeingang. Saas-Fee ist seit Jahrzehnten autofrei: Sie lassen das Auto am Rand stehen und gehen von dort zu Fuss weiter oder nehmen ein Elektrotaxi."),
        ("Gibt es eine richtige Küche?",
         "Ja, vollständig ausgestattet. Backofen und Herd, Induktionskochfeld, Mikrowelle, Geschirrspüler, Kaffeemaschine und Wasserkocher sowie Gläser und Geschirr für die ganze Gruppe, dazu ein Nussbaumtisch, an dem alle acht gleichzeitig sitzen."),
        ("Eignet sich die Wohnung für Kinder?",
         "Sehr gut. Das Dorf ist autofrei, es gibt also keine Strasse, von der man sie fernhalten müsste. In der Wohnung liegen Spiele für verregnete Nachmittage bereit, reichlich warme Wolldecken, und ein Lift erspart es, am Abend noch jemanden die Treppe hinaufzutragen."),
        ("Ist die Wohnung auch im Sommer offen?",
         "Ja. Die Metro Alpin fährt den ganzen Sommer über auf den Allalingletscher hinauf. Saas-Fee ist einer der wenigen Orte in den Alpen, wo man im Juli Ski fahren und am selben Nachmittag durch Lärchenwald wandern kann."),
        ("Ist die Direktbuchung wirklich günstiger?",
         "Der Übernachtungspreis ist derselbe wie auf den Plattformen. Der Unterschied liegt darin, was obendrauf kommt: Die Plattformen schlagen dem Gast ihre Servicegebühr auf, bei der Direktbuchung entfällt sie. Fragen Sie bei der Gelegenheit gleich nach einem späten Check-out."),
    ],

    "pages": {

        "home": {
            "title": "Luxus-Ferienwohnung Saas-Fee, 8 Personen | Bijou du Glacier",
            "desc": "Neu renovierte Ferienwohnung für acht im autofreien Saas-Fee, Wallis. Vier Kingsize-Betten, drei Badezimmer, vier Gehminuten zu den Pisten.",
            "h1": "Ein Juwel unter dem Gletscher von Saas-Fee",
            "lede": "Acht Gäste. Vier Kingsize-Betten. Ein Nussbaumtisch, an dem alle gleichzeitig sitzen, in einem Dorf, in dem das Lauteste draussen Schuhe auf frischem Schnee sind.",
            "facts": ["8 Personen", "4 Kingsize-Betten", "3 Badezimmer", "4 Min. zu den Pisten"],
            "jump": [
                ("overview", "Die Wohnung"),
                ("gallery", "Bilder"),
                ("location", "Lage"),
                ("resort", "Saas-Fee"),
                ("faq", "Fragen"),
                ("book", "Buchen"),
            ],
            "body": """
<section class="section" id="overview" aria-labelledby="overview-h">
  <div class="wrap">
    <p class="eyebrow reveal">Die Wohnung</p>
    <h2 id="overview-h" class="reveal">Platz genug, dass niemand zurückstecken muss</h2>
    <div class="split">
      <div class="measure reveal">
        <p class="lede">In den meisten Wohnungen für acht Personen muss jemand das kleine Zimmer nehmen. Hier gibt es kein kleines Zimmer.</p>
        <p>Bijou du Glacier belegt das Ostende des zweiten Obergeschosses der Residence du Glacier, eines von Grund auf sanierten Hauses mitten im Dorf. Vier Schlafzimmer, jedes mit eigenem Kingsize-Bett auf einer Hypnos-Matratze, eigenem Fenster und eigenem Morgenlicht. Drei Badezimmer in hellem Stein und dunklem Schiefer: zwei mit tiefer Wanne, das dritte mit Walk-in-Dusche.</p>
        <p>Und ein einziger langer, offener Raum. Küche, Wohnbereich und eine Nussbaumbohle mit Baumkante, an der alle acht gleichzeitig sitzen, damit die Gruppe zusammenbleibt, statt sich über Etagen zu verteilen.</p>
        <p>Und dann der Balkon. Er zieht sich über die ganze Front der Wohnung, gedeckt und mit Blick direkt in die Berge. Bequeme Sitzplätze, Nachmittagssonne, bis das Licht die Gipfel verlässt, und dreizehn Viertausender, die die Unterhaltung übernehmen.</p>
        <p><a href="{apartment}">Der Rundgang, Zimmer für Zimmer</a>.</p>
      </div>
      {{fig|living-wide||(min-width: 900px) 46vw, 92vw}}
    </div>
    {{fig|floorplan|plan reveal|(min-width: 900px) 620px, 92vw}}
  </div>
</section>

<section class="section section-panel" id="gallery" aria-labelledby="gallery-h">
  <div class="wrap">
    <p class="eyebrow reveal">Die Räume</p>
    <h2 id="gallery-h" class="reveal">Bijou du Glacier von innen</h2>
    <p class="measure muted reveal">Die Eleganz einer modernen Chalet-Wohnung: warme alpine Materialien und zeitgemässer Komfort, viel Licht, und aus fast jedem Fenster der Blick auf die Berge.</p>
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
    <p class="eyebrow reveal">Die Lage</p>
    <h2 id="location-h" class="reveal">Vier Minuten zu den Pisten. Welten vom Verkehr.</h2>
    <div class="cols">
      <div class="col reveal">
        <h3>Im Dorf, nicht oberhalb davon</h3>
        <p>Vier Minuten zu den Pisten. Zwanzig Meter zum Supermarkt. Bäckerei, Skiverleih und jedes Restaurant, für das sich der Weg lohnt, liegen noch näher. In einem Ort, in dem man fährt, ist eine zentrale Lage bequem; in einem Dorf, in dem niemand fährt, prägt sie die ganze Woche. Sie kommen an, lassen das Auto am Dorfeingang stehen und denken nie wieder über einen Weg nach.</p>
      </div>
      <div class="col reveal">
        <h3>Dreizehn Viertausender, vom eigenen Balkon</h3>
        <p>Der Balkon zeigt auf die Mischabelgruppe, jenes Massiv mit dem Dom, dem höchsten vollständig auf Schweizer Boden stehenden Gipfel. Morgens läuft das Licht diese Wand hinunter, bevor es das Dorf erreicht. Abends halten es die Gipfel zwanzig Minuten länger als die Gasse darunter, was Grund genug ist, um sieben Uhr noch draussen zu sitzen.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-panel" id="resort" aria-labelledby="resort-h">
  <div class="wrap">
    <p class="eyebrow reveal">Das Dorf</p>
    <h2 id="resort-h" class="reveal">Saas-Fee, die Perle der Alpen</h2>
    <div class="split">
      {{fig|massif||(min-width: 900px) 46vw, 92vw}}
      <div class="measure reveal">
        <p class="lede">Keine Autos. Keine Motoren. Und ein Gletscher direkt darüber, auf dem im Juli so selbstverständlich Ski gefahren wird wie im Januar.</p>
        <p>Saas-Fee liegt auf 1800 Metern in einem Halbkreis aus dreizehn Viertausendern und ist seit Jahrzehnten für den Verkehr geschlossen. Gäste lassen ihr Fahrzeug am Dorfeingang stehen und gehen zu Fuss weiter. Was bleibt, ist ein Dorf, das klingt, wie Bergdörfer klingen sollten.</p>
        <p>Darüber fährt die Metro Alpin im Berginnern auf 3500 Meter zum Allalingletscher, wo der Schnee das ganze Jahr über liegen bleibt. Deshalb trainieren hier im August Nationalmannschaften, und deshalb ist Ihre Saison nie ganz vorbei.</p>
        <p><a href="{resort}">Mehr zu Skifahren, Sommer und Anreise</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="faq" aria-labelledby="faq-h">
  <div class="wrap">
    <p class="eyebrow reveal">Gut zu wissen</p>
    <h2 id="faq-h" class="reveal">Alles, was Sie fragen werden</h2>
    <div class="reveal">{{faq}}</div>
  </div>
</section>

<section class="section section-panel" id="book" aria-labelledby="book-h">
  <div class="wrap">
    <p class="eyebrow reveal">Verfügbarkeit</p>
    <h2 id="book-h" class="reveal">Ihren Aufenthalt reservieren</h2>
    {{reservebox}}
  </div>
</section>
""",
        },

        "apartment": {
            "title": "Ferienwohnung, 4 Schlafzimmer, 8 Personen | Bijou du Glacier",
            "desc": "Zimmer für Zimmer: vier Schlafzimmer mit Hypnos-Kingsize-Betten, offene Küche und Wohnraum, Nussbaumtisch für acht, drei Badezimmer und ein grosser Balkon.",
            "h1": "Die Wohnung, Zimmer für Zimmer",
            "lede": "Breite Eiche, heller Stein, gebürstetes Messing. Modern alpin statt geschnitzter Folklore, und so bemessen, dass acht Personen gut miteinander wohnen, statt bloss hineinzupassen.",
            "jump": [
                ("sleeping", "Schlafen"),
                ("living", "Wohnen"),
                ("kitchen", "Küche"),
                ("bathrooms", "Bäder"),
                ("balcony", "Balkon"),
                ("floorplan", "Grundriss"),
                ("amenities", "Ausstattung"),
                ("practical", "Praktisches"),
                ("gallery", "Bilder"),
            ],
            "body": """
<section class="section" id="sleeping" aria-labelledby="sleeping-h">
  <div class="wrap">
    <p class="eyebrow">Schlafen</p>
    <h2 id="sleeping-h">Vier Schlafzimmer. Vier Kingsize-Betten. Schöne Bergsicht.</h2>
    <div class="split">
      <div class="measure">
        <p>In jedem der vier Schlafzimmer steht ein Kingsize-Bett, und jedes hat ein eigenes Fenster und Tageslicht. Genau darum geht es beim Grundriss: Vier Paare oder zwei Familien teilen sich die Wohnung, ohne dass jemand das kürzere Ende zieht.</p>
        <p>Jedes Bett ist ein Hypnos, weshalb Gäste eher über den Schlaf schreiben als über das Skifahren. Das Hauptschlafzimmer ist raumhoch mit heller Eiche getäfert und hat ein gepolstertes Kopfteil. Die drei anderen sind heller gehalten, mit weissen Wänden, gerahmten Alpendrucken, Wolldecken in Oliv, Rost und Ocker sowie Leselampen auf beiden Seiten.</p>
        <p>In jedem Zimmer Einbauschränke mit Kleiderstange und Tablaren, dazu ein Skidepot im Untergeschoss des Hauses, damit die Ausrüstung von acht Personen nie im Korridor landet.</p>
      </div>
      {{fig|bedroom-3||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="living" aria-labelledby="living-h">
  <div class="wrap">
    <p class="eyebrow">Wohnen</p>
    <h2 id="living-h">Ein Raum, der die ganze Gesellschaft hält</h2>
    <div class="split">
      {{fig|living-corner||(min-width: 900px) 44vw, 92vw}}
      <div class="measure">
        <p>Das Wohnzimmer geht ohne Trennung in die Küche über und bekommt von zwei Seiten Licht. Ein tiefes olivgrünes Sofa, zwei runde Bronze-Couchtische, ein weicher gemusterter Teppich auf breitem Eichenparkett und ein Fernseher, den man nutzen kann, aber gut übersieht, wenn man nicht will.</p>
        <p>Der Raum ist gross genug, dass die eine Hälfte der Gruppe liest, während die andere kocht. Für das Sofa liegen reichlich warme Wolldecken bereit, und in einem Schrank warten Spiele auf den Nachmittag, an dem ein Sturm durchzieht.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="kitchen" aria-labelledby="kitchen-h">
  <div class="wrap">
    <p class="eyebrow">Küche und Essen</p>
    <h2 id="kitchen-h">Eine Küche, die acht Abendessen gewachsen ist</h2>
    <div class="split">
      <div class="measure">
        <p>Vollständig ausgestattet und in weichem Taupe mit Steinrückwand und gebürstetem Messinghahn ausgeführt: Einbaubackofen und Herd, Induktionskochfeld, Mikrowelle, Geschirrspüler, Dunstabzug, Kühlschrank, Wasserkocher und Kaffeemaschine, dazu offene Tablare mit Gläsern, Schalen und Tellern für die ganze Gruppe.</p>
        <p>Der Esstisch ist eine einzige Nussbaumbohle mit Baumkante, dazu schwarze Crossback-Stühle. Acht Plätze, alle am selben Tisch. Für eine Gruppe zu kochen funktioniert nur, wenn Küche und Tisch die ganze Gruppe auf einmal fassen. Hier ist das der Fall.</p>
        <p>Der Supermarkt liegt zwanzig Meter vor der Tür. Der Einkauf ist damit eine Besorgung und keine Expedition.</p>
      </div>
      {{fig|kitchen-oven||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="bathrooms" aria-labelledby="bathrooms-h">
  <div class="wrap">
    <p class="eyebrow">Bäder</p>
    <h2 id="bathrooms-h">Drei Bäder in Stein und Schiefer</h2>
    <div class="split">
      {{fig|bathroom-shower||(min-width: 900px) 44vw, 92vw}}
      <div class="measure">
        <p>Alle drei sind in grossformatigem hellem Stein mit einem Band aus dunklem Schiefer ausgeführt, mit schwebenden Eichenwaschtischen, Steinbecken und hinterleuchteten Spiegeln. Zwei haben eine tiefe Badewanne, was man sich nach einem ganzen Tag auf dem Gletscher wünscht. Das dritte hat eine Walk-in-Dusche.</p>
        <p>Drei Bäder auf acht Personen ist das Verhältnis, mit dem ein Skimorgen aufgeht. Niemand wartet, und um acht Uhr verhandelt niemand über warmes Wasser. Bademäntel, Handtücher und Haartrockner sind vorhanden, für die Wochenwäsche gibt es Waschmaschine und Tumbler.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="balcony" aria-labelledby="balcony-h">
  <div class="wrap">
    <p class="eyebrow">Draussen</p>
    <h2 id="balcony-h">Ein Balkon, von dem man nicht hereinkommen will</h2>
    <div class="split">
      <div class="measure">
        <p>Ein grosser, gedeckter Balkon zieht sich über die ganze Länge der Wohnung, über den Dächern des Dorfes und mit Blick direkt in die Berge. Er ist zum Sitzen möbliert und nicht zum Stehen, mit tiefen Loungesesseln aus Geflecht, niedrigen Tischen und genug Schutz, um bei Schneefall draussen zu bleiben. Dann ist er am schönsten.</p>
        <p>Er blickt auf die Mischabelwand. Morgens läuft das Licht die Flanke hinunter, bevor es das Dorf erreicht. Abends halten es die Gipfel noch zwanzig Minuten, wenn die Gasse darunter längst im Schatten liegt, und bis dahin hat es niemand eilig, hineinzugehen.</p>
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
    <p class="eyebrow">Grundriss</p>
    <h2 id="floorplan-h">Wie die Wohnung aufgeteilt ist</h2>
    <div class="measure">
      <p>Vier Schlafzimmer, drei Badezimmer und ein langer offener Raum, alles auf einer Ebene am Ende des Geschosses. Das Wohnzimmer misst knapp vierzig Quadratmeter, die Schlafzimmer je elf bis vierzehn, und der gedeckte Balkon an der Front kommt mit weiteren fünfundzwanzig dazu.</p>
      <p>Unten sehen Sie den Originalplan des Architekten für die Wohnung B4. Schneller lässt sich nicht klären, wer welches Zimmer bekommt, bevor überhaupt jemand gepackt hat.</p>
    </div>
    {{fig|floorplan|plan|(min-width: 900px) 620px, 92vw}}
  </div>
</section>

<section class="section" id="amenities" aria-labelledby="amenities-h">
  <div class="wrap">
    <p class="eyebrow">Ausstattung</p>
    <h2 id="amenities-h">Was auf Sie wartet</h2>
    {{amenities}}
  </div>
</section>

<section class="section section-panel" id="practical" aria-labelledby="practical-h">
  <div class="wrap">
    <p class="eyebrow">Praktisches</p>
    <h2 id="practical-h">Die Einzelheiten</h2>
    {{facts}}
    <p class="fineprint">Check-in ab 15 Uhr, Check-out flexibel. Schlüssel und die Anmeldung für die Kurtaxe organisiert SaasFeeHolidays.com im Dorf und bestätigt sie vor der Anreise. <a href="{book}">So wird gebucht</a>.</p>
  </div>
</section>

<section class="section" id="gallery" aria-labelledby="gallery-h">
  <div class="wrap">
    <p class="eyebrow">Bilder</p>
    <h2 id="gallery-h">Mehr von der Wohnung</h2>
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
            "title": "Saas-Fee: autofreies Dorf, Gletscherski | Bijou du Glacier",
            "desc": "Wie es ist, in Saas-Fee zu wohnen: autofreies Dorf auf 1800 m, Metro Alpin zum Allalingletscher, Schnee das ganze Jahr und Wandern im Sommer.",
            "h1": "Saas-Fee, die Perle der Alpen",
            "lede": "Ein autofreies Dorf auf 1800 Metern, umstellt von dreizehn Viertausendern, unter einem Gletscher, auf dem im Juli so selbstverständlich Ski gefahren wird wie im Januar.",
            "jump": [
                ("car-free", "Autofrei"),
                ("skiing", "Skifahren"),
                ("summer", "Sommer"),
                ("eating", "Essen"),
                ("getting-here", "Anreise"),
            ],
            "body": """
<section class="section" id="car-free" aria-labelledby="carfree-h">
  <div class="wrap">
    <p class="eyebrow">Das Dorf</p>
    <h2 id="carfree-h">Was ein Dorf ohne Autos tatsächlich verändert</h2>
    <div class="split">
      <div class="measure">
        <p>Gäste stellen ihr Fahrzeug in den Parkhäusern am Dorfeingang ab und gehen zu Fuss weiter. Die wenigen Fahrzeuge im Dorf sind kleine Elektrofahrzeuge: Taxis, Lieferwagen, hin und wieder ein Werkfahrzeug.</p>
        <p>Die Wirkung ist sofort spürbar und schwer zu überschätzen. Kein Verkehrslärm, keine Abgase, kein Trottoirrand, von dem man Kinder fernhalten muss. Gruppen laufen auseinander und finden wieder zusammen, ohne dass jemand an einer Strasse Köpfe zählt. In den meisten Alpenorten ist das seit Jahrzehnten vorbei. In Saas-Fee nie.</p>
        <p>Damit verändert sich auch, was «zentral» wert ist. Weil alles zu Fuss zurückgelegt wird, ist eine Wohnung mitten im Dorf, wie <a href="{apartment}">diese hier</a>, keine kleine Bequemlichkeit, sondern der Unterschied zwischen Ferien mit Logistik und Ferien ohne.</p>
      </div>
      {{fig|village||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="skiing" aria-labelledby="skiing-h">
  <div class="wrap">
    <p class="eyebrow">Winter</p>
    <h2 id="skiing-h">Ein Gletscher über dem Dorf, eine Bahn im Berg</h2>
    <div class="split">
      {{fig|piste-dawn||(min-width: 900px) 44vw, 92vw}}
      <div class="measure">
        <p>Das Skigebiet steigt vom Dorf auf den Allalingletscher. Die Metro Alpin, eine Standseilbahn, die im Berginnern hinauffährt, bringt Skifahrerinnen und Skifahrer auf rund 3500 Meter nach Mittelallalin, wo der Schnee das ganze Jahr über liegen bleibt.</p>
        <p>Diese Höhe ist der Grund, weshalb Saas-Fee früh und spät in der Saison zuverlässig ist, während tiefer gelegene Gebiete auf die Wetterprognose schauen. Das Gelände ist oben weit und offen und wird auf dem Weg ins Dorf schmaler.</p>
        <p>Von der Wohnungstür sind es vier Gehminuten durch das Dorf bis zu den Pisten.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="summer" aria-labelledby="summer-h">
  <div class="wrap">
    <p class="eyebrow">Sommer</p>
    <h2 id="summer-h">Vor dem Mittag Ski. Danach zu Fuss.</h2>
    <div class="split">
      <div class="measure">
        <p>Saas-Fee gehört zu den wenigen Orten in den Alpen, an denen der Gletscher den ganzen Sommer über befahren wird, weshalb im Juli und August Nationalmannschaften hier trainieren. Die Metro Alpin fährt weiter, man steht also vor dem Mittag auf Schnee, ohne einen einzigen Höhenmeter zu Fuss zu machen.</p>
        <p>Unterhalb des Eises beginnt das Wanderland: hohe Wege durch Lärchen und Fels, Alpweiden, und der ganze Halbkreis der Gipfel im Blick. Lange Tage, kühle Nächte, und das Dorf von seiner entspanntesten und, nebenbei, günstigsten Seite.</p>
      </div>
      {{fig|glacier-view||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="eating" aria-labelledby="eating-h">
  <div class="wrap">
    <p class="eyebrow">Abende</p>
    <h2 id="eating-h">Abendessen, so oder so</h2>
    <div class="measure">
      <p>Die Restaurants liegen an und um die Dorfstrasse, alle in Gehdistanz zur Wohnung. Weil nichts weiter als ein paar Minuten entfernt ist, braucht ein Abendessen auswärts keine Planung. Man geht hinunter, isst, geht zurück, und niemand muss nüchtern bleiben, um zu fahren.</p>
      <p>Zu Hause essen ist die andere Hälfte des Arguments für eine Wohnung. Eine Achtergruppe im Hotel bezahlt jeden Abend acht Gedecke zu Hotelpreisen. Hier fassen <a href="{apartment}#kitchen">Küche und Tisch</a> die ganze Gruppe, der Supermarkt liegt zwanzig Meter entfernt, und gekocht wird, wenn einem danach ist.</p>
    </div>
  </div>
</section>

<section class="section" id="getting-here" aria-labelledby="getting-h">
  <div class="wrap">
    <p class="eyebrow">Anreise</p>
    <h2 id="getting-h">Die Anreise</h2>
    <div class="cols cols-3">
      <div class="col">
        <h3>Mit der Bahn</h3>
        <p>Bis Visp an der Hauptlinie durch das Rhonetal, dann mit dem Postauto ins Saastal, rund eine Stunde. Die Haltestelle liegt am Dorfeingang, wenige Gehminuten von der Wohnung entfernt.</p>
      </div>
      <div class="col">
        <h3>Mit dem Auto</h3>
        <p>Von Visp das Tal hinauf, dann in die Parkhäuser am Dorfeingang. Nach Saas-Fee hinein fährt man nicht; das tut niemand. Winterreifen sind ab November das vernünftige Minimum.</p>
      </div>
      <div class="col">
        <h3>Mit dem Flugzeug</h3>
        <p>Genf und Zürich sind beide realistisch, mit Bahn und Bus rund drei bis dreieinhalb Stunden. Im Sommer ist Mailand-Malpensa über den Simplon eine Alternative.</p>
      </div>
    </div>
    <p class="fineprint">Genaue Anreisehinweise und die Schlüsselübergabe kommen von der lokalen Verwaltung, sobald Ihre Daten bestätigt sind. <a href="{book}">Zur Buchung</a>.</p>
  </div>
</section>
""",
        },

        "book": {
            "title": "Direkt buchen ohne Servicegebühr | Bijou du Glacier",
            "desc": "Bijou du Glacier direkt buchen: gleicher Preis wie auf den Plattformen, ohne deren Servicegebühr. Vier Schlafzimmer, acht Personen, autofreies Saas-Fee.",
            "h1": "Ihren Aufenthalt buchen",
            "lede": "Die Wohnung ist über mehrere Kanäle buchbar. Wir empfehlen zuerst den direkten Weg, und die Begründung ist Rechenkunde, nicht Sentiment.",
            "jump": [
                ("direct", "Direkt buchen"),
                ("platforms", "Plattformen"),
                ("before-you-book", "Vor der Buchung"),
            ],
            "body": """
<section class="section" id="direct" aria-labelledby="direct-h">
  <div class="wrap">
    <p class="eyebrow">Direkt</p>
    <h2 id="direct-h">Direkt bei der Wohnung buchen</h2>
    <div class="measure">
      <p>Der Übernachtungspreis ist überall derselbe. Wir unterbieten die Plattformen nicht und dürfen es auch nicht. Unterschiedlich ist, was dazukommt: Die Plattformen verrechnen dem Gast ihre Servicegebühr, bei der Direktbuchung entfällt sie.</p>
      <p>Wer direkt bucht, spricht ausserdem von der ersten Nachricht an mit SaasFeeHolidays.com im Dorf statt mit einem Plattform-Postfach. Das klingt nebensächlich, ist es aber nicht, sobald es um einen späten Check-out oder einen frühen Schlüssel geht.</p>
    </div>
    {{bookblock}}
  </div>
</section>

<section class="section section-panel" id="platforms" aria-labelledby="platforms-h">
  <div class="wrap">
    <p class="eyebrow">Die Alternativen</p>
    <h2 id="platforms-h">Oder Sie finden uns auf den Plattformen</h2>
    <div class="measure">
      <p>Wenn Sie lieber dort buchen, wo Sie bereits ein Konto, eine hinterlegte Zahlungsart und eine Stornohistorie haben, ist das völlig nachvollziehbar. Die folgenden Inserate zeigen dieselbe Wohnung.</p>
    </div>
    {{platforms}}
  </div>
</section>

<section class="section" id="before-you-book" aria-labelledby="before-h">
  <div class="wrap">
    <p class="eyebrow">Gut zu wissen</p>
    <h2 id="before-h">Vor der Buchung</h2>
    <div class="cols">
      <div class="col">
        <h3>Bei wem Sie buchen</h3>
        <p>Eine privat gehaltene Wohnung, betreut von SaasFeeHolidays.com, einer Verwaltung an der Untere Dorfstrasse im Dorf. Keine Kette, kein Portfolio. Eine Wohnung, in einem Haus, mit einem Schlüsselbund.</p>
      </div>
      <div class="col">
        <h3>Zahlung und Stornierung</h3>
        <p>Zahlungsplan und Stornobedingungen teilt Ihnen SaasFeeHolidays.com bei der Bestätigung Ihrer Daten mit, bevor etwas fällig wird.</p>
        </div>
      <div class="col">
        <h3>Kurtaxe und Anmeldung</h3>
        <p>Schweizer Gemeinden verlangen eine Gästeanmeldung und erheben pro Person und Nacht eine Kurtaxe, die vor Ort eingezogen wird. Sie ist nicht im Übernachtungspreis enthalten und keine Buchungsgebühr.</p>
      </div>
      <div class="col">
        </div>
      <div class="col">
        <h3>Noch am Überlegen?</h3>
        <p>Am ehesten helfen <a href="{apartment}">die Beschreibung Zimmer für Zimmer</a> und <a href="{resort}">der Text darüber, wie Saas-Fee wirklich ist</a>, besonders wenn Sie noch nie in einem autofreien Dorf gewohnt haben.</p>
      </div>
    </div>
  </div>
</section>
""",
        },
    },

    "alt": {
        "patio-hero": "Ein Loungesessel aus Geflecht mit mauvefarbenem Kissen auf dem gedeckten Balkon der Wohnung, in der Nachmittagssonne über dem Lärchenwald des Saastals.",
        "patio-chair": "Ein runder Loungesessel aus Geflecht mit tiefem mauvefarbenem Kissen und ein niedriger runder Beistelltisch auf dem Balkon neben der Glastür, mit Blick über Lärchenwald und ein Chaletdach auf der anderen Talseite.",
        "patio-seating": "Der gedeckte Balkon über die ganze Länge der Wohnung, unter dunkler Holzdecke, mit Loungesesseln aus Geflecht und mauvefarbenen Kissen entlang eines schmiedeeisernen Geländers, zwei niedrigen runden Tischen und den Dächern von Saas-Fee darunter.",
        "floorplan": "Architektengrundriss der Wohnung B4 im zweiten Obergeschoss der Residence du Glacier: vier Schlafzimmer und drei Badezimmer um einen zentralen Eingangsbereich, ein offener Wohn-, Ess- und Küchenbereich entlang der Front und ein gedeckter Balkon über die ganze Breite.",
        "hero-video": "Ein Rundgang durch die Wohnung: die Piste und die Mischabelwand über Saas-Fee, dann Wohnzimmer, Küche, alle vier Schlafzimmer, die Bäder und der Balkon.",
        "piste-dawn": "Frisch präparierte Piste, die sich im ersten Licht über ein Schneefeld oberhalb von Saas-Fee hinunterzieht, dahinter Fels und Eis der Mischabelwand.",
        "dining-band": "Der lange Nussbaumtisch mit Baumkante, für acht gedeckt, in ganzer Länge durch den offenen Wohnraum gesehen, an einem Ende die Küche, dahinter eine Steinwand.",
        "massif": "Die vergletscherte Wand der Mischabelgruppe über Saas-Fee, weite Schneefelder und blau beschattete Grate über den Dächern des Dorfes.",
        "living-room": "Der offene Wohnraum der Ferienwohnung in Saas-Fee mit olivgrünem Sofa, runden Bronze-Couchtischen, gemustertem Teppich auf breitem Eichenparkett und Fenstern auf zwei Seiten.",
        "kitchen-shelves": "Offene Küchentablare mit weissem Geschirr und Gläsern über einer Steinarbeitsfläche, daneben Messinghahn, Wasserkocher und Messerblock.",
        "master-bedroom": "Das Hauptschlafzimmer mit Kingsize-Bett vor einer raumhoch in heller Eiche getäferten Wand, olivfarbener Steppdecke, rostroten Kissen und gerahmtem Alpendruck.",
        "balcony-view": "Der grosse gedeckte Balkon der Ferienwohnung mit schmiedeeisernem Geländer, Blick über die verschneiten Dächer von Saas-Fee zu den Bergen.",
        "living-wide": "Wohn- und Essbereich der Vierzimmer-Ferienwohnung in Saas-Fee im Zusammenhang, mit hohen Fenstern zum verschneiten Dorf und zu den Bergen.",
        "coffee-table": "Zwei runde zweistöckige Bronze-Couchtische auf einem weichen cremefarbenen Teppich vor dem olivgrünen Sofa im Wohnzimmer.",
        "living-corner": "Eine ruhige Ecke des Wohnzimmers mit hellem Sofa, senffarbenem Kissen, Bogenstehlampe und zwei Spiegeln mit organischer Kante an der Wand.",
        "dining-table": "Der lange Nussbaumtisch mit Baumkante und schwarzen Crossback-Stühlen, für acht gedeckt vor der offenen Küche, dahinter eine Steinwand.",
        "dining-walnut": "Der Nussbaumtisch vom Küchenende her gesehen, mit einer hellen Schale in der Mitte und den Wohnzimmerfenstern dahinter.",
        "kitchen": "Die vollständig ausgestattete Küche der Ferienwohnung in Saas-Fee in weichem Taupe mit Steinrückwand, Backofen und Induktionskochfeld, im Vordergrund der Esstisch.",
        "kitchen-oven": "Die Küchenzeile mit Einbaubackofen und Kaffeemaschine unter warmer Tablarbeleuchtung, direkt am Esstisch.",
        "kitchen-tap": "Nahaufnahme des gebürsteten Messinghahns und der Steinrückwand, daneben Kupferwasserkocher und Küchenwerkzeug auf der Arbeitsfläche.",
        "bedroom-2": "Das zweite Schlafzimmer mit Kingsize-Bett in weisser Bettwäsche, ockerfarbenen und schokoladenbraunen Kissen, warmen Nachttischlampen und gerahmtem Druck über dem Kopfteil.",
        "bedroom-3": "Das dritte Schlafzimmer mit Kingsize-Bett, hohem geriffeltem cremefarbenem Kopfteil, schokoladenbraunen Kissen und beidseitig brennenden Lampen.",
        "bedroom-4": "Das vierte Schlafzimmer mit Kingsize-Bett, hohem geriffeltem Eichenschrank, Stehlampe und tief gesetztem Fenster zum Dorf.",
        "wardrobe": "Ein offener Einbauschrank aus Eiche mit Kleiderstange und Tablaren, Stauraum für eine Achtergruppe.",
        "blanket": "Eine gefaltete Schweizer Wolldecke mit rotem Kreuzstreifen über der Lehne eines Bouclé-Sessels.",
        "bathroom": "Eines der drei Badezimmer in grossformatigem hellem Stein mit schwebendem Eichenwaschtisch, Steinbecken, Messinghahn und hinterleuchtetem Spiegel.",
        "bathroom-shower": "Die Walk-in-Dusche hinter Klarglas, dunkler Schiefer gegen hellen Stein, daneben hinterleuchteter Spiegel und Eichenwaschtisch.",
        "bathroom-bath": "Eine der beiden tiefen Badewannen vor einem Band aus dunklem Schiefer, daneben eine Glastür mit Blick in den Schnee.",
        "robe-door": "Ein weisser Bademantel an einer Fischgrät-Eichentür in der Wohnung.",
        "village": "Die verschneiten Dächer des autofreien Saas-Fee in der Dämmerung, eine Piste führt ins Dorf hinunter, dahinter die Berge.",
        "glacier-view": "Die hohen vergletscherten Gipfel über Saas-Fee im Sommerlicht, von den Fenstern der Wohnung über die Dächer hinweg gesehen.",
        "share": "Die vergletscherte Mischabelwand über dem Dorf Saas-Fee im Wallis.",
    },

    "caption": {
        "patio-chair": "Die Ecke bei der Tür, wo die Sonne zuerst ankommt.",
        "patio-seating": "Die ganze Länge, gedeckt, mit dem Dorf darunter.",
        "floorplan": "Der Originalplan des Architekten für die Wohnung B4, mit dem Treppenhaus, das direkt vor die Wohnungstür führt.",
        "living-wide": "Wohnzimmer und Küche, offen ineinander.",
        "coffee-table": "Bronze, Eiche, Wolle, die Palette der Renovation.",
        "living-corner": "Eine Ecke zum Lesen, während in der Küche gearbeitet wird.",
        "dining-table": "Ein Tisch, acht Plätze, dahinter eine voll ausgestattete Küche: Geschirrspüler, Mikrowelle, Herd und Backofen, Kaffeemaschine.",
        "dining-walnut": "Eine einzige Nussbaumbohle mit Baumkante.",
        "kitchen": "Voll ausgestattet und gross genug für eine Gruppe.",
        "kitchen-oven": "Backofen, Kochfeld und Kaffeemaschine unter der Tablarbeleuchtung.",
        "kitchen-tap": "Gebürstetes Messing auf Stein.",
        "bedroom-2": "Zweites Schlafzimmer.",
        "bedroom-3": "Drittes Schlafzimmer.",
        "bedroom-4": "Viertes Schlafzimmer.",
        "wardrobe": "Kleiderstange und Tablare in jedem Zimmer.",
        "blanket": "Wolle, wo man sie braucht.",
        "bathroom": "Stein, Schiefer und Eiche.",
        "bathroom-shower": "Die Walk-in-Dusche.",
        "bathroom-bath": "Eine tiefe Wanne, mit Fenster in den Schnee.",
        "robe-door": "Bademäntel vorhanden.",
        "village": "Saas-Fee in der Dämmerung, mit der Piste ins Dorf.",
        "glacier-view": "Der Gletscher, von den Fenstern aus.",
        "dining-band": "Ein Tisch, acht Plätze, ein Raum.",
        "massif": "Die Mischabelwand, direkt vor dem Balkon.",
        "piste-dawn": "Erstes Licht auf der Piste über dem Dorf.",
        "balcony-view": "Der Balkon, über den Dächern des Dorfes.",
    },

    "footer": {
        "explore": "Entdecken",
        "book": "Buchen",
        "contact": "Das Objekt",
        "address": "Residence du Glacier · Blomattenstrasse 2 · 3906 Saas-Fee · Wallis · Schweiz",
        "fine": "Eine privat gehaltene Vierzimmer-Ferienwohnung in Saas-Fee, lokal betreut.",
    },

    "next": {
        "apartment": ("Die Wohnung, Zimmer für Zimmer", "Vier Schlafzimmer, Küche, Bäder und Balkon, mit allen praktischen Angaben in einer Tabelle."),
        "resort": ("Saas-Fee", "Ein autofreies Dorf auf 1800 m, der Gletscher darüber und wie man herkommt."),
        "book": ("Direkt buchen", "Gleicher Übernachtungspreis wie auf den Plattformen, ohne deren Servicegebühr."),
        "home": ("Übersicht", "Wohnung, Dorf und Bilder auf einer Seite."),
    },
}
