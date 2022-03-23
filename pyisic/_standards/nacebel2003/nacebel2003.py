"""`NACEBEL2003 Standard <https://economie.fgov.be/sites/default/files/Files/Entreprises/KBO/conversiontable-Nacebel-2003-2008.xls>`_.
"""
from ...types import Category, Classification, Standard, Standards

NACEBEL2003 = Standard(
    standard=Standards.NACEBEL2003,
    classes=[
        Classification("01110", "Culture de céréales et cultures industrielles", Category.CLASS),
        Classification(
            "0111001",
            "la culture de céréales : blé dur, blé tendre, seigle, orge, avoine, maïs, riz, etc.",
            Category.CLASS,
        ),
        Classification("0111002", "la culture de pommes de terre", Category.CLASS),
        Classification("0111003", "la culture de betteraves sucrières", Category.CLASS),
        Classification(
            "0111004", "la culture de tabac (y compris la récolte et le séchage des feuilles de tabac)", Category.CLASS
        ),
        Classification(
            "0111005",
            "la culture des graines et des fruits oléagineux : arachides, fèves de soja, fèves de colza, etc.",
            Category.CLASS,
        ),
        Classification(
            "0111006",
            "la culture de cônes de houblon et de racines et tubercules à forte teneur en amidon ou en inuline",
            Category.CLASS,
        ),
        Classification(
            "0111007",
            "la culture du coton ou d'autres plantes textiles ; le rouissage de plantes à fibres végétales",
            Category.CLASS,
        ),
        Classification(
            "0111008", "la culture de légumes à cosse secs tels que pois fourragers et haricots", Category.CLASS
        ),
        Classification(
            "0111009",
            "la culture de plantes à usage pharmaceutique ou insecticide, parasiticide ou similaire",
            Category.CLASS,
        ),
        Classification("0111010", "la production de semences céréalières", Category.CLASS),
        Classification("0111011", "les cultures n.d.a.", Category.CLASS),
        Classification("01121", "Culture de légumes", Category.CLASS),
        Classification(
            "0112101",
            "la culture de légumes : tomates, melons,oignons, choux, laitues, carottes, haricots, cresson, cressonnette, maïs sucré, courgettes, aubergines, poireaux, etc.",
            Category.CLASS,
        ),
        Classification(
            "0112102",
            "la culture de condiments : câpres, poivrons, fenouil, persil, cerfeuil, estragon, marjolaine, etc.",
            Category.CLASS,
        ),
        Classification(
            "0112103",
            "la culture des champignons et des truffes, la cueillette des champignons et des truffes dans les bois",
            Category.CLASS,
        ),
        Classification("0112104", "la production de semences de légumes.", Category.CLASS),
        Classification("01122", "Culture de fleurs", Category.CLASS),
        Classification(
            "0112201", "la culture de fleurs, de fleurs à couper et de plantes ornementales d'intérieur", Category.CLASS
        ),
        Classification("0112202", "la fabrication de fleurs séchées", Category.CLASS),
        Classification("0112203", "la production de semences de fleurs.", Category.CLASS),
        Classification("01123", "Pépinières", Category.CLASS),
        Classification(
            "0112301",
            "la culture de plantes destinées à la plantation : arbustes, plantes ornementales d'intérieur, arbres, etc.",
            Category.CLASS,
        ),
        Classification("0112302", "la culture de gazon en rouleaux.", Category.CLASS),
        Classification("01130", "Culture de fruits", Category.CLASS),
        Classification(
            "0113001",
            "la culture de fruits : pommes, poires, agrumes, abricots, fraises, baies, cerises, pêches, bananes, avocats, dattes, etc.",
            Category.CLASS,
        ),
        Classification(
            "0113002",
            "la culture de raisins de cuve et de raisins de table ; la production de vin en combinaison avec la culture de raisins",
            Category.CLASS,
        ),
        Classification("0113003", "la culture de noix comestibles, y compris les noix de coco", Category.CLASS),
        Classification(
            "0113004",
            "la culture de plantes destinées à la production de boissons, telles que le café, le cacao, le thé, le maté",
            Category.CLASS,
        ),
        Classification(
            "0113005",
            "la culture de plantes pour épices : laurier, basilic, anis, coriandre, cumin, cannelle, clous de girofle, noix muscade, gingembre, etc.",
            Category.CLASS,
        ),
        Classification(
            "0113006",
            "la culture d'olives ; la fabrication d'huile d'olives en combinaison avec la culture d'olives.",
            Category.CLASS,
        ),
        Classification("01210", "Élevage de bovins", Category.CLASS),
        Classification("0121001", "l'élevage de bovins", Category.CLASS),
        Classification("0121002", "la production de lait cru de vache.", Category.CLASS),
        Classification("01220", "Élevage d'ovins, caprins et équidés", Category.CLASS),
        Classification("0122001", "l'élevage d'ovins et de caprins", Category.CLASS),
        Classification("0122002", "l'élevage de chevaux, d'ânes, de mulets et de bardots", Category.CLASS),
        Classification("0122003", "la production de laine brute", Category.CLASS),
        Classification("0122004", "la production de lait cru de brebis et de chèvre.", Category.CLASS),
        Classification("01231", "Élevage de porcs reproducteurs", Category.CLASS),
        Classification(
            "0123101", "l'élevage de porcs reproducteurs, y compris l'élevage de sangliers.", Category.CLASS
        ),
        Classification("01232", "Élevage de porcs à l'engrais", Category.CLASS),
        Classification(
            "0123201",
            "l'élevage de porcs à l'angrais, y compris l'engraissement pour le compte de tiers",
            Category.CLASS,
        ),
        Classification("01241", "Élevage de poules", Category.CLASS),
        Classification("0124101", "Elevage de poules", Category.CLASS),
        Classification("01242", "Production d'oeufs", Category.CLASS),
        Classification("0124201", "production d'oeufs", Category.CLASS),
        Classification("01243", "Élevage d'autres volailles", Category.CLASS),
        Classification("0124301", "l'élevage de canards, d'oies, de dindes et de pintades.", Category.CLASS),
        Classification("01250", "Élevage d'autres animaux", Category.CLASS),
        Classification(
            "0125001", "l'élevage d'abeilles et la production de miel et de cire d'abeilles", Category.CLASS
        ),
        Classification("0125002", "l'élevage de lapins", Category.CLASS),
        Classification("0125003", "l'élevage d'animaux domestiques", Category.CLASS),
        Classification("0125004", "l'élevage d'animaux à fourrure", Category.CLASS),
        Classification("0125005", "l'élevage de gibier", Category.CLASS),
        Classification("0125006", "l'élevage de vers à soie, la production de cocons de vers à soie", Category.CLASS),
        Classification("0125007", "l'élevage de grenouilles et de reptiles aquatiques", Category.CLASS),
        Classification("0125008", "l'élevage d'escargots", Category.CLASS),
        Classification("0125009", "l'élevage d'animaux divers n.d.a.", Category.CLASS),
        Classification("01300", "Culture et élevage associés", Category.CLASS),
        Classification(
            "0130001",
            "la culture associée à l'élevage de bétail, pour autant que le chiffre d'affaires d'une de ces deux activités n'atteigne pas les 2/3 du chiffre d'affaires total.",
            Category.CLASS,
        ),
        Classification("01410", "Services annexes à la culture; aménagement des paysages", Category.CLASS),
        Classification("0141001", "la préparation des terres", Category.CLASS),
        Classification("0141002", "la création de cultures", Category.CLASS),
        Classification("0141003", "le traitement des récoltes", Category.CLASS),
        Classification("0141004", "la pulvérisation des récoltes, y compris par voie aérienne", Category.CLASS),
        Classification(
            "0141005",
            "la lutte contre les animaux nuisibles (y compris les lapins) en relation avec l'agriculture",
            Category.CLASS,
        ),
        Classification("0141006", "la taille des arbres fruitiers et des vignes", Category.CLASS),
        Classification("0141007", "la transplantation du riz, le démariage des betteraves", Category.CLASS),
        Classification(
            "0141008",
            "la récolte et la préparation des cultures en vue de leur commercialisation primaire : nettoyage, triage, désinfection, emballage (y compris les emballages favorisant une conservation de courte durée),",
            Category.CLASS,
        ),
        Classification("0141009", "l'élagage des arbres et des haies", Category.CLASS),
        Classification("0141010", "l'exploitation de systèmes d'irrigation", Category.CLASS),
        Classification(
            "0141011",
            "la création et l'entretien de jardins, de parcs et d'espaces verts pour installations sportives",
            Category.CLASS,
        ),
        Classification("0141012", "la location de machines et d'équipements agricoles avec opérateur.", Category.CLASS),
        Classification("01411", "Création, implantation et entretien de jardins et parcs", Category.CLASS),
        Classification("01412", "Services annexes à la culture, n.d.a.", Category.CLASS),
        Classification(
            "01420", "Services annexes à l'élevage, à l'exclusion des services vétérinaires", Category.CLASS
        ),
        Classification("0142001", "l'insémination artificielle", Category.CLASS),
        Classification("0142002", "la tonte d'ovins pour le compte de tiers", Category.CLASS),
        Classification(
            "0142003",
            "les services de conduite de troupeaux, services de paissance, services de nettoyage des poulaillers, etc.",
            Category.CLASS,
        ),
        Classification("0142004", "les fourrières, pensions et autres refuges pour animaux", Category.CLASS),
        Classification("0142005", "le toilettage d'animaux domestiques.", Category.CLASS),
        Classification(
            "01500", "Chasse; capture d'animaux, repeuplement en gibier et services annexes", Category.CLASS
        ),
        Classification(
            "0150001",
            "la chasse ou le piégeage d'animaux pour l'alimentation commerciale, leur fourrure, leur peau, ou destinés à des centres de recherche ou des parcs zoologiques, ou utilisés comme animaux de compagnie",
            Category.CLASS,
        ),
        Classification(
            "0150002",
            "la production de pelleteries, de peaux de reptiles ou d'oiseaux provenant d'activités de chasse ou de piégeage",
            Category.CLASS,
        ),
        Classification(
            "0150003",
            "les activités des services visant à promouvoir la chasse et le piégeage à des fins commerciales",
            Category.CLASS,
        ),
        Classification(
            "0150004", "la capture de mammifères marins tels que les morses et les phoques.", Category.CLASS
        ),
        Classification("02011", "Sylviculture", Category.CLASS),
        Classification(
            "0201101",
            "la sylviculture sur pied : boisement, reboisement, transplantation, coupe d'éclaircie et conservation des forêts et des coupes",
            Category.CLASS,
        ),
        Classification("0201102", "la culture de taillis et de bois de trituration", Category.CLASS),
        Classification("0201103", "l'exploitation de pépinières (y compris les arbres de Noël)", Category.CLASS),
        Classification("0201104", "culture de végétaux pour la sparterie", Category.CLASS),
        Classification("02012", "Exploitation forestière", Category.CLASS),
        Classification(
            "0201201",
            "l'exploitation forestière : abattage d'arbres et production de bois brut tels que les bois de mine, les échalas fendus, les piquets et les bois de chauffage",
            Category.CLASS,
        ),
        Classification(
            "0201202",
            "la récolte de produits forestiers poussant à l'état sauvage : liège, laque, résines, baumes, extraits végétaux (crin végétal), glands, marrons d'Inde, mousses, lichens, balata et autres gommes.",
            Category.CLASS,
        ),
        Classification("02020", "Services annexes à la sylviculture et à l'exploitation forestière", Category.CLASS),
        Classification(
            "0202001",
            "l'inventaire des forêts, l'évaluation du bois, la protection contre les incendies",
            Category.CLASS,
        ),
        Classification("0202002", "le transport de grumes dans les forêts.", Category.CLASS),
        Classification("05010", "Pêche", Category.CLASS),
        Classification("0501001", "la pêche en haute mer, la pêche côtière et en eaux intérieures", Category.CLASS),
        Classification("0501002", "le ramassage en mer ou en eau douce de crustacés et de mollusques", Category.CLASS),
        Classification(
            "0501003",
            "les activités de bateaux de pêche qui, en outre, procèdent à la transformation et la conservation de poissons",
            Category.CLASS,
        ),
        Classification(
            "0501004", "la capture d'animaux marins : tortues, holothuries, tuniciers, oursins, etc.", Category.CLASS
        ),
        Classification("0501005", "la récolte de perles naturelles, éponges, coraux, algues, etc.", Category.CLASS),
        Classification("0501006", "les activités des services annexes à la pêche.", Category.CLASS),
        Classification("05020", "Aquaculture", Category.CLASS),
        Classification(
            "0502001",
            "la production de naissains d'huîtres, de moules, de jeunes langoustes, de larves de crevettes, d'alevins et de saumoneaux",
            Category.CLASS,
        ),
        Classification("0502002", "la culture d'algues et autres plantes aquatiques comestibles", Category.CLASS),
        Classification("0502003", "la pisciculture en eau de mer et en eau douce", Category.CLASS),
        Classification("0502004", "l'ostréiculture.", Category.CLASS),
        Classification("10100", "Extraction et agglomération de la houille", Category.CLASS),
        Classification(
            "1010001", "l'extraction de la houille : extraction souterraine ou à ciel ouvert", Category.CLASS
        ),
        Classification(
            "1010002", "le lavage, le calibrage, le triage, la pulvérisation, etc., de la houille", Category.CLASS
        ),
        Classification("1010003", "l'agglomération de la houille", Category.CLASS),
        Classification("1010004", "la récupération de la houille provenant des terrils.", Category.CLASS),
        Classification("10200", "Extraction et agglomération du lignite", Category.CLASS),
        Classification("1020001", "l'extraction du lignite : extraction souterraine ou à ciel ouvert", Category.CLASS),
        Classification("1020002", "le lavage, la déshydratation, la pulvérisation du lignite", Category.CLASS),
        Classification("1020003", "l'agglomération du lignite.", Category.CLASS),
        Classification("10300", "Extraction et agglomération de la tourbe", Category.CLASS),
        Classification("1030001", "l'extraction de la tourbe", Category.CLASS),
        Classification("1030002", "la production de tourbe pour l'horticulture", Category.CLASS),
        Classification("1030003", "l'agglomération de la tourbe.", Category.CLASS),
        Classification("11100", "Extraction de pétrole brut et de gaz naturel", Category.CLASS),
        Classification("1110001", "l'extraction de pétrole brut", Category.CLASS),
        Classification("1110002", "l'extraction d'hydrocarbures gazeux (gaz naturel)", Category.CLASS),
        Classification("1110003", "l'extraction de condensats", Category.CLASS),
        Classification(
            "1110004", "la décantation et la séparation de fractions d'hydrocarbures liquides", Category.CLASS
        ),
        Classification("1110005", "la liquéfaction et la regazéification du gaz naturel", Category.CLASS),
        Classification("1110006", "la désulfuration du gaz", Category.CLASS),
        Classification("1110007", "l'extraction de sables et de schistes bitumineux", Category.CLASS),
        Classification(
            "1110008", "la production de pétrole brut à partir de sables et schistes bitumineux.", Category.CLASS
        ),
        Classification("11200", "Services annexes à l'extraction de pétrole et de gaz", Category.CLASS),
        Classification("1120001", "forage et reforage dirigés", Category.CLASS),
        Classification("1120002", "montage in situ, réparation et démontage de tours de forage", Category.CLASS),
        Classification("1120003", "cimentation de puits de pétrole ou de gaz", Category.CLASS),
        Classification("1120004", "pompage de puits", Category.CLASS),
        Classification("1120005", "bouchage de puits", Category.CLASS),
        Classification("1120006", "extinction d'incendies de puits de pétrole.", Category.CLASS),
        Classification("12000", "Extraction de minerais d'uranium et de thorium", Category.CLASS),
        Classification("1200001", "l'extraction des minerais d'uranium et de thorium", Category.CLASS),
        Classification("1200002", "la concentration de ces minerais", Category.CLASS),
        Classification("1200003", 'la fabrication de concentré d\'uranium ("yellow cake").', Category.CLASS),
        Classification("13000", "Extraction de minerais métalliques", Category.CLASS),
        Classification("1300001", "EXTRACT. MINERAIS MÉTALL. & MéTAUX NATIFS", Category.CLASS),
        Classification("1300002", "PRéPARAT. MINERAIS : CONCASS.,BROYAGE", Category.CLASS),
        Classification("13100", "Extraction de minerais de fer", Category.CLASS),
        Classification(
            "1310001", "l'extraction de minerais dont la valeur tient surtout à leur teneur en fer", Category.CLASS
        ),
        Classification("1310002", "l'enrichissement et l'agglomération des minerais de fer.", Category.CLASS),
        Classification(
            "13200",
            "Extraction de minerais de métaux non ferreux, à l'exclusion des minerais d'uranium et de thorium",
            Category.CLASS,
        ),
        Classification(
            "1320001",
            "l'extraction et la préparation de minerais dont la valeur tient surtout à leur teneur en métaux non ferreux: aluminium (bauxite),cuivre,plomb,zinc,étain,manganèse,chrome,nickel, cobalt,molybdène,tanal",
            Category.CLASS,
        ),
        Classification("14110", "Extraction de pierres ornementales et de construction", Category.CLASS),
        Classification(
            "1411001",
            "l'extraction, la taille grossière et le sciage de pierres de taille pour les entreprises de travail de la pierre ou pour la construction, telles que le marbre, le granit, le grès, etc.",
            Category.CLASS,
        ),
        Classification("14121", "Extraction de pierres à ciment", Category.CLASS),
        Classification("1412101", "l'extraction, le broyage et le concassage des pierres à ciment.", Category.CLASS),
        Classification("14122", "Extraction de pierres calcaires, de gypse et de craie", Category.CLASS),
        Classification(
            "1412201",
            "l'extraction, le broyage et le concassage des pierres calcaires, y compris celles destinées à l'agriculture",
            Category.CLASS,
        ),
        Classification("1412202", "l'extraction du gypse et de l'anhydrite", Category.CLASS),
        Classification("1412203", "l'extraction du plâtre", Category.CLASS),
        Classification("1412204", "l'extraction de la craie", Category.CLASS),
        Classification("1412205", "l'extraction de dolomie.", Category.CLASS),
        Classification("14130", "Extraction d'ardoise", Category.CLASS),
        Classification("1413001", "extraction d'ardoise", Category.CLASS),
        Classification("14211", "Extraction de sable", Category.CLASS),
        Classification(
            "1421101",
            "l'extraction de sables industriels et de sables pour la construction, dans des carrières ou par dragage.",
            Category.CLASS,
        ),
        Classification("14212", "Extraction de gravier", Category.CLASS),
        Classification("1421201", "l'extraction de graviers dans des carrières ou par dragage", Category.CLASS),
        Classification("1421202", "le concassage et le broyage de pierres et de graviers.", Category.CLASS),
        Classification("14220", "Extraction d'argiles et de kaolin", Category.CLASS),
        Classification("1422001", "l'extraction d'argiles, d'argiles réfractaires et de kaolin.", Category.CLASS),
        Classification(
            "14300", "Extraction de minéraux pour l'industrie chimique et d'engrais naturels", Category.CLASS
        ),
        Classification(
            "1430001", "l'extraction de phosphates naturels et de sels potassiques naturels", Category.CLASS
        ),
        Classification("1430002", "l'extraction de soufre natif et de minerais de soufre", Category.CLASS),
        Classification("1430003", "l'extraction et la préparation des pyrites et des pyrrhotites", Category.CLASS),
        Classification(
            "1430004",
            "l'extraction de sulfates et de carbonates naturels de baryum (barytine et withérite), de borates naturels,de sulfates naturels de magnésium (kiesérite)",
            Category.CLASS,
        ),
        Classification("1430005", "l'extraction de terres colorantes et de spath fluor", Category.CLASS),
        Classification("1430006", "le ramassage de guano.", Category.CLASS),
        Classification("14400", "Production de sel", Category.CLASS),
        Classification("1440001", "l'extraction minière de sel, y compris par dissolution et pompage", Category.CLASS),
        Classification(
            "1440002", "la production de sel par évaporation de l'eau de mer ou d'autres eaux salées", Category.CLASS
        ),
        Classification("1440003", "la production de saumures et autres solutions salines", Category.CLASS),
        Classification("1440004", "le broyage, la purification et le raffinage du sel.", Category.CLASS),
        Classification("14500", "Autres activités extractives n.d.a.", Category.CLASS),
        Classification(
            "1450001",
            "l'extraction de minéraux et de matériaux divers : terraux et humus, matières abrasives, amiante, farines siliceuses fossiles, graphite naturel, stéatite (talc), feldspath, pierres gemmes, quartz, mica",
            Category.CLASS,
        ),
        Classification("15111", "Production de viande fraîche", Category.CLASS),
        Classification("1511101", "l'abattage des animaux", Category.CLASS),
        Classification("1511102", "la production de viande fraîche, en carcasses ou en morcceaux.", Category.CLASS),
        Classification("1511103", "la production de cuirs et de peaux bruts provenant des abattoirs", Category.CLASS),
        Classification(
            "1511104", "la fonte et le raffinage du saindoux et d'autres graisses animales comestibles", Category.CLASS
        ),
        Classification(
            "1511105",
            "la transformation des abats et charognes ; la production de farine de viandes et de farine d'os",
            Category.CLASS,
        ),
        Classification("1511106", "la préparation de boyaux naturels", Category.CLASS),
        Classification("1511107", "la production de laine de délainage.", Category.CLASS),
        Classification("15112", "Production de viande surgelée", Category.CLASS),
        Classification(
            "1511201", "la production de viande surgelée ou congelée, en carcasse ou en morceaux.", Category.CLASS
        ),
        Classification("15121", "Production de viande fraîche de volailles", Category.CLASS),
        Classification("1512101", "l'abattage de volailles et de lapins", Category.CLASS),
        Classification("1512102", "la préparation de viande fraîche de volailles et de lapins", Category.CLASS),
        Classification(
            "1512103",
            "la production de viande fraîche de volailles et de lapins en portions individuelles",
            Category.CLASS,
        ),
        Classification("1512104", "la production de plumes et de duvets.", Category.CLASS),
        Classification("15122", "Production de viande surgelée de volailles", Category.CLASS),
        Classification(
            "1512201",
            "la production de viande surgelée de volailles et de lapins en portions individuelles.",
            Category.CLASS,
        ),
        Classification(
            "15131", "Préparation de produits frais à base de viande et de conserves de viande", Category.CLASS
        ),
        Classification("1513101", "la production de viande séchée, salée ou fumée", Category.CLASS),
        Classification(
            "1513102",
            "la production de produits à base de viande : saucisses fraîches, salami, boudins, andouillettes, cervelas, saucisses de Boulogne, pâtés, galantines, rillettes, jambons cuits, extraits et jus de viande",
            Category.CLASS,
        ),
        Classification("1513103", "la production de plats préparés à base de viande.", Category.CLASS),
        Classification("15132", "Préparation de produits surgelés à base de viande", Category.CLASS),
        Classification("1513201", "la production de produits surgelés à base de viande", Category.CLASS),
        Classification("1513202", "la production de plats surgelés préparés à base de viande.", Category.CLASS),
        Classification(
            "15201",
            "Transformation et conservation de poisson et fabrication de produits frais à base de poisson",
            Category.CLASS,
        ),
        Classification(
            "1520101",
            "la conservation, sauf par congélation ou surgélation, de poissons, de crustacés et mollusques : séchage, fumage, salage, saumurage, mise en conserve, etc.",
            Category.CLASS,
        ),
        Classification(
            "1520102",
            "la préparation de produits à base de poissons, de crustacés et de mollusques (à l'exclusion de produits surgelés) : poissons cuits, filets de poisson, laitances, caviar, succédanés du caviar, etc.",
            Category.CLASS,
        ),
        Classification("1520103", "la production de plats frais préparés à base de poisson", Category.CLASS),
        Classification(
            "1520104",
            "les activités des navires se livrant uniquement à la transformation et à la conservation du poisson",
            Category.CLASS,
        ),
        Classification("1520105", "la production de farine de poisson.", Category.CLASS),
        Classification("15202", "Production de poisson surgelé et de produits à base de poisson", Category.CLASS),
        Classification(
            "1520201", "la congélation et la surgélation de poissons, de crustacés et de mollusques", Category.CLASS
        ),
        Classification(
            "1520202",
            "la préparation de produits surgelés à base de poissons, de crustacés et de mollusques",
            Category.CLASS,
        ),
        Classification("1520203", "la production de plats surgelés préparés à base de poisson.", Category.CLASS),
        Classification("15311", "Transformation et conservation de pommes de terre", Category.CLASS),
        Classification(
            "1531101",
            "la production de conserves de pommes de terre, à l'exclusion des produits surgelés",
            Category.CLASS,
        ),
        Classification("1531102", "la production de purées de pommes de terre déshydratées", Category.CLASS),
        Classification("1531103", "la production de pommes chips et de produits similaires", Category.CLASS),
        Classification("1531104", "la fabrication de farines et de fécules de pommes de terre", Category.CLASS),
        Classification("1531105", "l'épluchage industriel des pommes de terre.", Category.CLASS),
        Classification("15312", "Production de préparations surgelées à base de pommes de terre", Category.CLASS),
        Classification("1531201", "la production de pommes de terre précuites surgelées", Category.CLASS),
        Classification("1531202", "la fabrication de produits surgelés à base de pommes de terre.", Category.CLASS),
        Classification("15320", "Préparation de jus de fruits et de légumes", Category.CLASS),
        Classification("1532001", "la fabrication de nectars et de concentrés", Category.CLASS),
        Classification("1532002", "la fabrication de sirops de fruits.", Category.CLASS),
        Classification("15331", "Transformation et conservation de légumes", Category.CLASS),
        Classification(
            "1533101",
            "la conservation des légumes : séchage, immersion dans l'huile ou le vinaigre, mise en conserve, etc.",
            Category.CLASS,
        ),
        Classification("1533102", "l'élaboration de produits alimentaires à base de légumes.", Category.CLASS),
        Classification("15332", "Production de légumes surgelés", Category.CLASS),
        Classification("1533201", "la production de légumes surgelés", Category.CLASS),
        Classification("1533202", "l'élaboration de produits alimentaires à base de légumes surgelés", Category.CLASS),
        Classification("15333", "Transformation et conservation de fruits", Category.CLASS),
        Classification(
            "1533301",
            "la conservation de fruits : congélation, séchage, immersion, mise en conserve, etc.",
            Category.CLASS,
        ),
        Classification("1533302", "l'élaboration de produits alimentaires à base de fruits", Category.CLASS),
        Classification("1533303", "la fabrication de pulpes de fruits", Category.CLASS),
        Classification("1533304", "la fabrication de confitures, marmelades et gelées.", Category.CLASS),
        Classification("15411", "Production d'huiles végétales brutes", Category.CLASS),
        Classification(
            "1541101",
            "la production d'huiles végétales brutes : huiles d'olive, de soja, de palme, de tournesol, de coton, de navette, de colza, de moutarde, de lin, etc.",
            Category.CLASS,
        ),
        Classification(
            "1541102",
            "la production de farine ou de semoule de graines, noix ou amandes oléagineuses, non déshuilées.",
            Category.CLASS,
        ),
        Classification("15412", "Production d'huiles et de graisses brutes d'origine animale", Category.CLASS),
        Classification("1541201", "la production d'huiles et de graisses animales non comestibles", Category.CLASS),
        Classification("1541202", "l'extraction d'huiles de poissons et de mammifères marins.", Category.CLASS),
        Classification("15420", "Fabrication d'huiles et de graisses raffinées", Category.CLASS),
        Classification("1542001", "le raffinage d'huiles végétales : huiles d'olive, de soja, etc.", Category.CLASS),
        Classification(
            "1542002",
            "le traitement des huiles végétales : soufflage, cuisson, oxydation, polymérisation, déshydratation, hydrogénation, etc.",
            Category.CLASS,
        ),
        Classification("15430", "Fabrication de margarine et de graisses comestibles similaires", Category.CLASS),
        Classification("1543001", "la fabrication de margarine", Category.CLASS),
        Classification("1543002", "la fabrication de mélanges et autres pâtes à tartiner similaires", Category.CLASS),
        Classification(
            "1543003", "la fabrication de graisses composées destinées à la cuisson des aliments.", Category.CLASS
        ),
        Classification("15510", "Fabrication de produits laitiers", Category.CLASS),
        Classification(
            "1551001",
            "la production de laits liquides frais, pasteurisés, stérilisés, homogénéisés et/ou ayant subi un chauffage ultracourt (U.H.T.)",
            Category.CLASS,
        ),
        Classification("1551002", "la production de crèmes de lait", Category.CLASS),
        Classification("1551003", "la production de laits concentrés, édulcorés ou non", Category.CLASS),
        Classification("1551004", "la production de laits en poudre", Category.CLASS),
        Classification("1551005", "la production de beurre", Category.CLASS),
        Classification("1551006", "la production de fromages et de caillebotte", Category.CLASS),
        Classification("1551007", "la production de lactosérum", Category.CLASS),
        Classification("1551008", "la production de caséine et de lactose", Category.CLASS),
        Classification("1551009", "la production de yoghourt", Category.CLASS),
        Classification("1551010", "la production de desserts lactés frais.", Category.CLASS),
        Classification("15520", "Fabrication de glaces de consommation", Category.CLASS),
        Classification(
            "1552001",
            "la production de crèmes glacées et d'autres glaces de consommation (ex. sorbet), y compris les crèmes glacées mises en vente par le producteur sur la voie publique.",
            Category.CLASS,
        ),
        Classification("15610", "Travail des grains", Category.CLASS),
        Classification(
            "1561001",
            "la mouture des grains, y compris leur préparation (séchage, triage, etc.) et la production de farines, de gruaux, de semoules ou d'agglomérés sous forme de pellets, de blé, de seigle, d'avoine, de maï",
            Category.CLASS,
        ),
        Classification("1561002", "la mouture du riz et la production de farine de riz", Category.CLASS),
        Classification("1561003", "la production de riz blanchi, poli, glacé, etuvé ou converti", Category.CLASS),
        Classification(
            "1561004",
            "la mouture des légumes et la production de farines et de semoules de légumes à cosse secs, de racines ou tubercules, ou de fruits à coque comestibles",
            Category.CLASS,
        ),
        Classification(
            "1561005", "la fabrication d'aliments pour le petit déjeuner à base de céréales", Category.CLASS
        ),
        Classification(
            "1561006",
            "la fabrication de farines mélangées préparées pour la fabrication de pains, de gâteaux, de biscuits, de crêpes, etc.",
            Category.CLASS,
        ),
        Classification("15620", "Fabrication de produits amylacés", Category.CLASS),
        Classification(
            "1562001",
            "la fabrication de produits amylacés à partir de riz, de pommes de terre, de maïs, etc.",
            Category.CLASS,
        ),
        Classification("1562002", "la fabrication d'inuline", Category.CLASS),
        Classification("1562003", "la mouture du maïs par voie humide", Category.CLASS),
        Classification("1562004", "la fabrication de glucose, de sirop de glucose, de maltose, etc.", Category.CLASS),
        Classification("1562005", "la fabrication de gluten", Category.CLASS),
        Classification("1562006", "la fabrication de tapioca", Category.CLASS),
        Classification("1562007", "la fabrication d'huile de maïs", Category.CLASS),
        Classification("1562008", "la fabrication de miel artificiel et de caramel.", Category.CLASS),
        Classification("15710", "Fabrication d'aliments pour animaux de ferme", Category.CLASS),
        Classification(
            "1571001",
            "la fabrication de produits composés pour l'alimentation des animaux de ferme, y compris les aliments de complément",
            Category.CLASS,
        ),
        Classification(
            "1571002",
            "la préparation de produits non mélangés pour l'alimentation des animaux de ferme",
            Category.CLASS,
        ),
        Classification("1571003", "la fabrication de fourrage déshydraté.", Category.CLASS),
        Classification("15720", "Fabrication d'aliments pour animaux de compagnie", Category.CLASS),
        Classification("1572001", "Fabrication d'aliments pour animaux de compagnie.", Category.CLASS),
        Classification("15811", "Boulangeries industrielles", Category.CLASS),
        Classification(
            "1581101",
            "la fabrication à l'échelle industrielle de pains, petits pains,gâteaux frais,tartes et autres prod. frais de pâtisserie (prod.surgelés inclus) principalement destinés à être livrés au commerce de déta",
            Category.CLASS,
        ),
        Classification("1581102", "la fabrication de pâtes destinées à la cuisson.", Category.CLASS),
        Classification("15812", "Boulangeries et/ou pâtisseries artisanales", Category.CLASS),
        Classification(
            "1581201",
            "la fabrication artisanale de pains, de petits pains, de gâteaux frais, de tartes et d'autres produits frais de pâtisserie.",
            Category.CLASS,
        ),
        Classification("15820", "Biscotterie et biscuiterie, patisserie de conservation", Category.CLASS),
        Classification("1582001", "la fabrication de biscottes, de biscuits, de pains d'épices, etc.", Category.CLASS),
        Classification(
            "1582002",
            "la fabrication de pâtisserie et de gâteaux de conservation (à l'exclusion des produits surgelés)",
            Category.CLASS,
        ),
        Classification("1582003", 'la fabrication de produits "apéritifs" sucrés ou salés.', Category.CLASS),
        Classification("15830", "Fabrication de sucre", Category.CLASS),
        Classification(
            "1583001",
            "la production de sucre et de sirop de sucre obtenus à partir de jus de canne, de betterave, d'érable, de palme, etc.",
            Category.CLASS,
        ),
        Classification("1583002", "la production de saccharose", Category.CLASS),
        Classification("1583003", "la production de sucre candi", Category.CLASS),
        Classification("1583004", "le raffinage du sucre", Category.CLASS),
        Classification("1583005", "la production de mélasse.", Category.CLASS),
        Classification("15840", "Chocolaterie, confiserie", Category.CLASS),
        Classification(
            "1584001",
            "la fabrication de cacao, de beurre de cacao, de graisse de cacao et d'huile de cacao",
            Category.CLASS,
        ),
        Classification("1584002", "la fabrication du chocolat et de confiseries au chocolat", Category.CLASS),
        Classification("1584003", "la fabrication de confiseries", Category.CLASS),
        Classification("1584004", "la fabrication de confiseries médicinales", Category.CLASS),
        Classification("1584005", "la fabrication de pâtes à mâcher", Category.CLASS),
        Classification("1584006", "la fabrication de fruits confits.", Category.CLASS),
        Classification("15850", "Fabrication de pâtes alimentaires", Category.CLASS),
        Classification(
            "1585001",
            "la fabrication de pâtes alimentaires farcies ou non, fraîches ou cuites telles les macaronis, les spaghettis, les nouilles, les lasagnes, etc.",
            Category.CLASS,
        ),
        Classification("1585002", "la fabrication de couscous.", Category.CLASS),
        Classification("15860", "Transformation du thé et du café", Category.CLASS),
        Classification(
            "1586001",
            "la torréfaction et la décaféination du café : fabrication de café moulu, fabrication de café soluble, fabrication d'extraits et de concentrés de café",
            Category.CLASS,
        ),
        Classification("1586002", "la fabrication de succédanés du café", Category.CLASS),
        Classification("1586003", "la fabrication de chicorée", Category.CLASS),
        Classification("1586004", "le mélange du thé et du maté", Category.CLASS),
        Classification("1586005", "le conditionnement du thé, y compris en sachets", Category.CLASS),
        Classification(
            "1586006", "la fabrication de tisanes de plantes (menthe, verveine, camomille, etc.)", Category.CLASS
        ),
        Classification("15870", "Fabrication de condiments, assaisonnements et sauces", Category.CLASS),
        Classification(
            "1587001",
            "la fabrication de condiments et d'épices (y compris la mouture, le mélange, etc.)",
            Category.CLASS,
        ),
        Classification("1587002", "la fabrication du vinaigre", Category.CLASS),
        Classification("1587003", "la fabrication de sauces", Category.CLASS),
        Classification("1587004", "la fabrication de mayonnaise, ketchup, moutarde préparée, etc.", Category.CLASS),
        Classification("15880", "Fabrication de préparations homogénéisées et d'aliments diététiques", Category.CLASS),
        Classification(
            "1588001",
            "la fabrication de denrées alimentaires destinées à une alimentation particulière : préparations pour nourrissons, laits de suite et autres aliments du deuxième âge, aliments pour bébés, aliments à val",
            Category.CLASS,
        ),
        Classification(
            "1588002", "la préparation de laits de suite et autres aliments du deuxième âge", Category.CLASS
        ),
        Classification("1588003", "préparation d'aliments pour bébés", Category.CLASS),
        Classification(
            "1588004",
            "préparation d'aliments à valeur énergétique faible ou réduite destinés à un contrôle du poids",
            Category.CLASS,
        ),
        Classification(
            "1588005", "préparation d'aliments diététiques destinés à des fins médicales spéciales", Category.CLASS
        ),
        Classification(
            "1588006",
            "préparation d'aliments pauvres en sodium, y compris les sels diététiques hyposodiques ou asodiques",
            Category.CLASS,
        ),
        Classification("1588007", "préparation d'aliments sans gluten", Category.CLASS),
        Classification(
            "1588008",
            "préparation d'aliments adaptés à une dépense musculaire intense, surtout pour les sportifs",
            Category.CLASS,
        ),
        Classification(
            "1588009",
            "préparation d'aliments destinés aux personnes affectées d'un métabolisme glucidique perturbé (diabétiques).",
            Category.CLASS,
        ),
        Classification("15890", "Industries alimentaires n.d.a.", Category.CLASS),
        Classification("1589001", "la fabrication de soupes, de potages ou de bouillons, etc.", Category.CLASS),
        Classification("1589002", "la fabrication de succédanés de viande à base de plantes (quorn)", Category.CLASS),
        Classification("1589003", "la fabrication de levures, d'oeufs en poudre ou reconstitués, etc.", Category.CLASS),
        Classification("1589004", "la fabrication de poudre de levure et de poudre de pudding", Category.CLASS),
        Classification("1589005", "la fabrication de desserts lactés de conservation", Category.CLASS),
        Classification("1589006", "la fabrication de petits déjeuners en poudre ou granulés", Category.CLASS),
        Classification("1589007", "la fabrication de pâtes à tartiner contenant du cacao.", Category.CLASS),
        Classification("15910", "Production de boissons alcooliques distillées", Category.CLASS),
        Classification(
            "1591001",
            "la fabrication de boissons alcooliques distillées telles que le whisky, le cognac, le gin, etc.",
            Category.CLASS,
        ),
        Classification("1591002", "la fabrication de liqueurs et d'apéritifs à base d'alcool.", Category.CLASS),
        Classification("15920", "Production d'alcool éthylique de fermentation", Category.CLASS),
        Classification("1592001", "la production d'alcool éthylique de fermentation", Category.CLASS),
        Classification("1592002", "la production d'alcools neutres.", Category.CLASS),
        Classification("15930", "Production de vin", Category.CLASS),
        Classification(
            "1593001",
            "la production de vins à partir de raisins frais tels que les vins de table, les vins de pays, les vins de qualité, les vins mousseux, le champagne, etc.",
            Category.CLASS,
        ),
        Classification("1593002", "la production de vins à partir de moût de raisin concentré.", Category.CLASS),
        Classification("15940", "Fabrication de cidre et d'autres vins de fruits", Category.CLASS),
        Classification("1594001", "la fabrication de cidre, de poiré et d'autres vins de fruits", Category.CLASS),
        Classification("1594002", "la fabrication d'hydromel et de saké.", Category.CLASS),
        Classification("15950", "Production d'autres boissons fermentées", Category.CLASS),
        Classification("1595001", "la fabrication de vins aromatisés (vermouths)", Category.CLASS),
        Classification("1595002", "la fabrication d'autres boissons fermentées non distillées.", Category.CLASS),
        Classification("15960", "Production de la bière", Category.CLASS),
        Classification("1596001", "la production de bières.", Category.CLASS),
        Classification("15970", "Production de malt", Category.CLASS),
        Classification("1597001", "Malterie", Category.CLASS),
        Classification("15980", "Industrie des eaux minérales et des boissons rafraîchissantes", Category.CLASS),
        Classification(
            "1598001",
            "la mise en bouteilles des eaux, y compris la production d'eaux minérales naturelles",
            Category.CLASS,
        ),
        Classification(
            "1598002",
            "la production de boissons rafraîchissantes sans alcool : boissons édulcorées ou aromatisées : limonade, orangeade, cola, etc. ; boissons à base d'extraits naturels, tonics, etc. ; boissons à base de f",
            Category.CLASS,
        ),
        Classification("1598003", "la production de thé glacé", Category.CLASS),
        Classification("1598004", "la production de boissons rafraîchissantes en poudre", Category.CLASS),
        Classification("1598005", "la production de boissons à base de lait et de cacao", Category.CLASS),
        Classification("1598006", "la production de bières sans alcool", Category.CLASS),
        Classification("1598007", "la production de vins sans alcool", Category.CLASS),
        Classification("1598008", "la production d'apéritifs sans alcool.", Category.CLASS),
        Classification("16000", "Industrie du tabac", Category.CLASS),
        Classification(
            "1600001",
            "la fabrication de produits à base de tabac tels que les cigarettes, les cigares, le tabac à cigarettes, à pipe, à mâcher ou à priser",
            Category.CLASS,
        ),
        Classification("1600002", 'la fabrication de tabacs "homogénéisés" ou "reconstitués".', Category.CLASS),
        Classification("17110", "Préparation et filature de fibres de type cotonnier", Category.CLASS),
        Classification(
            "1711001", "la préparation, le cardage et le peignage de fibres de type cotonnier", Category.CLASS
        ),
        Classification(
            "1711002",
            "la filature de fils de type cotonnier en fibres de coton, en fibres artificielles ou en fibres synthétiques, pour le tissage, la bonneterie, etc.",
            Category.CLASS,
        ),
        Classification("17120", "Préparation et filature de fibres de type lainier - cycle cardé", Category.CLASS),
        Classification(
            "1712001",
            "la préparation de fibres de type lainier - cycle cardé : dégraissage et carbonisage de la laine, cardage",
            Category.CLASS,
        ),
        Classification(
            "1712002",
            "la filature de fils de type cardé en fibres de laine, en fibres artificielles ou en fibres synthétiques, pour le tissage, la bonneterie, etc.",
            Category.CLASS,
        ),
        Classification("17130", "Préparation et filature de fibres de type lainier - cycle peigné", Category.CLASS),
        Classification("1713001", "le peignage de fibres de type lainier - cycle peigné", Category.CLASS),
        Classification(
            "1713002",
            "la filature de fils de type peigné en fibres de laine, en fibres artificielles ou en fibres synthétiques, pour le tissage, la bonneterie, etc.",
            Category.CLASS,
        ),
        Classification("1713003", "la préparation et la filature de fibres de type semipeigné.", Category.CLASS),
        Classification("17140", "Préparation et filature de fibres de type linier", Category.CLASS),
        Classification("1714001", "le teillage du lin", Category.CLASS),
        Classification(
            "1714002",
            "la filature de fils de type linier en fibres de lin, en fibres artificielles ou en fibres synthétiques, pour le tissage, la bonneterie, etc.",
            Category.CLASS,
        ),
        Classification(
            "17150", "Moulinage et texturation de la soie et des textiles synthétiques ou artificiels", Category.CLASS
        ),
        Classification("1715001", "le tirage, le lavage et le moulinage de la soie", Category.CLASS),
        Classification("1715002", "le cardage et le peignage des déchets de soie", Category.CLASS),
        Classification(
            "1715003",
            "la filature de fils de type soie en fibres de soie,en fibres artificielles ou en fibres synthétiques, pour le tissage, la bonneterie, etc.",
            Category.CLASS,
        ),
        Classification(
            "1715004",
            "la texturation, le retordage, le moulinage, le câblage et le foulardage de fils de filaments artificiels ou synthétiques.",
            Category.CLASS,
        ),
        Classification("17160", "Fabrication de fils à coudre", Category.CLASS),
        Classification(
            "1716001",
            "la fabrication de fils à coudre à partir de toute matière textile, y compris les mélanges",
            Category.CLASS,
        ),
        Classification("1716002", "la fabrication de fils à broder.", Category.CLASS),
        Classification("17170", "Préparation et filature d'autres fibres", Category.CLASS),
        Classification(
            "1717001",
            "la préparation et la filature d'autres fibres textiles telles que les fibres de jute ou les fibres libériennes",
            Category.CLASS,
        ),
        Classification("1717002", "la fabrication de fils de papier.", Category.CLASS),
        Classification("17210", "Tissage de type cotonnier", Category.CLASS),
        Classification(
            "1721001",
            "la fabrication de tissus de type cotonnier en fils de coton ou en fibres synthétiques ou artificielles",
            Category.CLASS,
        ),
        Classification(
            "1721002",
            "la fabrication de velours, de tissus de chenile, de tissus bouclés (tissus-éponges), de tissus à points de gaze (y compris les tissus pour pansements), etc.",
            Category.CLASS,
        ),
        Classification("17220", "Tissage de type lainier - cycle cardé", Category.CLASS),
        Classification(
            "1722001",
            "la fabrication de tissus de type lainier, cycle cardé, en laine filée ou en fibres synthétiques ou artificielles.",
            Category.CLASS,
        ),
        Classification("17230", "Tissage de type lainier - cycle peigné", Category.CLASS),
        Classification(
            "1723001",
            "la fabrication de tissus de type lainier, cycle peigné, en laine filée ou en fibres synthétiques ou artificielles.",
            Category.CLASS,
        ),
        Classification("17240", "Tissage de type soie", Category.CLASS),
        Classification(
            "1724001",
            "la fabrication de tissus de type soie, en fils de soie ou en fibres synthétiques ou artificielles.",
            Category.CLASS,
        ),
        Classification("17250", "Tissage d'autres textiles", Category.CLASS),
        Classification(
            "1725001",
            "la fabrication d'autres tissus de lin, de ramie, de chanvre, de jute, de fibres libériennes et de fibres spéciales",
            Category.CLASS,
        ),
        Classification("1725002", "la fabrication de tissus en polypropène", Category.CLASS),
        Classification("1725003", "la fabrication de tissus en fibres de verre.", Category.CLASS),
        Classification("17300", "Ennoblissement textile", Category.CLASS),
        Classification(
            "1730001",
            "le blanchiment, la teinture, l'apprêt et l'impression (y compris la thermo-impression) de fibres, de fils, de tissus, d'étoffes de bonneterie et d'articles confectionnés (y compris les vêtements), fab",
            Category.CLASS,
        ),
        Classification(
            "1730002",
            "le séchage, le vaporisage, le décatissage, le stoppage, le sanforisage, le mercerisage, etc. de textiles fabriqués par des tiers.",
            Category.CLASS,
        ),
        Classification(
            "17401", "Confection de linge de lit et de table, d'articles textiles à usage domestique", Category.CLASS
        ),
        Classification(
            "1740101", "la fabrication de linge de table, de lit, de toilette ou de cuisine", Category.CLASS
        ),
        Classification(
            "1740102",
            "la fabrication d'édredons, couvertures, couvre-lits, coussins, poufs, oreillers, sacs de couchage, etc.",
            Category.CLASS,
        ),
        Classification("1740103", "la préparation des plumes et duvets", Category.CLASS),
        Classification(
            "1740104", "la fabrication de la partie textile des couvertures chauffantes électriques", Category.CLASS
        ),
        Classification(
            "1740105", "la fabrication de chiffons à épousseter, lavettes et articles similaires.", Category.CLASS
        ),
        Classification("17402", "Confection d'autres articles en textile", Category.CLASS),
        Classification(
            "1740201",
            "la fabrication d'articles confectionnés pour l'ammeublement : rideaux, tours de lit, stores, housses pour meubles, etc.",
            Category.CLASS,
        ),
        Classification(
            "1740202",
            "la fabrication de bâches,tentes,voiles pour bateaux de plaisance,parasols,auvents,housses amovibles pour véhicules et machines,etc., y compris les articles similaires en matières textiles imprégnées,e",
            Category.CLASS,
        ),
        Classification("1740203", "la fabrication de drapeaux, de banderoles, de bannières, etc.", Category.CLASS),
        Classification("1740204", "la fabrication de gilets de sauvetage, de parachutes, etc.", Category.CLASS),
        Classification("1740205", "la fabrication de sacs d'emballage en textile.", Category.CLASS),
        Classification("17510", "Fabrication de tapis et moquettes", Category.CLASS),
        Classification(
            "1751001",
            "la fabrication de revêtements de sols en matières textiles, y compris les feutres aiguilletés : tapis, carpettes, paillassons et carreaux.",
            Category.CLASS,
        ),
        Classification("17520", "Ficellerie, corderie, fabrication de filets", Category.CLASS),
        Classification(
            "1752001",
            "la fabrication de ficelles, de cordes et de cordages en fibres textiles, lames ou formes similaires, même imprégnés, enduits, recouverts ou gainés de caoutchouc ou de matière plastique",
            Category.CLASS,
        ),
        Classification(
            "1752002",
            "la fabrication de filets à mailles nouées, obtenus à partir de ficelles, cordes ou cordages",
            Category.CLASS,
        ),
        Classification(
            "1752003",
            "la fabrication d'articles de corderie et de filets : filets de pêche (y compris la réparation), défenses de bateau, coussins de déchargement, élingues de chargement, cordes ou cordages munis d'anneaux",
            Category.CLASS,
        ),
        Classification("17530", "Fabrication de non-tissés", Category.CLASS),
        Classification(
            "1753001",
            "la fabrication d'étoffes non-tissées et d'articles en étoffe non-tissée, à l'exclusion d'articles d'habillement.",
            Category.CLASS,
        ),
        Classification("17540", "Autres industries textiles n.d.a.", Category.CLASS),
        Classification(
            "1754001", "la fabrication d'articles de rubanerie, y compris les rubans sans trame", Category.CLASS
        ),
        Classification("1754002", "la fabrication de feutres (y compris les feutres aiguilletés)", Category.CLASS),
        Classification("1754003", "la fabrication d'étiquettes, d'écussons, etc.", Category.CLASS),
        Classification(
            "1754004", "la fabrication d'articles ornementaux : tresses, glands, floches, pompons, etc.", Category.CLASS
        ),
        Classification(
            "1754005",
            "la fabrication de tulles, tulles-bobinots et autres tissus à mailles nouées, de dentelles en pièces, en bandes ou en motifs, et de broderies",
            Category.CLASS,
        ),
        Classification(
            "1754006",
            "la fabrication de tissus imprégnés, enduits ou recouverts de matière plastique ou stratifiés avec de la matière plastique",
            Category.CLASS,
        ),
        Classification(
            "1754007",
            "la fabrication d'ouates en matière textile et d'articles d'ouaterie : serviettes et tampons hygiéniques",
            Category.CLASS,
        ),
        Classification(
            "1754008",
            "la fabrication de fils métalliques et de fils métallisés, même guipés, de fils et de cordes de caoutchouc recouverts de textiles, de fils textiles ou de lames recouverts, imprégnés,enduits ou gainés d",
            Category.CLASS,
        ),
        Classification("1754009", "la fabrication de tissu élastique", Category.CLASS),
        Classification(
            "1754010",
            "la fabrication de tissus divers: nappes pour pneumatiques (tyre cord fabric)faites de fils synthétiques ou artificiels à haute ténacité, toiles à calquer et pour le dessin, toiles préparées pour la pe",
            Category.CLASS,
        ),
        Classification(
            "1754011",
            "la fabrication d'articles divers en matières textiles, mèches, manchons à incandescence et étoffes tubulaires servant à leur fabrication,tuyaux pour pompes,courroies transporteuses ou de transmission,",
            Category.CLASS,
        ),
        Classification(
            "1754012", "la fabrication d'articles de passementerie, les travaux de plissage, etc.", Category.CLASS
        ),
        Classification("1754013", "la fabrication de matériel de rembourrage.", Category.CLASS),
        Classification("17600", "Fabrication d'étoffes à mailles", Category.CLASS),
        Classification(
            "1760001",
            "la fabrication d'étoffes à mailles : velours, peluches et étoffes bouclées ; tissus de types utilisés pour filets, rideaux et vitrages, tricotés sur métier Rachel ou sur des métiers similaires ; autre",
            Category.CLASS,
        ),
        Classification("17710", "Fabrication d'articles chaussants à mailles", Category.CLASS),
        Classification(
            "1771001",
            "la fabrication d'articles chaussants : chaussettes, bas, collants et articles similaires.",
            Category.CLASS,
        ),
        Classification("17720", "Fabrication de pull-overs et articles similaires à mailles", Category.CLASS),
        Classification(
            "1772001",
            "la fabrication de pull-overs, de cardigans, de chandails, de gilets et d'articles similaires à mailles.",
            Category.CLASS,
        ),
        Classification("18100", "Fabrication de vêtements en cuir", Category.CLASS),
        Classification("1810001", "la fabrication de vêtements en cuir ou en simili cuir.", Category.CLASS),
        Classification("18210", "Fabrication de vêtements de travail", Category.CLASS),
        Classification("1821001", "la fabrication de vêtements de travail", Category.CLASS),
        Classification(
            "1821002",
            "la fabrication de vêtements de sécurité contre le feu, le rayonnement, la contamination, etc.",
            Category.CLASS,
        ),
        Classification("18221", "Confection de vêtements de dessus pour hommes, femmes et enfants", Category.CLASS),
        Classification(
            "1822101",
            "la fabrication de vêtements de dessus pour hommes, femmes et enfants à partir de matériel produit ou non par le fabricant tels les tissus,étoffes à mailles,non-tissés etc.: mantaux, costumes, complêts",
            Category.CLASS,
        ),
        Classification("18222", "Confection sur mesure", Category.CLASS),
        Classification("1822201", "confection sur mesure.", Category.CLASS),
        Classification("18230", "Fabrication de vêtements de dessous", Category.CLASS),
        Classification(
            "1823001",
            "la fabrication de vêtements de dessous pour hommes,femmes et enfants à partir de matériel produit ou non par le fabricant tels les tissus,étoffes à mailles,dentelles etc: chemises,tshirts,blouses,slip",
            Category.CLASS,
        ),
        Classification("18241", "Fabrication de vêtements pour bébés", Category.CLASS),
        Classification("1824101", "fabrication de vêtements pour bébés.", Category.CLASS),
        Classification("18242", "Fabrication de vêtements de sport", Category.CLASS),
        Classification(
            "1824201",
            "la fabrication de survêtements de sport, de combinaisons et ensembles de ski, de maillots de bain et d'autres vêtements de sport.",
            Category.CLASS,
        ),
        Classification("18243", "Fabrication de chapeaux et de bonnets", Category.CLASS),
        Classification(
            "1824301", "la fabrication de chapeaux et de bonnets, y compris les coiffures en bonneterie", Category.CLASS
        ),
        Classification("1824302", "la fabrication de chapeaux en fourrure.", Category.CLASS),
        Classification("18244", "Fabrication d'autres vêtements et accessoires n.d.a.", Category.CLASS),
        Classification(
            "1824401",
            "la fabrication d'autres accessoires du vêtement : gants (y compris les gants en cuir), ceintures, châles, cravates, filets à cheveux, etc.",
            Category.CLASS,
        ),
        Classification(
            "1824402", "la fabrication de chaussures en matières textiles sans semelle rapportée.", Category.CLASS
        ),
        Classification("18300", "Industrie des fourrures", Category.CLASS),
        Classification(
            "1830001",
            "la préparation et la teinture des pelleteries et des peaux non épilées : drayage, corroyage, tannage, blanchiment, tondage, épluchage et teinture",
            Category.CLASS,
        ),
        Classification(
            "1830002", "la fabrication de vêtements et accessoires du vêtement en pelleteries.", Category.CLASS
        ),
        Classification(
            "1830003",
            'assemblages de pelleteries telles que peaux dites "allongées", nappes, nappettes, carrés, bandes, etc.',
            Category.CLASS,
        ),
        Classification(
            "1830004",
            "fabrication d'articles divers en fourrures : tapis, poufs non garnis, peaux à polir pour l'industrie, etc.",
            Category.CLASS,
        ),
        Classification(
            "1830005", "la fabrication de pelleteries factices et d'articles en ces pelleteries.", Category.CLASS
        ),
        Classification("19100", "Apprêt et tannage des cuirs", Category.CLASS),
        Classification("1910001", "la production de cuir tanné", Category.CLASS),
        Classification(
            "1910002", "la fabrication de cuirs et peaux chamoisés, parcheminés, vernis ou métallisés", Category.CLASS
        ),
        Classification("1910003", "la fabrication de cuirs reconstitués", Category.CLASS),
        Classification("1910004", "la finition du cuir.", Category.CLASS),
        Classification("19200", "Fabrication d'articles de voyage, de maroquinerie et de sellerie", Category.CLASS),
        Classification(
            "1920001",
            "la fabrication d'articles de voyage, de maroquinerie et art. similaires en cuir naturel ou reconstitué ou autre matériau, p.ex.les matières plastiques,textiles,carton etc., pour autant que la technolo",
            Category.CLASS,
        ),
        Classification("1920002", "la fabrication d'articles de sellerie et de bourrellerie", Category.CLASS),
        Classification("1920003", "la fabrication de bracelets de montre non métalliques", Category.CLASS),
        Classification(
            "1920004",
            "la fabrication d'articles divers en cuir naturel ou reconstitué : courroies, joints, garnitures, etc.",
            Category.CLASS,
        ),
        Classification(
            "19301", "Fabrication de chaussures, à l'exclusion des chaussures en caoutchouc", Category.CLASS
        ),
        Classification(
            "1930101",
            "la fabrication de chaussures pour tous usages, par tous procédés (y compris le moulage) et en toutes matières, à  l'exclusion des chaussures en caoutchouc",
            Category.CLASS,
        ),
        Classification("1930102", "la fabrication de guêtres, de jambières et d'articles similaires", Category.CLASS),
        Classification(
            "1930103",
            "la fabrication de parties de chaussures : dessus et parties de dessus, semelles extérieures et intérieures, talons, etc. à l'exclusion des parties en caoutchouc.",
            Category.CLASS,
        ),
        Classification("19302", "Fabrication de chaussures en caoutchouc", Category.CLASS),
        Classification(
            "1930201",
            "la fabrication de chaussures en caoutchouc, pour tous usages et par tous procédés (y compris le moulage)",
            Category.CLASS,
        ),
        Classification(
            "1930202",
            "la fabrication de parties de chaussures : dessus et parties de dessus, semelles, talons...en caoutchouc.",
            Category.CLASS,
        ),
        Classification("20101", "Sciage et rabotage du bois", Category.CLASS),
        Classification("2010101", "le sciage, le rabotage et le façonnage du bois", Category.CLASS),
        Classification(
            "2010102", "la fabrication de traverses en bois pour voies ferrées et de poteaux de ligne", Category.CLASS
        ),
        Classification("2010103", "la fabrication de lames non assemblées pour parquets", Category.CLASS),
        Classification(
            "2010104",
            "le séchage du bois et l'imprégnation ou le traitement chimique du bois au moyen d'agents de conservation ou d'autres produits, en combinaison avec le sciage et le façonnage",
            Category.CLASS,
        ),
        Classification(
            "2010105",
            "la fabrication de laine de bois, de farine de bois, de bois en copeaux ou en particules.",
            Category.CLASS,
        ),
        Classification("20102", "Imprégnation du bois", Category.CLASS),
        Classification(
            "2010201",
            "l'imprégnation ou le traitement chimique du bois au moyen d'agents de conservation ou d'autres produits pour compte de tiers.",
            Category.CLASS,
        ),
        Classification("20200", "Fabrication de panneaux de bois", Category.CLASS),
        Classification("2020001", "la fabrication de placage", Category.CLASS),
        Classification(
            "2020002",
            "la fabrication de contre-plaqués (duplex, triplex et multiplex), de panneaux pour meubles, de panneaux de fibres, de panneaux de particules et de panneaux similaires.",
            Category.CLASS,
        ),
        Classification("20300", "Fabrication de charpentes et de menuiseries", Category.CLASS),
        Classification("20301", "Fabrication article en bois (construction)", Category.CLASS),
        Classification("2030101", "FAB.DE POUTRES, POUTRELLES, CHEVRONS, ...", Category.CLASS),
        Classification("2030102", "FAB. PORTES, FENêTRES, VOLETS, CLôTUR,..", Category.CLASS),
        Classification("2030103", "FAB. D'ESCALIERS, RAMPES D'ESCALIERS", Category.CLASS),
        Classification("2030104", "FAB. BARDEAUX, BAGUETTES & MOULUR. BOIS", Category.CLASS),
        Classification("2030105", "FAB. BLOCS, LAMES, ASSEMB. PR PARQUETS", Category.CLASS),
        Classification("2030106", "FAB. BâTIMENTS PRéFAB./D'éLéMENTS", Category.CLASS),
        Classification("2030107", "FAB. CONSTRUC. SS ROUES : CARAVANS", Category.CLASS),
        Classification("20400", "Fabrication d'emballages en bois", Category.CLASS),
        Classification(
            "2040001",
            "la fabrication de caisses, de caissettes, de cageots, de cylindres et d'emballages similaires en bois",
            Category.CLASS,
        ),
        Classification(
            "2040002",
            "la fabrication de palettes simples, de caisses-palettes et d'autres plateaux de chargement en bois",
            Category.CLASS,
        ),
        Classification(
            "2040003",
            "la fabrication de tonneaux, de cuves, de baquets et d'autres ouvrages de tonnellerie en bois",
            Category.CLASS,
        ),
        Classification("2040004", "la fabrication de tambours en bois pour câbles.", Category.CLASS),
        Classification("20510", "Fabrication d'objets divers en bois", Category.CLASS),
        Classification(
            "2051001",
            "la fabrication d'articles de ménage et ustensiles de cuisine en bois : planches à repasser, porte-manteaux, etc.",
            Category.CLASS,
        ),
        Classification(
            "2051002",
            "la fabrication de statuettes et objets d'ornement en bois, en bois marquetés ou en bois incrustés",
            Category.CLASS,
        ),
        Classification(
            "2051003",
            "la fabrication de coffrets, écrins et étuis pour bijouterie ou orfèvrerie et ouvrages similaires en bois",
            Category.CLASS,
        ),
        Classification(
            "2051004",
            "la fabrication de bâtons ronds pour stores, manches et montures en bois pour outils, brosses et balais",
            Category.CLASS,
        ),
        Classification(
            "2051005",
            "la fabrication de cannettes, busettes, bobines pour filatures et tissage, bobines pour fil à coudre et articles similaires en bois tourné",
            Category.CLASS,
        ),
        Classification(
            "2051006",
            "la fabrication de formes, embauchoirs et tendeurs pour chaussures, cintres pour vêtements",
            Category.CLASS,
        ),
        Classification("2051007", "la fabrication de cercueils", Category.CLASS),
        Classification("2051008", "la fabrication d'échelles", Category.CLASS),
        Classification("2051009", "la fabrication de cadres en bois pour tableaux.", Category.CLASS),
        Classification("20520", "Fabrication d'objets en liège, vannerie ou sparterie", Category.CLASS),
        Classification("2052001", "le travail du liège naturel", Category.CLASS),
        Classification("2052002", "la fabrication d'articles en liège naturel ou aggloméré", Category.CLASS),
        Classification(
            "2052003",
            "la fabrication de tresses et d'articles de sparterie : nattes, paillassons, claies, etc.",
            Category.CLASS,
        ),
        Classification("2052004", "la fabrication d'ouvrages de vannerie.", Category.CLASS),
        Classification("21110", "Fabrication de pâte à papier", Category.CLASS),
        Classification(
            "2111001",
            "la fabrication de pâtes à papier blanchies, mi-blanchies ou écrues; le désencrage de vieux papiers et la fabrication de pâtes à papier à partir de déchets de papier.",
            Category.CLASS,
        ),
        Classification("21121", "Fabrication de papier", Category.CLASS),
        Classification(
            "2112101",
            "la fabrication de papiers destinés à faire l'objet d'une transformation ultérieure par l'industrie",
            Category.CLASS,
        ),
        Classification("2112102", "le couchage, l'enduction et l'imprégnation des papiers", Category.CLASS),
        Classification("2112103", "la fabrication de papiers asphaltés", Category.CLASS),
        Classification("2112104", "la fabrication de papiers crêpés ou plissés", Category.CLASS),
        Classification(
            "2112105", "la fabrication de papier journal et de papier pour l'impression ou l'écriture", Category.CLASS
        ),
        Classification(
            "2112106", "la fabrication de papiers de fantaisie et d'autres papiers spéciaux", Category.CLASS
        ),
        Classification(
            "2112107", "la fabrication d'ouate de cellulose et de nappes en fibres de cellulose.", Category.CLASS
        ),
        Classification("21122", "Fabrication de carton", Category.CLASS),
        Classification(
            "2112201",
            "la fabrication de cartons destinés à faire l'objet d'une transformation ultérieure par l'industrie",
            Category.CLASS,
        ),
        Classification("2112202", "le couchage, l'enduction et l'imprégnation des cartons.", Category.CLASS),
        Classification("21210", "Fabrication de carton ondulé et d'emballages en papier ou en carton", Category.CLASS),
        Classification("2121001", "la fabrication de papiers et de cartons ondulés", Category.CLASS),
        Classification("2121002", "la fabrication d'emballages en papiers ou en cartons ondulés", Category.CLASS),
        Classification("2121003", "la fabrication de cartonnages pliants", Category.CLASS),
        Classification("2121004", "la fabrication d'emballages en carton homogène", Category.CLASS),
        Classification("2121005", "la fabrication d'autres emballages en papier ou en carton", Category.CLASS),
        Classification("2121006", "la fabrication de sacs et sachets en papier", Category.CLASS),
        Classification("2121007", "la fabrication de cartonnages de bureau et d'articles similaires.", Category.CLASS),
        Classification("21220", "Fabrication d'articles en papier à usage sanitaire ou domestique", Category.CLASS),
        Classification(
            "2122001",
            "la fabrication d'articles en papier ou en ouate de cellulose à usage sanitaire ou domestique : serviettes à démaquiller, mouchoirs,essuie-mains,serviettes de table;papier,serviettes et tampons hygiéni",
            Category.CLASS,
        ),
        Classification("21230", "Fabrication d'articles de papeterie", Category.CLASS),
        Classification(
            "2123001", "la fabrication de papiers prêts à l'emploi pour l'écriture et l'imprimerie", Category.CLASS
        ),
        Classification("2123002", "la fabrication de papiers pour imprimantes", Category.CLASS),
        Classification(
            "2123003",
            "la fabrication de papiers autocopiants prêts à l'emploi, de papiers carbone et de stencils",
            Category.CLASS,
        ),
        Classification(
            "2123004",
            "la fabrication de papiers pour enregistrements électrographiques et d'autres papiers pour appareils de mesure et d'enregistrement",
            Category.CLASS,
        ),
        Classification("2123005", "la fabrication de papiers gommés ou adhésifs prêts à l'emploi", Category.CLASS),
        Classification("2123006", "la fabrication d'enveloppes et de cartes-lettres", Category.CLASS),
        Classification(
            "2123007",
            "la fabrication de boîtes, de pochettes et de présentations similaires renfermant un assortiment d'articles de correspondance.",
            Category.CLASS,
        ),
        Classification("21240", "Fabrication de papiers peints", Category.CLASS),
        Classification(
            "2124001",
            "la fabrication de papiers peints et de revêtements muraux similaires, y compris les papiers peints enduits de vinyle",
            Category.CLASS,
        ),
        Classification("2124002", "la fabrication de revêtements muraux en matières textiles.", Category.CLASS),
        Classification("21250", "Fabrication d'autres articles en papier ou en carton", Category.CLASS),
        Classification("2125001", "la fabrication d'étiquettes", Category.CLASS),
        Classification("2125002", "la fabrication de papier-filtre et de carton-filtre", Category.CLASS),
        Classification(
            "2125003", "la fabrication de cannettes, de bobines, de tambours,...en papier ou en carton", Category.CLASS
        ),
        Classification(
            "2125004", "la fabrication de cartes perforées pour métier Jacquard, en papier ou en carton", Category.CLASS
        ),
        Classification(
            "2125005",
            "la fabrication d'emballage pour oeufs et d'autres articles moulés en pâte à papier, pour l'emballage.",
            Category.CLASS,
        ),
        Classification("22110", "Édition de livres", Category.CLASS),
        Classification("2211001", "l'édition de livres, de livres scolaires, de brochures, etc.", Category.CLASS),
        Classification("2211002", "l'édition de dictionnaires et d'encyclopédies", Category.CLASS),
        Classification("2211003", "l'édition d'atlas, de cartes et de plans", Category.CLASS),
        Classification("2211004", "l'édition de livres de musique et de partitions musicales.", Category.CLASS),
        Classification("22120", "Édition de journaux", Category.CLASS),
        Classification(
            "2212001",
            "l'édition de journaux et de journaux régionaux (y compris les journaux publicitaires).",
            Category.CLASS,
        ),
        Classification("22130", "Édition de revues et périodiques", Category.CLASS),
        Classification("2213001", "l'édition de revues, périodiques et magazines.", Category.CLASS),
        Classification("22140", "Édition d'enregistrements sonores", Category.CLASS),
        Classification(
            "2214001",
            "l'édition de disques, de disques compacts et de bandes  contenant de la musique ou d'autres enregistrements sonores.",
            Category.CLASS,
        ),
        Classification("2214002", "l'édition de produits combinant livres et moyens audiovisuels.", Category.CLASS),
        Classification("22150", "Autres activités d'édition", Category.CLASS),
        Classification(
            "2215001",
            "l'édition de : photos, gravures et cartes postales illustrées ; calendriers, horaires et tableaux de service ; affiches et reproduction d'oeuvres d'art.",
            Category.CLASS,
        ),
        Classification("22210", "Imprimerie de journaux", Category.CLASS),
        Classification("2221001", "l'impression de journaux, y compris les journaux publicitaires.", Category.CLASS),
        Classification("22220", "Autre imprimerie", Category.CLASS),
        Classification(
            "2222001",
            "l'impression de magazines,autres périodiques,livres,... sur des presses typographiques,offset,d'héliogravure, flexographiques,sérigraphiques etc,imprimantes électroniques,app. de reproduction,app.de g",
            Category.CLASS,
        ),
        Classification("22230", "Reliure", Category.CLASS),
        Classification(
            "2223001",
            "le pliage, l'assemblage, l'agrafage, la reliure, le collage, le massicotage, le dorage de feuillets imprimés à insérer dans des livres, brochures, périodiques, catalogues, etc.",
            Category.CLASS,
        ),
        Classification(
            "2223002",
            "le pliage,timbrage,perçage,perforage,gaufrage,collage,pelliculage de papiers et cartons imprimés pour e.a. formulaires commerciaux, présentoirs, cartes à échantillons, étiquettes, calendriers, prospec",
            Category.CLASS,
        ),
        Classification("22240", "Activités de pré-presse", Category.CLASS),
        Classification(
            "2224001",
            "la composition, par exemple de textes et d'images, sur film, sur papier photographique ou papier normal",
            Category.CLASS,
        ),
        Classification(
            "2224002",
            "la reproduction : production de formes typographiques, reproduction offset et plaques d'impression, reproduction et cylindres d'héliogravure.",
            Category.CLASS,
        ),
        Classification("22250", "Activités graphiques auxilliaires", Category.CLASS),
        Classification(
            "2225001",
            "la préparation et la production de transparents pour rétroprojecteurs, ébauches, maquettes, etc.",
            Category.CLASS,
        ),
        Classification(
            "2225002",
            "la préparation de données digitales : l'enrichissement, la sélection, la liaison de données digitales stockées dans des appareils de traitement électronique de données",
            Category.CLASS,
        ),
        Classification("2225003", "autres activités graphiques.", Category.CLASS),
        Classification("22310", "Reproduction d'enregistrements sonores", Category.CLASS),
        Classification(
            "2231001",
            "la reproduction, à partir d'une matrice, de disques, de disques compacts, de bandes et de cassettes contenant de la musique ou d'autres enregistrements sonores.",
            Category.CLASS,
        ),
        Classification("22320", "Reproduction d'enregistrements vidéo", Category.CLASS),
        Classification(
            "2232001",
            "la reproduction, à partir d'une matrice, de disques, de disques compacts, de bandes et de cassettes contenant des films ou d'autres enregistrements vidéo.",
            Category.CLASS,
        ),
        Classification("22330", "Reproduction d'enregistrements informatiques", Category.CLASS),
        Classification(
            "2233001",
            "la reproduction, à partir d'une matrice, de logiciels et de données informatiques sur disques, disquettes, disques compacts, bandes ou cassettes.",
            Category.CLASS,
        ),
        Classification("23100", "Cokéfaction", Category.CLASS),
        Classification("2310001", "la production de coke", Category.CLASS),
        Classification("2310002", "la production de gaz de cokerie", Category.CLASS),
        Classification("2310003", "la production de goudrons bruts de houille et de lignite.", Category.CLASS),
        Classification("23200", "Raffinage de pétrole", Category.CLASS),
        Classification("2320001", "la production de carburants pour moteurs : essence, kérosène, etc.", Category.CLASS),
        Classification(
            "2320002",
            "la production de combustibles : fiouls légers et lourds, gaz de raffinerie tels que l'éthane, le propane, le butane, le GPL, etc.",
            Category.CLASS,
        ),
        Classification(
            "2320003",
            "la fabrication d'huiles de graissage et de graisses lubrifiantes à partir de pétrole, y compris les résidus de raffinage",
            Category.CLASS,
        ),
        Classification("2320004", "la fabrication de produits de base pour la pétrochimie", Category.CLASS),
        Classification("2320005", "la fabrication de produits pour revêtements routiers", Category.CLASS),
        Classification(
            "2320006",
            "la fabrication de produits pétroliers raffinés divers : white-spirit, vaseline, paraffine, etc.",
            Category.CLASS,
        ),
        Classification("23300", "Elaboration et transformation de matières nucléaires", Category.CLASS),
        Classification("2330001", "la production d'uranium et de thorium enrichis", Category.CLASS),
        Classification("2330002", "la production d'éléments combustibles pour centrales nucléaires", Category.CLASS),
        Classification("2330003", "la production de radioéléments à usage industriel ou médical", Category.CLASS),
        Classification("2330004", "le traitement des déchets de l'industrie nucléaire.", Category.CLASS),
        Classification("24110", "Fabrication de gaz industriels", Category.CLASS),
        Classification("2411001", "la fabrication de gaz élémentaires", Category.CLASS),
        Classification(
            "2411002",
            "la fabrication d'air liquide ou comprimé et ses composants (azote, oxygène, argon, etc.)",
            Category.CLASS,
        ),
        Classification("2411003", "la fabrication de gaz réfrigérants", Category.CLASS),
        Classification("2411004", "la fabrication de gaz industriels mélangés", Category.CLASS),
        Classification("2411005", "la fabrication de gaz inertes tel l'anhydride carbonique", Category.CLASS),
        Classification("2411006", "la fabrication de gaz isolants.", Category.CLASS),
        Classification("24120", "Fabrication de colorants et de pigments", Category.CLASS),
        Classification(
            "2412001",
            "la fabrication, sous forme fondamentale ou concentrée, de colorants et de pigments, quelle que soit l'origine",
            Category.CLASS,
        ),
        Classification(
            "2412002",
            "la fabrication de produits utilisés comme agents d'avivage ou comme luminophores.",
            Category.CLASS,
        ),
        Classification("24130", "Fabrication d'autres produits chimiques inorganiques de base", Category.CLASS),
        Classification(
            "2413001",
            "la fabrication d'éléments chimiques, à l'exclusion des métaux, des gaz élémentaires d'origine industrielle et des éléments radioactifs issus de l'industrie des combustibles nucléaires",
            Category.CLASS,
        ),
        Classification(
            "2413002", "la fabrication des acides inorganiques, à l'exclusion de l'acide nitrique", Category.CLASS
        ),
        Classification(
            "2413003",
            "la fabrication d'alcalis, de lessives et d'autres bases inorganiques, à l'exclusion de l'ammoniac",
            Category.CLASS,
        ),
        Classification("2413004", "la fabrication de chlorures, d'hypochlorites et d'eau de Javel", Category.CLASS),
        Classification("2413005", "la fabrication de sels métalliques inorganiques", Category.CLASS),
        Classification("2413006", "le grillage de la pyrite de fer", Category.CLASS),
        Classification("2413007", "la fabrication d'autres composés inorganiques.", Category.CLASS),
        Classification("24140", "Fabrication d'autres produits chimiques organiques de base", Category.CLASS),
        Classification(
            "2414001", "la fabrication de hydrocarbures cycliques et acycliques, saturés ou non saturés", Category.CLASS
        ),
        Classification(
            "2414002",
            "la fabrication d'alcools acycliques et cycliques, y compris l'alcool éthylique de synthèse",
            Category.CLASS,
        ),
        Classification(
            "2414003",
            "la fabrication d'acides monocarboxyliques et polycarboxyliques, y compris l'acide acétique",
            Category.CLASS,
        ),
        Classification(
            "2414004",
            "la fabrication d'autres composés à fonctions oxygénées, y compris les aldéhydes, les cétones, les quinones et les composés contenant deux fonctions oxygénées ou plus",
            Category.CLASS,
        ),
        Classification(
            "2414005", "la fabrication de composés organiques à fonctions azotées, y compris les amines", Category.CLASS
        ),
        Classification("2414006", "la fabrication des sels métalliques organiques", Category.CLASS),
        Classification(
            "2414007",
            "la fabrication d'autres composés organiques, y compris les produits de la distillation du bois, etc",
            Category.CLASS,
        ),
        Classification(
            "2414008",
            "la fabrication de produits chimiques organiques de base utilisés pour la fabrication de produits pharmaceutiques",
            Category.CLASS,
        ),
        Classification("2414009", "la fabrication de produits aromatiques synthétiques", Category.CLASS),
        Classification("2414010", "la production de charbon de bois", Category.CLASS),
        Classification("2414011", "la production de brai et de coke de brai", Category.CLASS),
        Classification("2414012", "la distillation des goudrons de houille", Category.CLASS),
        Classification("24151", "Fabrication d'engrais", Category.CLASS),
        Classification(
            "2415101",
            "la fabrication d'engrais: engrais azotés, phosphatés ou potassiques, simples ou complexes; urée, phosphates naturels bruts et sels de potassium naturels bruts",
            Category.CLASS,
        ),
        Classification("24152", "Fabrication de produits azotés associés aux engrais", Category.CLASS),
        Classification(
            "2415201",
            "la fabrication d'acides nitrique et sulfonitrique, ammoniac, chlorure d'ammonium, nitrites et nitrates de potassium, phosphates de triammonium et carbonates d'ammonium",
            Category.CLASS,
        ),
        Classification("24160", "Fabrication de matières plastiques de base", Category.CLASS),
        Classification(
            "2416001",
            "la fabrication des polymères, y compris les polymères acryliques et les polymères d'éthylène, de propylène, de styrène, de chlorure de vinyle, d'acétate de vinyle",
            Category.CLASS,
        ),
        Classification("2416002", "la fabrication de polyamides", Category.CLASS),
        Classification(
            "2416003", "la fabrication de résines phénoliques, résines époxydes et polyuréthanes", Category.CLASS
        ),
        Classification(
            "2416004", "la fabrication de résines alkydes, résines polyesters et polyéthers", Category.CLASS
        ),
        Classification("2416005", "la fabrication de silicones", Category.CLASS),
        Classification("2416006", "la fabrication d'échangeurs d'ions à base de polymères", Category.CLASS),
        Classification(
            "2416007", "la préparation de mélanges de matières plastiques de base, colorées ou non", Category.CLASS
        ),
        Classification("2416008", "la fabrication de celluloses", Category.CLASS),
        Classification("24170", "Fabrication de caoutchouc synthétique", Category.CLASS),
        Classification(
            "2417001",
            "la fabrication de caoutchouc synthétique sous formes primaires - caoutchouc factice - caoutchouc synthétique",
            Category.CLASS,
        ),
        Classification(
            "2417002",
            "la fabrication de mélanges de caoutchouc synthétique et de caoutchouc naturel ou de gommes caoutchouteuses (ex. le balata)",
            Category.CLASS,
        ),
        Classification("24200", "Fabrication de produits agrochimiques", Category.CLASS),
        Classification(
            "2420001",
            "la fabrication d'insecticides, d'antirongeurs, de fongicides d'herbicides, d'inhibiteurs de germination, de régulateurs de croissance pour plantes, de désinfectants et autres produits chimiques",
            Category.CLASS,
        ),
        Classification("24300", "Fabrication de peintures, vernis, encres d'imprimerie et mastics", Category.CLASS),
        Classification("2430001", "la fabrication de peintures et de vernis", Category.CLASS),
        Classification("2430002", "la fabrication de pigments, d'opacifiants et de couleurs préparés", Category.CLASS),
        Classification("2430003", "la fabrication de compositions vitrifiables, d'engobes, etc.", Category.CLASS),
        Classification("2430004", "la fabrication de mastics", Category.CLASS),
        Classification(
            "2430005",
            "la fabrication d'enduits utilisés en peinture et autres enduits non-réfractaires",
            Category.CLASS,
        ),
        Classification(
            "2430006",
            "la fabrication de solvants et de diluants organiques composites, et la préparation de décapants pour peintures et vernis",
            Category.CLASS,
        ),
        Classification(
            "2430007",
            "la fabrication de produits liquides pour la protection du bois et de préparations liquides hydrofuges à base de silicone",
            Category.CLASS,
        ),
        Classification("2430008", "la fabrication d'encres d'imprimerie", Category.CLASS),
        Classification("24410", "Fabrication de produits pharmaceutiques de base", Category.CLASS),
        Classification(
            "2441001",
            "l'étude, la mise au point de la production des principes actifs destinés à la fabrication de médicaments",
            Category.CLASS,
        ),
        Classification("2441002", "la fabrication des acides salicylique et o-acétylsalicylique", Category.CLASS),
        Classification("2441003", "le traitement du sang", Category.CLASS),
        Classification("2441004", "la fabrication de sucres chimiquement purs", Category.CLASS),
        Classification("2441005", "la fabrication de sucres synthétiquement purs", Category.CLASS),
        Classification("2441006", "la fabrication d'édulcorants de synthèse", Category.CLASS),
        Classification("24421", "Fabrication de médicaments", Category.CLASS),
        Classification(
            "2442101", "la fabrication des serums thérapeutiques et autres constituants du sangs", Category.CLASS
        ),
        Classification("2442102", "la fabrication de vaccins", Category.CLASS),
        Classification(
            "2442103", "la fabrication de médicaments divers, y compris les préparations homéopathiques", Category.CLASS
        ),
        Classification(
            "2442104",
            "préparations chimiques contraceptives à usage externe et médicaments contraceptifs à base d'hormones",
            Category.CLASS,
        ),
        Classification("2442105", "la fabrication de préparations vétérinaires", Category.CLASS),
        Classification("2442106", "la fabrication de tisanes de plantes médicinales", Category.CLASS),
        Classification("24422", "Fabrication d'autres produits pharmaceutiques", Category.CLASS),
        Classification(
            "2442201",
            "la fabrication de produits d'obturation dentaire et de ciments pour la réfection osseuse",
            Category.CLASS,
        ),
        Classification(
            "2442202",
            "la fabrication d'ouates, de gazes et de bandes imprégnées à usage médical, de pansements, de catguts, etc.",
            Category.CLASS,
        ),
        Classification("24511", "Fabrication de savons et de détergents", Category.CLASS),
        Classification("2451101", "la fabrication d'agents organiques de surface", Category.CLASS),
        Classification("2451102", "la fabrication de savons", Category.CLASS),
        Classification("2451103", "la fabrication de glycérine", Category.CLASS),
        Classification(
            "2451104",
            "la fabrication de préparations tensioactives: - produits pour lessives sous formes solides ou liquides, détergents; - préparations pour la vaisselle - adoucissants pour textiles",
            Category.CLASS,
        ),
        Classification("24512", "Fabrication de produits d'entretien et de nettoyage", Category.CLASS),
        Classification(
            "2451201", "la fabrication de préparations pour parfumer ou désodoriser les locaux", Category.CLASS
        ),
        Classification("2451202", "la fabrication de cires artificielles ou cires préparées", Category.CLASS),
        Classification(
            "2451203",
            "la fabrication de produits d'entretien pour le cuir, le bois, le verre et les métaux",
            Category.CLASS,
        ),
        Classification("2451204", "la fabrications de produits d'entretien pour carrosseries", Category.CLASS),
        Classification("2451205", "la fabrication de pâtes et poudres à récurer", Category.CLASS),
        Classification("24520", "Fabrication de parfums et de produits pour la toilette", Category.CLASS),
        Classification("2452001", "la fabrication de parfums et eaux de toilette", Category.CLASS),
        Classification("2452002", "la fabrication de produits de beauté ou de maquillage", Category.CLASS),
        Classification(
            "2452003", "la fabrication de préparations antisolaires et préparations pour le bronzage", Category.CLASS
        ),
        Classification("2452004", "la fabrication de préparations pour manucures et pédicures", Category.CLASS),
        Classification(
            "2452005",
            "la fabrication de shampoings, laques pour cheveux, préparations pour l'ondulation et le défrisage des cheveux",
            Category.CLASS,
        ),
        Classification(
            "2452006",
            "la fabrication de dentifrices et produits pour l'hygiène buccale, y compris les préparations destinées à faciliter l'adhérence des dentiers",
            Category.CLASS,
        ),
        Classification("2452007", "la fabrication de préparations pour le rasage", Category.CLASS),
        Classification("2452008", "la fabrication de désodorisants et sels pour le bain", Category.CLASS),
        Classification("2452009", "la fabrication de dépilatoires", Category.CLASS),
        Classification("24610", "Fabrication de produits explosifs", Category.CLASS),
        Classification("2461001", "la fabrication de poudres propulsives", Category.CLASS),
        Classification("2461002", "la fabrication d'explosifs", Category.CLASS),
        Classification(
            "2461003", "la fabrication d'amorces, de détonateurs et de fusées de signalisation", Category.CLASS
        ),
        Classification("2461004", "la fabrication d'articles de pyrotechnie", Category.CLASS),
        Classification("24620", "Fabrication de colles et gélatines", Category.CLASS),
        Classification("2462001", "la fabrication de gélatines et de leurs dérivés", Category.CLASS),
        Classification(
            "2462002",
            "la fabrication de colles et d'adhésifs préparés, y compris les colles et adhésifs à base de caoutchouc ou de matière plastique",
            Category.CLASS,
        ),
        Classification("2462003", "la fabrication de ciments-colles", Category.CLASS),
        Classification("24630", "Fabrication d'huiles essentielles", Category.CLASS),
        Classification("2463001", "la fabrication d'essences et de produits aromatiques naturels", Category.CLASS),
        Classification("2463002", "la fabrication de résinoïdes", Category.CLASS),
        Classification("2463003", "la fabrication d'eaux distillées aromatiques", Category.CLASS),
        Classification(
            "2463004",
            "la fabrications de compositions à base de produits odoriférants pour la parfumerie ou l'alimentation",
            Category.CLASS,
        ),
        Classification("24640", "Fabrication de produits chimiques pour la photographie", Category.CLASS),
        Classification(
            "2464001",
            "la fabrication de plaques et films photographiques, de papiers sensibilisés et d'autres matières sensibilisées non impressionnées",
            Category.CLASS,
        ),
        Classification("2464002", "la fabrication de préparations chimiques à usage photographique", Category.CLASS),
        Classification("24650", "Fabrication de supports de données", Category.CLASS),
        Classification(
            "2465001", "la fabrication de supports vierges pour l'enregistrement du son ou de l'image", Category.CLASS
        ),
        Classification(
            "2465002",
            "la fabrication de disques et de bandes vierges pour l'enregistrement de données informatiques",
            Category.CLASS,
        ),
        Classification("24660", "Fabrication d'autres produits chimiques", Category.CLASS),
        Classification(
            "2466001",
            "la fabrication de peptones et leurs dérivés, autres matières protéiques et leurs dérivés n.d.a.",
            Category.CLASS,
        ),
        Classification(
            "2466002", "la fabrication d'huiles et graisses modifiées par des procédés chimiques", Category.CLASS
        ),
        Classification(
            "2466003",
            "la fabrication d'huiles synthétiques spéciales de graissage et additifs pour huiles lubrifiantes",
            Category.CLASS,
        ),
        Classification(
            "2466004",
            "la fabrication de produits utilisés pour l'apprêt ou le finissage des textiles et du cuir",
            Category.CLASS,
        ),
        Classification("2466005", "la fabrication de pâtes et poudres à souder ou à braser", Category.CLASS),
        Classification("2466006", "la fabrication de préparations pour le décapage des métaux", Category.CLASS),
        Classification("2466007", "la fabrication d'additifs préparés pour ciments", Category.CLASS),
        Classification(
            "2466008",
            'la fabrication de charbons activés, préparations dites "accélérateurs de vulcanisation", catalyseurs et autres produits chimiques à usage industriel',
            Category.CLASS,
        ),
        Classification(
            "2466009",
            "la fabrication de préparations antidétonantes, préparations antigel, liquides pour transmissions hydrauliques",
            Category.CLASS,
        ),
        Classification(
            "2466010", "la fabrication de réactifs composés de diagnostic ou de laboratoire", Category.CLASS
        ),
        Classification("2466011", "la fabrication d'encres à écrire et à dessiner", Category.CLASS),
        Classification("24700", "Fabrication de fibres artificielles ou synthétiques", Category.CLASS),
        Classification("2470001", "la fabrication de câbles de filaments synthétiques ou artificiels", Category.CLASS),
        Classification(
            "2470002",
            "la fabrication de fibres synthétique ou artificielles discontinues, non cardées ni peignées ni autrement transformées pour la filature",
            Category.CLASS,
        ),
        Classification(
            "2470003",
            "la fabrication de fils synthétiques ou artificiels simples, y compris les fils à haute ténacité",
            Category.CLASS,
        ),
        Classification(
            "2470004",
            "la fabrication de monofilaments synthétiques ou artificiels et de lames en matières textiles synthétiques ou artificielles",
            Category.CLASS,
        ),
        Classification("25110", "Fabrication de pneumatiques et de chambres à air", Category.CLASS),
        Classification(
            "2511001",
            "la fabrication de pneumatiques en caoutchouc pour véhicules, avions, tracteurs agricoles, équipements, machines mobiles, etc.: - pneumatiques - bandages pleins ou creux",
            Category.CLASS,
        ),
        Classification("2511002", "la fabrication de chambres à air pour pneumatiques", Category.CLASS),
        Classification(
            "2511003",
            "la fabrication de bandes de roulement amovibles pour pneumatiques, de flaps, de profilés pour le rechapage des pneumatiques, etc.",
            Category.CLASS,
        ),
        Classification("25120", "Rechapage de pneumatiques", Category.CLASS),
        Classification("2512001", "le rechapage et le resculptage de pneumatiques", Category.CLASS),
        Classification("25130", "Fabrication d'autres articles en caoutchouc", Category.CLASS),
        Classification(
            "2513001",
            "la fabrication de plaques, feuilles, bandes, baguettes, profilés, etc. en caoutchouc",
            Category.CLASS,
        ),
        Classification("2513002", "la fabrication de tubes et tuyaux", Category.CLASS),
        Classification("2513003", "la fabrication de courroies transporteuses ou de transmission", Category.CLASS),
        Classification(
            "2513004",
            "la fabrication d'articles d'hygiène en caoutchouc: préservatifs, tétines, bouillottes, etc.",
            Category.CLASS,
        ),
        Classification(
            "2513005",
            "la fabrication d'articles d'habillement en caoutchouc, non assemblés par couture, mais simplement collés",
            Category.CLASS,
        ),
        Classification("2513006", "la fabrication de revêtements de sols", Category.CLASS),
        Classification("2513007", "la fabrication de textiles caoutchoutés", Category.CLASS),
        Classification("2513008", "la fabrication de fils et cordes", Category.CLASS),
        Classification("2513009", "la fabrication de fils et tissus caoutchoutés", Category.CLASS),
        Classification(
            "2513010", "la fabrication de bagues, anneaux, joints, rondelles et accessoires", Category.CLASS
        ),
        Classification("2513011", "la fabrication de revêtements de cylindres", Category.CLASS),
        Classification("2513012", "la fabrication de matelas pneumatiques", Category.CLASS),
        Classification("2513013", "la fabrication de matériaux de réparation en caoutchouc", Category.CLASS),
        Classification(
            "25210", "Fabrication de plaques, feuilles, tubes et profilés en matières plastiques", Category.CLASS
        ),
        Classification(
            "2521001",
            "la fabrication de produits semi-finis en matières plastiques plaques, feuilles, blocs, pellicules, bandes, lames, etc.",
            Category.CLASS,
        ),
        Classification(
            "2521002",
            "la fabrication de produits finis en matières plastiques: tubes, tuyaux et accessoires de tubes et tuyaux",
            Category.CLASS,
        ),
        Classification("25220", "Fabrication d'emballages en matières plastiques", Category.CLASS),
        Classification(
            "2522001",
            "la fabrication d'articles d'emballage en matières plastiques sacs, sachets, conteneurs, boîtes, caisses, bonbonnes, bouteilles, bouchons, etc.",
            Category.CLASS,
        ),
        Classification("25230", "Fabrication d'éléments en matières plastiques pour la construction", Category.CLASS),
        Classification(
            "2523001",
            "la fabrication de portes et fenêtres avec cadres et chambranles, volets, stores, plinthes, moulures, etc.",
            Category.CLASS,
        ),
        Classification("2523002", "la fabrication de cuves, foudres et réservoirs", Category.CLASS),
        Classification(
            "2523003",
            "la fabrication de revêtements de sols, de murs et de plafond isolants ou non, sous forme de rouleaux, de dalles, de carreaux, etc.",
            Category.CLASS,
        ),
        Classification(
            "2523004",
            "la fabrication d'articles en matières plastiques pour usages sanitaires ou hygiéniques: baignoires, douches, lavabos, bidets, cuvettes d'aisance, réservoirs de chasse, etc.",
            Category.CLASS,
        ),
        Classification("25240", "Fabrication d'autres articles en matières plastiques", Category.CLASS),
        Classification(
            "2524001",
            "la fabrication de vaisselle et autres pour le service de la table ou de la cuisine, et d'articles d'hygiène ou de toilette",
            Category.CLASS,
        ),
        Classification(
            "2524002",
            "la fabrication de produits divers en matières plastiques: - coiffures, pièces isolantes, parties d'appareils d'éclairage, fournitures de bureau et fournitures scolaires, articles d'habillement, garnit",
            Category.CLASS,
        ),
        Classification(
            "2524003",
            "la fabrication d'articles en matières plastiques (y compris les matériaux composites) pour usages techniques, sur devis et pour compte de tiers",
            Category.CLASS,
        ),
        Classification(
            "2524004", "la fabrication pour compte de tiers de parties de jouets en matières plastiques", Category.CLASS
        ),
        Classification("26110", "Fabrication de verre plat", Category.CLASS),
        Classification(
            "2611001", "la fabrication de verre plat, y compris le verre plat armé, coloré ou teinté", Category.CLASS
        ),
        Classification("26120", "Façonnage et transformation du verre plat", Category.CLASS),
        Classification(
            "2612001", "la fabrication de verre plat trempé ou formé de feuilles contre-collées", Category.CLASS
        ),
        Classification("2612002", "la fabrication de miroirs en verre", Category.CLASS),
        Classification("2612003", "la fabrication de vitrages isolants à parois multiples", Category.CLASS),
        Classification("26130", "Fabrication de verre creux", Category.CLASS),
        Classification(
            "2613001",
            "la fabrication de bouteilles et de flacons, de pots, de bocaux et autres récipients en verre ou en cristal",
            Category.CLASS,
        ),
        Classification(
            "2613002",
            "la fabrication de verres à boire et d'autres articles en verre ou en cristal à usage domestique",
            Category.CLASS,
        ),
        Classification("2613003", "la fabrication d'articles décoratifs en verre ou en cristal", Category.CLASS),
        Classification("2613004", "le façonnage du verre creux: taille, gravure, etc.", Category.CLASS),
        Classification("26140", "Fabrication de fibres de verre", Category.CLASS),
        Classification(
            "2614001", "la fabrication de fibres de verre et de produits non tissés en cette matière", Category.CLASS
        ),
        Classification("2614002", "la fabrication de laine de verre pour l'isolation", Category.CLASS),
        Classification("2614003", "la fabrication de fibres optiques", Category.CLASS),
        Classification(
            "26150",
            "Fabrication et façonnage d'autres articles en verre, y compris d'articles techniques en verre",
            Category.CLASS,
        ),
        Classification("2615001", "la fabrication de cônes et écrans pour téléviseurs", Category.CLASS),
        Classification("2615002", "la fabrication d'enveloppes en verre pour lampes", Category.CLASS),
        Classification(
            "2615003", "la fabrication de verrerie de laboratoire, d'hygiène ou de pharmacie", Category.CLASS
        ),
        Classification(
            "2615004",
            "la fabrication de verres d'horlogerie, verres d'optique et éléments d'optique non travaillés optiquement",
            Category.CLASS,
        ),
        Classification("2615005", "la fabrication de verrerie utilisée en bijouterie de fantaisie", Category.CLASS),
        Classification("2615006", "la fabrication de pavés de verre pour la construction", Category.CLASS),
        Classification("2615007", "la fabrication de verre en barres, baguettes ou tubes", Category.CLASS),
        Classification("2615008", "la fabrication d'isolateurs et pièces isolantes en verre", Category.CLASS),
        Classification(
            "26211", "Fabrication de produits céramiques en porcelaine à usage domestique et ornemental", Category.CLASS
        ),
        Classification(
            "2621101", "la fabrication de vaisselle et autres articles de ménage en porcelaine", Category.CLASS
        ),
        Classification(
            "2621102", "la fabrication de statuettes et autres objets d'ornementation en porcelaine", Category.CLASS
        ),
        Classification(
            "26212",
            "Fabrication de produits céramiques à usage domestique et ornemental, autres qu'en porcelaine",
            Category.CLASS,
        ),
        Classification(
            "2621201",
            "la fabrication de vaisselle et autres articles de ménage en faïence, grès ou terre commune",
            Category.CLASS,
        ),
        Classification(
            "2621202",
            "la fabrication de statuettes et objets d'ornementation en céramique autre que la porcelaine",
            Category.CLASS,
        ),
        Classification("26220", "Fabrication d'appareils sanitaires en céramique", Category.CLASS),
        Classification("2622001", "la fabrication d'appareils sanitaires en céramique", Category.CLASS),
        Classification("26230", "Fabrication d'isolateurs et pièces isolantes en céramique", Category.CLASS),
        Classification("2623001", "la fabrication d'isolateurs et pièces isolantes en céramique", Category.CLASS),
        Classification("26240", "Fabrication d'autres produits céramiques à usage technique", Category.CLASS),
        Classification(
            "2624001", "la fabrication de produits céramiques pour usages chimiques ou industriels", Category.CLASS
        ),
        Classification(
            "26250", "Fabrication d'autres produits céramiques autres que pour la construction", Category.CLASS
        ),
        Classification(
            "2625001",
            "la fabrication de cruchons et de récipients similaires, de transport ou d'emballage, en céramique",
            Category.CLASS,
        ),
        Classification("2625002", "la fabrications de produits céramiques n.d.a.", Category.CLASS),
        Classification("26260", "Fabrication de produits céramiques réfractaires", Category.CLASS),
        Classification("2626001", "la fabrication de mortiers, de bétons,..., réfractaires", Category.CLASS),
        Classification(
            "2626002", "la fabrication d'articles céramiques calorifuges en farines siliceuses fossiles", Category.CLASS
        ),
        Classification("2626003", "la fabrication de briques et dalles réfractaires", Category.CLASS),
        Classification(
            "2626004",
            "la fabrication de cornues, creusets, moufles, busettes, tubes, tuyaux, ... en céramique réfractaire",
            Category.CLASS,
        ),
        Classification(
            "2626005",
            "la fabrication d'articles contenant de la magnésite, de la dolomie ou de la chromite",
            Category.CLASS,
        ),
        Classification("26300", "Fabrication de carreaux en céramique", Category.CLASS),
        Classification(
            "2630001",
            "la fabrication de carreaux pour le revêtement des murs et des cheminées, d'abacules, en céramique non réfractaire",
            Category.CLASS,
        ),
        Classification(
            "2630002", "la fabrication de carreaux et dalles de pavement en céramique non réfractaire", Category.CLASS
        ),
        Classification("26401", "Fabrication de tuiles", Category.CLASS),
        Classification("2640101", "la fabrication de tuiles en terre cuite", Category.CLASS),
        Classification("26402", "Fabrication de briques", Category.CLASS),
        Classification(
            "2640201",
            "la fabrication de briques et des briques perforées ou creuses en terre cuite non réfractaire",
            Category.CLASS,
        ),
        Classification("26403", "Fabrication d'autres produits en terre cuite pour la construction", Category.CLASS),
        Classification("2640301", "la fabrication de hourdis creux en terre cuite", Category.CLASS),
        Classification(
            "2640302",
            "la fabrication d'éléments de cheminée, tubes, tuyaux, drains, etc., en terre cuite",
            Category.CLASS,
        ),
        Classification("2640303", "la fabrication de tuyaux en grès", Category.CLASS),
        Classification(
            "2640304", "la fabrication de produits divers en terre cuite:  bacs à fleurs, pots, etc.", Category.CLASS
        ),
        Classification("26510", "Fabrication de ciment", Category.CLASS),
        Classification(
            "2651001",
            'la fabrication de ciments dits "clinkers" et de ciments hydrauliques, y compris les ciments portland, les ciments alumineux, les ciments de laitier et les ciments surphosphatés',
            Category.CLASS,
        ),
        Classification("26520", "Fabrication de chaux", Category.CLASS),
        Classification(
            "2652001", "la fabrication de chaux: chaux vive, chaux éteinte et chaux hydraulique", Category.CLASS
        ),
        Classification("26530", "Fabrication de plâtre", Category.CLASS),
        Classification("2653001", "la fabrication de plâtre", Category.CLASS),
        Classification("26610", "Fabrication d'éléments en béton pour la construction", Category.CLASS),
        Classification(
            "2661001",
            "la fabrication d'ouvrages préfabriqués en béton, utilisés en construction: tuiles, carreaux, dalles, briques, hourdis creux, plaques, panneaux, tuyaux, piliers, etc.",
            Category.CLASS,
        ),
        Classification(
            "2661002",
            "la fabrication d'éléments préfabriqués en béton pour le bâtiment et le génie civil",
            Category.CLASS,
        ),
        Classification("26620", "Fabrication d'éléments en plâtre pour la construction", Category.CLASS),
        Classification(
            "2662001",
            "la fabrication d'ouvrages en plâtre utilisés en construction: plaques et panneaux",
            Category.CLASS,
        ),
        Classification("26630", "Fabrication de béton prêt à l'emploi", Category.CLASS),
        Classification("2663001", "la fabrication de béton prêt à l'emploi, y compris la livraison", Category.CLASS),
        Classification("26640", "Fabrication de mortiers", Category.CLASS),
        Classification("2664001", "la fabrication de mortiers en poudre", Category.CLASS),
        Classification("26650", "Fabrication d'ouvrages en fibre-ciment", Category.CLASS),
        Classification(
            "2665001",
            "la fabrication de matériaux de construction en substances végétales (laine de bois, paille, roseaux, joncs) agglomérés avec un liant minéral (ciment, plâtre, etc.)",
            Category.CLASS,
        ),
        Classification(
            "2665002",
            "la fabrication d'ouvrages en amiante-ciment, cellulose-ciment ou similaires: plaques ondulées ou autres, panneaux, carreaux,tuiles, tuyaux, gaines, réservoirs, auges, bassins, éviers, cruchons, meuble",
            Category.CLASS,
        ),
        Classification("26660", "Fabrication d'autres ouvrages en béton, en plâtre ou en ciment", Category.CLASS),
        Classification(
            "2666001",
            "la fabrication d'autres ouvrages en béton, en ciment, en plâtre ou en pierre artificielle, sans rapport direct avec la construction: statues,meubles, bas-reliefs,hauts-reliefs, vases, pots de fleurs,",
            Category.CLASS,
        ),
        Classification(
            "26700", "Taille, façonnage et finissage de pierres ornementales et de construction", Category.CLASS
        ),
        Classification(
            "2670001",
            "la taille, le façonnage et le finissage de la pierre destinée à la construction de bâtiments ou de routes, à la couverture de toitures, etc.",
            Category.CLASS,
        ),
        Classification(
            "2670002", "les opérations réalisées sur des pierres brutes fournies par les carriers", Category.CLASS
        ),
        Classification(
            "2670003",
            "la production de pierres tombales et de monuments funéraires y compris éventuellement leur pose",
            Category.CLASS,
        ),
        Classification("26810", "Fabrication de produits abrasifs", Category.CLASS),
        Classification("2681001", "la production de meules et de pierres à aiguiser ou à polir", Category.CLASS),
        Classification(
            "2681002",
            "la production d'abrasifs naturels ou artificiels, y compris ceux appliqués sur support souple",
            Category.CLASS,
        ),
        Classification("26820", "Fabrication de produits minéraux non métalliques n.d.a.", Category.CLASS),
        Classification(
            "2682001",
            "la fabrication de fils, de tissus, de feutres et d'articles divers (e.a. vêtements) en fibres d'amiante ou en matière minérales non métalliques similaires",
            Category.CLASS,
        ),
        Classification(
            "2682002",
            "la fabrication de garnitures de friction et de pièces non montées pour ces garnitures, à base de substances minérales ou de cellulose",
            Category.CLASS,
        ),
        Classification(
            "2682003",
            "la fabrication de matières minérales isolantes: laines de laitier,scories,roche et laines minérales similaires; vermiculite et argiles expansées et matières minérales similaires pour isolants thermiqu",
            Category.CLASS,
        ),
        Classification("2682004", "la fabrication d'ouvrages en asphalte", Category.CLASS),
        Classification(
            "2682005",
            "la fabrication d'articles en substances minérales diverses: fabrication de mica travaillé et d'ouvrages en mica, en tourbe, en graphite (autres que les articles électriques) etc.",
            Category.CLASS,
        ),
        Classification("2682006", "la fabrication d'articles d'ornement en onyx, albâtre, etc.", Category.CLASS),
        Classification("2682007", "la fabrication de corindon artificiel", Category.CLASS),
        Classification("27100", "Sidérurgie", Category.CLASS),
        Classification("27101", "Sidérurgie et fabrication de ferro-alliages (CECA)", Category.CLASS),
        Classification("2710101", "PROD.FONTE DE FONDERIE, FONTE PR FAB ACIER", Category.CLASS),
        Classification("2710102", "PRODUC. DE PROD. FERREUX PAR RéDUCTION", Category.CLASS),
        Classification("2710103", "PROD. ACIER DE CONVERTISSEURS, FOURS éLEC.", Category.CLASS),
        Classification("2710104", "PRODUC. DE GAZ DE HAUTS FOURNEAUX", Category.CLASS),
        Classification("27102", "Sidérurgie et fabrication de ferro-alliages (CECA)", Category.CLASS),
        Classification("2710201", "PROD. FEROMN CARBURé & DE FONTE SPIEGEL", Category.CLASS),
        Classification("27103", "Sidérurgie et fabrication de ferro-alliages (CECA)", Category.CLASS),
        Classification("2710301", "PROD. LINGOTS/AUTRS FORM.PRIM. ET DEM-PROD", Category.CLASS),
        Classification("2710302", "PRODUC. &/ REVêTEM. A CHAUD", Category.CLASS),
        Classification("2710303", "PRODUC. &/ REVêTEM. A FROID", Category.CLASS),
        Classification("2710304", "PROD.FE-BLANC,TôLES EN FE CHRMé, FE-NOIR", Category.CLASS),
        Classification("2710305", "PRODUC. DE FIL MACHINE EN ACIER", Category.CLASS),
        Classification("2710306", "PROD.PROFILéS LOURDS, LéGERS, A CHAUD", Category.CLASS),
        Classification("2710307", "PROD. RAILS & MAT. PR VOIES FERR. A CHAUD", Category.CLASS),
        Classification("27104", "Sidérurgie et fabrication de ferro-alliages (CECA)", Category.CLASS),
        Classification("2710401", "PROD.PROD.LAMINéS à CHAUD/FROID,.", Category.CLASS),
        Classification("27210", "Fabrication de tubes en fonte", Category.CLASS),
        Classification(
            "2721001",
            "la fabrication de tubes en fonte moulée et de tubes en fonte ou en acier coulés par centrifugation",
            Category.CLASS,
        ),
        Classification(
            "2721002",
            "la fabrication, par moulage, d'accessoires en fonte malléable ou non et en acier dont la jonction s'effectue par vissage pour les accessoires filetés ou par emmanchement ou par boulonnage pour les acc",
            Category.CLASS,
        ),
        Classification("27220", "Fabrication de tubes en acier", Category.CLASS),
        Classification(
            "2722001",
            "la fabrication de tubes sans soudure par laminage, filage ou étirage à chaud, ou par étirage ou laminage à froid",
            Category.CLASS,
        ),
        Classification(
            "2722002",
            "la fabrication de tubes soudés par formage et soudage à froid ou à chaud, par formage et étirage à froid ou par formage et réduction à chaud",
            Category.CLASS,
        ),
        Classification(
            "2722003",
            "la fabrication d'accessoires de tuyauterie en acier : .  brides plates ou à collerette forgée en acier .  raccords à souder bout à bout en acier .  raccords filetés et autres accessoires en acier",
            Category.CLASS,
        ),
        Classification("2725003", "(null)", Category.CLASS),
        Classification("27310", "Étirage à froid", Category.CLASS),
        Classification(
            "2731001",
            "la fabrication de barres ou de profilés en acier par étirage à froid, rectification ou écroûtage",
            Category.CLASS,
        ),
        Classification("27320", "Laminage à froid de feuillards", Category.CLASS),
        Classification(
            "2732001",
            "la fabrication de produits laminés plats en acier, nus ou revêtus, enroulés ou non, d'une largeur n'excédant pas 500 mm (non CECA), obtenus par relaminage à froid de produits plats laminés à chaud",
            Category.CLASS,
        ),
        Classification("27330", "Profilage à froid par formage ou pliage", Category.CLASS),
        Classification(
            "2733001",
            "la fabrication de profilés ouverts par déformation progressive sur machines à galets ou sur presse plieuse de produits laminés plats en acier",
            Category.CLASS,
        ),
        Classification("27340", "Tréfilage à froid", Category.CLASS),
        Classification("2734001", "la fabrication de fils d'acier par tréfilage ou étirage à froid", Category.CLASS),
        Classification(
            "27350",
            "Autres activités de première transformation; fabrication de ferro-alliages non CECA",
            Category.CLASS,
        ),
        Classification("2735001", "la production de ferro-alliages non CECA", Category.CLASS),
        Classification("2735002", "la production de grenailles et de poudres de fer pour le sablage", Category.CLASS),
        Classification(
            "2735003",
            "de productie van bijzonder zuiver ijzer door elektrolyse of andere chemische procédés",
            Category.CLASS,
        ),
        Classification("2735004", "la production de matériel fixe pour voies ferrées", Category.CLASS),
        Classification("27410", "Production de métaux précieux", Category.CLASS),
        Classification(
            "2741001",
            "la production et l'affinage des métaux précieux bruts: or, argent, platine, irridium, etc.",
            Category.CLASS,
        ),
        Classification("2741002", "la remise au titre des métaux précieux recyclés", Category.CLASS),
        Classification("2741003", "la production d'alliages de métaux précieux", Category.CLASS),
        Classification("2741004", "la production de demi-produits en métaux précieux", Category.CLASS),
        Classification("2741005", "la production de plaqués et de doublés d'argent sur métaux communs", Category.CLASS),
        Classification(
            "2741006", "la production de plaqués et doublés d'or sur métaux communs ou sur argent", Category.CLASS
        ),
        Classification(
            "2741007",
            "la production de plaqués et doublés de platine et de métaux du groupe du platine, sur or, argent ou métaux communs",
            Category.CLASS,
        ),
        Classification("27421", "Production d'aluminium", Category.CLASS),
        Classification("2742101", "la production d'oxyde d'aluminium (alumine)", Category.CLASS),
        Classification("2742102", "la production d'aluminium à partir d'alumine", Category.CLASS),
        Classification(
            "2742103", "la production par affinage électrolytique de déchets et débris d'aluminium", Category.CLASS
        ),
        Classification("2742104", "la production d'alliages d'aluminium", Category.CLASS),
        Classification("27422", "Première transformation d'aluminium", Category.CLASS),
        Classification("2742201", "la fabrication de demi-produits en aluminium", Category.CLASS),
        Classification(
            "2742202",
            "la fabrication de tôles, feuilles minces, barres, fils, profilés,..., en aluminium",
            Category.CLASS,
        ),
        Classification("2742203", "la fabrication de feuilles en aluminium pour emballage", Category.CLASS),
        Classification("27431", "Production de plomb, de zinc et d'étain", Category.CLASS),
        Classification(
            "2743101",
            "la production de plomb, de zinc ou d'étain à partir de minerais ou par affinage électrolytique de déchets et débris de plomb, de zinc ou d'étain",
            Category.CLASS,
        ),
        Classification("2743102", "la production d'alliages de plomb, de zinc ou d'étain", Category.CLASS),
        Classification("27432", "Première transformation du plomb, du zinc et de l'étain", Category.CLASS),
        Classification("2743201", "la fabrication de demi-produits en plomb,en zinc ou en étain", Category.CLASS),
        Classification(
            "2743202",
            "la fabrication de tôles, feuilles minces, barres, fils, profilés, ..., en plomb, en zinc ou en étain",
            Category.CLASS,
        ),
        Classification("27441", "Production de cuivre", Category.CLASS),
        Classification(
            "2744101",
            "la production de cuivre à partir de minerai ou par affinage électrolytique de déchets et débris de cuivre",
            Category.CLASS,
        ),
        Classification("2744102", "la production d'alliages de cuivre", Category.CLASS),
        Classification("2744103", "la production de mattes de cuivre", Category.CLASS),
        Classification("27442", "Première transformation du cuivre", Category.CLASS),
        Classification("2744201", "la production de demi-produits en cuivre", Category.CLASS),
        Classification(
            "2744202", "la production de tôles, feuilles minces, barres, fils, profilés,..., en cuivre", Category.CLASS
        ),
        Classification("2744203", "la fabrication de fils ou de lames fusibles", Category.CLASS),
        Classification("2744204", "la production de tuyaux en cuivre", Category.CLASS),
        Classification("27451", "Production d'autres métaux non ferreux", Category.CLASS),
        Classification(
            "2745101",
            "la production de chrome, de manganèse, de nickel,..., à partir de minerais ou d'oxydes",
            Category.CLASS,
        ),
        Classification(
            "2745102",
            "la production de chrome, de manganèse, de nickel, ..., par affinage électrolytique et aluminothermique de déchets et débris de chrome, de manganèse, de nickel, etc.",
            Category.CLASS,
        ),
        Classification("2745103", "la production d'alliages de chrome, de manganèse, de nickel, etc.", Category.CLASS),
        Classification("2745104", "la production de mattes de nickel", Category.CLASS),
        Classification("27452", "Première transformation d'autres métaux non ferreux", Category.CLASS),
        Classification(
            "2745201", "la fabrication de demi-produits en chrome, en manganèse, en nickel, etc.", Category.CLASS
        ),
        Classification(
            "2745202",
            "la production de tôles, feuilles minces, barres, fils, profilés,..., en chrome, en manganèse, en nickel, etc.",
            Category.CLASS,
        ),
        Classification("27500", "Fonderie", Category.CLASS),
        Classification("2750001", "FAB. DE DEMI-PRODUITS / PIèCES. DVRS", Category.CLASS),
        Classification("27510", "Fonderie de fonte", Category.CLASS),
        Classification("2751001", "la fonderie de produits finis ou de demi-produits en fonte", Category.CLASS),
        Classification("2751002", "la fonderie de pièces en fonte grise", Category.CLASS),
        Classification("2751003", "la fonderie de pièces en fonte à graphite sphéroïdal", Category.CLASS),
        Classification("2751004", "la fonderie de produits en fonte malléable", Category.CLASS),
        Classification("27520", "Fonderie d'acier", Category.CLASS),
        Classification("2752001", "la fonderie de produits finis ou de demi-produits en acier", Category.CLASS),
        Classification("2752002", "la fonderie de pièces en acier", Category.CLASS),
        Classification("27530", "Fonderie de métaux légers", Category.CLASS),
        Classification(
            "2753001",
            "la fonderie de produits finis ou de demi-produits en métaux légers (aluminium, magnésium, titane, béryllium, scandium, yttrium)",
            Category.CLASS,
        ),
        Classification("2753002", "la fonderie de pièces en métaux légers", Category.CLASS),
        Classification("27540", "Fonderie d'autres métaux non ferreux", Category.CLASS),
        Classification("2754001", "la fonderie de pièces en métaux lourds", Category.CLASS),
        Classification("2754002", "la fonderie de pièces en métaux précieux", Category.CLASS),
        Classification("28110", "Fabrication de constructions métalliques et de leurs parties", Category.CLASS),
        Classification(
            "2811001",
            "la fabrication et le montage de constructions métalliques et d'ossatures pour la construction",
            Category.CLASS,
        ),
        Classification(
            "2811002",
            "la fabrication d'ossatures métalliques pour équipements industriels (ossatures de hauts fourneaux, de matériels de manutention, etc.)",
            Category.CLASS,
        ),
        Classification(
            "2811003",
            "la fabrication de constructions préfabriquées principalement en métaux: baraques de chantier, éléments modulaires pour expositions, cabines téléphoniques, etc.",
            Category.CLASS,
        ),
        Classification("28120", "Fabrication de charpentes et menuiseries métalliques", Category.CLASS),
        Classification(
            "2812001",
            "la fabrication de menuiseries métalliques: portes et fenêtres avec chambranles, volets, cloisons mobiles,grilles, portes de garage, etc.",
            Category.CLASS,
        ),
        Classification("28210", "Fabrication de réservoirs, citernes et conteneurs métalliques", Category.CLASS),
        Classification(
            "2821001",
            "la fabrication et le montage de silos, de réservoirs, de citernes et de récipients similaires en métaux, d'une capacité supérieure à 300 litres",
            Category.CLASS,
        ),
        Classification(
            "2821002", "la fabrication de récipients métalliques pour gaz comprimés ou liquéfiés", Category.CLASS
        ),
        Classification("28220", "Fabrication de radiateurs et de chaudières pour le chauffage central", Category.CLASS),
        Classification(
            "2822001", "fabrication de radiateurs et de chaudières pour le chauffage central", Category.CLASS
        ),
        Classification("28300", "Fabrication de générateurs de vapeur", Category.CLASS),
        Classification(
            "2830001",
            "la fabrication de générateurs produisant de la vapeur d'eau ou d'autres types de vapeur",
            Category.CLASS,
        ),
        Classification(
            "2830002",
            "la fabrication d'appareils auxiliaires pour générateurs de vapeur:  condensateurs, économiseurs, surchauffeurs, collecteurs et accumulateurs de vapeur",
            Category.CLASS,
        ),
        Classification("2830003", "la fabrication de réacteurs nucléaires", Category.CLASS),
        Classification(
            "2830004",
            "la conception, la construction et l'installation de réseaux de tuyauterie, y compris le traitement complémentaire des tubes de manière à réaliser principalement des conduites ou des réseaux sous press",
            Category.CLASS,
        ),
        Classification("28401", "Forge", Category.CLASS),
        Classification("2840101", "la production pour des tiers de pièces forgées en métaux", Category.CLASS),
        Classification(
            "2840102",
            "la production et le montage de pièces forgées pour la construction: rampes d'escalier, balustrades, etc.",
            Category.CLASS,
        ),
        Classification("28402", "Emboutissage, estampage et profilage des métaux", Category.CLASS),
        Classification(
            "2840201", "la production pour des tiers de pièces matricées en métaux non ferreux", Category.CLASS
        ),
        Classification("28403", "Métallurgie des poudres", Category.CLASS),
        Classification(
            "2840301",
            "la production d'objets métalliques, directement à partir de poudres de métaux par traitement thermique (frittage) ou compression",
            Category.CLASS,
        ),
        Classification("28510", "Traitement et revêtement des métaux", Category.CLASS),
        Classification("2851001", "le placage, le traitement anodique, ..., des métaux", Category.CLASS),
        Classification("2851002", "le revêtement des métaux par électrolyse ou immersion", Category.CLASS),
        Classification("2851003", "le traitement thermique des métaux", Category.CLASS),
        Classification(
            "2851004",
            "l'ébarbage, le décapage au jet de sable, le dessablage au tonneau, le nettoyage des métaux",
            Category.CLASS,
        ),
        Classification("2851005", "la coloration, la gravure, l'impression des métaux", Category.CLASS),
        Classification(
            "2851006", "le revêtement non métallique des métaux: plastifiage, émaillage, laquage, etc.", Category.CLASS
        ),
        Classification("2851007", "le durcissement et le bufflage des métaux", Category.CLASS),
        Classification("28520", "Opérations de mécanique générale", Category.CLASS),
        Classification(
            "2852001",
            "la fabrication pour des tiers de pièces métalliques par application de techniques diverses: perçage, tournage, fraisage, arasage, rabotage, rodage, brochage, dressage, sciage, meulage, affûtage, souda",
            Category.CLASS,
        ),
        Classification("2852002", "travaux d'entretien et réparations mécaniques pour des tiers", Category.CLASS),
        Classification("2852003", "les activités des maréchaux-ferrants", Category.CLASS),
        Classification("28610", "Fabrication de coutellerie", Category.CLASS),
        Classification(
            "2861001",
            "la fabrication de coutellerie domestique: couteaux, fourchettes, cuillères, etc.",
            Category.CLASS,
        ),
        Classification(
            "2861002",
            "la fabrication de divers autres instruments tranchants: rasoirs et lames pour rasoirs, ciseaux, tondeuses à cheveux, etc.",
            Category.CLASS,
        ),
        Classification("28620", "Fabrication d'outillage", Category.CLASS),
        Classification(
            "2862001",
            "la fabrication d'outils à main tels que pinces, tournevis, clés, sécateurs, truelles, lampes à souder, etc.",
            Category.CLASS,
        ),
        Classification(
            "2862002",
            "la fabrication de couteaux et de lames tranchantes pour machines ou pour appareils mécaniques",
            Category.CLASS,
        ),
        Classification(
            "2862003",
            "la fabrication de scies et de lames de scies, y compris les lames de scies circulaires et de scies à chaîne",
            Category.CLASS,
        ),
        Classification(
            "2862004",
            "la fabrication d'outils interchangeables pour outillage à main, mécaniques ou non,ou pour machines-outils: forets, poinçons, matrices, fraises, etc.",
            Category.CLASS,
        ),
        Classification("2862005", "la fabrication d'outils de forgeron: forges, enclumes, etc.", Category.CLASS),
        Classification("2862006", "la fabrication d'étaux et de serre-joints", Category.CLASS),
        Classification("28630", "Fabrication de serrures et de ferrures", Category.CLASS),
        Classification(
            "2863001",
            "la fabrication de serrures, de cadenas, de verrous, de clés et d'articles similaires de serrurerie pour le bâtiment, l'ameublement, les véhicules,etc.",
            Category.CLASS,
        ),
        Classification("2863002", "la fabrication de charnières, de gonds, de paumelles,etc.", Category.CLASS),
        Classification("28710", "Fabrication de fûts et emballages similaires en métaux", Category.CLASS),
        Classification(
            "2871001", "la fabrication de récipients métalliques d'une capacité inférieure à 300 litres", Category.CLASS
        ),
        Classification(
            "2871002", "la fabrication de seaux, de cruches, de bidons, de tonneaux, ..., en métaux", Category.CLASS
        ),
        Classification("28720", "Fabrication d'emballages légers en métal", Category.CLASS),
        Classification(
            "2872001", "la fabrication de boîtes pour conserves alimentaires et pour boissons", Category.CLASS
        ),
        Classification("2872002", "la fabrication de tubes et d'étuis souples", Category.CLASS),
        Classification(
            "2872003", "la fabrication d'articles métalliques de bouchage et de surbouchage", Category.CLASS
        ),
        Classification("28730", "Fabrication d'articles en fils métalliques", Category.CLASS),
        Classification(
            "2873001",
            "la fabrication de câbles métalliques, de tresses métalliques et d'articles similaires",
            Category.CLASS,
        ),
        Classification("2873002", "la fabrication d'élingues de chargement", Category.CLASS),
        Classification(
            "2873003",
            "la fabrication d'articles en fils métalliques:ronces artificielles, clôtures, grillages, treillis, toiles métalliques, etc.",
            Category.CLASS,
        ),
        Classification("2873004", "la fabrication de clous, pointes, etc.", Category.CLASS),
        Classification("28741", "Fabrication de boulons, de vis et d'écrous", Category.CLASS),
        Classification(
            "2874101",
            "la fabrication d'articles de visserie: boulons, vis, écrous et autres produits similaires",
            Category.CLASS,
        ),
        Classification(
            "2874102",
            "la fabrication de rivets, de rondelles et d'autres produits non filetés similaires",
            Category.CLASS,
        ),
        Classification(
            "28742",
            "Fabrication de chaînes, à l'exception des chaînes pour la transmission de l'énergie",
            Category.CLASS,
        ),
        Classification("2874201", "fabrication de chaînes", Category.CLASS),
        Classification("28743", "Fabrication de ressorts", Category.CLASS),
        Classification(
            "2874301",
            "la fabrication de ressorts: ressorts à lames, ressorts hélicoïdaux, barres de torsion",
            Category.CLASS,
        ),
        Classification("2874302", "la fabrication de lames de ressorts", Category.CLASS),
        Classification("28751", "Fabrication d'articles de ménage", Category.CLASS),
        Classification(
            "2875101",
            "la fabrication de casseroles émaillées ou non, poêles à frire et autres ustensiles non électriques pour la table et la cuisine",
            Category.CLASS,
        ),
        Classification("2875102", "la fabrication de vaisselle plate en métaux communs", Category.CLASS),
        Classification("2875103", "la fabrication de petits appareils et accessoires de cuisine", Category.CLASS),
        Classification("2875104", "la fabrication de pailles de fer et laines d'acier", Category.CLASS),
        Classification("28752", "Fabrication d'articles sanitaires", Category.CLASS),
        Classification(
            "2875201",
            "la fabrication de baignoires, d'éviers, de bassines et d'articles similaires en métaux communs, émaillés ou non",
            Category.CLASS,
        ),
        Classification("28753", "Fabrication de coffres-forts", Category.CLASS),
        Classification(
            "2875301",
            "la fabrication de coffres-forts, de compartiments pour chambres fortes, de portes blindées, etc.",
            Category.CLASS,
        ),
        Classification("28754", "Fabrication de petits articles métalliques", Category.CLASS),
        Classification(
            "2875401",
            "la fabrication de petits articles divers en métaux communs: aiguilles, épingles, fermoirs, boucles, crochets, rivets creux, etc.",
            Category.CLASS,
        ),
        Classification(
            "2875402",
            "la fabrication de petits articles métalliques pour le bureau: agrafes, trombones, etc.",
            Category.CLASS,
        ),
        Classification("28755", "Fabrication d'autres articles métalliques, n.d.a.", Category.CLASS),
        Classification("2875501", "la fabrication de sabres, d'épées, de baïonnettes, etc.", Category.CLASS),
        Classification("2875502", "la fabrication de coiffures de sécurité en métaux", Category.CLASS),
        Classification(
            "2875503", "la fabrication de panneaux indicateurs et de panneaux de signalisation", Category.CLASS
        ),
        Classification(
            "2875504", "la fabrication d'éléments de couverture en métal:gouttières, faîtages, etc.", Category.CLASS
        ),
        Classification("2875505", "la fabrication d'échelles et escabeaux métalliques", Category.CLASS),
        Classification("2875506", "la fabrication de boîtes aux lettres", Category.CLASS),
        Classification("2875507", "la fabrication d'ancres et d'hélices de bateaux", Category.CLASS),
        Classification("2875508", "la fabrication à l'échelle industrielle de fers à cheval", Category.CLASS),
        Classification(
            "29110",
            "Fabrication de moteurs et turbines, à l'exclusion des moteurs pour avions et véhicules à moteur",
            Category.CLASS,
        ),
        Classification(
            "2911001",
            "la fabrication de moteurs à combustion interne et de leurs parties pour usages divers: pour véhicules ferroviaires, pour machines agricoles ou engins de génie civil, pour navires et bateaux (y compris",
            Category.CLASS,
        ),
        Classification(
            "2911002",
            "la fabrication de soupapes d'admission et d'échappement pour moteurs à combustion interne",
            Category.CLASS,
        ),
        Classification(
            "2911003",
            "la fabrication de turbines et de leurs parties: turbines produisant de la vapeur d'eau ou d'autres types de vapeur, turbines à gaz, turbines hydrauliques, roues hydrauliques et leurs régulateurs",
            Category.CLASS,
        ),
        Classification("29120", "Fabrication de pompes et compresseurs", Category.CLASS),
        Classification(
            "2912001",
            "la fabrication de pompes à air ou à vide et de compresseurs d'air ou d'autres gaz",
            Category.CLASS,
        ),
        Classification(
            "2912002", "la fabrication de pompes pour liquides, même comportant un dispositif mesureur", Category.CLASS
        ),
        Classification("2912003", "la fabrication de pompes à béton", Category.CLASS),
        Classification("2912004", "la fabrication de moteurs hydrauliques, pneumatiques et éoliens", Category.CLASS),
        Classification("29130", "Fabrication d'articles de robinetterie", Category.CLASS),
        Classification(
            "2913001",
            "la fabrication de robinetterie et de vannes industrielles, y compris les vannes de régulation et la robinetterie d'adduction",
            Category.CLASS,
        ),
        Classification("2913002", "la fabrication de robinetterie sanitaire", Category.CLASS),
        Classification("2913003", "la fabrication de robinetterie pour le chauffage", Category.CLASS),
        Classification(
            "29141", "Fabrication de roulements à billes, de paliers à roulements et similaires", Category.CLASS
        ),
        Classification(
            "2914101",
            "la fabrication de roulements à billes, à galets, à rouleaux ou à aiguilles et de leurs parties",
            Category.CLASS,
        ),
        Classification("29142", "Fabrication d'organes mécaniques de transmission de l'énergie", Category.CLASS),
        Classification(
            "2914201",
            "la fabrication d'organes mécaniques de transmission de l'énergie: arbres de transmission, arbres à cames, vilebrequins, etc., manivelles, paliers et coussinets",
            Category.CLASS,
        ),
        Classification(
            "2914202",
            "la fabrication d'engrenages et de roues de friction ainsi que de réducteurs, de multiplicateurs et de variateurs de vitesse",
            Category.CLASS,
        ),
        Classification("2914203", "la fabrication d'embrayages et d'organes d'accouplement", Category.CLASS),
        Classification("2914204", "la fabrication de volants et de poulies", Category.CLASS),
        Classification("2914205", "la fabrication de chaînes à maillons articulés", Category.CLASS),
        Classification("2914206", "la fabrication d'organes hydrauliques de transmission", Category.CLASS),
        Classification(
            "29210",
            "Fabrication de fours et brûleurs industriels, y compris les fours et les brûleurs électriques",
            Category.CLASS,
        ),
        Classification(
            "2921001",
            "la fabrication et le montage de fours électriques et autres fours industriels, de fours de laboratoires et d'incinérateurs",
            Category.CLASS,
        ),
        Classification(
            "2921002",
            "la fabrication de brûleurs, y compris les brûleurs pour chaudières de chauffage central",
            Category.CLASS,
        ),
        Classification(
            "2921003",
            "la fabrication de foyers automatiques, d'avant-foyers, de grilles mécaniques,de dispositifs pour l'évacuation des cendres, etc.",
            Category.CLASS,
        ),
        Classification("29220", "Fabrication de matériel de levage et de manutention", Category.CLASS),
        Classification("2922001", "la fabrication de palans, treuils et cabestans, crics et vérins", Category.CLASS),
        Classification(
            "2922002",
            "la fabrication de bigues, grues, portiques et grues mobiles, chariots-cavaliers, etc.",
            Category.CLASS,
        ),
        Classification(
            "2922003",
            "la fabrication de chariots, même automobiles, munis ou non d'un dispositif de levage ou de manutention, des types utilisés dans les usines",
            Category.CLASS,
        ),
        Classification(
            "2922004",
            "la fabrication de manipulateurs mécaniques et robots industriels spécialement conçus pour des opérations de levage, de manutention, de chargement ou de déchargement",
            Category.CLASS,
        ),
        Classification(
            "2922005",
            "la fabrication d'appareils transporteurs ou convoyeurs, de téléphériques, d'élévateurs à liquides, etc.",
            Category.CLASS,
        ),
        Classification(
            "2922006",
            "la fabrication, l'entretien et la réparation d'ascenseurs, d'escaliers mécaniques et de trottoirs roulants",
            Category.CLASS,
        ),
        Classification("29230", "Fabrication d'équipements aérauliques et frigorifiques industriels", Category.CLASS),
        Classification(
            "2923001",
            "la fabrication et l'installation d'équipements industriels pour la production du froid",
            Category.CLASS,
        ),
        Classification("2923002", "la fabrication de comptoirs frigo", Category.CLASS),
        Classification(
            "2923003", "la fabrication de machines et appareils pour le conditionnement de l'air", Category.CLASS
        ),
        Classification("2923004", "la fabrication d'échangeurs de chaleur", Category.CLASS),
        Classification("2923005", "la fabrication de ventilateurs à usage non domestique", Category.CLASS),
        Classification("29241", "Fabrication d'équipements d'emballage", Category.CLASS),
        Classification(
            "2924101",
            "la fabrication de machines et appareils à empaqueter ou emballer: machines et appareils à remplir, fermer, sceller, capsuler, étiqueter, etc.",
            Category.CLASS,
        ),
        Classification(
            "2924102",
            "la fabrication de machines et appareils servant à nettoyer ou à sécher les bouteilles ainsi que de machines et appareils à gazéifier les boissons",
            Category.CLASS,
        ),
        Classification(
            "2924103",
            "la fabrication de chaînes de conditionnement munies de dispositis de pesée ou de dosage",
            Category.CLASS,
        ),
        Classification("29242", "Fabrication d'appareils de pesage", Category.CLASS),
        Classification(
            "2924201",
            "la fabrication d'appareils et d'instruments de pesage: balances de ménage et de magasin, bascules, bascules à pesage continu, points bascules, poids pour balances, etc.",
            Category.CLASS,
        ),
        Classification("29243", "Fabrication d'appareils de projection, y compris les extincteurs", Category.CLASS),
        Classification(
            "2924301",
            "la fabrication d'appareils à projeter, disperser ou pulvériser des matières liquides ou en poudre: fabrication de pistolets aérographes, d'appareils à jet de vapeur, etc.",
            Category.CLASS,
        ),
        Classification("2924302", "la fabrication d'extincteurs", Category.CLASS),
        Classification("29244", "Fabrication de machines automatiques de vente de produits", Category.CLASS),
        Classification("2924401", "la fabrication de machines automatiques de vente de produits", Category.CLASS),
        Classification("29245", "Fabrication d'appareils de filtrage", Category.CLASS),
        Classification(
            "2924501",
            "la fabrication d'appareils pour la filtration ou l'épuration des liquides, de l'air ou d'autres gaz",
            Category.CLASS,
        ),
        Classification("2924502", "la fabrication de filtres à air ou à carburant pour moteurs", Category.CLASS),
        Classification(
            "29246",
            "Fabrication de nettoyeurs à haute pression, matériel industriel de nettoyage au sable et similaires",
            Category.CLASS,
        ),
        Classification(
            "2924601",
            "la fabrication de nettoyeurs à haute pression, matériel industriel de nettoyage au sable et similaires",
            Category.CLASS,
        ),
        Classification("29247", "Fabrication d'autres machines à usage général n.d.a.", Category.CLASS),
        Classification(
            "2924701",
            "la fabrication d'appareils de distillation ou de rectification pour les raffineries de pétrole, les industries chimiques ou pour les industries des boissons",
            Category.CLASS,
        ),
        Classification(
            "2924702",
            "la fabrication d'appareils et d'installations pour la liquéfaction d'air ou d'autres gaz",
            Category.CLASS,
        ),
        Classification("2924703", "la fabrication de générateurs de gaz", Category.CLASS),
        Classification("2924704", "la fabrication de centrifugeuses", Category.CLASS),
        Classification(
            "2924705",
            "la fabrication de joints d'étanchéité et de joints similaires composés de matériaux différents ou de plusieurs couches d'un même matériau",
            Category.CLASS,
        ),
        Classification(
            "2924706",
            "la fabrication de calandres et de laminoirs ainsi que de cylindres pour ces machines",
            Category.CLASS,
        ),
        Classification("29310", "Fabrication de tracteurs agricoles", Category.CLASS),
        Classification("2931001", "la fabrication de tracteurs agricoles et forestiers", Category.CLASS),
        Classification("2931002", "la fabrication de motoculteurs", Category.CLASS),
        Classification("29321", "Fabrication de machines agricoles et forestières", Category.CLASS),
        Classification("2932101", "la fabrication de faucheuses, y compris les tondeuses à gazon", Category.CLASS),
        Classification(
            "2932102",
            "la fabrication de remorques ou de semi-remorques autochargeuses ou autodéchargeuses, pour usages agricoles",
            Category.CLASS,
        ),
        Classification(
            "2932103",
            "la fabrication de machines, appareils et engins agricoles pour la préparation du sol, la plantation des cultures ou l'épandage des engrais: charrues, épandeurs de fumier, semoirs, herses, etc.",
            Category.CLASS,
        ),
        Classification(
            "2932104",
            "la fabrication de machines, appareils et engins pour la récolte de produits agricoles et horticoles: moissonneuses, arracheuses, batteuses, machines pour le triage, etc.",
            Category.CLASS,
        ),
        Classification(
            "2932105", "la fabrication de machines et appareils de pulvérisation pour l'agriculture", Category.CLASS
        ),
        Classification("2932106", "la fabrication de machines à traire", Category.CLASS),
        Classification(
            "2932107",
            "la fabrication d'autres machines et appareils pour l'agriculture: pour l'aviculture,l'apiculture,la préparation des aliments ou provendes pour animaux,etc.; machines pour nettoyage,triage,calibrage de",
            Category.CLASS,
        ),
        Classification("29322", "Réparation de matériel agricole", Category.CLASS),
        Classification(
            "2932201",
            "l'entretien et la réparation de tracteurs agricoles, de motoculteurs et de tondeuses à gazon",
            Category.CLASS,
        ),
        Classification(
            "2932202", "l'entretien et la réparation d'autres machines agricoles et forestières", Category.CLASS
        ),
        Classification("29401", "Fabrication de machines-outils à métaux", Category.CLASS),
        Classification(
            "2940101",
            "la fabrication de machines-outils travaillant par enlèvement de métal: tours, perceuses, aléseuses, fraiseuses, etc.",
            Category.CLASS,
        ),
        Classification(
            "2940102",
            "la fabrication de machines-outils travaillant sans enlèvement de métal: presses à forger ou à estamper, bancs à étirer, cisailles, etc.",
            Category.CLASS,
        ),
        Classification(
            "2940103",
            "la fabrication de machines-outils opérant sur métal et autres matières par des procédé spéciaux: laser, électroérosion, ultra-sons, etc.",
            Category.CLASS,
        ),
        Classification(
            "2940104",
            "la fabrication de porte-pièces, de porte-outils et de dispositifs spéciaux se montant sur machines-outils",
            Category.CLASS,
        ),
        Classification("29402", "Fabrication de matériel de soudage", Category.CLASS),
        Classification(
            "2940201",
            "la fabrication de matériel à main et de machines et appareils pour le soudage, le brasage, le coupage thermique,etc.",
            Category.CLASS,
        ),
        Classification("2940202", "la fabrication d'appareils de soudure automatisés", Category.CLASS),
        Classification("29403", "Fabrication de machines-outils pour le travail du bois", Category.CLASS),
        Classification(
            "2940301", "la fabrication de machines-outils à débiter, travailler ou profiler le bois", Category.CLASS
        ),
        Classification(
            "2940302", "la fabrication de presses à fabriquer les panneaux de bois ou de particules", Category.CLASS
        ),
        Classification("2940303", "la fabrication de machines à clouer, à agrafer, à coller, etc.", Category.CLASS),
        Classification(
            "29404", "Fabrication de machines-outils à moteur incorporé ou d'outils pneumatiques", Category.CLASS
        ),
        Classification(
            "2940401",
            "la fabrication de matériel à main et et de machines-outils à moteur incorporé: foreuses, perceuses, ponceuses, taillehaies, tronçonneuses à chaîne, etc.",
            Category.CLASS,
        ),
        Classification("2940402", "la fabrication d'outils pneumatiques", Category.CLASS),
        Classification("29405", "Fabrication d'autres machines-outils", Category.CLASS),
        Classification(
            "2940501",
            "la fabrication de machines à scier, cliver, polir ou meuler les pierres, le verre, la céramique et autres matières analogues",
            Category.CLASS,
        ),
        Classification("29410", "Fabrication de machines-outils à moteur incorporé ou pneumatiques", Category.CLASS),
        Classification("29420", "Fabrication de machines-outils pour le travail des métaux", Category.CLASS),
        Classification("29430", "Fabrication d'autres machines-outils n.d.a.", Category.CLASS),
        Classification("29431", "Fabrication de matériel de soudage", Category.CLASS),
        Classification("29432", "Fabrication de machines-outils pour le travail du bois", Category.CLASS),
        Classification("29433", "Fabrication d'autres machines-outils n.d.a.", Category.CLASS),
        Classification("29510", "Fabrication de machines pour la métallurgie", Category.CLASS),
        Classification(
            "2951001",
            "la fabrication de machines et appareils pour la manutention des métaux à haute température: convertisseurs, lingotières, poches de coulée, machines à couler (mouler)",
            Category.CLASS,
        ),
        Classification("2951002", "la fabrication de laminoirs et de leurs cylindres", Category.CLASS),
        Classification("29520", "Fabrication de machines pour l'extraction ou la construction", Category.CLASS),
        Classification(
            "2952001",
            "la fabrication d'appareils élévateurs, transporteurs ou convoyeurs à action continue pour fonds de mines ou autres travaux souterrains",
            Category.CLASS,
        ),
        Classification(
            "2952002",
            "la fabrication de machines de sondage, de haveuses, d'abatteuses, de machines de forage et de machines à creuser les tunnels ou les galeries",
            Category.CLASS,
        ),
        Classification(
            "2952003",
            "la fabrication de machines et appareils à traiter les minéraux par criblage, triage, séparation, etc.",
            Category.CLASS,
        ),
        Classification("2952004", "la fabrication de dragues", Category.CLASS),
        Classification("2952005", "la fabrication de machines à concasser ou à broyer le béton", Category.CLASS),
        Classification("2952006", "la fabrication de bétonnières et appareils à gâcher le ciment", Category.CLASS),
        Classification(
            "2952007",
            "la fabrication de machines et appareils de terrassement: bouteurs (bulldozers), bouteurs biais (angledozers), niveleuses,décapeuses (scrapers), pelles mécaniques, chargeuses, chargeuses-pelleteuses, e",
            Category.CLASS,
        ),
        Classification("2952008", "la fabrication de rouleaux-compresseurs", Category.CLASS),
        Classification(
            "2952009",
            "la fabrication de sonnettes de battage et de machines pour l'arrachage des pieux",
            Category.CLASS,
        ),
        Classification("2952010", "la fabrication d'épandeurs de béton et de bitume", Category.CLASS),
        Classification(
            "2952011", "la fabrication de machines et d'appareils mécaniques pour le surfaçage du béton", Category.CLASS
        ),
        Classification(
            "2952012",
            "la fabrication de lames de bouteurs (bulldozers) et de bouteurs biais (angledozers)",
            Category.CLASS,
        ),
        Classification("29530", "Fabrication de machines pour l'industrie agro-alimentaire", Category.CLASS),
        Classification("2953001", "la fabrication de séchoirs pour produits agricoles", Category.CLASS),
        Classification(
            "2953002",
            "la fabrication de machines et appareils de laiterie: écrémeuses; machines et appareils pour le traitement du lait; machines et appareils pour la transformation du lait; machines et appareils de fromag",
            Category.CLASS,
        ),
        Classification(
            "2953003",
            "la fabrication de machines et appareils pour la minoterie: tarares, toiles trieuses, nettoyeurs à cyclones, séparateurs pneumatiques, machines à brosser les grains et autres mach. simil.,moulins à meu",
            Category.CLASS,
        ),
        Classification(
            "2953004",
            "la fabrication de presses, pressoirs et fouloirs, utilisés pour la fabrication du vin, du cidre, des jus de fruits,etc.",
            Category.CLASS,
        ),
        Classification(
            "2953005",
            "la fabrication de machines et appareils pour la boulangerie, pâtisserie,biscuiterie ou la fabrication des pâtes aliment.: fours de boulangerie non électriques, malaxeurs, machines à trancher, à divise",
            Category.CLASS,
        ),
        Classification(
            "2953006",
            "la fabrication de machines et appareils pour la transformation de divers produits alimentaires: pour la confiserie, la fabrication du cacao, du chocolat, pour la sucrerie,la brasserie,la préparation d",
            Category.CLASS,
        ),
        Classification(
            "2953007",
            "la fabrication de machines et appareils pour l'extraction ou la préparation des huiles ou graisses animales ou végétales",
            Category.CLASS,
        ),
        Classification(
            "2953008",
            "la fabrication de machines et appareils pour la préparation du tabac et la fabrication de cigares, de cigarettes ou de tabac à pipe, à chiquer ou à priser",
            Category.CLASS,
        ),
        Classification(
            "2953009",
            "la fabrication de machines et appareils pour la préparation des aliments dans les hôtels, les restaurants, etc.",
            Category.CLASS,
        ),
        Classification(
            "29540",
            "Fabrication de machines pour les industries du textile, de l'habillement et du cuir",
            Category.CLASS,
        ),
        Classification(
            "2954001",
            "la fabrication de machines pour la préparation, la fabrication, le filage (extrusion), l'étirage, la texturation ou le tranchage des fibres, matières ou fils textiles,synthétiques ou artificiels",
            Category.CLASS,
        ),
        Classification(
            "2954002",
            "fabrication de machines pour la préparation des fibres textiles: égreneuses de coton,machines brise-balles,effilocheuses, batteurs-étaleurs à coton, machines à désuinter ou à carboniser la laine,peign",
            Category.CLASS,
        ),
        Classification("2954003", "la fabrication de métiers à filer", Category.CLASS),
        Classification(
            "2954004",
            "la fabrication de machines pour la préparation des fils textiles: bobinoirs, ourdissoirs et machines similaires",
            Category.CLASS,
        ),
        Classification("2954005", "la fabrication de machines à tisser, y compris les métiers à main", Category.CLASS),
        Classification("2954006", "la fabrication de machines et métiers à bonneterie", Category.CLASS),
        Classification(
            "2954007",
            "la fabrication de machines et métiers à filet, à tulle, à dentelle, à passementerie, etc.",
            Category.CLASS,
        ),
        Classification(
            "2954008",
            "#a fabrication de machines et appareils auxiliaires pour les machines de l'industrie textile: ratières, mécaniques Jacquard, casse-chaînes et casse-trames, mécanismes de changement de navettes, broche",
            Category.CLASS,
        ),
        Classification(
            "2954009",
            "la fabrication de machines et appareils pour le traitement des tissus: lavage,blanchîment,teinture,apprêt,finissage,enduction ou imprégnation des tissus en matière textile; machines à enrouler,déroule",
            Category.CLASS,
        ),
        Classification(
            "2954010",
            "la fabrication de machines et appareils de blanchisserie: machines à repasser, y compris les presses à fixer; machines à laver et à sécher le linge de types utilisés dans les blanchisseries; machines",
            Category.CLASS,
        ),
        Classification(
            "2954011",
            "la fabrication de machines à coudre (y compris les machines à coudre à usage domestique) ainsi que de têtes et d'aiguilles pour machines à coudre",
            Category.CLASS,
        ),
        Classification(
            "2954012",
            "la fabrication de machines et appareils pour la fabrication ou le finissage du feutre ou des non-tissés",
            Category.CLASS,
        ),
        Classification(
            "2954013",
            "la fabrication de machines et appareils pour l'industrie du cuir: machines et appareils pour la préparation, le tannage ou le travail des cuirs ou des peaux",
            Category.CLASS,
        ),
        Classification(
            "2954014",
            "machines et appareils pour la fabrication ou la réparation des chaussures et des autres ouvrages en cuir, en peau ou en pelleterie",
            Category.CLASS,
        ),
        Classification("29550", "Fabrication de machines pour les industries du papier et du carton", Category.CLASS),
        Classification(
            "2955001",
            "la fabrication de machines et de matériel pour la fabrication des pâtes à papier par des procédés mécaniques ou chimiques",
            Category.CLASS,
        ),
        Classification(
            "2955002",
            "la fabrication de machines et de matériel pour la fabrication du papier et du carton",
            Category.CLASS,
        ),
        Classification(
            "2955003",
            "la fabrication de machines et de matériel pour la fabrication d'articles en papier ou en carton",
            Category.CLASS,
        ),
        Classification("29561", "Fabrication de machines d'imprimerie", Category.CLASS),
        Classification(
            "2956101",
            "la fabrication de machines et de matériel pour l'imprimerie, le brochage et la reliure",
            Category.CLASS,
        ),
        Classification(
            "2956102", "la fabrication de machines pour la composition du texte ou de l'image", Category.CLASS
        ),
        Classification(
            "29562", "Fabrication de machines pour le travail du caoutchouc et des matières plastiques", Category.CLASS
        ),
        Classification(
            "2956201",
            "la fabrication de machines pour le travail du caoutchouc tendre ou des matières plastiques, ou pour la fabrication de produits en ces matières: extrudeuses, machines à mouler, machines à fabriquer ou",
            Category.CLASS,
        ),
        Classification("29563", "Fabrication de moules et modèles", Category.CLASS),
        Classification(
            "2956301",
            "la fabrication de châssis de fonderie pour tous matériaux, de plaques de fond pour moules, de modèles pour mouler, de moules",
            Category.CLASS,
        ),
        Classification("29564", "Fabrication d'autres machines pour industries spécifiques", Category.CLASS),
        Classification(
            "2956401",
            "la fabrication de machines et appareils pour la fabrication de tuiles, de briques, de pâtes céramiques formées, de tuyaux, d'électrodes de graphite, de craie à écrire et à dessiner",
            Category.CLASS,
        ),
        Classification(
            "2956402",
            "la fabrication de machines pour l'assemblage de lampes, tubes ou valves électriques ou électroniques",
            Category.CLASS,
        ),
        Classification(
            "2956403",
            "la fabrication de machines pour la fabrication ou le travail à chaud du verre ou des ouvrages en verre, des fibres et des fils de verre",
            Category.CLASS,
        ),
        Classification(
            "2956404",
            "la fabrication d'appareils à sècher le bois, la pâte à papier, le papier ou le carton.",
            Category.CLASS,
        ),
        Classification(
            "2956405", "la fabrication de machines et appareils pour la séparation isotopique", Category.CLASS
        ),
        Classification("2956406", "la fabrication de machines pour le traitement des déchets", Category.CLASS),
        Classification("2956407", "la fabrication de machines de corderie", Category.CLASS),
        Classification("2956408", "la fabrication de robots industriels à usage divers, etc.", Category.CLASS),
        Classification("29601", "Fabrication d'armes lourdes et d'armes de guerre", Category.CLASS),
        Classification("2960101", "la fabrication de chars et autres véhicules de combat", Category.CLASS),
        Classification("2960102", "la fabrication de matériel d'artillerie et de missiles balistiques", Category.CLASS),
        Classification("2960103", "la fabrication d'armes de guerre légères", Category.CLASS),
        Classification("2960104", "la fabrication de munitions de guerre", Category.CLASS),
        Classification(
            "2960105", "la fabrication d'engins explosifs tels que bombes, mines et torpilles", Category.CLASS
        ),
        Classification("29602", "Fabrication d'armes légères et d'armes de sport", Category.CLASS),
        Classification(
            "2960201",
            "la fabrication d'armes de chasse, de tir sportif et de défense ainsi que de leurs munitions",
            Category.CLASS,
        ),
        Classification("29710", "Fabrication d'appareils électroménagers", Category.CLASS),
        Classification(
            "2971001",
            "la fabrication de réfrigérateurs et congélateurs-conservateurs, machines à laver la vaisselle, machines à laver et à sécher le linge",
            Category.CLASS,
        ),
        Classification("2971002", "la fabrication d'aspirateurs de poussières et cireuses à parquets", Category.CLASS),
        Classification(
            "2971003",
            "la fabrication de broyeurs pour déchets, broyeurs et mélangeurs pour aliments, presse-fruits et presse-légumes, ouvre-boîtes et appareils à aiguiser les couteaux",
            Category.CLASS,
        ),
        Classification(
            "2971004", "la fabrication de rasoirs électriques, brosses à dents électriques, etc.", Category.CLASS
        ),
        Classification("2971005", "la fabrication de hottes aspirantes ou à recyclage", Category.CLASS),
        Classification(
            "2971006",
            "la fabrication d'appareils électrothermiques: chauffe-eau, couvertures chauffantes, appareils pour le chauffage des locaux et ventilateurs de type ménager, fers à repasser, à usage domestique",
            Category.CLASS,
        ),
        Classification(
            "2971007", "la fabrication de sèche-cheveux, peignes, brosses et appareils à friser", Category.CLASS
        ),
        Classification(
            "2971008",
            "la fabrication de fours, fours à micro-ondes, cuisinières, chauffe-plats, grille-pain, appareils pour la préparation du café et du thé, poêles à frire, rôtissoires, grils, résistances chauffantes, etc",
            Category.CLASS,
        ),
        Classification("29720", "Fabrication d'appareils ménagers non électriques", Category.CLASS),
        Classification(
            "2972001",
            "la fabrication d'appareils pour le chauffage des locaux, cuisinières, grils, poêles, chauffe-eau à gaz, ustensiles de cuisine et chauffe-plats, non électriques",
            Category.CLASS,
        ),
        Classification(
            "2972002", "la fabrication de récupérateurs de chaleur solaire non photovoltaïques", Category.CLASS
        ),
        Classification("30010", "Fabrication de machines de bureau", Category.CLASS),
        Classification("3001001", "la fabrication de machines à écrire électriques ou manuelles", Category.CLASS),
        Classification(
            "3001002",
            "la fabrication de matériel de photocopie, de duplicateurs hectographiques ou à stencils et de machines à imprimer offset alimentées en feuilles (offset de bureau)",
            Category.CLASS,
        ),
        Classification(
            "3001003",
            "la fabrication de machines à calculer, de caisses enregistreuses, de machines à affranchir, de terminaux spécialisés pour l'édition de billets ou la réservation de places, etc.",
            Category.CLASS,
        ),
        Classification(
            "3001004",
            "la fabrication d'autres machines et appareils de bureau: machines à imprimer les adresses, à trier, compter ou encartoucher la monnaie,distributeurs de billets,machines pour le triage et la mise sous",
            Category.CLASS,
        ),
        Classification("30020", "Fabrication d'ordinateurs et d'autres équipements informatiques", Category.CLASS),
        Classification(
            "3002001",
            "la fabrication de machines automatiques de traitement de l'information, y compris les micro-ordinateurs et les machines pour le traitement des textes: unités centrales, interfaces, consoles, machines",
            Category.CLASS,
        ),
        Classification(
            "3002002",
            "la fabrication d'unités périphériques: imprimantes, terminaux, etc.; lecteurs magnétiques ou optiques, machines de mise d'informations sur support sous forme codée",
            Category.CLASS,
        ),
        Classification("3002003", "l'isolation intérieure des boîtiers d'ordinateurs", Category.CLASS),
        Classification("31100", "Fabrication de moteurs, génératrices et transformateurs électriques", Category.CLASS),
        Classification("3110001", "la fabrication de moteurs à courant alternatif", Category.CLASS),
        Classification("3110002", "la fabrication de machines génératrices à courant alternatif", Category.CLASS),
        Classification(
            "3110003", "la fabrication de moteurs universels (courant alternatif/ courant continu)", Category.CLASS
        ),
        Classification(
            "3110004", "la fabrication de moteurs ou de machines génératrices à courant continu", Category.CLASS
        ),
        Classification(
            "3110005",
            "la fabrication de groupes électrogènes à courant alternatif ou à courant continu",
            Category.CLASS,
        ),
        Classification("3110006", "la fabrication de convertisseurs électriques rotatifs ou statiques", Category.CLASS),
        Classification("3110007", "la fabrication de transformateurs électriques", Category.CLASS),
        Classification("3110008", "le rebobinage d'électromoteurs et de transformateurs", Category.CLASS),
        Classification(
            "3110009", "la fabrication de panneaux électriques pour la récupération de chaleur solaire", Category.CLASS
        ),
        Classification("31200", "Fabrication de matériel de distribution et de commande électrique", Category.CLASS),
        Classification(
            "3120001",
            "la fabrication d'appareillages pour la coupure,le sectionment,la protection,le branchement,le raccordement ou la connexion des circuits électriques: interrupteurs,commutateurs, coupe-circuits,parafoud",
            Category.CLASS,
        ),
        Classification(
            "3120002",
            "la fabrication de tableaux, panneaux, consoles,pupitres, d'armoires et d'autres supports pour la commande ou la distribution électrique",
            Category.CLASS,
        ),
        Classification("31300", "Fabrication de fils et câbles isolés", Category.CLASS),
        Classification(
            "3130001",
            "la fabrication de fils, de câbles, de bandes et d'autres conducteurs isolés, munis ou non de pièces de connexion",
            Category.CLASS,
        ),
        Classification(
            "3130002",
            "la fabrication de câbles de fibres optiques pour la transmision de données codées: télécommunication, vidéo, données informatiques, surveillance, etc.",
            Category.CLASS,
        ),
        Classification("31400", "Fabrication d'accumulateurs et de piles électriques", Category.CLASS),
        Classification(
            "3140001",
            "la fabrication de piles et de batteries de piles électriques, y compris les batteries pour véhicules à moteur",
            Category.CLASS,
        ),
        Classification(
            "3140002", "la fabrication d'accumulateurs électriques et de parties de ces appareils", Category.CLASS
        ),
        Classification("31501", "Fabrication de lampes", Category.CLASS),
        Classification(
            "3150101", "la fabrication de lampes et de tubes électriques à incandescence ou à décharge", Category.CLASS
        ),
        Classification("3150102", "la fabrication de lampes à arc", Category.CLASS),
        Classification(
            "3150103", "la fabrication de lampes et de tubes à rayons ultra-violets ou infra-rouges", Category.CLASS
        ),
        Classification(
            "3150104", "la fabrication de lampes-éclair et de cubes-éclair pour la photographie", Category.CLASS
        ),
        Classification("31502", "Fabrication d'appareils d'éclairage", Category.CLASS),
        Classification(
            "3150201",
            "la fabrication de lustres, de lampes de bureau, de lampes de chevet ou de lampadaires d'intérieur, même non électriques",
            Category.CLASS,
        ),
        Classification("3150202", "la fabrication de lampes électriques portatives", Category.CLASS),
        Classification(
            "3150203",
            "la fabrication de lampes-réclames, d'enseignes lumineuses, de plaques indicatrices lumineuses, etc.",
            Category.CLASS,
        ),
        Classification("3150204", "la fabrication de projecteurs", Category.CLASS),
        Classification(
            "3150205",
            "la fabrication d'appareils d'éclairage extérieur et d'éclairage des voies publiques",
            Category.CLASS,
        ),
        Classification(
            "3150206",
            "la fabrication de guirlandes électriques de types utilisés pour la décoration des arbres de Noël",
            Category.CLASS,
        ),
        Classification("3150207", "la fabrication d'appareils d'éclairage non électriques", Category.CLASS),
        Classification("31610", "Fabrication de matériels électriques pour moteurs et véhicules", Category.CLASS),
        Classification(
            "3161001",
            "la fabrication d'appareils et de dispositifs électriques d'allumage ou de démarrage pour moteurs à combustion interne: magnétos, dynamos-magnétos, bobines d'allumage, bougies, démarreurs, génératrices",
            Category.CLASS,
        ),
        Classification(
            "3161002",
            "la fabrication d'appareils électriques d'éclairage ou de signalisation acoustique ou visuelle pour les cycles, les motocycles ou les automobiles: phares, feux tournants, avertisseurs sonores, sirènes,",
            Category.CLASS,
        ),
        Classification("3161003", "la fabrication de jeux de fils", Category.CLASS),
        Classification(
            "3161004",
            "la fabrication d'essuie-glaces, de dégivreurs et de dispositifs électriques anti-buée, etc.",
            Category.CLASS,
        ),
        Classification("3161005", "la fabrication de dynamos et d'appareils d'éclairage pour cycles", Category.CLASS),
        Classification("31621", "Fabrication d'appareils électriques de signalisation et d'alarme", Category.CLASS),
        Classification(
            "3162101",
            "la fabrication d'appareils électriques de signalisation, de sécurité, de contrôle ou de commande pour voies routières, pour voies ferrées, pour voies fluviales et installations portuaires et pour aéro",
            Category.CLASS,
        ),
        Classification(
            "3162102",
            "la fabrication d'autres appareils électriques de signalisation acoustique ou visuelle: sonneries, sirènes, tableaux annonciateurs, appareils avertisseurs pour la protection contre le vol ou l'incendie",
            Category.CLASS,
        ),
        Classification("31622", "Fabrication de matériel électromagnétique industriel", Category.CLASS),
        Classification(
            "3162201",
            "la fabrication d'électro-aimants,y compris les plateaux, mandrins et dispositifs magnétiques ou électromagnétiques similaires, les embrayages, freins, accouplements, variateurs de vitesse et têtes de",
            Category.CLASS,
        ),
        Classification("31623", "Fabrication d'autres matériels électriques n.d.a.", Category.CLASS),
        Classification(
            "3162301",
            "la fabrication de pièces isolantes pour machines, appareils et installations électriques.",
            Category.CLASS,
        ),
        Classification(
            "3162302", "la fabrication d'isolateurs pour l'électricité  et de pièces isolantes", Category.CLASS
        ),
        Classification(
            "3162303",
            "la fabrication de tubes isolateurs et de leurs pièces de raccordement, en métaux communs, isolés intérieurement",
            Category.CLASS,
        ),
        Classification("3162304", "la fabrication d'électrodes en charbon ou graphite", Category.CLASS),
        Classification(
            "3162305", "la fabrication de bancs et ciels solaires et autres appareils de bronzage", Category.CLASS
        ),
        Classification(
            "3162306",
            "la fabrication d'autres machines et appareils électriques: accélérateurs de particules, générateurs de signaux, détecteurs de mines, détonateurs électriques, etc.",
            Category.CLASS,
        ),
        Classification("32100", "Fabrication de composants électroniques", Category.CLASS),
        Classification(
            "3210001",
            "la fabrication de condensateurs électriques, y compris les condensateurs de puissance",
            Category.CLASS,
        ),
        Classification(
            "3210002", "la fabrication de résistances, y compris les rhéostats et les potentiomètres", Category.CLASS
        ),
        Classification("3210003", "la fabrication de circuits imprimés", Category.CLASS),
        Classification(
            "3210004",
            "la fabrication de lampes, tubes et valves électroniques à cathode chaude, froide ou à photocathode:tubes cathodiques pour récepteurs et pour caméras de TV, tubes de conversion, intensification,récepti",
            Category.CLASS,
        ),
        Classification(
            "3210005",
            "la fabrication de diodes, de transistors et de dispositifs similaires à semi-conducteur",
            Category.CLASS,
        ),
        Classification(
            "3210006",
            "la fabrication de dispositifs photosensibles à semi-conducteur, y compris les cellules photovoltaïques",
            Category.CLASS,
        ),
        Classification("3210007", "la fabrication de cristaux piézo-électriques montés", Category.CLASS),
        Classification(
            "3210008",
            "la fabrication de circuits intégrés et de micro-assemblage électroniques: circuits intégrés monolithiques, circuits intégrés hybrides et micro-assemblages électroniques de blocs moulés, de micromodule",
            Category.CLASS,
        ),
        Classification("32201", "Fabrication d'appareils d'émission et de transmission", Category.CLASS),
        Classification(
            "3220101",
            "la fabrication d'appareils d'émission pour la télévision, y compris la fabrication d'émetteurs-relais et d'émetteurs de télévision à usage industriel",
            Category.CLASS,
        ),
        Classification("3220102", "la fabrication de caméras de télévision", Category.CLASS),
        Classification("3220103", "la fabrication d'appareils d'émission pour la radiodiffusion", Category.CLASS),
        Classification(
            "3220104", "la fabrication d'équipements de radiodistribution et de télédistribution", Category.CLASS
        ),
        Classification("3220105", "la fabrication de relais hertziens, fixes ou mobiles", Category.CLASS),
        Classification(
            "3220106",
            "la fabrication d'appareils de commande, de mesure ou de signalisation à distance par voie hertzienne",
            Category.CLASS,
        ),
        Classification("3220107", "la fabrication d'antennes d'émission", Category.CLASS),
        Classification("32202", "Fabrication d'appareils de téléphonie", Category.CLASS),
        Classification(
            "3220201",
            "la fabrication d'appareils d'émission pour la radiotéléphonie ou la radiotélégraphie: émetteurs fixes et émetteurs-récepteurs, appareils d'intercommunication pour moyens le transport, radiotéléphones,",
            Category.CLASS,
        ),
        Classification(
            "3220202",
            "la fabrication d'appareils récepteurs pour la radiotéléphonie et la radiotélégraphie",
            Category.CLASS,
        ),
        Classification(
            "3220203",
            "la fabrication d'appareils pour la téléphonie par fil et pour la télégraphie:postes téléphoniques d'usagers,appareils de télécopie, appareils et centraux automatiques ou non pour la commutation, téléi",
            Category.CLASS,
        ),
        Classification(
            "32300",
            "Fabrication d'appareils de réception, enregistrement ou reproduction du son et de l'image",
            Category.CLASS,
        ),
        Classification(
            "3230001",
            "la fabrication d'appareils récepteurs de télévision, y compris les moniteurs vidéo et les projecteurs vidéo",
            Category.CLASS,
        ),
        Classification(
            "3230002",
            "la fabrication d'appareils d'enregistrement ou de reproduction vidéophoniques, y compris les caméscopes",
            Category.CLASS,
        ),
        Classification("3230003", "la fabrication d'appareils récepteurs de radiodiffusion", Category.CLASS),
        Classification(
            "3230004",
            "la fabrication de magnétophones et autres appareils d'enregistrement du son, les appareils d'enregistrement de cassettes, etc.",
            Category.CLASS,
        ),
        Classification("3230005", "la fabrication de tables de mixage", Category.CLASS),
        Classification(
            "3230006",
            "la fabrication d'appareils électro-acoustiques tels que interphones,installations d'interprétation simultanée,systèmes électroniques de vote,équipements pour conférences,téléavertisseurs, répondeurs t",
            Category.CLASS,
        ),
        Classification(
            "3230007",
            "la fabrication de tourne-disques, d'électrophones, de lecteurs de cassettes, de lecteurs de disques compacts, etc.",
            Category.CLASS,
        ),
        Classification(
            "3230008",
            "la fabrication de microphones, de hauts-parleurs, d'écouteurs, d'amplificateurs d'audiofréquence et d'appareils d'amplification du son",
            Category.CLASS,
        ),
        Classification(
            "3230009",
            "la fabrication de lecteurs phonographiques,bras de lecture, têtes magnétiques,platines pour tourne-disques,graveurs de disques,antennes,réflecteurs et rotors d'antenne,convertisseurs pour la télév. pa",
            Category.CLASS,
        ),
        Classification(
            "33101",
            "Fabrication d'appareils électriques pour la médecine, l'art dentaire et l'art vétérinaire",
            Category.CLASS,
        ),
        Classification(
            "3310101",
            "fabrication d'appareils électriques pour la médecine, l'art dentaire et l'art vétérinaire",
            Category.CLASS,
        ),
        Classification(
            "33102",
            "Fabrication d'appareils non-électriques pour la médecine, l'art dentaire et l'art vétérinaire",
            Category.CLASS,
        ),
        Classification(
            "3310201",
            "la fabrication d'appareils d'électrodiagnostic tels qu'électrocardiographes, appareils de diagnostic par ultrasons, tomodensitomètres à scintillation, installations de résonance magnétique nucléaire,",
            Category.CLASS,
        ),
        Classification("3310202", "la fabrication de tours dentaires", Category.CLASS),
        Classification("3310203", "la fabrication d'instruments d'ophtalmologie", Category.CLASS),
        Classification(
            "3310204",
            "la fabrication de stérilisateurs,de seringues, d'aiguilles à usage médical, de miroirs, de réflecteurs, d'endoscopes,etc.",
            Category.CLASS,
        ),
        Classification(
            "3310205",
            "la fabrication d'appareils à rayons X et d'appareils utilisant les radiations alpha, bêta ou gamma, même autres qu'à usage médical ou vétérinaire: tubes à rayons X, générateurs de tension, pupitres de",
            Category.CLASS,
        ),
        Classification(
            "3310206",
            "la fabrication de mobilier pour la médecine, la chirurgie, l'art dentaire ou l'art vétérinaire: tables d'opération, lits à mécanismes pour usages cliniques, fauteuils de dentistes",
            Category.CLASS,
        ),
        Classification(
            "3310207",
            "la fabrication d'appareils de mécanothérapie, de massage, de psychotechnie, d'ozonthérapie, d'oxygénothérapie, d'appareils respiratoires de réanimation, de masques à gaz, etc.",
            Category.CLASS,
        ),
        Classification("33103", "Fabrication d'articles orthopédiques et de prothèses", Category.CLASS),
        Classification(
            "3310301",
            "la fabrication d'articles et appareils d'orthopédie en toutes matières: ceintures et bandages médico-chirurgicaux, béquilles,attelles,gouttières,dents artif.,chaussures orthop., membres artific. et au",
            Category.CLASS,
        ),
        Classification(
            "33201",
            "Fabrication d'appareils électriques pour la mesure, la vérification, le contrôle et la navigation",
            Category.CLASS,
        ),
        Classification(
            "33202",
            "Fabrication d'appareils autres qu'électriques pour la mesure, la vérification, le contrôle et la navigation",
            Category.CLASS,
        ),
        Classification(
            "3320201",
            "la fabrication de balances de précision des types utilisés dans les laboratoires",
            Category.CLASS,
        ),
        Classification(
            "3320202",
            "la fabrication d'instruments de dessin, de traçage ou de calcul: mètres, micromètres, pieds à coulisse, calibres et jauges, etc.",
            Category.CLASS,
        ),
        Classification(
            "3320203", "la fabrication de microscopes autres qu'optiques et de diffractographes", Category.CLASS
        ),
        Classification(
            "3320204",
            "la fabrication d'appareils de mesure ou de contrôle de grandeurs électriques: oscilloscopes, analyseurs de spectre, hypsomètres, instruments de contrôle de l'intensité, de la tension, de la résistance",
            Category.CLASS,
        ),
        Classification(
            "3320205",
            "la fabrication d'appareils de mesure ou de contrôle de grandeurs non électriques:détecteurs et compteurs de radiations, appareils d'essai et de réglage de moteurs automobiles, etc.",
            Category.CLASS,
        ),
        Classification(
            "3320206",
            "la fabrication d'instruments et appareils de navigation, de météorologie, de géophysique, etc. (géodésie,océanographie, hydrologie,topographie,arpentage; radars,sonars,radionavigation; sismomètres,tél",
            Category.CLASS,
        ),
        Classification(
            "3320207", "la fabrication de compteurs d'électricité, d'eau, de gaz, d'essence, etc.", Category.CLASS
        ),
        Classification(
            "3320208",
            "la fabrication de machines et appareils d'essai des propriétés mécaniques des matériaux",
            Category.CLASS,
        ),
        Classification(
            "3320209",
            "la fabrication d'instruments et appareils pour analyses physiques ou chimiques : polarimètres, photomètres, réfractomètres, colorimètres, spectromètres, pH-mètres, viscomètres, instrum. et app. pour e",
            Category.CLASS,
        ),
        Classification(
            "3320210",
            "la fabrication d'instruments et appareils pour la mesure ou le contrôle du débit, du niveau, de la pression ou d'autres caractérist. variables des liquides ou des gaz: débitmètres, indicateurs de nive",
            Category.CLASS,
        ),
        Classification(
            "3320211", "la fabrication d'appareils et d'instruments optiques de mesure et de contrôle", Category.CLASS
        ),
        Classification(
            "3320212",
            "la fabrication d'autres instruments, appareils ou machines de mesure, de contrôle ou d'essais: densimètres, aréomètres, pèse-liquides,thermomètres,baromètres,compte-tours,taximètres,podomètres,tachymè",
            Category.CLASS,
        ),
        Classification("33300", "Fabrication d'équipements de contrôle des processus industriels", Category.CLASS),
        Classification(
            "3330001",
            "la conception, l'assemblage et l'entretien de systèmes de contrôle des processus industriels continus",
            Category.CLASS,
        ),
        Classification(
            "3330002",
            "la conception, l'assemblage et l'entretien d'unités de production automatisées comprenant plusieurs machines, équipements de manutention et appareils de contrôle centralisés",
            Category.CLASS,
        ),
        Classification("33401", "Fabrication de lunettes", Category.CLASS),
        Classification("3340101", "la fabrication de verres de lunetterie et de verres de contact", Category.CLASS),
        Classification("3340102", "la fabrication de montures de lunettes", Category.CLASS),
        Classification(
            "3340103",
            "la fabrication de montures équipées de verres travaillés optiquement ou non; lunettes solaires, lunettes protectrices (y compris les écrans protecteurs pour soudage) ou correctrices, etc.",
            Category.CLASS,
        ),
        Classification("33402", "Fabrication d'instruments d'optique et de matériel photographique", Category.CLASS),
        Classification(
            "3340201",
            "la fabrication d'éléments d'optique non travaillés et des matières autres que le verre",
            Category.CLASS,
        ),
        Classification(
            "3340202",
            "la fabrication de prismes, lentilles, miroirs optiques, filtres sélectifs de couleur, éléments polarisants,..., en verre ou en toute autre matière",
            Category.CLASS,
        ),
        Classification(
            "3340203",
            "la fabrication de fibres optiques et câbles de fibres optiques pour la transmission en direct d'images: endoscopie, éclairage, images en direct, etc.",
            Category.CLASS,
        ),
        Classification(
            "3340204",
            "la fabrication de microscopes optiques, matériel pour la photomicrographie ou la microprojection, loupes, verres pour la vision rapprochée, compte-fils, etc.",
            Category.CLASS,
        ),
        Classification(
            "3340205",
            "la fabrication de jumelles, lunettes astronomique, lunettes de visée, télescopes d'observation, instruments destinés à l'astronomie, etc.",
            Category.CLASS,
        ),
        Classification("3340206", "la fabrication de lasers autres que les diodes laser, etc.", Category.CLASS),
        Classification("3340207", "la fabrication d'appareils photographiques et caméras", Category.CLASS),
        Classification(
            "3340208",
            "la fabrication de projecteurs d'images fixes, appareils appareils d'agrandissement ou de réduction",
            Category.CLASS,
        ),
        Classification(
            "3340209",
            'la fabrication d\'appareils à tube à décharge (dits "flashes électroniques") et autres appareils et dispositifs pour la production de la lumière-éclair',
            Category.CLASS,
        ),
        Classification(
            "3340210",
            "la fabrication d'appareils et matériels pour les laboratoires photographiques ou cinématograph.,appareils pour la projection des tracés de circuits sur les surfaces sensibisées des matériaux semi-cond",
            Category.CLASS,
        ),
        Classification("33500", "Horlogerie", Category.CLASS),
        Classification(
            "3350001",
            "la fabrication de montres et d'horloges de tous types (y compris les horloges de tableau de bord), de boîtiers de montres, de cages et cabinets d'horlogerie (y compris ceux en métaux précieux),de mouv",
            Category.CLASS,
        ),
        Classification(
            "3350002",
            "la fabrication d'appareils de contrôle du temps ou d'appareils compteurs de temps tels que parcmètres, chronomicromètres, interrupteurs horaires et autres appareils de déclenchement",
            Category.CLASS,
        ),
        Classification(
            "3350003",
            "la fabrication de fournitures d'horlogerie telles que ressorts, pierres, cadrans, aiguilles, bracelets de montres métalliques, platines, ponts et autres pièces",
            Category.CLASS,
        ),
        Classification("34100", "Construction et assemblage de véhicules automobiles", Category.CLASS),
        Classification("3410001", "la fabrication de voitures de tourisme", Category.CLASS),
        Classification(
            "3410002",
            "la fabrication de véhicules utilitaires: camions et camionnettes, tracteurs routiers pour semi-remorques, tombereaux automoteurs, camions-grues, dépanneuses, véhicules blindés pour le transport de val",
            Category.CLASS,
        ),
        Classification("3410003", "la fabrication d'autobus, de trolleybus et d'autocars", Category.CLASS),
        Classification("3410004", "la fabrication de moteurs pour véhicules automobiles", Category.CLASS),
        Classification("3410005", "la fabrication de châssis avec moteur", Category.CLASS),
        Classification(
            "3410006",
            "la fabrication d'autres véhicules automobiles: autoneiges et motoneiges, véhicules spéciaux pour le transport de personnes sur les terrains de golf, véhicules amphibies, autopompes, balayeuses, biblio",
            Category.CLASS,
        ),
        Classification("34201", "Fabrication de carrosseries et remorques", Category.CLASS),
        Classification(
            "3420101",
            "la fabrication de carrosseries (y compris les cabines) pour véhicules automobiles",
            Category.CLASS,
        ),
        Classification("3420102", "la fabrication de remorques et de semi-remorques", Category.CLASS),
        Classification("3420103", "la fabrication de conteneurs spécialement conçus pour le transport", Category.CLASS),
        Classification(
            "3420104",
            "l'aménagement de tous types de véhicules automobiles (autocars, camions-citernes, camions-frigoriphiques, etc.)",
            Category.CLASS,
        ),
        Classification("34202", "Fabrication de caravanes et similaires", Category.CLASS),
        Classification("3420201", "la fabrication et l'aménagement de caravanes", Category.CLASS),
        Classification("3420202", "l'aménagement de véhicules de type autocaravane (motorhomes)", Category.CLASS),
        Classification("3420203", "la fabrication de remorques pour le camping", Category.CLASS),
        Classification("3420204", "la fabrication de baraques mobiles de chantier", Category.CLASS),
        Classification(
            "34300",
            "Fabrication de parties et accessoires pour les véhicules à moteur et pour leurs moteurs",
            Category.CLASS,
        ),
        Classification(
            "3430001",
            "la fabrication de freins, boîtes de vitesses, essieux,roues, amortisseurs de suspension,radiateurs, silencieux, tuyaux d'échappement, pots d'échappement catalytiques, embrayages, volants, colonnes et",
            Category.CLASS,
        ),
        Classification("3430002", "la fabrication de culasses, bielles, pistons, segments, etc.", Category.CLASS),
        Classification(
            "3430003", "la fabrication de ceintures de sécurité, portières, parechocs, etc.", Category.CLASS
        ),
        Classification("35110", "Construction et réparation de navires", Category.CLASS),
        Classification(
            "3511001",
            "la construction, l'entretien, la réparation ou la transformation de navires ou de parties de navires: navires à passagers, transbordeurs, cargos, bateaux-citernes, etc.",
            Category.CLASS,
        ),
        Classification(
            "3511002",
            "la construction, l'entretien, la réparation ou la transformation de navires ou de parties de navires: navires de guerre (y compris l'implantation des systèmes d'armes)",
            Category.CLASS,
        ),
        Classification(
            "3511003",
            "la construction, l'entretien, la réparation ou la transformation de navires ou de parties de navires: remorqueurs",
            Category.CLASS,
        ),
        Classification(
            "3511004",
            "la construction, l'entretien, la réparation ou la transformation de navires ou de parties de navires: bateaux de pêche",
            Category.CLASS,
        ),
        Classification("3511005", "la construction d'aéroglisseurs", Category.CLASS),
        Classification(
            "3511006", "la construction de plates-formes de forage flottantes ou submersibles", Category.CLASS
        ),
        Classification(
            "3511007",
            "la construction de docks flottants, pontons, caissons, coffres d'amarrage flottants, bouées, réservoir flottants, barges, allèges, gabares, grues, etc.",
            Category.CLASS,
        ),
        Classification("3511008", "la peinture des navires par des unités spécialisées", Category.CLASS),
        Classification("3511009", "la démolition de bateaux", Category.CLASS),
        Classification("35120", "Construction et réparation de bâteaux de plaisance et de sport", Category.CLASS),
        Classification("3512001", "la fabrication de canots pneumatiques", Category.CLASS),
        Classification("3512002", "la construction de voiliers, avec ou sans moteur auxiliaire", Category.CLASS),
        Classification("3512003", "la construction de bateaux à moteur", Category.CLASS),
        Classification(
            "3512004",
            "la construction d'autres embarcations de plaisance et de sport: canoës, kayaks, skiffs, etc.",
            Category.CLASS,
        ),
        Classification(
            "3512005", "l'entretien, la réparation et l'aménagement de bateaux de plaisance ou de sport", Category.CLASS
        ),
        Classification("35200", "Construction de matériel ferroviaire roulant", Category.CLASS),
        Classification(
            "3520001", "la fabrication de locomotives et de locotracteurs diesel ou électriques", Category.CLASS
        ),
        Classification(
            "3520002",
            "la fabrication d'automotrices, d'autorails, de véhicules d'entretien ou de service",
            Category.CLASS,
        ),
        Classification(
            "3520003",
            "la fabrication de véhicules pour voies ferrées ou similaires dépourvus d'organes moteurs:voitures à voyageurs,wagons pour le transport de marchandises,wagons-citernes,wagons à déchar gement automatiqu",
            Category.CLASS,
        ),
        Classification(
            "3520004",
            "la fabrication de parties de véhicules pour voies ferrées ou similaires: bogies, essieux et roues, freins et leurs parties, crochets et autres systèmes d'attelage,tampons de choc et leurs parties,amor",
            Category.CLASS,
        ),
        Classification(
            "3520005",
            "la fabrication d'appareils mécaniques et électromécaniques de signalisation, de sécurité, de contrôle ou de commande pour voies ferrées, voies routières, voies fluviales et installations portuaires, a",
            Category.CLASS,
        ),
        Classification(
            "3520006",
            "l'entretien et la réparation de matériel ferroviaire roulant et d'appareils mécaniques et électromécaniques de signalisation ou de sécurité",
            Category.CLASS,
        ),
        Classification("35300", "Construction aéronautique et spatiale", Category.CLASS),
        Classification(
            "3530001",
            "la construction d'avions conçus pour le transport de marchandises ou de passagers, pour les forces militaires (y compris l'implantation des armements), pour le sport ou pour d'autres usages",
            Category.CLASS,
        ),
        Classification("3530002", "la construction d'hélicoptères", Category.CLASS),
        Classification("3530003", "la construction d'avions dits ULM", Category.CLASS),
        Classification("3530004", "la construction de planeurs et d'ailes delta", Category.CLASS),
        Classification("3530005", "la construction de dirigeables et de ballons", Category.CLASS),
        Classification(
            "3530006",
            "la construction de véhicules spatiaux et de leurs lanceurs, de satellites, de sondes planétaires, de stations orbitales, de navettes spatiales",
            Category.CLASS,
        ),
        Classification(
            "3530007",
            "la fabrication et l'assemblage de parties et accessoires de véhicules aériens: fuselages, ailes, portes, empennages, gouvernes, trains d'atterrissage, réservoirs à combustibles, nacelles, etc.",
            Category.CLASS,
        ),
        Classification(
            "3530008",
            "la fabrication et l'assemblage de parties et accessoires de véhicules aériens: hélices, rotors et pales de rotors pour hélicoptères",
            Category.CLASS,
        ),
        Classification(
            "3530009",
            "la fabrication et l'assemblage de parties et accessoires de véhicules aériens: moteurs des types généralement utilisés pour la propulsion des véhicules aériens et parties de turboréacteurs et de turbo",
            Category.CLASS,
        ),
        Classification(
            "3530010",
            "la fabrication d'appareils et de dispositifs pour le lancement de véhicules aériens ainsi que d'appareils et de dispositifs d'appontage, etc.",
            Category.CLASS,
        ),
        Classification(
            "3530011", "la fabrication d'appareils d'entraînement au vol au (simulateurs de vol)", Category.CLASS
        ),
        Classification("35410", "Fabrication de motocycles", Category.CLASS),
        Classification(
            "3541001",
            "la fabrication de motocycles, de cyclomoteurs et de cycles équipés d'un moteur auxiliaire",
            Category.CLASS,
        ),
        Classification("3541002", "la fabrication de moteurs pour motocycles", Category.CLASS),
        Classification("3541003", "la fabrication de side-cars", Category.CLASS),
        Classification("3541004", "la fabrication de parties et accessoires pour motocycles", Category.CLASS),
        Classification("35420", "Fabrication de bicyclettes", Category.CLASS),
        Classification(
            "3542001",
            "la fabrication de bicyclettes et autres cycles (y compris les triporteurs), sans moteur",
            Category.CLASS,
        ),
        Classification("3542002", "la fabrication de parties et accessoires de bicyclettes", Category.CLASS),
        Classification("35430", "Fabrication de véhicules pour invalides", Category.CLASS),
        Classification("3543001", "la fabrication de véhicules pour invalides, avec ou sans moteur", Category.CLASS),
        Classification(
            "3543002", "la fabrication de parties et accessoires de véhicules pour invalides", Category.CLASS
        ),
        Classification("35500", "Fabrication d'autres matériels de transport n.d.a.", Category.CLASS),
        Classification(
            "3550001", "la fabrication de brouettes, de diables, de charrettes à bras, de caddies, etc.", Category.CLASS
        ),
        Classification("3550002", "la fabrication de véhicules à traction animale", Category.CLASS),
        Classification("36100", "Fabrication de meubles", Category.CLASS),
        Classification("3610001", "FAB. DE MEUBLES EN TOUS MATéRIAUX", Category.CLASS),
        Classification("36111", "Fabrication de chaises et de sièges d'ameublement et de bureau", Category.CLASS),
        Classification(
            "3611101",
            "la fabrication de sièges d'ameublement et de parties de sièges: chaises, bancs, fauteuils, canapés, tabourets, etc.",
            Category.CLASS,
        ),
        Classification("3611102", "la fabrication de sièges de bureau et d'atelier", Category.CLASS),
        Classification(
            "3611103", "le finissage des sièges par des opérations telles que le rembourrage", Category.CLASS
        ),
        Classification(
            "36112",
            "Fabrication de chaises et de sièges pour salles de spectacle et pour véhicules et autres moyens de transport en tous matériaux",
            Category.CLASS,
        ),
        Classification(
            "3611201",
            "la fabrication et le finissage de sièges pour théâtres et cinémas, pour véhicules automobiles, pour navires et avions, ..., y compris la fabrication de parties de sièges telles les carcasses et les mé",
            Category.CLASS,
        ),
        Classification(
            "36121", "Fabrication de meubles de bureaux, de magasins et d'ateliers, en métal", Category.CLASS
        ),
        Classification(
            "3612101",
            "la fabrication de meubles spéciaux pour magasins: comptoirs, présentoirs, rayonnages, etc.",
            Category.CLASS,
        ),
        Classification(
            "3612102",
            "la fabrication de meubles de bureau et d'atelier, meubles pour restaurants, écoles, églises, etc.",
            Category.CLASS,
        ),
        Classification(
            "36122", "Fabrication de meubles de bureaux, de magasins et d'ateliers, autres qu'en métal", Category.CLASS
        ),
        Classification(
            "3612201",
            "la fabrication de meubles spéciaux pour magasins, autres qu'en métal: comptoirs, présentoirs, rayonnages, etc.",
            Category.CLASS,
        ),
        Classification(
            "3612202",
            "la fabrication de meubles de bureau et d'atelier, meubles pour restaurants, écoles, églises, etc., autres qu'en métal",
            Category.CLASS,
        ),
        Classification("36130", "Fabrication d'autres meubles de cuisine", Category.CLASS),
        Classification(
            "3613001", "la fabrication de meubles et d'éléments modulaires pour cuisines équipées", Category.CLASS
        ),
        Classification("3613002", "la fabrication de meubles de salle de bains", Category.CLASS),
        Classification(
            "36141", "Fabrication de meubles pour salles à manger, salons et chambres à coucher", Category.CLASS
        ),
        Classification(
            "3614101",
            "la fabrication et le finissage (y compris le capitonnage, la mise en peinture, le vernissage, etc.) de meubles des types utilisés dans les chambres à coucher et dans les salles à manger et de séjour",
            Category.CLASS,
        ),
        Classification(
            "3614102",
            "la fabrication de placards, de meubles spéciaux pour appareils de télévision, de meubles de complément, etc.",
            Category.CLASS,
        ),
        Classification("3614103", "la rénovation et la restauration de meubles", Category.CLASS),
        Classification("36142", "Fabrication de meubles de jardin et d'extérieur", Category.CLASS),
        Classification("3614201", "la fabrication de meubles de jardin et d'extérieur", Category.CLASS),
        Classification("36150", "Fabrication de matelas", Category.CLASS),
        Classification(
            "3615001",
            "la fabrication de sommiers, de sommiers à lattes et d'autres supports de matelas",
            Category.CLASS,
        ),
        Classification(
            "3615002",
            "la fabrication de matelas: matelas comportant des ressorts ou rembourrés ou garnis intérieurement d'un matériau de soutien; matelas non recouverts en caoutchouc alvéolaire ou en matières plastiques al",
            Category.CLASS,
        ),
        Classification("36210", "Fabrication de monnaies", Category.CLASS),
        Classification("3621001", "la fabrication de monnaies, y compris celles ayant cours légal", Category.CLASS),
        Classification(
            "3621002", "la fabrication de médailles et de médaillons, en métaux précieux ou non", Category.CLASS
        ),
        Classification("36221", "Travail du diamant", Category.CLASS),
        Classification(
            "3622101",
            "le travail du diamant, y compris le diamant de qualité industrielle: scier, tailler, polir, etc.",
            Category.CLASS,
        ),
        Classification("36222", "Travail des autres pierres précieuses et des pierres semi-précieuses", Category.CLASS),
        Classification("3622201", "la fabrication de perles travaillées", Category.CLASS),
        Classification(
            "3622202",
            "la fabrication de pierres gemmes (précieuses ou fines) travaillées, à l'exclusion du diamant",
            Category.CLASS,
        ),
        Classification(
            "3622203",
            "le travail de pierres de qualité industrielle (à l'exclusion du diamant) et de pierres synthétiques ou reconstituées",
            Category.CLASS,
        ),
        Classification("36223", "Fabrication de bijoux et de parures", Category.CLASS),
        Classification(
            "3622301",
            "la fabrication d'articles de bijouterie en métaux précieux, en plaqués ou en doublés de métaux précieux ou de pierres gemmes sur des métaux communs, ou en assemblage de métal précieux et de pierres ge",
            Category.CLASS,
        ),
        Classification("3622302", "la fabrication de bracelets de montres en métaux précieux", Category.CLASS),
        Classification("36224", "Fabrication d'articles d'orfèvrerie", Category.CLASS),
        Classification(
            "3622401",
            "la fabrication d'articles d'orfèvrerie en métaux précieux ou en plaqués ou doublés de métaux précieux sur des métaux communs: vaisselle plate ou creuse, couverts, articles de toilette,garnitures de bu",
            Category.CLASS,
        ),
        Classification(
            "3622402",
            "la fabrication de catalyseurs en métaux précieux et d'articles d'usage pour laboratoires",
            Category.CLASS,
        ),
        Classification("3622403", "la gravure d'objets en métaux précieux", Category.CLASS),
        Classification("36300", "Fabrication d'instruments de musique", Category.CLASS),
        Classification("3630001", "la fabrication d'instruments à cordes", Category.CLASS),
        Classification(
            "3630002",
            "la fabrication d'instruments à cordes à clavier, y compris les pianos automatiques",
            Category.CLASS,
        ),
        Classification(
            "3630003",
            "la fabrication d'orges à tuyaux et à clavier, y compris les harmoniums et instruments similaires à clavier et à anches libres métalliques",
            Category.CLASS,
        ),
        Classification(
            "3630004",
            "la fabrication d'accordéons et d'instruments similaires, y compris les harmonicas à bouche",
            Category.CLASS,
        ),
        Classification("3630005", "la fabrication d'instruments à vent", Category.CLASS),
        Classification("3630006", "la fabrication d'instruments de musique à percussion", Category.CLASS),
        Classification(
            "3630007",
            "la fabrication d'instruments de musique dont le son est produit électroniquement",
            Category.CLASS,
        ),
        Classification(
            "3630008", "la fabrication de boîtes à musique, d'orchestrions, d'orges du Barbarie, etc.", Category.CLASS
        ),
        Classification(
            "3630009",
            "La fabrication de parties et accessoires d'instruments de musique: métronomes, diapasons, cartes, disques et rouleaux pour instruments mécaniques, etc.",
            Category.CLASS,
        ),
        Classification(
            "3630010",
            "la fabrication de sifflets, de cornes d'appel et d'autres instruments d'appel ou de signalisation à bouche",
            Category.CLASS,
        ),
        Classification("3630011", "la réparation d'instruments de musique", Category.CLASS),
        Classification("36400", "Fabrication d'articles de sport", Category.CLASS),
        Classification("3640001", "la fabrication de balles et ballons durs, mous ou gonflables", Category.CLASS),
        Classification("3640002", "la fabrication de raquettes, battes et clubs de golf", Category.CLASS),
        Classification("3640003", "la fabrication de filets pour la pratique de sports divers", Category.CLASS),
        Classification("3640004", "la fabrication de matériel pour les sports d'hiver et l'alpinisme", Category.CLASS),
        Classification(
            "3640005",
            "la fabrication d'articles pour la pêche sportive (y compris les épuisettes) et pour la chasse",
            Category.CLASS,
        ),
        Classification(
            "3640006",
            "la fabrication de matériel pour les sports nautiques (y compris planches à voile et combinaisons isothermes)",
            Category.CLASS,
        ),
        Classification("3640007", "la fabrication d'arcs et arbalètes", Category.CLASS),
        Classification("3640008", "la fabrication de patins à glace, patins à roulettes, etc.", Category.CLASS),
        Classification("3640009", "la fabrication de bassins pour piscines et pataugeoires", Category.CLASS),
        Classification("3640010", "la fabrication de matériels pour la gymnastique ou l'athlétisme", Category.CLASS),
        Classification(
            "3640011",
            "la fabrication d'appareils et matériels pour le body-building et les centres fitness",
            Category.CLASS,
        ),
        Classification("3640012", "la fabrication de gants et coiffures de sport en cuir", Category.CLASS),
        Classification("36500", "Fabrication de jeux et jouets", Category.CLASS),
        Classification(
            "3650001", "la fabrication de poupées et de vêtements et accessoires pour poupées", Category.CLASS
        ),
        Classification("3650002", "la fabrication de jouets représentant des animaux", Category.CLASS),
        Classification(
            "3650003",
            "la fabrication de jouets à roues conçus pour être montés par les enfants, y compris les tricycles",
            Category.CLASS,
        ),
        Classification(
            "3650004", "la fabrication d'instruments de musique ayant le caractère de jouets", Category.CLASS
        ),
        Classification(
            "3650005", "la fabrication d'articles pour jeux de société et de cartes à jouer", Category.CLASS
        ),
        Classification(
            "3650006",
            "la fabrication de jeux à moteur ou à mouvement, de jeux fonctionnant au moyen de pièces de monnaie, de billard, de tables spéciales pour jeux de casino,de jeux de quilles automatiques (bowlings), etc.",
            Category.CLASS,
        ),
        Classification(
            "3650007", "la fabrication de jeux électroniques: jeux vidéo, jeux d'échecs, etc.", Category.CLASS
        ),
        Classification(
            "3650008",
            "la fabrication de modèles réduits et de modèles similaires pour le divertissement, de trains électriques, de circuits auto, de jeux de construction, etc.",
            Category.CLASS,
        ),
        Classification("3650009", "la fabrication de puzzles, etc.", Category.CLASS),
        Classification("36610", "Fabrication de bijoux de fantaisie", Category.CLASS),
        Classification(
            "3661001",
            "la fabrication de bijouterie de fantaisie et d'articles de parure en toutes matières ne comprenant ni métaux précieux, ni plaqués, ni doublés de métaux précieux, ni pierres fines ou précieuses",
            Category.CLASS,
        ),
        Classification("36620", "Fabrication d'articles de brosserie", Category.CLASS),
        Classification(
            "3662001",
            "la fabrication de brosserie: balais mécaniques à usage manuel, balais, plumeaux, balayettes, brosses, etc.; raclettes en caoutchouc ou en d'autres matières souples; brosses, pinceaux, rouleaux et tamp",
            Category.CLASS,
        ),
        Classification("3662002", "la fabrication de brosses à habits et à chaussures", Category.CLASS),
        Classification("36630", "Autres activités manufacturières n.d.a.", Category.CLASS),
        Classification(
            "3663001", "la fabrication de stylos et de crayons de tous types, mécaniques ou non", Category.CLASS
        ),
        Classification("3663002", "la fabrication de mines pour crayons", Category.CLASS),
        Classification(
            "3663003",
            "la fabrication de dateurs, de cachets ou de numéroteurs, d'appareils manuels pour l'impression d'étiquettes, d'imprimeries à main, de rubans encreurs préparés pour machines à écrire et de tampons encr",
            Category.CLASS,
        ),
        Classification("3663004", "la fabrication de landaux et de poussettes", Category.CLASS),
        Classification(
            "3663005",
            "la fabrication de parapluies, d'ombrelles, de parasols, de cannes, de fouets, de cravaches",
            Category.CLASS,
        ),
        Classification(
            "3663006", "la fabrication de boutons, de boutons-pression et de fermetures à glissière", Category.CLASS
        ),
        Classification("3663007", "la fabrication de briquettes et d'allumettes", Category.CLASS),
        Classification(
            "3663008",
            "la fabrication d'articles à usage personnel: pipes, peignes à coiffer, barrettes, vaporisateurs de toilette, perruques, fausses barbes, etc.; bouteilles isolantes et autres récipients isothermiques à",
            Category.CLASS,
        ),
        Classification(
            "3663009",
            "la fabrication de manèges, de balançoires, de stands de tir et d'autres attractions pour foires et parcs d'attractions",
            Category.CLASS,
        ),
        Classification(
            "3663010",
            "la fabrication de linoléum et de revêtements de sol rigides en des matières autres que les matières plastiques",
            Category.CLASS,
        ),
        Classification(
            "3663011", "la fabrication de bougies, chandelles, cierges et articles similaires", Category.CLASS
        ),
        Classification(
            "3663012",
            "la fabrication de fleurs, fruits et feuillages artificiels et d'articles d'ornementation en fleurs séchées",
            Category.CLASS,
        ),
        Classification(
            "3663013",
            "la fabrication d'articles-surprises, d'articles pour fêtes et d'articles de prestidigitation",
            Category.CLASS,
        ),
        Classification("3663014", "les activités des taxidermistes", Category.CLASS),
        Classification(
            "3663015",
            "la fabrication d'articles divers: tamis et cribles à main, mannequins et autres articles de vitrine, etc.",
            Category.CLASS,
        ),
        Classification("37100", "Récupération des matières métalliques recyclables", Category.CLASS),
        Classification(
            "3710001",
            "la récupération de métaux ferreux et non ferreux recyclables par broyage par des procédés mécaniques d'objets métalliques tels que vieilles voitures, machines à laver hors d'usage, vieux vélos, .., su",
            Category.CLASS,
        ),
        Classification(
            "3710002",
            "la récupération de métaux ferreux et non ferreux recyclables par la réduction par des procédés mécaniques, d'objets métalliques volumineux tels que wagons de chemin de fer",
            Category.CLASS,
        ),
        Classification(
            "3710003",
            "la récupération de métaux ferreux et non ferreux recyclables par le compactage des ferrailles et des véhicules usagés",
            Category.CLASS,
        ),
        Classification(
            "3710004",
            "la récupération de métaux ferreux et non ferreux recyclables par le démontage d'objets hors d'usage (voitures p.ex.) afin d'en extraire les éléments récupérables",
            Category.CLASS,
        ),
        Classification(
            "3710005",
            "la récupération de métaux ferreux et non ferreux recyclables par le démontage d'objets hors d'usage (voitures ou réfrigérateurs p.ex.) afin d'en éliminer les éléments toxiques (huile, liquide de refro",
            Category.CLASS,
        ),
        Classification("37200", "Récupération de matières non métalliques recyclables", Category.CLASS),
        Classification(
            "3720001",
            "la régénération de caoutchouc (p.ex. régénération de pneumatiques usagés) afin d'obtenir des matières premières secondaires",
            Category.CLASS,
        ),
        Classification(
            "3720002",
            "le triage et le pastillage de matières plastiques en vue d'obtenir des matières premières secondaires utilisables pour la fabrication de tubes, de pots à fleurs, de palettes, etc.",
            Category.CLASS,
        ),
        Classification(
            "3720003",
            "la récupération de produits chimiques (y compris les huiles) à partir de déchets chimiques",
            Category.CLASS,
        ),
        Classification("3720004", "le broyage, le nettoyage et le triage du verre", Category.CLASS),
        Classification(
            "3720005",
            "le broyage, le nettoyage et le triage d'autres déchets en vue d'obtenir des matières premières secondaires",
            Category.CLASS,
        ),
        Classification("37210", "Récupération de papier", Category.CLASS),
        Classification("37220", "Récupération du textile", Category.CLASS),
        Classification("37230", "Récupération des matières chimiques", Category.CLASS),
        Classification("40100", "Production et distribution d'électricité", Category.CLASS),
        Classification(
            "4010001",
            "la production d'électricité par n'importe quelle technique: centrale thermique classique ou nucléaire, usine hydro-électrique ou par turbine à gaz, par centrale diesel ou à partir d'autres sources d'é",
            Category.CLASS,
        ),
        Classification("4010002", "la transmission et la distribution d'électricité", Category.CLASS),
        Classification("40110", "Production d'électricité", Category.CLASS),
        Classification("40120", "Transport d'électricité", Category.CLASS),
        Classification("40130", "Distribution et commerce d'électricité", Category.CLASS),
        Classification("40200", "Production et distribution de gaz", Category.CLASS),
        Classification(
            "4020001",
            "la production de combustibles gazeux d'une valeur calorifique déterminée par purification,mélange ou autres traitements de gaz d'origines diverses, y compris le biogaz et le gaz de houille",
            Category.CLASS,
        ),
        Classification(
            "4020002",
            "le transport et la distribution par conduites de combustibles gazeux de tous types",
            Category.CLASS,
        ),
        Classification("4020003", "la gestion de réservoirs de stockage", Category.CLASS),
        Classification("4020004", "la mise en bouteille de gaz", Category.CLASS),
        Classification("40210", "Production de gaz", Category.CLASS),
        Classification("40220", "Distribution et commerce de combustibles gazeux", Category.CLASS),
        Classification(
            "40300",
            "Production et distribution de vapeur et d'eau chaude; production de glace hydriques non destinées à la consommation",
            Category.CLASS,
        ),
        Classification(
            "4030001",
            "la production, la collecte et la distribution de vapeur et d'eau chaude pour le chauffage, la force motrice et d'autres usages",
            Category.CLASS,
        ),
        Classification(
            "4030002",
            "la production et la distribution d'eau froide ou de glace pour le refroidissement",
            Category.CLASS,
        ),
        Classification("40400", "Production et distribution de plusieurs sortes d'énergie", Category.CLASS),
        Classification("41000", "Captage, épuration et distribution d'eau", Category.CLASS),
        Classification("4100001", "le captage, l'épuration et la distribution d'eau", Category.CLASS),
        Classification(
            "4100002",
            "le dessalement de l'eau de mer, pour autant que la production d'eau constitue l'activité principale",
            Category.CLASS,
        ),
        Classification("45111", "Démolition d'immeubles", Category.CLASS),
        Classification("4511101", "le démolition d'immeubles et autres constructions", Category.CLASS),
        Classification("4511102", "le déblayage des chantiers", Category.CLASS),
        Classification("45112", "Terrassements", Category.CLASS),
        Classification(
            "4511201",
            "les travaux de terrassement: creusement, comblement, nivellement de chantiers de construction, ouverture de tranchées, dérochement, destruction à l'explosifs, etc.",
            Category.CLASS,
        ),
        Classification(
            "4511202",
            "la préparation de sites pour l'exploitation minière: enlèvement de déblais et autres travaux d'aménagement et de préparation des terrains et sites miniers",
            Category.CLASS,
        ),
        Classification(
            "4511203",
            "le rabattement de la nappe aquifère et le drainage des chantiers des construction",
            Category.CLASS,
        ),
        Classification("4511204", "le drainage des terrains agricoles et sylvicoles", Category.CLASS),
        Classification("45120", "Forages et sondages", Category.CLASS),
        Classification(
            "4512001",
            "les sondages d'essai, les forages d'essai et les carottages pour la construction ainsi que pour les études géophysiques, géologiques et similaires",
            Category.CLASS,
        ),
        Classification(
            "4512002", "l'exécution de forages horizontaux pour passages de câbles ou de canalisations", Category.CLASS
        ),
        Classification("45200", "Construction d'ouvrages de bâtiment ou de génie civil", Category.CLASS),
        Classification("4520001", "RéALISAT. DU GROS OEUVRE DES BâTIMENTS", Category.CLASS),
        Classification("4520002", "LA COORDINATION GéNéRALE SUR LE CHANTIER", Category.CLASS),
        Classification("45211", "Construction de maisons individuelles", Category.CLASS),
        Classification("4521101", "la réalisation du gros oeuvre de maisons individuelles", Category.CLASS),
        Classification("4521102", 'la construction de maisons individuelles "clés en mains"', Category.CLASS),
        Classification(
            "45212", "Construction d'autres immeubles résidentiels et d'immeubles de bureaux", Category.CLASS
        ),
        Classification(
            "4521201",
            "la réalisation du gros oeuvre de bâtiments à cellules multiples (appartements, bureaux, etc.)",
            Category.CLASS,
        ),
        Classification("4521202", 'la réalisation d\'appartements "clés en mains"', Category.CLASS),
        Classification("45213", "Construction de bâtiments d'usage industriel, commercial ou agricole", Category.CLASS),
        Classification(
            "4521301",
            "la réalisation du gros oeuvre de bâtiments et ouvrages industriels ou commerciaux,de dépôts de véhicules,d'entrepôts, d'écoles, de cliniques, de bâtiments pour la pratique d'un culte, d'un sport ou à",
            Category.CLASS,
        ),
        Classification("4521302", "le montage de hangars, granges, silos, ..., à usages agricoles", Category.CLASS),
        Classification("45214", "Construction de tunnels, ponts, viaducs et similaires", Category.CLASS),
        Classification(
            "4521401",
            "la construction de ponts, y compris ceux destinés à supporter des routes surélevées, viaducs, etc.",
            Category.CLASS,
        ),
        Classification(
            "4521402",
            "la construction de tunnels routiers et ferroviaires et d'autres passages souterrains",
            Category.CLASS,
        ),
        Classification(
            "45215",
            "Réalisation de canalisations à longue distance, construction de réseaux de télécommunication, construction de lignes de transport d'énergie",
            Category.CLASS,
        ),
        Classification(
            "4521501",
            "la construction de réseaux d'adduction, de distribution et d'évacuation des eaux",
            Category.CLASS,
        ),
        Classification(
            "4521502", "la construction de réseaux de transport de gaz, de produits pétroliers, etc.", Category.CLASS
        ),
        Classification(
            "4521503", "la construction de lignes de transport et de distribution d'énergie électrique", Category.CLASS
        ),
        Classification("4521504", "la construction de lignes et de réseaux de télécommunication", Category.CLASS),
        Classification("45220", "Réalisation de charpentes et de couvertures", Category.CLASS),
        Classification("4522001", "le montage de charpentes", Category.CLASS),
        Classification("4522002", "les travaux de couverture en tous matériaux", Category.CLASS),
        Classification("4522003", "la mise en place des éléments d'évacuation des eaux de pluie", Category.CLASS),
        Classification("4522004", "les travaux d'étanchéification des toits et des toituresterrasses", Category.CLASS),
        Classification(
            "45230", "Construction d'autoroutes, de routes, d'aérodromes et d'installations sportives", Category.CLASS
        ),
        Classification(
            "4523001",
            "la construction de voies ferrées: pose du ballast et des rails, remise en état et réparations des voies",
            Category.CLASS,
        ),
        Classification(
            "4523002",
            "la constructions d'autoroutes, de routes, de rues, de chaussées et d'autres voies pour véhicules et piétons (y compris la pose de glissières de sécurité)",
            Category.CLASS,
        ),
        Classification("4523003", "la construction de pistes d'atterrissage", Category.CLASS),
        Classification(
            "4523004", "la construction de terrains de jeux et de sport, de bassins de natation, etc.", Category.CLASS
        ),
        Classification(
            "4523005", "la marquage à la peinture des chaussées et des aires ou parcs de stationnement", Category.CLASS
        ),
        Classification("45241", "Travaux de dragage", Category.CLASS),
        Classification("4524101", "la réalisation de travaux de dragage", Category.CLASS),
        Classification("4524102", "le curage des cours d'eau, fossés, etc.", Category.CLASS),
        Classification("45242", "Autres travaux maritimes et fluviaux", Category.CLASS),
        Classification(
            "4524201", "la construction de ports (y compris les ports de plaisance) et de bassins", Category.CLASS
        ),
        Classification("4524202", "la construction de barrages et de digues", Category.CLASS),
        Classification("4524203", "la construction de canaux et d'autres voies navigables", Category.CLASS),
        Classification("4524204", "la construction d'écluses et autres ouvrages de régulation", Category.CLASS),
        Classification(
            "4524205",
            "la construction de bassins de décantation et d'autres ouvrages pour l'épuration des eaux usées",
            Category.CLASS,
        ),
        Classification("4524206", "l'exécution des travaux sous-marins de toute nature", Category.CLASS),
        Classification("45250", "Autres travaux de construction spécialisés", Category.CLASS),
        Classification("4525001", "mise en place de fondations, y compris battage de pieux", Category.CLASS),
        Classification("4525002", "forage et construction de puits d'eau, fonçage de puits", Category.CLASS),
        Classification("4525003", "travaux de ferraillage et pose de coffrage", Category.CLASS),
        Classification("4525004", "maçonnerie", Category.CLASS),
        Classification("4525005", "pose de chape", Category.CLASS),
        Classification("4525006", "la construction de cheminées et de fours industriels", Category.CLASS),
        Classification("4525007", "la construction de cheminées décoratives et de feux ouverts", Category.CLASS),
        Classification(
            "4525008",
            "montage d'éléments de structures métalliques non fabriqués par l'unité qui exécute les travaux",
            Category.CLASS,
        ),
        Classification("4525009", "l'exécution pour les tiers de travaux de levage", Category.CLASS),
        Classification("4525010", "montage et démontage d'échafaudages et de plates-formes de travail", Category.CLASS),
        Classification("4525011", "l'exécution de travaux de rejointoiement", Category.CLASS),
        Classification("4525012", "la construction de chambres froides, chambres fortes, etc.", Category.CLASS),
        Classification("45310", "Travaux d'installation électrique", Category.CLASS),
        Classification("4531001", "l'installation de câbles et appareils électriques", Category.CLASS),
        Classification(
            "4531002", "l'installation de systèmes d'alimentation de secours (groupes électrogènes)", Category.CLASS
        ),
        Classification(
            "4531003", "l'installation de systèmes de télécommunication et installations informatiques", Category.CLASS
        ),
        Classification("4531004", "l'installation de installations électriques de chauffage", Category.CLASS),
        Classification("4531005", "l'installation d'ascenseurs et escaliers mécaniques", Category.CLASS),
        Classification(
            "4531006", "l'installation de systèmes de surveillance et d'alarme contre les effractions", Category.CLASS
        ),
        Classification("4531007", "l'installation d'antennes d'immeubles et paratonnerres", Category.CLASS),
        Classification("45320", "Travaux d'isolation", Category.CLASS),
        Classification(
            "4532001",
            "la mise en oeuvre dans des bâtiments ou d'autres projets de construction de: matériaux d'isolation thermique, matériaux d'isolation acoustique et antivibratile",
            Category.CLASS,
        ),
        Classification(
            "4532002", "les travaux d'isolation de canalisations de chauffage ou de réfrigération", Category.CLASS
        ),
        Classification(
            "4532003", "les travaux d'isolation de chambres froides ou d'entrepôts frigorifiques", Category.CLASS
        ),
        Classification(
            "45331", "Installation de systèmes de chauffage, de climatisation et de ventilation", Category.CLASS
        ),
        Classification(
            "4533101",
            "l'installation dans des bâtiments ou d'autres projets de construction de: conduites et équipements de chauffage (y compris les systèmes de régularisation), de ventilation, de réfrigération ou de clima",
            Category.CLASS,
        ),
        Classification(
            "4533102",
            "Installation de systèmes de chauffage, de climatisation et de      ventilation (sauf chauffage)",
            Category.CLASS,
        ),
        Classification("45332", "Autres travaux de plomberie", Category.CLASS),
        Classification(
            "4533201",
            "l'installation dans des bâtiments ou autres constructions de réseaux de distribution de l'eau ou du gaz dans les locaux, plomberie et appareils sanitaires fixes, installation d'extinction automatique,",
            Category.CLASS,
        ),
        Classification("45340", "Autres travaux d'installation", Category.CLASS),
        Classification(
            "4534001",
            "l'installation de systèmes d'éclairage et de signalisation pour chaussées, voies ferrées, aéroports et installations portuaires (y compris l'installation de panneaux de signalisation)",
            Category.CLASS,
        ),
        Classification("4534002", "l'installation de stores et bannes", Category.CLASS),
        Classification("4534003", "l'installation d'enseignes, lumineuses ou non", Category.CLASS),
        Classification(
            "4534004", "autres travaux d'installation n.d.a., y compris l'installation d'accessoires", Category.CLASS
        ),
        Classification("4534005", "travaux d'installation générale", Category.CLASS),
        Classification("45410", "Plâtrerie", Category.CLASS),
        Classification(
            "4541001",
            "l'application dans des bâtiments ou d'autres projets de construction, de plâtre ou de stuc pour l'intérieur ou l'extérieur, y compris les matériaux de lattage associés",
            Category.CLASS,
        ),
        Classification("4541002", "le montage de cloisons sèches à base de plâtre", Category.CLASS),
        Classification("45421", "Menuiserie en bois ou en matières plastiques", Category.CLASS),
        Classification(
            "4542101",
            "le montage de menuiseries extérieures et intérieures:portes, fenêtres, escaliers, placards, cuisines équipées, équipements pour magasins, dormants de portes et fenêtres, etc.",
            Category.CLASS,
        ),
        Classification(
            "4542102", "le montage de cloisons mobiles; le revêtement de murs, de plafonds, etc.", Category.CLASS
        ),
        Classification(
            "4542103",
            "le montage de portes de garage, de volets, de persiennes, de grillages, de grilles, etc.",
            Category.CLASS,
        ),
        Classification("4542104", "le montage de portes blindées et de portes coupe-feux", Category.CLASS),
        Classification("4542105", "le montage de serres, de vérandas, etc.", Category.CLASS),
        Classification("45422", "Menuiserie métallique", Category.CLASS),
        Classification(
            "4542201",
            "le montage de menuiseries extérieurs et intérieurs métallique: portes, fenêtres, dormants de portes et fenêtres, escaliers, placards, cuisines équipées, équipements pour magasins, etc.",
            Category.CLASS,
        ),
        Classification(
            "4542202",
            "le montage de cloisons mobiles; le revêtement de murs, de plafonds, etc., métallique",
            Category.CLASS,
        ),
        Classification(
            "4542203",
            "le montage de portes de garage, de volets, de persiennes, de grillages, de grilles, etc., métallique",
            Category.CLASS,
        ),
        Classification("4542204", "le montage de portes blindées et portes coupe-feux, métallique", Category.CLASS),
        Classification("4542205", "le montage de serres, de vérandas, etc., métallique", Category.CLASS),
        Classification(
            "4542206", "Montage de menuiseries extérieures et intérieures en matière plastique", Category.CLASS
        ),
        Classification(
            "4542207", "Commerce de détail de châssis de fenêtres métalliques ou plastiques", Category.CLASS
        ),
        Classification("45431", "Pose de carrelages", Category.CLASS),
        Classification(
            "4543101",
            "la pose dans des bâtiments ou d'autres projets de construction des éléments suivants: revêtements muraux ou carrelages en céramique, en béton ou en pierre de taille,revêtements de sols et de murs en g",
            Category.CLASS,
        ),
        Classification("45432", "Pose de revêtements de sol en bois ou en d'autres matériaux", Category.CLASS),
        Classification(
            "4543201",
            "la pose dans des bâtiments ou d'autres projets de construction des éléments suivants: parquets et autres revêtements de sols en bois; moquettes et revêtements de sols en linoléum, y compris en caoutch",
            Category.CLASS,
        ),
        Classification("45433", "Pose de papiers peints", Category.CLASS),
        Classification("4543301", "pose de papier peints", Category.CLASS),
        Classification("45441", "Peinture", Category.CLASS),
        Classification("4544101", "la peinture intérieure et extérieure des bâtiments", Category.CLASS),
        Classification("4544102", "le traitement des murs avec des produits hydrofuges", Category.CLASS),
        Classification("4544103", "la peinture d'ossatures métalliques", Category.CLASS),
        Classification(
            "4544104", "la peinture de navires et de bateaux par des unités non spécialisées", Category.CLASS
        ),
        Classification("45442", "Vitrerie", Category.CLASS),
        Classification("4544201", "la pose de vitres, de miroirs, etc.", Category.CLASS),
        Classification(
            "4544202", "l'installation de portes intérieures, de cloisons de séparation, ..., en verre", Category.CLASS
        ),
        Classification("45450", "Autres travaux de finition", Category.CLASS),
        Classification("4545001", "l'installation de piscines privées", Category.CLASS),
        Classification(
            "4545002",
            "le nettoyage à la vapeur, le sablage et les activités analogues appliquées aux parties extérieures des bâtiments",
            Category.CLASS,
        ),
        Classification(
            "4545003", "le nettoyage de bâtiments nouveaux et la remise en état des lieux après travaux", Category.CLASS
        ),
        Classification(
            "4545004", "les autres travaux d'achèvement et de finition des bâtiments n.d.a.", Category.CLASS
        ),
        Classification("45500", "Location avec opérateur de matériel de construction", Category.CLASS),
        Classification("4550001", "location avec opérateur de matériel de construction", Category.CLASS),
        Classification("50101", "Commerce de gros des véhicules automobiles", Category.CLASS),
        Classification(
            "5010101",
            "commerce de gros de véhicules automobiles pour le transport des personnes, y compris les véhicules automobiles spéciaux (p.ex. ambulances), neufs ou usagés",
            Category.CLASS,
        ),
        Classification(
            "5010102",
            "commerce de gros de camions,tracteurs routiers,camionnettes, véhicules automobiles tous terrains (p.ex. jeeps), etc., neufs ou usagés",
            Category.CLASS,
        ),
        Classification(
            "5010103",
            "commerce de gros d'autobus, autocars, minibus, motorhomes, etc., neufs ou usagés",
            Category.CLASS,
        ),
        Classification("50102", "Intermédiaires du commerce en véhicules automobiles", Category.CLASS),
        Classification(
            "5010201",
            "intermédiaires du commerce en véhicules automobiles pour le transport des personnes, y compris les véhicules automobiles spéciaux (p.ex. ambulances), neufs ou usagés",
            Category.CLASS,
        ),
        Classification(
            "5010202",
            "intermédiaires du commerce en camions, tracteurs routiers, camionnettes, véhicules automobiles tous terrains (p.ex. jeeps), etc, neufs ou usagés",
            Category.CLASS,
        ),
        Classification(
            "5010203",
            "intermédiaires du commerce en autobus, autocars, minibus, motorhomes, etc., neufs ou usagés",
            Category.CLASS,
        ),
        Classification("50103", "Commerce de détail de véhicules automobiles", Category.CLASS),
        Classification(
            "5010301",
            "commerce de détail de véhicules automobiles pour le transport des personnes, y compris les véhicules automobiles spéciaux (p.ex. ambulances), neufs ou usagés",
            Category.CLASS,
        ),
        Classification(
            "5010302",
            "commerce de détail de camions, tracteurs routiers, camionnettes, véhicules automobiles tous terrains (p.ex. jeeps), etc., neufs ou usagés",
            Category.CLASS,
        ),
        Classification(
            "5010303",
            "commerce de détail d'autobus, autocars, minibus, motorhomes, etc., neufs ou usagés",
            Category.CLASS,
        ),
        Classification("50104", "Commerce de remorques, semi-remorques, caravanes et similaires", Category.CLASS),
        Classification("5010401", "le commerce de remorques et semi-remorques neuves ou usagés", Category.CLASS),
        Classification(
            "5010402",
            "le commerce de véhicules neufs ou usagés pour le camping tels que caravanes, camping cars, etc.",
            Category.CLASS,
        ),
        Classification("50200", "Entretien et réparation de véhicules automobiles", Category.CLASS),
        Classification(
            "5020001",
            "la réparation de véhicules automobiles: réparation de parties mécaniques, réparation électrique",
            Category.CLASS,
        ),
        Classification(
            "5020002", "réparation de la carrosserie (y compris la peinture et la peinture au pistolet)", Category.CLASS
        ),
        Classification("5020003", "la révision du moteur des véhicules automobiles", Category.CLASS),
        Classification(
            "5020004",
            "l'entretien courant des véhicules automobiles: lavage, traitement antirouille, vidange, réparation, pose ou remplacement de pneumatiques et de chambres à air, réparation de pare-brises et de vitres, e",
            Category.CLASS,
        ),
        Classification(
            "5020005", "le montage de pièces et d'accessoires, y compris les travaux de transformation", Category.CLASS
        ),
        Classification("5020006", "le remorquage et le dépannage routier", Category.CLASS),
        Classification(
            "50301", "Commerce de gros de pièces détachées et accessoires pour véhicules automobiles", Category.CLASS
        ),
        Classification(
            "5030101",
            "le commerce de gros d'accessoires, de pièces détachées et d'équipements divers pour véhicules automobiles, y compris la vente de gros de pièces détachées et d'équipements automobiles d'occasion",
            Category.CLASS,
        ),
        Classification("5030102", "le commerce de gros de pneumatiques", Category.CLASS),
        Classification(
            "50302", "Commerce de détail de pièces détachées et accessoires pour véhicules automobiles", Category.CLASS
        ),
        Classification(
            "5030201",
            "commerce de détail d'accessoires, de pièces détachées et d'équipements divers pour véhicules automobiles, y compris la vente de détail de pièces détachées et d'équipements automobiles d'occasion",
            Category.CLASS,
        ),
        Classification("5030202", "commerce de détail de pneumatiques", Category.CLASS),
        Classification(
            "5030203",
            "le commerce de détail spécialisé dans la vente d'équipements automobiles sur catalogue",
            Category.CLASS,
        ),
        Classification(
            "50400", "Commerce, entretien et réparation de motocycles, y compris pièces et accessoires", Category.CLASS
        ),
        Classification(
            "5040001",
            "l'intermédiation de commerce de motocycles, neufs ou usagés, y compris les cyclomoteurs",
            Category.CLASS,
        ),
        Classification("5040002", "commerce de gros de motocycles, neufs ou usagés", Category.CLASS),
        Classification("5040003", "le commerce de gros de cyclomoteurs, neufs ou usagés", Category.CLASS),
        Classification("5040004", "le commerce de gros de pièces et d'accessoires de motocycles", Category.CLASS),
        Classification("5040005", "le commerce de détail de motocycles, neufs ou usagés", Category.CLASS),
        Classification("5040006", "le commerce de détail de cyclomoteurs, neufs ou usagés", Category.CLASS),
        Classification("5040007", "le commerce de détail de pièces et d'accessoires de motocycles", Category.CLASS),
        Classification("5040008", "l'entretien et la réparation de motocycles", Category.CLASS),
        Classification("5040009", "l'entretien et la réparation de cyclomoteurs", Category.CLASS),
        Classification("50500", "Commerce de détail de carburants", Category.CLASS),
        Classification(
            "5050001",
            "le commerce de détail de carburants (y compris le GPL) pour véhicules automobiles et motocycles",
            Category.CLASS,
        ),
        Classification(
            "5050002",
            "le commerce de détail de lubrifiants et de produits de refroidissement pour véhicules automobiles",
            Category.CLASS,
        ),
        Classification(
            "51110",
            "Intermédiaires du commerce en matières premières agricoles, animaux vivants, matières premières textiles et demi-produits",
            Category.CLASS,
        ),
        Classification(
            "5111001",
            "intermédiaires du commerce en matières premières agricoles, animaux vivants, matières premières textiles et demi-produits associés",
            Category.CLASS,
        ),
        Classification(
            "51120",
            "Intermédiaires du commerce en combustibles, minéraux, métaux et produits chimiques",
            Category.CLASS,
        ),
        Classification(
            "5112001",
            "intermédiaires du commerce en combustibles, minéraux, métaux et produits chimiques",
            Category.CLASS,
        ),
        Classification(
            "5112002",
            "les intermédiaires du commerce en engrais, produits phytosanitaires et produits chimiques à usage agricole",
            Category.CLASS,
        ),
        Classification("51130", "Intermédiaires du commerce en bois et matériaux de construction", Category.CLASS),
        Classification("5113001", "intermédiaires du commerce en bois et matériaux de construction", Category.CLASS),
        Classification("5113002", "intermédiaires du commerce en peintures et vernis", Category.CLASS),
        Classification("5113003", "intermédiaires du commerce en articles sanitaires", Category.CLASS),
        Classification(
            "51140",
            "Intermédiaires du commerce en machines, équipements industriels et commerciaux, navires et avions",
            Category.CLASS,
        ),
        Classification(
            "5114001",
            "intermédiaires du commerce en machines, équipements industriels et commerciaux, navires et avions",
            Category.CLASS,
        ),
        Classification("5114002", "intermédiaires du commerce en machines pour la construction", Category.CLASS),
        Classification(
            "5114003",
            "intermédiaires du commerce en machines à coudre et machines et métiers à bonneterie",
            Category.CLASS,
        ),
        Classification(
            "5114004", "intermédiaires du commerce en machines, tracteurs et matériel agricoles", Category.CLASS
        ),
        Classification(
            "5114005",
            "intermédiaires du commerce en matériel électrique et électronique, y compris le matériel d'installation à usage industriel",
            Category.CLASS,
        ),
        Classification(
            "5114006",
            "intermédiaires du commerce en machines et équipements utilisés dans le secteur de services",
            Category.CLASS,
        ),
        Classification(
            "51150", "Intermédiaires du commerce en meubles, articles de ménage et quincaillerie", Category.CLASS
        ),
        Classification(
            "5115001", "intermédiaires du commerce en meubles, articles de ménage et quincaillerie", Category.CLASS
        ),
        Classification(
            "5115002",
            "intermédiaires du commerce en appareils audio-vidéo, matériel photographique et cinématographique et articles d'optique",
            Category.CLASS,
        ),
        Classification(
            "5115003",
            "intermédiaires du commerce en fournitures pour plomberie, matériels d'installation électrique à usage domestique et installations de chauffage",
            Category.CLASS,
        ),
        Classification(
            "5115004",
            "intermédiaires du commerce en articles en porcelaine, verrerie, papiers peints et revêtements de sol",
            Category.CLASS,
        ),
        Classification(
            "5115005",
            "intermédiaires du commerce en parfums, cosmétiques, articles de toilette et produits de nettoyage",
            Category.CLASS,
        ),
        Classification(
            "5115006",
            "intermédiaires du commerce en produits pharmaceutiques et articles orthopédiques",
            Category.CLASS,
        ),
        Classification(
            "5115007",
            "intermédiaires du commerce en articles de papeterie, journaux, livres et magazines",
            Category.CLASS,
        ),
        Classification(
            "5115008", "intermédiaires du commerce en montres, articles en métaux précieux et bijoux", Category.CLASS
        ),
        Classification(
            "5115009",
            "intermédiaires du commerce en articles de sport et matériel de camping, jeux et jouets",
            Category.CLASS,
        ),
        Classification(
            "51160",
            "Intermédiaires du commerce en textiles, habillement, chaussures et articles en cuir",
            Category.CLASS,
        ),
        Classification(
            "5116001",
            "intermédiaires du commerce en textiles, habillement, chaussures et articles en cuir",
            Category.CLASS,
        ),
        Classification("5116002", "intermédiaires du commerce en fourrures", Category.CLASS),
        Classification(
            "51170", "Intermédiaires du commerce en denrées alimentaires, en boissons et en tabac", Category.CLASS
        ),
        Classification("5117001", "intermédiaires du commerce en denrées alimentaires et en tabac", Category.CLASS),
        Classification("51180", "Autres intermédiaires spécialisés du commerce", Category.CLASS),
        Classification("5118001", "autres intermédiaires spécialisés du commerce n.d.a.", Category.CLASS),
        Classification("51190", "Intermédiaires du commerce en produits divers", Category.CLASS),
        Classification("5119001", "intermédiaires non spécialisés du commerce", Category.CLASS),
        Classification("51210", "Commerce de gros de céréales, semences et aliments pour le bétail", Category.CLASS),
        Classification("5121001", "commerce de gros de céréales, semences et aliments pour animaux", Category.CLASS),
        Classification("5121002", "le commerce de gros d'huiles et de graisses non comestibles", Category.CLASS),
        Classification("5121003", "le commerce de gros de pommes de terre de semence", Category.CLASS),
        Classification("5121004", "le commerce de gros de bulbes de tulipes", Category.CLASS),
        Classification("5121005", "le commerce de gros d'aliments pour animaux de ferme", Category.CLASS),
        Classification("51220", "Commerce de gros de fleurs et plantes", Category.CLASS),
        Classification("5122001", "commerce de gros de fleurs et plantes", Category.CLASS),
        Classification("51230", "Commerce de gros d'animaux vivants", Category.CLASS),
        Classification("5123001", "commerce de gros d'animaux vivants", Category.CLASS),
        Classification("51240", "Commerce de gros de cuirs et peaux", Category.CLASS),
        Classification("5124001", "le commerce de gros de cuirs et de peaux", Category.CLASS),
        Classification("51250", "Commerce de gros de tabac non manufacturé", Category.CLASS),
        Classification("5125001", "commerce de gros de tabac non manufacturé", Category.CLASS),
        Classification("51310", "Commerce de gros de fruits et légumes", Category.CLASS),
        Classification(
            "5131001",
            "commerce de gros de fruits et de légumes frais et en l'état, y compris les pommes de terre",
            Category.CLASS,
        ),
        Classification(
            "51321",
            "Commerce de gros de viande et de produits à base de viande et de charcuterie à l'exclusion de viande de volailles et de gibiers",
            Category.CLASS,
        ),
        Classification(
            "5132101",
            "commerce de gros de viande et de produits à base de viande, à l'exclusion de viande de volailles et de gibiers",
            Category.CLASS,
        ),
        Classification("51322", "Commerce de gros de viande de volailles et de gibiers", Category.CLASS),
        Classification("5132201", "commerce de gros de viande de volailles et de gibiers", Category.CLASS),
        Classification("5132202", "le commerce de gros de viande de lapins", Category.CLASS),
        Classification("51331", "Commerce de gros de produits laitiers et oeufs", Category.CLASS),
        Classification(
            "5133101", "le commerce de gros de produits laitiers (lait, beurre, fromage, etc.)", Category.CLASS
        ),
        Classification("5133102", "le commerce de gros d'oeufs et de produits à base d'oeufs", Category.CLASS),
        Classification("51332", "Commerce de gros d'huiles et de graisses comestibles", Category.CLASS),
        Classification(
            "5133201",
            "le commerce de gros d'huiles et de graisses comestibles d'origine animale et végétale",
            Category.CLASS,
        ),
        Classification("51340", "Commerce de gros de boissons", Category.CLASS),
        Classification("5134001", "le commerce de gros de toutes boissons, alcoolisées ou non", Category.CLASS),
        Classification(
            "5134002",
            "le mélange, la purification et la mise en bouteilles pour compte propre de vins achetés en vrac",
            Category.CLASS,
        ),
        Classification("51350", "Commerce de gros de tabac", Category.CLASS),
        Classification("5135001", "le commerce de gros de tabac", Category.CLASS),
        Classification("51360", "Commerce de gros de sucre, chocolat, confiserie", Category.CLASS),
        Classification("5136001", "commerce de gros de sucre, chocolat, confiserie", Category.CLASS),
        Classification("51370", "Commerce de gros de café, thé, cacao, épices", Category.CLASS),
        Classification("5137001", "le commerce de gros de café, thé, cacao, épices", Category.CLASS),
        Classification("51381", "Commerce de gros de poissons, crustacés et coquillages", Category.CLASS),
        Classification("5138101", "le commerce de gros de poissons, crustacés et coquillages", Category.CLASS),
        Classification("51382", "Commerce de gros de produits à base de pommes de terre", Category.CLASS),
        Classification("5138201", "commerce de gros de produits à base de pommes de terre", Category.CLASS),
        Classification("51383", "Commerce de gros d'aliments pour animaux de compagnie", Category.CLASS),
        Classification("5138301", "le commerce de gros d'aliments pour animaux domestiques", Category.CLASS),
        Classification("51384", "Autres commerces de gros alimentaires spécialisés", Category.CLASS),
        Classification("5138401", "le commerce de gros de farines et produits pour la boulangerie", Category.CLASS),
        Classification("5138402", "le commerce de plats cuisinés frais et prêts à emporter", Category.CLASS),
        Classification("5138403", "le commerce de gros de conserves", Category.CLASS),
        Classification("5138404", "le commerce de gros de confitures et de miel", Category.CLASS),
        Classification("5138405", "le commerce de gros pâtes alimentaires et de riz", Category.CLASS),
        Classification("5138406", "le commerce de gros de desserts", Category.CLASS),
        Classification("5138407", "les autres commerces de gros alimentaires spécialisés n.d.a.", Category.CLASS),
        Classification("51391", "Commerce de gros de produits surgelés", Category.CLASS),
        Classification(
            "5139101",
            "le commerce de gros d'une gamme de produits alimentaires surgelés: viandes et charcuteries, volailles et gibiers, poissons et crustacés, fruits et légumes, plats cuisinés, desserts, glaces de consomma",
            Category.CLASS,
        ),
        Classification("51392", "Autres commerces de gros non spécialisés de produits alimentaires", Category.CLASS),
        Classification("5139201", "autres commerces de gros non spécialisés de produits alimentaires", Category.CLASS),
        Classification("51410", "Commerce de gros de textiles", Category.CLASS),
        Classification("5141001", "le commerce de gros de fils", Category.CLASS),
        Classification("5141002", "le commerce de gros de tissus et d'étoffes", Category.CLASS),
        Classification("5141003", "le commerce de gros de linge de maison et de literie", Category.CLASS),
        Classification("5141004", "le commerce de gros de bâches, housses, parasols, stores, etc.", Category.CLASS),
        Classification(
            "5141005", "le commerce de gros d'articles de mercerie: aiguilles, fils, rubans, etc.", Category.CLASS
        ),
        Classification(
            "51421",
            "Commerce de gros d'habillement, d'accessoires d'habillement et d'articles en fourrure",
            Category.CLASS,
        ),
        Classification(
            "5142101", "le commerce de gros d'articles d'habillement, y compris les vêtements de sport", Category.CLASS
        ),
        Classification("5142102", "le commerce de gros d'articles en fourrure", Category.CLASS),
        Classification(
            "5142103",
            "le commerce de gros d'accessoires du vêtement tels que gants, cravates, ceintures, parapluies, etc.",
            Category.CLASS,
        ),
        Classification("51422", "Commerce de gros de chaussures", Category.CLASS),
        Classification("5142201", "le commerce de gros de chaussures", Category.CLASS),
        Classification(
            "51430", "Commerce de gros d'appareils électroménagers, de radio et de télévision", Category.CLASS
        ),
        Classification("5143001", "le commerce de gros d'appareils électroménagers", Category.CLASS),
        Classification(
            "5143002",
            "le commerce de gros d'appareils audio et vidéo: radio, télévision, chaînes, magnétoscopes, etc.",
            Category.CLASS,
        ),
        Classification(
            "5143003",
            "le commerce de gros de disques, de disques compacts,d'audiocassettes et de vidéocassettes enregistrés ou non",
            Category.CLASS,
        ),
        Classification("5143004", "le commerce de gros d'appareils d'éclairage", Category.CLASS),
        Classification(
            "5143005", "le commerce de gros de matériels électriques d'installation à usage domestique", Category.CLASS
        ),
        Classification("51441", "Commerce de gros de vaisselle et de verrerie de ménage", Category.CLASS),
        Classification("5144101", "le commerce de gros de vaisselle et de verrerie de ménage", Category.CLASS),
        Classification(
            "5144102",
            "le commerce de gros de couverts et d'articles métalliques de table et de cuisine",
            Category.CLASS,
        ),
        Classification("51442", "Commerce de gros de papiers peints et de produits d'entretien", Category.CLASS),
        Classification("5144201", "le commerce de gros de papier peints et de revêtements muraux", Category.CLASS),
        Classification(
            "5144202",
            "le commerce de gros de produits d'entretien et de nettoyage, y compris les poudres de lessive",
            Category.CLASS,
        ),
        Classification("51450", "Commerce de gros de parfumerie et de produits de beauté", Category.CLASS),
        Classification("5145001", "le commerce de gros de parfumeries et de cosmétiques", Category.CLASS),
        Classification("5145002", "le commerce de gros de produits d'hygiène", Category.CLASS),
        Classification("51460", "Commerce de gros de produits pharmaceutiques", Category.CLASS),
        Classification("5146001", "le commerce de gros de produits pharmaceutiques", Category.CLASS),
        Classification(
            "5146002", "le commerce de gros de matériel médiochirurgical et de fournitures dentaires", Category.CLASS
        ),
        Classification("5146003", "le commerce de gros d'articles d'orthopédie", Category.CLASS),
        Classification(
            "51471",
            "Commerce de gros de meubles, d'appareils ménagers non électriques et de revêtements de sol, y compris les tapis",
            Category.CLASS,
        ),
        Classification(
            "5147101",
            "le commerce de gros de meubles, d'appareils ménagers non-électriques et de revêtements de sol, y compris les tapis",
            Category.CLASS,
        ),
        Classification("51472", "Commerce de gros de journaux, livres et périodiques", Category.CLASS),
        Classification("5147201", "le commerce de gros de journaux, livres et périodiques", Category.CLASS),
        Classification(
            "51473",
            "Commerce de gros d'appareils photographiques, cinématographiques et d'autres articles d'optique",
            Category.CLASS,
        ),
        Classification(
            "5147301",
            "le commerce de gros d'appareils photographiques, cinématographiques et d'autres articles d'optique",
            Category.CLASS,
        ),
        Classification(
            "51474", "Commerce de gros d'horlogerie, d'articles en métaux précieux et de bijoux", Category.CLASS
        ),
        Classification(
            "5147401", "le commerce de gros d'horlogerie, d'articles en métaux précieux et de bijoux", Category.CLASS
        ),
        Classification(
            "51475",
            "Commerce de gros d'articles de papeterie, de fournitures de bureau et de fournitures scolaires",
            Category.CLASS,
        ),
        Classification(
            "5147501",
            "le commerce de gros d'articles de papeterie, de fournitures de bureau et de fournitures scolaires",
            Category.CLASS,
        ),
        Classification(
            "51476",
            "Commerce de gros d'articles de sport et de camping, de cycles et de leurs pièces et accessoires, de jeux et de jouets",
            Category.CLASS,
        ),
        Classification(
            "5147601",
            "le commerce de gros d'articles de sport et de camping, de cycles etde leurs pieces et accessoires, de jeux et de jouets",
            Category.CLASS,
        ),
        Classification("51477", "Commerce de gros de maroquinerie et d'articles de voyage", Category.CLASS),
        Classification("5147701", "le commerce de gros de maroquinerie et d'articles de voyage", Category.CLASS),
        Classification("51478", "Autres commerces de gros d'articles de consommation n.d.a.", Category.CLASS),
        Classification("5147801", "le commerce de gros d'instruments de musique", Category.CLASS),
        Classification("5147802", "le commerce de gros d'ouvrages en bois, en osier ou en liège", Category.CLASS),
        Classification("5147803", "les autres commerces de gros d'articles de consommation n.d.a.", Category.CLASS),
        Classification("51510", "Commerce de gros de combustibles et de produits dérivés", Category.CLASS),
        Classification("5151001", "le commerce de gros de combustibles solides, liquides et gazeux", Category.CLASS),
        Classification("5151002", "le commerce de gros de combustibles nucléaires", Category.CLASS),
        Classification(
            "5151003", "le commerce de gros de carburants, graisses, lubrifiants, huiles, etc.", Category.CLASS
        ),
        Classification("51520", "Commerce de gros de métaux et minerais", Category.CLASS),
        Classification("5152001", "le commerce de gros de minerais métalliques ferreux et non ferreux", Category.CLASS),
        Classification(
            "5152002",
            "le commerce de gros de métaux ferreux et non ferreux sous formes primaires, y compris l'or et les autres métaux précieux",
            Category.CLASS,
        ),
        Classification(
            "5152003", "le commerce de gros de demi-produits en métaux ferreux et non ferreux", Category.CLASS
        ),
        Classification("51531", "Commerce de gros de bois", Category.CLASS),
        Classification("5153101", "le commerce de gros de bois brut", Category.CLASS),
        Classification(
            "5153102", "le commerce de gros de produits de la transformation primaire du bois", Category.CLASS
        ),
        Classification("5153103", "le commerce de gros de panneaux, parquets, lambris, etc.", Category.CLASS),
        Classification(
            "5153104", "le commerce de gros de menuiseries et fermetures de bâtiment en bois", Category.CLASS
        ),
        Classification(
            "51532",
            "Commerce de gros de peintures, vernis et matériaux de construction, y compris les appareils sanitaires",
            Category.CLASS,
        ),
        Classification("5153201", "le commerce de gros de peintures et de vernis", Category.CLASS),
        Classification(
            "5153202",
            "le commerce de gros de matériaux de construction: sable, gravier, ciment, briques, etc.",
            Category.CLASS,
        ),
        Classification("5153203", "le commerce de gros de verre plat", Category.CLASS),
        Classification(
            "5153204",
            "le commerce de gros d'appareils sanitaires: baignoires, lavabos, cuvettes d'aisance, etc.",
            Category.CLASS,
        ),
        Classification(
            "5153205", "le commerce de gros de menuiseries et fermetures de bâtiment autres qu'en bois", Category.CLASS
        ),
        Classification("51541", "Commerce de gros de quincaillerie", Category.CLASS),
        Classification(
            "5154101",
            "le commerce de gros de quincaillerie générale (clous, fils, visserie, boulonnerie, etc.), d'outils à main (marteaux, scies, tournevis, etc.) et d'outillage électroportatif",
            Category.CLASS,
        ),
        Classification(
            "5154102",
            "le commerce de gros de quincaillerie d'ameublement et de bâtiment: serrures, clés, charnières, etc.",
            Category.CLASS,
        ),
        Classification("5154103", "le commerce de gros d'ustensiles de ménage métalliques", Category.CLASS),
        Classification(
            "51542", "Commerce de gros de fournitures et équipements pour plomberie et chauffage", Category.CLASS
        ),
        Classification("5154201", "le commerce de gros d'appareils de chauffage central", Category.CLASS),
        Classification(
            "5154202",
            "le commerce de gros de fournitures pour installations sanitaires et chauffage central: tubes, tuyaux, raccords de tuyauterie, robinets, tuyaux en caoutchouc, etc.",
            Category.CLASS,
        ),
        Classification("51550", "Commerce de gros de produits chimiques", Category.CLASS),
        Classification(
            "5155001",
            "le commerce de gros de produits chimiques industriels: aniline,encres d'imprimerie,huiles essentielles,gaz industriels ,colles chimiques,colorants,résine synthétiques,méthanol, paraffine,parfums,essen",
            Category.CLASS,
        ),
        Classification(
            "5155002", "le commerce de gros d'engrais et de produits phytosanitaires à usage agricole", Category.CLASS
        ),
        Classification("5155003", "le commerce de gros de matières plastiques sous formes primaires", Category.CLASS),
        Classification("5155004", "le commerce de gros caoutchouc brut", Category.CLASS),
        Classification("5155005", "le commerce de gros de produits de nettoyage à usage industriel", Category.CLASS),
        Classification("51561", "Commerce de gros de diamants", Category.CLASS),
        Classification("5156101", "le commerce de gros de diamants bruts et de diamants façonnés", Category.CLASS),
        Classification("5156102", "le commerce de gros d'autres pierres précieuses et semi-précieuses", Category.CLASS),
        Classification("51562", "Commerce de gros d'autres produits intermédiaires n.d.a.", Category.CLASS),
        Classification(
            "5156201", "le commerce de gros de matières premières textiles et de fibres textiles", Category.CLASS
        ),
        Classification(
            "5156202",
            "le commerce de gros de papiers et cartons destinés à faire l'objet d'une transformation ultérieure par l'industrie",
            Category.CLASS,
        ),
        Classification("5156203", "le commerce de gros d'autres produits intermédiaires n.d.a.", Category.CLASS),
        Classification("51570", "Commerce de gros de déchets et débris", Category.CLASS),
        Classification(
            "5157001",
            "le commerce de gros de déchets, de débris et de matériaux de récupération, métalliques et non métalliques",
            Category.CLASS,
        ),
        Classification("51610", "Commerce de gros de machines-outils", Category.CLASS),
        Classification("5161001", "le commerce de gros de machines-outils", Category.CLASS),
        Classification("5161002", "le commerce de gros de machines-outils commandées par ordinateur", Category.CLASS),
        Classification("51620", "Commerce de gros d'équipements pour la construction", Category.CLASS),
        Classification(
            "5162001", "le commerce de gros de matériel de chantier, grues, engins de génie civil, etc.", Category.CLASS
        ),
        Classification("5162002", "le commerce de gros d'outillage mécanique pour la construction", Category.CLASS),
        Classification(
            "51630",
            "Commerce de gros de machines pour l'industrie textile et l'habillement, de machines à coudre et à tricoter",
            Category.CLASS,
        ),
        Classification(
            "5163001",
            "le commerce de gros de machines pour l'industrie textile et l'habillement, de machines à coudre et à tricoter",
            Category.CLASS,
        ),
        Classification(
            "5163002",
            "le commerce de gros de machines pour l'industrie textile et de machines à coudre et à tricoter, commandées par ordinateur",
            Category.CLASS,
        ),
        Classification("51640", "Commerce de gros de machines et matériel de bureau", Category.CLASS),
        Classification("5164001", "le commerce de gros d'ordinateurs et de matériels périphériques", Category.CLASS),
        Classification(
            "5164002",
            "le commerce de gros d'autres machines et matériels de bureau tels que machines à écrire, machines à calculer, etc.",
            Category.CLASS,
        ),
        Classification("5164003", "le commerce de gros de mobilier de bureau", Category.CLASS),
        Classification(
            "51651",
            "Commerce de gros de matériel électrique et électronique, y compris le matériel d'installation",
            Category.CLASS,
        ),
        Classification(
            "5165101",
            "le commerce de gros de fils, de câbles, d'interrupteurs et d'autres matériels d'installation à usage industriel",
            Category.CLASS,
        ),
        Classification(
            "5165102",
            "le commerce de gros d'autres matériels électriques et électroniques, tels les électromoteurs, les transformateurs, les tableaux de commande et les composants électroniques",
            Category.CLASS,
        ),
        Classification(
            "51652", "Commerce de gros de fournitures et d'équipements divers pour l'industrie n.d.a.", Category.CLASS
        ),
        Classification("5165201", "le commerce de gros de matériel de levage et de manutention", Category.CLASS),
        Classification("5165202", "le commerce de gros de robots industriels", Category.CLASS),
        Classification(
            "5165203", "le commerce de gros d'instruments et d'appareils de mesure et de navigation", Category.CLASS
        ),
        Classification("5165204", "le commerce de gros de matériel de garage et de soudage", Category.CLASS),
        Classification("5165205", "le commerce de gros d'engrenages et d'organes de transmission", Category.CLASS),
        Classification(
            "5165206",
            "le commerce de gros d'articles de caoutchouc ou en matières plastiques à usage technique",
            Category.CLASS,
        ),
        Classification(
            "5165207",
            "le commerce de gros d'autres machines et équipements n.d.a. utilisés dans l'industrie",
            Category.CLASS,
        ),
        Classification(
            "51653",
            "Commerce de gros de fournitures et d'équipements divers pour le commerce et les services n.d.a.",
            Category.CLASS,
        ),
        Classification(
            "5165301",
            "le commerce de gros d'équipements de magasin (présentoirs, vitrines amovibles, mannequins, etc.)",
            Category.CLASS,
        ),
        Classification("5165302", "le commerce de gros de machines automatiques de vente de produits", Category.CLASS),
        Classification(
            "5165303", "le commerce de gros d'équipements pour hôtels, cafés et restaurants", Category.CLASS
        ),
        Classification(
            "5165304",
            "le commerce de gros de jeux automatiques et électroniques pour cafés, casinos, lunaparcs, etc.",
            Category.CLASS,
        ),
        Classification(
            "5165305",
            "le commerce de gros d'autres machines et équipements n.d.a. utilisés dans le commerce et les services",
            Category.CLASS,
        ),
        Classification("51660", "Commerce de gros de machines, matériels et tracteurs agricoles", Category.CLASS),
        Classification("5166001", "commerce de gros de machines, matériels et tracteurs agricoles", Category.CLASS),
        Classification("5166002", "le commerce de gros de tondeuses à gazon, de tout type", Category.CLASS),
        Classification("5166003", "le commerce de gros de motoculteurs", Category.CLASS),
        Classification("51700", "Autres commerces de gros", Category.CLASS),
        Classification(
            "5170001",
            "les divers commerces de gros spécialisés ne relevant pas d'une des catégories précédentes (p.ex. le commerce de gros de cordages, de cordes,de ficelles et d'articles similaires, le commerce de gros de",
            Category.CLASS,
        ),
        Classification(
            "5170002",
            "le commerce de gros de divers produits et articles sans spécialisation particulière, tel l'approvisionnement des navires p.ex.(shipchandlers)",
            Category.CLASS,
        ),
        Classification("51810", "Commerce de gros de machines-outils", Category.CLASS),
        Classification(
            "51820", "Commerce de gros de machines pour l'extraction, la construction et le génie civil", Category.CLASS
        ),
        Classification(
            "51830",
            "Commerce de gros de machines pour l'industrie textile et l'habillement, de machines à coudre et à tricoter",
            Category.CLASS,
        ),
        Classification(
            "51840",
            "Commerce de gros d'ordinateurs, d'équipements informatiques périphériques et de logiciels",
            Category.CLASS,
        ),
        Classification("51850", "Commerce de gros d'autres machines et équipements de bureau", Category.CLASS),
        Classification("51860", "Commerce de gros d'autres composants et équipements électroniques", Category.CLASS),
        Classification(
            "51871", "Commerce de gros de matériel électrique y compris le matériel d'installation", Category.CLASS
        ),
        Classification(
            "51872",
            "Commerce de gros de fournitures et d'équipements divers pour l'industrie et de matériels de transport autres que les véhicules automobiles, les cycles et les motocycles",
            Category.CLASS,
        ),
        Classification(
            "51873",
            "Commerce de gros de fournitures et d'équipements divers pour le commerce et les services n.d.a.",
            Category.CLASS,
        ),
        Classification("51880", "Commerce de gros de machines, matériels et tracteurs agricoles", Category.CLASS),
        Classification("51900", "Autres commerces de gros", Category.CLASS),
        Classification("52111", "Commerce de détail non spécialisé en produits surgelés", Category.CLASS),
        Classification(
            "5211101",
            "le commerce de détail en magasin ou par livraison à domicile de tous produits alimentaires surgelés ou congelés, y compris les crèmes glacées",
            Category.CLASS,
        ),
        Classification(
            "52112",
            "Commerce de détail non spécialisé d'alimentation générale (surface de vente inférieure à 100 m2)",
            Category.CLASS,
        ),
        Classification(
            "5211201",
            "commerce de détail non spécialisé d'alimentation générale (surface de vente inférieure à 100 m2)",
            Category.CLASS,
        ),
        Classification("52113", "Supérettes (surface de vente comprise entre 100 et moins de 400 m2)", Category.CLASS),
        Classification("5211301", "superettes (surface de vente comprise entre 100 et 400 m2)", Category.CLASS),
        Classification("52114", "Supermarchés (surface de vente entre 400 et moins de 2.500 m2)", Category.CLASS),
        Classification("5211401", "supermarchés (surface de vente comprise entre 400 et 2500 m2)", Category.CLASS),
        Classification("52115", "Hypermarchés (surface de vente de 2.500 m2 et plus)", Category.CLASS),
        Classification("5211501", "hypermarchés (surface de vente supérieure à 2500 m2)", Category.CLASS),
        Classification(
            "52116", "Autres commerces de détail en magasins non spécialisés à prédominance alimentaire", Category.CLASS
        ),
        Classification(
            "5211601",
            "autres commerces de détail en magasins non spécialisés à prédominance alimentaire",
            Category.CLASS,
        ),
        Classification(
            "52121",
            "Grands magasins (sans prédominance alimentaire et surface de vente de 2.500 m2 et plus)",
            Category.CLASS,
        ),
        Classification(
            "5212101",
            "grand magasin: commerce de détail d'une large gamme de produits sans prédominance de l'alimentation, boissons et tabac tels habillement,meubles,petits appareils,quincaillerie,cosmétiques,joaillerie,jo",
            Category.CLASS,
        ),
        Classification(
            "52122",
            "Autres commerces de détail en magasins non spécialisés (sans prédominance alimentaire et surface de vente inférieure à 2.500 m2)",
            Category.CLASS,
        ),
        Classification(
            "5212201",
            "le commerce de détail d'une large gamme de produits sans prédominance de l'alimentation, boissons et tabac, tels habillement,meubles,petits appareils,quincaillerie,cosmétique,joaillerie,jouets etc. -",
            Category.CLASS,
        ),
        Classification("52210", "Commerce de détail de fruits et légumes frais", Category.CLASS),
        Classification(
            "5221001", "le commerce de détail de fruits et légumes frais, y compris les pommes de terre", Category.CLASS
        ),
        Classification("52220", "Commerce de détail de viandes et produits à base de viande", Category.CLASS),
        Classification(
            "5222001",
            "le commerce de détail de viandes et produits à base de viande exploité par les bouchers/charcutiers",
            Category.CLASS,
        ),
        Classification("5222002", "le commerce de détail de volailles, de lapins et de gibier", Category.CLASS),
        Classification("52230", "Commerce de détail de poissons, crustacés et mollusques", Category.CLASS),
        Classification("5223001", "le commerce de détail de poissons, crustacés et mollusques", Category.CLASS),
        Classification("52240", "Commerce de détail de pain, pâtisserie et confiserie", Category.CLASS),
        Classification("5224001", "le commerce de détail de pain, pâtisserie et confiserie", Category.CLASS),
        Classification("52250", "Commerce de détail de boissons", Category.CLASS),
        Classification(
            "5225001",
            "le commerce de détail de toutes boissons,alcoolisées ou non, y compris la livraison à domicile",
            Category.CLASS,
        ),
        Classification(
            "5225002", "la mise en bouteilles, le mélange et l'épuration du vin sans transformation", Category.CLASS
        ),
        Classification("52260", "Commerce de détail de tabac", Category.CLASS),
        Classification("5226001", "le commerce de détail de tabac", Category.CLASS),
        Classification("52271", "Commerce de détail de produits laitiers et oeufs", Category.CLASS),
        Classification(
            "5227101",
            "le commerce de détail de produits laitiers et oeufs, y compris la livraison à domicile",
            Category.CLASS,
        ),
        Classification(
            "52272", "Autres commerces de détail alimentaires en magasins spécialisés n.d.a.", Category.CLASS
        ),
        Classification("5227201", "le commerce de détail de café", Category.CLASS),
        Classification("5227202", "le commerce de détail de condiments et épices", Category.CLASS),
        Classification("5227203", "le commerce de détail de conserves de fruits et légumes", Category.CLASS),
        Classification(
            "5227204", "les autres commerces de détail alimentaires en magasins spécialisés n.d.a.", Category.CLASS
        ),
        Classification("52310", "Pharmacies", Category.CLASS),
        Classification("5231001", "pharmacies", Category.CLASS),
        Classification("52320", "Commerce de détail d'articles médicaux et orthopédiques", Category.CLASS),
        Classification("5232001", "le commerce de détail d'articles médicaux et orthopédiques", Category.CLASS),
        Classification("5232002", "le commerce de détail d'herboristerie", Category.CLASS),
        Classification("5232003", "le commerce de détail de prothèses et de véhicules pour invalides", Category.CLASS),
        Classification("52330", "Commerce de détail de parfumerie et de produits de beauté", Category.CLASS),
        Classification("5233001", "le commerce de détail de parfumerie et de produits de beauté", Category.CLASS),
        Classification("5233002", "le commerce de détail d'articles de toilette", Category.CLASS),
        Classification("52410", "Commerce de détail de textiles", Category.CLASS),
        Classification("5241001", "le commerce de détail de tissus d'habillement et d'ameublement", Category.CLASS),
        Classification("5241002", "le commerce de détail de fils à tricoter", Category.CLASS),
        Classification(
            "5241003",
            "le commerce de détail de matériaux de base pour la fabrication de tapis, de tapisseries ou de broderies",
            Category.CLASS,
        ),
        Classification(
            "5241004",
            "le commerce de détail d'articles de mercerie: aiguilles, fils à coudre, boutons, lacets, rubans, etc.",
            Category.CLASS,
        ),
        Classification(
            "5241005", "le commerce de détail de bâches, housses, parasols, cabas, etc., en textile", Category.CLASS
        ),
        Classification(
            "5241006",
            "le commerce de détail de textiles à usage domestique tels que draps, couvertures, nappes, serviettes, etc.",
            Category.CLASS,
        ),
        Classification(
            "52421",
            "Commerce de détail de vêtements pour hommes, dames et enfants (assortiment général)",
            Category.CLASS,
        ),
        Classification(
            "5242101",
            "le commerce de détail de vêtements de dessus, y compris les vêtements de travail, de sport et de cérémonie, en toutes matières (tissus textiles,étoffes de bonneterie,cuir,fourrure,etc.) pour hommes, d",
            Category.CLASS,
        ),
        Classification("52422", "Commerce de détail de vêtements pour hommes", Category.CLASS),
        Classification(
            "5242201",
            "le commerce de détail de vêtements de dessus, y compris les vêtements de travail, de sport et de cérémonie, en toutes matières (tissus textiles, étoffes de bonneterie, cuir, fourrure, etc.) pour homme",
            Category.CLASS,
        ),
        Classification("52423", "Commerce de détail de vêtements pour dames", Category.CLASS),
        Classification(
            "5242301",
            "le commerce de détail de vêtements de dessus, y compris les vêtements de travail, de sport et de cérémonie, en toutes matières (tissus textiles, étoffes de bonneterie, cuir, fourrure, etc.) pour dames",
            Category.CLASS,
        ),
        Classification("52424", "Commerce de détail de vêtements pour bébés et enfants", Category.CLASS),
        Classification("5242401", "le commerce de détail de vêtements pour bébés et enfants", Category.CLASS),
        Classification("52425", "Commerce de détail de sous-vêtements, lingerie et vêtements de bain", Category.CLASS),
        Classification(
            "5242501", "le commerce de détail de sous-vêtements, lingerie et de vêtements de bain", Category.CLASS
        ),
        Classification("52426", "Commerce de détail d'accessoires du vêtement", Category.CLASS),
        Classification(
            "5242601", "le commerce de détail de chapeaux, gants, cravates, ceintures, parapluies, etc.", Category.CLASS
        ),
        Classification("52431", "Commerce de détail de chaussures", Category.CLASS),
        Classification("5243101", "le commerce de détail de chaussures", Category.CLASS),
        Classification("52432", "Commerce de détail de maroquinerie et d'articles de voyage", Category.CLASS),
        Classification(
            "5243201",
            "le commerce de détail de maroquinerie et d'accessoires de voyage en cuir ou en cuir synthétique",
            Category.CLASS,
        ),
        Classification("52441", "Commerce de détail de meubles", Category.CLASS),
        Classification("5244101", "le commerce de détail de meubles", Category.CLASS),
        Classification("5244102", "le commerce de détail de cuisines équipées", Category.CLASS),
        Classification(
            "5244103", "le commerce de détail de matelas, sommiers et autres supports de matelas", Category.CLASS
        ),
        Classification("52442", "Commerce de détail d'appareils d'éclairage et d'équipements du foyer", Category.CLASS),
        Classification("5244201", "le commerce de détail d'appareils d'éclairage", Category.CLASS),
        Classification(
            "5244202",
            "le commerce de détail d'appareils ménagers non électriques, de coutellerie, de vaisselle, de verrerie, de porcelaine et de poteries",
            Category.CLASS,
        ),
        Classification(
            "5244203",
            "le commerce de détail de rideaux, vitrages et articles d'ameublement divers en matières textiles",
            Category.CLASS,
        ),
        Classification("5244204", "le commerce de détail d'ouvrages en bois, en liège et en vannerie", Category.CLASS),
        Classification(
            "5244205", "le commerce de détail spécialisé en cadeaux portant sur l'équipement du foyer", Category.CLASS
        ),
        Classification(
            "5244206",
            "le commerce de détail d'appareils et articles de ménage ou d'économie domestique n.d.a.",
            Category.CLASS,
        ),
        Classification(
            "52450", "Commerce de détail d'appareils électroménagers, de radio et de télévision", Category.CLASS
        ),
        Classification("5245001", "le commerce de détail d'appareils électroménagers", Category.CLASS),
        Classification(
            "5245002",
            "le commerce de détail d'appareils de radio et de télévision et d'autres matériels audio/vidéo à usage domestique tels les magnétoscopes, les caméscopes, le matériel hi-fi, etc.",
            Category.CLASS,
        ),
        Classification(
            "5245003",
            "le commerce de détail de disques, de disques compacts, bandes et cassettes audio ou vidéo, vierges ou enregistrées",
            Category.CLASS,
        ),
        Classification(
            "5245004", "le commerce de détail d'instruments de musique et de partitions musicales", Category.CLASS
        ),
        Classification(
            "52461",
            "Commerce de détail de quincaillerie, peintures, matériaux de construction et verre (y compris les bricocenters) avec une surface de vente jusqu'à 400 m2.",
            Category.CLASS,
        ),
        Classification(
            "5246101",
            "le commerce de détail de quincaillerie, peintures et matériaux de construction (y compris les bricocenters) avec une surface de vente moins de 400 m2",
            Category.CLASS,
        ),
        Classification(
            "52462",
            "Commerce de détail de quincaillerie, peintures, matériaux de construction et verre (y compris les bricocenters) avec une surface de vente de plus de 400 m2.",
            Category.CLASS,
        ),
        Classification(
            "5246201",
            "le commerce de détail de quincaillerie, peintures et matériaux de construction (y compris les bricocenters) avec une surface de vente de plus de 400 m2",
            Category.CLASS,
        ),
        Classification("52470", "Commerce de détail de livres, journaux et papeterie", Category.CLASS),
        Classification("5247001", "le commerce de détail de livres, journaux et papeterie", Category.CLASS),
        Classification("5247002", "le commerce de détail de journaux et périodiques en kiosque", Category.CLASS),
        Classification("52481", "Commerce de détail spécialisé de combustibles solides et liquides", Category.CLASS),
        Classification(
            "5248101",
            "le commerce de détail de combustibles solides tels que charbon, bois de chauffage, charbon de bois, etc.",
            Category.CLASS,
        ),
        Classification("5248102", "le commerce de détail de combustibles liquides et gazeux", Category.CLASS),
        Classification(
            "52482", "Commerce de détail spécialisé d'articles de sport et de matériel de camping", Category.CLASS
        ),
        Classification(
            "5248201",
            "le commerce de détail d'articles de sport, de matériel de camping (y compris les tentes) et d'articles pour autres activités de loisir",
            Category.CLASS,
        ),
        Classification(
            "5248202", "le commerce de détail de bateaux de plaisance, planches à voile, voiles, etc.", Category.CLASS
        ),
        Classification(
            "52483", "Commerce de détail spécialisé de fleurs et de plantes, de graines et d'engrais", Category.CLASS
        ),
        Classification(
            "5248301", "le commerce de détail de fleurs, y compris les fleurs coupées, et de plantes", Category.CLASS
        ),
        Classification(
            "5248302", "le commerce de détail de graines, d'engrais, de produits phytosanitaires, etc.", Category.CLASS
        ),
        Classification(
            "5248303",
            "le commerce de détail de fleurs artificielles et d'articles d'ornementation en fleurs artificielles",
            Category.CLASS,
        ),
        Classification(
            "5248304",
            "le commerce de détail spécialisé portant sur une large gamme d'articles de jardinage et de produits horticoles (centres de jardinage)",
            Category.CLASS,
        ),
        Classification("52484", "Commerce de détail spécialisé d'horlogerie et de bijouterie", Category.CLASS),
        Classification("5248401", "le commerce de détail de montres et autres articles d'horlogerie", Category.CLASS),
        Classification("5248402", "le commerce de détail d'articles de bijouterie et d'orfèvrerie", Category.CLASS),
        Classification(
            "52485", "Commerce de détail spécialisé de matériel photographique, optique et de pécision", Category.CLASS
        ),
        Classification(
            "5248501",
            "le commerce de détail d'articles d'optique (y compris les lunettes), de photographie (y compris les pellicules) et de précision",
            Category.CLASS,
        ),
        Classification(
            "52486",
            "Commerce de détail spécialisé de papiers peints, de revêtements de murs et de sols",
            Category.CLASS,
        ),
        Classification("5248601", "le commerce de détail de tapis et moquettes", Category.CLASS),
        Classification(
            "5248602",
            "le commerce de détail de revêtements de sols en plastique, caoutchouc, liège, etc.",
            Category.CLASS,
        ),
        Classification("5248603", "le commerce de détail de papier peints", Category.CLASS),
        Classification(
            "52487",
            "Commerce de détail spécialisé d'équipements de bureau, d'ordinateurs et de matériel de télécommunication",
            Category.CLASS,
        ),
        Classification(
            "5248701", "le commerce de détail d'ordinateurs et de logiciels non personnalisés", Category.CLASS
        ),
        Classification("5248702", "le commerce de détail de matériel et mobilier de bureau", Category.CLASS),
        Classification(
            "52488", "Commerce de détail spécialisé d'articles de droguerie et de produits d'entretien", Category.CLASS
        ),
        Classification(
            "5248801", "le commerce de détail d'articles de droguerie et de produits d'entretien", Category.CLASS
        ),
        Classification("5248802", "le commerce de détail de produits de nettoyage", Category.CLASS),
        Classification("52489", "Commerce de détail spécialisé de jeux et de jouets", Category.CLASS),
        Classification("5248901", "le commerce de détail de jeux et jouets", Category.CLASS),
        Classification("52491", "Commerce de détail spécialisé d'armes et de munitions", Category.CLASS),
        Classification(
            "5249101", "le commerce de détail d'armes et de munitions pour la chasse ou le tir au fusil", Category.CLASS
        ),
        Classification("5249102", "le commerce de détail d'armes défensives", Category.CLASS),
        Classification("52492", "Commerce de détail spécialisé de cycles", Category.CLASS),
        Classification("5249201", "le commerce de détail de cycles", Category.CLASS),
        Classification("52493", "Commerce de détail spécialisé de voitures d'enfant", Category.CLASS),
        Classification("5249301", "le commerce de détail de voitures d'enfant", Category.CLASS),
        Classification(
            "5249302",
            "le commerce de détail de berceaux, de sièges de sécurité pour enfants et d'autres articles de puériculture",
            Category.CLASS,
        ),
        Classification("52494", "Commerce de détail spécialisé de machines à coudre et à tricoter", Category.CLASS),
        Classification("5249401", "le commerce de détail de machines à coudre et à tricoter", Category.CLASS),
        Classification(
            "52495", "Commerce de détail spécialisé de timbres-postes et de pièces de monnaies", Category.CLASS
        ),
        Classification("5249501", "le commerce de détail de timbres et de monnaies", Category.CLASS),
        Classification(
            "52496",
            "Commerce de détail spécialisé d'animaux de compagnie et d'aliments pour ces animaux",
            Category.CLASS,
        ),
        Classification(
            "5249601", "le commerce de détail d'animaux de compagnie et de fournitures pour animaux", Category.CLASS
        ),
        Classification(
            "52497",
            "Commerce de détail spécialisé de souvenirs, d'objets artisanaux et d'articles religieux",
            Category.CLASS,
        ),
        Classification(
            "5249701", "le commerce de détail de souvenirs, d'objets artisanaux et d'articles religieux", Category.CLASS
        ),
        Classification("5249702", "le commerce de détail de bijouterie fantaisie, de gadgets, etc.", Category.CLASS),
        Classification(
            "52498", "Autres commerces de détail spécialisés de produits non alimentaires n.d.a.", Category.CLASS
        ),
        Classification(
            "5249801",
            "le commerce de détail d'art contemporain, de tableaux nouveaux, de reproductions, de cadres, etc.",
            Category.CLASS,
        ),
        Classification("5249802", "le commerce de détail de ficelles, de cordes et de cordages", Category.CLASS),
        Classification(
            "5249803", "le commerce de détail d'articles n.d.a. autres que produits alimentaires", Category.CLASS
        ),
        Classification("52501", "Commerce de détail d'antiquités", Category.CLASS),
        Classification("5250101", "le commerce de détail d'antiquités et objets d'art anciens", Category.CLASS),
        Classification("52502", "Commerce de détail de biens d'occasion", Category.CLASS),
        Classification("5250201", "le commerce de détail de livres d'occasion", Category.CLASS),
        Classification(
            "5250202",
            "le commerce de détail d'autres biens d'occasion tels que meubles, matériaux de démolition, vêtements, brocante, etc.",
            Category.CLASS,
        ),
        Classification(
            "5250203",
            "le commerce de détail de biens de récupération de toute nature, exercé dans des magasins qui appartiennent à des centres de récupération",
            Category.CLASS,
        ),
        Classification("52610", "Vente par correspondance", Category.CLASS),
        Classification(
            "5261001",
            "le commerce de détail de tous types de produits par correspondance. Les produits et articles sont expédiés à l'acheteur qui fait son choix au départ de publicités, catalogues spécialisés ou non, modèl",
            Category.CLASS,
        ),
        Classification(
            "5261002",
            "la vente direct par téléphone ou par le truchement de la radio ou de la télévision",
            Category.CLASS,
        ),
        Classification("52621", "Commerce de détail alimentaire sur marchés et éventaires", Category.CLASS),
        Classification("5262101", "commerce de détail alimentaire sur marchés et éventaires", Category.CLASS),
        Classification(
            "52622", "Commerce de détail d'habillement et d'articles textiles sur marchés et éventaires", Category.CLASS
        ),
        Classification(
            "5262201",
            "commerce de détail d'habillement et d'articles textiles sur marchés et éventaires",
            Category.CLASS,
        ),
        Classification("52623", "Autres commerces de détail sur marchés et éventaires", Category.CLASS),
        Classification("5262301", "autres commerces de détail sur marchés et éventaires", Category.CLASS),
        Classification("52630", "Autres commerces de détail hors magasins", Category.CLASS),
        Classification(
            "5263001",
            "le commerce de détail de tous types de produits exercé selon des modalités non prévues dans les classes précédentes: par démarcheurs, par distributeurs automatiques, par démonstrateurs, par marchands",
            Category.CLASS,
        ),
        Classification("52710", "Réparation de chaussures et d'articles en cuir", Category.CLASS),
        Classification(
            "5271001",
            "la réparation de chaussures, bagages, articles de maroquinerie et articles similaires, en cuir ou en autres matières",
            Category.CLASS,
        ),
        Classification("52720", "Réparation d'appareils électriques à usage domestique", Category.CLASS),
        Classification("5272001", "la réparation d'appareils électroménagers", Category.CLASS),
        Classification("5272002", "la réparation d'appareils audio et vidéo", Category.CLASS),
        Classification("52730", "Réparation de montres, horloges et bijoux", Category.CLASS),
        Classification("5273001", "la réparation de montres, horloges et bijoux", Category.CLASS),
        Classification("52740", "Autres réparations n.d.a.", Category.CLASS),
        Classification("5274001", "la réparation de bicyclettes", Category.CLASS),
        Classification("5274002", "la réparation de jouets", Category.CLASS),
        Classification("5274003", "la réparation d'articles de sport et de camping", Category.CLASS),
        Classification("5274004", "la réparation et l'entretien de chaudières domestiques", Category.CLASS),
        Classification(
            "5274005", "la réparation de vêtements déjà portés: stoppage,remaillage, retouche, etc.", Category.CLASS
        ),
        Classification(
            "5274006",
            "la réparation d'articles divers (clés,serrures,talons,etc.), y compris la réparations urgentes à domicile",
            Category.CLASS,
        ),
        Classification(
            "5274007", "les activités des accordeurs de piano et autres instruments de musique", Category.CLASS
        ),
        Classification("5274008", "la réparation d'articles de photographie", Category.CLASS),
        Classification("5274009", "autres réparations de biens de consommation n.d.a.", Category.CLASS),
        Classification("55100", "Hôtels", Category.CLASS),
        Classification(
            "5510001",
            "la mise à disposition de lieux d'hébergement pour des séjours de courte durée, en liaison ou non avec l'exploitation d'un restaurant, dans les hôtels, motels et auberges (avec service hôtelier), ou da",
            Category.CLASS,
        ),
        Classification("55101", "Hôtels et motels, avec restaurant", Category.CLASS),
        Classification("55102", "Hôtels et motels, sans restaurant", Category.CLASS),
        Classification("55110", "Hôtels et motels, avec restaurant", Category.CLASS),
        Classification("5511001", "hôtels, motels, avec restaurant", Category.CLASS),
        Classification("55120", "Hôtels et motels, sans restaurant", Category.CLASS),
        Classification("5512001", "hôtels, motels, sans restaurant", Category.CLASS),
        Classification("5512002", "les hôtels et motels n'assurant que le petit déjeuner", Category.CLASS),
        Classification("55210", "Auberges de jeunesse et refuges", Category.CLASS),
        Classification("5521001", "auberges de jeunesse, refuges", Category.CLASS),
        Classification("55220", "Exploitation de terrains de camping", Category.CLASS),
        Classification("5522001", "exploitation de terrains de camping", Category.CLASS),
        Classification("55231", "Centres et villages de vacances", Category.CLASS),
        Classification(
            "5523101",
            "les centres et villages de vacances (y compris les parcs résidentiels de bungalows et chalets) avec ou sans restaurant et infrastructure de sports à usage des touristes",
            Category.CLASS,
        ),
        Classification("5523102", "les colonies de vacances pour enfants ou adultes", Category.CLASS),
        Classification("55232", "Autres moyens d'hébergement de courte durée", Category.CLASS),
        Classification(
            "5523201",
            "la mise à disposition de logement pour des séjours de courte durée dans des maisons et appartements des vacances",
            Category.CLASS,
        ),
        Classification(
            "5523202",
            "la location des chambres par des particuliers (avec ou sans fourniture de repas), l'hébergement de courte durée à la ferme, etc.",
            Category.CLASS,
        ),
        Classification("5523203", "l'exploitation de wagon-lits", Category.CLASS),
        Classification("5523204", "autres moyens d'hébergement de courte durée n.d.a.", Category.CLASS),
        Classification("55233", "Hébergement collectif non touristique", Category.CLASS),
        Classification(
            "5523301",
            "la mise à disposition d'hébergement collectif à des étudiants, ouvriers saisonniers, etc.",
            Category.CLASS,
        ),
        Classification(
            "5523302",
            "les internats d'élèves lorsque ceux-ci sont indépendants d'un établissement scolaire",
            Category.CLASS,
        ),
        Classification("55301", "Restauration de type traditionnel", Category.CLASS),
        Classification("5530101", "restauration de type traditionnel", Category.CLASS),
        Classification("5530102", "la vente de repas à bord de navires ou de voitures-restaurants", Category.CLASS),
        Classification(
            "5530103",
            "les restaurants spécialisés en week-ends gastronomiques, les restaurants exotiques, etc.",
            Category.CLASS,
        ),
        Classification(
            "5530104",
            "les restaurants disposant de quelques chambres (max. 5) à usage de leur propre clientèle",
            Category.CLASS,
        ),
        Classification("5530105", "les cafés-restaurants (tavernes)", Category.CLASS),
        Classification("55302", "Restauration de type rapide", Category.CLASS),
        Classification(
            "5530201",
            "la vente au comptoir d'aliments et de boissons à consommer sur place, généralement présentés dans des conditionnements jetables: établissements de restauration rapide (fast-foods) tels les snack-bars,",
            Category.CLASS,
        ),
        Classification(
            "5530202",
            "la vente au comptoir d'aliments et de boissons à consommer sur place, généralement présentés dans des conditionnements jetables: friteries, échoppes de hot-dogs, etc.",
            Category.CLASS,
        ),
        Classification(
            "5530203",
            "la vente au comptoir d'aliments et de boissons à consommer sur place, généralement présentés dans des conditionnements jetables: croissanteries, crêperies et gaufreries",
            Category.CLASS,
        ),
        Classification(
            "5530204",
            "la vente au comptoir d'aliments et de boissons à consommer sur place, généralement présentés dans des conditionnements jetables: laiteries, salons de thé, salons de dégustation de crèmes glacées et si",
            Category.CLASS,
        ),
        Classification(
            "5530205",
            "la vente au comptoir d'aliments et de boissons à consommer sur place, généralement présentés dans des conditionnements jetables: cafétérias",
            Category.CLASS,
        ),
        Classification(
            "5530206",
            "la vente au comptoir d'aliments et de boissons à consommer sur place, généralement présentés dans des conditionnements jetables: services au volant (drive-in)",
            Category.CLASS,
        ),
        Classification(
            "5530207",
            "la vente au comptoir d'aliments et de boissons à consommer sur place, généralement présentés dans des conditionnements jetables: pizzerias",
            Category.CLASS,
        ),
        Classification("55401", "Cafés et bars", Category.CLASS),
        Classification(
            "5540101",
            "la vente de boissons destinées en général à être consommées sur place, par les établissements suivants, avec ou sans présentation d'un spectacle: cafés, bars, boîtes de nuit, débits de bière, etc.",
            Category.CLASS,
        ),
        Classification("55402", "Discothèques, dancings et similaires", Category.CLASS),
        Classification(
            "5540201",
            "l'exploitation régulière de discothèques, salles de bal et clubs privés, qui réalisent leur chiffre d'affaires par la vente de boissons, avec ou sans obligation d'achat de tickets d'entrée donnant dro",
            Category.CLASS,
        ),
        Classification("55510", "Cantines", Category.CLASS),
        Classification("55521", "Restauration collective sous contrat (catering)", Category.CLASS),
        Classification(
            "5552101",
            "la préparation de repas et de mets dans les cuisines centrales pour le compte de tiers,tels les: compagnies aériennes, cantines, restaurants d'entreprises, etc.",
            Category.CLASS,
        ),
        Classification("55522", "Traiteurs et organisation de réceptions", Category.CLASS),
        Classification(
            "5552201",
            "la préparation, la livraison à domicile et le service de repas et de plats cuisinés",
            Category.CLASS,
        ),
        Classification(
            "5552202",
            "l'organisation de noces, banquets, cocktails, buffets, lunches et réceptions diverses",
            Category.CLASS,
        ),
        Classification("60100", "Transports ferroviaires", Category.CLASS),
        Classification(
            "6010001", "le transport interurbain de passagers et de marchandises par chemin de fer", Category.CLASS
        ),
        Classification("60211", "Transports urbains ou suburbains de voyageurs", Category.CLASS),
        Classification(
            "6021101",
            "les activités de transport urbain ou suburbain de passagers sur des lignes déterminées, conformément à un horaire publié des départs et arrivées aux arrêts indiqués sur ces horaires Transport par auto",
            Category.CLASS,
        ),
        Classification("60212", "Autres transports routiers réguliers de voyageurs", Category.CLASS),
        Classification(
            "6021201",
            "les activités de transport interurbain de voyageurs par auto car ou tramway, sur des lignes déterminées, conformément à un horaire publié des départs et arrivées aux arrêts indiqués sur ces horaires",
            Category.CLASS,
        ),
        Classification(
            "6021202",
            "l'exploitation d'autobus scolaires, de navettes vers les aéroports et les gares, le transport de personnel, etc.",
            Category.CLASS,
        ),
        Classification(
            "6021203", "l'exploitation de téléphériques, funiculaires et remontées mécaniques diverses", Category.CLASS
        ),
        Classification("60220", "Exploitation de taxis", Category.CLASS),
        Classification("6022001", "exploitation de taxis", Category.CLASS),
        Classification("6022002", "la location de voitures particulières avec chauffeur", Category.CLASS),
        Classification("60230", "Autres transports terrestres de voyageurs", Category.CLASS),
        Classification(
            "6023001",
            "les autres transports routiers de passagers, non réguliers: transports à la demande,excursions touristiques par autocar, etc.",
            Category.CLASS,
        ),
        Classification("6023002", "le transport de personnes par véhicules à traction animale", Category.CLASS),
        Classification("60241", "Déménagement", Category.CLASS),
        Classification(
            "6024101", "le déménagement de mobilier de particuliers, de bureaux, d'ateliers ou d'usines", Category.CLASS
        ),
        Classification("6024102", "les garde-meubles", Category.CLASS),
        Classification("6024103", "la livraison de meubles et équipements ménagers", Category.CLASS),
        Classification("60242", "Transports routiers de marchandises", Category.CLASS),
        Classification(
            "6024201",
            "les activités de transport de marchandises par route: transport de bois de sciage, transport de bétail, transport frigorifique, transport lourd international, transport en vrac, y compris par camions-",
            Category.CLASS,
        ),
        Classification(
            "6024202", "la collecte de lait et le transport vers les unités de traitement du lait", Category.CLASS
        ),
        Classification(
            "6024203", "le transport de béton, prêt à l'emploi, non fabriqué par l'unité même", Category.CLASS
        ),
        Classification("6024204", "le transport de marchandises par véhicules à traction animale", Category.CLASS),
        Classification("60243", "Location de camions avec conducteur", Category.CLASS),
        Classification("6024301", "location de camions avec conducteur", Category.CLASS),
        Classification("60300", "Transports par conduites", Category.CLASS),
        Classification(
            "6030001", "le transport de gaz, de liquides et d'autres substances, par conduites", Category.CLASS
        ),
        Classification("6030002", "l'exploitation de stations de pompage", Category.CLASS),
        Classification("61100", "Transports maritimes et côtiers", Category.CLASS),
        Classification(
            "6110001", "le transport par eau, régulier ou non, de personnes et de marchandises", Category.CLASS
        ),
        Classification("6110002", "l'exploitation de bateaux d'excursion, de croisière ou de tourisme", Category.CLASS),
        Classification("6110003", "l'exploitation de bacs, de bateaux-taxis, etc.", Category.CLASS),
        Classification("6110004", "l'exploitation de remorqueurs et de pousseurs de péniches", Category.CLASS),
        Classification("6110005", "la location de bateaux et navires avec équipage", Category.CLASS),
        Classification("61200", "Transports fluviaux", Category.CLASS),
        Classification(
            "6120001",
            "le transport de passagers et de marchandises: sur les fleuves, les canaux, les lacs et les autres voies navigables intérieures; à l'intérieur des ports et des docks",
            Category.CLASS,
        ),
        Classification("62100", "Transports aériens réguliers", Category.CLASS),
        Classification(
            "6210001",
            "le transport aérien de passagers et de marchandises sur des lignes régulières et selon des horaires réguliers",
            Category.CLASS,
        ),
        Classification("62200", "Transports aériens non réguliers", Category.CLASS),
        Classification("6220001", "le transport aérien non régulier de personnes et de marchandises", Category.CLASS),
        Classification("6220002", "les vols par charters, réguliers ou non", Category.CLASS),
        Classification("6220003", "l'exploitation d'avions-taxis", Category.CLASS),
        Classification("6220004", "les excursions aériennes, les baptêmes de l'air, etc.", Category.CLASS),
        Classification("6220005", "la location d'avions avec pilote", Category.CLASS),
        Classification("62300", "Transports spatiaux", Category.CLASS),
        Classification("6230001", "le lancement de satellites et de véhicules spatiaux", Category.CLASS),
        Classification("6230002", "le transport, dans l'espace, de marchandises et de personnes", Category.CLASS),
        Classification("63111", "Manutention portuaire", Category.CLASS),
        Classification(
            "6311101",
            "le chargement et le déchargement de marchandises ou de bagages dans les ports maritimes",
            Category.CLASS,
        ),
        Classification("6311102", "l'arrimage et le débardage de marchandises", Category.CLASS),
        Classification("63112", "Autre manutention", Category.CLASS),
        Classification(
            "6311201",
            "le chargement, le transbordement et le déchargement de marchandises et de bagages ailleurs que dans les ports maritimes (manutention routière, ferroviaire, fluviale et sur aéroports)",
            Category.CLASS,
        ),
        Classification("63121", "Entreposage frigorifique", Category.CLASS),
        Classification(
            "6312101",
            "l'exploitation pour compte de tiers d'installations d'entreposage frigorifique ou de lieux de stockage réfrigéré pour tous les types de produits, y compris les produits agricoles",
            Category.CLASS,
        ),
        Classification("63122", "Autre entreposage", Category.CLASS),
        Classification(
            "6312201",
            "l'exploitation pour compte de tiers d'installations de stockage et d'entreposage non frigorifiques (silos, entrepôts, hangars, parcs à conteneurs, citernes, etc.) pour tous les types de marchandises,",
            Category.CLASS,
        ),
        Classification("63210", "Services annexes des transports terrestres", Category.CLASS),
        Classification(
            "6321001",
            "l'exploitation de gares ferroviaires et routières et de terminaux de manutention de fret",
            Category.CLASS,
        ),
        Classification(
            "6321002",
            "l'exploitation d'autoroutes, de tunnels, de ponts, de parcs et emplacements de stationnement de véhicules et de garages pour bicyclettes",
            Category.CLASS,
        ),
        Classification("6321003", "le gardiennage de caravanes durant l'hiver", Category.CLASS),
        Classification(
            "6321004",
            "l'organisation de covoiturage et d'autres formes de transport en commun non public de personnes",
            Category.CLASS,
        ),
        Classification("6321005", "l'exploitation de centrales d'appel pour taxis", Category.CLASS),
        Classification("63220", "Services annexes des transports par eau", Category.CLASS),
        Classification(
            "6322001",
            "l'exploitation d'installations portuaires: jetées, quais, bassins, terminaux, etc.",
            Category.CLASS,
        ),
        Classification("6322002", "l'exploitation de ports fluviaux, voies fluviales et écluses", Category.CLASS),
        Classification("6322003", "la navigation, le pilotage, le mouillage", Category.CLASS),
        Classification("6322004", "le renflouement des navires, les services de sauvetage", Category.CLASS),
        Classification("6322005", "la signalisation par phares, balises et radiobalises", Category.CLASS),
        Classification("63230", "Services annexes des transports aériens", Category.CLASS),
        Classification(
            "6323001", "l'exploitation d'installations aéroportuaires tels les terminaux, etc.", Category.CLASS
        ),
        Classification("6323002", "le contrôle des aéroports et de la circulation aérienne", Category.CLASS),
        Classification("6323003", "les activités des écoles de pilotage pour pilotes de ligne", Category.CLASS),
        Classification("6323004", "les services au sol d'entretien-maintenance des avions", Category.CLASS),
        Classification("6323005", "la protection et la lutte contre les incendies", Category.CLASS),
        Classification("63301", "Agences de voyage", Category.CLASS),
        Classification("6330101", "la fourniture d'informations et de conseils en matière de voyages", Category.CLASS),
        Classification(
            "6330102",
            "l'organisation de voyages et d'excursions de courte durée, l'organisation de voyages personnalisés, de l'hébergement et du transport des voyageurs et des touristes",
            Category.CLASS,
        ),
        Classification(
            "6330103",
            "la vente sur base de brochures et de catalogues de voyages organisés par les tour operators",
            Category.CLASS,
        ),
        Classification("6330104", "la vente de billets d'entrée", Category.CLASS),
        Classification("63302", "Voyagistes", Category.CLASS),
        Classification(
            "6330201",
            "les organisateurs de voyages qui, en général, présentent une large gamme de voyages.  Leurs clients peuvent choisir parmi plusieurs formules et destinations à l'aide de brochures et de catalogues.",
            Category.CLASS,
        ),
        Classification(
            "6330202",
            "les organisateurs spécialisés dans une formule de vacances déterminée pour laquelle ils offrent des destinations diverses",
            Category.CLASS,
        ),
        Classification("63303", "Guides, services d'information touristique et similaires", Category.CLASS),
        Classification("6330301", "guides, services d'information touristique et similaires", Category.CLASS),
        Classification("63401", "Agences d'expédition", Category.CLASS),
        Classification("6340101", "agences d'expédition", Category.CLASS),
        Classification("63402", "Affrètement", Category.CLASS),
        Classification("6340201", "l'affrètement maritime", Category.CLASS),
        Classification(
            "6340202",
            "l'affrètement qui consiste à confier des envois sans groupage préalable à des transporteurs publics (transport ferroviaire, transport par eau, transport aérien ou une combinaison de ces moyens)",
            Category.CLASS,
        ),
        Classification("63403", "Agences maritimes", Category.CLASS),
        Classification("6340301", "agences maritimes", Category.CLASS),
        Classification("63404", "Agences en douane", Category.CLASS),
        Classification("6340401", "agences en douane", Category.CLASS),
        Classification("63405", "Intermédiaires du transport", Category.CLASS),
        Classification(
            "6340501",
            "les activités des commissionnaires de transport qui concluent pour compte propre des contrats de transport de marchandises mais font effectuer le transport par des tiers",
            Category.CLASS,
        ),
        Classification("6340502", "les activités des courtiers de transport", Category.CLASS),
        Classification("6340503", "les activités des commissionnaires-expéditeurs, etc.", Category.CLASS),
        Classification("63406", "Autres activités annexes de l'organisation du transport de fret", Category.CLASS),
        Classification(
            "6340601",
            "les messageries: l'enlèvement de marchandises et le groupage d'envois individuels pour l'expédition, la distribution et la livraison des marchandises à l'arrivée",
            Category.CLASS,
        ),
        Classification("6340602", "la livraison de fret express", Category.CLASS),
        Classification(
            "6340603", "les autres activités annexes de l'organisation du transport de fret", Category.CLASS
        ),
        Classification("64110", "Postes nationales", Category.CLASS),
        Classification(
            "6411001", "la levée, l'acheminement et la distribution du courrier et des colis", Category.CLASS
        ),
        Classification(
            "6411002",
            "la collecte du courrier et des colis dans les boîtes à lettres publiques ou les bureaux de poste",
            Category.CLASS,
        ),
        Classification("6411003", "la distribution et la livraison du courrier et des colis", Category.CLASS),
        Classification("6411004", "l'émission de timbres postaux", Category.CLASS),
        Classification("6411005", "la location de boîtes postales,le service de poste restante, etc.", Category.CLASS),
        Classification("64120", "Autres activités de courrier", Category.CLASS),
        Classification(
            "6412001",
            "la levée, l'acheminement et la distribution de lettres,colis et paquets par des entreprises autres que l'admininistration postale nationale. Il peut être fait appel à un seul ou à plusieurs modes de t",
            Category.CLASS,
        ),
        Classification("64200", "Télécommunications", Category.CLASS),
        Classification(
            "6420001",
            "la transmission des sons, des images, de données ou d'autres informations par câble, par voie hertzienne, par relais ou par satellite",
            Category.CLASS,
        ),
        Classification(
            "6420002",
            "l'exploitation de réseaux de communication électroniques à usage général ou à usage de catégories déterminées d'utilisateurs (p.ex. institutions financières)",
            Category.CLASS,
        ),
        Classification("6420003", "téléphone, mobilophones, télégraphe, télex, fax", Category.CLASS),
        Classification("6420004", "l'entretien des réseaux", Category.CLASS),
        Classification(
            "6420005",
            "la transmission (transport) de programmes de radio et de télévision (radiodistribution et télédistribution, sociétés de câble)",
            Category.CLASS,
        ),
        Classification("64201", "Régie des télégraphes et téléphones - Belgacom", Category.CLASS),
        Classification("64202", "Autres activités de télécommunication, y compris télédistribution", Category.CLASS),
        Classification("65110", "Banques centrales", Category.CLASS),
        Classification("6511001", "les activités de la Banque Nationale et du Fond des Rentes.", Category.CLASS),
        Classification("65120", "Autres intermédiations monétaires", Category.CLASS),
        Classification("65121", "Banques", Category.CLASS),
        Classification(
            "6512101",
            "les activités des unités qui figurent sur la liste des banques publiée par la Commission Bancaire et Financière (CBF)",
            Category.CLASS,
        ),
        Classification("65122", "Caisses d'épargne", Category.CLASS),
        Classification(
            "6512201",
            "les activités des unités qui figurent sur la liste des caisses d'épargne publiée par la Commission Bancaire et Financière (CBF)",
            Category.CLASS,
        ),
        Classification("65123", "Institutions publiques de crédit", Category.CLASS),
        Classification("6512301", "la CGER-banque", Category.CLASS),
        Classification("6512302", "le Crédit Communal de Belgique", Category.CLASS),
        Classification(
            "6512303",
            "la Caisse Nationale de Crédit Professionnel, y compris les associations de crédit agréées par elle",
            Category.CLASS,
        ),
        Classification(
            "6512304",
            "l'Institut National de Crédit Agricole, y compris les caisses de crédit agréées par cet institut",
            Category.CLASS,
        ),
        Classification("6512305", "la Société Nationale de Crédit à l'Industrie", Category.CLASS),
        Classification("6512306", "l'Office Central de Crédit Hypothécaire", Category.CLASS),
        Classification("6512307", "les caisses d'épargne communales", Category.CLASS),
        Classification(
            "6512308",
            "l'Institut de Réescompte et de Garantie, considéré par convention comme institution publique de crédit",
            Category.CLASS,
        ),
        Classification("65124", "Le Postchèque", Category.CLASS),
        Classification("65210", "Crédit-bail", Category.CLASS),
        Classification(
            "6521001",
            "la conclusion d'un contrat de location-financement sur des biens d'équipement entre le bailleur et le locataire",
            Category.CLASS,
        ),
        Classification("65221", "Crédit à la consommation", Category.CLASS),
        Classification(
            "6522101",
            "les activités des organismes de financement qui concluent uniquement des contrats de crédit avec un consommateur: ventes et prêts à tempérament, crédit-bail étranger aux activités professionelles du c",
            Category.CLASS,
        ),
        Classification("65222", "Autre distribution de crédit", Category.CLASS),
        Classification(
            "6522201",
            "les unités qui consentent uniquement les crédits suivants: crédits hypothécaires, crédits professionnels, crédits permanents, crédit de caisse, etc.",
            Category.CLASS,
        ),
        Classification("6522202", "les activités exercées par les bureaux d'escompte", Category.CLASS),
        Classification("6522203", "les activités exercées par les monts-de-piété et assimilés", Category.CLASS),
        Classification("6522204", "autre distribution de crédit n.d.a.", Category.CLASS),
        Classification("65223", "Affacturage", Category.CLASS),
        Classification("65231", "Holdings financiers", Category.CLASS),
        Classification(
            "6523101",
            "la détention à long terme d'actions émanant de plusieurs autres entreprises classées en majorité dans le secteur financier",
            Category.CLASS,
        ),
        Classification("65232", "Affacturage", Category.CLASS),
        Classification(
            "6523201",
            "l'acquisition de toutes les factures exigibles des entreprises aux termes desquelles le factor reprend tous les risques et paie aux entreprises le montant intégral de la facture moins une rémunération",
            Category.CLASS,
        ),
        Classification("65233", "Sociétés de bourse", Category.CLASS),
        Classification(
            "6523301",
            "l'intervention pour compte propre et, accessoirement, comme intermédiaire pour compte d'autrui, dans les émissions publiques, les transactions avec le public sur valeurs mobilières ou les offres publi",
            Category.CLASS,
        ),
        Classification("65234", "Sociétés de portefeuille", Category.CLASS),
        Classification("6523401", "le placement en actions", Category.CLASS),
        Classification("65235", "Organismes de placement collectif", Category.CLASS),
        Classification(
            "6523501",
            "le placement en valeurs mobilières (actions,obligations,etc) ou en biens immobiliers par des organismes de placement collectif: sociétés d'investissement (Sicav,Sicaf), fonds communs de placement ou d",
            Category.CLASS,
        ),
        Classification("65236", "Autre intermédiation financière n.d.a.", Category.CLASS),
        Classification("6523601", "la Caisse des Dépôts et Consignations", Category.CLASS),
        Classification(
            "6523602",
            "les institutions financières qui offrent des formes de financement spécifique: capital à haut risque ou venture capital, investmentbanking, etc.",
            Category.CLASS,
        ),
        Classification(
            "6523603", "les transactions sur lingots d'or réalisées sur les marchés financiers", Category.CLASS
        ),
        Classification("6523604", "les activités des sociétés de football-invest", Category.CLASS),
        Classification("6523605", "les financements d'import/export", Category.CLASS),
        Classification("6523606", "les intermédiations financières n.d.a.", Category.CLASS),
        Classification("66011", "Opérations directes d'assurances vie", Category.CLASS),
        Classification("6601101", "opérations directes d'assurance Vie", Category.CLASS),
        Classification("66012", "Réassurances vie acceptées", Category.CLASS),
        Classification("6601201", "Réassurances Vie acceptées", Category.CLASS),
        Classification("66013", "Entreprises d'assurances multibranches à prédominance vie", Category.CLASS),
        Classification(
            "6601301",
            "les entreprises d'assurances qui concluent tant des assurances Vie que des Non Vie, mais dont l'activité principale consiste à conclure des assurances Vie",
            Category.CLASS,
        ),
        Classification("66020", "Caisses de retraite", Category.CLASS),
        Classification(
            "6602001",
            "les activités (encaissement de cotisations, placement des fonds, prestations des pensions) des institutions de prévoyance créées par l'employeur(privé ou public) afin de constituer une pension extra-l",
            Category.CLASS,
        ),
        Classification(
            "6602002",
            "les activités des caisses de pensions créées en faveur de professions libérales et indépendantes auxquelles on peut s'affilier sur une base individuelle et volontaire pour constituer une pension extra",
            Category.CLASS,
        ),
        Classification("66031", "Opérations directes d'assurances non-vie", Category.CLASS),
        Classification("6603101", "les activités d'assurances concernant accidents et maladie", Category.CLASS),
        Classification("6603102", "les activités d'assurances concernant véhicules automobiles", Category.CLASS),
        Classification(
            "6603103",
            "les activités d'assurances concernant assurance maritime, assurance transports, assurance aérienne",
            Category.CLASS,
        ),
        Classification(
            "6603104", "les activités d'assurances concernant l'incendie et autres dommages aux biens", Category.CLASS
        ),
        Classification("6603105", "les activités d'assurances concernant la responsabilité civile", Category.CLASS),
        Classification("6603106", "les activités d'assurances concernant crédit et caution", Category.CLASS),
        Classification("6603107", "les activités d'assurances concernant pertes pécuniaires diverses", Category.CLASS),
        Classification("6603108", "les activités d'assurances concernant la protection juridique", Category.CLASS),
        Classification("6603109", "les activités d'assurances concernant l'assistance", Category.CLASS),
        Classification("66032", "Réassurances non-vie", Category.CLASS),
        Classification("6603201", "Réassurances Non Vie", Category.CLASS),
        Classification("66033", "Entreprises d'assurances multibranches à prédominance non-vie", Category.CLASS),
        Classification(
            "6603301",
            "les entreprises d'assurances qui concluent tant des assurances Vie que des Non Vie, mais dont l'activité principale consiste à conclure des assurances Non Vie",
            Category.CLASS,
        ),
        Classification("67110", "Administration de marchés financiers", Category.CLASS),
        Classification(
            "6711001",
            "l'exploitation et la supervision de marchés financiers autrement que par des organismes publics: activités des bourses de valeurs mobilières, bourses d'option et de futures, etc.",
            Category.CLASS,
        ),
        Classification("67120", "Gestion de portefeuilles et de fortunes, conseils en placements", Category.CLASS),
        Classification(
            "6712001",
            "les opérations exécutées sur des marchés financiers pour le compte de tiers (p.ex. le courtage en valeurs mobilières) ainsi que les activités qui s'y rattachent",
            Category.CLASS,
        ),
        Classification("6712002", "les sociétés de gestion des fonds communs de placement", Category.CLASS),
        Classification(
            "6712003",
            "les conseils en placements et la gestion de patrimoines financiers des tiers (AR du 5 août 1991 relatif à la gestion de fortune et au conseil en placements)",
            Category.CLASS,
        ),
        Classification("67130", "Autres auxiliaires financiers", Category.CLASS),
        Classification("6713001", "courtiers en crédits hypothécaires", Category.CLASS),
        Classification("6713002", "bureaux de change", Category.CLASS),
        Classification("6713003", "la caution et la garantie", Category.CLASS),
        Classification(
            "6713004", "l'intermédiation en crédits et prêts par des courtiers et autres intermédiaires", Category.CLASS
        ),
        Classification(
            "6713005",
            "les représentants de banques étrangères, qui n'exécutent pas des opérations de banque proprement dites",
            Category.CLASS,
        ),
        Classification(
            "6713006",
            "la création et l'exploitation de systèmes électroniques de circulation monétaire",
            Category.CLASS,
        ),
        Classification("6713007", "l'émission de chèques-repas", Category.CLASS),
        Classification("6713008", "la mise à disposition de coffres-forts, etc.", Category.CLASS),
        Classification("67201", "Agents et courtiers d'assurances", Category.CLASS),
        Classification("6720101", "agents et courtiers d'assurances", Category.CLASS),
        Classification("67202", "Experts en dommages et risques", Category.CLASS),
        Classification("6720201", "experts en dommages et risques", Category.CLASS),
        Classification("67203", "Autres auxiliaires d'assurances", Category.CLASS),
        Classification("6720301", "autres auxiliaires d'assurances", Category.CLASS),
        Classification("70111", "Promotion immobilière de logements", Category.CLASS),
        Classification(
            "7011101",
            "la promotion immobilière de maisons d'habitation neuves ou de travaux de rénovation",
            Category.CLASS,
        ),
        Classification("7011102", "la promotion immobilière d'immeubles résidentiels", Category.CLASS),
        Classification("70112", "Promotion immobilière de bureaux", Category.CLASS),
        Classification("7011201", "promotion immobilière de bureaux", Category.CLASS),
        Classification("70113", "Promotion immobilière d'infrastructures", Category.CLASS),
        Classification(
            "7011301",
            "la promotion immobilière de: centres commerciaux et industriels, hôtels, zones d'activités et marchés, ports de plaisance, autoroutes, stations de sports d'hiver, etc.",
            Category.CLASS,
        ),
        Classification(
            "7011302", "l'aménagement ou la rénovation de zones urbaines par voie de promotion", Category.CLASS
        ),
        Classification("7011303", "le lotissement foncier", Category.CLASS),
        Classification("7011304", "l'aménagement et le remembrement de zones rurales", Category.CLASS),
        Classification("7011305", "l'aménagement de parcelles de cimetières", Category.CLASS),
        Classification("70120", "Marchands de biens immobiliers", Category.CLASS),
        Classification(
            "7012001",
            "les activités de transactions sur biens immobiliers tels que: immeubles résidentiels et maisons d'habitation, immeubles non résidentiels, terres et terrains",
            Category.CLASS,
        ),
        Classification(
            "7012002",
            "les transactions sur biens propres tels que fonds de commerce, droits à bail et pas de porte (reprise)",
            Category.CLASS,
        ),
        Classification("70201", "Location d'habitations, à l'exclusion des logements sociaux", Category.CLASS),
        Classification(
            "7020101",
            "la location d'appartements et de maisons, vides ou meublés, destinés à l'habitation",
            Category.CLASS,
        ),
        Classification("7020102", "la location de longue durée en hôtels-appartements", Category.CLASS),
        Classification("7020103", "l'exploitation de biens immobiliers en multipropriété", Category.CLASS),
        Classification("70202", "Location de logements sociaux", Category.CLASS),
        Classification(
            "7020201",
            "la promotion immobilière à objectif locatif par des sociétés de logements sociaux",
            Category.CLASS,
        ),
        Classification(
            "70203", "Location d'immeubles non résidentiels, y compris les salles d'exposition", Category.CLASS
        ),
        Classification(
            "7020301",
            "la location d'immeubles non résidentiels ( bureaux, espaces commerciaux, halls d'exposition, etc.)",
            Category.CLASS,
        ),
        Classification("7020302", "la location à l'année de boxes ou de lieux de garage de véhicules", Category.CLASS),
        Classification(
            "7020303", "la location de fonds de commerce (dans un système de gérances libres)", Category.CLASS
        ),
        Classification("70204", "Location de terres et terrains", Category.CLASS),
        Classification("7020401", "la location de terrains ( bâtis ou non) à usage agricole", Category.CLASS),
        Classification("7020402", "la location à l'année d'emplacements de caravanes", Category.CLASS),
        Classification(
            "70311",
            "Agences immobilières et intermédiaires en achat, vente et location de biens immobiliers",
            Category.CLASS,
        ),
        Classification(
            "7031101",
            "agences immobilières et intermédiaires en achat, vente et location de biens immobiliers",
            Category.CLASS,
        ),
        Classification("70312", "Estimation et évaluation de biens immobiliers", Category.CLASS),
        Classification("7031201", "estimation et évaluation de biens immobiliers", Category.CLASS),
        Classification("70321", "Administration d'immeubles résidentiels", Category.CLASS),
        Classification(
            "7032101",
            "la prise en charge au nom du (ou des) propriétaire(s) de l'ensemble des services nécessaires au fonctionnement des immeubles gérés (immeubles résidentiels)",
            Category.CLASS,
        ),
        Classification("7032102", "la collecte des loyers (immeubles résidentiels)", Category.CLASS),
        Classification("70322", "Administration d'autres biens immobiliers", Category.CLASS),
        Classification(
            "7032201",
            "la prise en charge au nom du (ou des) propriétaire (s) de l'ensemble des services nécessaires au fonctionnement des immeubles gérés (immeubles non résidentiels)",
            Category.CLASS,
        ),
        Classification("7032202", "la collecte des loyers (immeubles non résidentiels)", Category.CLASS),
        Classification("71100", "Location de véhicules automobiles", Category.CLASS),
        Classification("7110001", "la location à court terme de voitures particulières sans chauffeur", Category.CLASS),
        Classification(
            "7110002", "la location à longue durée de voitures particulières sans chauffeur", Category.CLASS
        ),
        Classification(
            "7110003",
            "la location à court terme ou la location-bail de véhicules utilitaires légers (max. 3,5 t) sans conducteur",
            Category.CLASS,
        ),
        Classification("71210", "Location d'autres matériels de transport terrestre", Category.CLASS),
        Classification(
            "7121001",
            "la location et la location-bail de matériels de transport terrestre,sans chauffeur, à l'excl.de voitures particulières et de véhicules utilit.légers: véhicules de chem.de fer, camions,tract.de halage,",
            Category.CLASS,
        ),
        Classification("71220", "Location de matériels de transport par eau", Category.CLASS),
        Classification(
            "7122001",
            "la location et la location-bail de matériels de transport maritime et fluvial tels que bateaux, cargos et navires de transport, sans équipage",
            Category.CLASS,
        ),
        Classification("71230", "Location de matériels de transport aérien", Category.CLASS),
        Classification(
            "7123001", "la location et la location-bail de matériels de transport aérien, sans pilote", Category.CLASS
        ),
        Classification("71310", "Location de matériel agricole", Category.CLASS),
        Classification("7131001", "la location de tracteurs agricoles et de motoculteurs", Category.CLASS),
        Classification(
            "7131002",
            "la location de machines et équipements pour l'agriculture, l'élevage et l'exploitation forestière, sans opérateur (= la location des produits fabriqués dans le groupe 29.3)",
            Category.CLASS,
        ),
        Classification("71320", "Location de machines et équipements pour la construction", Category.CLASS),
        Classification(
            "7132001",
            "la location et la location-bail de machines et équipements pour le bâtiment et le génie-civil, sans opérateur (grues, bouteurs, bétonnières, etc.)",
            Category.CLASS,
        ),
        Classification(
            "7132002",
            "la location d'échafaudages et de plates-formes de travail, sans montage ni démontage",
            Category.CLASS,
        ),
        Classification("71330", "Location de machines de bureau et de matériel informatique", Category.CLASS),
        Classification(
            "7133001",
            "la location et la location-bail de machines et équipements de bureau, sans opérateur: ordinateurs,machines et matériels informatiques,duplicateurs, machines à écrire et de traitem. de texte, matériel",
            Category.CLASS,
        ),
        Classification("7133002", "la location, ou la redevance d'utilisation, de logiciels", Category.CLASS),
        Classification("71340", "Location d'autres machines et équipements", Category.CLASS),
        Classification(
            "7134001",
            "la location et la location-bail de moteurs et turbines, compresseurs, machines-outils, sans opérateur",
            Category.CLASS,
        ),
        Classification(
            "7134002",
            "la location et la location-bail de matériels de radiodiffusion, de télévision et de communication, sans opérateur",
            Category.CLASS,
        ),
        Classification(
            "7134003",
            "location et la location-bail de matériels de mesure et de contrôle, sans opérateur",
            Category.CLASS,
        ),
        Classification(
            "7134004",
            "la location et la location-bail d'autres machines et matériels à usage scientifique, commercial et industriel, y compris les machines automatiques de vente de produits, sans opérateur",
            Category.CLASS,
        ),
        Classification(
            "7134005",
            "la location et la location-bail de chapiteaux pour expositions, fêtes d'entreprises, concerts, etc., sans opérateur",
            Category.CLASS,
        ),
        Classification(
            "7134006",
            "la location et la location-bail de machines à sous et jeux, électroniques ou non, pour cafés, casinos, etc.",
            Category.CLASS,
        ),
        Classification(
            "71401", "Location de machines-outils, d'outils à main et de matériel de bricolage", Category.CLASS
        ),
        Classification("7140101", "location de machines-outils et de matériel de bricolage", Category.CLASS),
        Classification("7140102", "la location de tondeuses à gazon", Category.CLASS),
        Classification("71402", "Location de vidéocassettes, bandes-vidéo, DVD, disques et CD", Category.CLASS),
        Classification("7140201", "la location de vidéocassettes et bandes-vidéo", Category.CLASS),
        Classification("7140202", "la location de disques, de disques compacts, etc.", Category.CLASS),
        Classification("71403", "Location de téléviseurs et d'autres appareils audiovisuels", Category.CLASS),
        Classification("7140301", "la location de téléviseurs et d'autres appareils audio-visuels", Category.CLASS),
        Classification(
            "71404",
            "Location de vaisselle, couverts, verrerie, articles pour la cuisine et la table, appareils électriques et électroménagers, etc.",
            Category.CLASS,
        ),
        Classification(
            "7140401", "la location de vaisselle, couverts, verrerie, appareils électroménagers, etc.", Category.CLASS
        ),
        Classification("71405", "Location de textiles, d'habillement et de chaussures", Category.CLASS),
        Classification("7140501", "la location de textiles, d'habillement et de chaussures", Category.CLASS),
        Classification(
            "7140502",
            "la location de costumes de scène, de vêtements de carnaval, de vêtements de cérémonie, de bijoux, etc.",
            Category.CLASS,
        ),
        Classification("71406", "Location d'articles de sport et de camping", Category.CLASS),
        Classification("7140601", "la location d'articles de sport et de camping", Category.CLASS),
        Classification("7140602", "la location de bicyclettes", Category.CLASS),
        Classification("7140603", "la location d'embarcations de plaisance", Category.CLASS),
        Classification("71407", "Location de matériel médical et paramédical", Category.CLASS),
        Classification("7140701", "la location de matériel médical et paramédical", Category.CLASS),
        Classification("71408", "Location d'autres biens personnels et domestiques", Category.CLASS),
        Classification("7140801", "la location de décors", Category.CLASS),
        Classification("7140802", "la location de livres et périodiques", Category.CLASS),
        Classification("7140803", "la location de fleurs et plantes", Category.CLASS),
        Classification("7140804", "la location d'instruments de musique", Category.CLASS),
        Classification("7140805", "la location d'autres biens personnels et domestiques,n.d.a.", Category.CLASS),
        Classification("72100", "Conseil en systèmes informatiques", Category.CLASS),
        Classification(
            "7210001",
            "les activités de conseil concernant le type et la configuration du matériel informatique et les applications logicielles: analyse des besoins et des problèmes des utilisateurs et présentation de la so",
            Category.CLASS,
        ),
        Classification("7210002", "les activités des intégrateurs de réseaux", Category.CLASS),
        Classification("72200", "Réalisation de programmes et de logiciels", Category.CLASS),
        Classification(
            "7220001",
            "analyse, conception, programmation et éventuellement édition de systèmes prêts à l'emploi, y compris les d'identification automatique de données: développement, production, fourniture et documentation",
            Category.CLASS,
        ),
        Classification("7220002", "les services de conseil en logiciels", Category.CLASS),
        Classification("7220003", "les services d'assistance à la mise en oeuvre de logiciels", Category.CLASS),
        Classification("72210", "Edition de logiciels", Category.CLASS),
        Classification("72220", "Autres activités de réalisation de logiciels", Category.CLASS),
        Classification("72300", "Traitement de données", Category.CLASS),
        Classification(
            "7230001",
            "le traitement en continu ou non de données à l'aide, soit du programme du client, soit d'un programme propre à un constructeur: service de saisie de données, traitement complet de données",
            Category.CLASS,
        ),
        Classification(
            "7230002",
            "la gestion et l'exploitation en continu de matériel informatique appartenant à des tiers",
            Category.CLASS,
        ),
        Classification("72400", "Activités de banques de données", Category.CLASS),
        Classification(
            "7240001",
            "la création de banques de données par l'assemblage et l'interprétation éventuelle de données provenant d'une ou plusieurs sources: horaires, catalogues, industriels, données scientifiques,information",
            Category.CLASS,
        ),
        Classification(
            "7240002",
            "le stockage de données: préparation d'un enregistrement informatique de ces informations selon une structure prédéterminée",
            Category.CLASS,
        ),
        Classification(
            "7240003",
            "la mise à disposition de banques de données: fournir les données dans un certain ordre ou séquence, par accès direct (on-line), ou rendre les données, triées sur demande, accessibles aux utilisateurs",
            Category.CLASS,
        ),
        Classification(
            "72500", "Entretien et réparation de machines de bureau et de matériel informatique", Category.CLASS
        ),
        Classification(
            "7250001",
            "l'entretien et la réparation d'ordinateurs et de matériel informatique périphérique",
            Category.CLASS,
        ),
        Classification(
            "7250002",
            "l'entretien et la réparation de machines comptables et autres machines de bureau",
            Category.CLASS,
        ),
        Classification("72600", "Autres activités rattachées à l'informatique", Category.CLASS),
        Classification("7260001", "autres activités rattachées à l'informatique", Category.CLASS),
        Classification("73100", "Recherche et développement en sciences physiques et naturelles", Category.CLASS),
        Classification(
            "7310001",
            "les études systématiques et les efforts de création entrepris dans divers types de recherche-développement en sciences naturelles (mathématiques,physiques,astronomie,chimie, sciences médicales et biol",
            Category.CLASS,
        ),
        Classification("73200", "Recherche et développement en sciences humaines et sociales", Category.CLASS),
        Classification(
            "7320001",
            "les études systématiques et les efforts de création entrepris dans divers types de recherche-développement en sciences sociales et humaines (économie, psychologie, sociologie, droit, linguistique et l",
            Category.CLASS,
        ),
        Classification("74111", "Cabinets d'avocats et conseillers juridiques", Category.CLASS),
        Classification("7411101", "cabinets d'avocats et conseillers juridiques", Category.CLASS),
        Classification("74112", "Étude de notaire", Category.CLASS),
        Classification("7411201", "Etude de notaire", Category.CLASS),
        Classification("74113", "Cabinet d'huissier", Category.CLASS),
        Classification("7411301", "cabinet d'huissier", Category.CLASS),
        Classification("74114", "Autre assistance juridique", Category.CLASS),
        Classification("7411401", "autre assistance juridique", Category.CLASS),
        Classification("74121", "Comptables", Category.CLASS),
        Classification(
            "7412101",
            "les activités de conseil en matière comptable et l'organisation des services comptables pour des tiers",
            Category.CLASS,
        ),
        Classification(
            "7412102",
            "l'ouverture, la tenue, la centralisation et la clôture des écritures comptables propres à l'établissement des comptes",
            Category.CLASS,
        ),
        Classification(
            "7412103",
            "la détermination des résultats et la rédaction des comptes annuels dans la forme de requise par les dispositions légales en la matière",
            Category.CLASS,
        ),
        Classification("74122", "Experts-comptables", Category.CLASS),
        Classification(
            "7412201",
            "les activités des membres et des stagiaires de l'Institut des Experts-Comptables",
            Category.CLASS,
        ),
        Classification("74123", "Réviseurs d'entreprises", Category.CLASS),
        Classification(
            "7412301",
            "les activités des membres et des stagiaires de l'Institut des Réviseurs d'entreprises",
            Category.CLASS,
        ),
        Classification("74124", "Conseillers fiscaux", Category.CLASS),
        Classification(
            "7412401",
            "l'établissement de déclarations fiscales pour les particuliers et les entreprises",
            Category.CLASS,
        ),
        Classification(
            "7412402",
            "les activités de conseil et de représentation (autre que la représentation juridique), pour le compte de clients, devant l'administration fiscale",
            Category.CLASS,
        ),
        Classification("74131", "Bureau d'étude de marché", Category.CLASS),
        Classification(
            "7413101",
            "les études portant sur le potentiel commercial de produits, leur acceptation et leur connaissance par le public ainsi que sur les habitudes d'achat des consommateurs aux fins de la promotion des vente",
            Category.CLASS,
        ),
        Classification("7413102", "les analyses statistiques des résultats de ces études", Category.CLASS),
        Classification("74132", "Organisation de sondages", Category.CLASS),
        Classification(
            "7413201",
            "les sondages d'opinion sur les questions politiques, économiques et sociales ainsi que l'analyse statistique des résultats",
            Category.CLASS,
        ),
        Classification("74141", "Bureau de relations publiques", Category.CLASS),
        Classification(
            "7414101",
            "les conseils et l'assistance opérationnelle aux entreprises dans les domaines des relations publiques et de la communication",
            Category.CLASS,
        ),
        Classification(
            "7414102",
            "l'arbitrage et la conciliation entre la direction des entreprises et ses salariés",
            Category.CLASS,
        ),
        Classification("74142", "Autres conseils pour les affaires et le management", Category.CLASS),
        Classification(
            "7414201",
            "les conseils et l'assistance aux entreprises et aux services publics en matière de planification, d'organisation, de recherche du rendement, de contrôle, d'information du gestion, etc.",
            Category.CLASS,
        ),
        Classification(
            "7414202",
            "le calcul des coûts et des profits des mesures proposées en matière de planification, d'organisation, de rendement, etc.",
            Category.CLASS,
        ),
        Classification("7414203", "les activités d'audit général", Category.CLASS),
        Classification(
            "7414204",
            "les conseils en gestion donnés par exemple par des agronomes ou des économistes agricoles auprès d'exploitations agricoles etc.",
            Category.CLASS,
        ),
        Classification("74151", "Activités de gestion et d'administration de holdings", Category.CLASS),
        Classification(
            "7415101",
            "activités de gestion et d'administration de holdings: l'intervention dans la gestion journalière, la représentation des entreprises sur base de la possession ou du contrôle du du capital social et aut",
            Category.CLASS,
        ),
        Classification(
            "7415102",
            "la détention à long terme des actions émanant de plusieurs autres entreprises classées dans différents secteurs économiques",
            Category.CLASS,
        ),
        Classification("74152", "Centres de coordination", Category.CLASS),
        Classification(
            "7415201",
            "centres de coordination: la prestation de services financiers et les activités de management assurées par les étatsmajors régionaux agréés de groupes multinationaux, pour les besoins de leurs propres",
            Category.CLASS,
        ),
        Classification("74201", "Bureau d'architecte", Category.CLASS),
        Classification(
            "7420101", "les activités de conseil en matière d'architecture au maître d'ouvrage", Category.CLASS
        ),
        Classification("7420102", "la conception de bâtiments et l'établissement de plans", Category.CLASS),
        Classification(
            "7420103",
            "la surveillance des travaux de construction (gros oeuvre, installation, travaux de finition, etc.)",
            Category.CLASS,
        ),
        Classification(
            "7420104",
            "les études et le conseil en matière d'aménagement urbain et d'architecture paysagère",
            Category.CLASS,
        ),
        Classification("7420105", "la conception de jardins, de parcs, etc.", Category.CLASS),
        Classification("7420106", "la conduite des opérations de gros entretien des bâtiments", Category.CLASS),
        Classification("74202", "Bureau de géomètre", Category.CLASS),
        Classification("7420201", "les activités des géomètres-experts immobiliers", Category.CLASS),
        Classification("7420202", "les activités des économistes en construction", Category.CLASS),
        Classification(
            "7420203", "l'établissement de levées topographiques et le bornage des propriétés", Category.CLASS
        ),
        Classification("7420204", "le calcul du métré des ouvrages", Category.CLASS),
        Classification("74203", "Études techniques et activités d'ingénierie", Category.CLASS),
        Classification(
            "7420301",
            "la conception et la réalisation de projets intéressant le génie électrique et électronique, le génie minier, le génie chimique, le génie mécanique, le génie industriel, l'ingénierie de systèmes, les t",
            Category.CLASS,
        ),
        Classification("7420302", "le dessin industriel", Category.CLASS),
        Classification(
            "7420303",
            "l'élaboration de projets faisant appel au génie acoustique, aux techniques de la climatisation, de la réfrigération, de l'assainissement et de la lutte contre la pollution, etc.",
            Category.CLASS,
        ),
        Classification(
            "7420304",
            "l'élaboration de projets comportant des activités ayant trait au génie civil ou de bâtiment, au génie hydraulique et à la technique du trafic",
            Category.CLASS,
        ),
        Classification(
            "7420305",
            "les activités géologiques et de prospection: observation et mesures de surface pour recueillir des informations sur la structure du sous-sol et l'emplacement des gisements de pétrole,gaz naturel,minér",
            Category.CLASS,
        ),
        Classification(
            "7420306",
            "les activités de levé géodésique: levé hydrographique, souterrain, de délimitation; cartographie et activ. de collecte de données géographiques, y compris par la photographie aérienne; levé à des fins",
            Category.CLASS,
        ),
        Classification("7420307", "l'établissement de prévisions météorologiques", Category.CLASS),
        Classification(
            "74301",
            "Contrôle technique automobile et autres centres de diagnostic pour véhicules automobiles",
            Category.CLASS,
        ),
        Classification(
            "7430101",
            "contrôle technique automobile et autres centres de diagnostic pour véhicules automobiles",
            Category.CLASS,
        ),
        Classification("74302", "Autres essais et analyses techniques", Category.CLASS),
        Classification(
            "7430201",
            "les essais et les analyses portant sur la composition,caractéristiques physiques,performances,conformité à des textes réglementaires et à des normes ou à un cahier des charges de matériaux, de produit",
            Category.CLASS,
        ),
        Classification(
            "7430202",
            "les essais ou les analyses en laboratoire visant à la vérification du fonctionnement, du vieillissement ou de la sécurité des installations et matériels",
            Category.CLASS,
        ),
        Classification(
            "7430203",
            "la réalisation de mesures concernant la pureté de l'eau ou de l'air, de mesures de la radioactivité et d'autres phénomènes analogues, l'analyse des sources potentielles de la pollution telles que la f",
            Category.CLASS,
        ),
        Classification("7430204", "les activités d'essais dans le domaine de l'hygiène alimentaire", Category.CLASS),
        Classification("7430205", "le contrôle des calculs des éléments de constructions", Category.CLASS),
        Classification(
            "7430206",
            "la certification des navires, des aéronefs, des véhicules automobiles, des conteneurs sous pression, des installations nucléaires, etc.",
            Category.CLASS,
        ),
        Classification("74401", "Agences de publicité", Category.CLASS),
        Classification(
            "7440101",
            "la conception et la réalisation de campagnes publicitaires pour des tiers, en utilisant tous les médias",
            Category.CLASS,
        ),
        Classification(
            "7440102",
            "la création et le placement de publicités: affiches, panneaux publicitaires, journaux lumineux, enseignes lumineuses au néon, affichage sur les autobus, etc.",
            Category.CLASS,
        ),
        Classification("7440103", "la conception de textes et de slogans publicitaires (copywriters)", Category.CLASS),
        Classification("7440104", "la conception de films publicitaires", Category.CLASS),
        Classification("7440105", "la conception d'objets publicitaires", Category.CLASS),
        Classification(
            "7440106",
            "la conception de techniques de publicité visant à toucher le consommateur (marketing direct) au moyen de publicité de personnalisée (publipostage), propositions de téléphoniques d'achat, etc.",
            Category.CLASS,
        ),
        Classification("7440107", "la publicité aérienne", Category.CLASS),
        Classification("74402", "Gestion de supports de publicité", Category.CLASS),
        Classification(
            "7440201",
            "les régies publicitaires de médias pour la vente de temps d'antenne et d'espaces publicitaires",
            Category.CLASS,
        ),
        Classification(
            "7440202",
            "la location d'emplacements à des fins publicitaires sur des panneaux, autour des terrains de sport, dans les halls de gare, etc.",
            Category.CLASS,
        ),
        Classification(
            "7440203",
            "la distribution à domicilie d'échantillons, de prospectus publicitaires et d'autre matériel de publicité, y compris les journaux publicitaires régionaux et similaires",
            Category.CLASS,
        ),
        Classification("74403", "Étalagistes et similaires", Category.CLASS),
        Classification("7440301", "les activités d'étalagiste", Category.CLASS),
        Classification("7440302", "la conception de showrooms, etc.", Category.CLASS),
        Classification("74501", "Sélection de personnel et placement", Category.CLASS),
        Classification(
            "7450101",
            "la recherche, la sélection, l'orientation et le placement de personnel à l'intention de l'employeur potentiel ou du demandeur d'emploi: formulation des descriptions de postes;sélection et examen des c",
            Category.CLASS,
        ),
        Classification(
            "7450102", 'les activités de recherche et de placement de cadres ("chasseurs de têtes")', Category.CLASS
        ),
        Classification(
            "7450103",
            "le placement, pour compte des entreprises, de personnel ayant perdu son travail par suite d'une réorganisation (outplacement)",
            Category.CLASS,
        ),
        Classification(
            "7450104",
            "les services publics pour l'emploi, y compris éventuellement leurs activités de formation professionnelle (Office communautaire et régional de la formation professionnelle et de l'emploi, ORBEM, etc.)",
            Category.CLASS,
        ),
        Classification("7450105", "les agences locales pour l'emploi (ALE)", Category.CLASS),
        Classification("74502", "Agences d'intérimaires et fourniture de personnel temporaire", Category.CLASS),
        Classification(
            "7450201",
            "les activités de placement de main-d'oeuvre temporaire: fourniture à des tiers, sur une base essentiellement temporaire, de personnel recruté et rémunéré par l'agence de travail temporaire",
            Category.CLASS,
        ),
        Classification("74503", "Agences de mannequins, hôtesses et similaires", Category.CLASS),
        Classification("7450301", "agences de mannequins, hôtesses et similaires", Category.CLASS),
        Classification("74601", "Entreprise de gardiennage et service de sécurité", Category.CLASS),
        Classification(
            "7460101",
            "les activités de surveillance, de garde et autres activités de protection des personnes ou des biens: gardes du corps, patrouilles urbaines, surveillance d'habitations, bureaux, usines,chantiers,hôtel",
            Category.CLASS,
        ),
        Classification(
            "7460102",
            "les activités de conseil en matière de sécurité industrielle de sécurité des ménages et des services publics",
            Category.CLASS,
        ),
        Classification("7460103", "le transport de fonds et d'objets précieux", Category.CLASS),
        Classification("7460104", "le dressage des chiens de garde", Category.CLASS),
        Classification("74602", "Service de recherches et bureau de détective", Category.CLASS),
        Classification("7460201", "les activités d'enquête", Category.CLASS),
        Classification("7460202", "les activités des détectives privés", Category.CLASS),
        Classification("74700", "Nettoyage industriel", Category.CLASS),
        Classification(
            "7470001",
            "le nettoyage intérieur de bâtiments de tous types, y compris les bureaux, les usines, les ateliers, les locaux d'institutions et autres locaux à usage commercial ou professionnel ainsi que les immeubl",
            Category.CLASS,
        ),
        Classification("7470002", "le nettoyage des vitres", Category.CLASS),
        Classification(
            "7470003",
            "le ramonage des cheminées et le nettoyage des âtres, des fourneaux, des incinérateurs des chaudières, des gaines de ventilation et des dispositifs d'évacuation de fumées",
            Category.CLASS,
        ),
        Classification(
            "7470004",
            "les activités de désinfection et de destruction des parasites dans les bâtiments, les navires, les trains, etc.",
            Category.CLASS,
        ),
        Classification(
            "7470005",
            "le nettoyage des trains, des autobus, des avions, des navires, etc., y compris les navires pétroliers",
            Category.CLASS,
        ),
        Classification("74811", "Studios et autres activités photographiques", Category.CLASS),
        Classification(
            "7481101",
            "la production photographique réalisée à titre commercial ou privé: photos d'identité,de classe,de mariage,etc.; photogr. publicitaires,d'édition,de mode,à des fins immobilières ou touristiques,etc.; p",
            Category.CLASS,
        ),
        Classification("7481102", "l'exploitation de machines automatiques de photographie", Category.CLASS),
        Classification(
            "7481103",
            "le tournage de reportages vidéo sur des mariages et autres événements similaires",
            Category.CLASS,
        ),
        Classification("74812", "Laboratoires photographiques", Category.CLASS),
        Classification(
            "7481201",
            "le traitement des films: développement, tirage et agrandissement de photos ou de films réalisés par les clients, montage de diapositives, copie, restauration et retouche de photographies et de films",
            Category.CLASS,
        ),
        Classification("74820", "Conditionnement à façon", Category.CLASS),
        Classification(
            "7482001",
            "les activités de conditionnement (automatique ou non) pour des tiers de produits divers: remplissage d'atomiseurs; embouteillage, remplissage de boîtes de boissons; emballage de denrées aliment.(y com",
            Category.CLASS,
        ),
        Classification("7482002", "l'étiquetage, l'estampillage et le scellage", Category.CLASS),
        Classification("7482003", "l'emballage de colis et de paquets-cadeaux", Category.CLASS),
        Classification("74831", "Secrétariats", Category.CLASS),
        Classification("7483101", "les activités de sténographie", Category.CLASS),
        Classification("7483102", "les travaux de dactylographie", Category.CLASS),
        Classification(
            "7483103",
            'les autres travaux de secrétariat tels que la transcription de bandes ou de disques, la copie (y compris les activités des "copycenters"), l\'exécution de calques, de polycopiés et les activités analog',
            Category.CLASS,
        ),
        Classification("7483104", "la domiciliation téléphonique pour compte des entreprises", Category.CLASS),
        Classification("7483105", "la correction sur épreuves", Category.CLASS),
        Classification("74832", "Services de traduction et interprètes", Category.CLASS),
        Classification("7483201", "services de traduction et interprètes", Category.CLASS),
        Classification("74833", "Routage", Category.CLASS),
        Classification(
            "7483301",
            "le mailing direct: l'adressage, la mise sous enveloppe et l'expédition (à partir de fichiers d'adresses constitués ou non par l'unité) de matériau éventuellement publicitaire",
            Category.CLASS,
        ),
        Classification("7483302", "l'adressage et le groupage de journaux et de périodiques", Category.CLASS),
        Classification(
            "7483303",
            "les messageries de journaux et de périodiques et la livraison de ceux-ci à domicile",
            Category.CLASS,
        ),
        Classification("74834", "Secrétariats sociaux", Category.CLASS),
        Classification(
            "7483401",
            "l'accomplissement pour le compte des entreprises des formalités légales en matière de sécurité sociale (inscription à l'ONSS,versement des cotisations,etc) et d'impôts (versement du précompte profess.",
            Category.CLASS,
        ),
        Classification(
            "7483402",
            "l'accomplissement pour le compte des entreprises des obligations légales en matière de pensions des travailleurs, d'allocations familiales, d'assurance accidents de travail, d'assurance maladie-invali",
            Category.CLASS,
        ),
        Classification(
            "7483403",
            "le calcul des salaires, l'établissement d'attestations de travail, d'attestations de chômage, etc.",
            Category.CLASS,
        ),
        Classification("74835", "Autres activités d'administration n.d.a.", Category.CLASS),
        Classification(
            "7483501",
            "l'assistance administratrice aux apprentis pendant leur stage (secrétariats d'apprentissage)",
            Category.CLASS,
        ),
        Classification("7483502", "les activités des offices de tarification", Category.CLASS),
        Classification("7483503", "les autres activités d'administration, n.d.a.", Category.CLASS),
        Classification("74841", "Ventes aux enchères", Category.CLASS),
        Classification(
            "7484101",
            "l'exploitation ou l'organisation de: criées aux fruits, criées horticoles, criées aux poissons, etc.",
            Category.CLASS,
        ),
        Classification(
            "7484102",
            "l'exploitation ou l'organisation de: ventes aux enchères de véhicules automobiles d'occasion",
            Category.CLASS,
        ),
        Classification(
            "7484103", "l'exploitation ou l'organisation de: ventes aux enchères d'objets d'art, etc.", Category.CLASS
        ),
        Classification("74842", "Organisation de salons, expositions et bourses", Category.CLASS),
        Classification(
            "7484201", "l'organisation de foires, d'expositions et de salons professionnels", Category.CLASS
        ),
        Classification("7484202", "l'organisation de défilés de mode", Category.CLASS),
        Classification(
            "7484203",
            "l'organisation de congrès, de rencontres scientifiques ou culturelles, de séminaires, etc.",
            Category.CLASS,
        ),
        Classification("7484204", "l'organisation d'expositions et de défilés d'animaux", Category.CLASS),
        Classification(
            "7484205", "la conception, la fourniture et l'installation de stands d'exposition", Category.CLASS
        ),
        Classification("74843", "Recouvrement de factures et évaluation de la solvabilité", Category.CLASS),
        Classification("7484301", "le recouvrement de factures", Category.CLASS),
        Classification(
            "7484302",
            "l'évaluation de la solvabilité et de la respectabilité d'un particulier ou d'une entreprise",
            Category.CLASS,
        ),
        Classification("74844", "Décorateurs d'intérieurs", Category.CLASS),
        Classification("7484401", "décorateurs d'intérieurs", Category.CLASS),
        Classification("74845", "Centre d'entreprises", Category.CLASS),
        Classification(
            "7484501",
            "les activités d'aide à des jeunes entreprises durant leur période de démarrage: mise à disposition de locaux appropriés à un loyer relativement bas; offre d'une gamme de services collectifs; conseil e",
            Category.CLASS,
        ),
        Classification(
            "74846", "Activités relatives à l'émission de coupons de réduction et de timbres-prime", Category.CLASS
        ),
        Classification(
            "7484601", "activités relatives à l'émission de coupons de réduction et de timbres-prime", Category.CLASS
        ),
        Classification(
            "74847",
            "Création de modèles pour le textile, l'habillement, les bijoux, les meubles et les objets de décoration",
            Category.CLASS,
        ),
        Classification(
            "7484701",
            "la création de modèles pour les articles textiles, les articles d'habillement,les chaussures,les bijoux,les meubles,les objets de décoration intérieure et autres articles de mode ainsi que pour les au",
            Category.CLASS,
        ),
        Classification("7484702", "la réalisation de maquettes et de modèles réduits", Category.CLASS),
        Classification("74848", "Imprésarios et agences de théâtre", Category.CLASS),
        Classification(
            "7484801",
            "les activités exercées par des agents ou des agences pour des particuliers,consistant à obtenir un engagement dans des pièces,films,spectacles,etc., et à placer des livres,oeuvres d'art,photos,etc. ch",
            Category.CLASS,
        ),
        Classification("74849", "Autres services aux entreprises n.d.a.", Category.CLASS),
        Classification(
            "7484901",
            "les activités d'expertise de biens mobiliers, autres que celles qui ont trait à l'assurance",
            Category.CLASS,
        ),
        Classification("7484902", "les activités des lobbyistes", Category.CLASS),
        Classification(
            "7484903",
            "le relèvement de compteurs de consommation (gaz,électricité, eau, calories, etc.) pour le compte de tiers",
            Category.CLASS,
        ),
        Classification(
            "7484904",
            "l'intermédiation en fonds de commerce, c'est-à-dire l'organisation de l'achat ou de la vente de petits et moyens fonds de commerce, y compris de cabinets de professions libérales",
            Category.CLASS,
        ),
        Classification("7484905", "la télévente aux consommateurs pour le compte de tiers", Category.CLASS),
        Classification("7484906", "les autres services fournis principalement aux entreprises n.d.a.", Category.CLASS),
        Classification("74851", "Secrétariats", Category.CLASS),
        Classification("74852", "Services de traduction et interprètes", Category.CLASS),
        Classification("74853", "Routages", Category.CLASS),
        Classification("74854", "Secrétariats sociaux", Category.CLASS),
        Classification("74855", "Autres activités d'administration n.d.a.", Category.CLASS),
        Classification("74860", "Activités de centres d'appels", Category.CLASS),
        Classification(
            "74871",
            "Organisation de marchés particuliers divers, y compris les marchés aux puces et brocantes",
            Category.CLASS,
        ),
        Classification("74872", "Organitation de salons, expositions et bourses", Category.CLASS),
        Classification("74873", "Recouvrement de factures et évoluation de la solvabilité", Category.CLASS),
        Classification("74874", "Décorateurs d'intérieurs", Category.CLASS),
        Classification("74875", "Centre d'entreprises", Category.CLASS),
        Classification(
            "74876", "Activités relatives à l'émission de coupons de réduction et de timbres-prime", Category.CLASS
        ),
        Classification(
            "74877",
            "Création de modèles pour le textile, l'habillement, les bijoux, les meubles et les objets de décoration",
            Category.CLASS,
        ),
        Classification("74878", "Imprésarios et agences de théâtre", Category.CLASS),
        Classification("74879", "Autres services aux entreprises n.d.a", Category.CLASS),
        Classification("75111", "Administration centrale", Category.CLASS),
        Classification("75112", "Administration communautaire et régionale", Category.CLASS),
        Classification("75113", "Administration provinciale", Category.CLASS),
        Classification("75114", "Administration communale, à l'exclusion des C.P.A.S.", Category.CLASS),
        Classification("75115", "C.P.A.S.", Category.CLASS),
        Classification("75116", "Intercommunales à vocation générale", Category.CLASS),
        Classification(
            "75120",
            "Activités d'organismes publics relatives aux soins de santé, à l'environnement, à l'enseignement, à la culture et aux autres matières sociales",
            Category.CLASS,
        ),
        Classification("75130", "Activités d'organismes publics relatives aux matières économiques", Category.CLASS),
        Classification("75140", "Activités de soutien aux administrations", Category.CLASS),
        Classification("75210", "Affaires étrangères", Category.CLASS),
        Classification("75220", "Défense", Category.CLASS),
        Classification("75231", "Tribunaux", Category.CLASS),
        Classification("75232", "Prisons et institutions assimilées", Category.CLASS),
        Classification("75233", "Autres activités relatives à la justice", Category.CLASS),
        Classification("75241", "Services de la sûreté", Category.CLASS),
        Classification("75242", "Gendarmerie", Category.CLASS),
        Classification("75243", "Police", Category.CLASS),
        Classification("75244", "Police fédérale", Category.CLASS),
        Classification("75245", "Police locale", Category.CLASS),
        Classification("75250", "Pompiers et protection civile", Category.CLASS),
        Classification("75301", "Sécurité sociale obligatoire, à l'exclusion des mutuelles", Category.CLASS),
        Classification("75302", "Mutuelles et caisses d'assurance soins", Category.CLASS),
        Classification("75303", "Autres organismes de sécurité sociale", Category.CLASS),
        Classification("80101", "Enseignement fondamental communautaire", Category.CLASS),
        Classification("80102", "Enseignement fondamental provincial", Category.CLASS),
        Classification("80103", "Enseignement fondamental communal", Category.CLASS),
        Classification("80104", "Enseignement fondamental libre subventionné", Category.CLASS),
        Classification("80105", "Enseignement fondamental international", Category.CLASS),
        Classification(
            "80109",
            "Enseignement fondamental et gardien auquel les codes 80.101 à 80.105 ne peuvent être attribués",
            Category.CLASS,
        ),
        Classification("80211", "Enseignement secondaire général communautaire", Category.CLASS),
        Classification("80212", "Enseignement secondaire général provincial", Category.CLASS),
        Classification("80213", "Enseignement secondaire général communal", Category.CLASS),
        Classification("80214", "Enseignement secondaire général libre subventionné", Category.CLASS),
        Classification("80215", "Enseignement secondaire général international", Category.CLASS),
        Classification("80216", "Enseignement secondaire général organisé par les forces armées", Category.CLASS),
        Classification(
            "80219",
            "Enseignement secondaire général auquel les codes 80.211 à 80.216 ne peuvent être attribués",
            Category.CLASS,
        ),
        Classification("80221", "Enseignement secondaire professionnel ou technique communautaire", Category.CLASS),
        Classification("80222", "Enseignement secondaire professionnel ou technique provincial", Category.CLASS),
        Classification("80223", "Enseignement secondaire professionnel ou technique communal", Category.CLASS),
        Classification(
            "80224", "Enseignement secondaire professionnel ou technique libre subventionné", Category.CLASS
        ),
        Classification("80225", "Enseignement secondaire professionnel ou technique international", Category.CLASS),
        Classification(
            "80226", "Enseignement secondaire professionnel ou technique organisé par les forces armées", Category.CLASS
        ),
        Classification("80301", "Enseignement supérieur communautaire", Category.CLASS),
        Classification("80302", "Enseignement supérieur provincial", Category.CLASS),
        Classification("80303", "Enseignement supérieur communal", Category.CLASS),
        Classification("80304", "Enseignement supérieur libre subventionné", Category.CLASS),
        Classification("80305", "Enseignement supérieur international", Category.CLASS),
        Classification("80306", "Enseignement supérieur organisé par les forces armées", Category.CLASS),
        Classification(
            "80309", "Enseignement supérieur auquel les codes 83.301 à 80.306 ne peuvent être attribués", Category.CLASS
        ),
        Classification("80411", "Auto-écoles", Category.CLASS),
        Classification("8041101", "les auto-écoles", Category.CLASS),
        Classification("8041102", "les moto-écoles", Category.CLASS),
        Classification("80412", "Écoles de pilotage de bateaux et d'avions", Category.CLASS),
        Classification("8041201", "la préparation au certificat de pilotage d'avions de tourisme", Category.CLASS),
        Classification("8041202", "la formation aux permis bateaux à voiles et bateaux de plaisance", Category.CLASS),
        Classification("80421", "Formation permanente", Category.CLASS),
        Classification("80422", "Enseignement artistique non classable par niveau", Category.CLASS),
        Classification("80423", "Enseignement par correspondance", Category.CLASS),
        Classification("80424", "Autres formes d'enseignement n.d.a.", Category.CLASS),
        Classification("85110", "Activités hospitalières", Category.CLASS),
        Classification("85120", "Pratique médicale", Category.CLASS),
        Classification("85130", "Pratique dentaire", Category.CLASS),
        Classification("85141", "Laboratoires médicaux", Category.CLASS),
        Classification("85142", "Ambulances", Category.CLASS),
        Classification("85143", "Activités paramédicales, à l'exclusion des kinésithérapeutes", Category.CLASS),
        Classification("85144", "Kinésithérapeutes", Category.CLASS),
        Classification("85145", "Centres de collecte de sang, banques d'organes et similaires", Category.CLASS),
        Classification("85146", "Autres activités relatives aux soins de santé n.d.a.", Category.CLASS),
        Classification("85200", "Activités vétérinaires", Category.CLASS),
        Classification("85311", "Instituts pour mineurs handicapés", Category.CLASS),
        Classification("85312", "Orphelinats", Category.CLASS),
        Classification("85313", "Instituts pour enfants en difficulté", Category.CLASS),
        Classification("85314", "Instituts pour adultes handicapés", Category.CLASS),
        Classification("85315", "Maisons de repos pour personnes âgées", Category.CLASS),
        Classification(
            "8531501",
            "l'accueil et l'hébergement des personnes âgées en hospices, maisons de retraite, homes, pensions, etc.",
            Category.CLASS,
        ),
        Classification("85316", "Autres activités d'action sociale avec hébergement n.d.a.", Category.CLASS),
        Classification(
            "85321",
            "Crèches et garderies d'enfants, y compris les centres de jour pour enfants handicapés",
            Category.CLASS,
        ),
        Classification("8532101", "crèches et garderies d'enfants", Category.CLASS),
        Classification("85322", "Ateliers protégés", Category.CLASS),
        Classification("85323", "Autres activités d'action sociale sans hébergement n.d.a.", Category.CLASS),
        Classification("8532301", "visites à des personnes âgées ou malades", Category.CLASS),
        Classification(
            "85324", "Centres P.M.S. et centres d'orientation ou reformation professionnelle", Category.CLASS
        ),
        Classification("90001", "(null)", Category.CLASS),
        Classification(
            "9000101", "la gestion et l'entretien des égouts et des canalisations d'évacuation", Category.CLASS
        ),
        Classification(
            "9000102",
            "l'évacuation par canalisations, égouts ou autres moyens de produits résiduaires humains ou industriels",
            Category.CLASS,
        ),
        Classification(
            "9000103",
            "la vidange et le nettoyage des puisards et des fosses septiques, l'entretien des toilettes chimiques",
            Category.CLASS,
        ),
        Classification(
            "9000104",
            "le traitement et l'élimination des déchets liquides par dilution, criblage ou filtration, sédimentation, décantation chimique, traitement par boues activées et autres processus",
            Category.CLASS,
        ),
        Classification("9000105", "le traitement des eaux usées de piscines", Category.CLASS),
        Classification("90002", "Ramassage, déversement et traitement des déchets ménagers", Category.CLASS),
        Classification(
            "9000201",
            "l'enlèvement des ordures ménagères solides, des déchets, des détritus et des immondices, y compris le ramassage sélectif de verre, de papier, de produits chimiques et pharmaceutiques, de piles usées,",
            Category.CLASS,
        ),
        Classification(
            "9000202", "l'enlèvement des détritus collectés dans les conteneurs publics à ordures", Category.CLASS
        ),
        Classification(
            "9000203",
            "l'élimination des déchets par incinération ou par d'autres moyens: trituration des déchets, déchargement, immersion, enfouissement, compostage des déchets, traitement et destruction de déchets toxique",
            Category.CLASS,
        ),
        Classification(
            "90003",
            "Ramassage, déversement et traitement des déchets agricoles et industriels et des débris de construction ou de démolition",
            Category.CLASS,
        ),
        Classification(
            "9000301",
            "la collecte et le traitement des déchets et des excédents provenant de l'agriculture et de l'élevage, y compris les activités ayant trait aux excédents de fumier (banques de fumier)",
            Category.CLASS,
        ),
        Classification("9000302", "la fabrication de fumier de vache déshydraté et similaires", Category.CLASS),
        Classification(
            "9000303",
            "la collecte et le traitement des déchets industriels, solides ou liquides, y compris les déchets hautement toxiques: incinération, déchargement, enfouissement, dilution, criblage, filtration, traiteme",
            Category.CLASS,
        ),
        Classification("9000304", "l'enlèvement de l'amiante", Category.CLASS),
        Classification("9000305", "le nettoyage de sols pollués", Category.CLASS),
        Classification("9000306", "l'enlèvement de gravats et de décombres", Category.CLASS),
        Classification("90004", "Gestion des décharges et des sites définitifs de stockage", Category.CLASS),
        Classification("9000401", "gestion des décharges et des sites définitifs de stockage", Category.CLASS),
        Classification("90005", "Nettoyage des rues et déneigement", Category.CLASS),
        Classification(
            "9000501", "le balayage et l'arrosage des chaussées, des aires de stationnement, etc.", Category.CLASS
        ),
        Classification(
            "9000502",
            "l'enlèvement de la neige et de la glace sur les routes et les pistes d'atterrissage, y compris l'épandage de sel et de sable, etc.",
            Category.CLASS,
        ),
        Classification("90010", "Collecte et traitement des eaux usées", Category.CLASS),
        Classification(
            "90021",
            "Ramassage, déversement et traitement des déchets des ménages et des entreprises, des déchets agricoles et des débris de construction ou de démolition",
            Category.CLASS,
        ),
        Classification("90022", "Gestion des décharges et des sites définitifs de stockage", Category.CLASS),
        Classification("90023", "Gestion des décharges et des sites définitifs de stockage", Category.CLASS),
        Classification("90030", "Voirie, dépollution et activités similaires", Category.CLASS),
        Classification("90031", "Nettoyage de la voirie", Category.CLASS),
        Classification("90032", "Dépollution et activités similaires", Category.CLASS),
        Classification("91110", "Activités d'organisations économiques et patronales", Category.CLASS),
        Classification("91120", "Activités d'organisations professionnelles", Category.CLASS),
        Classification("91200", "Activités de syndicats de salariés", Category.CLASS),
        Classification("91310", "Organisations religieuses ou philosophiques", Category.CLASS),
        Classification("91311", "Organisations religieuses", Category.CLASS),
        Classification("91319", "Religieux à charge du budget des cultes", Category.CLASS),
        Classification("91320", "Organisations politiques", Category.CLASS),
        Classification("91330", "Organisations associatives n.d.a.", Category.CLASS),
        Classification("92111", "Production de films cinématographiques", Category.CLASS),
        Classification(
            "9211101",
            "la production et la réalisation de films d'auteurs, courts ou longs métrages, destinés principalement à la projection dans les salles",
            Category.CLASS,
        ),
        Classification("92112", "Production de films pour la télévision", Category.CLASS),
        Classification(
            "9211201",
            "la production et la réalisation de films de tous types (séries, téléfilms, documentaires, etc.) destinés à la diffusion télévisuelle",
            Category.CLASS,
        ),
        Classification("92113", "Production d'autres films", Category.CLASS),
        Classification(
            "9211301",
            "la production et la réalisation de films publicitaires et films promotionnels, films techniques et d'entreprise, films à caractère éducatif ou de formation, clips vidéo",
            Category.CLASS,
        ),
        Classification(
            "9211302",
            "la production et la réalisation de dessins animés par des laboratoires spécialisés",
            Category.CLASS,
        ),
        Classification("92114", "Services annexes à la production de films", Category.CLASS),
        Classification(
            "9211401",
            "les activités connexes à la production de films telles que postsynchronisation, effets spéciaux, développement, montage, coloriage, doublage, etc., exercées pour le compte de tiers",
            Category.CLASS,
        ),
        Classification(
            "9211402",
            "les activités des studios de cinéma, y compris la mise à disposition de matériel technique",
            Category.CLASS,
        ),
        Classification("92120", "Distribution de films", Category.CLASS),
        Classification(
            "9212001",
            "la distribution (vente ou location) de films cinématographiques et de bandes de vidéo à d'autres unités, mais non au public général",
            Category.CLASS,
        ),
        Classification(
            "9212002",
            "les activités liées à la distribution telles que la réservation, la livraison et la conservation de films",
            Category.CLASS,
        ),
        Classification(
            "9212003",
            "l'édition et la distribution de films de tous types sur bandes vidéo à destination du public",
            Category.CLASS,
        ),
        Classification(
            "9212004",
            "la gestion de droits cinématographiques et audiovisuels d'oeuvres réalisées par des tiers",
            Category.CLASS,
        ),
        Classification("92130", "Projection de films cinématographiques", Category.CLASS),
        Classification(
            "9213001",
            "la projection de films cinématographiques ou de bandes de vidéo dans des salles de cinéma, en plein air ou dans d'autres installations de projection",
            Category.CLASS,
        ),
        Classification("9213002", "les activités des ciné-clubs", Category.CLASS),
        Classification("92201", "Production et diffusion de programmes de radio", Category.CLASS),
        Classification(
            "9220101",
            "la production de programmes de radio, que cette production soit combinée ou non avec des activités de diffusion",
            Category.CLASS,
        ),
        Classification("9220102", "les activités des radios locales et des radios libres", Category.CLASS),
        Classification("92202", "Production de programmes de télévision", Category.CLASS),
        Classification(
            "9220201", "la production de programmes de télévision non diffusés par leur producteur", Category.CLASS
        ),
        Classification("9220202", "les activités des maisons de production indépendantes", Category.CLASS),
        Classification("92203", "Émission de programmes de télévision", Category.CLASS),
        Classification(
            "9220301",
            "l'émission de programmes de télévision par des chaînes subventionnées ou par des chaînes appartenant au secteur privé, que cette émission soit combinée ou non avec des activités de production",
            Category.CLASS,
        ),
        Classification(
            "9220302",
            "les activités dans la domaine da la production et de l'émission de programmes de télévision exercées par: les chaînes régionales et locales, les chaînes payantes",
            Category.CLASS,
        ),
        Classification("92204", "Production et diffusion de programmes de radio et de télévision", Category.CLASS),
        Classification("92311", "Artistes indépendants", Category.CLASS),
        Classification("92312", "Production de spectacles par des ensembles artistiques", Category.CLASS),
        Classification("92313", "Services annexes à l'art dramatique et à la musique", Category.CLASS),
        Classification("92321", "Exploitation de salles de théâtre, de concert et similaires", Category.CLASS),
        Classification(
            "9232101",
            "l'exploitation de salles de concert, de théâtre,music-halls, cabarets et autres salles de spectacles",
            Category.CLASS,
        ),
        Classification(
            "9232102", "l'exploitation d'agences de vente de billets et de réservations de places", Category.CLASS
        ),
        Classification(
            "9232103", "l'exploitation de studios d'enregistrements sonores pour compte de tiers", Category.CLASS
        ),
        Classification("92322", "Gestion et exploitation de centres culturels", Category.CLASS),
        Classification("9232201", "la gestion et l'exploitation de centres culturels", Category.CLASS),
        Classification(
            "9232202",
            "la gestion et l'exploitation de centres polyvalents, principalement destinés à des activités dans le domaine de l'art dramatique et de la musique",
            Category.CLASS,
        ),
        Classification("92331", "Attractions foraines", Category.CLASS),
        Classification("9233101", "attractions foraines", Category.CLASS),
        Classification("92332", "Parcs d'attractions", Category.CLASS),
        Classification("9233201", "l'exploitation de parcs d'attractions", Category.CLASS),
        Classification("9233202", "l'exploitation de chemins de fer touristiques", Category.CLASS),
        Classification("92340", "Autres activités de spectacle et d'amusement n.d.a.", Category.CLASS),
        Classification(
            "9234001", "l'exploitation d'écoles de danse et les activités des professeurs de danse", Category.CLASS
        ),
        Classification(
            "9234002",
            "l'organisation d'activités récréatives n.d.a.: spectacles de cirque, spectacles de marionnettes, rodéos, spectacles \"son et lumière\", etc.",
            Category.CLASS,
        ),
        Classification("92400", "Agences de presse", Category.CLASS),
        Classification(
            "9240001",
            "les activités des agences de presse, c'est-à-dire la communication aux médias d'informations, de photos",
            Category.CLASS,
        ),
        Classification(
            "9240002", "les activités des journalistes et des photographes de presse indépendants", Category.CLASS
        ),
        Classification("92510", "Gestion des bibliothèques et archives publiques", Category.CLASS),
        Classification(
            "9251001", "la recherche et gestion de collections d'ouvrages spécialisés ou non", Category.CLASS
        ),
        Classification("9251002", "la tenue des archives historiques", Category.CLASS),
        Classification("9251003", "l'établissement de catalogues", Category.CLASS),
        Classification(
            "9251004",
            "prêt à stockage de livres, de cartes, de périodiques, de films, de disques, de bandes magnétiques, d'oeuvres d'art, etc.",
            Category.CLASS,
        ),
        Classification(
            "9251005", "activités de recherche visant à répondre aux demandes d'information", Category.CLASS
        ),
        Classification("92520", "Gestion des musées et du patrimoine culturel", Category.CLASS),
        Classification(
            "9252001", "la préservation de sites (y compris les fouilles) et de bâtiments historiques", Category.CLASS
        ),
        Classification("9252002", "la conservation de monuments historiques", Category.CLASS),
        Classification(
            "9252003",
            "la gestion des musées de toute nature, y compris les musées en plein air: musées d'art,d'orfèvrerie,de meubles,de costumes,de céramiques,d'argenterie,etc.; musées d'histoire naturelle,des sciences,des",
            Category.CLASS,
        ),
        Classification("92530", "Jardins botaniques, zoologiques et réserves naturelles", Category.CLASS),
        Classification("9253001", "la conservation du patrimoine naturel", Category.CLASS),
        Classification(
            "9253002",
            "la gestion de jardins botaniques et zoologiques, des zoos pour enfants, des réserves et parcs naturels, y compris la protection de la flore et de la faune",
            Category.CLASS,
        ),
        Classification(
            "9253003", "l'exploitation d'autres curiosités touristiques (grottes et similaires)", Category.CLASS
        ),
        Classification("92611", "Gestion et exploitation de centres sportifs", Category.CLASS),
        Classification(
            "9261101",
            "la gestion et l'exploitation de centres sportifs destinés à accueillir des événements ou des disciplines sportifs de toute nature",
            Category.CLASS,
        ),
        Classification(
            "9261102",
            "la gestion et l'exploitation de centres polyvalents, principalement destinés à la pratique du sport",
            Category.CLASS,
        ),
        Classification("92612", "Exploitation de centres de fitness et salles de gymnastique", Category.CLASS),
        Classification(
            "9261201",
            "l'exploitation de salles de gymnastique et de centres de fitness, de musculation, d'aérobic, de body-building, etc., y compris l'accompagnement de la clientèle sur le plan sportif",
            Category.CLASS,
        ),
        Classification("92613", "Exploitation d'autres installations sportives", Category.CLASS),
        Classification(
            "9261301",
            "l'exploitation de stades de football, piscines, stades d'athlétisme, établissements de bowling, terrains de golf, courts de tennis, patinoires, stands de tir, salles et arènes spécialisées, etc.",
            Category.CLASS,
        ),
        Classification("9261302", "l'exploitation de ports de plaisance et aérodromes de tourisme", Category.CLASS),
        Classification("9261303", "l'exploitation de viviers, hippodromes et manèges", Category.CLASS),
        Classification("9261304", "l'exploitation de circuits automobiles, vélodromes, etc.", Category.CLASS),
        Classification("92621", "Activités de clubs de sport et d'associations sportives", Category.CLASS),
        Classification(
            "9262101",
            "l'organisation et la gestion d'activités sportives: clubs de football,de cyclisme,de bowling,de natation,de golf,de boxe, de lutte et autres arts martiaux,de musculation,associations de sports d'hiver",
            Category.CLASS,
        ),
        Classification(
            "9262102",
            "les activités liées aux courses et concours d'animaux (cheveux, lévriers, pigeons, etc.)",
            Category.CLASS,
        ),
        Classification(
            "9262103", "les activités liées aux sport mécaniques (automobiles, motos, karts, etc.)", Category.CLASS
        ),
        Classification(
            "9262104",
            "la pratique de la chasse et de la pêche en tant que sports ou activités de loisir",
            Category.CLASS,
        ),
        Classification(
            "9262105",
            "les activités liées aux régates, ski nautique, jetski, deltaplane, vol à voile, vol en ULM, en avion de tourisme ou de sport, etc.",
            Category.CLASS,
        ),
        Classification("92622", "Sportifs indépendants, instructeurs de sport et managers sportifs", Category.CLASS),
        Classification("92623", "Autres activités sportives", Category.CLASS),
        Classification(
            "9262301",
            "la promotion et l'organisation d'événements sportifs tant pour compte propre que pour le compte de tiers",
            Category.CLASS,
        ),
        Classification("9262302", "les activités de services connexes", Category.CLASS),
        Classification("92710", "Jeux de hasard et d'argent", Category.CLASS),
        Classification("9271001", "l'organisation de loteries, lotos, pronostics,paris mutuels, etc.", Category.CLASS),
        Classification("9271002", "l'exploitation de casinos et de salles de jeux", Category.CLASS),
        Classification(
            "9271003", "l'exploitation de machines à sous basées sur le hasard avec gain d'argent", Category.CLASS
        ),
        Classification(
            "9271004",
            "les activités liées à la vente de billets de loterie, la distribution et la collecte de bulletins de participation, etc.",
            Category.CLASS,
        ),
        Classification("92721", "Exploitation de salles de billards", Category.CLASS),
        Classification("9272101", "exploitation de salles de billards", Category.CLASS),
        Classification("92722", "Exploitation de parcs de récréation, lunaparcs et similaires", Category.CLASS),
        Classification(
            "9272201",
            "l'exploitation de jeux, automatiques ou non (flippers, jeux électroniques, baby foot, etc.) en principe sans gain d'argent",
            Category.CLASS,
        ),
        Classification(
            "92723",
            "Exploitation d'infrastructures de plage, de bicyclettes, pédalos, poneys et similaires",
            Category.CLASS,
        ),
        Classification(
            "9272301",
            "l'exploitation d'infrastructures de plage (location de cabines de bain, paravents, sièges, etc.)",
            Category.CLASS,
        ),
        Classification(
            "9272302",
            "la mise à disposition à des fins récréatives de pédalos, barques, bicyclettes, poneys, etc.",
            Category.CLASS,
        ),
        Classification("92724", "Autres activités récréatives", Category.CLASS),
        Classification(
            "9272401",
            "l'engagement et le placement d'acteurs pour les films cinématographiques, les émissions de télévision et les pièces de théâtre",
            Category.CLASS,
        ),
        Classification("9272402", "les autres activités liées aux loisirs non classées ailleurs", Category.CLASS),
        Classification("93011", "Blanchisseries, teintureries et similaires", Category.CLASS),
        Classification(
            "9301101",
            "lavage,blanchissage,nettoyage à sec,repassage,teinture,etc., des habits et textiles pour les entreprises,les utilisateurs professionels ou les exploitants de dépôts qui acceptent le le linge des parti",
            Category.CLASS,
        ),
        Classification("9301102", "le ramassage et la livraison du linge", Category.CLASS),
        Classification("9301103", "le nettoyage d'articles en cuir ou en fourrure", Category.CLASS),
        Classification("9301104", "le nettoyage des tapis, des moquettes, des tentures et des rideaux", Category.CLASS),
        Classification(
            "9301105",
            "la réparation de vêtements et d'autres articles textiles ou les petites retouches apportées à ces articles lorsqu'elles sont faites en liaison avec le nettoyage",
            Category.CLASS,
        ),
        Classification(
            "9301106",
            "la location, par les blanchisseries, de linge, de vêtements de travail et d'articles similaires",
            Category.CLASS,
        ),
        Classification(
            "93012",
            "Salons-lavoirs, blanchisseries, services de nettoyage de vêtements, linges et autres textiles pour particuliers",
            Category.CLASS,
        ),
        Classification("9301201", "le service des laveries automatiques en libre service", Category.CLASS),
        Classification(
            "9301202",
            "le traitement (ramassage, lavage, repassage, livraison à domicile, etc.) du linge à une échelle non industrielle et le nettoyage d'articles d'habillement pour le compte de particuliers",
            Category.CLASS,
        ),
        Classification(
            "93013",
            "Magasins-dépôts pour le nettoyage des vêtements, linges et autres textiles des particuliers",
            Category.CLASS,
        ),
        Classification(
            "9301301",
            "les exploitants de magasins-dépôts qui n'exercent eux-mêmes aucune activité ayant trait au lavage ou au nettoyage mais qui confient le traitement du linge et le nettoyage des vêtements aux laveries et",
            Category.CLASS,
        ),
        Classification("93021", "Salons de coiffure", Category.CLASS),
        Classification(
            "9302101",
            "la coiffure pour hommes, femmes et enfants (coupe, shampooing, soins capillaires, coloration, ondulation, etc.)",
            Category.CLASS,
        ),
        Classification("93022", "Instituts de beauté", Category.CLASS),
        Classification(
            "9302201",
            "les conseils en beauté et les soins du visage: massages fasciaux, traitement anti-rides, maquillage, etc.",
            Category.CLASS,
        ),
        Classification("9302202", "les soins de la peau et l'épilation", Category.CLASS),
        Classification("9302203", "les soins de manucure et de pédicure", Category.CLASS),
        Classification("93031", "Entreprises de pompes funèbres", Category.CLASS),
        Classification(
            "9303101",
            "les soins aux défunts: la préparation des corps pour la sépulture ou l'incinération, l'embaumement, etc.",
            Category.CLASS,
        ),
        Classification(
            "9303102",
            "les services connexes à l'inhumation et l'incinération: la location de locaux aménagés dans les funérariums, etc.",
            Category.CLASS,
        ),
        Classification("9303103", "les services d'inhumation et d'incinération des défunts", Category.CLASS),
        Classification("9303104", "les services funéraires aux animaux", Category.CLASS),
        Classification("93032", "Gestion de cimetières et crématoriums", Category.CLASS),
        Classification("9303201", "la location ou vente de concessions", Category.CLASS),
        Classification("9303202", "la gestion et l'entretien des cimetières", Category.CLASS),
        Classification(
            "9303203",
            "les services fournis par les crématoriums (incinération, dispersion des cendres, columbarium, etc.)",
            Category.CLASS,
        ),
        Classification("93040", "Autres soins corporels", Category.CLASS),
        Classification(
            "9304001",
            "les services liés au bien-être et au confort physique tels que ceux fournis dans les établissements de thalassothérapie,les stations thermales,les bains turcs,les saunas, les bains de vapeur,les solar",
            Category.CLASS,
        ),
        Classification(
            "93051",
            "Agences matrimoniales, agences de rencontres, services d'escorte, activités d'hôtesses  et autres activités similaires liées à la vie sociale",
            Category.CLASS,
        ),
        Classification(
            "9305101", "agences matrimoniales, agences de rencontres, services d'escorte et similaires", Category.CLASS
        ),
        Classification("93052", "Graphologues, astrologues, voyants, radiesthésistes et similaires", Category.CLASS),
        Classification("9305201", "graphologues, astrologues, voyants, radiesthésistes et similaires", Category.CLASS),
        Classification("93053", "Autres services  n.d.a.", Category.CLASS),
        Classification("9305301", "les services de recherche généalogique", Category.CLASS),
        Classification("9305302", "les services de tatouement", Category.CLASS),
        Classification(
            "9305303",
            "les concessions diverses, notamment sur la voie publique cireurs, porteurs, etc.) ou à l'intérieur des bâtiments accessibles au public (vestiaires, toilettes, etc.)",
            Category.CLASS,
        ),
        Classification(
            "9305304", "le dressage et l'entraînement d'animaux de compagnie et de chiens d'aveugles", Category.CLASS
        ),
        Classification("95000", "Activités des ménages en tant qu'employeurs de personnel domestique", Category.CLASS),
        Classification("95001", "Personnel occupé à des tâches ménagères", Category.CLASS),
        Classification("95002", "Personnel occupé à des travaux d'ordre non ménager", Category.CLASS),
        Classification("95003", "Personnel occupé dans des domaines et jardins privés", Category.CLASS),
        Classification(
            "96000",
            "Activités indifférenciées des ménages en tant que producteurs de biens pour usage propre",
            Category.CLASS,
        ),
        Classification(
            "97000",
            "Activités indifférenciées des ménages en tant que producteurs de biens pour usage propre",
            Category.CLASS,
        ),
        Classification("98901", "Chômeurs en réadaptation professionnelle", Category.CLASS),
        Classification(
            "98902",
            "Travailleurs bénéficiant d'indemnités ou de rentes d'accident de travail ou de maladie professionnelle",
            Category.CLASS,
        ),
        Classification("98903", "Travailleurs bénéficiant d'autres prestations", Category.CLASS),
        Classification(
            "98904",
            "C.S.T., T.C.T., PRIME, jeunes stagiaires d'entreprises publiques soumises à un plan d'assainissement",
            Category.CLASS,
        ),
        Classification("98905", "Activités mal définies", Category.CLASS),
        Classification("99000", "Organismes extra-territoriaux", Category.CLASS),
    ],
)
