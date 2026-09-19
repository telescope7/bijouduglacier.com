# -*- coding: utf-8 -*-
"""
English content.

HOUSE RULE: no em dashes anywhere in this file. They read as machine-written.
Where one was doing real work, the sentence has been rebuilt around a full stop,
a colon or a comma instead. audit.py fails the build if one creeps back in.
"""

EN = {
    "lang": "en",
    "name": "English",
    "locale": "en_GB",
    "dir_label": "EN",

    # ---- keyword intent this language is written against ------------------
    # saas fee apartment / apartment saas fee / 4 bedroom apartment saas fee /
    # saas fee luxury apartment / saas fee accommodation sleeps 8 /
    # ski apartment saas fee / saas fee chalet apartment
    "ui": {
        "skip": "Skip to the main content",
        "brand_sub": "Saas-Fee · Valais · Switzerland",
        "home_label": "Home",
        "lang_label": "Choose a language",
        "jump_label": "On this page",
        "nav_label": "Main",
        "crumb_label": "Breadcrumb",
        "book_cta": "Book direct for the best rate",
        "book_cta_short": "Book Direct",
        "note": "The nightly rate is identical to the platforms. Booking with us simply takes their service fee off your total, and puts you in touch with the people who look after the apartment from your very first message.",
        "book_block_title": "Book direct",
        "or_label": "Or find the same apartment on",
        "next_label": "Continue",
        "gallery_note": "Photographs of the apartment as it is now, after the renovation.",
    },

    "nav": {
        "home": "Overview",
        "apartment": "The apartment",
        "resort": "Saas-Fee",
        "book": "Book",
    },

    "amenities": [
        "Four double bedrooms: two king beds, two zip-and-link",
        "Zip-and-link rooms made up as a king or twins, your choice",
        "Hypnos beds and mattresses throughout",
        "Sleeps eight",
        "Three bathrooms: two deep baths and a walk-in shower",
        "Open-plan living room and kitchen",
        "Fully equipped kitchen",
        "Walnut dining table seating eight",
        "Oven, induction hob, range and microwave",
        "Dishwasher",
        "Coffee maker and kettle",
        "Washing machine and tumble dryer",
        "High-speed internet throughout",
        "Television in the living room",
        "Large balcony facing the mountains",
        "Balcony furniture for long afternoons",
        "Lift access to the apartment",
        "Ski locker in the building",
        "Fitted wardrobes and storage for kit",
        "Bed linen, towels and hairdryer provided",
        "Shampoo, conditioner, shower gel and soap provided",
        "Room-darkening blinds in every bedroom",
        "Hangers and clothing storage in every room",
        "Plenty of warm blankets",
        "Games for the children",
        "Cleaning supplies provided",
        "Oak floors, underfloor-warm and quiet",
        "Smoke and carbon-monoxide detectors",
        "Non-smoking, no pets",
        "Four minutes' walk from the slopes",
        "Car-free village location",
        "The whole building newly renovated",
        "No air conditioning: at 1,800 m it has never been missed",
    ],

    "facts_table": {
        "caption": "Everything you would want confirmed before you commit a week to it.",
        "rows": [
            ("Sleeps", "8 guests"),
            ("Bedrooms", "4 doubles. Two king beds; two zip-and-link, made up as a king or twins"),
            ("Bathrooms", "3: two with deep baths, one with a walk-in shower"),
            ("Address", "Residence du Glacier, Blomattenstrasse 2, 3906 Saas-Fee, Valais, Switzerland"),
            ("Distance to the slopes", "A four-minute walk through the village"),
            ("Nearest supermarket", "Twenty metres from the door"),
            ("Ski storage", "A ski locker in the basement of the building"),
            ("Lift", "Yes, to the apartment door"),
            ("Parking", "In the car parks at the village entrance. Saas-Fee is car-free."),
            ("Nearest station", "Visp, then the postbus up the valley (about an hour)"),
            ("Check-in / check-out", "From 3pm; check-out is flexible"),
            ("Managed by", "SaasFeeHolidays.com, in the village"),
            ("Open", "Winter and summer"),
        ],
    },

    "faq": [
        ("How many people does the apartment sleep?",
         "Eight, in four bedrooms, all of them doubles. Two have fixed king-size beds. The other two are zip-and-link: two singles that join into a king, so they can be made up whichever way suits your group. Say which you want before you arrive and they will be ready. Every bed is a Hypnos. No sofa beds, no mezzanines, and no room that turns out to be a cupboard with a window."),
        ("Is the apartment ski-in, ski-out?",
         "No, and we would rather say so plainly. Bijou du Glacier stands in the very heart of the village, a four-minute walk from the slopes. Saas-Fee is car-free, so everyone walks everywhere in any case. But if a ski-in, ski-out door is what you are after, this is not that apartment."),
        ("Where do the skis go?",
         "There is a ski locker in the basement of the building, included with the apartment, and a lift up to the door. Many guests still leave their skis at the slopes overnight, on the grounds that four minutes each way in ski boots is four minutes better spent at breakfast."),
        ("Where do we park?",
         "In the covered car parks at the entrance to the village. Saas-Fee has been car-free for decades: you leave the car at the edge, and from there it is a short walk or a village electric taxi to the door."),
        ("Is there a proper kitchen?",
         "Yes, fully equipped. Oven and range, induction hob, microwave, dishwasher, coffee maker and kettle, and enough glassware and crockery for the whole party, with a live-edge walnut table that seats eight without anyone eating off their lap."),
        ("Is it good for children?",
         "Very. The village is car-free, so there is no road to keep them off, and the apartment has games for wet afternoons, plenty of warm blankets, and a lift that saves carrying anyone up the stairs at the end of a long day."),
        ("Is it open in summer?",
         "Yes. The Metro Alpin runs up to the Allalin glacier through the summer, so Saas-Fee is one of the few places in the Alps where you can ski in July and walk below the treeline the same afternoon."),
        ("Is booking direct actually cheaper?",
         "The nightly rate is the same as on the platforms. The difference is what sits on top of it: the platforms add their own service fee to the guest's total, and booking direct does not. Ask about a flexible check-out while you are at it."),
    ],

    "pages": {

        # ==================================================================
        "home": {
            "title": "Luxury 4-Bedroom Apartment, Saas-Fee | Bijou du Glacier",
            "desc": "A newly renovated four-bedroom apartment for eight in car-free Saas-Fee, Valais. Kings or twins, three bathrooms, four minutes from the slopes. Book direct.",
            "h1": "A jewel beneath the glacier in car-free Saas-Fee",
            "lede": "Eight guests. Four double bedrooms, made up as kings or twins to suit the party. A walnut table long enough for every one of them, in a village where the loudest thing outside is boots on new snow.",
            "facts": ["Sleeps 8", "4 double bedrooms", "3 bathrooms", "4 min to the slopes"],
            "jump": [
                ("overview", "The apartment"),
                ("gallery", "Photographs"),
                ("location", "Location"),
                ("resort", "Saas-Fee"),
                ("faq", "Questions"),
                ("book", "Book"),
            ],
            "body": """
<section class="section" id="overview" aria-labelledby="overview-h">
  <div class="wrap">
    <p class="eyebrow reveal">The apartment</p>
    <h2 id="overview-h" class="reveal">Room enough that nobody has to compromise</h2>
    <div class="split">
      <div class="measure reveal">
        <p class="lede">Most apartments that sleep eight ask somebody to take the small room. This one has no small room.</p>
        <p>Bijou du Glacier occupies the east end of the second floor of Residence du Glacier, a building renovated from the ground up, in the very heart of the village. Four double bedrooms, each on Hypnos mattresses, each with its own window and its own morning light. Two have king-size beds; the other two are zip-and-link, made up as a king or as twins, whichever your group needs. Three bathrooms in pale stone and dark slate: two with deep baths, the third with a walk-in shower.</p>
        <p>And one long open room. Kitchen, sitting room and a live-edge walnut table that seats all eight at once, so the party stays together instead of scattering across floors.</p>
        <p>Then there is the balcony. It runs the whole front of the apartment, covered, and faces straight into the mountains. Comfortable seating, afternoon sun until the light leaves the summits, and thirteen four-thousand-metre peaks doing the entertaining.</p>
        <p><a href="{apartment}">Take the tour, room by room</a>.</p>
      </div>
      {{fig|living-wide||(min-width: 900px) 46vw, 92vw}}
    </div>
    {{fig|floorplan|plan reveal|(min-width: 900px) 620px, 92vw}}
  </div>
</section>

<section class="section section-panel" id="gallery" aria-labelledby="gallery-h">
  <div class="wrap">
    <p class="eyebrow reveal">The rooms</p>
    <h2 id="gallery-h" class="reveal">Inside Bijou du Glacier</h2>
    <p class="measure muted reveal">The elegance of a modern chalet apartment: warm alpine materials and contemporary comfort throughout, generous light, and mountain views from almost every window.</p>
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
    <p class="eyebrow reveal">The address</p>
    <h2 id="location-h" class="reveal">Four minutes from the slopes. A world from the traffic.</h2>
    <div class="cols">
      <div class="col reveal">
        <h3>In the village, not above it</h3>
        <p>Four minutes to the slopes. Twenty metres to the supermarket. The bakery, the ski hire and every restaurant worth the walk are closer still. In a resort where you drive, being central is a convenience; in a village where nobody drives, it is the entire shape of the week. You arrive, you leave the car at the entrance, and you never think about getting anywhere again.</p>
      </div>
      <div class="col reveal">
        <h3>Thirteen four-thousanders, from your own balcony</h3>
        <p>The balcony faces the Mischabel, the massif that carries the Dom, the highest summit standing entirely on Swiss soil. Morning light comes down that face before it reaches the village. In the evening the summits hold it twenty minutes longer than the street below, which is reason enough to still be sitting out there at seven.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-panel" id="resort" aria-labelledby="resort-h">
  <div class="wrap">
    <p class="eyebrow reveal">The village</p>
    <h2 id="resort-h" class="reveal">Saas-Fee, the Pearl of the Alps</h2>
    <div class="split">
      {{fig|massif||(min-width: 900px) 46vw, 92vw}}
      <div class="measure reveal">
        <p class="lede">No cars. No engines. A glacier directly overhead that skis in July as readily as in January.</p>
        <p>Saas-Fee stands at 1,800 metres inside a horseshoe of thirteen four-thousand-metre peaks, and it has been closed to traffic for decades. Visitors leave their cars at the entrance and continue on foot. What is left is a village that sounds the way alpine villages are supposed to sound.</p>
        <p>Above it, the Metro Alpin climbs inside the mountain to the Allalin glacier at 3,500 metres, where the snow holds all year. It is why national teams train here in August, and why your season is never quite over.</p>
        <p><a href="{resort}">More on the skiing, the summer and how to arrive</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="faq" aria-labelledby="faq-h">
  <div class="wrap">
    <p class="eyebrow reveal">Good to know</p>
    <h2 id="faq-h" class="reveal">Everything you will want to ask</h2>
    <div class="reveal">{{faq}}</div>
  </div>
</section>

<section class="section section-panel" id="book" aria-labelledby="book-h">
  <div class="wrap">
    <p class="eyebrow reveal">Availability</p>
    <h2 id="book-h" class="reveal">Reserve your stay</h2>
    {{reservebox}}
  </div>
</section>
""",
        },

        # ==================================================================
        "apartment": {
            "title": "Four-Bedroom Apartment, Sleeps Eight | Bijou du Glacier",
            "desc": "Room by room: four double bedrooms on Hypnos beds, made up as kings or twins, an open kitchen and living room, a walnut table for eight, three bathrooms and a large balcony.",
            "h1": "The apartment, room by room",
            "lede": "Wide oak, pale stone, brushed brass. Modern alpine rather than carved-pine pastiche, and scaled so that eight people live well together rather than merely fit.",
            "jump": [
                ("sleeping", "Sleeping"),
                ("living", "Living"),
                ("kitchen", "Kitchen"),
                ("bathrooms", "Bathrooms"),
                ("balcony", "Balcony"),
                ("floorplan", "Floor plan"),
                ("amenities", "What's included"),
                ("practical", "Practical"),
                ("gallery", "Photographs"),
            ],
            "body": """
<section class="section" id="sleeping" aria-labelledby="sleeping-h">
  <div class="wrap">
    <p class="eyebrow">Sleeping</p>
    <h2 id="sleeping-h">Four double bedrooms. Kings or twins, your choice.</h2>
    <div class="split">
      <div class="measure">
        <p>All four bedrooms are doubles, and each has its own window and daylight. Two have fixed king-size beds. The other two are zip-and-link: two single beds that join into a king, so the room can be made up either way.</p>
        <p>That is more useful than four fixed kings would be. Four couples get four kings. Two families get two kings and four singles for the children. Tell the local team which arrangement you want when you book, and the beds will be made up that way before you arrive. Nobody draws the short straw either way.</p>
        <p>Every bed is a Hypnos, which is why guests tend to write about how well they slept rather than about the skiing. The master bedroom is panelled floor to ceiling in pale oak with an upholstered headboard. The other three are lighter, with white walls, framed alpine prints, wool throws in olive, rust and ochre, and reading lamps on both sides.</p>
        <p>Fitted wardrobes in each room, with hanging space and shelves, and a ski locker in the basement of the building, so eight people's kit never ends up living in the hallway.</p>
      </div>
      {{fig|bedroom-3||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="living" aria-labelledby="living-h">
  <div class="wrap">
    <p class="eyebrow">Living</p>
    <h2 id="living-h">One room that holds the whole party</h2>
    <div class="split">
      {{fig|living-corner||(min-width: 900px) 44vw, 92vw}}
      <div class="measure">
        <p>The living room runs into the kitchen with nothing between them, and takes light from windows on two sides. A deep olive sofa, a pair of round bronze coffee tables, a soft patterned rug over wide oak boards, and a television that is there if you want it and easy to ignore if you don't.</p>
        <p>It is a big enough room that half the party can be reading while the other half is cooking, which is not true of most four-bedroom apartments at this size. There are plenty of warm blankets for the sofa, and a cupboard of games for the afternoon a storm comes through.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="kitchen" aria-labelledby="kitchen-h">
  <div class="wrap">
    <p class="eyebrow">Kitchen and eating</p>
    <h2 id="kitchen-h">A kitchen equal to eight dinners</h2>
    <div class="split">
      <div class="measure">
        <p>Fully equipped, and fitted in soft taupe with a stone splashback and a brushed-brass tap: built-in oven and range, induction hob, microwave, dishwasher, extractor, fridge, kettle and coffee maker, with open shelving for glasses, bowls and plates enough for the full party.</p>
        <p>The dining table is a single live-edge walnut board with black cross-back chairs. Eight places, all at the same table. Cooking for a group only works if the kitchen and the table can take the whole group at once, and this one can.</p>
        <p>The supermarket is twenty metres from the door, which makes a food shop an errand rather than an expedition.</p>
      </div>
      {{fig|kitchen-oven||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="bathrooms" aria-labelledby="bathrooms-h">
  <div class="wrap">
    <p class="eyebrow">Bathrooms</p>
    <h2 id="bathrooms-h">Three bathrooms in stone and slate</h2>
    <div class="split">
      {{fig|bathroom-shower||(min-width: 900px) 44vw, 92vw}}
      <div class="measure">
        <p>All three are finished in large-format pale stone with a band of dark slate, floating oak vanities, stone basins and backlit mirrors. Two have deep baths, which is what you want after a full day on the glacier. The third has a walk-in shower.</p>
        <p>Three bathrooms for eight people is the ratio that makes a ski morning work. Nobody queues, and nobody negotiates for hot water at eight o'clock. Robes, towels and a hairdryer are provided, and there is a washing machine and tumble dryer for the week's kit.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="balcony" aria-labelledby="balcony-h">
  <div class="wrap">
    <p class="eyebrow">Outside</p>
    <h2 id="balcony-h">A balcony you will not want to come in from</h2>
    <div class="split">
      <div class="measure">
        <p>A large covered balcony runs the full length of the apartment, above the village roofs and facing straight into the mountains. It is furnished for sitting rather than standing, with deep woven lounge chairs, low tables and enough shelter to stay out in falling snow, which is when it is at its best.</p>
        <p>It looks onto the Mischabel wall. In the morning the light comes down the face before it reaches the village. In the evening the summits hold it for another twenty minutes after the street below is already in shadow, and by then nobody is in any hurry to go inside.</p>
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
    <p class="eyebrow">Layout</p>
    <h2 id="floorplan-h">How the apartment fits together</h2>
    <div class="measure">
      <p>Four bedrooms, three bathrooms and one long open room, all on one level at the end of the floor. The living room runs to nearly forty square metres, the bedrooms are between eleven and fourteen each, and the covered balcony along the front adds another twenty-five.</p>
      <p>Below is the architect's own drawing for apartment B4. It is the quickest way to settle who takes which room, before anybody has started packing.</p>
    </div>
    {{fig|floorplan|plan|(min-width: 900px) 620px, 92vw}}
  </div>
</section>

<section class="section" id="amenities" aria-labelledby="amenities-h">
  <div class="wrap">
    <p class="eyebrow">What's included</p>
    <h2 id="amenities-h">What is waiting for you</h2>
    {{amenities}}
  </div>
</section>

<section class="section section-panel" id="practical" aria-labelledby="practical-h">
  <div class="wrap">
    <p class="eyebrow">Practical</p>
    <h2 id="practical-h">The particulars</h2>
    {{facts}}
    <p class="fineprint">Check-in is from 3pm and check-out is flexible. Keys and the tourist-tax registration are handled by SaasFeeHolidays.com, in the village, and confirmed with you before you travel. <a href="{book}">See how to book</a>.</p>
  </div>
</section>

<section class="section" id="gallery" aria-labelledby="gallery-h">
  <div class="wrap">
    <p class="eyebrow">Photographs</p>
    <h2 id="gallery-h">More of the apartment</h2>
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

        # ==================================================================
        "resort": {
            "title": "Saas-Fee: Car-Free Village, Glacier Ski | Bijou du Glacier",
            "desc": "What staying in Saas-Fee is like: a car-free village at 1,800 m, the Metro Alpin to the Allalin glacier, year-round snow and high walking in summer.",
            "h1": "Saas-Fee, the Pearl of the Alps",
            "lede": "A car-free village at 1,800 metres, ringed by thirteen four-thousand-metre peaks, beneath a glacier that skis in July as readily as in January.",
            "jump": [
                ("car-free", "Car-free"),
                ("skiing", "Skiing"),
                ("summer", "Summer"),
                ("eating", "Eating out"),
                ("getting-here", "Getting here"),
            ],
            "body": """
<section class="section" id="car-free" aria-labelledby="carfree-h">
  <div class="wrap">
    <p class="eyebrow">The village</p>
    <h2 id="carfree-h">What a village without cars actually changes</h2>
    <div class="split">
      <div class="measure">
        <p>Visitors leave their vehicles in the car parks at the entrance and continue on foot. The few vehicles inside the village are small electric ones: taxis, delivery carts, the odd works vehicle.</p>
        <p>The effect is immediate and difficult to overstate. There is no traffic noise, no exhaust, and no kerb to keep children off. Groups spread out and reconvene without anyone counting heads at a road. Most alpine resorts stopped being like this decades ago. Saas-Fee never did.</p>
        <p>It also changes what "central" is worth. Because everything is walked, an apartment in the middle of the village, like <a href="{apartment}">this one</a>, is not a marginal convenience. It is the difference between a holiday with logistics and one without.</p>
      </div>
      {{fig|village||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="skiing" aria-labelledby="skiing-h">
  <div class="wrap">
    <p class="eyebrow">Winter</p>
    <h2 id="skiing-h">A glacier above the village, and a railway inside the mountain</h2>
    <div class="split">
      {{fig|piste-dawn||(min-width: 900px) 44vw, 92vw}}
      <div class="measure">
        <p>The ski area rises from the village onto the Allalin glacier. The Metro Alpin, an underground funicular that runs up inside the mountain, carries skiers to Mittelallalin at around 3,500 metres, where the snow holds through the year.</p>
        <p>That altitude is the reason Saas-Fee is a reliable early- and late-season resort while lower ones are watching the forecast. The terrain is broad and open at the top and narrows into the trees on the way home.</p>
        <p>The slopes are four minutes' walk from the apartment door, through the village.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="summer" aria-labelledby="summer-h">
  <div class="wrap">
    <p class="eyebrow">Summer</p>
    <h2 id="summer-h">Ski before lunch. Walk after it.</h2>
    <div class="split">
      <div class="measure">
        <p>Saas-Fee is one of a handful of places in the Alps where the glacier skis through the summer, which is why national teams camp here in July and August. The Metro Alpin keeps running, so you can be on snow before lunch without a single step of climbing.</p>
        <p>Below the ice it becomes walking country: high paths through larch and rock, meadows, and the whole horseshoe of peaks in view. Long days, cool nights, and the village at its most relaxed and, for what it's worth, its cheapest.</p>
      </div>
      {{fig|glacier-view||(min-width: 900px) 44vw, 92vw}}
    </div>
  </div>
</section>

<section class="section section-panel" id="eating" aria-labelledby="eating-h">
  <div class="wrap">
    <p class="eyebrow">Evenings</p>
    <h2 id="eating-h">Dinner, either way</h2>
    <div class="measure">
      <p>The restaurants sit on and around the main street, all within a walk of the apartment. Because nothing is more than a few minutes away, dinner out never needs a plan. You walk down, you eat, you walk back, and nobody has to stay sober to drive.</p>
      <p>Eating in is the other half of the argument for an apartment. A group of eight in a hotel eats eight covers at hotel prices every night. Here, the <a href="{apartment}#kitchen">kitchen and the table</a> take the whole party, the supermarket is twenty metres away, and you cook when you feel like it.</p>
    </div>
  </div>
</section>

<section class="section" id="getting-here" aria-labelledby="getting-h">
  <div class="wrap">
    <p class="eyebrow">Getting here</p>
    <h2 id="getting-h">Arriving</h2>
    <div class="cols cols-3">
      <div class="col">
        <h3>By train</h3>
        <p>To Visp, which is on the main line through the Rhône valley, and then the postbus up the Saas valley, around an hour. The bus stops at the village entrance, a short walk from the apartment.</p>
      </div>
      <div class="col">
        <h3>By car</h3>
        <p>Up the valley from Visp, then into the car parks at the village entrance. You do not drive into Saas-Fee; nobody does. Winter tyres are the sensible minimum from November.</p>
      </div>
      <div class="col">
        <h3>By air</h3>
        <p>Geneva and Zurich are both realistic, at roughly three to three and a half hours by train and bus. Milan Malpensa is an option in summer over the Simplon.</p>
      </div>
    </div>
    <p class="fineprint">Exact arrival instructions and key collection come from the local manager once your dates are confirmed. <a href="{book}">Booking details</a>.</p>
  </div>
</section>
""",
        },

        # ==================================================================
        "book": {
            "title": "Book Direct, No Platform Fee | Bijou du Glacier, Saas-Fee",
            "desc": "Book Bijou du Glacier direct: the same nightly rate as the platforms, without their service fee on top. Four bedrooms, sleeps eight, in car-free Saas-Fee.",
            "h1": "Reserve your stay",
            "lede": "The apartment is available through several channels. We point you to the direct one first, and the reason is arithmetic rather than sentiment.",
            "jump": [
                ("direct", "Book direct"),
                ("platforms", "Platforms"),
                ("before-you-book", "Before you book"),
            ],
            "body": """
<section class="section" id="direct" aria-labelledby="direct-h">
  <div class="wrap">
    <p class="eyebrow">Direct</p>
    <h2 id="direct-h">Book directly with the apartment</h2>
    <div class="measure">
      <p>The nightly rate is the same wherever you book. We do not undercut the platforms, and we are not allowed to. What differs is what gets added on top: the platforms charge the guest a service fee, and booking direct does not.</p>
      <p>Booking direct also puts you in touch with SaasFeeHolidays.com, in the village, from the first message rather than through a platform inbox. That matters more than it sounds when you want a flexible check-out or an early key.</p>
    </div>
    {{bookblock}}
  </div>
</section>

<section class="section section-panel" id="platforms" aria-labelledby="platforms-h">
  <div class="wrap">
    <p class="eyebrow">The alternatives</p>
    <h2 id="platforms-h">Or find us on the platforms</h2>
    <div class="measure">
      <p>If you would rather book somewhere you already have an account, a payment method and a cancellation history, that is a completely reasonable thing to want. The listings below are the same apartment.</p>
    </div>
    {{platforms}}
  </div>
</section>

<section class="section" id="before-you-book" aria-labelledby="before-h">
  <div class="wrap">
    <p class="eyebrow">Worth knowing</p>
    <h2 id="before-h">Before you book</h2>
    <div class="cols">
      <div class="col">
        <h3>Who you are booking with</h3>
        <p>A privately owned apartment, looked after by Adam and the team at SaasFeeHolidays.com, based in the village on Untere Dorfstrasse. Not a chain, not a portfolio. One apartment, in one building, with one set of keys.</p>
        <p>They are not new at this. Nine years hosting in Saas-Fee, Superhost status on Airbnb, and <strong>308 guest reviews averaging 4.76 out of 5</strong> across the apartments they look after in the village. They live here all year, they know which restaurant is worth the walk in February, and they are the people who will answer your messages and hand you the keys.</p>
      </div>
      <div class="col">
        <h3>Payment and cancellation</h3>
        <p>Payment schedule and cancellation terms are set out by SaasFeeHolidays.com when they confirm your dates, before anything is due.</p>
        </div>
      <div class="col">
        <h3>Tourist tax and registration</h3>
        <p>Swiss municipalities require guest registration and charge a small nightly tourist tax per person, collected locally. It is not included in the nightly rate and it is not a booking fee.</p>
      </div>
      <div class="col">
        </div>
      <div class="col">
        <h3>Still deciding?</h3>
        <p>The two things worth reading first are <a href="{apartment}">the room-by-room description</a> and <a href="{resort}">what Saas-Fee is actually like</a>, particularly if you have not stayed in a car-free village before.</p>
      </div>
    </div>
  </div>
</section>
""",
        },
    },

    # ---- image alt text and captions --------------------------------------
    "alt": {
        "patio-hero": "A woven lounge chair with a mauve cushion on the apartment's covered balcony in afternoon sun, above the larch woods of the Saas valley.",
        "patio-chair": "A round woven lounge chair with a deep mauve cushion and a low round side table on the balcony beside the glass doors, looking out over larch woods and a chalet roof across the valley.",
        "patio-seating": "The covered balcony running the length of the apartment beneath a dark timber soffit, with woven lounge chairs and mauve cushions along a wrought-iron balustrade, a pair of low round tables, and the roofs of Saas-Fee below.",
        "floorplan": "Architect's floor plan of apartment B4 on the second floor of Residence du Glacier, showing four bedrooms and three bathrooms arranged around a central entrance hall, an open-plan living room, dining area and kitchen along the front, and a covered balcony running the full width of the apartment.",
        "hero-video": "A walkthrough of the apartment: the piste and the Mischabel face above Saas-Fee, then the living room, the kitchen, all four bedrooms, the bathrooms and the balcony.",
        "piste-dawn": "A freshly groomed piste curving down a snowfield above Saas-Fee at first light, with the dark rock and ice of the Mischabel face rising behind it.",
        "dining-band": "The long live-edge walnut dining table laid for eight, seen the length of the open-plan room, with the kitchen at one end and a stone feature wall behind.",
        "massif": "The glaciated wall of the Mischabel massif above Saas-Fee, deep snowfields and blue-shadowed ridges filling the sky above the village rooftops.",
        "living-room": "The open-plan living room of the Saas-Fee apartment, with a deep olive sofa, round bronze coffee tables, a patterned rug on wide oak boards and windows on two sides.",
        "kitchen-shelves": "Open kitchen shelving with white crockery and glasses above a stone worktop, beside a brushed-brass tap, kettle and knife block.",
        "master-bedroom": "The master bedroom, with a king-size bed against a full-height pale oak panelled wall, an olive quilted throw, rust cushions and a framed alpine print.",
        "balcony-view": "The large covered balcony of the apartment, with wrought-iron railings, looking over the snow-covered roofs of Saas-Fee to the peaks beyond.",
        "living-wide": "The living room and dining area of the four-bedroom Saas-Fee apartment seen together, with tall windows looking out to the snowy village and mountains.",
        "coffee-table": "A pair of round two-tier bronze coffee tables on a soft cream rug in front of the olive sofa in the living room.",
        "living-corner": "A quiet corner of the living room with a pale sofa, a mustard cushion, an arc floor lamp and two organic-edged mirrors on the wall.",
        "dining-table": "The long live-edge walnut dining table with black cross-back chairs, set for eight in front of the open kitchen, with a stone feature wall behind.",
        "dining-walnut": "The walnut dining table seen from the kitchen end, with a single pale bowl at its centre and the living room windows beyond.",
        "kitchen": "The fully equipped kitchen of the Saas-Fee apartment in soft taupe with a stone splashback, built-in oven and induction hob, with the dining table in the foreground.",
        "kitchen-oven": "The kitchen run with a built-in oven and coffee machine under warm shelf lighting, opening straight onto the dining table.",
        "kitchen-tap": "Close view of the brushed-brass kitchen tap and stone splashback, with a copper kettle and utensils on the worktop.",
        "bedroom-2": "The second bedroom, with a king-size bed dressed in white linen, ochre and chocolate cushions, warm bedside lamps and a framed print above the headboard.",
        "bedroom-3": "The third bedroom, with a king-size bed, a fluted cream headboard, chocolate-brown cushions and lit lamps on both sides.",
        "bedroom-4": "The fourth bedroom, with a king-size bed, a tall fluted oak wardrobe, a floor lamp and a deep-set window looking onto the village.",
        "wardrobe": "An open fitted oak wardrobe with hanging rail and shelves, providing storage for a party of eight.",
        "blanket": "A folded Swiss wool blanket with a red cross stripe over the arm of a bouclé chair.",
        "bathroom": "One of the three bathrooms, finished in large pale stone tiles with a floating oak vanity, a stone basin, a brushed-brass tap and a backlit mirror.",
        "bathroom-shower": "The walk-in shower behind clear glass, tiled in dark slate against pale stone, beside the backlit mirror and oak vanity.",
        "bathroom-bath": "One of the two deep baths, set against a band of dark slate tiling, with a glazed door onto a snowy view.",
        "robe-door": "A white bathrobe hanging on a herringbone oak door inside the apartment.",
        "village": "The snow-covered rooftops of car-free Saas-Fee at dusk, with a piste running down into the village and the peaks behind.",
        "glacier-view": "The high glaciated peaks above Saas-Fee in summer light, seen from the apartment's windows above the village roofs.",
        "share": "The glaciated Mischabel wall above the village of Saas-Fee, Valais.",
    },

    "caption": {
        "patio-chair": "The corner by the doors, where the sun arrives first.",
        "patio-seating": "The whole length of it, under cover, with the village below.",
        "floorplan": "The architect's plan of apartment B4. The labels are the original German: Zimmer is a bedroom, Bad a bathroom, Dusche the shower room, Küche the kitchen, Wohnzimmer the living room, Balkon the balcony.",
        "living-wide": "Living room and kitchen, open to each other.",
        "coffee-table": "Bronze, oak and wool, the palette of the renovation.",
        "living-corner": "A corner to read in while the kitchen is busy.",
        "dining-table": "One table, eight places, and a fully equipped kitchen behind it: dishwasher, microwave, range and oven, coffee maker.",
        "dining-walnut": "A single live-edge walnut board.",
        "kitchen": "Fully equipped, and big enough for a group.",
        "kitchen-oven": "Oven, hob and coffee machine, under the shelf lighting.",
        "kitchen-tap": "Brushed brass against stone.",
        "bedroom-2": "Second bedroom.",
        "bedroom-3": "Third bedroom.",
        "bedroom-4": "Fourth bedroom.",
        "wardrobe": "Hanging space and shelves in every room.",
        "blanket": "Wool, where you'd want it.",
        "bathroom": "Stone, slate and oak.",
        "bathroom-shower": "The walk-in shower.",
        "bathroom-bath": "A deep bath, with a window onto the snow.",
        "robe-door": "Robes provided.",
        "village": "Saas-Fee at dusk, with the piste running in.",
        "glacier-view": "The glacier, from the windows.",
        "dining-band": "One table, eight places, one room.",
        "massif": "The Mischabel wall, straight ahead of the balcony.",
        "piste-dawn": "First light on the piste above the village.",
        "balcony-view": "The balcony, over the village roofs.",
    },

    "footer": {
        "explore": "Explore",
        "book": "Book",
        "contact": "The property",
        "address": "Residence du Glacier · Blomattenstrasse 2 · 3906 Saas-Fee · Valais · Switzerland",
        "fine": "A privately owned four-bedroom apartment in Saas-Fee, managed locally.",
    },

    "next": {
        "apartment": ("The apartment, room by room", "Four bedrooms, the kitchen, the bathrooms and the balcony, with the practical details in a table."),
        "resort": ("Saas-Fee", "A car-free village at 1,800 m, glacier skiing above it, and how to get here."),
        "book": ("Book direct", "The same nightly rate as the platforms, without their service fee on top."),
        "home": ("Overview", "The apartment, the village and the photographs, on one page."),
    },
}
