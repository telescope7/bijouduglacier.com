# -*- coding: utf-8 -*-
"""
Français (usage suisse romand).

RÈGLE DE MAISON : aucun tiret cadratin « — » dans ce fichier. Il sent la
rédaction automatique. Là où il y en avait un, la phrase a été reconstruite
autour d'un point, d'un deux-points ou d'une virgule. audit.py fait échouer le
build si l'un d'eux revient.

Intention de recherche visée :
  appartement saas-fee · location appartement saas-fee · appartement 8 personnes
  saas-fee · appartement de vacances valais · chalet saas-fee · location ski saas-fee
Choix volontaires : « appartement de vacances » et « location » plutôt que la
traduction littérale de l'anglais ; « village sans voitures » (formule officielle
de Saas-Fee) ; « parquer » et « car postal », qui sont l'usage romand.
"""

FR = {
    "lang": "fr",
    "name": "Français",
    "locale": "fr_CH",
    "dir_label": "FR",

    "ui": {
        "skip": "Aller au contenu principal",
        "brand_sub": "Saas-Fee · Valais · Suisse",
        "home_label": "Accueil",
        "lang_label": "Choisir une langue",
        "jump_label": "Sur cette page",
        "nav_label": "Navigation principale",
        "crumb_label": "Fil d'Ariane",
        "book_cta": "Réserver en direct au meilleur tarif",
        "book_cta_short": "Réserver en direct",
        "note": "Le tarif par nuit est identique à celui des plateformes. Réserver auprès de nous retire simplement leurs frais de service de votre total, et vous met en relation dès le premier message avec les personnes qui veillent sur l'appartement.",
        "book_block_title": "Réserver en direct",
        "or_label": "Ou retrouvez le même appartement sur",
        "next_label": "Poursuivre",
        "gallery_note": "Photographies de l'appartement dans son état actuel, après rénovation.",
    },

    "nav": {
        "home": "Aperçu",
        "apartment": "L'appartement",
        "resort": "Saas-Fee",
        "book": "Réserver",
    },

    "amenities": [
        "Quatre chambres doubles : deux lits king size, deux en lits jumelables",
        "Les deux chambres jumelables faites en king size ou en lits simples, au choix",
        "Literie et matelas Hypnos dans toutes les chambres",
        "Huit personnes",
        "Trois salles de bains : deux baignoires profondes et une douche à l'italienne",
        "Séjour et cuisine ouverts l'un sur l'autre",
        "Cuisine entièrement équipée",
        "Table en noyer pour huit personnes",
        "Four, cuisinière, plaque à induction et micro-ondes",
        "Lave-vaisselle",
        "Machine à café et bouilloire",
        "Lave-linge et sèche-linge",
        "Internet haut débit dans tout l'appartement",
        "Télévision au séjour",
        "Grand balcon face aux sommets",
        "Mobilier de balcon pour les longs après-midis",
        "Ascenseur jusqu'à l'appartement",
        "Casier à skis dans l'immeuble",
        "Armoires encastrées et rangement pour le matériel",
        "Linge de lit, serviettes et sèche-cheveux fournis",
        "Shampooing, après-shampooing, gel douche et savon fournis",
        "Stores occultants dans chaque chambre",
        "Cintres et rangement dans chaque chambre",
        "Quantité de plaids bien chauds",
        "Jeux pour les enfants",
        "Produits d'entretien à disposition",
        "Parquet en chêne, chaleureux et silencieux",
        "Détecteurs de fumée et de monoxyde de carbone",
        "Non-fumeurs, animaux non admis",
        "Quatre minutes à pied des pistes",
        "Au cœur du village sans voitures",
        "Immeuble entièrement rénové",
        "Pas de climatisation : à 1800 mètres, personne ne l'a jamais regrettée",
    ],

    "facts_table": {
        "caption": "Tout ce que l'on souhaite voir confirmé avant d'y consacrer une semaine.",
        "rows": [
            ("Capacité", "8 personnes"),
            ("Chambres", "4 doubles. Deux en lit king size, deux jumelables en king size ou lits simples"),
            ("Salles de bains", "3 : deux avec baignoire profonde, une avec douche à l'italienne"),
            ("Adresse", "Residence du Glacier, Blomattenstrasse 2, 3906 Saas-Fee, Valais, Suisse"),
            ("Distance des pistes", "Quatre minutes à pied, à travers le village"),
            ("Supermarché le plus proche", "À vingt mètres de la porte"),
            ("Rangement à skis", "Un casier au sous-sol de l'immeuble"),
            ("Ascenseur", "Oui, jusqu'à la porte de l'appartement"),
            ("Parking", "Dans les parkings de l'entrée du village. Saas-Fee est sans voitures."),
            ("Gare la plus proche", "Viège, puis le car postal jusqu'au fond de la vallée (environ une heure)"),
            ("Arrivée / départ", "À partir de 15 h ; départ flexible"),
            ("Géré par", "SaasFeeHolidays.com, au village"),
            ("Ouverture", "Hiver et été"),
        ],
    },

    "faq": [
        ("Combien de personnes l'appartement peut-il accueillir ?",
         "Huit, dans quatre chambres, toutes doubles. Deux ont un lit king size fixe. Les deux autres sont en lits jumelables : deux lits simples qui s'assemblent en king size, selon ce qui convient au groupe. Dites-nous avant l'arrivée et les lits seront faits en conséquence. Tous les matelas sont des Hypnos. Pas de canapé-lit, pas de mezzanine, pas de pièce qui se révèle être un réduit avec une fenêtre."),
        ("L'appartement est-il ski aux pieds (ski-in / ski-out) ?",
         "Non, et nous préférons le dire clairement. Bijou du Glacier se trouve au cœur même du village, à quatre minutes à pied des pistes. Saas-Fee étant sans voitures, tout le monde se déplace de toute façon à pied. Mais si vous voulez chausser devant la porte, ce n'est pas cet appartement-là."),
        ("Où met-on les skis ?",
         "Un casier à skis se trouve au sous-sol de l'immeuble, compris avec l'appartement, et un ascenseur monte jusqu'à la porte. Beaucoup d'hôtes laissent malgré tout leurs skis en haut, aux pistes : quatre minutes de marche en chaussures de ski, c'est quatre minutes mieux employées au petit-déjeuner."),
        ("Où peut-on parquer ?",
         "Dans les parkings couverts situés à l'entrée du village. Saas-Fee est sans voitures depuis des décennies : vous laissez la voiture à l'entrée et continuez à pied, ou en taxi électrique du village."),
        ("Y a-t-il une vraie cuisine ?",
         "Oui, entièrement équipée. Four et cuisinière, plaque à induction, micro-ondes, lave-vaisselle, machine à café et bouilloire, verrerie et vaisselle pour tout le groupe, et une table en noyer à bord naturel où les huit convives tiennent en même temps."),
        ("Est-ce adapté aux enfants ?",
         "Tout à fait. Le village est sans voitures, il n'y a donc pas de route dont il faille les écarter. L'appartement dispose de jeux pour les après-midis pluvieux, de quantité de plaids bien chauds, et d'un ascenseur qui évite de porter qui que ce soit dans les escaliers en fin de journée."),
        ("L'appartement est-il ouvert en été ?",
         "Oui. Le Metro Alpin monte au glacier de l'Allalin tout l'été. Saas-Fee est l'un des rares endroits des Alpes où l'on peut skier en juillet et redescendre marcher sous les mélèzes le même après-midi."),
        ("Réserver en direct est-il vraiment moins cher ?",
         "Le tarif par nuit est le même que sur les plateformes. La différence est ce qui vient s'ajouter par-dessus : les plateformes facturent leurs frais de service au client, la réservation en direct non. Profitez-en pour demander un départ tardif."),
    ],

    "pages": {

        "home": {
            "title": "Appartement de luxe 4 chambres, Saas-Fee | Bijou du Glacier",
            "desc": "Appartement de quatre chambres pour huit au cœur de Saas-Fee sans voitures. King size ou lits simples, trois salles de bains, quatre minutes des pistes.",
            "h1": "Un bijou sous le glacier, au cœur de Saas-Fee",
            "lede": "Huit personnes. Quatre chambres doubles, faites en king size ou en lits simples selon le groupe. Une table en noyer assez longue pour tous, dans un village où le bruit le plus fort, dehors, ce sont les chaussures sur la neige fraîche.",
            "facts": ["8 personnes", "4 chambres doubles", "3 salles de bains", "4 min des pistes"],
            "jump": [
                ("overview", "L'appartement"),
                ("gallery", "Photographies"),
                ("location", "Situation"),
                ("resort", "Saas-Fee"),
                ("faq", "Questions"),
                ("book", "Réserver"),
            ],
            "body": """
<section class="section" id="overview" aria-labelledby="overview-h">
  <div class="wrap">
    <p class="eyebrow reveal">L'appartement</p>
    <h2 id="overview-h" class="reveal">Assez d'espace pour que personne ne cède</h2>
    <div class="split">
      <div class="measure reveal">
        <p class="lede">Dans la plupart des appartements pour huit, quelqu'un doit prendre la petite chambre. Ici, il n'y a pas de petite chambre.</p>
        <p>Bijou du Glacier occupe l'extrémité est du deuxième étage de la Residence du Glacier, un immeuble rénové de fond en comble, au cœur même du village. Quatre chambres, chacune avec son lit king size sur un matelas Hypnos, sa fenêtre et sa lumière du matin. Trois salles de bains en pierre claire et ardoise sombre : deux avec baignoire profonde, la troisième avec douche à l'italienne.</p>
        <p>Et une seule longue pièce ouverte. Cuisine, séjour et une planche de noyer à bord naturel où les huit s'assoient ensemble, pour que le groupe reste réuni au lieu de se disperser d'un étage à l'autre.</p>
        <p>Et puis il y a le balcon. Il court sur toute la façade de l'appartement, couvert, et regarde droit vers la montagne. Des assises confortables, le soleil de l'après-midi jusqu'à ce que la lumière quitte les sommets, et treize sommets de plus de quatre mille mètres qui se chargent du spectacle.</p>
        <p><a href="{apartment}">La visite, pièce par pièce</a>.</p>
      </div>
      {{fig|living-wide||(min-width: 900px) 46vw, 92vw}}
    </div>
    {{fig|floorplan|plan reveal|(min-width: 900px) 620px, 92vw}}
  </div>
</section>

<section class="section section-panel" id="gallery" aria-labelledby="gallery-h">
  <div class="wrap">
    <p class="eyebrow reveal">Les pièces</p>
    <h2 id="gallery-h" class="reveal">L'intérieur de Bijou du Glacier</h2>
    <p class="measure muted reveal">L'élégance d'un appartement de chalet contemporain : matériaux alpins chaleureux et confort d'aujourd'hui, beaucoup de lumière, et la montagne à presque chaque fenêtre.</p>
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
    <p class="eyebrow reveal">L'adresse</p>
    <h2 id="location-h" class="reveal">À quatre minutes des pistes. À des lieues de la circulation.</h2>
    <div class="cols">
      <div class="col reveal">
        <h3>Dans le village, pas au-dessus</h3>
        <p>Quatre minutes des pistes. Vingt mètres du supermarché. La boulangerie, la location de skis et chaque restaurant qui vaut le détour sont plus près encore. Dans une station où l'on roule, être au centre est un confort ; dans un village où personne ne roule, cela dessine toute la semaine. Vous arrivez, vous laissez la voiture à l'entrée, et vous ne pensez plus jamais au trajet.</p>
      </div>
      <div class="col reveal">
        <h3>Treize quatre-mille, depuis votre balcon</h3>
        <p>Le balcon regarde les Mischabel, le massif qui porte le Dom, le plus haut sommet entièrement situé en Suisse. Le matin, la lumière descend cette paroi avant d'atteindre le village. Le soir, les sommets la retiennent vingt minutes de plus que la rue en contrebas, ce qui suffit à expliquer pourquoi l'on est encore dehors à sept heures.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-panel" id="resort" aria-labelledby="resort-h">
  <div class="wrap">
    <p class="eyebrow reveal">Le village</p>
    <h2 id="resort-h" class="reveal">Saas-Fee, la Perle des Alpes</h2>
    <div class="split">
      {{fig|massif||(min-width: 900px) 46vw, 92vw}}
      <div class="measure reveal">
        <p class="lede">Pas de voitures. Pas de moteurs. Et un glacier juste au-dessus, que l'on skie en juillet aussi naturellement qu'en janvier.</p>
        <p>Saas-Fee se tient à 1800 mètres dans un fer à cheval de treize sommets de plus de quatre mille mètres, et le village est fermé à la circulation depuis des décennies. Les visiteurs laissent leur voiture à l'entrée et continuent à pied. Il reste un village qui sonne comme un village de montagne devrait sonner.</p>
        <p>Au-dessus, le Metro Alpin monte à l'intérieur de la montagne jusqu'au glacier de l'Allalin, à 3500 mètres, où la neige tient toute l'année. C'est pourquoi des équipes nationales s'y entraînent en août, et pourquoi votre saison n'est jamais tout à fait finie.</p>
        <p><a href="{resort}">Le ski, l'été et l'accès</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="faq" aria-labelledby="faq-h">
  <div class="wrap">
    <p class="eyebrow reveal">Bon à savoir</p>
    <h2 id="faq-h" class="reveal">Tout ce que vous allez demander</h2>
    <div class="reveal">{{faq}}</div>
  </div>
</section>

<section class="section section-panel" id="book" aria-labelledby="book-h">
  <div class="wrap">
    <p class="eyebrow reveal">Disponibilités</p>
    <h2 id="book-h" class="reveal">Réservez votre séjour</h2>
    {{reservebox}}
  </div>
</section>
""",
        },

        "apartment": {
            "title": "Appartement 4 chambres, huit personnes | Bijou du Glacier",
            "desc": "Pièce par pièce : quatre chambres doubles sur literie Hypnos, en king size ou lits simples, cuisine ouverte, table en noyer pour huit, trois salles de bains, grand balcon.",
            "h1": "L'appartement, pièce par pièce",
            "lede": "Chêne large, pierre claire, laiton brossé. Alpin contemporain plutôt que pastiche de bois sculpté, et dimensionné pour que huit personnes vivent bien ensemble, et non simplement y tiennent.",
            "jump": [
                ("sleeping", "Chambres"),
                ("living", "Séjour"),
                ("kitchen", "Cuisine"),
                ("bathrooms", "Salles de bains"),
                ("balcony", "Balcon"),
                ("floorplan", "Plan"),
                ("amenities", "Équipement"),
                ("practical", "Pratique"),
                ("gallery", "Photographies"),
            ],
            "body": """
<section class="section" id="sleeping" aria-labelledby="sleeping-h">
  <div class="wrap">
    <p class="eyebrow">Chambres</p>
    <h2 id="sleeping-h">Quatre chambres doubles. King size ou lits simples, à votre choix.</h2>
    <div class="split">
      <div class="measure">
        <p>Les quatre chambres sont doubles, et chacune a sa propre fenêtre et sa lumière du jour. Deux ont un lit king size fixe. Les deux autres sont en lits jumelables : deux lits simples qui s'assemblent en king size.</p>
        <p>C'est plus utile que quatre king size fixes. Quatre couples ont quatre king size. Deux familles ont deux king size et quatre lits simples pour les enfants. Indiquez la configuration souhaitée à la réservation et les lits seront faits avant votre arrivée. Personne ne tire la courte paille.</p>
        <p>Chaque lit est un Hypnos, ce qui explique pourquoi les hôtes écrivent sur leurs nuits plutôt que sur leurs journées de ski. La chambre principale est lambrissée du sol au plafond en chêne clair, avec une tête de lit capitonnée. Les trois autres sont plus claires : murs blancs, gravures alpines encadrées, plaids de laine olive, rouille et ocre, et une lampe de lecture de chaque côté.</p>
        <p>Des armoires encastrées dans chaque chambre, penderie et étagères, et un casier à skis au sous-sol de l'immeuble, pour que le matériel de huit personnes ne finisse jamais dans le couloir.</p>
      </div>
      {{fig|bedroom-3||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="living" aria-labelledby="living-h">
  <div class="wrap">
    <p class="eyebrow">Séjour</p>
    <h2 id="living-h">Une pièce qui tient toute la tablée</h2>
    <div class="split">
      {{fig|living-corner||(min-width: 900px) 44vw, 92vw}}
      <div class="measure">
        <p>Le séjour se prolonge dans la cuisine sans cloison et prend la lumière sur deux côtés. Un canapé profond vert olive, deux tables basses rondes en bronze, un tapis doux à motifs sur un large parquet de chêne, et une télévision qui est là si on la veut et facile à oublier sinon.</p>
        <p>La pièce est assez vaste pour que la moitié du groupe lise pendant que l'autre cuisine. Il y a quantité de plaids bien chauds pour le canapé, et une armoire de jeux pour l'après-midi où passe une tempête.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="kitchen" aria-labelledby="kitchen-h">
  <div class="wrap">
    <p class="eyebrow">Cuisine et repas</p>
    <h2 id="kitchen-h">Une cuisine à la hauteur de huit dîners</h2>
    <div class="split">
      <div class="measure">
        <p>Entièrement équipée, et aménagée en taupe clair avec crédence de pierre et robinetterie en laiton brossé : four encastré et cuisinière, plaque à induction, micro-ondes, lave-vaisselle, hotte, réfrigérateur, bouilloire et machine à café, avec des étagères ouvertes pour les verres, les bols et les assiettes de tout le groupe.</p>
        <p>La table est une planche unique de noyer à bord naturel, entourée de chaises noires à dossier croisé. Huit places, toutes à la même table. Cuisiner pour un groupe ne fonctionne que si la cuisine et la table encaissent le groupe entier d'un coup. C'est le cas ici.</p>
        <p>Le supermarché est à vingt mètres de la porte : faire les courses relève de la commission, pas de l'expédition.</p>
      </div>
      {{fig|kitchen-oven||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="bathrooms" aria-labelledby="bathrooms-h">
  <div class="wrap">
    <p class="eyebrow">Salles de bains</p>
    <h2 id="bathrooms-h">Trois salles de bains, pierre et ardoise</h2>
    <div class="split">
      {{fig|bathroom-shower||(min-width: 900px) 44vw, 92vw}}
      <div class="measure">
        <p>Les trois sont finies en pierre claire grand format avec un bandeau d'ardoise foncée, meubles de chêne suspendus, vasques en pierre et miroirs rétroéclairés. Deux ont une baignoire profonde, ce dont on rêve après une journée entière sur le glacier. La troisième a une douche à l'italienne.</p>
        <p>Trois salles de bains pour huit personnes, c'est le rapport qui permet à un matin de ski de fonctionner. Personne ne fait la queue, personne ne négocie l'eau chaude à huit heures. Peignoirs, serviettes et sèche-cheveux fournis, et un lave-linge avec sèche-linge pour le matériel de la semaine.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="balcony" aria-labelledby="balcony-h">
  <div class="wrap">
    <p class="eyebrow">Dehors</p>
    <h2 id="balcony-h">Un balcon dont vous n'aurez pas envie de rentrer</h2>
    <div class="split">
      <div class="measure">
        <p>Un grand balcon couvert court sur toute la longueur de l'appartement, au-dessus des toits du village et tourné droit vers la montagne. Il est meublé pour s'asseoir et non pour rester debout, avec de profonds fauteuils lounge en tressage, des tables basses et assez d'abri pour rester dehors quand il neige. C'est alors qu'il est le plus beau.</p>
        <p>Il regarde la paroi des Mischabel. Le matin, la lumière descend la face avant d'atteindre le village. Le soir, les sommets la retiennent encore vingt minutes alors que la rue est déjà à l'ombre, et à ce moment-là personne n'est pressé de rentrer.</p>
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
    <p class="eyebrow">Plan</p>
    <h2 id="floorplan-h">Comment l'appartement est distribué</h2>
    <div class="measure">
      <p>Quatre chambres, trois salles de bains et une longue pièce ouverte, le tout de plain-pied à l'extrémité de l'étage. Le séjour approche les quarante mètres carrés, les chambres font entre onze et quatorze chacune, et le balcon couvert en façade en ajoute vingt-cinq.</p>
      <p>Ci-dessous, le plan d'origine de l'architecte pour l'appartement B4. C'est le moyen le plus rapide de décider qui prend quelle chambre, avant même que quiconque ait fait ses valises.</p>
    </div>
    {{fig|floorplan|plan|(min-width: 900px) 620px, 92vw}}
  </div>
</section>

<section class="section" id="amenities" aria-labelledby="amenities-h">
  <div class="wrap">
    <p class="eyebrow">Équipement</p>
    <h2 id="amenities-h">Ce qui vous attend</h2>
    {{amenities}}
  </div>
</section>

<section class="section section-panel" id="practical" aria-labelledby="practical-h">
  <div class="wrap">
    <p class="eyebrow">Pratique</p>
    <h2 id="practical-h">Les détails</h2>
    {{facts}}
    <p class="fineprint">Arrivée à partir de 15 h, départ flexible. Les clés et l'enregistrement pour la taxe de séjour sont gérés par SaasFeeHolidays.com, au village, et confirmés avant votre départ. <a href="{book}">Voir comment réserver</a>.</p>
  </div>
</section>

<section class="section" id="gallery" aria-labelledby="gallery-h">
  <div class="wrap">
    <p class="eyebrow">Photographies</p>
    <h2 id="gallery-h">L'appartement, suite</h2>
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
            "title": "Saas-Fee : sans voitures, ski sur glacier | Bijou du Glacier",
            "desc": "Séjourner à Saas-Fee : village sans voitures à 1800 m, Metro Alpin jusqu'au glacier de l'Allalin, neige toute l'année et randonnée d'altitude en été.",
            "h1": "Saas-Fee, la Perle des Alpes",
            "lede": "Un village sans voitures à 1800 mètres, cerné de treize quatre-mille, sous un glacier que l'on skie en juillet aussi naturellement qu'en janvier.",
            "jump": [
                ("car-free", "Sans voitures"),
                ("skiing", "Ski"),
                ("summer", "Été"),
                ("eating", "Restaurants"),
                ("getting-here", "Accès"),
            ],
            "body": """
<section class="section" id="car-free" aria-labelledby="carfree-h">
  <div class="wrap">
    <p class="eyebrow">Le village</p>
    <h2 id="carfree-h">Ce qu'un village sans voitures change réellement</h2>
    <div class="split">
      <div class="measure">
        <p>Les visiteurs laissent leur véhicule dans les parkings de l'entrée et continuent à pied. Les rares véhicules qui circulent dans le village sont de petits engins électriques : taxis, chariots de livraison, un véhicule technique de temps à autre.</p>
        <p>L'effet est immédiat et difficile à exagérer. Pas de bruit de circulation, pas de gaz d'échappement, pas de bord de route dont il faut écarter les enfants. Les groupes se dispersent et se retrouvent sans que personne ne compte les têtes devant une chaussée. La plupart des stations alpines ont cessé d'être ainsi il y a des décennies. Saas-Fee, jamais.</p>
        <p>Cela change aussi ce que vaut le mot « central ». Comme tout se fait à pied, un appartement au milieu du village, <a href="{apartment}">comme celui-ci</a>, n'est pas un confort marginal. C'est la différence entre des vacances avec logistique et des vacances sans.</p>
      </div>
      {{fig|village||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="skiing" aria-labelledby="skiing-h">
  <div class="wrap">
    <p class="eyebrow">Hiver</p>
    <h2 id="skiing-h">Un glacier au-dessus du village, un funiculaire dans la montagne</h2>
    <div class="split">
      {{fig|piste-dawn||(min-width: 900px) 44vw, 92vw}}
      <div class="measure">
        <p>Le domaine s'élève depuis le village jusqu'au glacier de l'Allalin. Le Metro Alpin, un funiculaire souterrain qui monte à l'intérieur de la montagne, dépose les skieurs à Mittelallalin, vers 3500 mètres, là où la neige tient toute l'année.</p>
        <p>Cette altitude explique la fiabilité de Saas-Fee en début et en fin de saison, quand les domaines plus bas scrutent les prévisions. Le terrain est large et ouvert en haut, puis se resserre dans les mélèzes au retour.</p>
        <p>Les pistes sont à quatre minutes à pied de la porte de l'appartement, à travers le village.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="summer" aria-labelledby="summer-h">
  <div class="wrap">
    <p class="eyebrow">Été</p>
    <h2 id="summer-h">Ski avant midi. Marche après.</h2>
    <div class="split">
      <div class="measure">
        <p>Saas-Fee fait partie de la poignée d'endroits des Alpes où le glacier se skie tout l'été, ce qui explique que des équipes nationales y campent en juillet et en août. Le Metro Alpin continue de circuler : vous êtes sur la neige avant midi sans un mètre de dénivelé à pied.</p>
        <p>Sous la glace commence le pays de la marche : sentiers d'altitude entre mélèzes et rochers, alpages, et tout le fer à cheval de sommets en vue. Journées longues, nuits fraîches, et le village dans sa version la plus détendue et, accessoirement, la moins chère.</p>
      </div>
      {{fig|glacier-view||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="eating" aria-labelledby="eating-h">
  <div class="wrap">
    <p class="eyebrow">Soirées</p>
    <h2 id="eating-h">Dîner, dans un sens ou dans l'autre</h2>
    <div class="measure">
      <p>Les restaurants se trouvent sur la rue principale et autour, tous à distance de marche de l'appartement. Comme rien n'est à plus de quelques minutes, sortir dîner ne demande jamais d'organisation. On descend, on mange, on remonte, et personne ne doit rester sobre pour conduire.</p>
      <p>Manger chez soi est l'autre moitié de l'argument en faveur d'un appartement. Un groupe de huit à l'hôtel paie huit couverts au tarif de l'hôtel tous les soirs. Ici, <a href="{apartment}#kitchen">la cuisine et la table</a> encaissent tout le groupe, le supermarché est à vingt mètres, et l'on cuisine quand on en a envie.</p>
    </div>
  </div>
</section>

<section class="section" id="getting-here" aria-labelledby="getting-h">
  <div class="wrap">
    <p class="eyebrow">Accès</p>
    <h2 id="getting-h">L'arrivée</h2>
    <div class="cols cols-3">
      <div class="col">
        <h3>En train</h3>
        <p>Jusqu'à Viège, sur la ligne principale de la vallée du Rhône, puis le car postal jusqu'au fond de la vallée de Saas, environ une heure. L'arrêt est à l'entrée du village, à quelques minutes à pied de l'appartement.</p>
      </div>
      <div class="col">
        <h3>En voiture</h3>
        <p>Depuis Viège, on remonte la vallée jusqu'aux parkings de l'entrée du village. On n'entre pas en voiture dans Saas-Fee ; personne ne le fait. Les pneus d'hiver sont le minimum raisonnable dès novembre.</p>
      </div>
      <div class="col">
        <h3>En avion</h3>
        <p>Genève et Zurich sont toutes deux réalistes, à environ trois heures à trois heures et demie en train et en car. Milan Malpensa est une option en été, par le Simplon.</p>
      </div>
    </div>
    <p class="fineprint">Les indications d'arrivée précises et la remise des clés viennent de la régie locale une fois vos dates confirmées. <a href="{book}">Modalités de réservation</a>.</p>
  </div>
</section>
""",
        },

        "book": {
            "title": "Réserver en direct, sans frais | Bijou du Glacier",
            "desc": "Réservez Bijou du Glacier en direct : le même tarif que sur les plateformes, sans leurs frais de service. Quatre chambres, huit personnes, à Saas-Fee.",
            "h1": "Réserver votre séjour",
            "lede": "L'appartement se réserve par plusieurs canaux. Nous indiquons le direct en premier, et la raison tient de l'arithmétique plutôt que du sentiment.",
            "jump": [
                ("direct", "En direct"),
                ("platforms", "Plateformes"),
                ("before-you-book", "Avant de réserver"),
            ],
            "body": """
<section class="section" id="direct" aria-labelledby="direct-h">
  <div class="wrap">
    <p class="eyebrow">Direct</p>
    <h2 id="direct-h">Réserver directement auprès de l'appartement</h2>
    <div class="measure">
      <p>Le tarif par nuit est le même partout. Nous ne cassons pas les prix des plateformes, et nous n'en avons pas le droit. Ce qui diffère, c'est ce qui s'ajoute par-dessus : les plateformes facturent leurs frais de service au client, et la réservation en direct, non.</p>
      <p>Réserver en direct vous met aussi en relation avec SaasFeeHolidays.com, au village, dès le premier message plutôt qu'avec une messagerie de plateforme. Cela paraît secondaire, et cela cesse de l'être au moment où l'on souhaite un départ tardif ou des clés en avance.</p>
    </div>
    {{bookblock}}
  </div>
</section>

<section class="section section-panel" id="platforms" aria-labelledby="platforms-h">
  <div class="wrap">
    <p class="eyebrow">Les alternatives</p>
    <h2 id="platforms-h">Ou retrouvez-nous sur les plateformes</h2>
    <div class="measure">
      <p>Si vous préférez réserver là où vous avez déjà un compte, un moyen de paiement enregistré et un historique d'annulations, c'est parfaitement légitime. Les annonces ci-dessous portent sur le même appartement.</p>
    </div>
    {{platforms}}
  </div>
</section>

<section class="section" id="before-you-book" aria-labelledby="before-h">
  <div class="wrap">
    <p class="eyebrow">Bon à savoir</p>
    <h2 id="before-h">Avant de réserver</h2>
    <div class="cols">
      <div class="col">
        <h3>Auprès de qui vous réservez</h3>
        <p>Un appartement privé, entretenu par Adam et l'équipe de SaasFeeHolidays.com, établie au village, à l'Untere Dorfstrasse. Pas une chaîne, pas un portefeuille de biens. Un appartement, dans un immeuble, avec un seul trousseau de clés.</p>
        <p>Ce n'est pas leur premier hiver. Neuf ans à recevoir des hôtes à Saas-Fee, le statut Superhost sur Airbnb et <strong>308 avis, avec une moyenne de 4,76 sur 5</strong>, sur les appartements dont ils s'occupent au village. Ils vivent ici toute l'année, savent quel restaurant vaut le déplacement en février, et ce sont eux qui répondront à vos messages et vous remettront les clés.</p>
      </div>
      <div class="col">
        <h3>Paiement et annulation</h3>
        <p>L'échéancier de paiement et les conditions d'annulation vous sont communiqués par SaasFeeHolidays.com à la confirmation de vos dates, avant tout versement.</p>
        </div>
      <div class="col">
        <h3>Taxe de séjour et enregistrement</h3>
        <p>Les communes suisses exigent l'enregistrement des hôtes et perçoivent une taxe de séjour par personne et par nuit, encaissée sur place. Elle n'est pas comprise dans le tarif par nuit et n'est pas des frais de réservation.</p>
      </div>
      <div class="col">
        </div>
      <div class="col">
        <h3>Encore hésitant ?</h3>
        <p>Les deux textes à lire en priorité sont <a href="{apartment}">la description pièce par pièce</a> et <a href="{resort}">ce qu'est réellement Saas-Fee</a>, surtout si vous n'avez jamais séjourné dans un village sans voitures.</p>
      </div>
    </div>
  </div>
</section>
""",
        },
    },

    "alt": {
        "patio-hero": "Un fauteuil lounge en tressage avec un coussin mauve sur le balcon couvert de l'appartement, au soleil de l'après-midi, au-dessus des mélèzes de la vallée de Saas.",
        "patio-chair": "Un fauteuil lounge rond en tressage avec un coussin mauve profond et une table d'appoint ronde et basse sur le balcon, près des portes vitrées, avec vue sur les mélèzes et le toit d'un chalet de l'autre côté de la vallée.",
        "patio-seating": "Le balcon couvert sur toute la longueur de l'appartement, sous un plafond de bois sombre, avec des fauteuils lounge en tressage et des coussins mauves le long d'une balustrade en fer forgé, deux tables basses rondes, et les toits de Saas-Fee en contrebas.",
        "floorplan": "Plan d'architecte de l'appartement B4 au deuxième étage de la Residence du Glacier : quatre chambres et trois salles de bains autour d'un hall d'entrée central, un séjour, un coin repas et une cuisine ouverts en façade, et un balcon couvert sur toute la largeur.",
        "hero-video": "Une visite de l'appartement : la piste et la paroi des Mischabel au-dessus de Saas-Fee, puis le séjour, la cuisine, les quatre chambres, les salles de bains et le balcon.",
        "piste-dawn": "Piste fraîchement damée descendant un champ de neige au-dessus de Saas-Fee aux premières lueurs, avec le rocher et la glace de la paroi des Mischabel derrière.",
        "dining-band": "La longue table en noyer à bord naturel dressée pour huit, vue dans la longueur de la pièce ouverte, la cuisine à un bout et un mur de pierre en fond.",
        "massif": "La muraille glaciaire du massif des Mischabel au-dessus de Saas-Fee, vastes champs de neige et arêtes aux ombres bleues au-dessus des toits du village.",
        "living-room": "Le séjour ouvert de l'appartement de Saas-Fee, canapé vert olive, tables basses rondes en bronze, tapis à motifs sur large parquet de chêne et fenêtres sur deux côtés.",
        "kitchen-shelves": "Étagères ouvertes de la cuisine, vaisselle blanche et verres au-dessus d'un plan de travail en pierre, robinet en laiton brossé, bouilloire et bloc à couteaux.",
        "master-bedroom": "La chambre principale, lit king size contre un lambris de chêne clair toute hauteur, courtepointe olive, coussins rouille et gravure alpine encadrée.",
        "balcony-view": "Le grand balcon couvert de l'appartement, garde-corps en fer forgé, vue sur les toits enneigés de Saas-Fee et les sommets au-delà.",
        "living-wide": "Séjour et coin repas de l'appartement de quatre chambres à Saas-Fee vus ensemble, hautes fenêtres ouvertes sur le village enneigé et les montagnes.",
        "coffee-table": "Deux tables basses rondes à deux plateaux en bronze sur un tapis crème, devant le canapé vert olive du séjour.",
        "living-corner": "Un coin tranquille du séjour, canapé clair, coussin moutarde, lampadaire arqué et deux miroirs aux contours organiques au mur.",
        "dining-table": "La longue table en noyer à bord naturel et ses chaises noires à dossier croisé, dressée pour huit devant la cuisine ouverte, mur de pierre en fond.",
        "dining-walnut": "La table en noyer vue depuis la cuisine, une coupe claire en son centre et les fenêtres du séjour au-delà.",
        "kitchen": "La cuisine entièrement équipée de l'appartement de Saas-Fee, taupe clair, crédence de pierre, four encastré et plaque à induction, table à manger au premier plan.",
        "kitchen-oven": "Le linéaire de cuisine avec four encastré et machine à café sous un éclairage d'étagère chaleureux, donnant directement sur la table.",
        "kitchen-tap": "Gros plan sur le robinet en laiton brossé et la crédence de pierre, bouilloire en cuivre et ustensiles sur le plan de travail.",
        "bedroom-2": "La deuxième chambre, lit king size en linge blanc, coussins ocre et chocolat, lampes de chevet allumées et gravure encadrée au-dessus de la tête de lit.",
        "bedroom-3": "La troisième chambre, lit king size, haute tête de lit crème cannelée, coussins brun chocolat et lampes allumées de part et d'autre.",
        "bedroom-4": "La quatrième chambre, lit king size, haute armoire de chêne cannelé, lampadaire et fenêtre en embrasure donnant sur le village.",
        "wardrobe": "Une armoire encastrée en chêne ouverte, penderie et étagères, rangement pour un groupe de huit.",
        "blanket": "Une couverture de laine suisse pliée, bande rouge à croix, posée sur l'accoudoir d'un fauteuil en bouclette.",
        "bathroom": "L'une des trois salles de bains, en grande pierre claire, meuble suspendu en chêne, vasque en pierre, robinet en laiton brossé et miroir rétroéclairé.",
        "bathroom-shower": "La douche à l'italienne derrière une paroi de verre, ardoise foncée contre pierre claire, à côté du miroir rétroéclairé et du meuble de chêne.",
        "bathroom-bath": "L'une des deux baignoires profondes, devant un bandeau d'ardoise foncée, avec une porte vitrée ouvrant sur la neige.",
        "robe-door": "Un peignoir blanc suspendu à une porte de chêne à chevrons dans l'appartement.",
        "village": "Les toits enneigés de Saas-Fee, village sans voitures, au crépuscule, avec une piste qui descend dans le village et les sommets derrière.",
        "glacier-view": "Les hauts sommets glaciaires au-dessus de Saas-Fee dans la lumière d'été, vus des fenêtres de l'appartement par-dessus les toits.",
        "share": "La paroi glaciaire des Mischabel au-dessus du village de Saas-Fee, en Valais.",
    },

    "caption": {
        "patio-chair": "Le coin près des portes, là où le soleil arrive en premier.",
        "patio-seating": "Toute sa longueur, à couvert, le village en contrebas.",
        "floorplan": "Le plan d'origine de l'architecte pour l'appartement B4. Les libellés sont en allemand : Zimmer une chambre, Bad une salle de bains, Dusche la douche, Küche la cuisine, Wohnzimmer le séjour, Balkon le balcon.",
        "living-wide": "Séjour et cuisine, ouverts l'un sur l'autre.",
        "coffee-table": "Bronze, chêne et laine, la palette de la rénovation.",
        "living-corner": "Un coin pour lire pendant que la cuisine s'active.",
        "dining-table": "Une table, huit places, et derrière elle une cuisine entièrement équipée : lave-vaisselle, micro-ondes, cuisinière et four, machine à café.",
        "dining-walnut": "Une planche unique de noyer à bord naturel.",
        "kitchen": "Entièrement équipée, et dimensionnée pour un groupe.",
        "kitchen-oven": "Four, plaque et machine à café sous l'éclairage d'étagère.",
        "kitchen-tap": "Laiton brossé sur pierre.",
        "bedroom-2": "Deuxième chambre.",
        "bedroom-3": "Troisième chambre.",
        "bedroom-4": "Quatrième chambre.",
        "wardrobe": "Penderie et étagères dans chaque chambre.",
        "blanket": "De la laine, là où il en faut.",
        "bathroom": "Pierre, ardoise et chêne.",
        "bathroom-shower": "La douche à l'italienne.",
        "bathroom-bath": "Une baignoire profonde, fenêtre sur la neige.",
        "robe-door": "Peignoirs fournis.",
        "village": "Saas-Fee au crépuscule, la piste descendant au village.",
        "glacier-view": "Le glacier, depuis les fenêtres.",
        "dining-band": "Une table, huit places, une seule pièce.",
        "massif": "La paroi des Mischabel, droit devant le balcon.",
        "piste-dawn": "Premières lueurs sur la piste au-dessus du village.",
        "balcony-view": "Le balcon, au-dessus des toits du village.",
    },

    "footer": {
        "explore": "Explorer",
        "book": "Réserver",
        "contact": "L'objet",
        "address": "Residence du Glacier · Blomattenstrasse 2 · 3906 Saas-Fee · Valais · Suisse",
        "fine": "Appartement privé de quatre chambres à Saas-Fee, géré localement.",
    },

    "next": {
        "apartment": ("L'appartement, pièce par pièce", "Quatre chambres, la cuisine, les salles de bains et le balcon, avec les informations pratiques en tableau."),
        "resort": ("Saas-Fee", "Un village sans voitures à 1800 m, le glacier au-dessus, et comment y venir."),
        "book": ("Réserver en direct", "Le même tarif par nuit que sur les plateformes, sans leurs frais de service."),
        "home": ("Aperçu", "L'appartement, le village et les photographies sur une seule page."),
    },
}
