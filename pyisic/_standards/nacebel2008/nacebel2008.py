"""`NACEBEL2008 Standard <https://economie.fgov.be/sites/default/files/Files/Entreprises/KBO/conversiontable-Nacebel-2003-2008.xls>`_.
"""
from ...types import Category, Classification, Standard, Standards

NACEBEL2008 = Standard(
    standard=Standards.NACEBEL2008,
    classes=[
        Classification(
            "01110",
            "Culture de céréales (à l'exception du riz), de légumineuses et de graines oléagineuses",
            Category.CLASS,
        ),
        Classification("01120", "Culture du riz", Category.CLASS),
        Classification("01130", "Culture de légumes, de melons, de racines et de tubercules", Category.CLASS),
        Classification("01140", "Culture de la canne à sucre", Category.CLASS),
        Classification("01150", "Culture du tabac", Category.CLASS),
        Classification("01160", "Culture de plantes à fibres", Category.CLASS),
        Classification("01199", "Autres cultures non permanentes n.c.a.", Category.CLASS),
        Classification("01260", "Culture de fruits oléagineux", Category.CLASS),
        Classification(
            "01280", "Culture de plantes à épices, aromatiques, médicinales et pharmaceutiques", Category.CLASS
        ),
        Classification("01290", "Autres cultures permanentes", Category.CLASS),
        Classification("01630", "Traitement primaire des récoltes", Category.CLASS),
        Classification("01640", "Traitement des semences", Category.CLASS),
        Classification(
            "0111001",
            "Culture de céréales (à l'exception du riz) : blé dur, blé tendre, seigle, orge, avoine, maïs, etc.",
            Category.CLASS,
        ),
        Classification("0113011", "Culture de pommes de terre", Category.CLASS),
        Classification(
            "0111002",
            "Culture de graines oléagineuses et de légumineuses : arachides, fèves de soja, fèves de colza, etc.",
            Category.CLASS,
        ),
        Classification(
            "0113012", "Culture de racines et de tubercules à forte teneur en amidon ou en inuline", Category.CLASS
        ),
        Classification(
            "0111003", "Culture de légumes à cosse secs tels que pois fourragers et haricots", Category.CLASS
        ),
        Classification(
            "0128021",
            "Culture de plantes à usage pharmaceutique ou insecticide, parasiticide ou similaire",
            Category.CLASS,
        ),
        Classification("0111004", "Production de semences céréalières", Category.CLASS),
        Classification("0111005", "Cultures n.d.a.", Category.CLASS),
        Classification("02300", "Récolte de produits forestiers non ligneux poussant à l'état sauvage", Category.CLASS),
        Classification(
            "0128001",
            "Culture de condiments : câpres, poivrons, fenouil, persil, cerfeuil, estragon, marjolaine, etc.",
            Category.CLASS,
        ),
        Classification("0113001", "Culture des champignons et des truffes", Category.CLASS),
        Classification("0113002", "Production de semences de légumes", Category.CLASS),
        Classification("01191", "Culture de fleurs", Category.CLASS),
        Classification("0119101", "Culture de fleurs et de fleurs à couper", Category.CLASS),
        Classification("0119102", "Fabrication de fleurs séchées", Category.CLASS),
        Classification("0119103", "Production de semences de fleurs", Category.CLASS),
        Classification("01301", "Exploitation de pépinières, sauf pépinières forestières", Category.CLASS),
        Classification("01250", "Culture d'autres fruits d'arbres ou d'arbustes et de fruits à coque", Category.CLASS),
        Classification("01309", "Autre reproduction de plantes", Category.CLASS),
        Classification("02100", "Sylviculture et autres activités forestières", Category.CLASS),
        Classification(
            "0130901",
            "Culture de plantes destinées à la plantation et à l'ornementation : buissons, arbustes, plantes ornementales d'intérieur, arbres, etc.",
            Category.CLASS,
        ),
        Classification("0130902", "Culture de gazon en rouleaux", Category.CLASS),
        Classification("01240", "Culture de fruits à pépins et à noyau", Category.CLASS),
        Classification("01210", "Culture de la vigne", Category.CLASS),
        Classification("01220", "Culture de fruits tropicaux et subtropicaux", Category.CLASS),
        Classification("01230", "Culture d'agrumes", Category.CLASS),
        Classification("01270", "Culture de plantes à boissons", Category.CLASS),
        Classification("10410", "Fabrication d'huiles et de graisses", Category.CLASS),
        Classification("11020", "Production de vin (de raisin)", Category.CLASS),
        Classification(
            "0124001", "Culture de fruits : pommes, poires, abricots, cerises, pêches, etc.", Category.CLASS
        ),
        Classification("0121001", "Culture de raisins de cuve et de raisins de table", Category.CLASS),
        Classification(
            "0128011",
            "Culture de plantes pour épices : laurier, basilic, anis, coriandre, cumin, cannelle, clous de girofle, noix muscade, gingembre, etc.",
            Category.CLASS,
        ),
        Classification("01410", "Élevage de vaches laitières", Category.CLASS),
        Classification("01420", "Élevage d'autres bovins et de buffles", Category.CLASS),
        Classification("0141001", "Élevage de vaches laitières", Category.CLASS),
        Classification("0141002", "Production de lait cru de vache ou de bufflonne", Category.CLASS),
        Classification("01450", "Élevage d'ovins et de caprins", Category.CLASS),
        Classification("01430", "Élevage de chevaux et d'autres équidés", Category.CLASS),
        Classification("01490", "Élevage d'autres animaux", Category.CLASS),
        Classification("0145001", "Elevage d'ovins et de caprins", Category.CLASS),
        Classification("0145002", "Production de laine brute", Category.CLASS),
        Classification("0145003", "Production de lait cru de brebis et de chèvre", Category.CLASS),
        Classification("01461", "Élevage de porcs reproducteurs", Category.CLASS),
        Classification("0146101", "Elevage de porcs reproducteurs, y compris l'élevage de sangliers", Category.CLASS),
        Classification("01462", "Élevage de porcs à l'engrais", Category.CLASS),
        Classification(
            "0146201", "Elevage de porcs à l'engrais, y compris l'engraissement pour le compte de tiers", Category.CLASS
        ),
        Classification("01471", "Élevage de poules", Category.CLASS),
        Classification("01472", "Production d'oeufs de volailles", Category.CLASS),
        Classification("01479", "Élevage de volailles, sauf poules", Category.CLASS),
        Classification("01440", "Élevage de chameaux et d'autres camélidés", Category.CLASS),
        Classification("03220", "Aquaculture en eau douce", Category.CLASS),
        Classification("0149001", "Elevage d'abeilles et la production de miel et de cire d'abeilles", Category.CLASS),
        Classification("0149002", "Elevage de lapins", Category.CLASS),
        Classification("0149003", "Elevage d'animaux domestiques (à l'exception des poissons)", Category.CLASS),
        Classification("0149004", "Elevage d'animaux à fourrure", Category.CLASS),
        Classification("0149005", "Elevage de gibier dans les fermes d'élevage", Category.CLASS),
        Classification("0149006", "Elevage d'escargots", Category.CLASS),
        Classification("0149007", "Elevage d’autres animaux n.c.a.", Category.CLASS),
        Classification("01500", "Culture et élevage associés", Category.CLASS),
        Classification(
            "0150001",
            "Culture associée à l'élevage de bétail, pour autant que le chiffre d'affaires d'une de ces deux activités n'atteigne pas les 2/3 du chiffre d'affaires total",
            Category.CLASS,
        ),
        Classification("81300", "Services d'aménagement paysager", Category.CLASS),
        Classification("01610", "Activités de soutien aux cultures", Category.CLASS),
        Classification(
            "10392", "Transformation et conservation de fruits, sauf fabrication de fruits surgelés", Category.CLASS
        ),
        Classification("0161001", "Préparation des terres", Category.CLASS),
        Classification("0161002", "Création de cultures", Category.CLASS),
        Classification("0161003", "Pulvérisation des récoltes, y compris par voie aérienne", Category.CLASS),
        Classification(
            "0161007",
            "Lutte contre les animaux nuisibles (y compris les lapins) en relation avec l'agriculture",
            Category.CLASS,
        ),
        Classification("0161004", "Taille des arbres fruitiers et des vignes", Category.CLASS),
        Classification("0161005", "Transplantation du riz et démariage des betteraves", Category.CLASS),
        Classification(
            "0163001",
            "Préparation des cultures en vue de leur commercialisation primaire : nettoyage, taille, triage, désinfection",
            Category.CLASS,
        ),
        Classification("8130001", "Elagage des arbres et des haies", Category.CLASS),
        Classification("0161008", "Exploitation de systèmes d'irrigation pour l’agriculture", Category.CLASS),
        Classification(
            "8130002",
            "Création et entretien de jardins, de parcs et d'espaces verts pour installations sportives",
            Category.CLASS,
        ),
        Classification("0161006", "Location de machines et d'équipements agricoles avec opérateur", Category.CLASS),
        Classification("01620", "Activités de soutien à la production animale", Category.CLASS),
        Classification("0162001", "Activités en rapport avec l'insémination artificielle", Category.CLASS),
        Classification("0162002", "Tonte d'ovins pour le compte de tiers", Category.CLASS),
        Classification(
            "0162003",
            "Services de conduite de troupeaux, services de paissance, services de nettoyage des poulaillers, etc.",
            Category.CLASS,
        ),
        Classification("9609501", "Hébergement d'animaux de compagnie", Category.CLASS),
        Classification("9609301", "Toilettage d'animaux domestiques", Category.CLASS),
        Classification("01700", "Chasse, piégeage et services annexes", Category.CLASS),
        Classification("94999", "Autres associations n.c.a.", Category.CLASS),
        Classification(
            "0170001",
            "Chasse ou piégeage d'animaux pour l'alimentation commerciale, leur fourrure, leur peau, ou destinés à des centres de recherche ou des parcs zoologiques, ou utilisés comme animaux de compagnie",
            Category.CLASS,
        ),
        Classification(
            "0210001",
            "Sylviculture sur pied : boisement, reboisement, transplantation, coupe d'éclaircie et conservation des forêts et des coupes",
            Category.CLASS,
        ),
        Classification("0210002", "Culture de taillis et de bois de trituration", Category.CLASS),
        Classification("0210003", "Exploitation de pépinières forestières", Category.CLASS),
        Classification("0129001", "Culture de végétaux pour la sparterie", Category.CLASS),
        Classification("02200", "Exploitation forestière", Category.CLASS),
        Classification("16100", "Sciage et rabotage du bois", Category.CLASS),
        Classification(
            "0220001",
            "Exploitation forestière : abattage d'arbres et production de bois brut tels que les bois de mine, les échalas fendus, les piquets et les bois de chauffage",
            Category.CLASS,
        ),
        Classification("02400", "Services de soutien à l'exploitation forestière", Category.CLASS),
        Classification(
            "0240001", "Inventaire des forêts, évaluation du bois, protection contre les incendies", Category.CLASS
        ),
        Classification("0240002", "Transport de grumes dans les forêts", Category.CLASS),
        Classification("03110", "Pêche en mer", Category.CLASS),
        Classification("03120", "Pêche en eau douce", Category.CLASS),
        Classification("0311001", "Pêche en haute mer et côtière", Category.CLASS),
        Classification("0311002", "Ramassage en mer de crustacés et de mollusques", Category.CLASS),
        Classification(
            "0311003",
            "Activités des services annexes à la pêche en mer à l'exclusion des services de soutien à la pêche sportive ou récréative",
            Category.CLASS,
        ),
        Classification("03210", "Aquaculture en mer", Category.CLASS),
        Classification(
            "0321001",
            "Production de naissains d'huîtres, de moules, de jeunes langoustes, de larve de crevettes, d'alevins et de saumoneaux",
            Category.CLASS,
        ),
        Classification("0321002", "Culture d'algues et autres plantes aquatiques comestibles", Category.CLASS),
        Classification("0322001", "Pisciculture en eau douce", Category.CLASS),
        Classification("09900", "Activités de soutien aux autres industries extractives", Category.CLASS),
        Classification("05100", "Extraction de houille", Category.CLASS),
        Classification("19200", "Raffinage du pétrole", Category.CLASS),
        Classification("0510001", "Lavage, calibrage, triage, pulvérisation, etc., de la houille", Category.CLASS),
        Classification("0510002", "Agglomération de la houille", Category.CLASS),
        Classification("05200", "Extraction de lignite", Category.CLASS),
        Classification("08920", "Extraction de tourbe", Category.CLASS),
        Classification("0892001", "Production de tourbe pour l'horticulture", Category.CLASS),
        Classification("09100", "Activités de soutien à l'extraction d'hydrocarbures", Category.CLASS),
        Classification("06100", "Extraction de pétrole brut", Category.CLASS),
        Classification("06200", "Extraction de gaz naturel", Category.CLASS),
        Classification("52210", "Services auxiliaires des transports terrestres", Category.CLASS),
        Classification("52220", "Services auxiliaires des transports par eau", Category.CLASS),
        Classification("0620001", "Extraction de condensats", Category.CLASS),
        Classification("0620002", "Décantation et la séparation de fractions d'hydrocarbures liquides", Category.CLASS),
        Classification(
            "0910001", "Forage et reforage dirigés liés à l'extraction du pétrole et du gaz", Category.CLASS
        ),
        Classification("0910002", "Montage in situ, réparation et démontage de tours de forage", Category.CLASS),
        Classification("07210", "Extraction de minerais d'uranium et de thorium", Category.CLASS),
        Classification("07100", "Extraction de minerais de fer", Category.CLASS),
        Classification("07290", "Extraction d'autres minerais de métaux non ferreux", Category.CLASS),
        Classification("08111", "Extraction de pierres ornementales et de construction", Category.CLASS),
        Classification(
            "0811101",
            "Extraction, taille grossière et sciage de pierres de taille pour les entreprises de travail de la pierre ou pour la construction, telles que le marbre, le granit, le grès, etc.",
            Category.CLASS,
        ),
        Classification("08112", "Extraction de pierres calcaires, de gypse, de craie et d'ardoise", Category.CLASS),
        Classification("0811201", "Extraction, broyage et concassage des pierres à ciment", Category.CLASS),
        Classification("0811211", "Extraction, broyage et concassage des pierres calcaires", Category.CLASS),
        Classification("0811212", "Extraction de dolomie non calcinée", Category.CLASS),
        Classification("0811221", "Extraction d'ardoise", Category.CLASS),
        Classification("08122", "Extraction de sable", Category.CLASS),
        Classification(
            "0812201",
            "Extraction de sables industriels et de sables pour la construction, dans des carrières ou par dragage",
            Category.CLASS,
        ),
        Classification("08121", "Extraction de gravier", Category.CLASS),
        Classification("0812101", "Extraction de graviers dans des carrières ou par dragage", Category.CLASS),
        Classification("0812102", "Concassage et broyage de graviers", Category.CLASS),
        Classification("08123", "Extraction d'argiles et de kaolin", Category.CLASS),
        Classification("08910", "Extraction des minéraux chimiques et d'engrais minéraux", Category.CLASS),
        Classification("10840", "Fabrication de condiments et d'assaisonnements", Category.CLASS),
        Classification("08930", "Production de sel", Category.CLASS),
        Classification("08990", "Autres activités extractives n.c.a.", Category.CLASS),
        Classification(
            "0899001",
            "Extraction de minéraux et de matériaux divers : terraux et humus, mat. abrasives, amiante, farines siliceuses fossiles, graphite naturel, stéatite (talc), feldspath, pierres gemmes, quartz, mica, etc.",
            Category.CLASS,
        ),
        Classification(
            "10110",
            "Transformation et conservation de la viande de boucherie, à l'exclusion de la viande de volaille",
            Category.CLASS,
        ),
        Classification("1011001", "Abattage des animaux", Category.CLASS),
        Classification("1011002", "Production de viandes fraîches, en carcasses ou en morceaux", Category.CLASS),
        Classification("1011003", "Production de cuirs et de peaux bruts provenant des abattoirs", Category.CLASS),
        Classification(
            "1011004", "Fonte et raffinage du saindoux et d'autres graisses animales comestibles", Category.CLASS
        ),
        Classification(
            "1011005",
            "Transformation des abats et charognes ; la production de farine de viandes et de farine d'os",
            Category.CLASS,
        ),
        Classification("1011006", "Préparation de boyaux naturels", Category.CLASS),
        Classification(
            "1011007", "Production de laine de délainage en suint, y compris laine lavée à dos", Category.CLASS
        ),
        Classification(
            "1011011", "Production de viandes surgelées ou congelées, en carcasses ou en morceaux", Category.CLASS
        ),
        Classification("10120", "Transformation et conservation de la viande de volaille", Category.CLASS),
        Classification("1012001", "Abattage de volailles", Category.CLASS),
        Classification("1012002", "Préparation de viande fraîche de volailles", Category.CLASS),
        Classification(
            "1012003", "Production de viandes fraîches de volailles en portions individuelles", Category.CLASS
        ),
        Classification("1012004", "Production de plumes et de duvets", Category.CLASS),
        Classification("10130", "Préparation de produits à base de viande ou de viande de volaille", Category.CLASS),
        Classification("10850", "Fabrication de plats préparés", Category.CLASS),
        Classification("10890", "Fabrication d'autres produits alimentaires n.c.a.", Category.CLASS),
        Classification("1013001", "Production de viandes séchées, salées ou fumées", Category.CLASS),
        Classification(
            "1013002",
            "Production de produits à base de viande (charcuterie) : saucisses, salami, boudins, andouillettes, cervelas, pâtés, galantines, rillettes, jambons cuits, etc.",
            Category.CLASS,
        ),
        Classification("1085001", "Production de plats préparés à base de viande", Category.CLASS),
        Classification("1013011", "Production de produits surgelés à base de viande", Category.CLASS),
        Classification("1085011", "Production de plats surgelés préparés à base de viande", Category.CLASS),
        Classification(
            "10200", "Transformation et conservation de poisson, de crustacés et de mollusques", Category.CLASS
        ),
        Classification(
            "1020001",
            "Conservation, congélation ou surgélation de poissons, de crustacés et mollusques : séchage, fumage, salage, saumurage, mise en conserve, etc.",
            Category.CLASS,
        ),
        Classification(
            "1020002",
            "Préparation de produits à base de poissons, de crustacés et de mollusques : poissons cuits, filets de poisson, laitances, caviar, succédanés du caviar, etc.",
            Category.CLASS,
        ),
        Classification("1085021", "Production de plats frais préparés à base de poisson", Category.CLASS),
        Classification(
            "1020011", "Congélation et surgélation de poissons, de crustacés et de mollusques", Category.CLASS
        ),
        Classification("1085031", "Production de plats surgelés préparés à base de poisson", Category.CLASS),
        Classification(
            "10311",
            "Transformation et conservation de pommes de terre, sauf fabrication de préparations surgelées à base de pommes de terre",
            Category.CLASS,
        ),
        Classification(
            "1031101", "Production de conserves de pommes de terre, à l'exclusion des produits surgelés", Category.CLASS
        ),
        Classification("1031102", "Production de purées de pommes de terre déshydratées", Category.CLASS),
        Classification("1031103", "Production de pommes chips et de produits similaires", Category.CLASS),
        Classification("1031104", "Epluchage industriel des pommes de terre", Category.CLASS),
        Classification("10312", "Fabrication de préparations surgelées à base de pommes de terre", Category.CLASS),
        Classification("1031201", "Fabrication de produits surgelés à base de pommes de terre", Category.CLASS),
        Classification("10320", "Préparation de jus de fruits et de légumes", Category.CLASS),
        Classification("1032001", "Fabrication de sirops de fruits", Category.CLASS),
        Classification(
            "10391", "Transformation et conservation de légumes, sauf fabrication de légumes surgelés", Category.CLASS
        ),
        Classification(
            "1039102",
            "Conservation des légumes : séchage, immersion dans l'huile ou le vinaigre, mise en conserve, etc.",
            Category.CLASS,
        ),
        Classification("1039101", "Production de produits alimentaires à base de légumes", Category.CLASS),
        Classification("10393", "Fabrication de légumes et de fruits surgelés", Category.CLASS),
        Classification(
            "1039203",
            "Conservation de fruits : congélation, séchage, immersion, mise en conserve, etc.",
            Category.CLASS,
        ),
        Classification("1039201", "Production de produits alimentaires à base de fruits", Category.CLASS),
        Classification("1039202", "Fabrication de confitures, marmelades et gelées", Category.CLASS),
        Classification("1041001", "Raffinage d'huiles végétales : huiles d'olive, de soja, etc.", Category.CLASS),
        Classification("10420", "Fabrication de margarine et de graisses comestibles similaires", Category.CLASS),
        Classification("10510", "Exploitation de laiteries et fabrication de fromage", Category.CLASS),
        Classification(
            "1051001",
            "Production de laits liquides frais, pasteurisés, stérilisés, homogénéisés et/ou ayant subi un chauffage ultracourt (U.H.T.)",
            Category.CLASS,
        ),
        Classification(
            "1051002",
            "Production de crèmes de laits liquides frais, pasteurisées, stérilisées, homogénéisées",
            Category.CLASS,
        ),
        Classification("1051003", "Production de laits concentrés, édulcorés ou non", Category.CLASS),
        Classification("1051004", "Production de beurre", Category.CLASS),
        Classification("1051005", "Production de fromages et de caillebotte", Category.CLASS),
        Classification("1051006", "Production de lactosérum", Category.CLASS),
        Classification("1051007", "Production de caséine et de lactose", Category.CLASS),
        Classification("1051008", "Production de yoghourt", Category.CLASS),
        Classification("1051009", "Production de desserts lactés frais", Category.CLASS),
        Classification("10520", "Fabrication de glaces de consommation", Category.CLASS),
        Classification(
            "1052001",
            "Production de crèmes glacées et d'autres glaces de consommation (ex. sorbet), y compris les crèmes glacées mises en vente par le producteur sur la voie publique",
            Category.CLASS,
        ),
        Classification("10610", "Travail des grains", Category.CLASS),
        Classification(
            "1061001",
            "Mouture des grains: production de farines, de gruaux, de semoules ou d'agglomérés sous forme de pellets, de blé, de seigle, d'avoine, de maïs ou d’autres grains de céréales",
            Category.CLASS,
        ),
        Classification("1061002", "Fabrication d'aliments pour le petit déjeuner à base de céréales", Category.CLASS),
        Classification(
            "1061003",
            "Fabrication de farines mélangées préparées pour la fabrication de pains, de gâteaux, de biscuits, de crêpes, etc.",
            Category.CLASS,
        ),
        Classification("10620", "Fabrication de produits amylacés", Category.CLASS),
        Classification("1089011", "Fabrication de miel artificiel et de caramel", Category.CLASS),
        Classification("10910", "Fabrication d'aliments pour animaux de ferme", Category.CLASS),
        Classification(
            "1091001",
            "Fabrication de produits composés pour l'alimentation des animaux de ferme, y compris les aliments de complément",
            Category.CLASS,
        ),
        Classification("10920", "Fabrication d'aliments pour animaux de compagnie", Category.CLASS),
        Classification("10711", "Fabrication industrielle de pain et de pâtisserie fraîche", Category.CLASS),
        Classification(
            "1071101",
            "Fabrication industrielle de produits de boulangerie principalement destinés à être livrés au commerce de détail, horeca, etc.: pains, gâteaux, tartes et autres produits frais ou surgelés",
            Category.CLASS,
        ),
        Classification("1071102", "Fabrication de pâtes destinées à la cuisson", Category.CLASS),
        Classification("10712", "Fabrication artisanale de pain et de pâtisserie fraîche", Category.CLASS),
        Classification(
            "1071201",
            "Fabrication artisanale de pains, de petits pains, de gâteaux frais, de tartes et d'autres produits frais de pâtisserie",
            Category.CLASS,
        ),
        Classification(
            "10720", "Fabrication de biscuits, de biscottes et de pâtisseries de conservation", Category.CLASS
        ),
        Classification("1072001", "Fabrication de biscottes, de biscuits, de pains d'épices, etc.", Category.CLASS),
        Classification(
            "1072002",
            "Fabrication de pâtisserie et de gâteaux de conservation (à l'exclusion des produits surgelés)",
            Category.CLASS,
        ),
        Classification("1072003", 'Fabrication de produits "apéritifs" sucrés ou salés', Category.CLASS),
        Classification("10810", "Fabrication de sucre", Category.CLASS),
        Classification(
            "1081001",
            "Production de sucre et de sirop de sucre obtenus à partir de jus de canne, de betterave, d'érable, de palme, etc.",
            Category.CLASS,
        ),
        Classification("1081002", "Production de saccharose", Category.CLASS),
        Classification("10820", "Fabrication de cacao, de chocolat et de produits de confiserie", Category.CLASS),
        Classification(
            "1082001",
            "Fabrication de cacao, de beurre de cacao, de graisse de cacao et d'huile de cacao",
            Category.CLASS,
        ),
        Classification("1082002", "Fabrication du chocolat et de confiseries au chocolat", Category.CLASS),
        Classification("1082003", "Fabrication de confiseries", Category.CLASS),
        Classification("1082004", "Fabrication de fruits confits", Category.CLASS),
        Classification("10730", "Fabrication de pâtes alimentaires", Category.CLASS),
        Classification(
            "1073001",
            "Fabrication de pâtes alimentaires farcies ou non, fraîches ou cuites telles les macaronis, les spaghettis, les nouilles, les lasagnes, etc.",
            Category.CLASS,
        ),
        Classification("10830", "Transformation du thé et du café", Category.CLASS),
        Classification(
            "1083001",
            "Torréfaction et décaféination du café : fabrication de café moulu, de café soluble, d'extraits et de concentrés de café",
            Category.CLASS,
        ),
        Classification("1083002", "Fabrication de succédanés du café", Category.CLASS),
        Classification("1083003", "Mélange du thé et du maté", Category.CLASS),
        Classification("82920", "Activités de conditionnement", Category.CLASS),
        Classification(
            "1083004", "Fabrication de tisanes de plantes (menthe, verveine, camomille, etc.)", Category.CLASS
        ),
        Classification(
            "1084001", "Fabrication de condiments et d'épices (y compris la mouture, le mélange, etc.)", Category.CLASS
        ),
        Classification("1084002", "Fabrication du vinaigre", Category.CLASS),
        Classification("1084003", "Fabrication de sauces", Category.CLASS),
        Classification("10860", "Fabrication d'aliments homogénéisés et diététiques", Category.CLASS),
        Classification(
            "1086001",
            "Fabrication de denrées alimentaires destinées à une alimentation particulière : préparations pour nourrissons, laits de suite et autres aliments du deuxième âge, aliments pour bébés, etc.",
            Category.CLASS,
        ),
        Classification("1089001", "Fabrication de soupes, de potages ou de bouillons préparés", Category.CLASS),
        Classification("1089002", "Fabrication de desserts lactés de conservation", Category.CLASS),
        Classification("11010", "Production de boissons alcooliques distillées", Category.CLASS),
        Classification(
            "1101001",
            "Fabrication de boissons alcooliques distillées telles que le whisky, le cognac, le gin, etc.",
            Category.CLASS,
        ),
        Classification("1101002", "Fabrication de liqueurs et d'apéritifs à base d'alcool", Category.CLASS),
        Classification("20140", "Fabrication d'autres produits chimiques organiques de base", Category.CLASS),
        Classification(
            "1102001",
            "Production de vins à partir de raisins frais tels que les vins de table, les vins de pays, les vins de qualité, les vins mousseux, le champagne, etc.",
            Category.CLASS,
        ),
        Classification("11030", "Fabrication de cidre et de vins d'autres fruits", Category.CLASS),
        Classification("1103001", "Fabrication de cidre, de poiré et de vins d'autres fruits", Category.CLASS),
        Classification("11040", "Production d'autres boissons fermentées non distillées", Category.CLASS),
        Classification("1104001", "Fabrication de vins aromatisés (vermouths)", Category.CLASS),
        Classification("11050", "Fabrication de bière", Category.CLASS),
        Classification("11060", "Fabrication de malt", Category.CLASS),
        Classification(
            "11070",
            "Industrie des eaux minérales et autres eaux embouteillées et des boissons rafraîchissantes",
            Category.CLASS,
        ),
        Classification("1107001", "Production d'eaux minérales naturelles", Category.CLASS),
        Classification(
            "1107002",
            "Fabrication de boissons sans alcool excepté bière et vin sans alcool : eaux minérales naturelles, boissons non alcoolisées édulcorées et/ou aromatisées comme citronnade, cola, tonics, etc.",
            Category.CLASS,
        ),
        Classification("1107003", "Production de thé glacé", Category.CLASS),
        Classification("12000", "Fabrication de produits à base de tabac", Category.CLASS),
        Classification(
            "1200001",
            "Fabrication de produits à base de tabac tels que les cigarettes, les cigares, le tabac à cigarettes, à pipe, à mâcher ou à priser",
            Category.CLASS,
        ),
        Classification("1200002", 'Fabrication de tabacs "homogénéisés" ou "reconstitués"', Category.CLASS),
        Classification("13100", "Préparation de fibres textiles et filature", Category.CLASS),
        Classification("1310001", "Préparation, cardage et peignage de fibres de type cotonnier", Category.CLASS),
        Classification(
            "1310002",
            "Filature de fils de type cotonnier en fibres de coton, en fibres artificielles ou en fibres synthétiques, pour le tissage, la bonneterie, etc.",
            Category.CLASS,
        ),
        Classification(
            "1310011",
            "Filature de fils de type linier en fibres de lin, en fibres artificielles ou en fibres synthétiques, pour le tissage, la bonneterie, etc.",
            Category.CLASS,
        ),
        Classification(
            "1310021",
            "Texturation, retordage, moulinage, câblage et foulardage de fils de filaments artificiels ou synthétiques",
            Category.CLASS,
        ),
        Classification("1310031", "Fabrication de fils à broder", Category.CLASS),
        Classification(
            "1310041",
            "Préparation et filature d'autres fibres textiles telles que les fibres de jute ou les fibres libériennes",
            Category.CLASS,
        ),
        Classification("1310042", "Fabrication de fils de papier", Category.CLASS),
        Classification("13200", "Tissage", Category.CLASS),
        Classification(
            "1320001",
            "Fabrication de tissus de type cotonnier en fils de coton ou en fibres synthétiques ou artificielles",
            Category.CLASS,
        ),
        Classification(
            "1320002",
            "Fabrication de velours, de tissus de chenile, de tissus bouclés (tissus-éponges), de tissus à points de gaze (y compris les tissus pour pansements), etc.",
            Category.CLASS,
        ),
        Classification(
            "1320011",
            "Fabrication de tissus de type lainier, cycle peigné, en laine filée ou en fibres synthétiques ou artificielles",
            Category.CLASS,
        ),
        Classification("1320021", "Fabrication de tissus en polypropène", Category.CLASS),
        Classification("13300", "Ennoblissement textile", Category.CLASS),
        Classification("18120", "Autre imprimerie (labeur)", Category.CLASS),
        Classification(
            "1330001",
            "Blanchiment, teinture, apprêtage et impression (sérigraphique) de fibres textiles, de fils, de tissus et d’articles en textile, y compris les vêtements",
            Category.CLASS,
        ),
        Classification(
            "1330002",
            "Séchage, vaporisage, décatissage, stoppage, sanforisage, mercerisage, etc. de textiles fabriqués par des tiers",
            Category.CLASS,
        ),
        Classification(
            "13921", "Fabrication de linge de lit et de table et d'articles textiles à usage domestique", Category.CLASS
        ),
        Classification("1392101", "Fabrication de linge de table, de lit, de toilette ou de cuisine", Category.CLASS),
        Classification(
            "1392102",
            "Fabrication d'édredons, couvertures, couvre-lits, coussins, poufs, oreillers, sacs de couchage, etc.",
            Category.CLASS,
        ),
        Classification(
            "1392103", "Fabrication de chiffons à épousseter, lavettes et articles similaires", Category.CLASS
        ),
        Classification(
            "13929", "Fabrication d'autres articles textiles confectionnés, sauf habillement", Category.CLASS
        ),
        Classification(
            "32500", "Fabrication d'instruments et de fournitures à usage médical et dentaire", Category.CLASS
        ),
        Classification("33190", "Réparation d'autres équipements", Category.CLASS),
        Classification("95290", "Réparation d'autres biens personnels et domestiques", Category.CLASS),
        Classification(
            "1392901",
            "Fabrication d'articles confectionnés pour l'ammeublement : rideaux, tours de lit, stores, housses pour meubles, etc.",
            Category.CLASS,
        ),
        Classification(
            "1392902",
            "Fabrication d’articles confectionnés pour l’ameublement : bâches, tentes, voiles pour embarcations, stores d’extérieur, housses amovibles pour voitures, machines ou mobilier, etc.",
            Category.CLASS,
        ),
        Classification("1392903", "Fabrication de drapeaux, de banderoles, de bannières, etc.", Category.CLASS),
        Classification("13930", "Fabrication de tapis et de moquettes", Category.CLASS),
        Classification(
            "1393001",
            "Fabrication de revêtements de sols en matières textiles, y compris les feutres aiguilletés : tapis, carpettes, paillassons et carreaux",
            Category.CLASS,
        ),
        Classification("13940", "Fabrication de ficelles, de cordes et de filets", Category.CLASS),
        Classification("13950", "Fabrication de non-tissés, sauf habillement", Category.CLASS),
        Classification("13960", "Fabrication d'autres textiles techniques et industriels", Category.CLASS),
        Classification("13990", "Fabrication d'autres textiles n.c.a.", Category.CLASS),
        Classification("17220", "Fabrication d'articles en papier à usage sanitaire ou domestique", Category.CLASS),
        Classification(
            "1396001",
            "Fabrication d'articles de rubanerie, y compris les rubans sans trame, en fils ou fibres parallélisés et encollés",
            Category.CLASS,
        ),
        Classification("1399001", "Fabrication de feutres", Category.CLASS),
        Classification("1396002", "Fabrication d'étiquettes, d'écussons, etc.", Category.CLASS),
        Classification(
            "1396003", "Fabrication d'articles ornementaux : tresses, glands, floches, pompons, etc.", Category.CLASS
        ),
        Classification(
            "1399002",
            "Fabrication de tulles, tulles-bobinots et autres tissus à mailles nouées, de dentelles en pièces, en bandes ou en motifs, et de broderies",
            Category.CLASS,
        ),
        Classification(
            "1396004",
            "Fabrication de tissus imprégnés, enduits ou recouverts de matière plastique ou stratifiés avec de la matière plastique",
            Category.CLASS,
        ),
        Classification("13910", "Fabrication d'étoffes à mailles", Category.CLASS),
        Classification("14310", "Fabrication d'articles chaussants à mailles", Category.CLASS),
        Classification("14199", "Fabrication d'autres vêtements et accessoires n.c.a.", Category.CLASS),
        Classification("14390", "Fabrication d'autres articles à mailles", Category.CLASS),
        Classification("14110", "Fabrication de vêtements en cuir", Category.CLASS),
        Classification("32990", "Autres activités manufacturières n.c.a.", Category.CLASS),
        Classification("14120", "Fabrication de vêtements de travail", Category.CLASS),
        Classification(
            "3299011",
            "Fabrication de vêtements de sécurité contre le feu, le rayonnement, la contamination, etc.",
            Category.CLASS,
        ),
        Classification("14130", "Fabrication d'autres vêtements de dessus", Category.CLASS),
        Classification(
            "1413001",
            "Fabrication de vêtements de dessus pour hommes, femmes et enfants à partir de matériel produit ou non par le fabricant tels tissus, étoffes à mailles, non-tissés etc.: manteaux, costumes, etc.",
            Category.CLASS,
        ),
        Classification("1413011", "Confection sur mesure", Category.CLASS),
        Classification("14140", "Fabrication de vêtements de dessous", Category.CLASS),
        Classification(
            "1414001",
            "Fabrication de vêtements de dessous pour hommes, femmes et enfants à partir de matériel produit ou non par le fabricant tels tissus, étoffes à mailles, dentelles, etc: chemises, slips, pyjamas, etc.",
            Category.CLASS,
        ),
        Classification("14191", "Fabrication de chapeaux et de bonnets", Category.CLASS),
        Classification("1419101", "Fabrication de chapeaux et de bonnets", Category.CLASS),
        Classification("1419102", "Fabrication de chapeaux en fourrure", Category.CLASS),
        Classification(
            "1419901",
            "Fabrication d'autres accessoires du vêtement : gants (y compris les gants en cuir), ceintures, châles, cravates, filets à cheveux, etc.",
            Category.CLASS,
        ),
        Classification(
            "1419902", "Fabrication de chaussures en matières textiles sans semelle rapportée", Category.CLASS
        ),
        Classification("14200", "Fabrication d'articles en fourrure", Category.CLASS),
        Classification("15110", "Apprêt et tannage des cuirs; préparation et teinture des fourrures", Category.CLASS),
        Classification(
            "1511011",
            "Préparation et teinture des pelleteries et des peaux non épilées : drayage, corroyage, tannage, blanchiment, tondage, épluchage et teinture",
            Category.CLASS,
        ),
        Classification("1420001", "Fabrication de vêtements et accessoires du vêtement en pelleteries", Category.CLASS),
        Classification(
            "1420002",
            "Fabrication d'articles divers en fourrures : tapis, poufs non garnis, peaux à polir pour l'industrie, etc.",
            Category.CLASS,
        ),
        Classification(
            "1511001", "Fabrication de cuirs et peaux chamoisés, parcheminés, vernis ou métallisés", Category.CLASS
        ),
        Classification("1511002", "Fabrication de cuirs reconstitués", Category.CLASS),
        Classification("1511003", "Finition du cuir", Category.CLASS),
        Classification("15120", "Fabrication d'articles de voyage, de maroquinerie et de sellerie", Category.CLASS),
        Classification(
            "1512001",
            "Fabrication d'art. de voyage, de maroqu. et art. simil. en cuir naturel, recstitué ou tt autre matériau : les mat. plastiques, tex., carton, etc. pr autant que la technol. soit la même que pr le cuir",
            Category.CLASS,
        ),
        Classification("1512002", "Fabrication d'articles de sellerie et de bourrellerie", Category.CLASS),
        Classification(
            "1512003",
            "Fabrication d'articles divers en cuir naturel ou reconstitué : courroies, joints, garnitures, etc.",
            Category.CLASS,
        ),
        Classification("15200", "Fabrication de chaussures", Category.CLASS),
        Classification("16291", "Fabrication d'objets divers en bois", Category.CLASS),
        Classification("22190", "Fabrication d'autres articles en caoutchouc", Category.CLASS),
        Classification("22290", "Fabrication d'autres articles en matières plastiques", Category.CLASS),
        Classification(
            "1520001",
            "Fabrication de chaussures pour tous usages, par tous procédés (y compris le moulage) et en toutes matières, à  l'exclusion des chaussures en caoutchouc",
            Category.CLASS,
        ),
        Classification(
            "1520002",
            "Fabrication de parties de chaussures : dessus et parties de dessus, semelles extérieures et intérieures, talons, etc. à l'exclusion des parties en caoutchouc",
            Category.CLASS,
        ),
        Classification("1610001", "Sciage, rabotage et façonnage du bois", Category.CLASS),
        Classification(
            "1610002", "Fabrication de traverses en bois pour voies ferrées et de poteaux de ligne", Category.CLASS
        ),
        Classification("1610003", "Fabrication de lames non assemblées pour parquets", Category.CLASS),
        Classification(
            "1610004",
            "Séchage du bois et imprégnation ou traitement chimique du bois au moyen d'agents de conservation ou d'autres produits, en combinaison avec le sciage et le façonnage",
            Category.CLASS,
        ),
        Classification(
            "1610005",
            "Fabrication de laine de bois, de farine de bois, de bois en copeaux ou en particules",
            Category.CLASS,
        ),
        Classification(
            "1610011",
            "Imprégnation ou traitement chimique du bois au moyen d'agents de conservation ou d'autres produits pour compte de tiers",
            Category.CLASS,
        ),
        Classification("16210", "Fabrication de placage et de panneaux de bois", Category.CLASS),
        Classification("1621001", "Fabrication de placage", Category.CLASS),
        Classification(
            "1621002",
            "Fabrication de contre-plaqués (duplex, triplex et multiplex), de panneaux pour meubles, de panneaux de fibres, de panneaux de particules et de panneaux similaires",
            Category.CLASS,
        ),
        Classification("16230", "Fabrication de charpentes et d'autres menuiseries", Category.CLASS),
        Classification("16220", "Fabrication de parquets assemblés", Category.CLASS),
        Classification("43320", "Travaux de menuiserie", Category.CLASS),
        Classification("16240", "Fabrication d'emballages en bois", Category.CLASS),
        Classification(
            "1624001",
            "Fabrication de caisses, de caissettes, de cageots, de cylindres et d'emballages similaires en bois",
            Category.CLASS,
        ),
        Classification(
            "1624002",
            "Fabrication de palettes simples, de caisses-palettes et d'autres plateaux de chargement en bois",
            Category.CLASS,
        ),
        Classification(
            "1624003",
            "Fabrication de tonneaux, de cuves, de baquets et d'autres ouvrages de tonnellerie en bois",
            Category.CLASS,
        ),
        Classification(
            "1629101",
            "Fabrication d'articles de ménage et ustensiles de cuisine en bois : planches à repasser, porte-manteaux, etc.",
            Category.CLASS,
        ),
        Classification(
            "1629102",
            "Fabrication de statuettes et objets d'ornement en bois, en bois marquetés ou en bois incrustés",
            Category.CLASS,
        ),
        Classification(
            "1629103",
            "Fabrication de coffrets, écrins et étuis pour bijouterie ou orfèvrerie et ouvrages similaires en bois",
            Category.CLASS,
        ),
        Classification(
            "1629104",
            "Fabrication de bâtons ronds pour stores, manches et montures en bois pour outils, brosses et balais",
            Category.CLASS,
        ),
        Classification(
            "1629105",
            "Fabrication de cannettes, busettes, bobines pour filatures et tissage, bobines pour fil à coudre et articles similaires en bois tourné",
            Category.CLASS,
        ),
        Classification(
            "1629106",
            "Fabrication de formes, embauchoirs et tendeurs pour chaussures, cintres pour vêtements",
            Category.CLASS,
        ),
        Classification("3299021", "Fabrication de cercueils", Category.CLASS),
        Classification("1629107", "Fabrication d'échelles en bois", Category.CLASS),
        Classification("1629108", "Fabrication de cadres en bois pour tableaux", Category.CLASS),
        Classification("16292", "Fabrication d'objets en liège, vannerie et sparterie", Category.CLASS),
        Classification("1629201", "Travail du liège naturel", Category.CLASS),
        Classification(
            "1629202",
            "Fabrication de tresses et d'articles de sparterie : nattes, paillassons, claies, etc.",
            Category.CLASS,
        ),
        Classification("17110", "Fabrication de pâte à papier", Category.CLASS),
        Classification("17120", "Fabrication de papier et de carton", Category.CLASS),
        Classification("1712001", "Couchage, enduction et imprégnation des papiers", Category.CLASS),
        Classification("2399011", "Fabrication de papiers asphaltés", Category.CLASS),
        Classification(
            "1712002", "Fabrication de papier journal et de papier pour l'impression ou l'écriture", Category.CLASS
        ),
        Classification("1712003", "Fabrication de papiers de fantaisie et d'autres papiers spéciaux", Category.CLASS),
        Classification("1712011", "Couchage, enduction et imprégnation des cartons", Category.CLASS),
        Classification(
            "17210", "Fabrication de papier et de carton ondulés et d'emballages en papier ou en carton", Category.CLASS
        ),
        Classification("1721001", "Fabrication de papiers et de cartons ondulés", Category.CLASS),
        Classification("1721002", "Fabrication d'emballages en papiers ou en cartons ondulés", Category.CLASS),
        Classification("1721003", "Fabrication de cartonnages pliants", Category.CLASS),
        Classification("1721004", "Fabrication d'autres emballages en papier ou en carton", Category.CLASS),
        Classification("17230", "Fabrication d'articles de papeterie", Category.CLASS),
        Classification("1723001", "Fabrication d'enveloppes et de cartes-lettres", Category.CLASS),
        Classification("17240", "Fabrication de papiers peints", Category.CLASS),
        Classification("17290", "Fabrication d'autres articles en papier ou en carton", Category.CLASS),
        Classification("1729001", "Fabrication d'étiquettes", Category.CLASS),
        Classification("58110", "Édition de livres", Category.CLASS),
        Classification("58120", "Édition de répertoires et de fichiers d'adresses", Category.CLASS),
        Classification("5811001", "Edition de livres, de livres scolaires, de brochures, etc.", Category.CLASS),
        Classification("5811002", "Edition de dictionnaires et d'encyclopédies", Category.CLASS),
        Classification("5811003", "Edition d'atlas, de cartes et de plans", Category.CLASS),
        Classification("5920311", "Edition de livres de musique et de partitions musicales", Category.CLASS),
        Classification("58130", "Édition de journaux", Category.CLASS),
        Classification(
            "5813001",
            "Edition de journaux et de journaux régionaux (y compris les journaux publicitaires).",
            Category.CLASS,
        ),
        Classification("58140", "Édition de revues et de périodiques", Category.CLASS),
        Classification("5814001", "Edition de revues, périodiques et magazines", Category.CLASS),
        Classification("59203", "Edition musicale", Category.CLASS),
        Classification(
            "5920301",
            "Edition de disques, de disques compacts et de bandes  contenant de la musique ou d'autres enregistrements sonores",
            Category.CLASS,
        ),
        Classification("5920302", "Edition de produits combinant livres et moyens audiovisuels", Category.CLASS),
        Classification("58190", "Autres activités d'édition", Category.CLASS),
        Classification(
            "5819001",
            "Edition de : photos, gravures et cartes postales illustrées ; calendriers, horaires et tableaux de service ; affiches et reproduction d'oeuvres d'art",
            Category.CLASS,
        ),
        Classification("18110", "Imprimerie de journaux", Category.CLASS),
        Classification("1811001", "Impression de journaux, y compris les journaux publicitaires", Category.CLASS),
        Classification(
            "1812001",
            "Impression de magazines, autres périodiques, livres , etc. sur des presses typograph., offset, héliogravure, flexograph., sérigraph. etc, imprimantes électron., app. de reproduction, app.de gaufrage",
            Category.CLASS,
        ),
        Classification("18140", "Reliure et activités annexes", Category.CLASS),
        Classification(
            "1814001",
            "Pliage, assemblage, agrafage, reliure, collage, massicotage, dorage de feuillets imprimés à insérer dans des livres, brochures, périodiques, catalogues, etc.",
            Category.CLASS,
        ),
        Classification(
            "1814002",
            "Pliage, timbrage, perçage, perforage, gaufrage, collage, pelliculage de papiers et cartons imprimés pour e.a. formulaires commerciaux, présentoirs, cartes à échantillons, étiquettes, calendriers, etc.",
            Category.CLASS,
        ),
        Classification("18130", "Activités de prépresse", Category.CLASS),
        Classification(
            "1813001",
            "Composition, par exemple de textes et d'images, sur film, sur papier photographique ou papier normal",
            Category.CLASS,
        ),
        Classification(
            "1813002",
            "Reproduction : production de formes typographiques, reproduction offset et plaques d'impression, reproduction et cylindres d'héliogravure",
            Category.CLASS,
        ),
        Classification(
            "1813011",
            "Préparation et la production de transparents pour rétroprojecteurs, ébauches, maquettes, etc.",
            Category.CLASS,
        ),
        Classification(
            "1813012",
            "Préparation de données digitales : l'enrichissement, la sélection, la liaison de données digitales stockées dans des appareils de traitement électronique de données",
            Category.CLASS,
        ),
        Classification("1813013", "Autres activités graphiques", Category.CLASS),
        Classification("18200", "Reproduction d'enregistrements", Category.CLASS),
        Classification(
            "1820001",
            "Reproduction, à partir d'une matrice, de disques, de disques compacts, de bandes et de cassettes contenant de la musique ou d'autres enregistrements sonores",
            Category.CLASS,
        ),
        Classification(
            "1820011",
            "Reproduction, à partir d'une matrice, de disques, de disques compacts, de bandes et de cassettes contenant des films ou d'autres enregistrements vidéo",
            Category.CLASS,
        ),
        Classification(
            "1820021",
            "Reproduction, à partir d'une matrice, de logiciels et de données informatiques sur disques, disquettes, disques compacts, bandes ou cassettes",
            Category.CLASS,
        ),
        Classification("19100", "Cokéfaction", Category.CLASS),
        Classification("1920001", "Production de carburants pour moteurs : essence, kérosène, etc.", Category.CLASS),
        Classification("38222", "Traitement et élimination des déchets dangereux", Category.CLASS),
        Classification("20130", "Fabrication d'autres produits chimiques inorganiques de base", Category.CLASS),
        Classification("21209", "Fabrication d'autres produits pharmaceutiques", Category.CLASS),
        Classification("24460", "Élaboration et transformation de matières nucléaires", Category.CLASS),
        Classification("3822201", "Traitement des déchets de l'industrie nucléaire", Category.CLASS),
        Classification("20110", "Fabrication de gaz industriels", Category.CLASS),
        Classification("2011001", "Fabrication de gaz élémentaires", Category.CLASS),
        Classification("2011002", "Fabrication de gaz industriels mélangés", Category.CLASS),
        Classification("20120", "Fabrication de colorants et de pigments", Category.CLASS),
        Classification(
            "2012001",
            "Fabrication, sous forme fondamentale ou concentrée, de colorants et de pigments, quelle que soit l'origine",
            Category.CLASS,
        ),
        Classification(
            "2013001",
            "Fabrication d'éléments chimiques, à l'exclusion des métaux, des gaz élémentaires d'origine industrielle et des éléments radioactifs issus de l'industrie des combustibles nucléaires",
            Category.CLASS,
        ),
        Classification(
            "2013002",
            "Fabrication d'alcalis, de lessives et d'autres bases inorganiques, à l'exclusion de l'ammoniac",
            Category.CLASS,
        ),
        Classification("2013003", "Fabrication de sels métalliques inorganiques", Category.CLASS),
        Classification("2013004", "Grillage de la pyrite de fer", Category.CLASS),
        Classification(
            "2014001", "Fabrication de hydrocarbures cycliques et acycliques, saturés ou non saturés", Category.CLASS
        ),
        Classification("2014002", "Distillation des goudrons de houille", Category.CLASS),
        Classification("20150", "Fabrication de produits azotés et d'engrais", Category.CLASS),
        Classification(
            "2015001",
            "Fabrication d'engrais: engrais azotés, phosphatés ou potassiques, simples ou complexes; urée, phosphates naturels bruts et sels de potassium naturels bruts",
            Category.CLASS,
        ),
        Classification("20160", "Fabrication de matières plastiques de base", Category.CLASS),
        Classification(
            "2016001",
            "Fabrication des polymères, y compris les polymères acryliques et les polymères d'éthylène, de propylène, de styrène, de chlorure de vinyle, d'acétate de vinyle",
            Category.CLASS,
        ),
        Classification("20170", "Fabrication de caoutchouc synthétique", Category.CLASS),
        Classification(
            "2017001",
            "Fabrication de caoutchouc synthétique sous formes primaires - caoutchouc factice - caoutchouc synthétique",
            Category.CLASS,
        ),
        Classification("20200", "Fabrication de pesticides et d'autres produits agrochimiques", Category.CLASS),
        Classification("20300", "Fabrication de peintures, de vernis, d'encres et de mastics", Category.CLASS),
        Classification("2030001", "Fabrication de peintures et de vernis", Category.CLASS),
        Classification("2030002", "Fabrication de pigments, d'opacifiants et de couleurs préparés", Category.CLASS),
        Classification("2030003", "Fabrication de compositions vitrifiables, d'engobes, etc.", Category.CLASS),
        Classification("21100", "Fabrication de produits pharmaceutiques de base", Category.CLASS),
        Classification(
            "2110001",
            "Etude, mise au point de la production des principes actifs destinés à la fabrication de médicaments",
            Category.CLASS,
        ),
        Classification("2110002", "Fabrication des acides salicylique et o-acétylsalicylique", Category.CLASS),
        Classification("2110003", "Traitement du sang", Category.CLASS),
        Classification(
            "2110004", "Transformation de glandes et production d'extraits de glandes, etc.", Category.CLASS
        ),
        Classification("21201", "Fabrication de médicaments", Category.CLASS),
        Classification(
            "2120101", "Fabrication de médicaments divers, y compris les préparations homéopathiques", Category.CLASS
        ),
        Classification(
            "2120102",
            "Préparations chimiques contraceptives à usage externe et médicaments contraceptifs à base d'hormones",
            Category.CLASS,
        ),
        Classification("2120103", "Fabrication de préparations vétérinaires", Category.CLASS),
        Classification("2120104", "Fabrication de tisanes de plantes médicinales", Category.CLASS),
        Classification("20411", "Fabrication de savons et de détergents", Category.CLASS),
        Classification("20420", "Fabrication de parfums et de produits de toilette", Category.CLASS),
        Classification("2041101", "Fabrication de savons", Category.CLASS),
        Classification("20412", "Fabrication de produits d'entretien", Category.CLASS),
        Classification(
            "2041201", "Fabrication de préparations pour parfumer ou désodoriser les locaux", Category.CLASS
        ),
        Classification("2041202", "Fabrication de cires artificielles ou cires préparées", Category.CLASS),
        Classification("2042001", "Fabrication de parfums et eaux de toilette", Category.CLASS),
        Classification("2042002", "Fabrication de produits de beauté ou de maquillage", Category.CLASS),
        Classification("2042003", "Fabrication de préparations pour manucures et pédicures", Category.CLASS),
        Classification(
            "2042004",
            "Fabrication de shampoings, laques pour cheveux, préparations pour l'ondulation et le défrisage des cheveux",
            Category.CLASS,
        ),
        Classification("2042005", "Fabrication de dépilatoires", Category.CLASS),
        Classification("20510", "Fabrication de produits explosifs", Category.CLASS),
        Classification("2051001", "Fabrication de poudres propulsives", Category.CLASS),
        Classification(
            "2051002", "Fabrication d'amorces, de détonateurs et de fusées de signalisation", Category.CLASS
        ),
        Classification("20520", "Fabrication de colles", Category.CLASS),
        Classification("20590", "Fabrication d'autres produits chimiques n.c.a.", Category.CLASS),
        Classification("2059021", "Fabrication de gélatines et de leurs dérivés", Category.CLASS),
        Classification("2052001", "Fabrication de ciments-colles", Category.CLASS),
        Classification("20530", "Fabrication d'huiles essentielles", Category.CLASS),
        Classification("2053001", "Fabrication d'essences et de produits aromatiques naturels", Category.CLASS),
        Classification(
            "2059001",
            "Fabrication de plaques et films photographiques, de papiers sensibilisés et d'autres matières sensibilisées non impressionnées",
            Category.CLASS,
        ),
        Classification("26800", "Fabrication de supports magnétiques et optiques", Category.CLASS),
        Classification(
            "2680001", "Fabrication de supports vierges pour l'enregistrement du son ou de l'image", Category.CLASS
        ),
        Classification(
            "2680002",
            "Fabrication de disques et de bandes vierges pour l'enregistrement de données informatiques",
            Category.CLASS,
        ),
        Classification("26110", "Fabrication de composants électroniques", Category.CLASS),
        Classification(
            "2059011", "Fabrication d'huiles et graisses modifiées par des procédés chimiques", Category.CLASS
        ),
        Classification(
            "2059012",
            "Fabrication d'huiles synthétiques spéciales de graissage et additifs pour huiles lubrifiantes",
            Category.CLASS,
        ),
        Classification("2059013", "Fabrication de réactifs composés de diagnostic ou de laboratoire", Category.CLASS),
        Classification("20600", "Fabrication de fibres artificielles ou synthétiques", Category.CLASS),
        Classification("2060001", "Fabrication de câbles de filaments synthétiques ou artificiels", Category.CLASS),
        Classification("22110", "Fabrication et rechapage de pneumatiques", Category.CLASS),
        Classification("2219001", "Fabrication de courroies transporteuses ou de transmission", Category.CLASS),
        Classification(
            "2219002",
            "Fabrication d'articles d'habillement en caoutchouc, non assemblés par couture, mais simplement collés",
            Category.CLASS,
        ),
        Classification("2219003", "Fabrication de matériaux de réparation en caoutchouc", Category.CLASS),
        Classification(
            "22210", "Fabrication de plaques, feuilles, tubes et profilés en matières plastiques", Category.CLASS
        ),
        Classification("33200", "Installation de machines et d'équipements industriels", Category.CLASS),
        Classification(
            "2221001",
            "Fabrication de produits semi-finis en matières plastiques : plaques, feuilles, blocs, pellicules, bandes, lames, etc.",
            Category.CLASS,
        ),
        Classification(
            "2221002",
            "Fabrication de produits finis en matières plastiques: tubes, tuyaux et accessoires de tuyauterie en plastique",
            Category.CLASS,
        ),
        Classification("22220", "Fabrication d'emballages en matières plastiques", Category.CLASS),
        Classification("22230", "Fabrication d'éléments en matières plastiques pour la construction", Category.CLASS),
        Classification(
            "2223001",
            "Fabrication de portes et fenêtres avec cadres et chambranles, volets, stores, plinthes, moulures, etc.",
            Category.CLASS,
        ),
        Classification("2223002", "Fabrication de cuves, foudres et réservoirs", Category.CLASS),
        Classification(
            "2223003",
            "Fabrication de revêtements de sols, de murs et de plafonds isolants ou non, sous forme de rouleaux, de dalles, de carreaux, etc.",
            Category.CLASS,
        ),
        Classification(
            "2223004",
            "Fabrication d'articles en matières plastiques pour usages sanitaires ou hygiéniques: baignoires, douches, lavabos, bidets, cuvettes d'aisance, réservoirs de chasse, etc.",
            Category.CLASS,
        ),
        Classification("27330", "Fabrication de matériel d'installation électrique", Category.CLASS),
        Classification(
            "2229001",
            "Fabrication de produits divers en matières plastiques: coiffures, pièces isolantes, parties d'appareils d'éclairage, fournit. de bureau et scolaires, articles d'habillement (simplement collés), etc.",
            Category.CLASS,
        ),
        Classification(
            "2229002",
            "Fabrication d'articles en matières plastiques (y compris les matériaux composites) pour usages techniques, sur devis et pour compte de tiers",
            Category.CLASS,
        ),
        Classification(
            "2229003", "Fabrication pour compte de tiers de parties de jouets en matières plastiques", Category.CLASS
        ),
        Classification("23110", "Fabrication de verre plat", Category.CLASS),
        Classification(
            "2311001", "Fabrication de verre plat, y compris le verre plat armé, coloré ou teinté", Category.CLASS
        ),
        Classification("23120", "Façonnage et transformation du verre plat", Category.CLASS),
        Classification(
            "2312001", "Fabrication de verre plat trempé ou formé de feuilles contre-collées", Category.CLASS
        ),
        Classification("2312002", "Fabrication de miroirs en verre", Category.CLASS),
        Classification("2312003", "Fabrication de vitrages isolants à parois multiples", Category.CLASS),
        Classification("23130", "Fabrication de verre creux", Category.CLASS),
        Classification(
            "2313001",
            "Fabrication de bouteilles et de flacons, de pots, de bocaux et autres récipients en verre ou en cristal",
            Category.CLASS,
        ),
        Classification(
            "2313002",
            "Fabrication de verres à boire et d'autres articles en verre ou en cristal à usage domestique",
            Category.CLASS,
        ),
        Classification("2313003", "Fabrication d'articles décoratifs en verre ou en cristal", Category.CLASS),
        Classification("2313004", "Façonnage du verre creux : taille, gravure, etc.", Category.CLASS),
        Classification("23140", "Fabrication de fibres de verre", Category.CLASS),
        Classification(
            "2314001", "Fabrication de fibres de verre et de produits non tissés en cette matière", Category.CLASS
        ),
        Classification(
            "23190", "Fabrication et façonnage d'autres articles en verre, y compris verre technique", Category.CLASS
        ),
        Classification("2319001", "Fabrication de cônes et écrans pour téléviseurs", Category.CLASS),
        Classification(
            "2319002",
            "Fabrication de verres d'horlogerie, verres d'optique et d'éléments d'optique non travaillés optiquement",
            Category.CLASS,
        ),
        Classification("2319003", "Fabrication de verrerie utilisée en bijouterie de fantaisie", Category.CLASS),
        Classification("23410", "Fabrication d'articles céramiques à usage domestique ou ornemental", Category.CLASS),
        Classification(
            "2341001", "Fabrication de vaisselle et autres articles de ménage en porcelaine", Category.CLASS
        ),
        Classification(
            "2341002", "Fabrication de statuettes et autres objets d'ornementation en porcelaine", Category.CLASS
        ),
        Classification(
            "2341011",
            "Fabrication de vaisselle et autres articles de ménage en faïence, grès ou terre commune",
            Category.CLASS,
        ),
        Classification(
            "2341012",
            "Fabrication de statuettes et d'objets d'ornementation en céramique autre que la porcelaine",
            Category.CLASS,
        ),
        Classification("23420", "Fabrication d'appareils sanitaires en céramique", Category.CLASS),
        Classification("2342001", "Fabrication d'appareils sanitaires en céramique", Category.CLASS),
        Classification("23430", "Fabrication d'isolateurs et de pièces isolantes en céramique", Category.CLASS),
        Classification("23440", "Fabrication d'autres produits céramiques à usage technique", Category.CLASS),
        Classification(
            "2344001", "Fabrication de produits céramiques pour usages chimiques ou industriels", Category.CLASS
        ),
        Classification("23490", "Fabrication d'autres produits céramiques", Category.CLASS),
        Classification("2349001", "Fabrications de produits céramiques n.d.a.", Category.CLASS),
        Classification("23200", "Fabrication de produits réfractaires", Category.CLASS),
        Classification("2320001", "Fabrication de mortiers, de bétons, etc., réfractaires", Category.CLASS),
        Classification("23310", "Fabrication de carreaux en céramique", Category.CLASS),
        Classification(
            "2331001",
            "Fabrication de carreaux pour le revêtement des murs et des cheminées, d'abacules, en céramique non réfractaire",
            Category.CLASS,
        ),
        Classification(
            "23322",
            "Fabrication de tuiles, de carrelages et d'autres produits de construction en terre cuite",
            Category.CLASS,
        ),
        Classification("2332201", "Fabrication de tuiles en terre cuite", Category.CLASS),
        Classification("23321", "Fabrication de briques", Category.CLASS),
        Classification(
            "2332101",
            "Fabrication de briques et de briques perforées ou creuses en terre cuite non réfractaire",
            Category.CLASS,
        ),
        Classification("2332211", "Fabrication de hourdis creux en terre cuite", Category.CLASS),
        Classification(
            "2332212", "Fabrication de produits divers en terre cuite:  bacs à fleurs, pots, etc.", Category.CLASS
        ),
        Classification("23510", "Fabrication de ciment", Category.CLASS),
        Classification("23520", "Fabrication de chaux et de plâtre", Category.CLASS),
        Classification(
            "2352001", "Fabrication de chaux: chaux vive, chaux éteinte et chaux hydraulique", Category.CLASS
        ),
        Classification("2352011", "Fabrication de plâtre", Category.CLASS),
        Classification("23610", "Fabrication d'éléments en béton pour la construction", Category.CLASS),
        Classification(
            "2361001",
            "Fabrication d'ouvrages préfabriqués en béton, utilisés en construction: tuiles, carreaux, dalles, briques, hourdis creux, plaques, panneaux, tuyaux, piliers, etc.",
            Category.CLASS,
        ),
        Classification(
            "2361002", "Fabrication d'éléments préfabriqués en béton pour le bâtiment et le génie civil", Category.CLASS
        ),
        Classification("23620", "Fabrication d'éléments en plâtre pour la construction", Category.CLASS),
        Classification("23630", "Fabrication de béton prêt à l'emploi", Category.CLASS),
        Classification("2363001", "Fabrication de bétons et de mortiers prêts à l'emploi", Category.CLASS),
        Classification("23640", "Fabrication de mortiers et de bétons secs", Category.CLASS),
        Classification("23650", "Fabrication d'ouvrages en fibre-ciment", Category.CLASS),
        Classification(
            "2365001",
            "Fabrication de matériaux de construction en substances végétales (laine de bois, paille, roseaux, joncs) agglomérés avec un liant minéral (ciment, plâtre, etc.)",
            Category.CLASS,
        ),
        Classification(
            "2365002",
            "Fabrication d'ouvrages en amiante-ciment, cellulose-ciment ou similaires : plaques ondulées ou autres, panneaux, carreaux, tuiles, tuyaux, gaines, réservoirs, auges, bassins, éviers, cruchons, etc.",
            Category.CLASS,
        ),
        Classification("23690", "Fabrication d'autres ouvrages en béton, en ciment ou en plâtre", Category.CLASS),
        Classification(
            "2369001",
            "Fabrication d'autres ouvrages en béton, ciment, plâtre ou pierre artificielle, sans rapport direct avec la construction :statues, meubles, bas-reliefs, hauts-reliefs, vases, pots de fleurs, enz.",
            Category.CLASS,
        ),
        Classification("23700", "Taille, façonnage et finissage de pierres", Category.CLASS),
        Classification(
            "2370001",
            "Taille, façonnage et finissage de la pierre destinée à la construction de bâtiments ou de routes, à la couverture de toitures, etc.",
            Category.CLASS,
        ),
        Classification(
            "2370002", "Opérations réalisées sur des pierres brutes fournies par les carriers", Category.CLASS
        ),
        Classification(
            "2370003",
            "Production de pierres tombales et de monuments funéraires y compris éventuellement leur pose",
            Category.CLASS,
        ),
        Classification("23910", "Fabrication de produits abrasifs", Category.CLASS),
        Classification("23990", "Fabrication d'autres produits minéraux non métalliques n.c.a.", Category.CLASS),
        Classification(
            "2399001",
            "Fabrication de garnitures de friction et de pièces non montées pour ces garnitures, à base de substances minérales ou de cellulose",
            Category.CLASS,
        ),
        Classification("2399002", "Fabrication d'ouvrages en asphalte", Category.CLASS),
        Classification("2399003", "Fabrication de corindon artificiel", Category.CLASS),
        Classification("24100", "Sidérurgie", Category.CLASS),
        Classification("24510", "Fonderie de fonte", Category.CLASS),
        Classification("24520", "Fonderie d'acier", Category.CLASS),
        Classification("24410", "Production de métaux précieux", Category.CLASS),
        Classification(
            "24200",
            "Fabrication de tubes, de tuyaux, de profilés creux et d'accessoires correspondants en acier",
            Category.CLASS,
        ),
        Classification(
            "2420001",
            "Fabrication de tubes soudés par formage et soudage à froid ou à chaud, par formage et étirage à froid ou par formage et réduction à chaud",
            Category.CLASS,
        ),
        Classification(
            "2420002",
            "Fabrication d'accessoires de tuyauterie en acier : brides plates ou à collerette forgée en acier, accessoires à souder bout à bout en acier, accessoires filetés et autres accessoires en acier",
            Category.CLASS,
        ),
        Classification("24310", "Étirage à froid de barres", Category.CLASS),
        Classification("24320", "Laminage à froid de feuillards", Category.CLASS),
        Classification(
            "2432001",
            "Fabrication de produits laminés plats en acier, nus ou revêtus, enroulés ou non, d'une largeur n'excédant pas 600 mm, obtenus par relaminage à froid de produits plats laminés à chaud",
            Category.CLASS,
        ),
        Classification("24330", "Profilage à froid par formage ou pliage", Category.CLASS),
        Classification("24340", "Tréfilage à froid", Category.CLASS),
        Classification("2434001", "Fabrication de fils d'acier par tréfilage ou étirage à froid", Category.CLASS),
        Classification(
            "24100",
            "Productie van bijzonder zuiver ijzer door elektrolyse of andere chemische procédés",
            Category.CLASS,
        ),
        Classification("2441001", "Production d'alliages de métaux précieux", Category.CLASS),
        Classification("24420", "Métallurgie de l'aluminium", Category.CLASS),
        Classification("24430", "Métallurgie du plomb, du zinc ou de l'étain", Category.CLASS),
        Classification("24440", "Métallurgie du cuivre", Category.CLASS),
        Classification("24450", "Métallurgie des autres métaux non ferreux", Category.CLASS),
        Classification("2451001", "Fonderie de produits finis ou de demi-produits en fonte", Category.CLASS),
        Classification("2452001", "Fonderie de produits finis ou de demi-produits en acier", Category.CLASS),
        Classification("24530", "Fonderie de métaux légers", Category.CLASS),
        Classification("24540", "Fonderie d'autres métaux non ferreux", Category.CLASS),
        Classification("25110", "Fabrication de structures métalliques et de parties de structures", Category.CLASS),
        Classification("33110", "Réparation d'ouvrages en métaux", Category.CLASS),
        Classification(
            "2511001", "Fabrication de cadres métalliques ou d'ossatures pour la construction", Category.CLASS
        ),
        Classification(
            "2511002",
            "Fabrication d'ossatures métalliques pour équipements industriels (ossatures de hauts fourneaux, de matériels de manutention, etc.)",
            Category.CLASS,
        ),
        Classification(
            "2511003",
            "Fabrication de constructions préfabriquées principalement en métaux: baraques de chantier, éléments modulaires pour expositions, cabines téléphoniques, etc.",
            Category.CLASS,
        ),
        Classification("25120", "Fabrication de portes et de fenêtres en métal", Category.CLASS),
        Classification(
            "2512001",
            "Fabrication de menuiseries métalliques: portes et fenêtres avec chambranles, volets, cloisons mobiles,grilles, portes de garage, etc.",
            Category.CLASS,
        ),
        Classification("25290", "Fabrication d'autres réservoirs, citernes et conteneurs métalliques", Category.CLASS),
        Classification(
            "2529001",
            "Fabrication de silos, de réservoirs, de citernes et de récipients similaires en métaux, d'une capacité supérieure à 300 litres",
            Category.CLASS,
        ),
        Classification(
            "2529002", "Fabrication de récipients métalliques pour gaz comprimés ou liquéfiés", Category.CLASS
        ),
        Classification("25210", "Fabrication de radiateurs et de chaudières pour le chauffage central", Category.CLASS),
        Classification(
            "2521001", "Fabrication de radiateurs et de chaudières pour le chauffage central", Category.CLASS
        ),
        Classification(
            "25300",
            "Fabrication de générateurs de vapeur, à l'exception des chaudières pour le chauffage central",
            Category.CLASS,
        ),
        Classification(
            "2530001",
            "Fabrication de générateurs produisant de la vapeur d'eau ou d'autres types de vapeur",
            Category.CLASS,
        ),
        Classification(
            "2530002",
            "Fabrication d'appareils auxiliaires pour générateurs de vapeur:  condensateurs, économiseurs, surchauffeurs, collecteurs et accumulateurs de vapeur",
            Category.CLASS,
        ),
        Classification(
            "2530003",
            "Conception, construction et installation de réseaux de tuyauterie, comprenant un traitement complémentaire des tubes de manière à réaliser principalement des conduites ou des réseaux sous pression",
            Category.CLASS,
        ),
        Classification("25501", "Forge", Category.CLASS),
        Classification("2550101", "Production pour des tiers de pièces forgées en métaux", Category.CLASS),
        Classification(
            "2550102",
            "Production et montage de pièces forgées pour la construction: rampes d'escalier, balustrades, etc.",
            Category.CLASS,
        ),
        Classification(
            "25502", "Emboutissage, estampage et profilage des métaux; métallurgie des poudres", Category.CLASS
        ),
        Classification(
            "2550201", "Production pour des tiers de pièces matricées en métaux non ferreux", Category.CLASS
        ),
        Classification(
            "2550211",
            "Production d'objets métalliques, directement à partir de poudres de métaux par traitement thermique (frittage) ou compression",
            Category.CLASS,
        ),
        Classification("25610", "Traitement et revêtement des métaux", Category.CLASS),
        Classification("2561001", "Placage, traitement anodique, etc., des métaux", Category.CLASS),
        Classification("2561002", "Revêtement des métaux par électrolyse ou immersion", Category.CLASS),
        Classification("2561003", "Traitement thermique des métaux", Category.CLASS),
        Classification(
            "2561004", "Ebarbage, décapage au jet de sable, dessablage au tonneau, nettoyage des métaux", Category.CLASS
        ),
        Classification("2561005", "Coloration, gravure, impression des métaux", Category.CLASS),
        Classification(
            "2561006", "Revêtement non métallique des métaux: plastifiage, émaillage, laquage, etc.", Category.CLASS
        ),
        Classification("2561007", "Durcissement et bufflage des métaux", Category.CLASS),
        Classification("25620", "Usinage", Category.CLASS),
        Classification(
            "2562001",
            "Perçage, tournage, fraisage, arasage, rabotage, rodage, brochage, dressage, sciage, meulage, affûtage, etc., de pièces métalliques",
            Category.CLASS,
        ),
        Classification("3312011", "Travaux d'entretien et réparations mécaniques pour des tiers", Category.CLASS),
        Classification("0162011", "Activités des maréchaux-ferrants", Category.CLASS),
        Classification("25710", "Fabrication de coutellerie", Category.CLASS),
        Classification(
            "2571001", "Fabrication de coutellerie domestique: couteaux, fourchettes, cuillères, etc.", Category.CLASS
        ),
        Classification("25739", "Fabrication d'outillage, à l'exclusion des moules et des modèles", Category.CLASS),
        Classification("28410", "Fabrication de machines de formage des métaux", Category.CLASS),
        Classification("28490", "Fabrication d'autres machines-outils", Category.CLASS),
        Classification("28920", "Fabrication de machines pour l'extraction ou la construction", Category.CLASS),
        Classification(
            "2573901",
            "Fabrication d'outils à main tels que pinces, tournevis, clés, sécateurs, truelles, lampes à souder, etc.",
            Category.CLASS,
        ),
        Classification(
            "2573902",
            "Fabrication de couteaux et de lames tranchantes pour machines ou pour appareils mécaniques",
            Category.CLASS,
        ),
        Classification(
            "2573903",
            "Fabrication d'outils interchangeables pour outillage à main, mécaniques ou non, ou pour machines-outils: forets, poinçons, matrices, fraises, etc.",
            Category.CLASS,
        ),
        Classification("2573904", "Fabrication d'outils de forgeron: forges, enclumes, etc.", Category.CLASS),
        Classification("25720", "Fabrication de serrures et de ferrures", Category.CLASS),
        Classification(
            "2572001",
            "Fabrication de serrures, de cadenas, de verrous, de clés et d'articles similaires de serrurerie pour le bâtiment, l'ameublement, les véhicules, etc.",
            Category.CLASS,
        ),
        Classification("2572002", "Fabrication de charnières, de gonds, de paumelles,etc.", Category.CLASS),
        Classification("25910", "Fabrication de fûts et d'emballages métalliques similaires", Category.CLASS),
        Classification(
            "2591001", "Fabrication de récipients métalliques d'une capacité inférieure à 300 litres", Category.CLASS
        ),
        Classification(
            "2591002", "Fabrication de seaux, de cruches, de bidons, de tonneaux, ..., en métaux", Category.CLASS
        ),
        Classification("25920", "Fabrication d'emballages métalliques légers", Category.CLASS),
        Classification("2592001", "Fabrication de boîtes pour conserves alimentaires et pour boissons", Category.CLASS),
        Classification("2592002", "Fabrication d'articles métalliques de bouchage et de surbouchage", Category.CLASS),
        Classification(
            "25930", "Fabrication d'articles en fils métalliques, de chaînes et de ressorts", Category.CLASS
        ),
        Classification(
            "2593001",
            "Fabrication d'articles en fils métalliques : ronces artificielles, clôtures, grillages, treillis, toiles métalliques, etc.",
            Category.CLASS,
        ),
        Classification("2593002", "Fabrication de clous, pointes, etc.", Category.CLASS),
        Classification("25940", "Fabrication de vis et de boulons", Category.CLASS),
        Classification(
            "2593011",
            "la fabrication de ressorts: ressorts à lames, ressorts hélicoïdaux, barres de torsion",
            Category.CLASS,
        ),
        Classification("25991", "Fabrication d'articles métalliques à usage ménager et sanitaire", Category.CLASS),
        Classification(
            "2599101",
            "Fabrication de casseroles émaillées ou non, poêles à frire et autres ustensiles non électriques pour la table et la cuisine",
            Category.CLASS,
        ),
        Classification(
            "2599111",
            "Fabrication de baignoires, d'éviers, de bassines et d'articles similaires en métaux communs, émaillés ou non",
            Category.CLASS,
        ),
        Classification("25999", "Fabrication d'autres articles métalliques n.c.a.", Category.CLASS),
        Classification(
            "2599901",
            "Fabrication de coffres-forts, de compartiments pour chambres fortes, de portes blindées, etc.",
            Category.CLASS,
        ),
        Classification(
            "2599911", "Fabrication de panneaux indicateurs et de panneaux de signalisation", Category.CLASS
        ),
        Classification(
            "2599914", "Fabrication d'éléments de couverture en métal : gouttières, faîtages, etc.", Category.CLASS
        ),
        Classification("2599912", "Fabrication d'échelles et escabeaux métalliques", Category.CLASS),
        Classification("2599913", "Fabrication de boîtes aux lettres", Category.CLASS),
        Classification(
            "28110",
            "Fabrication de moteurs et de turbines, à l'exception des moteurs d'avions, de véhicules automobiles et de motocycles",
            Category.CLASS,
        ),
        Classification(
            "27110", "Fabrication de moteurs, de génératrices et de transformateurs électriques", Category.CLASS
        ),
        Classification("33120", "Réparation de machines", Category.CLASS),
        Classification(
            "2811001",
            "Fabrication de moteurs à piston à combustion interne et de leurs parties pour usages divers: pour véhicules ferroviaires, machines agricoles ou engins de génie civil, navires et bateaux",
            Category.CLASS,
        ),
        Classification(
            "2811002",
            "Fabrication de turbines et de leurs parties: turbines produisant de la vapeur d'eau ou d'autres types de vapeur, turbines à gaz, turbines hydrauliques, roues hydrauliques et leurs régulateurs",
            Category.CLASS,
        ),
        Classification("28120", "Fabrication d'équipements hydrauliques et pneumatiques", Category.CLASS),
        Classification("28130", "Fabrication d'autres pompes et de compresseurs", Category.CLASS),
        Classification(
            "2813001", "Fabrication de pompes à air ou à vide et de compresseurs d'air ou d'autres gaz", Category.CLASS
        ),
        Classification(
            "2813002", "Fabrication de pompes pour liquides, même comportant un dispositif mesureur", Category.CLASS
        ),
        Classification("2813003", "Fabrication de pompes à béton", Category.CLASS),
        Classification("2812001", "Fabrication de moteurs hydrauliques, pneumatiques et éoliens", Category.CLASS),
        Classification("28140", "Fabrication d'autres articles de robinetterie", Category.CLASS),
        Classification(
            "2814001",
            "Fabrication de robinetterie et de vannes industrielles, y compris les vannes de régulation et la robinetterie d'adduction",
            Category.CLASS,
        ),
        Classification("28150", "Fabrication d'engrenages et d'organes mécaniques de transmission", Category.CLASS),
        Classification(
            "2815001",
            "Fabrication d'organes mécaniques de transmission de l'énergie: arbres de transmission, arbres à cames, vilebrequins, etc., manivelles, paliers et coussinets",
            Category.CLASS,
        ),
        Classification(
            "2815002",
            "Fabrication d'engrenages et de roues de friction ainsi que de réducteurs, de multiplicateurs et de variateurs de vitesse",
            Category.CLASS,
        ),
        Classification("2815003", "Fabrication d'embrayages et d'organes d'accouplement", Category.CLASS),
        Classification("2812011", "Fabrication d'organes hydrauliques de transmission", Category.CLASS),
        Classification("28210", "Fabrication de fours et de brûleurs", Category.CLASS),
        Classification(
            "2821001",
            "Fabrication et montage de fours électriques et d'autres fours industriels, de fours de laboratoires et d'incinérateurs",
            Category.CLASS,
        ),
        Classification(
            "2821002",
            "Fabrication de brûleurs, y compris les brûleurs pour chaudières de chauffage central",
            Category.CLASS,
        ),
        Classification("28220", "Fabrication de matériel de levage et de manutention", Category.CLASS),
        Classification("43299", "Autres travaux d'installation n.c.a.", Category.CLASS),
        Classification("2822001", "la fabrication de palans, treuils et cabestans, crics et vérins", Category.CLASS),
        Classification(
            "2822002",
            "Fabrication de bigues, grues, portiques et grues mobiles, chariots-cavaliers, etc.",
            Category.CLASS,
        ),
        Classification(
            "2822003",
            "Fabrication de chariots, même automobiles, munis ou non d'un dispositif de levage ou de manutention, des types utilisés dans les usines",
            Category.CLASS,
        ),
        Classification(
            "2822004",
            "Fabrication de manipulateurs mécaniques et robots industriels spécialement conçus pour des opérations de levage, de manutention, de chargement ou de déchargement",
            Category.CLASS,
        ),
        Classification(
            "2822005",
            "Fabrication d'appareils transporteurs ou convoyeurs, de téléphériques, d'élévateurs à liquides, etc.",
            Category.CLASS,
        ),
        Classification(
            "2822006", "Fabrication d'ascenseurs, d'escaliers mécaniques et de trottoirs roulants", Category.CLASS
        ),
        Classification("28250", "Fabrication d'équipements aérauliques et frigorifiques industriels", Category.CLASS),
        Classification(
            "2825001",
            "Fabrication et l'installation d'équipements industriels pour la production du froid",
            Category.CLASS,
        ),
        Classification("2825002", "Fabrication de comptoirs frigo", Category.CLASS),
        Classification(
            "2825003", "Fabrication de machines et appareils pour le conditionnement de l'air", Category.CLASS
        ),
        Classification("2825004", "Fabrication d'échangeurs de chaleur", Category.CLASS),
        Classification("2825005", "Fabrication de ventilateurs à usage non domestique", Category.CLASS),
        Classification("2829", "(null)", Category.CLASS),
        Classification("28291", "Fabrication de machines à emballer", Category.CLASS),
        Classification(
            "2829101",
            "Fabrication de machines et appareils à empaqueter ou emballer: machines et appareils à remplir, fermer, sceller, capsuler, étiqueter, etc.",
            Category.CLASS,
        ),
        Classification(
            "2829102",
            "Fabrication de chaînes de conditionnement munies de dispositis de pesée ou de dosage",
            Category.CLASS,
        ),
        Classification("28292", "Fabrication d'appareils de pesage", Category.CLASS),
        Classification(
            "28293", "Fabrication d'appareils de projection de matières liquides ou en poudre", Category.CLASS
        ),
        Classification(
            "2829301",
            "Fabrication d'appareils à projeter, disperser ou pulvériser des matières liquides ou en poudre: fabrication de pistolets aérographes, d'appareils à jet de vapeur, etc.",
            Category.CLASS,
        ),
        Classification("28294", "Fabrication de machines automatiques de vente de produits", Category.CLASS),
        Classification("28295", "Fabrication d'appareils de filtrage", Category.CLASS),
        Classification(
            "2829501",
            "Fabrication d'appareils pour la filtration ou l'épuration des liquides, de l'air ou d'autres gaz",
            Category.CLASS,
        ),
        Classification(
            "28296",
            "Fabrication de nettoyeurs à haute pression, de matériel industriel de nettoyage au sable et similaires",
            Category.CLASS,
        ),
        Classification("28299", "Fabrication d'autres machines d'usage général n.c.a.", Category.CLASS),
        Classification("33130", "Réparation de matériels électroniques et optiques", Category.CLASS),
        Classification(
            "2829901",
            "Fabrication d'appareils de distillation ou de rectification pour les raffineries de pétrole, les industries chimiques ou pour les industries des boissons",
            Category.CLASS,
        ),
        Classification("28300", "Fabrication de machines agricoles et forestières", Category.CLASS),
        Classification("2830001", "Fabrication de tracteurs agricoles et forestiers", Category.CLASS),
        Classification("2830002", "Fabrication de motoculteurs", Category.CLASS),
        Classification("2830011", "Fabrication de faucheuses, y compris les tondeuses à gazon", Category.CLASS),
        Classification(
            "2830012",
            "Fabrication de remorques ou de semi-remorques autochargeuses ou autodéchargeuses, pour usages agricoles",
            Category.CLASS,
        ),
        Classification(
            "2830013",
            "Fabrication de machines, appareils et engins agricoles pour la préparation du sol, la plantation des cultures ou l'épandage des engrais : charrues, épandeurs de fumier, semoirs, herses, etc.",
            Category.CLASS,
        ),
        Classification(
            "2830014",
            "Fabrication de machines, appareils et engins pour la récolte de produits agricoles et horticoles: moissonneuses, arracheuses, batteuses, machines pour le triage, etc.",
            Category.CLASS,
        ),
        Classification(
            "2830015", "Fabrication de machines et appareils de pulvérisation pour l'agriculture", Category.CLASS
        ),
        Classification(
            "2830016",
            "Fabrication d'autres machines et app. pour agriculture, aviculture, apiculture, prépar. des aliments ou provendes pour animaux, etc.; machines pour nettoyage, triage, calibrage des œufs, fruits, etc.",
            Category.CLASS,
        ),
        Classification(
            "95220",
            "Réparation d'appareils électroménagers et d'équipements pour la maison et le jardin",
            Category.CLASS,
        ),
        Classification(
            "3312001",
            "Entretien et réparation de tracteurs agricoles, de motoculteurs et de tondeuses à gazon",
            Category.CLASS,
        ),
        Classification("3312002", "Entretien et réparation d'autres machines agricoles et forestières", Category.CLASS),
        Classification("28240", "Fabrication d'outillage portatif à moteur incorporé", Category.CLASS),
        Classification("27900", "Fabrication d'autres matériels électriques", Category.CLASS),
        Classification("33140", "Réparation d'équipements électriques", Category.CLASS),
        Classification("28910", "Fabrication de machines pour la métallurgie", Category.CLASS),
        Classification(
            "2891001",
            "Fabrication de machines et appareils pour la manutention des métaux à haute température: convertisseurs, lingotières, poches de coulée, machines à couler (mouler)",
            Category.CLASS,
        ),
        Classification(
            "2892001",
            "Fabrication d'appareils élévateurs, transporteurs ou convoyeurs à action continue pour fonds de mines ou autres travaux souterrains",
            Category.CLASS,
        ),
        Classification("2892002", "Fabrication de bétonnières et appareils à gâcher le ciment", Category.CLASS),
        Classification(
            "2892003",
            "Fabrication de machines et appareils de terrassement : bouteurs (bulldozers), bouteurs biais (angledozers), niveleuses, décapeuses (scrapers), pelles mécaniques, chargeuses, etc.",
            Category.CLASS,
        ),
        Classification("28930", "Fabrication de machines pour l'industrie agro-alimentaire", Category.CLASS),
        Classification("2893001", "Fabrication de séchoirs pour produits agricoles", Category.CLASS),
        Classification(
            "2893002",
            "Fabrication de machines et appareils de laiterie : écrémeuses; machines et appareils pour le traitement du lait; machines et app. pour la transformation du lait; machines et app. de fromage",
            Category.CLASS,
        ),
        Classification(
            "2893003",
            "Fabrication de machines et app. pour la boulangerie, pâtisserie, biscuiterie ou la fabrication des pâtes aliment.: fours de boulangerie, malaxeurs à pâte, machines à trancher et à diviser la pâte, etc.",
            Category.CLASS,
        ),
        Classification(
            "2893004",
            "Fabrication de machines et appareils pour la transformation de divers produits alimentaires (pour la confiserie, la fabrication du cacao, du chocolat, pour la sucrerie, la brasserie, etc.)",
            Category.CLASS,
        ),
        Classification(
            "2893005",
            "Fabrication de machines et appareils pour la préparation des aliments dans les hôtels, les restaurants, etc.",
            Category.CLASS,
        ),
        Classification("28940", "Fabrication de machines pour les industries textiles", Category.CLASS),
        Classification(
            "2894001",
            "Fabrication de machines pour la préparation, la fabrication, le filage (extrusion), l'étirage, la texturation ou le tranchage des fibres, matières ou fils textiles,synthétiques ou artificiels",
            Category.CLASS,
        ),
        Classification(
            "2894002",
            "Fabrication de machines et appareils auxiliaires pour les machines de l'industrie textile: ratières, mécaniques Jacquard, casse-chaînes et casse-trames, mécanismes de changement de navettes, etc.",
            Category.CLASS,
        ),
        Classification(
            "2894003",
            "Fabrication de machines et app. pour le traitement des tissus: lavage, blanchîment, teinture, apprêt, finissage, enduction ou imprégnation; machines à enrouler, dérouler, etc. des tissus en mat. tex.",
            Category.CLASS,
        ),
        Classification(
            "2894004",
            "la fabrication de machines et appareils pour la fabrication ou le finissage du feutre ou des non-tissés",
            Category.CLASS,
        ),
        Classification(
            "2894005",
            "Fabrication de machines et appareils pour l'industrie du cuir: machines et appareils pour la préparation, le tannage ou le travail des cuirs ou des peaux",
            Category.CLASS,
        ),
        Classification("28950", "Fabrication de machines pour les industries du papier et du carton", Category.CLASS),
        Classification(
            "2895001",
            "Fabrication de machines et de matériel pour la fabrication des pâtes à papier par des procédés mécaniques ou chimiques",
            Category.CLASS,
        ),
        Classification("28990", "Fabrication d'autres machines d'usage spécifique n.c.a.", Category.CLASS),
        Classification(
            "28960", "Fabrication de machines pour le travail du caoutchouc ou des plastiques", Category.CLASS
        ),
        Classification("25731", "Fabrication de moules et modèles", Category.CLASS),
        Classification("2899001", "Fabrication de machines pour le traitement des déchets", Category.CLASS),
        Classification("2899002", "Fabrication de robots industriels à usage spécifique", Category.CLASS),
        Classification("25400", "Fabrication d'armes et de munitions", Category.CLASS),
        Classification("30300", "Construction aéronautique et spatiale", Category.CLASS),
        Classification("30400", "Construction de véhicules militaires de combat", Category.CLASS),
        Classification("33160", "Réparation et maintenance d'aéronefs et d'engins spatiaux", Category.CLASS),
        Classification("2540001", "Fabrication de matériel d'artillerie et de missiles balistiques", Category.CLASS),
        Classification("2540002", "Fabrication d'armes de guerre légères", Category.CLASS),
        Classification("27510", "Fabrication d'appareils électroménagers", Category.CLASS),
        Classification(
            "2751001",
            "Fabrication de réfrigérateurs et congélateurs-conservateurs, machines à laver la vaisselle, machines à laver et à sécher le linge",
            Category.CLASS,
        ),
        Classification(
            "2751002",
            "Fabrication d'appareils électrothermiques: chauffe-eau, couvertures chauffantes, appareils pour le chauffage des locaux et ventilateurs de type ménager, fers à repasser, à usage domestique",
            Category.CLASS,
        ),
        Classification("27520", "Fabrication d'appareils ménagers non électriques", Category.CLASS),
        Classification(
            "2752001",
            "Fabrication d'appareils pour le chauffage des locaux, cuisinières, grils, poêles, chauffe-eau à gaz, ustensiles de cuisine et chauffe-plats, non électriques",
            Category.CLASS,
        ),
        Classification(
            "2821011", "Fabrication de récupérateurs de chaleur solaire non photovoltaïques", Category.CLASS
        ),
        Classification(
            "28230",
            "Fabrication de machines et d'équipements de bureau (à l'exception des ordinateurs et des équipements périphériques)",
            Category.CLASS,
        ),
        Classification("2823001", "Fabrication de machines à écrire électriques ou manuelles", Category.CLASS),
        Classification("26200", "Fabrication d'ordinateurs et d'équipements périphériques", Category.CLASS),
        Classification("62090", "Autres activités informatiques", Category.CLASS),
        Classification(
            "2620001",
            "Fabrication de machines automatiques de traitement de l'information, y compris les micro-ordinateurs et les machines pour le traitement des textes: unités centrales, interfaces, consoles, etc.",
            Category.CLASS,
        ),
        Classification(
            "2620002",
            "Fabrication d'unités périphériques: imprimantes, terminaux, etc.; lecteurs de disques magnétiques ou optiques, machines de mise d'informations sur support sous forme codée",
            Category.CLASS,
        ),
        Classification("2561011", "Isolation intérieure des boîtiers d'ordinateurs", Category.CLASS),
        Classification("2711001", "Fabrication de moteurs à courant alternatif", Category.CLASS),
        Classification("2711002", "Fabrication de machines génératrices à courant alternatif", Category.CLASS),
        Classification("2711003", "Fabrication de transformateurs électriques", Category.CLASS),
        Classification("2711004", "Rebobinage d'électromoteurs et de transformateurs", Category.CLASS),
        Classification(
            "2711005", "Fabrication de panneaux électriques pour la récupération de chaleur solaire", Category.CLASS
        ),
        Classification("27120", "Fabrication de matériel de distribution et de commande électrique", Category.CLASS),
        Classification(
            "2733001",
            "Fabrication d'appareillages pour coupure, sectionnement, protection, branchement, raccordement ou connexion des circuits électriques: interrupteurs, commutateurs, coupe-circuits, etc.",
            Category.CLASS,
        ),
        Classification(
            "2712002",
            "Fabrication de tableaux, panneaux, consoles,pupitres, d'armoires et d'autres supports pour la commande ou la distribution électrique",
            Category.CLASS,
        ),
        Classification("27320", "Fabrication d'autres fils et de câbles électroniques ou électriques", Category.CLASS),
        Classification("27310", "Fabrication de câbles de fibres optiques", Category.CLASS),
        Classification(
            "2732001",
            "Fabrication de fils, de câbles, de bandes et d'autres conducteurs isolés, munis ou non de pièces de connexion",
            Category.CLASS,
        ),
        Classification("27200", "Fabrication de piles et d'accumulateurs électriques", Category.CLASS),
        Classification(
            "2720001",
            "Fabrication de piles et de batteries électriques, y compris les batteries pour véhicules à moteur",
            Category.CLASS,
        ),
        Classification("27401", "Fabrication de lampes", Category.CLASS),
        Classification(
            "2740101", "Fabrication de lampes et de tubes électriques à incandescence ou à décharge", Category.CLASS
        ),
        Classification("27402", "Fabrication d'appareils d'éclairage électrique", Category.CLASS),
        Classification(
            "2740201",
            "Fabrication de lustres, de lampes de bureau, de lampes de chevet ou de lampadaires d'intérieur, même non électriques",
            Category.CLASS,
        ),
        Classification("2740202", "Fabrication de lampes électriques portatives", Category.CLASS),
        Classification(
            "2740203",
            "Fabrication de lampes-réclames, d'enseignes lumineuses, de plaques indicatrices lumineuses, etc.",
            Category.CLASS,
        ),
        Classification("2740204", "Fabrication de projecteurs", Category.CLASS),
        Classification(
            "2740205",
            "Fabrication d'appareils d'éclairage extérieur et d'éclairage des voies publiques (à l’exception des feux de signalisation)",
            Category.CLASS,
        ),
        Classification(
            "2740206",
            "Fabrication de guirlandes électriques de types utilisés pour la décoration des arbres de Noël",
            Category.CLASS,
        ),
        Classification("2740207", "Fabrication d'appareils d'éclairage non électriques", Category.CLASS),
        Classification(
            "29310", "Fabrication d'équipements électriques et électroniques pour véhicules automobiles", Category.CLASS
        ),
        Classification(
            "2740211",
            "Fabrication d'appareils électriques d'éclairage pour les cycles, les motocycles ou les automobiles: phares, feux tournants, avertisseurs sonores, etc.",
            Category.CLASS,
        ),
        Classification(
            "2931001",
            "Fabrication d'essuie-glaces, de dégivreurs et de dispositifs électriques anti-buée, etc.",
            Category.CLASS,
        ),
        Classification("3092011", "Fabrication de dynamos pour cycles", Category.CLASS),
        Classification("26300", "Fabrication d'équipements de communication", Category.CLASS),
        Classification("30200", "Construction de locomotives et d'autre matériel ferroviaire roulant", Category.CLASS),
        Classification(
            "2790011",
            "Fabrication d'appareils électriques de signalisation, de sécurité, de contrôle ou de commande pour voies routières, ferrées, fluviales et installations portuaires, et pour aéroport",
            Category.CLASS,
        ),
        Classification(
            "2790012",
            "Fabrication d'autres appareils électriques de signalisation acoustique ou visuelle : sonneries, sirènes, tableaux annonciateurs, appareils avertisseurs pour la protection contre le vol ou l'incendie",
            Category.CLASS,
        ),
        Classification(
            "26510", "Fabrication d'instruments et d'appareils de mesure, d'essai et de navigation", Category.CLASS
        ),
        Classification(
            "2790001",
            "Fabrication de tubes isolateurs et de leurs pièces de raccordement, en métaux communs, isolés intérieurement",
            Category.CLASS,
        ),
        Classification(
            "2899011", "Fabrication de bancs et ciels solaires et autres appareils de bronzage", Category.CLASS
        ),
        Classification(
            "2790002",
            "Fabrication d'autres machines et appareils électriques: accélérateurs de particules, générateurs de signaux, détecteurs de mines, détonateurs électriques, etc.",
            Category.CLASS,
        ),
        Classification("26120", "Fabrication de cartes électroniques assemblées", Category.CLASS),
        Classification("2611001", "Fabrication de circuits imprimés nus", Category.CLASS),
        Classification("2611002", "Fabrication de cristaux piézo-électriques montés", Category.CLASS),
        Classification(
            "2611003",
            "Fabrication de circuits intégrés et de micro-assemblage électroniques: circuits intégrés monolithiques, circuits intégrés hybrides et micro-assemblages électroniques de blocs moulés, etc.",
            Category.CLASS,
        ),
        Classification("95120", "Réparation d'équipements de communication", Category.CLASS),
        Classification("2630001", "Fabrication de caméras de télévision", Category.CLASS),
        Classification(
            "2630002", "Fabrication d'équipements de radiodistribution et de télédistribution", Category.CLASS
        ),
        Classification("2630003", "Fabrication d'antennes d'émission", Category.CLASS),
        Classification("26400", "Fabrication de produits électroniques grand public", Category.CLASS),
        Classification(
            "2640001",
            "Fabrication d'appareils récepteurs de télévision, y compris les moniteurs vidéo et les projecteurs vidéo",
            Category.CLASS,
        ),
        Classification(
            "2640002",
            "Fabrication d’équipements de reproduction (appareils d'enregistrement ou de reproduction vidéophoniques), y compris les caméscopes",
            Category.CLASS,
        ),
        Classification(
            "2630011",
            "Fabrication d'appareils électro-acoustiques tels que interphones, installations d'interprétation simultanée, systèmes électroniques de vote, équipements pour conférences, etc.",
            Category.CLASS,
        ),
        Classification(
            "2640003",
            "Fabrication de microphones, de hauts-parleurs, d'écouteurs, d'amplificateurs d'audiofréquence et d'appareils d'amplification du son",
            Category.CLASS,
        ),
        Classification(
            "26600",
            "Fabrication d'équipements d'irradiation médicale, d'équipements électromédicaux et électrothérapeutiques",
            Category.CLASS,
        ),
        Classification(
            "2660001",
            "Fabrication d'appareils électriques pour la médecine, l'art dentaire et l'art vétérinaire",
            Category.CLASS,
        ),
        Classification(
            "2660011",
            "Fabrication d'appareils d'électrodiagnostic tels qu'électrocardiographes, app. de diagnostic par ultrasons, tomodensitomètres à scintillation, installations de résonance magnétique nucléaire, etc.",
            Category.CLASS,
        ),
        Classification("3250001", "Fabrication de tours dentaires", Category.CLASS),
        Classification("3250002", "Fabrication d'instruments d'ophtalmologie", Category.CLASS),
        Classification(
            "3250003",
            "Fabrication de mobilier pour la médecine, la chirurgie, l'art dentaire ou l'art vétérinaire: tables d'opération, lits à mécanismes pour usages cliniques, fauteuils de dentistes",
            Category.CLASS,
        ),
        Classification(
            "3250011",
            "Fabrication de matériel orthopédique et prothétique : ceintures et bandages médico-chirurgicaux, béquilles, attelles, gouttières, dents artific., chaussures orthopédiques, membres artific., etc.",
            Category.CLASS,
        ),
        Classification("26700", "Fabrication de matériels optiques et photographiques", Category.CLASS),
        Classification(
            "2651001", "Fabrication de balances de précision des types utilisés dans les laboratoire", Category.CLASS
        ),
        Classification(
            "2651002", "Fabrication de microscopes autres qu'optiques et de diffractographes", Category.CLASS
        ),
        Classification(
            "2651003",
            "Fabrication d'instruments et appareils de navigation, de météorologie, de géophysique, etc. (géodésie, océanographie, hydrologie, topographie, arpentage, radars, sonars,etc.)",
            Category.CLASS,
        ),
        Classification(
            "2651004", "Fabrication de compteurs d'électricité, d'eau, de gaz, d'essence, etc.", Category.CLASS
        ),
        Classification(
            "2651005", "Fabrication d'appareils et d'instruments optiques de mesure et de contrôle", Category.CLASS
        ),
        Classification(
            "2651006",
            "Fabrication d'autres instruments, appareils ou machines de mesure, de contrôle ou d'essais: densimètres, aréomètres, pèse-liquides, thermomètres, baromètres, compte-tours, taximètres, podomètres, etc.",
            Category.CLASS,
        ),
        Classification(
            "3320001",
            "Conception, assemblage et entretien de systèmes de contrôle des processus industriels continus",
            Category.CLASS,
        ),
        Classification(
            "3320002",
            "Conception, assemblage et entretien d'unités de production automatisées comprenant plusieurs machines, équipements de manutention et appareils de contrôle centralisés",
            Category.CLASS,
        ),
        Classification("3250021", "Fabrication de verres de lunetterie et de verres de contact", Category.CLASS),
        Classification("3250022", "Fabrication de montures de lunettes", Category.CLASS),
        Classification(
            "3250023",
            "Fabrication de montures équipées de verres travaillés optiquement ou non ; lunettes solaires, lunettes protectrices (y compris les écrans protecteurs pour soudage) ou correctrices, etc.",
            Category.CLASS,
        ),
        Classification(
            "2670001",
            "Fabrication de prismes, lentilles, miroirs optiques, filtres sélectifs de couleur, éléments polarisants,..., en verre ou en toute autre matière",
            Category.CLASS,
        ),
        Classification("26520", "Horlogerie", Category.CLASS),
        Classification("32123", "Fabrication d'articles de joaillerie et de bijouterie", Category.CLASS),
        Classification(
            "32130", "Fabrication d'articles de bijouterie de fantaisie et d'articles similaires", Category.CLASS
        ),
        Classification(
            "2652001",
            "Fabrication de montres et d'horloges de tous types (y compris les horloges de tableau de bord), de boîtiers de montres, de cages et cabinets d'horlogerie (y compris ceux en métaux précieux)",
            Category.CLASS,
        ),
        Classification("29100", "Construction et assemblage de véhicules automobiles", Category.CLASS),
        Classification("30910", "Fabrication de motocycles", Category.CLASS),
        Classification("2910001", "Fabrication de voitures de tourisme", Category.CLASS),
        Classification(
            "2910002",
            "Fabrication de véhicules utilitaires: camions et camionnettes, tracteurs routiers pour semi-remorques, etc.",
            Category.CLASS,
        ),
        Classification("2910003", "Fabrication de châssis pour véhicules à moteur", Category.CLASS),
        Classification(
            "2910004",
            "Fabrication d'autres véhic. automobiles : autoneiges et motoneiges, véhic. spéciaux pr le transport de pers. sur les terrains de golf, véhic. amphibies, autopompes, balayeuses, etc.",
            Category.CLASS,
        ),
        Classification("29201", "Fabrication de carrosseries de véhicules automobiles", Category.CLASS),
        Classification("29202", "Fabrication de remorques, de semi-remorques et de caravanes", Category.CLASS),
        Classification(
            "2920101", "Fabrication de carrosseries (y compris les cabines) pour véhicules automobiles", Category.CLASS
        ),
        Classification("2920211", "Fabrication de remorques et de semi-remorques", Category.CLASS),
        Classification("2920103", "Fabrication de conteneurs spécialement conçus pour le transport", Category.CLASS),
        Classification(
            "2920102",
            "Aménagement de tous types de véhicules automobiles (autocars, camions-citernes, camions-frigoriphiques, etc.)",
            Category.CLASS,
        ),
        Classification("2920201", "Fabrication et l'aménagement de caravanes", Category.CLASS),
        Classification("2920111", "Aménagement de véhicules de type autocaravane (motorhomes)", Category.CLASS),
        Classification("2920202", "Fabrication de remorques pour le camping", Category.CLASS),
        Classification("29320", "Fabrication d'autres équipements pour véhicules automobiles", Category.CLASS),
        Classification(
            "2932001",
            "Fabrication de freins, boîtes de vitesses, essieux, roues, amortisseurs, radiateurs, silencieux, tuyaux d'échappement, catalyseurs, embrayages, volants, colonnes et boîtiers de direction",
            Category.CLASS,
        ),
        Classification("2811011", "Fabrication de culasses, bielles, pistons, segments, etc.", Category.CLASS),
        Classification("2932002", "Fabrication de ceintures de sécurité, portières, parechocs, etc.", Category.CLASS),
        Classification("33150", "Réparation et maintenance navale", Category.CLASS),
        Classification("30110", "Construction de navires et de structures flottantes", Category.CLASS),
        Classification(
            "3315001",
            "Entretien et réparation de navires ou de parties de navires: navires à passagers, transbordeurs, cargos, bateaux-citernes, etc.",
            Category.CLASS,
        ),
        Classification(
            "3315002",
            "Entretien et réparation de navires ou de parties de navires: navires de guerre (y compris l'implantation des systèmes d'armes)",
            Category.CLASS,
        ),
        Classification(
            "3315003", "Entretien et réparation de navires ou de parties de navires : remorqueurs", Category.CLASS
        ),
        Classification(
            "3315004", "Entretien et réparation de navires ou de parties de navires: bateaux de pêche", Category.CLASS
        ),
        Classification("3011001", "Construction d'aéroglisseurs", Category.CLASS),
        Classification(
            "3011002",
            "Construction de docks flottants, pontons, caissons, coffres d'amarrage flottants, etc.",
            Category.CLASS,
        ),
        Classification("3011003", "Peinture des navires par des unités spécialisées", Category.CLASS),
        Classification("3831001", "Démolition de bateaux", Category.CLASS),
        Classification("30120", "Construction de bateaux de plaisance", Category.CLASS),
        Classification("3012001", "Construction de bateaux et de radeaux gonflables", Category.CLASS),
        Classification("3012002", "Construction de voiliers, avec ou sans moteur auxiliaire", Category.CLASS),
        Classification("3012003", "Construction de bateaux à moteur", Category.CLASS),
        Classification(
            "3012004",
            "Construction d'autres embarcations de plaisance et de sport: canoës, kayaks, skiffs, etc.",
            Category.CLASS,
        ),
        Classification("3315011", "Entretien et réparation de bateaux de plaisance ou de sport", Category.CLASS),
        Classification("33170", "Réparation et maintenance d'autres équipements de transport", Category.CLASS),
        Classification(
            "3020001",
            "Fabrication d'appareils mécaniques et électromécaniques de signalisation, de sécurité, de contrôle ou de commande pour voies: ferrées, routières, fluviales, installations portuaires, etc.",
            Category.CLASS,
        ),
        Classification(
            "3317001",
            "Entretien et la réparation de matériel ferroviaire roulant et d'appareils mécaniques et électromécaniques de signalisation ou de sécurité",
            Category.CLASS,
        ),
        Classification(
            "3030001",
            "Construction d'avions conçus pour le transport de marchandises ou de passagers, pour les forces militaires (y compris l'implantation des armements), pour le sport ou pour d'autres usages",
            Category.CLASS,
        ),
        Classification("3030002", "Construction d'hélicoptères", Category.CLASS),
        Classification("3030003", "Construction d'avions dits ULM", Category.CLASS),
        Classification(
            "3030004",
            "Fabrication et assemblage de parties et accessoires de véhicules aériens: fuselages, ailes, portes, empennages, gouvernes, trains d'atterrissage, réservoirs à combustibles, nacelles, etc.",
            Category.CLASS,
        ),
        Classification(
            "3030005",
            "Fabrication et assemblage de parties et accessoires de véhicules aériens : moteurs des types généralement utilisés pour la propulsion des véhic. aériens et parties de turboréacteurs et -propulseurs",
            Category.CLASS,
        ),
        Classification(
            "3091001",
            "Fabrication de motocycles, de cyclomoteurs et de cycles équipés d'un moteur auxiliaire",
            Category.CLASS,
        ),
        Classification("30920", "Fabrication de bicyclettes et de véhicules pour invalides", Category.CLASS),
        Classification(
            "3092001",
            "Fabrication de bicyclettes et autres cycles sans moteur, y compris les triporteurs, les tandems ainsi que les bicyclettes et tricycles d’enfants",
            Category.CLASS,
        ),
        Classification("3092002", "Fabrication de parties et accessoires de bicyclettes", Category.CLASS),
        Classification("30990", "Fabrication d'autres équipements de transport n.c.a.", Category.CLASS),
        Classification("31010", "Fabrication de meubles de bureau et de magasin", Category.CLASS),
        Classification(
            "3099001", "Fabrication de brouettes, de diables, de charrettes à bras, de caddies, etc.", Category.CLASS
        ),
        Classification("3099002", "Fabrication de véhicules à traction animale", Category.CLASS),
        Classification(
            "31091",
            "Fabrication de salles à manger, de salons, de chambres à coucher et de salles de bain",
            Category.CLASS,
        ),
        Classification("31020", "Fabrication de meubles de cuisine", Category.CLASS),
        Classification("31092", "Fabrication de meubles de jardin et d'extérieur", Category.CLASS),
        Classification("95240", "Réparation de meubles et d'équipements du foyer", Category.CLASS),
        Classification(
            "3109101",
            "Fabrication de sièges d'ameublement et de parties de sièges: chaises, bancs, fauteuils, canapés, tabourets, etc.",
            Category.CLASS,
        ),
        Classification("3101021", "Fabrication de sièges de bureau et d'atelier", Category.CLASS),
        Classification("3109102", "Finissage des sièges par des opérations telles que le rembourrage", Category.CLASS),
        Classification(
            "3101001",
            "Fabrication de meubles spéciaux pour magasins: comptoirs, présentoirs, rayonnages, etc.",
            Category.CLASS,
        ),
        Classification(
            "3101002",
            "Fabrication de meubles de bureau et d'atelier, meubles pour restaurants, écoles, églises, etc.",
            Category.CLASS,
        ),
        Classification(
            "3101011",
            "Fabrication de meubles spéciaux pour magasins, autres qu'en métal: comptoirs, présentoirs, rayonnages, etc.",
            Category.CLASS,
        ),
        Classification(
            "3101012",
            "Fabrication de meubles de bureau et d'atelier, meubles pour restaurants, écoles, églises, etc., autres qu'en métal",
            Category.CLASS,
        ),
        Classification(
            "3102001", "Fabrication de meubles et d'éléments modulaires pour cuisines équipées", Category.CLASS
        ),
        Classification("3109121", "Fabrication de meubles de salle de bains", Category.CLASS),
        Classification("31099", "Fabrication d'autres meubles n.c.a.", Category.CLASS),
        Classification(
            "3109111",
            "Fabrication et finissage (y compris le capitonnage, la mise en peinture, le vernissage, etc.) de meubles de types utilisés dans les chambres à coucher et dans les salles à manger et de séjour",
            Category.CLASS,
        ),
        Classification(
            "3109901",
            "Fabrication de placards, de meubles spéciaux pour appareils de télévision, de meubles de complément, etc.",
            Category.CLASS,
        ),
        Classification("9524001", "Rénovation et la restauration de meubles", Category.CLASS),
        Classification("31030", "Fabrication de matelas", Category.CLASS),
        Classification(
            "3103001", "Fabrication de sommiers, de sommiers à lattes et d'autres supports de matelas", Category.CLASS
        ),
        Classification(
            "3103002",
            "Fabrication de matelas: matelas comportant des ressorts ou rembourrés ou garnis intérieurement d'un matériau de soutien; matelas non recouverts en caoutchouc ou en matières plastiques alvéolaires",
            Category.CLASS,
        ),
        Classification("32110", "Frappe de monnaie", Category.CLASS),
        Classification(
            "3211001", "Fabrication de médailles et de médaillons, en métaux précieux ou non", Category.CLASS
        ),
        Classification("32121", "Travail du diamant", Category.CLASS),
        Classification(
            "3212101",
            "Travail du diamant, y compris le diamant de qualité industrielle: scier, tailler, polir, etc.",
            Category.CLASS,
        ),
        Classification(
            "32122", "Travail des pierres précieuses (sauf le diamant) et des pierres semi-précieuses", Category.CLASS
        ),
        Classification("3212201", "Fabrication de perles travaillées", Category.CLASS),
        Classification(
            "3212202",
            "Fabrication de pierres gemmes (précieuses ou fines) travaillées, à l'exclusion du diamant",
            Category.CLASS,
        ),
        Classification(
            "3212203",
            "Travail de pierres de qualité industrielle (à l'exclusion du diamant) et de pierres synthétiques ou reconstituées",
            Category.CLASS,
        ),
        Classification(
            "3212301",
            "Fabrication d'art. de bijouterie en métaux précieux, en plaqués ou en doublés de métaux précieux ou de pierres gemmes sur des métaux communs, ou en assembl. de métaux précieux et de pierres gemmes",
            Category.CLASS,
        ),
        Classification("3212302", "Fabrication de bracelets de montres en métaux précieux", Category.CLASS),
        Classification("32124", "Fabrication d'articles d'orfèvrerie", Category.CLASS),
        Classification("32129", "Fabrication d'autres articles en métaux précieux", Category.CLASS),
        Classification(
            "3212401",
            "Fabrication d'art. d'orfèvrerie en métaux précieux ou en plaqués ou doublés de métaux précieux sur des métaux communs: vaisselle plate ou creuse, couverts, art. de toilette, garnitures de bureau, etc.",
            Category.CLASS,
        ),
        Classification("3212901", "Gravure d'objets en métaux précieux", Category.CLASS),
        Classification("32200", "Fabrication d'instruments de musique", Category.CLASS),
        Classification("3220001", "Fabrication d'instruments à cordes", Category.CLASS),
        Classification(
            "3220002",
            "Fabrication d'instruments à cordes et à clavier, y compris les pianos automatiques",
            Category.CLASS,
        ),
        Classification("3220003", "Fabrication d'instruments à vent", Category.CLASS),
        Classification("3220004", "Fabrication d'instruments de musique à percussion", Category.CLASS),
        Classification(
            "3220005", "Fabrication d'instruments de musique dont le son est produit électroniquement", Category.CLASS
        ),
        Classification("9529021", "Réparation d'instruments de musique", Category.CLASS),
        Classification("32300", "Fabrication d'articles de sport", Category.CLASS),
        Classification("3230001", "Fabrication de balles et ballons durs, mous ou gonflables", Category.CLASS),
        Classification("3230002", "Fabrication de raquettes, battes et clubs de golf", Category.CLASS),
        Classification("3230003", "Fabrication de bassins pour piscines et pataugeoires", Category.CLASS),
        Classification("3230004", "Fabrication de gants et coiffures de sport en cuir", Category.CLASS),
        Classification("32400", "Fabrication de jeux et de jouets", Category.CLASS),
        Classification("3240001", "Fabrication de poupées, de vêtements et accessoires pour poupées", Category.CLASS),
        Classification("3240002", "Fabrication de jouets représentant des animaux", Category.CLASS),
        Classification("3240003", "Fabrication d'articles pour jeux de société et de cartes à jouer", Category.CLASS),
        Classification(
            "3240004",
            "Fabrication de jeux à moteur ou à mouvement, de jeux fonctionnant au moyen de pièces de monnaie, de billard, de tables spéciales pour jeux de casino, de jeux de quilles automatiques (bowlings), etc.",
            Category.CLASS,
        ),
        Classification("3240005", "Fabrication de jeux électroniques: jeux vidéo, jeux d'échecs, etc.", Category.CLASS),
        Classification(
            "3240006",
            "Fabrication de modèles réduits et de modèles similaires pour le divertissement, de trains électriques, de circuits auto, de jeux de construction, etc.",
            Category.CLASS,
        ),
        Classification(
            "3213001",
            "Fabrication de bijoux de fantaisie et art. simil. ni plaqués, ni doublés de métaux précieux; art. de bijouterie contenant des pierres artific. : pierres précieuses artific., diamants de synthèse, etc.",
            Category.CLASS,
        ),
        Classification("32910", "Fabrication d'articles de brosserie", Category.CLASS),
        Classification(
            "3299001",
            "Fabrication de dateurs, de cachets ou de numéroteurs, d'app. manuels pour l'impression d'étiquettes, d'imprimeries à main, de rubans encreurs prépar. pour machines à écrire et de tampons encreurs",
            Category.CLASS,
        ),
        Classification("3299002", "Fabrication de briquettes", Category.CLASS),
        Classification(
            "3299003",
            "Fabrication d'articles à usage personnel: pipes, peignes à coiffer, barrettes, vaporisateurs de toilette, perruques, fausses barbes, bouteilles isolantes, etc.",
            Category.CLASS,
        ),
        Classification(
            "2899021",
            "Fabrication de manèges, de balançoires, de stands de tir et d'autres attractions pour foires et parcs d'attractions",
            Category.CLASS,
        ),
        Classification(
            "2223011",
            "Fabrication de linoléum et de revêtements de sol rigides en des matières autres que les matières plastiques",
            Category.CLASS,
        ),
        Classification("3299004", "Fabrication de bougies, chandelles, cierges et articles similaires", Category.CLASS),
        Classification(
            "3299005",
            "Fabrication de fleurs, fruits et feuillages artificiels et d'articles d'ornementation en fleurs séchées",
            Category.CLASS,
        ),
        Classification(
            "3299006",
            "Fabrication d'articles-surprises, d'articles pour fêtes et d'articles de prestidigitation",
            Category.CLASS,
        ),
        Classification(
            "3299007",
            "Fabrication d'articles divers: tamis et cribles à main, mannequins et autres articles de vitrine, etc.",
            Category.CLASS,
        ),
        Classification("38322", "Récupération de déchets métalliques", Category.CLASS),
        Classification("38310", "Démantèlement d'épaves", Category.CLASS),
        Classification("38321", "Tri de matériaux récupérables", Category.CLASS),
        Classification(
            "3832201",
            "Récupération de métaux ferreux et non ferreux recyclables par broyage par des procédés mécaniques d'objets métalliques tels que vieilles voitures, machines à laver hors d'usage, vieux vélos, etc.",
            Category.CLASS,
        ),
        Classification(
            "3832202",
            "Récupération de métaux ferreux et non ferreux recyclables par la réduction par des procédés mécaniques, d'objets métalliques volumineux tels que wagons de chemin de fer",
            Category.CLASS,
        ),
        Classification(
            "3831011",
            "Récupération de métaux ferreux et non ferreux recyclables par le compactage des ferrailles et des véhicules usagés",
            Category.CLASS,
        ),
        Classification(
            "3831012",
            "Récupération de métaux ferreux et non ferreux recyclables par le démontage d'objets hors d'usage (voitures p.ex.) afin d'en extraire les éléments récupérables",
            Category.CLASS,
        ),
        Classification(
            "3831013",
            "Récupération de métaux ferreux et non ferreux recyclables par le démontage d'objets hors d'usage (voitures ou réfrigérateurs p.ex.) afin d'en éliminer les éléments toxiques (huile p.ex.)",
            Category.CLASS,
        ),
        Classification("38323", "Récupération de déchets inertes", Category.CLASS),
        Classification(
            "3832901",
            "Régénération de caoutchouc (p.ex. régénération de pneumatiques usagés) afin d'obtenir des matières premières secondaires",
            Category.CLASS,
        ),
        Classification(
            "3832902",
            "Triage et pastillage de matières plastiques en vue d'obtenir des matières premières secondaires utilisables pour la fabrication de tubes, de pots à fleurs, de palettes, etc.",
            Category.CLASS,
        ),
        Classification("38329", "Récupération d'autres déchets triés", Category.CLASS),
        Classification(
            "3832903",
            "Broyage, nettoyage et triage d'autres déchets en vue d'obtenir des matières premières secondaires",
            Category.CLASS,
        ),
        Classification("35140", "Commerce d'électricité", Category.CLASS),
        Classification("35110", "Production d'électricité", Category.CLASS),
        Classification("35120", "Transport d'électricité", Category.CLASS),
        Classification("38120", "Collecte des déchets dangereux", Category.CLASS),
        Classification("35130", "Distribution d'électricité", Category.CLASS),
        Classification("35220", "Distribution de combustibles gazeux par conduites", Category.CLASS),
        Classification("35210", "Production de combustibles gazeux", Category.CLASS),
        Classification("35230", "Commerce de combustibles gazeux par conduites", Category.CLASS),
        Classification("35300", "Production et distribution de vapeur et d'air conditionné", Category.CLASS),
        Classification(
            "3530001",
            "Production, collecte et distribution de vapeur et d'eau chaude pour le chauffage, la force motrice et d'autres usages",
            Category.CLASS,
        ),
        Classification(
            "3530002", "Production et la distribution d'eau froide ou de glace pour le refroidissement", Category.CLASS
        ),
        Classification("36000", "Captage, traitement et distribution d'eau", Category.CLASS),
        Classification("3600001", "Captage, épuration et distribution d'eau", Category.CLASS),
        Classification("43110", "Travaux de démolition", Category.CLASS),
        Classification("4311001", "Démolition d'immeubles et autres constructions", Category.CLASS),
        Classification("4312011", "Déblayage des chantiers", Category.CLASS),
        Classification("43120", "Travaux de préparation des sites", Category.CLASS),
        Classification(
            "4312001",
            "Travaux de terrassement: creusement, comblement, nivellement de chantiers de construction, ouverture de tranchées, dérochement, destruction à l'explosif, etc.",
            Category.CLASS,
        ),
        Classification(
            "4312002",
            "Préparation de sites pour l'exploitation minière: enlèvement de déblais et autres travaux d'aménagement et de préparation des terrains et sites miniers",
            Category.CLASS,
        ),
        Classification(
            "4312003", "Rabattement de la nappe aquifère et drainage des chantiers des construction", Category.CLASS
        ),
        Classification("4312004", "Drainage des terrains agricoles et sylvicoles", Category.CLASS),
        Classification("43130", "Forages d'essai et sondages", Category.CLASS),
        Classification(
            "4313001",
            "Sondages d'essai, les forages d'essai et les carottages pour la construction ainsi que pour les études géophysiques, géologiques et similaires",
            Category.CLASS,
        ),
        Classification(
            "4313002", "Exécution de forages horizontaux pour passages de câbles ou de canalisations", Category.CLASS
        ),
        Classification("41203", "Construction générale d'autres bâtiments non résidentiels", Category.CLASS),
        Classification("4120121", "Réalisation du gros œuvre des bâtiments", Category.CLASS),
        Classification("4120122", "Coordination générale sur le chantier", Category.CLASS),
        Classification("41201", "Construction générale de bâtiments résidentiels", Category.CLASS),
        Classification("4120101", "Réalisation du gros oeuvre de maisons individuelles", Category.CLASS),
        Classification("4120102", 'Construction de maisons individuelles "clés en mains"', Category.CLASS),
        Classification("41202", "Construction générale d'immeubles de bureaux", Category.CLASS),
        Classification(
            "4120111",
            "Réalisation du gros oeuvre de bâtiments à cellules multiples (appartements, etc.)",
            Category.CLASS,
        ),
        Classification("4120112", 'Réalisation d\'appartements "clés en mains"', Category.CLASS),
        Classification("42990", "Construction d'autres ouvrages de génie civil n.c.a.", Category.CLASS),
        Classification("43999", "Autres activités de construction spécialisées", Category.CLASS),
        Classification(
            "4120301",
            "Réalisation du gros oeuvre de bâtiments et ouvrages industriels ou commerciaux, de dépôts de véhicules, d'entrepôts, d'écoles, de cliniques, de bâtiments pour la pratique d'un culte, etc.",
            Category.CLASS,
        ),
        Classification("4120302", "Montage de hangars, granges, silos, ..., à usages agricoles", Category.CLASS),
        Classification("42130", "Construction de ponts et de tunnels", Category.CLASS),
        Classification(
            "4213001",
            "Construction de ponts, y compris ceux destinés à supporter des routes surélevées, viaducs, etc.",
            Category.CLASS,
        ),
        Classification(
            "4213002",
            "Construction de tunnels routiers et ferroviaires et d'autres passages souterrains",
            Category.CLASS,
        ),
        Classification("42220", "Construction de réseaux électriques et de télécommunications", Category.CLASS),
        Classification("42211", "Construction de réseaux de distribution d'eau et de gaz", Category.CLASS),
        Classification("42212", "Construction de réseaux d'évacuation des eaux usées", Category.CLASS),
        Classification("42219", "Construction de réseaux pour fluides n.c.a.", Category.CLASS),
        Classification(
            "4221911", "Construction de réseaux d'adduction, de distribution et d'évacuation des eaux", Category.CLASS
        ),
        Classification(
            "4221912", "Construction de réseaux de transport de gaz, de produits pétroliers, etc.", Category.CLASS
        ),
        Classification(
            "4222001", "Construction de lignes de transport et de distribution d'énergie électrique", Category.CLASS
        ),
        Classification("4222002", "Construction de lignes et de réseaux de télécommunication", Category.CLASS),
        Classification("43910", "Travaux de couverture", Category.CLASS),
        Classification("43991", "Travaux d'étanchéification des murs", Category.CLASS),
        Classification("4391001", "Montage de charpentes", Category.CLASS),
        Classification("4391002", "Travaux de couverture en tous matériaux", Category.CLASS),
        Classification("4391003", "Mise en place des éléments d'évacuation des eaux de pluie", Category.CLASS),
        Classification("4399101", "Travaux d'étanchéification des toits et des toituresterrasses", Category.CLASS),
        Classification("42110", "Construction de routes et d'autoroutes", Category.CLASS),
        Classification("42120", "Construction de voies ferrées de surface et souterraines", Category.CLASS),
        Classification(
            "4212001",
            "Construction de voies ferrées: pose du ballast et des rails, remise en état et réparations des voies",
            Category.CLASS,
        ),
        Classification(
            "4211001",
            "Constructions d'autoroutes, de routes, de rues, de chaussées et d'autres voies pour véhicules et piétons (y compris la pose de glissières de sécurité)",
            Category.CLASS,
        ),
        Classification("4211002", "Construction de pistes d'atterrissage", Category.CLASS),
        Classification(
            "4299001", "Construction de terrains de jeux et de sport, de bassins de natation, etc.", Category.CLASS
        ),
        Classification(
            "4211003", "Marquage à la peinture des chaussées et des aires ou parcs de stationnement", Category.CLASS
        ),
        Classification("42911", "Travaux de dragage", Category.CLASS),
        Classification("4291101", "Réalisation de travaux de dragage", Category.CLASS),
        Classification("4291102", "Curage des cours d'eau, fossés, etc.", Category.CLASS),
        Classification(
            "42919", "Construction d'ouvrages maritimes et fluviaux, sauf travaux de dragage", Category.CLASS
        ),
        Classification(
            "4291901", "Construction de ports (y compris les ports de plaisance) et de bassins", Category.CLASS
        ),
        Classification("4291902", "Construction de barrages et de digues", Category.CLASS),
        Classification("4291903", "Construction de canaux et d'autres voies navigables", Category.CLASS),
        Classification("4291904", "Construction d'écluses et autres ouvrages de régulation", Category.CLASS),
        Classification(
            "4291905",
            "Construction de bassins de décantation et d'autres ouvrages pour l'épuration des eaux usées",
            Category.CLASS,
        ),
        Classification("4399921", "Exécution des travaux sous-marins de toute nature", Category.CLASS),
        Classification("43993", "Construction de cheminées décoratives et de feux ouverts", Category.CLASS),
        Classification("43994", "Travaux de maçonnerie et de rejointoiement", Category.CLASS),
        Classification("43995", "Travaux de restauration des bâtiments", Category.CLASS),
        Classification("43996", "Pose de chapes", Category.CLASS),
        Classification("4399901", "Mise en place de fondations, y compris le battage de pieux", Category.CLASS),
        Classification("4221901", "Forage et construction de puits d'eau, fonçage de puits", Category.CLASS),
        Classification("4399902", "Travaux de ferraillage et pose de coffrage", Category.CLASS),
        Classification("4399401", "Maçonnerie", Category.CLASS),
        Classification("4399601", "Pose de chape", Category.CLASS),
        Classification("4399903", "Construction de cheminées et de fours industriels", Category.CLASS),
        Classification("4399301", "Construction de cheminées décoratives et de feux ouverts", Category.CLASS),
        Classification(
            "4399904",
            "Montage d'éléments de structures métalliques non fabriqués par l'unité qui exécute les travaux",
            Category.CLASS,
        ),
        Classification("4399905", "Exécution pour les tiers de travaux de levage", Category.CLASS),
        Classification("4399906", "Montage et démontage d'échafaudages et de plates-formes de travail", Category.CLASS),
        Classification("4399402", "Exécution de travaux de rejointoiement", Category.CLASS),
        Classification("4399907", "Construction de chambres froides, chambres fortes, etc.", Category.CLASS),
        Classification("43211", "Travaux d'installation électrotechnique de bâtiment", Category.CLASS),
        Classification(
            "43222", "Installation de chauffage, de ventilation et de conditionnement d'air", Category.CLASS
        ),
        Classification("80200", "Activités liées aux systèmes de sécurité", Category.CLASS),
        Classification("4321101", "Installation de câbles et appareils électriques", Category.CLASS),
        Classification(
            "3320011", "Installation de systèmes d'alimentation de secours (groupes électrogènes)", Category.CLASS
        ),
        Classification(
            "4321102", "Installation de systèmes de télécommunication et installations informatiques", Category.CLASS
        ),
        Classification("4322211", "Installation d'installations électriques de chauffage", Category.CLASS),
        Classification("4329911", "Installation d'ascenseurs et escaliers mécaniques", Category.CLASS),
        Classification(
            "4321103", "Installation de systèmes de surveillance et d'alarme contre les effractions", Category.CLASS
        ),
        Classification("4329912", "Installation d'antennes d'immeubles et paratonnerres", Category.CLASS),
        Classification("43291", "Travaux d'isolation", Category.CLASS),
        Classification(
            "4329101",
            "Mise en oeuvre dans des bâtiments ou d'autres projets de construction de: matériaux d'isolation thermique, matériaux d'isolation acoustique et antivibratile",
            Category.CLASS,
        ),
        Classification(
            "4329102", "Travaux d'isolation de canalisations de chauffage ou de réfrigération", Category.CLASS
        ),
        Classification(
            "4329103", "Travaux d'isolation de chambres froides ou d'entrepôts frigorifiques", Category.CLASS
        ),
        Classification(
            "4322201",
            "Installation dans des bâtim. ou d'autres projets de construction de: systèmes de chauff. à l’électricité, au gaz et au mazout, chaudières, matér. et conduites de ventilation et de climatisation, etc.",
            Category.CLASS,
        ),
        Classification(
            "4322202",
            "Installation de systèmes de chauffage, de climatisation et de ventilation (sauf chauffage)",
            Category.CLASS,
        ),
        Classification("43221", "Travaux de plomberie", Category.CLASS),
        Classification(
            "4322101",
            "Installation dans des bâtim. ou autres constr. de : plomberie et app. sanitaires, conduites et raccordements de gaz ou d'eau (excepté pour chauff.), installation d'extinction automat. d'incendie, etc.",
            Category.CLASS,
        ),
        Classification("43212", "Travaux d'installation électrotechnique autres que de bâtiment", Category.CLASS),
        Classification(
            "4321201",
            "Installation de systèmes d'éclairage et de signalisation pour chaussées, voies ferrées, aéroports et installations portuaires (y compris l'installation de panneaux de signalisation)",
            Category.CLASS,
        ),
        Classification("4329901", "Installation de stores et bannes", Category.CLASS),
        Classification("4329902", "Installation d'enseignes, lumineuses ou non", Category.CLASS),
        Classification(
            "4329903", "Autres travaux d'installation n.d.a., y compris l'installation d'accessoires", Category.CLASS
        ),
        Classification("4329904", "Travaux d'installation générale", Category.CLASS),
        Classification("43310", "Travaux de plâtrerie", Category.CLASS),
        Classification(
            "4331001",
            "Application dans des bâtiments ou d'autres projets de construction, de plâtre ou de stuc pour l'intérieur ou l'extérieur, y compris les matériaux de lattage associés",
            Category.CLASS,
        ),
        Classification("4332031", "Montage de cloisons sèches à base de plâtre", Category.CLASS),
        Classification("43332", "Pose de revêtements en bois de sols et de murs", Category.CLASS),
        Classification(
            "4332001",
            "Montage de menuiseries extérieures et intérieures: portes, fenêtres, escaliers, placards de cuisines équipées, équipements pour magasins, dormants de portes et fenêtres, etc.",
            Category.CLASS,
        ),
        Classification(
            "4332002",
            "Montage de cloisons mobiles; revêtement de murs, de plafonds etc., en bois ou en matière plastique",
            Category.CLASS,
        ),
        Classification(
            "4332003",
            "Montage de portes de garage, de volets, de persiennes, de grillages, de grilles etc., en bois ou en matière plastique",
            Category.CLASS,
        ),
        Classification(
            "4332004",
            "Montage de portes blindées et de portes coupe-feux en bois ou en matière plastique",
            Category.CLASS,
        ),
        Classification(
            "4332005", "Montage de serres, de vérandas etc., en bois ou en matière plastique", Category.CLASS
        ),
        Classification(
            "4332011",
            "Montage de menuiseries extérieurs et intérieurs métallique: portes, fenêtres, dormants de portes et fenêtres, escaliers, placards de cuisines équipées, équipements pour magasins, etc.",
            Category.CLASS,
        ),
        Classification(
            "4332012", "Montage de cloisons mobiles; revêtement de murs, de plafonds, etc., métallique", Category.CLASS
        ),
        Classification(
            "4332013",
            "Montage de portes de garage, de volets, de persiennes, de grillages, de grilles, etc., métallique",
            Category.CLASS,
        ),
        Classification("4332014", "Montage de portes blindées et portes coupe-feux, métallique", Category.CLASS),
        Classification("4332015", "Montage de serres, de vérandas, etc., métallique", Category.CLASS),
        Classification(
            "4332016", "Montage de menuiseries extérieures et intérieures en matière plastique", Category.CLASS
        ),
        Classification("43331", "Pose de carrelages de sols et de murs", Category.CLASS),
        Classification(
            "4333101",
            "Pose dans des bâtiments ou d'autres projets de construction: revêtements muraux ou carrelages en céramique, en béton ou en pierre de taille; revêtements de sols et de murs en granit, etc.",
            Category.CLASS,
        ),
        Classification(
            "43333", "Pose de papiers peints et de revêtements de murs et de sols en d'autres matériaux", Category.CLASS
        ),
        Classification(
            "4333201",
            "Pose dans des bâtiments ou d'autres projets de construction de : parquets et autres revêtements de sols en bois, revêtement de cloison en bois",
            Category.CLASS,
        ),
        Classification("4333301", "Pose de papiers peints", Category.CLASS),
        Classification("43341", "Peinture de bâtiments", Category.CLASS),
        Classification("43342", "Peinture de travaux de génie civil", Category.CLASS),
        Classification("4334101", "Peinture intérieure et extérieure des bâtiments", Category.CLASS),
        Classification("4399111", "Traitement des murs avec des produits hydrofuges", Category.CLASS),
        Classification("4334201", "Peinture d'ossatures métalliques", Category.CLASS),
        Classification("4334202", "Peinture de navires et de bateaux par des unités non spécialisées", Category.CLASS),
        Classification("43343", "Vitrerie", Category.CLASS),
        Classification("4334301", "Pose de vitres, de miroirs, etc.", Category.CLASS),
        Classification(
            "4332021", "Installation de portes intérieures, de cloisons de séparation, ..., en verre", Category.CLASS
        ),
        Classification("43390", "Autres travaux de finition", Category.CLASS),
        Classification("43992", "Ravalement des façades", Category.CLASS),
        Classification("4399931", "Installation de piscines privées", Category.CLASS),
        Classification(
            "4399201",
            "Nettoyage à la vapeur, le sablage et les activités analogues appliquées aux parties extérieures des bâtiments",
            Category.CLASS,
        ),
        Classification(
            "4339001", "Nettoyage de bâtiments nouveaux et remise en état des lieux après travaux", Category.CLASS
        ),
        Classification("4339002", "Autres travaux d'achèvement et de finition des bâtiments n.d.a.", Category.CLASS),
        Classification("4399911", "Location avec opérateur de matériel de construction", Category.CLASS),
        Classification(
            "45111",
            "Commerce de gros d'automobiles et d'autres véhicules automobiles légers ( = 3,5 tonnes )",
            Category.CLASS,
        ),
        Classification("45191", "Commerce de gros d'autres véhicules automobiles ( > 3,5 tonnes )", Category.CLASS),
        Classification(
            "4511101",
            "Commerce de gros de véhicules automobiles pour le transport des personnes, y compris les véhicules automobiles spéciaux (p.ex. ambulances), neufs ou usagés",
            Category.CLASS,
        ),
        Classification(
            "4519101",
            "Commerce de gros de camions, tracteurs routiers, camionnettes, véhicules automobiles tous terrains (p.ex. jeeps), etc., neufs ou usagés",
            Category.CLASS,
        ),
        Classification(
            "4519102",
            "Commerce de gros d'autobus, autocars, minibus, motorhomes, etc., neufs ou usagés",
            Category.CLASS,
        ),
        Classification(
            "45112",
            "Intermédiaires du commerce en automobiles et autres véhicules automobiles légers( = 3,5 tonnes )",
            Category.CLASS,
        ),
        Classification(
            "45192", "Intermédiaires du commerce en autres véhicules automobiles ( > 3,5 tonnes )", Category.CLASS
        ),
        Classification(
            "4511201",
            "Intermédiaires du commerce en véhicules automobiles pour le transport des personnes, y compris les véhicules automobiles spéciaux (p.ex. ambulances), neufs ou usagés",
            Category.CLASS,
        ),
        Classification(
            "4519201",
            "Intermédiaires du commerce en camions, tracteurs routiers, camionnettes, véhicules automobiles tous terrains (p.ex. jeeps), etc, neufs ou usagés",
            Category.CLASS,
        ),
        Classification(
            "4519202",
            "Intermédiaires du commerce en autobus, autocars, minibus, motorhomes, etc., neufs ou usagés",
            Category.CLASS,
        ),
        Classification(
            "45113",
            "Commerce de détail d'automobiles et d'autres véhicules automobiles légers ( = 3,5 tonnes )",
            Category.CLASS,
        ),
        Classification("45193", "Commerce de détail d'autres véhicules automobiles ( > 3,5 tonnes )", Category.CLASS),
        Classification(
            "4511301",
            "Commerce de détail de véhicules automobiles pour le transport des personnes, y compris les véhicules automobiles spéciaux (p.ex. ambulances), neufs ou usagés",
            Category.CLASS,
        ),
        Classification(
            "4519301",
            "Commerce de détail de camions, tracteurs routiers, camionnettes, véhicules automobiles tous terrains (p.ex. jeeps), etc., neufs ou usagés",
            Category.CLASS,
        ),
        Classification(
            "4519302",
            "Commerce de détail d'autobus, autocars, minibus, motorhomes, etc., neufs ou usagés",
            Category.CLASS,
        ),
        Classification("45194", "Commerce de remorques, de semi-remorques et de caravanes", Category.CLASS),
        Classification("4519401", "Commerce de remorques et semi-remorques neuves ou usagés", Category.CLASS),
        Classification(
            "4519402",
            "Commerce de véhicules neufs ou usagés pour le camping tels que caravanes, camping cars, etc.",
            Category.CLASS,
        ),
        Classification(
            "45201",
            "Entretien et réparation général d'automobiles et d'autres véhicules automobiles légers ( = 3,5 tonnes )",
            Category.CLASS,
        ),
        Classification(
            "45202", "Entretien et réparation général d'autres véhicules automobiles ( > 3,5 tonnes )", Category.CLASS
        ),
        Classification("45203", "Réparation de parties spécifiques de véhicules automobiles", Category.CLASS),
        Classification("45204", "Réparations de carrosseries", Category.CLASS),
        Classification("45205", "Services spécialisés relatifs au pneu", Category.CLASS),
        Classification("45206", "Lavage de véhicules automobiles", Category.CLASS),
        Classification("45209", "Entretien et réparation de véhicules automobiles n.c.a.", Category.CLASS),
        Classification(
            "4520301",
            "Réparation de véhicules automobiles: réparation de parties mécaniques, réparation électrique",
            Category.CLASS,
        ),
        Classification("4520302", "Révision du moteur des véhicules automobiles", Category.CLASS),
        Classification(
            "4520101",
            "Entretien et réparation général de voitures et de véhicules légers (≤ 3,5 tonnes)",
            Category.CLASS,
        ),
        Classification(
            "4520901", "Montage de pièces et d'accessoires, y compris les travaux de transformation", Category.CLASS
        ),
        Classification("5221011", "Remorquage et le dépannage routier", Category.CLASS),
        Classification(
            "45310",
            "Intermédiaires du commerce et commerce de gros d'équipements de véhicules automobiles",
            Category.CLASS,
        ),
        Classification(
            "4531001",
            "Commerce de gros d'accessoires, de pièces détachées et d'équipements divers pour véhicules automobiles, y compris la vente de gros de pièces détachées et d'équipements automobiles d'occasion",
            Category.CLASS,
        ),
        Classification("4531002", "Commerce de gros de pneumatiques", Category.CLASS),
        Classification("45320", "Commerce de détail d'équipements de véhicules automobiles", Category.CLASS),
        Classification(
            "4532001",
            "Commerce de détail d'accessoires, de pièces détachées et d'équipements divers pour véhicules automobiles, y compris la vente de détail de pièces détachées et d'équipements automobiles d'occasion",
            Category.CLASS,
        ),
        Classification("4532002", "Commerce de détail de pneumatiques", Category.CLASS),
        Classification(
            "4532003",
            "Commerce de détail spécialisé dans la vente d'équipements automobiles sur catalogue",
            Category.CLASS,
        ),
        Classification(
            "45402",
            "Entretien, réparation et commerce de détail de motocycles, y compris les pièces et accessoires",
            Category.CLASS,
        ),
        Classification(
            "45401",
            "Intermédiaires du commerce et commerce de gros de motocycles, y compris les pièces et accessoires",
            Category.CLASS,
        ),
        Classification(
            "4540101",
            "Intermédiation de commerce de motocycles, neufs ou usagés, y compris les cyclomoteurs",
            Category.CLASS,
        ),
        Classification("4540102", "Commerce de gros de motocycles, neufs ou usagés", Category.CLASS),
        Classification("4540103", "Commerce de gros de cyclomoteurs, neufs ou usagés", Category.CLASS),
        Classification("4540104", "Commerce de gros de pièces et d'accessoires de motocycles", Category.CLASS),
        Classification("4540201", "Commerce de détail de motocycles, neufs ou usagés", Category.CLASS),
        Classification("4540202", "Commerce de détail de cyclomoteurs, neufs ou usagés", Category.CLASS),
        Classification("4540203", "Commerce de détail de pièces et d'accessoires de motocycles", Category.CLASS),
        Classification("4540204", "Entretien et réparation de motocycles", Category.CLASS),
        Classification("4540205", "Entretien et réparation de cyclomoteurs", Category.CLASS),
        Classification("47300", "Commerce de détail de carburants automobiles en magasin spécialisé", Category.CLASS),
        Classification(
            "4730001",
            "Commerce de détail de carburants (y compris le GPL) pour véhicules automobiles et motocycles",
            Category.CLASS,
        ),
        Classification(
            "4730002",
            "Commerce de détail de lubrifiants et de produits de refroidissement pour véhicules automobiles",
            Category.CLASS,
        ),
        Classification(
            "46110",
            "Intermédiaires du commerce en matières premières agricoles, animaux vivants, matières premières textiles et produits semi-finis",
            Category.CLASS,
        ),
        Classification(
            "4611001",
            "Intermédiaires du commerce en matières premières agricoles, animaux vivants, matières premières textiles et produits semi-finis",
            Category.CLASS,
        ),
        Classification(
            "46120",
            "Intermédiaires du commerce en combustibles, métaux, minéraux et produits chimiques",
            Category.CLASS,
        ),
        Classification(
            "4612001",
            "Intermédiaires du commerce en combustibles, minéraux, métaux et produits chimiques",
            Category.CLASS,
        ),
        Classification(
            "4612002",
            "Intermédiaires du commerce en engrais, produits phytosanitaires et produits chimiques à usage agricole",
            Category.CLASS,
        ),
        Classification("46130", "Intermédiaires du commerce en bois et matériaux de construction", Category.CLASS),
        Classification("4613001", "Intermédiaires du commerce en bois et matériaux de construction", Category.CLASS),
        Classification("4613002", "Intermédiaires du commerce en peintures et vernis", Category.CLASS),
        Classification("4613003", "Intermédiaires du commerce en articles sanitaires", Category.CLASS),
        Classification(
            "46140",
            "Intermédiaires du commerce en machines, équipements industriels, navires et avions",
            Category.CLASS,
        ),
        Classification(
            "4614001",
            "Intermédiaires du commerce en machines, équipements industriels, navires et avions",
            Category.CLASS,
        ),
        Classification("4614002", "Intermédiaires du commerce en machines pour la construction", Category.CLASS),
        Classification(
            "4614003",
            "Intermédiaires du commerce en machines à coudre et machines et métiers à bonneterie",
            Category.CLASS,
        ),
        Classification(
            "4614004", "Intermédiaires du commerce en machines, tracteurs et matériel agricoles", Category.CLASS
        ),
        Classification(
            "4614005",
            "Intermédiaires du commerce en matériel électrique et électronique, y compris le matériel d'installation à usage industriel",
            Category.CLASS,
        ),
        Classification(
            "4614006",
            "Intermédiaires du commerce en machines et équipements utilisés dans le secteur de services",
            Category.CLASS,
        ),
        Classification(
            "46150", "Intermédiaires du commerce en meubles, articles de ménage et quincaillerie", Category.CLASS
        ),
        Classification(
            "4615001", "Intermédiaires du commerce en meubles, articles de ménage et quincaillerie", Category.CLASS
        ),
        Classification(
            "4615002",
            "Intermédiaires du commerce en appareils audio-vidéo, matériel photographique et cinématographique et articles d'optique",
            Category.CLASS,
        ),
        Classification(
            "4615003",
            "Intermédiaires du commerce en fournitures pour plomberie, matériels d'installation électrique à usage domestique et installations de chauffage",
            Category.CLASS,
        ),
        Classification(
            "4615004",
            "Intermédiaires du commerce en articles en porcelaine, verrerie, papiers peints et revêtements de sol",
            Category.CLASS,
        ),
        Classification(
            "4615005",
            "Intermédiaires du commerce en parfums, cosmétiques, articles de toilette et produits de nettoyage",
            Category.CLASS,
        ),
        Classification(
            "4615006",
            "Intermédiaires du commerce en produits pharmaceutiques et articles orthopédiques",
            Category.CLASS,
        ),
        Classification(
            "4615007",
            "Intermédiaires du commerce en articles de papeterie, journaux, livres et magazines",
            Category.CLASS,
        ),
        Classification(
            "4615008", "Intermédiaires du commerce en montres, articles en métaux précieux et bijoux", Category.CLASS
        ),
        Classification(
            "4615009",
            "Intermédiaires du commerce en articles de sport et matériel de camping, jeux et jouets",
            Category.CLASS,
        ),
        Classification(
            "46160",
            "Intermédiaires du commerce en textiles, habillement, fourrures, chaussures et articles en cuir",
            Category.CLASS,
        ),
        Classification(
            "4616001",
            "Intermédiaires du commerce en textiles, habillement, chaussures et articles en cuir",
            Category.CLASS,
        ),
        Classification("4616002", "Intermédiaires du commerce en fourrures", Category.CLASS),
        Classification("46170", "Intermédiaires du commerce en denrées, boissons et tabac", Category.CLASS),
        Classification("4617001", "Intermédiaires du commerce en denrées alimentaires et en tabac", Category.CLASS),
        Classification(
            "46180", "Intermédiaires spécialisés dans le commerce d'autres produits spécifiques", Category.CLASS
        ),
        Classification("4618001", "Autres intermédiaires spécialisés du commerce n.d.a.", Category.CLASS),
        Classification("46190", "Intermédiaires du commerce en produits divers", Category.CLASS),
        Classification("4619001", "Intermédiaires du commerce en produits divers", Category.CLASS),
        Classification(
            "46216",
            "Commerce de gros d'aliments pour le bétail et de produits agricoles, assortiment général",
            Category.CLASS,
        ),
        Classification("46211", "Commerce de gros de céréales et de semences", Category.CLASS),
        Classification("46212", "Commerce de gros d'aliments pour le bétail", Category.CLASS),
        Classification(
            "46213", "Commerce de gros d'huiles et de graisses brutes d'origine végétale ou animale", Category.CLASS
        ),
        Classification("46214", "Commerce de gros d'autres produits agricoles", Category.CLASS),
        Classification("4621101", "Commerce de gros de céréales et semences", Category.CLASS),
        Classification("4621301", "Commerce de gros d'huiles et de graisses non comestibles", Category.CLASS),
        Classification("4621102", "Commerce de gros de pommes de terre de semence", Category.CLASS),
        Classification("4622001", "Commerce de gros de bulbes de tulipes", Category.CLASS),
        Classification("46220", "Commerce de gros de fleurs et de plantes", Category.CLASS),
        Classification("46231", "Commerce de gros de bétail", Category.CLASS),
        Classification("46232", "Commerce de gros d'animaux vivants, sauf bétail", Category.CLASS),
        Classification("46240", "Commerce de gros de cuirs et de peaux", Category.CLASS),
        Classification("46215", "Commerce de gros de tabac non manufacturé", Category.CLASS),
        Classification(
            "46319", "Commerce de gros de fruits et de légumes, sauf pommes de terre de consommation", Category.CLASS
        ),
        Classification("46311", "Commerce de gros de pommes de terre de consommation", Category.CLASS),
        Classification(
            "4631901",
            "Commerce de gros de fruits et de légumes frais et en l'état, y compris les pommes de terre",
            Category.CLASS,
        ),
        Classification(
            "46321",
            "Commerce de gros de viandes et de produits à base de viande, sauf viande de volaille et de gibier",
            Category.CLASS,
        ),
        Classification(
            "4632101",
            "Commerce de gros de viande et de produits à base de viande, à l'exclusion de viande de volailles et de gibiers",
            Category.CLASS,
        ),
        Classification("46322", "Commerce de gros de viande de volaille et de gibier", Category.CLASS),
        Classification("4632102", "Commerce de gros de viande de lapins", Category.CLASS),
        Classification("46331", "Commerce de gros de produits laitiers et d'oeufs", Category.CLASS),
        Classification(
            "4633101", "Commerce de gros de produits laitiers (lait, beurre, fromage, etc.)", Category.CLASS
        ),
        Classification("4633102", "Commerce de gros d'oeufs et de produits à base d'oeufs", Category.CLASS),
        Classification("46332", "Commerce de gros d'huiles et de matières grasses comestibles", Category.CLASS),
        Classification(
            "4633201",
            "Commerce de gros d'huiles et de graisses comestibles d'origine animale et végétale",
            Category.CLASS,
        ),
        Classification("46349", "Commerce de gros de boissons, assortiment général", Category.CLASS),
        Classification("4634901", "Commerce de gros de toutes boissons, alcoolisées ou non", Category.CLASS),
        Classification("4634101", "Mise en bouteilles pour compte propre de vins achetés en vrac", Category.CLASS),
        Classification("46350", "Commerce de gros de produits à base de tabac", Category.CLASS),
        Classification("46360", "Commerce de gros de sucre, de chocolat et de confiserie", Category.CLASS),
        Classification("46370", "Commerce de gros de café, de thé, de cacao et d'épices", Category.CLASS),
        Classification("46381", "Commerce de gros de poissons, crustacés et mollusques", Category.CLASS),
        Classification("46382", "Commerce de gros de produits à base de pommes de terre", Category.CLASS),
        Classification("46383", "Commerce de gros d'aliments pour animaux de compagnie", Category.CLASS),
        Classification("4638301", "Commerce de gros d'aliments pour animaux domestiques", Category.CLASS),
        Classification("46389", "Commerce de gros d'autres produits alimentaires n.c.a.", Category.CLASS),
        Classification("4638901", "Commerce de gros de farines et produits pour la boulangerie", Category.CLASS),
        Classification("4638902", "Commerce de plats cuisinés frais et prêts à emporter", Category.CLASS),
        Classification("4638903", "Commerce de gros de conserves", Category.CLASS),
        Classification("4638904", "Commerce de gros de confitures et de miel", Category.CLASS),
        Classification("4638905", "Commerce de gros de pâtes alimentaires et de riz", Category.CLASS),
        Classification("4638906", "Commerce de gros de desserts", Category.CLASS),
        Classification("4638907", "Autres commerces de gros alimentaires spécialisés n.d.a.", Category.CLASS),
        Classification("46391", "Commerce de gros non spécialisé de denrées surgelées", Category.CLASS),
        Classification(
            "4639101",
            "Commerce de gros d'une gamme de pdts alimentaires surgelés: viandes et charcuteries, volailles et gibiers, poissons et crustacés, fruits et légumes, plats cuisinés, desserts, glaces de consomm., etc.",
            Category.CLASS,
        ),
        Classification(
            "46392", "Commerce de gros non spécialisé de denrées non-surgelées, boissons et tabac", Category.CLASS
        ),
        Classification("4639201", "Autres commerces de gros non spécialisés de produits alimentaires", Category.CLASS),
        Classification("46412", "Commerce de gros de linge de maison et de literie", Category.CLASS),
        Classification("46411", "Commerce de gros de tissus, d'étoffes et d'articles de mercerie", Category.CLASS),
        Classification("46419", "Commerce de gros d'autres textiles", Category.CLASS),
        Classification("4641101", "Commerce de gros de fils", Category.CLASS),
        Classification("4641102", "Commerce de gros de tissus et d'étoffes", Category.CLASS),
        Classification("4641201", "Commerce de gros de linge de maison et de literie", Category.CLASS),
        Classification("4641901", "Commerce de gros de bâches, housses, parasols, stores, etc.", Category.CLASS),
        Classification(
            "4641103", "Commerce de gros d'articles de mercerie: aiguilles, fils, rubans, etc.", Category.CLASS
        ),
        Classification(
            "46423", "Commerce de gros de vêtements, autres que vêtements de travail et sous-vêtements", Category.CLASS
        ),
        Classification("46421", "Commerce de gros de vêtements de travail", Category.CLASS),
        Classification("46422", "Commerce de gros de sous-vêtements", Category.CLASS),
        Classification("46424", "Commerce de gros d'accessoires du vêtement", Category.CLASS),
        Classification(
            "4642301", "Commerce de gros d'articles d'habillement, y compris les vêtements de sport", Category.CLASS
        ),
        Classification("4642302", "Commerce de gros d'articles en fourrure", Category.CLASS),
        Classification("46425", "Commerce de gros de chaussures", Category.CLASS),
        Classification("4642501", "Commerce de gros de chaussures", Category.CLASS),
        Classification("46431", "Commerce de gros d'appareils électroménagers et audio-vidéo", Category.CLASS),
        Classification("46432", "Commerce de gros de supports enregistrés d'images et de sons", Category.CLASS),
        Classification("46473", "Commerce de gros d'appareils d'éclairage", Category.CLASS),
        Classification(
            "46520",
            "Commerce de gros de composants et d'équipements électroniques et de télécommunication",
            Category.CLASS,
        ),
        Classification("4643101", "Commerce de gros d'appareils électroménagers", Category.CLASS),
        Classification(
            "4643102",
            "Commerce de gros d'appareils audio et vidéo: radio, télévision, chaînes, magnétoscopes, etc.",
            Category.CLASS,
        ),
        Classification(
            "4643201",
            "Commerce de gros de disques, de disques compacts, d'audiocassettes et de vidéocassettes enregistrés",
            Category.CLASS,
        ),
        Classification(
            "4643103", "Commerce de gros de matériels électriques d'installation à usage domestique", Category.CLASS
        ),
        Classification("46494", "Commerce de gros d'articles ménagers non électriques", Category.CLASS),
        Classification("46441", "Commerce de gros de porcelaine et de verrerie", Category.CLASS),
        Classification("4644101", "Commerce de gros de vaisselle et de verrerie de ménage", Category.CLASS),
        Classification(
            "4649401", "Commerce de gros de couverts et d'articles métalliques de table et de cuisine", Category.CLASS
        ),
        Classification("46442", "Commerce de gros de produits d'entretien", Category.CLASS),
        Classification(
            "46733", "Commerce de gros de papiers peints, de peintures et de tissus d'ameublement", Category.CLASS
        ),
        Classification("4673301", "Commerce de gros de papier peints et de revêtements muraux", Category.CLASS),
        Classification(
            "4644201",
            "Commerce de gros de produits d'entretien et de nettoyage, y compris les poudres de lessive",
            Category.CLASS,
        ),
        Classification("46450", "Commerce de gros de parfumerie et de produits de beauté", Category.CLASS),
        Classification("4645001", "Commerce de gros de produits d'hygiène", Category.CLASS),
        Classification("46460", "Commerce de gros de produits pharmaceutiques", Category.CLASS),
        Classification(
            "4646001", "Commerce de gros de matériel médico-chirurgical et de fournitures dentaires", Category.CLASS
        ),
        Classification("4646002", "Commerce de gros d'articles d'orthopédie", Category.CLASS),
        Classification("46471", "Commerce de gros de mobilier domestique", Category.CLASS),
        Classification("46472", "Commerce de gros de tapis", Category.CLASS),
        Classification("4649411", "Commerce de gros d'appareils ménagers non-électriques", Category.CLASS),
        Classification("46491", "Commerce de gros de journaux, de livres et de périodiques", Category.CLASS),
        Classification(
            "46433",
            "Commerce de gros d'appareils photographiques et cinématographiques et d'autres articles d'optique",
            Category.CLASS,
        ),
        Classification("46480", "Commerce de gros d'articles d'horlogerie et de bijouterie", Category.CLASS),
        Classification("46492", "Commerce de gros de fournitures scolaires et de bureau", Category.CLASS),
        Classification("46493", "Commerce de gros d'articles en papier ou en carton", Category.CLASS),
        Classification(
            "4649201",
            "Commerce de gros d'articles de papeterie, de fournitures de bureau et de fournitures scolaires",
            Category.CLASS,
        ),
        Classification("46496", "Commerce de gros d'articles de sport et de camping, sauf cycles", Category.CLASS),
        Classification("46495", "Commerce de gros de cycles", Category.CLASS),
        Classification("46497", "Commerce de gros de jeux et de jouets", Category.CLASS),
        Classification("4649601", "Commerce de gros d'articles de sport et de camping", Category.CLASS),
        Classification("46498", "Commerce de gros de maroquinerie et d'articles de voyage", Category.CLASS),
        Classification("4649801", "Commerce de gros de maroquinerie et d'articles de voyage", Category.CLASS),
        Classification("46499", "Commerce de gros d'autres biens domestiques n.c.a.", Category.CLASS),
        Classification("4649901", "Commerce de gros d'instruments de musique", Category.CLASS),
        Classification("4649902", "Commerce de gros d'ouvrages en bois, en osier ou en liège", Category.CLASS),
        Classification("4649903", "Autres commerces de gros d'articles de consommation n.d.a.", Category.CLASS),
        Classification(
            "46710",
            "Commerce de gros de combustibles solides, liquides et gazeux et de produits annexes",
            Category.CLASS,
        ),
        Classification("4671001", "Commerce de gros de combustibles solides, liquides et gazeux", Category.CLASS),
        Classification(
            "4671002", "Commerce de gros de carburants, graisses, lubrifiants, huiles, etc.", Category.CLASS
        ),
        Classification("46720", "Commerce de gros de minerais et de métaux", Category.CLASS),
        Classification("4672001", "Commerce de gros de minerais métalliques ferreux et non ferreux", Category.CLASS),
        Classification(
            "4672002",
            "Commerce de gros de métaux ferreux et non ferreux sous formes primaires, y compris l'or et les autres métaux précieux",
            Category.CLASS,
        ),
        Classification("4672003", "Commerce de gros de demi-produits en métaux ferreux et non ferreux", Category.CLASS),
        Classification("46732", "Commerce de gros de bois", Category.CLASS),
        Classification("46731", "Commerce de gros de matériaux de construction, assortiment général", Category.CLASS),
        Classification("4673201", "Commerce de gros de bois brut", Category.CLASS),
        Classification("4673202", "Commerce de gros de produits de la transformation primaire du bois", Category.CLASS),
        Classification("4673203", "Commerce de gros de panneaux, parquets, lambris, etc.", Category.CLASS),
        Classification("4673204", "Commerce de gros de menuiseries et fermetures de bâtiment en bois", Category.CLASS),
        Classification("46734", "Commerce de gros de verre plat", Category.CLASS),
        Classification("46735", "Commerce de gros de carrelages", Category.CLASS),
        Classification("46736", "Commerce de gros d'équipements sanitaires", Category.CLASS),
        Classification("46739", "Commerce de gros d'autres matériaux de construction", Category.CLASS),
        Classification("4673311", "Commerce de gros de peintures et de vernis", Category.CLASS),
        Classification(
            "4673101",
            "Commerce de gros de matériaux de construction: sable, gravier, ciment, briques, etc.",
            Category.CLASS,
        ),
        Classification("4673401", "Commerce de gros de verre plat", Category.CLASS),
        Classification(
            "4673601",
            "Commerce de gros d'appareils sanitaires: baignoires, lavabos, cuvettes d'aisance, etc.",
            Category.CLASS,
        ),
        Classification(
            "4673102", "Commerce de gros de menuiseries et fermetures de bâtiment autres qu'en bois", Category.CLASS
        ),
        Classification("46741", "Commerce de gros de quincaillerie", Category.CLASS),
        Classification(
            "4674101",
            "Commerce de gros de quincaillerie générale (clous, fils, visserie, boulonnerie, etc.), d'outils à main (marteaux, scies, tournevis, etc.) et d'outillage électroportatif",
            Category.CLASS,
        ),
        Classification(
            "4674102",
            "Commerce de gros de quincaillerie d'ameublement et de bâtiment: serrures, clés, charnières, etc.",
            Category.CLASS,
        ),
        Classification("4674103", "Commerce de gros d'ustensiles de ménage métalliques", Category.CLASS),
        Classification("46742", "Commerce de gros de fournitures pour plomberie et chauffage", Category.CLASS),
        Classification("4674201", "Commerce de gros d'appareils de chauffage central", Category.CLASS),
        Classification(
            "4674202",
            "Commerce de gros de fournitures pour installations sanitaires et chauffage central: tubes, tuyaux, raccords de tuyauterie, robinets, tuyaux en caoutchouc, etc.",
            Category.CLASS,
        ),
        Classification("46751", "Commerce de gros de produits chimiques industriels", Category.CLASS),
        Classification("46752", "Commerce de gros d'engrais et de produits phytosanitaires", Category.CLASS),
        Classification("46769", "Commerce de gros d'autres produits intermédiaires n.c.a.", Category.CLASS),
        Classification(
            "4675101",
            "Commerce de gros de produits chimiques industriels: aniline, encres d'imprimerie, huiles essentielles, gaz industriels, colles chimiques, colorants, résine synthétiques, méthanol, paraffine, etc.",
            Category.CLASS,
        ),
        Classification(
            "4675201", "Commerce de gros d'engrais et de produits phytosanitaires à usage agricole", Category.CLASS
        ),
        Classification("4676911", "Commerce de gros de matières plastiques sous formes primaires", Category.CLASS),
        Classification("4676912", "Commerce de gros caoutchouc brut", Category.CLASS),
        Classification("4675102", "Commerce de gros de produits de nettoyage à usage industriel", Category.CLASS),
        Classification("46761", "Commerce de gros de diamants et d'autres pierres précieuses", Category.CLASS),
        Classification("4676101", "Commerce de gros de diamants bruts et de diamants façonnés", Category.CLASS),
        Classification("4676102", "Commerce de gros d'autres pierres précieuses et semi-précieuses", Category.CLASS),
        Classification(
            "4676901", "Commerce de gros de matières premières textiles et de fibres textiles", Category.CLASS
        ),
        Classification(
            "4676902",
            "Commerce de gros de papiers et cartons destinés à faire l'objet d'une transformation ultérieure par l'industrie",
            Category.CLASS,
        ),
        Classification("4676903", "Commerce de gros d'autres produits intermédiaires n.d.a.", Category.CLASS),
        Classification(
            "46772", "Commerce de gros de déchets et de débris métalliques et non-métalliques", Category.CLASS
        ),
        Classification(
            "46771", "Commerce de gros d'épaves de véhicules automobiles et de pièces réutilisables", Category.CLASS
        ),
        Classification("46779", "Commerce de gros de déchets et débris n.c.a.", Category.CLASS),
        Classification(
            "4677201",
            "Commerce de gros de déchets, de débris et de matériaux de récupération, métalliques et non métalliques",
            Category.CLASS,
        ),
        Classification("46620", "Commerce de gros de machines-outils", Category.CLASS),
        Classification(
            "46630", "Commerce de gros de machines pour l'extraction, la construction et le génie civil", Category.CLASS
        ),
        Classification(
            "46640", "Commerce de gros de machines pour l'industrie textile et l'habillement", Category.CLASS
        ),
        Classification(
            "46510",
            "Commerce de gros d'ordinateurs, d'équipements informatiques périphériques et de logiciels",
            Category.CLASS,
        ),
        Classification("46660", "Commerce de gros d'autres machines et équipements de bureau", Category.CLASS),
        Classification("46650", "Commerce de gros de mobilier de bureau", Category.CLASS),
        Classification(
            "46693", "Commerce de gros de matériel électrique, y compris le matériel d'installation", Category.CLASS
        ),
        Classification("46699", "Commerce de gros d'autres machines et équipements n.c.a.", Category.CLASS),
        Classification("46694", "Commerce de gros de matériel de levage et de manutention", Category.CLASS),
        Classification(
            "46696", "Commerce de gros d'instruments de mesure, de contrôle et de navigation", Category.CLASS
        ),
        Classification("46610", "Commerce de gros de matériel agricole", Category.CLASS),
        Classification("46900", "Commerce de gros non spécialisé", Category.CLASS),
        Classification(
            "46691",
            "Commerce de gros de machines pour la production d'aliments, de boissons et de tabac",
            Category.CLASS,
        ),
        Classification("46692", "Commerce de gros de machines d'emballage et d'appareils de pesage", Category.CLASS),
        Classification("46695", "Commerce de gros de pompes et de compresseurs", Category.CLASS),
        Classification(
            "46697",
            "Commerce de gros de machines et d'appareils de chauffage et de refroidissement à usage industriel",
            Category.CLASS,
        ),
        Classification("47111", "Commerce de détail en magasin non spécialisé de produits surgelés", Category.CLASS),
        Classification(
            "4711101",
            "Commerce de détail en magasin ou par livraison à domicile de tous produits alimentaires surgelés ou congelés, y compris les crèmes glacées",
            Category.CLASS,
        ),
        Classification(
            "47112",
            "Commerce de détail en magasin non spécialisé à prédominance alimentaire (surface de vente < 100m²)",
            Category.CLASS,
        ),
        Classification(
            "4711201",
            "Commerce de détail non spécialisé d'alimentation générale (surface de vente inférieure à 100 m2)",
            Category.CLASS,
        ),
        Classification(
            "47113",
            "Commerce de détail en magasin non spécialisé à prédominance alimentaire (surface de vente comprise entre 100m² et moins de 400m²)",
            Category.CLASS,
        ),
        Classification("4711301", "Superettes (surface de vente comprise entre 100 et 400 m2)", Category.CLASS),
        Classification(
            "47114",
            "Commerce de détail en magasin non spécialisé à prédominance alimentaire (surface de vente comprise entre 400m² et moins de 2500m²)",
            Category.CLASS,
        ),
        Classification("4711401", "Supermarchés (surface de vente comprise entre 400 et 2500 m2)", Category.CLASS),
        Classification(
            "47115",
            "Commerce de détail en magasin non spécialisé à prédominance alimentaire (surface de vente > ou = 2500m²)",
            Category.CLASS,
        ),
        Classification(
            "4711211",
            "Autres commerces de détail en magasins non spécialisés à prédominance alimentaire",
            Category.CLASS,
        ),
        Classification(
            "47192",
            "Commerce de détail en magasin non spécialisé sans prédominance alimentaire (surface de vente  > ou = 2500m²)",
            Category.CLASS,
        ),
        Classification(
            "4719201",
            "Grand magasin: commerce de détail d'une large gamme de pdts sans prédominance de l'alimentation, boissons et tabac tels habillement, meubles, petits app., quincaillerie, cosmétiques, joaillerie, etc.",
            Category.CLASS,
        ),
        Classification(
            "47191",
            "Commerce de détail en magasin non spécialisé sans prédominance alimentaire (surface de vente < 2500m²)",
            Category.CLASS,
        ),
        Classification(
            "4719101",
            "Commerce de détail d'une large gamme de pdts sans prédominance de l'alimentation, boissons et tabac tels habillement, meubles, petits appareils, quincaillerie, cosmétique, joaillerie, jouets, etc.",
            Category.CLASS,
        ),
        Classification("47210", "Commerce de détail de fruits et de légumes en magasin spécialisé", Category.CLASS),
        Classification(
            "4721001", "Commerce de détail de fruits et légumes frais, y compris les pommes de terre", Category.CLASS
        ),
        Classification(
            "47221",
            "Commerce de détail de viandes et de produits à base de viande en magasin spécialisé, sauf viande de gibier et de volaille",
            Category.CLASS,
        ),
        Classification(
            "47222", "Commerce de détail de viande de gibier et de volaille en magasin spécialisé", Category.CLASS
        ),
        Classification(
            "4722101",
            "Commerce de détail de viandes et produits à base de viande exploité par les bouchers/charcutiers",
            Category.CLASS,
        ),
        Classification(
            "47230", "Commerce de détail de poissons, crustacés et mollusques en magasin spécialisé", Category.CLASS
        ),
        Classification("4723001", "Commerce de détail de poissons, crustacés et mollusques", Category.CLASS),
        Classification(
            "47241", "Commerce de détail de pain et de pâtisserie en magasin spécialisé (dépôt)", Category.CLASS
        ),
        Classification(
            "47242", "Commerce de détail de chocolat et de confiserie en magasin spécialisé", Category.CLASS
        ),
        Classification("4724101", "Commerce de détail de pain et de pâtisserie", Category.CLASS),
        Classification(
            "47252", "Commerce de détail de boissons en magasin spécialisé, assortiment général", Category.CLASS
        ),
        Classification("47251", "Commerce de détail de vins et de spiritueux en magasin spécialisé", Category.CLASS),
        Classification(
            "4725201",
            "Commerce de détail de toutes boissons,alcoolisées ou non, y compris la livraison à domicile",
            Category.CLASS,
        ),
        Classification(
            "4725202", "Mise en bouteilles, mélange et épuration du vin sans transformation", Category.CLASS
        ),
        Classification("47260", "Commerce de détail de produits à base de tabac en magasin spécialisé", Category.CLASS),
        Classification("4726001", "Commerce de détail de tabac", Category.CLASS),
        Classification(
            "47291", "Commerce de détail de produits laitiers et d'oeufs en magasin spécialisé", Category.CLASS
        ),
        Classification(
            "4729101",
            "Commerce de détail de produits laitiers et oeufs, y compris la livraison à domicile",
            Category.CLASS,
        ),
        Classification("47299", "Autres commerces de détail alimentaires en magasin spécialisé n.c.a.", Category.CLASS),
        Classification("4729901", "Commerce de détail de café", Category.CLASS),
        Classification("4729902", "Commerce de détail de condiments et épices", Category.CLASS),
        Classification("4721011", "Commerce de détail de conserves de fruits et légumes", Category.CLASS),
        Classification(
            "4729903", "Autres commerces de détail alimentaires en magasins spécialisés n.d.a.", Category.CLASS
        ),
        Classification("47730", "Commerce de détail de produits pharmaceutiques en magasin spécialisé", Category.CLASS),
        Classification("4773001", "Pharmacies", Category.CLASS),
        Classification(
            "47740", "Commerce de détail d'articles médicaux et orthopédiques en magasin spécialisé", Category.CLASS
        ),
        Classification("4774001", "Commerce de détail d'articles médicaux et orthopédiques", Category.CLASS),
        Classification("4774002", "Commerce de détail d'herboristerie", Category.CLASS),
        Classification("4774003", "Commerce de détail de prothèses et de véhicules pour invalides", Category.CLASS),
        Classification(
            "47750", "Commerce de détail de parfumerie et de produits de beauté en magasin spécialisé", Category.CLASS
        ),
        Classification("4775001", "Commerce de détail de parfumerie et de produits de beauté", Category.CLASS),
        Classification("4775002", "Commerce de détail d'articles de toilette", Category.CLASS),
        Classification("47512", "Commerce de détail de linge de maison en magasin spécialisé", Category.CLASS),
        Classification("47511", "Commerce de détail de tissus d'habillement en magasin spécialisé", Category.CLASS),
        Classification(
            "47513",
            "Commerce de détail de fils à tricoter et d'articles de mercerie en magasin spécialisé",
            Category.CLASS,
        ),
        Classification("47519", "Commerce de détail d'autres textiles en magasin spécialisé", Category.CLASS),
        Classification("4751201", "Commerce de détail de tissus d'habillement et d'ameublement", Category.CLASS),
        Classification("4751301", "Commerce de détail de fils à tricoter", Category.CLASS),
        Classification(
            "4751302",
            "Commerce de détail de matériaux de base pour la fabrication de tapis, de tapisseries ou de broderies",
            Category.CLASS,
        ),
        Classification(
            "4751303", "Commerce de détail d'articles de mercerie: aiguilles, fils à coudre, boutons", Category.CLASS
        ),
        Classification(
            "4751901", "Commerce de détail de bâches, housses, parasols, cabas, etc., en textile", Category.CLASS
        ),
        Classification(
            "4751202",
            "Commerce de détail de textiles à usage domestique tels que draps, couvertures, nappes, serviettes, etc.",
            Category.CLASS,
        ),
        Classification(
            "47716",
            "Commerce de détail de vêtements, de sous-vêtements et d'accessoires pour dame, homme, enfant et bébé en magasin spécialisé, assortiment général",
            Category.CLASS,
        ),
        Classification(
            "4771601",
            "Commerce de détail de vêtem. de dessus, y compris les vêtem. de travail, de sport et de cérémonie, en ttes mat. (tissus textiles, cuir, fourrure, etc.) pour homme, dame, enfant et bébé (assort. gén.)",
            Category.CLASS,
        ),
        Classification("47712", "Commerce de détail de vêtements pour homme en magasin spécialisé", Category.CLASS),
        Classification(
            "4771201",
            "Commerce de détail de vêtements de dessus, y compris les vêtements de travail, de sport et de cérémonie, en toutes matières (tissus textiles, étoffes de bonneterie, cuir, fourrure, etc.) pour homme",
            Category.CLASS,
        ),
        Classification("47711", "Commerce de détail de vêtements pour dame en magasin spécialisé", Category.CLASS),
        Classification(
            "4771101",
            "Commerce de détail de vêtements de dessus, y compris les vêtements de travail, de sport et de cérémonie, en toutes matières (tissus textiles, étoffes de bonneterie, cuir, fourrure, etc.) pour dames",
            Category.CLASS,
        ),
        Classification(
            "47713", "Commerce de détail de vêtements pour bébé et enfant en magasin spécialisé", Category.CLASS
        ),
        Classification("4771301", "Commerce de détail de vêtements pour bébés et enfants", Category.CLASS),
        Classification(
            "47714",
            "Commerce de détail de sous-vêtements, de lingerie et de vêtements de bain en magasin spécialisé",
            Category.CLASS,
        ),
        Classification(
            "4771401", "Commerce de détail de sous-vêtements, lingerie et de vêtements de bain", Category.CLASS
        ),
        Classification("47715", "Commerce de détail d'accessoires du vêtement en magasin spécialisé", Category.CLASS),
        Classification(
            "4771501", "Commerce de détail de chapeaux, gants, cravates, ceintures, parapluies, etc.", Category.CLASS
        ),
        Classification("47721", "Commerce de détail de chaussures en magasin spécialisé", Category.CLASS),
        Classification("4772101", "Commerce de détail de chaussures", Category.CLASS),
        Classification(
            "47722", "Commerce de détail de maroquinerie et d'articles de voyage en magasin spécialisé", Category.CLASS
        ),
        Classification(
            "4772201",
            "Commerce de détail de maroquinerie et d'accessoires de voyage en cuir ou en cuir synthétique",
            Category.CLASS,
        ),
        Classification("47591", "Commerce de détail de mobilier de maison en magasin spécialisé", Category.CLASS),
        Classification("4759101", "Commerce de détail de meubles", Category.CLASS),
        Classification("4759102", "Commerce de détail de cuisines équipées", Category.CLASS),
        Classification(
            "4759103", "Commerce de détail de matelas, sommiers et autres supports de matelas", Category.CLASS
        ),
        Classification("47592", "Commerce de détail d'appareils d'éclairage en magasin spécialisé", Category.CLASS),
        Classification(
            "47530",
            "Commerce de détail de tapis, de moquettes et de revêtements de murs et de sols en magasin spécialisé",
            Category.CLASS,
        ),
        Classification(
            "47593",
            "Commerce de détail d'appareils ménagers non électriques, de vaisselle, de verrerie, de porcelaine et de poterie en magasin spécialisé",
            Category.CLASS,
        ),
        Classification(
            "47599", "Commerce de détail d'autres articles de ménage en magasin spécialisé n.c.a.", Category.CLASS
        ),
        Classification("4759201", "Commerce de détail d'appareils d'éclairage", Category.CLASS),
        Classification(
            "4759301",
            "Commerce de détail d'appareils ménagers non électriques, de coutellerie, de vaisselle, de verrerie, de porcelaine et de poteries",
            Category.CLASS,
        ),
        Classification("4753011", "Commerce de détail de rideaux", Category.CLASS),
        Classification("4759901", "Commerce de détail d'ouvrages en bois, en liège et en vannerie", Category.CLASS),
        Classification(
            "4759902", "Commerce de détail spécialisé en cadeaux portant sur l'équipement du foyer", Category.CLASS
        ),
        Classification(
            "4759903",
            "Commerce de détail d'appareils et articles de ménage ou d'économie domestique n.d.a.",
            Category.CLASS,
        ),
        Classification("47540", "Commerce de détail d'appareils électroménagers en magasin spécialisé", Category.CLASS),
        Classification("47430", "Commerce de détail de matériels audio-vidéo en magasin spécialisé", Category.CLASS),
        Classification("47594", "Commerce de détail d'instruments de musique en magasin spécialisé", Category.CLASS),
        Classification(
            "47630", "Commerce de détail d'enregistrements musicaux et vidéo en magasin spécialisé", Category.CLASS
        ),
        Classification("4754001", "Commerce de détail d'appareils électroménagers", Category.CLASS),
        Classification(
            "4743001",
            "Commerce de détail d'appareils de radio et de télévision et d'autres matériels audio/vidéo à usage domestique tels les magnétoscopes, les caméscopes, le matériel hi-fi, etc.",
            Category.CLASS,
        ),
        Classification(
            "4763001",
            "Commerce de détail de disques, de disques compacts, bandes et cassettes audio ou vidéo, vierges ou enregistrées",
            Category.CLASS,
        ),
        Classification(
            "4759401", "Commerce de détail d'instruments de musique et de partitions musicales", Category.CLASS
        ),
        Classification(
            "47521",
            "Commerce de détail de matériaux de construction en magasin spécialisé, assortiment général",
            Category.CLASS,
        ),
        Classification(
            "47522",
            "Commerce de détail de matériaux de construction et de matériaux de jardin en bois en magasin spécialisé",
            Category.CLASS,
        ),
        Classification(
            "47523", "Commerce de détail de carrelages de sols et de murs en magasin spécialisé", Category.CLASS
        ),
        Classification(
            "47525", "Commerce de détail de quincaillerie et d'outils en magasin spécialisé", Category.CLASS
        ),
        Classification("47526", "Commerce de détail de peinture et de vernis en magasin spécialisé", Category.CLASS),
        Classification(
            "47527",
            "Commerce de détail d'articles et de matériels d'installations sanitaires en magasin spécialisé",
            Category.CLASS,
        ),
        Classification(
            "47529", "Commerce de détail d'autres matériaux de construction en magasin spécialisé", Category.CLASS
        ),
        Classification(
            "4752101",
            "Commerce de détail de quincaillerie, peintures et matériaux de construction (y compris les bricocenters) avec une surface de vente moins de 400 m2",
            Category.CLASS,
        ),
        Classification(
            "4752111",
            "Commerce de détail de quincaillerie, peintures et matériaux de construction (y compris les bricocenters) avec une surface de vente de plus de 400 m2",
            Category.CLASS,
        ),
        Classification("47620", "Commerce de détail de journaux et de papeterie en magasin spécialisé", Category.CLASS),
        Classification("47610", "Commerce de détail de livres en magasin spécialisé", Category.CLASS),
        Classification(
            "4762001", "Commerce de détail de livres, journaux et papeterie en magasin spécialisé", Category.CLASS
        ),
        Classification("4762002", "Commerce de détail de livres, journaux et périodiques en kiosque", Category.CLASS),
        Classification(
            "47781",
            "Commerce de détail de combustibles en magasin spécialisé, à l'exclusion des carburants automobiles",
            Category.CLASS,
        ),
        Classification(
            "4778101",
            "Commerce de détail de combustibles solides tels que charbon, bois de chauffage, charbon de bois, etc.",
            Category.CLASS,
        ),
        Classification("4778102", "Commerce de détail de combustibles liquides et gazeux", Category.CLASS),
        Classification("47640", "Commerce de détail d'articles de sport en magasin spécialisé", Category.CLASS),
        Classification(
            "4764001",
            "Commerce de détail d'articles de sport, de matériel de camping (y compris les tentes) et d'articles pour autres activités de loisir",
            Category.CLASS,
        ),
        Classification(
            "4764002", "Commerce de détail de bateaux de plaisance, planches à voile, voiles, etc.", Category.CLASS
        ),
        Classification(
            "47761",
            "Commerce de détail de fleurs, de plantes, de graines et d'engrais en magasin spécialisé",
            Category.CLASS,
        ),
        Classification(
            "4776101", "Commerce de détail de fleurs (y compris les fleurs coupées) et de plantes", Category.CLASS
        ),
        Classification(
            "4776102", "Commerce de détail de graines, d'engrais, de produits phytosanitaires, etc.", Category.CLASS
        ),
        Classification(
            "4776103",
            "Commerce de détail de fleurs artificielles et d'articles d'ornementation en fleurs artificielles",
            Category.CLASS,
        ),
        Classification(
            "4776104",
            "Commerce de détail spécialisé portant sur une large gamme d'articles de jardinage et de produits horticoles (centres de jardinage)",
            Category.CLASS,
        ),
        Classification(
            "47770", "Commerce de détail d'articles d'horlogerie et de bijouterie en magasin spécialisé", Category.CLASS
        ),
        Classification("4777001", "Commerce de détail de montres et autres articles d'horlogerie", Category.CLASS),
        Classification("4777002", "Commerce de détail d'articles de bijouterie et d'orfèvrerie", Category.CLASS),
        Classification(
            "47782",
            "Commerce de détail de matériel photographique, d'optique et de précision en magasin spécialisé",
            Category.CLASS,
        ),
        Classification(
            "4778201",
            "Commerce de détail d'articles d'optique (y compris les lunettes), de photographie (y compris les pellicules) et de précision",
            Category.CLASS,
        ),
        Classification(
            "47524",
            "Commerce de détail de parquet, de laminés et de revêtement en liège en magasin spécialisé",
            Category.CLASS,
        ),
        Classification("4753001", "Commerce de détail de tapis et moquettes", Category.CLASS),
        Classification(
            "4753002", "Commerce de détail de revêtements de sols en plastique, caoutchouc, liège, etc.", Category.CLASS
        ),
        Classification("4753003", "Commerce de détail de papier peints", Category.CLASS),
        Classification(
            "47410",
            "Commerce de détail d'ordinateurs, d'unités périphériques et de logiciels en magasin spécialisé",
            Category.CLASS,
        ),
        Classification(
            "47420", "Commerce de détail de matériels de télécommunication en magasin spécialisé", Category.CLASS
        ),
        Classification("4741001", "Commerce de détail d'ordinateurs et de logiciels non personnalisés", Category.CLASS),
        Classification("4741002", "Commerce de détail de matériel et mobilier de bureau", Category.CLASS),
        Classification(
            "47784",
            "Commerce de détail d'articles de droguerie et de produits d'entretien en magasin spécialisé",
            Category.CLASS,
        ),
        Classification(
            "4778401", "Commerce de détail d'articles de droguerie et de produits d'entretien", Category.CLASS
        ),
        Classification("4778402", "Commerce de détail de produits de nettoyage", Category.CLASS),
        Classification("47650", "Commerce de détail de jeux et de jouets en magasin spécialisé", Category.CLASS),
        Classification("4765001", "Commerce de détail de jeux et jouets", Category.CLASS),
        Classification("47783", "Commerce de détail d'armes et de munitions en magasin spécialisé", Category.CLASS),
        Classification(
            "4778301", "Commerce de détail d'armes et de munitions pour la chasse ou le tir au fusil", Category.CLASS
        ),
        Classification("4778302", "Commerce de détail d'armes défensives", Category.CLASS),
        Classification("47785", "Commerce de détail de cycles en magasin spécialisé", Category.CLASS),
        Classification("4778501", "Commerce de détail de cycles", Category.CLASS),
        Classification(
            "47788",
            "Commerce de détail d'articles de puériculture en magasin spécialisé, assortiment général",
            Category.CLASS,
        ),
        Classification("4778801", "Commerce de détail de voitures d'enfant", Category.CLASS),
        Classification(
            "4778802",
            "Commerce de détail de berceaux, de sièges de sécurité pour enfants et d'autres articles de puériculture",
            Category.CLASS,
        ),
        Classification("47789", "Autre commerce de détail de biens neufs en magasin spécialisé n.c.a.", Category.CLASS),
        Classification(
            "47762",
            "Commerce de détail d'animaux de compagnie, d'aliments et d'accessoires pour ces animaux en magasin spécialisé",
            Category.CLASS,
        ),
        Classification(
            "4776201", "Commerce de détail d'animaux de compagnie et de fournitures pour animaux", Category.CLASS
        ),
        Classification(
            "47786", "Commerce de détail de souvenirs et d'articles religieux en magasin spécialisé", Category.CLASS
        ),
        Classification(
            "4778601", "Commerce de détail de souvenirs, d'objets artisanaux et d'articles religieux", Category.CLASS
        ),
        Classification("4778602", "Commerce de détail de bijouterie fantaisie, de gadgets, etc.", Category.CLASS),
        Classification("47787", "Commerce de détail d'objets d'art neufs en magasin spécialisé", Category.CLASS),
        Classification(
            "4778701",
            "Commerce de détail d'art contemporain, de tableaux nouveaux, de reproductions, de cadres, etc.",
            Category.CLASS,
        ),
        Classification("4778901", "Commerce de détail de ficelles, de cordes et de cordages", Category.CLASS),
        Classification(
            "4778902", "Commerce de détail d'articles n.d.a. autres que produits alimentaires", Category.CLASS
        ),
        Classification("47791", "Commerce de détail d'antiquités en magasin", Category.CLASS),
        Classification("4779101", "Commerce de détail d'antiquités et objets d'art anciens", Category.CLASS),
        Classification("47792", "Commerce de détail de vêtements d'occasion en magasin", Category.CLASS),
        Classification(
            "47793", "Commerce de détail de biens d'occasion en magasin, sauf vêtements d'occasion", Category.CLASS
        ),
        Classification("4779301", "Commerce de détail de livres d'occasion", Category.CLASS),
        Classification(
            "4779302", "Commerce de détail d'autres biens d'occasion tels que meubles, matériaux de", Category.CLASS
        ),
        Classification(
            "4779303",
            "Commerce de détail de biens de récupération de toute nature, exercé dans des magasins qui appartiennent à des centres de récupération",
            Category.CLASS,
        ),
        Classification("47910", "Commerce de détail par correspondance ou par Internet", Category.CLASS),
        Classification(
            "4791001",
            "Commerce de détail de tous types de produits par correspondance. Les produits et articles sont expédiés à l'acheteur qui fait son choix au départ de publicités, catalogues spécialisés ou non, etc.",
            Category.CLASS,
        ),
        Classification(
            "4791002", "Vente direct par téléphone ou par le truchement de la radio ou de la télévision", Category.CLASS
        ),
        Classification("47810", "Commerce de détail alimentaire sur éventaires et marchés", Category.CLASS),
        Classification("4781001", "Commerce de détail alimentaire sur marchés et éventaires", Category.CLASS),
        Classification(
            "47820",
            "Commerce de détail de textiles, d'habillement et de chaussures sur éventaires et marchés",
            Category.CLASS,
        ),
        Classification(
            "4782001",
            "Commerce de détail d'habillement et d'articles textiles sur marchés et éventaires",
            Category.CLASS,
        ),
        Classification("47890", "Autres commerces de détail sur éventaires et marchés", Category.CLASS),
        Classification("4789001", "Autres commerces de détail sur marchés et éventaires", Category.CLASS),
        Classification("47990", "Autres commerces de détail hors magasin, éventaires ou marchés", Category.CLASS),
        Classification(
            "4799001",
            "Commerce de détail de tous types de produits exercé selon des modalités non prévues dans les classes précédentes: par démarcheurs, distributeurs automatiques, démonstrateurs, marchands ambulant, etc.",
            Category.CLASS,
        ),
        Classification("95230", "Réparation de chaussures et d'articles en cuir", Category.CLASS),
        Classification(
            "9523001",
            "Réparation de chaussures, bagages, articles de maroquinerie et articles similaires, en cuir ou en autres matières",
            Category.CLASS,
        ),
        Classification("95210", "Réparation de produits électroniques grand public", Category.CLASS),
        Classification("9522001", "Réparation d'appareils électroménagers", Category.CLASS),
        Classification("9521001", "Réparation d'appareils audio et vidéo", Category.CLASS),
        Classification("95250", "Réparation d'articles d'horlogerie et de bijouterie", Category.CLASS),
        Classification("9525001", "Réparation de montres, horloges et bijoux", Category.CLASS),
        Classification("96099", "Autres services personnels", Category.CLASS),
        Classification("9529001", "Réparation de bicyclettes", Category.CLASS),
        Classification("9529002", "Réparation de jouets", Category.CLASS),
        Classification("9529003", "Réparation d'articles de sport et de camping", Category.CLASS),
        Classification("3311001", "Réparation et l'entretien de chaudières domestiques", Category.CLASS),
        Classification(
            "9529004", "Réparation de vêtements déjà portés: stoppage, remaillage, retouche, etc.", Category.CLASS
        ),
        Classification(
            "9529005",
            "Réparation d'articles divers (clés,serrures,talons,etc.), y compris la réparations urgentes à domicile",
            Category.CLASS,
        ),
        Classification("9529006", "Activités des accordeurs de piano et autres instruments de musique", Category.CLASS),
        Classification("9529007", "Réparation d'articles de photographie", Category.CLASS),
        Classification("9529008", "Autres réparations de biens de consommation n.d.a.", Category.CLASS),
        Classification("55100", "Hôtels et hébergement similaire", Category.CLASS),
        Classification(
            "5510001",
            "Services d'hébergement pour séjours de courte durée, en liaison ou non avec l'exploitation d'un restaurant, dans hôtels, motels et auberges (avec service hôtelier)",
            Category.CLASS,
        ),
        Classification("5510011", "Hôtels, motels, avec restaurant", Category.CLASS),
        Classification("55201", "Auberges pour jeunes", Category.CLASS),
        Classification("55209", "Hébergement touristique et autre hébergement de courte durée n.c.a.", Category.CLASS),
        Classification("5520101", "Auberges de jeunesse, refuges", Category.CLASS),
        Classification("55300", "Terrains de camping et parcs pour caravanes ou véhicules de loisirs", Category.CLASS),
        Classification("5530001", "Exploitation de terrains de camping", Category.CLASS),
        Classification("55202", "Centres et villages de vacances", Category.CLASS),
        Classification(
            "5520201",
            "Centres et villages de vacances (y compris les parcs résidentiels de bungalows et chalets) avec ou sans restaurant et infrastructure de sports à usage des touristes",
            Category.CLASS,
        ),
        Classification("5520901", "Colonies de vacances pour enfants ou adultes", Category.CLASS),
        Classification("55203", "Gîtes de vacances, appartements et meublés de vacances", Category.CLASS),
        Classification("55204", "Chambres d'hôtes", Category.CLASS),
        Classification("55900", "Autres hébergements", Category.CLASS),
        Classification(
            "5520301",
            "Mise à disposition de logement pour des séjours de courte durée dans des maisons et appartements des vacances",
            Category.CLASS,
        ),
        Classification("5520302", "Hébergement de courte durée à la ferme", Category.CLASS),
        Classification("5520902", "Autres moyens d'hébergement de courte durée n.d.a.", Category.CLASS),
        Classification(
            "5590001",
            "Mise à disposition d'hébergement collectif à des étudiants, ouvriers saisonniers, etc.",
            Category.CLASS,
        ),
        Classification("56101", "Restauration à service complet", Category.CLASS),
        Classification("56102", "Restauration à service restreint", Category.CLASS),
        Classification("5610101", "Restauration de type traditionnel", Category.CLASS),
        Classification("5610102", "Vente de repas à bord de navires ou de voitures-restaurants", Category.CLASS),
        Classification(
            "5610103",
            "Restaurants spécialisés en week-ends gastronomiques, les restaurants exotiques, etc.",
            Category.CLASS,
        ),
        Classification(
            "5610104",
            "Restaurants disposant de quelques chambres (max. 5) à usage de leur propre clientèle",
            Category.CLASS,
        ),
        Classification("5610105", "Cafés-restaurants (tavernes)", Category.CLASS),
        Classification(
            "5610201",
            "Vente au comptoir ou par téléphone, fax, internet d'aliments et de boissons : établissements de restauration rapide (snack-bars, sandwiches-bars, etc.)",
            Category.CLASS,
        ),
        Classification(
            "5610202",
            "Vente au comptoir ou par téléphone, fax, internet d'aliments et de boissons à consommer sur place : friteries, échoppes de hot-dogs, etc.",
            Category.CLASS,
        ),
        Classification(
            "5610203",
            "Vente au comptoir ou par téléphone, fax, internet d'aliments et de boissons : croissanteries, crêperies et gaufreries",
            Category.CLASS,
        ),
        Classification(
            "5610204",
            "Vente au comptoir ou par téléphone, fax, internet d'aliments et de boissons : laiteries, salons de thé, salons de dégustation de crèmes glacées, etc.",
            Category.CLASS,
        ),
        Classification(
            "5610205",
            "Vente au comptoir ou par téléphone, fax, internet d'aliments et de boissons : cafétérias",
            Category.CLASS,
        ),
        Classification(
            "5610206",
            "Vente au comptoir ou par téléphone, fax, internet  d'aliments et de boissons : services au volant (drive-in)",
            Category.CLASS,
        ),
        Classification(
            "5610207",
            "Vente au comptoir ou par téléphone, fax, internet d'aliments et de boissons : pizzerias",
            Category.CLASS,
        ),
        Classification("56301", "Cafés et bars", Category.CLASS),
        Classification(
            "5630101",
            "Vente de boissons destinées en général à être consommées sur place, par les établissements suivants, avec ou sans présentation d'un spectacle: cafés, bars, débits de bière, etc.",
            Category.CLASS,
        ),
        Classification("56302", "Discothèques, dancings et similaires", Category.CLASS),
        Classification("56309", "Autres débits de boissons", Category.CLASS),
        Classification(
            "5630201",
            "Exploitation régul. de discothèques, salles de bal et clubs privés, qui réalisent leur C.A. par la vente de boissons, avec ou sans obligation d'achat de tickets d'entrée donnant droit à des consomm.",
            Category.CLASS,
        ),
        Classification("56290", "Autres services de restauration", Category.CLASS),
        Classification(
            "5629001",
            "Préparation de repas et de mets dans les cuisines centrales pour le compte de tiers, tels les: compagnies aériennes, cantines, restaurants d'entreprises, etc.",
            Category.CLASS,
        ),
        Classification("56210", "Services des traiteurs", Category.CLASS),
        Classification(
            "5621001",
            "Préparation, la livraison à domicile et le service de repas et de plats cuisinés",
            Category.CLASS,
        ),
        Classification(
            "5621002",
            "Organisation de noces, banquets, cocktails, buffets, lunches et réceptions diverses",
            Category.CLASS,
        ),
        Classification("49200", "Transports ferroviaires de fret", Category.CLASS),
        Classification("49100", "Transport ferroviaire de voyageurs autre qu'urbain et suburbain", Category.CLASS),
        Classification("49310", "Transports urbains et suburbains de voyageurs", Category.CLASS),
        Classification(
            "4931001",
            "Transport par voie terrestre de passagers, urbain ou suburbain (autobus, tramway, métro, etc.) sur des lignes déterminées et conformément à un horaire établi",
            Category.CLASS,
        ),
        Classification("49390", "Autres transports terrestres de voyageurs n.c.a.", Category.CLASS),
        Classification(
            "4931011",
            "Transport interurbain de voyageurs, par autocar ou tramway, sur des lignes déterminées et conformément à un horaire établi",
            Category.CLASS,
        ),
        Classification(
            "4931012",
            "Exploitation d'autobus scolaires, de navettes vers les aéroports et les gares, le transport de personnel, etc.",
            Category.CLASS,
        ),
        Classification("49320", "Transports de voyageurs par taxis", Category.CLASS),
        Classification("4932001", "Exploitation de taxis", Category.CLASS),
        Classification("4932002", "Location de voitures particulières avec chauffeur", Category.CLASS),
        Classification(
            "4939001",
            "Autres transports routiers de passagers, non réguliers: transports à la demande, excursions touristiques par autocar ou autobus, etc.",
            Category.CLASS,
        ),
        Classification("4939002", "Transport de personnes par véhicules à traction animale", Category.CLASS),
        Classification("49420", "Services de déménagement", Category.CLASS),
        Classification(
            "4942001", "Déménagement de mobilier de particuliers, de bureaux, d'ateliers ou d'usines", Category.CLASS
        ),
        Classification("4942002", "Garde-meubles", Category.CLASS),
        Classification("4942003", "Livraison de meubles et équipements ménagers", Category.CLASS),
        Classification("49410", "Transports routiers de fret, sauf services de déménagement", Category.CLASS),
        Classification(
            "4941001",
            "Transport de marchandises par route : transport de bois de sciage, de bétail, de voit., de déchets, transp. frigorifique, transp. lourd international, transp. en vrac, y compris par camions-citernes",
            Category.CLASS,
        ),
        Classification(
            "4941002", "Collecte de lait et transport vers les unités de traitement du lait", Category.CLASS
        ),
        Classification("4941003", "Transport de béton, prêt à l'emploi, non fabriqué par l'unité même", Category.CLASS),
        Classification(
            "4941004", "Transport de marchandises par véhicules à traction humaine ou animale", Category.CLASS
        ),
        Classification("4941011", "Location de camions avec conducteur", Category.CLASS),
        Classification("49500", "Transports par conduites", Category.CLASS),
        Classification(
            "4950001", "Transport de gaz, de liquides et d'autres substances, par conduites", Category.CLASS
        ),
        Classification("4950002", "Exploitation de stations de pompage", Category.CLASS),
        Classification("50200", "Transports maritimes et côtiers de fret", Category.CLASS),
        Classification("50100", "Transports maritimes et côtiers de passagers", Category.CLASS),
        Classification("5020001", "Transport par eau, régulier ou non, de marchandises", Category.CLASS),
        Classification("5010001", "Exploitation de bateaux d'excursion, de croisière ou de tourisme", Category.CLASS),
        Classification("5020002", "Exploitation de bacs, de bateaux-taxis, etc.", Category.CLASS),
        Classification("5020003", "Exploitation de remorqueurs et de pousseurs de péniches", Category.CLASS),
        Classification("5020004", "Location de bateaux et navires avec équipage", Category.CLASS),
        Classification("50400", "Transports fluviaux de fret", Category.CLASS),
        Classification("50300", "Transports fluviaux de passagers", Category.CLASS),
        Classification(
            "5040001",
            "Transport de marchandises: sur les fleuves, les canaux, les lacs et les autres voies navigables intérieures; à l'intérieur des ports et des docks",
            Category.CLASS,
        ),
        Classification("51100", "Transports aériens de passagers", Category.CLASS),
        Classification("51210", "Transports aériens de fret", Category.CLASS),
        Classification(
            "5110001",
            "Transport aérien de passagers sur des lignes régulières et selon des horaires réguliers",
            Category.CLASS,
        ),
        Classification("5110011", "Transport aérien non régulier de personnes", Category.CLASS),
        Classification("5110012", "Vols par charters, réguliers ou non", Category.CLASS),
        Classification("5110013", "Exploitation d'avions-taxis", Category.CLASS),
        Classification("5110014", "Excursions aériennes, les baptêmes de l'air, etc.", Category.CLASS),
        Classification("5110015", "Location d'avions avec pilote", Category.CLASS),
        Classification("51220", "Transports spatiaux", Category.CLASS),
        Classification("52241", "Manutention portuaire", Category.CLASS),
        Classification(
            "5224101",
            "Chargement et déchargement de marchandises ou de bagages dans les ports maritimes",
            Category.CLASS,
        ),
        Classification("5224102", "Arrimage et débardage de marchandises", Category.CLASS),
        Classification("52249", "Manutention autre que portuaire", Category.CLASS),
        Classification(
            "5224901",
            "Chargement, transbordement et déchargement de marchandises et de bagages ailleurs que dans les ports maritimes (manutention routière, ferroviaire, fluviale et sur aéroports)",
            Category.CLASS,
        ),
        Classification("52100", "Entreposage et stockage, y compris frigorifique", Category.CLASS),
        Classification(
            "5210001",
            "Exploitation pour compte de tiers d'installations d'entreposage frigorifique ou de lieux de stockage réfrigéré pour tous les types de produits, y compris les produits agricoles",
            Category.CLASS,
        ),
        Classification(
            "5210011",
            "Exploitation pour cpte de tiers d'install. d'entreposage non frigorifiques (silos, entrepôts, hangars, parcs à conteneurs, citernes, etc.) pour ts types de mchdises, y compris les pdts agricoles",
            Category.CLASS,
        ),
        Classification(
            "5221001",
            "Exploitation de gares ferroviaires et routières et de terminaux de manutention de fret",
            Category.CLASS,
        ),
        Classification(
            "5221002",
            "Exploitation d'autoroutes, de tunnels, de ponts, de parcs et emplacements de stationnement de véhicules et de garages pour bicyclettes",
            Category.CLASS,
        ),
        Classification("5221003", "Gardiennage de caravanes durant l'hiver", Category.CLASS),
        Classification(
            "4939011",
            "Organisation de covoiturage et d'autres formes de transport en commun non public de personnes",
            Category.CLASS,
        ),
        Classification("5221004", "Exploitation de centrales d'appel pour taxis", Category.CLASS),
        Classification(
            "85329", "Enseignement secondaire technique, professionnel et spécialisé n.c.a.", Category.CLASS
        ),
        Classification(
            "5222001",
            "Exploitation d'installations portuaires: jetées, quais, bassins, terminaux, etc.",
            Category.CLASS,
        ),
        Classification("5222002", "Exploitation de ports fluviaux, voies fluviales et écluses", Category.CLASS),
        Classification("5222003", "Navigation, pilotage, mouillage", Category.CLASS),
        Classification("5222004", "Renflouement des navires, services de sauvetage", Category.CLASS),
        Classification("52230", "Services auxiliaires des transports aériens", Category.CLASS),
        Classification("8532901", "Activités des écoles de pilotage pour pilotes de ligne", Category.CLASS),
        Classification("5223001", "Services au sol d'entretien-maintenance des avions", Category.CLASS),
        Classification("5223002", "Protection et la lutte contre les incendies", Category.CLASS),
        Classification("79110", "Activités des agences de voyage", Category.CLASS),
        Classification("7911001", "Fourniture d'informations et de conseils en matière de voyages", Category.CLASS),
        Classification(
            "7911002",
            "Organisation de voyages et d'excursions de courte durée, l'organisation de voyages personnalisés, de l'hébergement et du transport des voyageurs et des touristes",
            Category.CLASS,
        ),
        Classification(
            "7911003",
            "Vente sur base de brochures et de catalogues de voyages organisés par les tour operators",
            Category.CLASS,
        ),
        Classification("7911004", "Vente de billets d'entrée", Category.CLASS),
        Classification("79120", "Activités des voyagistes", Category.CLASS),
        Classification(
            "7912001",
            "Organisateurs de voyages qui, en général, présentent une large gamme de voyages.  Leurs clients peuvent choisir parmi plusieurs formules et destinations à l'aide de brochures et de catalogues",
            Category.CLASS,
        ),
        Classification(
            "7912002",
            "Organisateurs spécialisés dans une formule de vacances déterminée pour laquelle ils offrent des destinations diverses",
            Category.CLASS,
        ),
        Classification("79901", "Services d'information touristique", Category.CLASS),
        Classification("79909", "Autres services de réservation", Category.CLASS),
        Classification("7990101", "Guides, services d'information touristique et similaires", Category.CLASS),
        Classification("52290", "Autres services auxiliaires des transports", Category.CLASS),
        Classification("5229001", "Agences d'expédition", Category.CLASS),
        Classification("5229011", "Affrètement maritime", Category.CLASS),
        Classification(
            "5229012",
            "Affrètement qui consiste à confier des envois sans groupage préalable à des transporteurs publics (transport ferroviaire, transport par eau, transport aérien ou une combinaison de ces moyens)",
            Category.CLASS,
        ),
        Classification("5229021", "Agences maritimes", Category.CLASS),
        Classification(
            "5229031",
            "Activités des commissionnaires de transport qui concluent pour compte propre des contrats de transport de marchandises mais font effectuer le transport par des tiers",
            Category.CLASS,
        ),
        Classification("5229032", "Activités des courtiers de transport", Category.CLASS),
        Classification("5229033", "Activités des commissionnaires-expéditeurs, etc.", Category.CLASS),
        Classification(
            "5229041",
            "Messageries: l'enlèvement de marchandises et le groupage d'envois individuels pour l'expédition, la distribution et la livraison des marchandises à l'arrivée",
            Category.CLASS,
        ),
        Classification("5229042", "Livraison de fret express", Category.CLASS),
        Classification("5229043", "Autres activités annexes de l'organisation du transport de fret", Category.CLASS),
        Classification(
            "53100", "Activités de poste dans le cadre d'une obligation de service universel", Category.CLASS
        ),
        Classification(
            "82190",
            "Photocopie, préparation de documents et autres activités spécialisées de soutien de bureau",
            Category.CLASS,
        ),
        Classification("5310001", "Levée, acheminement et distribution du courrier et des colis", Category.CLASS),
        Classification(
            "5310002",
            "Collecte du courrier et des colis dans les boîtes à lettres publiques ou les bureaux de poste",
            Category.CLASS,
        ),
        Classification("5310003", "Distribution et la livraison du courrier et des colis", Category.CLASS),
        Classification("8219001", "Location de boîtes postales, le service de poste restante, etc.", Category.CLASS),
        Classification("53200", "Autres activités de poste et de courrier", Category.CLASS),
        Classification(
            "5320001",
            "Levée, acheminement et distribution de lettres, colis et paquets par des entr. autres que l'admininistration postale nationale. Il peut être fait appel à un seul ou à plusieurs modes de transp.",
            Category.CLASS,
        ),
        Classification("61200", "Télécommunications sans fil", Category.CLASS),
        Classification("60200", "Programmation de télévision et télédiffusion", Category.CLASS),
        Classification("61100", "Télécommunications filaires", Category.CLASS),
        Classification("61300", "Télécommunications par satellite", Category.CLASS),
        Classification("61900", "Autres activités de télécommunication", Category.CLASS),
        Classification(
            "6120001",
            "Transmission des sons, des images, de données ou d'autres informations par câble, par voie hertzienne, par relais ou par satellite",
            Category.CLASS,
        ),
        Classification(
            "6120002",
            "Exploitation de réseaux de communication électroniques à usage général ou à usage de catégories déterminées d'utilisateurs (p.ex. institutions financières)",
            Category.CLASS,
        ),
        Classification("6120003", "Téléphone, mobilophones, télégraphe, télex, fax", Category.CLASS),
        Classification("6120004", "Entretien des réseaux", Category.CLASS),
        Classification(
            "6120005",
            "Transmission (transport) de programmes de radio et de télévision (radiodistribution et télédistribution, sociétés de câble)",
            Category.CLASS,
        ),
        Classification("64110", "Activités de banque centrale", Category.CLASS),
        Classification("64190", "Autres intermédiations monétaires", Category.CLASS),
        Classification("66191", "Activités des agents et courtiers en services bancaires", Category.CLASS),
        Classification("64910", "Crédit-bail", Category.CLASS),
        Classification(
            "6491001",
            "Conclusion d'un contrat de location-financement sur des biens d'équipement entre le bailleur et le locataire",
            Category.CLASS,
        ),
        Classification("64921", "Octroi de crédit à la consommation", Category.CLASS),
        Classification(
            "6492101",
            "Activités des organismes de financement concluant des contrats de crédit avec un consommateur : ventes et prêts à tempérament, crédit-bail (hors activités professionnelles), ouvertures de crédit, etc.",
            Category.CLASS,
        ),
        Classification("64922", "Octroi de crédit hypothécaire", Category.CLASS),
        Classification("64929", "Autre distribution de crédit n.c.a.", Category.CLASS),
        Classification(
            "6492201",
            "Unités qui consentent uniquement les crédits suivants: crédits hypothécaires, crédits professionnels, crédits permanents, crédit de caisse, etc.",
            Category.CLASS,
        ),
        Classification("6492202", "Activités exercées par les bureaux d'escompte", Category.CLASS),
        Classification("6492203", "Autre distribution de crédit n.d.a.", Category.CLASS),
        Classification("64991", "Activités d'affacturage (Factoring)", Category.CLASS),
        Classification("64200", "Activités des sociétés holding", Category.CLASS),
        Classification(
            "6420001",
            "Détention à long terme d'actions émanant de plusieurs autres entreprises classées en majorité dans le secteur financier",
            Category.CLASS,
        ),
        Classification("64992", "Activités des sociétés de bourse", Category.CLASS),
        Classification("64300", "Fonds de placement et entités financières similaires", Category.CLASS),
        Classification("64999", "Autres activités des services financiers", Category.CLASS),
        Classification("6499901", "Caisse des Dépôts et Consignations", Category.CLASS),
        Classification(
            "6499902",
            "Institutions financières qui offrent des formes de financement spécifique: capital à haut risque ou venture capital, investmentbanking, etc.",
            Category.CLASS,
        ),
        Classification("6499903", "Transactions sur lingots d'or réalisées sur les marchés financiers", Category.CLASS),
        Classification("6499904", "Financements d'import/export", Category.CLASS),
        Classification("6499905", "Intermédiations financières n.d.a.", Category.CLASS),
        Classification("65111", "Opérations directes d'assurance vie", Category.CLASS),
        Classification("65200", "Réassurance", Category.CLASS),
        Classification(
            "65112", "Activités des entreprises d'assurances multibranches à prédominance vie", Category.CLASS
        ),
        Classification(
            "6511201",
            "Entreprises d'assurances qui concluent tant des assurances Vie que des Non Vie, mais dont l'activité principale consiste à conclure des assurances Vie",
            Category.CLASS,
        ),
        Classification("65300", "Caisses de retraite", Category.CLASS),
        Classification(
            "6530001",
            "Activités (encaiss. de cotisations, placem. de fonds, prestat. des pensions) des institutions de prévoyance créées par l'employeur (privé ou public) afin de constituer une pension extra-légale",
            Category.CLASS,
        ),
        Classification(
            "6530002",
            "Activités des caisses de pensions créées en faveur de professions libérales et indépend. auxquelles on peut s'affilier sur une base individ. et volontaire pour constituer une pension extra-légale",
            Category.CLASS,
        ),
        Classification("65121", "Opérations directes d'assurance non-vie", Category.CLASS),
        Classification("6512101", "Activités d'assurances concernant accidents et maladie", Category.CLASS),
        Classification("6512102", "Activités d'assurances concernant véhicules automobiles", Category.CLASS),
        Classification(
            "6512103",
            "Activités d'assurances concernant assurance maritime, assurance transports, assurance aérienne",
            Category.CLASS,
        ),
        Classification(
            "6512104", "Activités d'assurances concernant l'incendie et autres dommages aux biens", Category.CLASS
        ),
        Classification("6512105", "Activités d'assurances concernant la responsabilité civile", Category.CLASS),
        Classification("6512106", "Activités d'assurances concernant crédit et caution", Category.CLASS),
        Classification("6512107", "Activités d'assurances concernant pertes pécuniaires diverses", Category.CLASS),
        Classification("6512108", "Activités d'assurances concernant la protection juridique", Category.CLASS),
        Classification("6512109", "Activités d'assurances concernant l'assistance", Category.CLASS),
        Classification(
            "65122", "Activités des entreprises d'assurances multibranches à prédominance non-vie", Category.CLASS
        ),
        Classification("66110", "Administration de marchés financiers", Category.CLASS),
        Classification(
            "6611001",
            "Exploitation et la supervision de marchés financiers autrement que par des organismes publics: activités des bourses de valeurs mobilières, bourses d'option et de futures, etc.",
            Category.CLASS,
        ),
        Classification(
            "66199",
            "Autres activités auxiliaires de services financiers n.c.a., hors assurance et caisses de retraite",
            Category.CLASS,
        ),
        Classification("66120", "Courtage de valeurs mobilières et de marchandises", Category.CLASS),
        Classification("66300", "Gestion de fonds", Category.CLASS),
        Classification(
            "6619901",
            "Opérations exécutées sur des marchés financiers pour le compte de tiers (p.ex. le courtage en valeurs mobilières) ainsi que les activités qui s'y rattachent",
            Category.CLASS,
        ),
        Classification("6619902", "Sociétés de gestion des fonds communs de placement", Category.CLASS),
        Classification(
            "6619903",
            "Conseils en placements et la gestion de patrimoines financiers des tiers (AR du 5 août 1991 relatif à la gestion de fortune et au conseil en placements)",
            Category.CLASS,
        ),
        Classification("6619911", "Courtiers en crédits hypothécaires", Category.CLASS),
        Classification("6619912", "Bureaux de change", Category.CLASS),
        Classification("6619913", "Caution et garantie", Category.CLASS),
        Classification(
            "6619914", "Intermédiation en crédits et prêts par des courtiers et autres intermédiaires", Category.CLASS
        ),
        Classification(
            "6619915",
            "Représentants de banques étrangères, qui n'exécutent pas des opérations de banque proprement dites",
            Category.CLASS,
        ),
        Classification(
            "6619916", "Création et l'exploitation de systèmes électroniques de circulation monétair", Category.CLASS
        ),
        Classification("6619917", "Emission de chèques-repas", Category.CLASS),
        Classification("6619918", "Mise à disposition de coffres-forts, etc.", Category.CLASS),
        Classification("66220", "Activités des agents et courtiers d'assurances", Category.CLASS),
        Classification("6622001", "Agents et courtiers d'assurances", Category.CLASS),
        Classification("66210", "Évaluation des risques et dommages", Category.CLASS),
        Classification("6621001", "Experts en dommages et risques", Category.CLASS),
        Classification("66290", "Autres activités auxiliaires d'assurance et de caisses de retraite", Category.CLASS),
        Classification("6629001", "Autres auxiliaires d'assurances", Category.CLASS),
        Classification("41101", "Promotion immobilière résidentielle", Category.CLASS),
        Classification(
            "4110101",
            "Promotion immobilière de maisons d'habitation neuves ou de travaux de rénovation",
            Category.CLASS,
        ),
        Classification("4110102", "Promotion immobilière d'immeubles résidentiels", Category.CLASS),
        Classification("41102", "Promotion immobilière non résidentielle", Category.CLASS),
        Classification("4110201", "Promotion immobilière de bureaux", Category.CLASS),
        Classification(
            "4110211",
            "Promotion immobilière de: centres commerciaux et industriels, hôtels, zones d'activités et marchés, ports de plaisance, stations de sports d'hiver, etc.",
            Category.CLASS,
        ),
        Classification("4110212", "Aménagement ou rénovation de zones urbaines par voie de promotion", Category.CLASS),
        Classification("4299011", "Lotissement foncier", Category.CLASS),
        Classification("4299012", "Aménagement et remembrement de zones rurales", Category.CLASS),
        Classification("4299013", "Aménagement de parcelles de cimetières", Category.CLASS),
        Classification("68100", "Activités des marchands de biens immobiliers", Category.CLASS),
        Classification(
            "6810001",
            "Activités de transactions sur biens immobiliers tels que: immeubles résidentiels et maisons d'habitation, immeubles non résidentiels, terres et terrains",
            Category.CLASS,
        ),
        Classification(
            "6810002",
            "Transactions sur biens propres tels que fonds de commerce, droits à bail et pas de porte (reprise)",
            Category.CLASS,
        ),
        Classification(
            "68201",
            "Location et exploitation de biens immobiliers résidentiels propres ou loués, sauf logements sociaux",
            Category.CLASS,
        ),
        Classification(
            "6820101",
            "Location d'appartements et de maisons, vides ou meublés, destinés à l'habitation",
            Category.CLASS,
        ),
        Classification("6820102", "Location de longue durée en hôtels-appartements", Category.CLASS),
        Classification("6820103", "Exploitation de biens immobiliers en multipropriété", Category.CLASS),
        Classification("68202", "Location et exploitation de logements sociaux", Category.CLASS),
        Classification(
            "6820201", "Promotion immobilière à objectif locatif par des sociétés de logements sociaux", Category.CLASS
        ),
        Classification(
            "68203",
            "Location et exploitation de biens immobiliers non résidentiels propres ou loués, sauf terrains",
            Category.CLASS,
        ),
        Classification(
            "6820301",
            "Location d'immeubles non résidentiels ( bureaux, espaces commerciaux, halls d'exposition, etc.)",
            Category.CLASS,
        ),
        Classification("6820302", "Location à l'année de boxes ou de lieux de garage de véhicules", Category.CLASS),
        Classification("6820303", "Location de fonds de commerce (dans un système de gérances libres)", Category.CLASS),
        Classification("68204", "Location et exploitation de terrains", Category.CLASS),
        Classification("6820401", "Location de terrains ( bâtis ou non) à usage agricole", Category.CLASS),
        Classification("6820402", "Location à l'année d'emplacements de caravanes", Category.CLASS),
        Classification(
            "68311",
            "Intermédiation en achat, vente et location de biens immobiliers pour compte de tiers",
            Category.CLASS,
        ),
        Classification(
            "6831101",
            "Agences immobilières et intermédiaires en achat, vente et location de biens immobiliers",
            Category.CLASS,
        ),
        Classification("68312", "Estimation et évaluation de biens immobiliers pour compte de tiers", Category.CLASS),
        Classification("6831201", "Estimation et évaluation de biens immobiliers", Category.CLASS),
        Classification("81100", "Activités combinées de soutien lié aux bâtiments", Category.CLASS),
        Classification(
            "68321", "Administration de biens immobiliers résidentiels pour compte de tiers", Category.CLASS
        ),
        Classification(
            "6832101",
            "Prise en charge au nom du (ou des) propriétaire(s) de l'ensemble des services nécessaires au fonctionnement des immeubles gérés (immeubles résidentiels)",
            Category.CLASS,
        ),
        Classification("6832102", "Collecte des loyers (immeubles résidentiels)", Category.CLASS),
        Classification(
            "68322", "Administration de biens immobiliers non résidentiels pour compte de tiers", Category.CLASS
        ),
        Classification(
            "6832201",
            "Prise en charge au nom du (ou des) propriétaire (s) de l'ensemble des services nécessaires au fonctionnement des immeubles gérés (immeubles non résidentiels)",
            Category.CLASS,
        ),
        Classification("6832202", "Collecte des loyers (immeubles non résidentiels)", Category.CLASS),
        Classification(
            "77110",
            "Location et location-bail d'automobiles et d'autres véhicules automobiles légers (< 3,5 tonnes)",
            Category.CLASS,
        ),
        Classification("7711001", "Location à court terme de voitures particulières sans chauffeur", Category.CLASS),
        Classification("7711002", "Location à longue durée de voitures particulières sans chauffeur", Category.CLASS),
        Classification(
            "7711003",
            "Location à court terme ou la location-bail de véhicules utilitaires légers (max. 3,5 t) sans conducteur",
            Category.CLASS,
        ),
        Classification(
            "77120",
            "Location et location-bail de camions et d'autres véhicules automobiles lourds (> 3,5 ton)",
            Category.CLASS,
        ),
        Classification("77393", "Location et location-bail de caravanes et de motorhomes", Category.CLASS),
        Classification(
            "77399", "Location et location-bail d'autres machines, équipements et biens matériels", Category.CLASS
        ),
        Classification(
            "7712001",
            "Location et location-bail de matériels de transp. terrestre, sans chauffeur, à l'excl. de voit. particulières et de véhicules utilit. légers: véhicules de chem.de fer, camions, tract. de halage, etc.",
            Category.CLASS,
        ),
        Classification("77340", "Location et location-bail de matériels de transport par eau", Category.CLASS),
        Classification(
            "7734001",
            "Location et location-bail de matériels de transport maritime et fluvial tels que bateaux, cargos et navires de transport, sans équipage",
            Category.CLASS,
        ),
        Classification("77350", "Location et location-bail de matériels de transport aérien", Category.CLASS),
        Classification(
            "7735001", "Location et location-bail de matériels de transport aérien, sans pilote", Category.CLASS
        ),
        Classification("77310", "Location et location-bail de machines et d'équipements agricoles", Category.CLASS),
        Classification("7731001", "Location de tracteurs agricoles et de motoculteurs", Category.CLASS),
        Classification(
            "7731002",
            "Location de machines et équipements pour l'agriculture, l'élevage et l'exploitation forestière, sans opérateur (= la location des produits fabriqués dans le groupe 29.3)",
            Category.CLASS,
        ),
        Classification(
            "77320", "Location et location-bail de machines et d'équipements pour la construction", Category.CLASS
        ),
        Classification(
            "77394",
            "Location et location-bail de conteneurs à usage d'habitation, de bureau et similaires",
            Category.CLASS,
        ),
        Classification(
            "7732001",
            "Location et location-bail de machines et équipements pour le bâtiment et le génie-civil, sans opérateur (grues, bouteurs, bétonnières, etc.)",
            Category.CLASS,
        ),
        Classification(
            "7732002",
            "Location d'échafaudages et de plates-formes de travail, sans montage ni démontage",
            Category.CLASS,
        ),
        Classification(
            "77330", "Location et location-bail de machines de bureau et de matériel informatique", Category.CLASS
        ),
        Classification(
            "7733001",
            "Location et location-bail de machines et équipements de bureau, sans opérateur: ordinateurs, machines et matériels informatiques, duplicateurs, photocop., machines à écr. et de traitem. de texte, etc.",
            Category.CLASS,
        ),
        Classification("7733002", "Location, ou la redevance d'utilisation, de logiciels", Category.CLASS),
        Classification(
            "77391",
            "Location et location-bail de machines à sous, de machines de jeux et de machines automatiques de vente de produits",
            Category.CLASS,
        ),
        Classification("77392", "Location et location-bail de tentes", Category.CLASS),
        Classification(
            "7739901",
            "Location et location-bail de moteurs et turbines, compresseurs, machines-outils, sans opérateur",
            Category.CLASS,
        ),
        Classification(
            "7739902",
            "Location et location-bail de matériels de radiodiffusion, de télévision et de communication, sans opérateur",
            Category.CLASS,
        ),
        Classification(
            "7739903", "Location et location-bail de matériels de mesure et de contrôle, sans opérateur", Category.CLASS
        ),
        Classification(
            "7739904",
            "Location et location-bail d'autres machines et matériels à usage scientifique, commercial et industriel, y compris les machines automatiques de vente de produits, sans opérateur",
            Category.CLASS,
        ),
        Classification(
            "7739201",
            "Location et location-bail de chapiteaux pour expositions, fêtes d'entreprises, concerts, etc., sans opérateur",
            Category.CLASS,
        ),
        Classification(
            "7739101",
            "Location et location-bail de machines à sous et jeux, électroniques ou non, pour cafés, casinos, etc.",
            Category.CLASS,
        ),
        Classification(
            "77291",
            "Location et location-bail de machines-outils, de matériel et d'outils à main pour le bricolage",
            Category.CLASS,
        ),
        Classification("7729101", "Location de machines-outils et de matériel de bricolage", Category.CLASS),
        Classification("7729102", "Location de tondeuses à gazon", Category.CLASS),
        Classification("77220", "Location de vidéocassettes et de disques vidéo", Category.CLASS),
        Classification("7722001", "Location de vidéocassettes et bandes-vidéo", Category.CLASS),
        Classification("7722002", "Location de disques, de disques compacts, etc.", Category.CLASS),
        Classification(
            "77292", "Location et location-bail de téléviseurs et d'autres appareils audiovisuels", Category.CLASS
        ),
        Classification("7729201", "Location de téléviseurs et d'autres appareils audio-visuels", Category.CLASS),
        Classification(
            "77293",
            "Location et location-bail de vaisselle, couverts, verrerie, articles pour la cuisine, appareils électriques et électroménagers",
            Category.CLASS,
        ),
        Classification(
            "7729301", "Location de vaisselle, couverts, verrerie, appareils électroménagers, etc.", Category.CLASS
        ),
        Classification(
            "77294", "Location et location-bail de textiles, d'habillement, de bijoux et de chaussures", Category.CLASS
        ),
        Classification("7729401", "Location de textiles, d'habillement et de chaussures", Category.CLASS),
        Classification(
            "7729402",
            "Location de costumes de scène, de vêtements de carnaval, de vêtements de cérémonie, de bijoux, etc.",
            Category.CLASS,
        ),
        Classification("77210", "Location et location-bail d'articles de loisirs et de sport", Category.CLASS),
        Classification("7721001", "Location d'articles de sport et de camping", Category.CLASS),
        Classification("7721002", "Location de bicyclettes", Category.CLASS),
        Classification("7721003", "Location d'embarcations de plaisance", Category.CLASS),
        Classification("77295", "Location et location-bail de matériel médical et paramédical", Category.CLASS),
        Classification("7729501", "Location de matériel médical et paramédical", Category.CLASS),
        Classification(
            "77299", "Location et location-bail d'autres biens personnels et domestiques n.c.a.", Category.CLASS
        ),
        Classification("77296", "Location et location-bail de fleurs et de plantes", Category.CLASS),
        Classification("7729901", "Location de décors", Category.CLASS),
        Classification("7729902", "Location de livres et périodiques", Category.CLASS),
        Classification("7729601", "Location de fleurs et plantes", Category.CLASS),
        Classification("7729903", "Location d'instruments de musique", Category.CLASS),
        Classification("7729904", "Location d'autres biens personnels et domestiques, n.d.a.", Category.CLASS),
        Classification("62020", "Conseil informatique", Category.CLASS),
        Classification(
            "6202001",
            "Activités de conseil aux utilisateurs concernant le type et la configuration du matériel informatique et les applications logicielles",
            Category.CLASS,
        ),
        Classification("6202002", "Activités des intégrateurs de réseaux", Category.CLASS),
        Classification("62010", "Programmation informatique", Category.CLASS),
        Classification("58290", "Édition d'autres logiciels", Category.CLASS),
        Classification("58210", "Édition de jeux électroniques", Category.CLASS),
        Classification("63110", "Traitement de données, hébergement et activités connexes", Category.CLASS),
        Classification("62030", "Gestion d'installations informatiques", Category.CLASS),
        Classification(
            "6311001",
            "Traitement en continu ou non de données à l'aide, soit du programme du client, soit d'un programme propre à un constructeur: service de saisie de données, traitement complet de données",
            Category.CLASS,
        ),
        Classification(
            "6311002",
            "Gestion et exploitation en continu de matériel informatique appartenant à des tiers",
            Category.CLASS,
        ),
        Classification("60100", "Diffusion de programmes radio", Category.CLASS),
        Classification("63120", "Portails Internet", Category.CLASS),
        Classification(
            "6311011",
            "Création de banques de données par assemblage et interprétation éventuelle de données provenant d'une ou plusieurs sources: horaires, catalogues industriels, données scientifiques, etc.",
            Category.CLASS,
        ),
        Classification(
            "6311012",
            "Stockage de données: préparation d'un enregistrement informatique de ces informations selon une structure prédéterminée",
            Category.CLASS,
        ),
        Classification(
            "6311013",
            "Mise à disposition de banques de données : fourniture des données aux utilisateurs (individuels ou groupés), dans un certain ordre ou séquence, par accès direct (on-line) ou extraction",
            Category.CLASS,
        ),
        Classification("95110", "Réparation d'ordinateurs et d'équipements périphériques", Category.CLASS),
        Classification(
            "9511001", "Entretien et réparation d'ordinateurs et de matériel informatique périphérique", Category.CLASS
        ),
        Classification(
            "9511002", "Entretien et réparation de machines comptables et autres machines de bureau", Category.CLASS
        ),
        Classification("72190", "Recherche-développement en autres sciences physiques et naturelles", Category.CLASS),
        Classification("72110", "Recherche-développement en biotechnologie", Category.CLASS),
        Classification("72200", "Recherche-développement en sciences humaines et sociales", Category.CLASS),
        Classification(
            "7219001",
            "Etudes systématiques et efforts de création entrepris dans divers types de recherche-développement en math. et sciences naturelles (physique, astronomie,chimie, sciences médicales, biologie, etc.)",
            Category.CLASS,
        ),
        Classification(
            "7220001",
            "Etudes systématiques et efforts de création entrepris dans divers types de recherche-développement en sciences sociales et humaines (économie, psychologie, sociologie, droit, etc.)",
            Category.CLASS,
        ),
        Classification("69101", "Activités des avocats", Category.CLASS),
        Classification("69109", "Autres activités juridiques", Category.CLASS),
        Classification("69102", "Activités des notaires", Category.CLASS),
        Classification("69103", "Activités des huissiers de justice", Category.CLASS),
        Classification("6910901", "Autre assistance juridique", Category.CLASS),
        Classification("69202", "Activités des comptables et des comptables-fiscalistes", Category.CLASS),
        Classification(
            "6920201",
            "Activités de conseil en matière comptable et l'organisation des services comptables pour des tiers",
            Category.CLASS,
        ),
        Classification(
            "6920202",
            "Ouverture, tenue, centralisation et clôture des écritures comptables propres à l'établissement des comptes",
            Category.CLASS,
        ),
        Classification(
            "6920203",
            "Détermination des résultats et rédaction des comptes annuels dans la forme de requise par les dispositions légales en la matière",
            Category.CLASS,
        ),
        Classification("69201", "Activités des experts-comptables et des conseils fiscaux", Category.CLASS),
        Classification("69203", "Activités des réviseurs d'entreprises", Category.CLASS),
        Classification(
            "6920101", "Etablissement de déclarations fiscales pour les particuliers et les entreprises", Category.CLASS
        ),
        Classification(
            "6920102",
            "Activités de conseil et de représentation (autre que la représentation juridique), pour le compte de clients, devant l'administration fiscale",
            Category.CLASS,
        ),
        Classification("73200", "Études de marché et sondages d'opinion", Category.CLASS),
        Classification(
            "7320001",
            "Etudes portant sur potentiel commercial de pdts, leur acceptation et connaissance par le public, sur les habitudes d'ach. des consommateurs aux fins de la promotion des ventes et élab. de pdts. nouv.",
            Category.CLASS,
        ),
        Classification("7320002", "Analyses statistiques des résultats de ces études", Category.CLASS),
        Classification(
            "7320011",
            "Sondages d'opinion sur les questions politiques, économiques et sociales ainsi que l'analyse statistique des résultats",
            Category.CLASS,
        ),
        Classification("70210", "Conseil en relations publiques et en communication", Category.CLASS),
        Classification(
            "7021001",
            "Conseils et assistance opérationnelle aux entreprises dans les domaines des relations publiques et de la communication",
            Category.CLASS,
        ),
        Classification(
            "7021002", "Arbitrage et conciliation entre la direction des entreprises et ses salariés", Category.CLASS
        ),
        Classification("70220", "Conseil pour les affaires et autres conseils de gestion", Category.CLASS),
        Classification(
            "74901",
            "Activités des agents et représentants d'artistes, de sportifs et d'autres personnalités publiques",
            Category.CLASS,
        ),
        Classification(
            "7022001",
            "Conseils et assistance aux entreprises et aux services publics en matière de planification, d'organisation, de recherche du rendement, de contrôle, d'information du gestion, etc.",
            Category.CLASS,
        ),
        Classification(
            "7022002",
            "Calcul des coûts et des profits des mesures proposées en matière de planification, d'organisation, de rendement, etc.",
            Category.CLASS,
        ),
        Classification("7022003", "Activités d'audit général", Category.CLASS),
        Classification(
            "7022004",
            "Conseils en gestion donnés par exemple par des agronomes ou des économistes agricoles auprès d'exploitations agricoles etc.",
            Category.CLASS,
        ),
        Classification("70100", "Activités des sièges sociaux", Category.CLASS),
        Classification(
            "6420011",
            "Activités de gestion de holdings : intervention dans la gestion journalière, représentation des entreprises sur base de la possession ou du contrôle du capital social, etc.",
            Category.CLASS,
        ),
        Classification(
            "6420012",
            "Détention à long terme des actions émanant de plusieurs autres entreprises classées dans différents secteurs économiques",
            Category.CLASS,
        ),
        Classification("71111", "Activités d'architecture de construction", Category.CLASS),
        Classification("71113", "Activités d'architecture d'urbanisme, de paysage et de jardin", Category.CLASS),
        Classification("7111101", "Activités de conseil en matière d'architecture au maître d'ouvrage", Category.CLASS),
        Classification("7111102", "Conception de bâtiments et établissement de plans", Category.CLASS),
        Classification(
            "7111103",
            "Surveillance des travaux de construction (gros oeuvre, installation, travaux de finition, etc.)",
            Category.CLASS,
        ),
        Classification(
            "7111301", "Etudes et conseil en matière d'aménagement urbain et d'architecture paysagère", Category.CLASS
        ),
        Classification("7111302", "Conception de jardins, de parcs, etc.", Category.CLASS),
        Classification("7111104", "Conduite des opérations de gros entretien des bâtiments", Category.CLASS),
        Classification("71122", "Activités des géomètres", Category.CLASS),
        Classification("7112201", "Activités des géomètres-experts immobiliers", Category.CLASS),
        Classification("7112202", "Activités des économistes en construction", Category.CLASS),
        Classification(
            "7112203", "Etablissement de levées topographiques et le bornage des propriétés", Category.CLASS
        ),
        Classification("7112204", "Calcul du métré des ouvrages", Category.CLASS),
        Classification(
            "71121", "Activités d'ingénierie et de conseils techniques, sauf activités des géomètres", Category.CLASS
        ),
        Classification("74102", "Activités de design industriel", Category.CLASS),
        Classification("74909", "Autres activités spécialisées, scientifiques et techniques", Category.CLASS),
        Classification(
            "7112101",
            "Conception et réalisation de projets intéressant le génie électrique et électronique; le génie minier, chimique, mécanique et industriel, l'ingénierie de systèmes, les techniques de sécurité, etc.",
            Category.CLASS,
        ),
        Classification("7112102", "Dessin industriel", Category.CLASS),
        Classification(
            "7112103",
            "Elaboration de projets faisant appel au génie acoustique, aux techniques de la climatisation, de la réfrigération, de l'assainissement et de la lutte contre la pollution, etc.",
            Category.CLASS,
        ),
        Classification(
            "7112104",
            "Elaboration de projets comportant des activités ayant trait au génie civil ou de bâtiment, au génie hydraulique et à la technique du trafic",
            Category.CLASS,
        ),
        Classification(
            "7112105",
            "Activités géologiques et prospection: observation et mesures de surface pour recueillir des infos sur structure du sous-sol et emplacement gisements pétrole, gaz naturel, minéraux et nappes eau sout.",
            Category.CLASS,
        ),
        Classification(
            "7112106",
            "Activités de levé géodésique: levé hydrographique, souterrain, de délimitation; cartographie et activités de collecte de données géographiques, y compris par la photographie aérienne, etc.",
            Category.CLASS,
        ),
        Classification("7112107", "Etablissement de prévisions météorologiques", Category.CLASS),
        Classification("71201", "Contrôle technique des véhicules automobiles", Category.CLASS),
        Classification("71209", "Autres activités de contrôle et analyses techniques", Category.CLASS),
        Classification(
            "7120901",
            "Essais et analyses portant sur composition, caractéristiques physiques, performances, conformité à des textes réglementaires et à des normes ou à un cahier des chges de matériaux, pdts, install., etc.",
            Category.CLASS,
        ),
        Classification(
            "7120902",
            "Essais ou analyses en laboratoire visant à la vérification du fonctionnement, du vieillissement ou de la sécurité des installations et matériels",
            Category.CLASS,
        ),
        Classification(
            "7120903",
            "Réalisation de mesures concernant pureté de l'eau ou de l'air, de mesures de radioactivité et d'autres phénomènes analogues, analyse des sources potentielles de la pollution (fumée, eaux usées, etc.)",
            Category.CLASS,
        ),
        Classification("7120904", "Activités d'essais dans le domaine de l'hygiène alimentaire", Category.CLASS),
        Classification("7120905", "Contrôle des calculs des éléments de constructions", Category.CLASS),
        Classification(
            "7120906",
            "Certification des navires, des aéronefs, des véhicules automobiles, des conteneurs sous pression, des installations nucléaires, etc.",
            Category.CLASS,
        ),
        Classification("73110", "Activités des agences de publicité", Category.CLASS),
        Classification(
            "7311001",
            "Conception et réalisation de campagnes publicitaires pour des tiers, en utilisant tous les médias",
            Category.CLASS,
        ),
        Classification(
            "7311002",
            "Création et placement de publicités: affiches, panneaux publicitaires, journaux lumineux, enseignes lumineuses au néon, affichage sur les autobus, etc.",
            Category.CLASS,
        ),
        Classification("7311003", "Conception de textes et de slogans publicitaires (copywriters)", Category.CLASS),
        Classification("7311004", "Conception de films publicitaires", Category.CLASS),
        Classification("7311005", "Conception d'objets publicitaires", Category.CLASS),
        Classification(
            "7311006",
            "Conception de techniques de publicité visant à toucher le consommateur (marketing direct) au moyen de publicité personnalisée (publipostage), propositions téléphoniques d'achat, etc.",
            Category.CLASS,
        ),
        Classification("7311007", "Publicité aérienne", Category.CLASS),
        Classification("73120", "Régie publicitaire de médias", Category.CLASS),
        Classification(
            "7312001",
            "Régies publicitaires de médias pour la vente de temps d'antenne et d'espaces publicitaires",
            Category.CLASS,
        ),
        Classification(
            "7312002",
            "Location d'emplacements à des fins publicitaires sur des panneaux, autour des terrains de sport, dans les halls de gare, etc.",
            Category.CLASS,
        ),
        Classification(
            "7311011",
            "Distribution à domicilie d'échantillons, de prospectus publicitaires et d'autre matériel de publicité, y compris les journaux publicitaires régionaux et similaires",
            Category.CLASS,
        ),
        Classification("74105", "Décoration d'étalage", Category.CLASS),
        Classification("7410501", "Activités d'étalagiste", Category.CLASS),
        Classification("7410502", "Conception de showrooms, etc.", Category.CLASS),
        Classification("78100", "Activités des agences de placement de main-d'oeuvre", Category.CLASS),
        Classification(
            "7810001",
            "Recherche, sélection, orientation et placement de personnel à l'intention de l'employeur ou du demandeur d'emploi: formulation des descriptions de postes; sélection et examen des cand.; vérif. réf.",
            Category.CLASS,
        ),
        Classification(
            "7810002", 'Activités de recherche et de placement de cadres ("chasseurs de têtes")', Category.CLASS
        ),
        Classification(
            "7810003",
            "Placement, pour compte des entreprises, de personnel ayant perdu son travail par suite d'une réorganisation (outplacement)",
            Category.CLASS,
        ),
        Classification(
            "7810004",
            "Services publics pour l'emploi, y compris éventuellement leurs activités de formation professionnelle (Office communautaire et régional de la formation professionnelle et de l'emploi, ORBEM, etc.)",
            Category.CLASS,
        ),
        Classification("78200", "Activités des agences de travail temporaire", Category.CLASS),
        Classification("78300", "Autre mise à disposition de ressources humaines", Category.CLASS),
        Classification("78200", "Agences d'intérimaires", Category.CLASS),
        Classification("7810011", "Agences de mannequins, hôtesses et similaires", Category.CLASS),
        Classification("80100", "Activités de sécurité privée", Category.CLASS),
        Classification("80100", "Entreprise de gardiennage et service de sécurité", Category.CLASS),
        Classification(
            "8010001",
            "Activités de surveillance, de garde et autres activités de protection des personnes ou des biens: gardes du corps, patrouilles urbaines, surveillance d'habitations, bureaux, usines, chantiers, etc.",
            Category.CLASS,
        ),
        Classification(
            "7490901",
            "Activités de conseil en matière de sécurité industrielle de sécurité des ménages et des services publics",
            Category.CLASS,
        ),
        Classification("8010002", "Transport de fonds et d'objets précieux", Category.CLASS),
        Classification("8010003", "Dressage des chiens de garde", Category.CLASS),
        Classification("80300", "Activités d'enquête", Category.CLASS),
        Classification("8030001", "Activités d'enquête", Category.CLASS),
        Classification("8030002", "Activités des détectives privés", Category.CLASS),
        Classification("81220", "Autres activités de nettoyage des bâtiments; nettoyage industriel", Category.CLASS),
        Classification("81210", "Nettoyage courant des bâtiments", Category.CLASS),
        Classification("81290", "Autres activités de nettoyage", Category.CLASS),
        Classification(
            "8122001",
            "Nettoyage intérieur de bâtiments de tous types : bureaux, usines, ateliers, locaux d'institutions et autres locaux à usage commercial ou professionnel, immeubles à appartement, etc.",
            Category.CLASS,
        ),
        Classification("8122002", "Nettoyage des vitres", Category.CLASS),
        Classification(
            "8122003",
            "Ramonage des cheminées et le nettoyage des âtres, des fourneaux, des incinérateurs des chaudières, des gaines de ventilation et des dispositifs d'évacuation de fumées",
            Category.CLASS,
        ),
        Classification(
            "8129001",
            "Activités de désinfection et de destruction des parasites dans les bâtiments, les navires, les trains, etc.",
            Category.CLASS,
        ),
        Classification(
            "8129002",
            "Nettoyage des trains, des autobus, des avions, des navires, etc., y compris les navires pétroliers",
            Category.CLASS,
        ),
        Classification("74201", "Production photographique, sauf activités des photographes de presse", Category.CLASS),
        Classification(
            "7420101",
            "Production photographique réalisée à titre commercial ou privé: photos d'identité, de classe , de mariage, etc.; photogr. publicitaires, d'édition, de mode, à des fins immob. ou touristiques, etc.",
            Category.CLASS,
        ),
        Classification("9609921", "Exploitation de machines automatiques de photographie", Category.CLASS),
        Classification(
            "7420102", "Tournage de reportages vidéo sur des mariages et autres événements similaire", Category.CLASS
        ),
        Classification("74209", "Autres activités photographiques", Category.CLASS),
        Classification(
            "7420901",
            "Traitement des films: développement, tirage et agrandissement de photos ou de films réalisés par les clients; montage de diapositives; copie, restauration et retouche de photographies et de films",
            Category.CLASS,
        ),
        Classification(
            "8292001",
            "Activités de conditionnement (automatique ou non) pour des tiers de produits divers: remplissage d'atomiseurs; embouteillage, remplissage de boîtes de boissons; emballage de denrées aliment., etc.",
            Category.CLASS,
        ),
        Classification("8292002", "Etiquetage, estampillage et scellage", Category.CLASS),
        Classification("8292003", "Emballage de colis et de paquets-cadeaux", Category.CLASS),
        Classification("82200", "Activités des centres d'appels", Category.CLASS),
        Classification("74300", "Traduction et interprétation", Category.CLASS),
        Classification("82110", "Services administratifs combinés de bureau", Category.CLASS),
        Classification("82300", "Organisation de salons professionnels et de congrès", Category.CLASS),
        Classification("74109", "Autres activités spécialisées de design", Category.CLASS),
        Classification(
            "82910",
            "Activités des agences de recouvrement de factures et des sociétés d'information financière sur la clientèle",
            Category.CLASS,
        ),
        Classification("71112", "Activités d'architecture d'intérieur", Category.CLASS),
        Classification("82990", "Autres activités de soutien aux entreprises n.c.a.", Category.CLASS),
        Classification("74101", "Création de modèles pour les biens personnels et domestiques", Category.CLASS),
        Classification("82190", "Secrétariats", Category.CLASS),
        Classification("74103", "Activités de design graphique", Category.CLASS),
        Classification("74104", "Décoration d'intérieur", Category.CLASS),
        Classification("59209", "Autres services d'enregistrements sonores", Category.CLASS),
        Classification("63990", "Autres services d'information n.c.a.", Category.CLASS),
        Classification(
            "77400",
            "Location-bail de propriété intellectuelle et de produits similaires, à l'exception des oeuvres soumises au droit d'auteur",
            Category.CLASS,
        ),
        Classification("84111", "Administration publique fédérale", Category.CLASS),
        Classification("84112", "Administration publique communautaire et régionale", Category.CLASS),
        Classification("84113", "Administration publique provinciale", Category.CLASS),
        Classification(
            "84114",
            "Administration publique communale, sauf Centres Publics d'Action Sociale (C.P.A.S.)",
            Category.CLASS,
        ),
        Classification("84115", "Centres Publics d'Action Sociale (C.P.A.S.)", Category.CLASS),
        Classification("84119", "Autre administration publique générale", Category.CLASS),
        Classification(
            "84120",
            "Administration publique (tutelle) de la santé, de la formation, de la culture et des autres services sociaux, à l'exclusion de la sécurité sociale",
            Category.CLASS,
        ),
        Classification("84130", "Administration publique (tutelle) des activités économiques", Category.CLASS),
        Classification("91012", "Gestion des archives publiques", Category.CLASS),
        Classification("84210", "Affaires étrangères", Category.CLASS),
        Classification("88999", "Autres formes d'action sociale sans hébergement n.c.a.", Category.CLASS),
        Classification("84220", "Défense", Category.CLASS),
        Classification("84231", "Tribunaux", Category.CLASS),
        Classification("84232", "Etablissements pénitentiaires", Category.CLASS),
        Classification("84239", "Autres activités relatives à la justice", Category.CLASS),
        Classification("84249", "Autres activités d'ordre public et de sécurité civile", Category.CLASS),
        Classification("84241", "Police fédérale", Category.CLASS),
        Classification("84242", "Police locale", Category.CLASS),
        Classification("84250", "Services du feu", Category.CLASS),
        Classification("84301", "Sécurité sociale obligatoire, à l'exclusion des mutuelles", Category.CLASS),
        Classification("84302", "Mutuelles et caisses d'assurance soins", Category.CLASS),
        Classification("84309", "Autres organismes de sécurité sociale", Category.CLASS),
        Classification("85201", "Enseignement primaire ordinaire communautaire", Category.CLASS),
        Classification("85101", "Enseignement maternel ordinaire communautaire", Category.CLASS),
        Classification("85105", "Enseignement maternel spécialisé organisé par les pouvoirs publics", Category.CLASS),
        Classification("85205", "Enseignement primaire spécialisé organisé par les pouvoirs publics", Category.CLASS),
        Classification("85202", "Enseignement primaire ordinaire provincial subventionné", Category.CLASS),
        Classification("85102", "Enseignement maternel ordinaire provincial subventionné", Category.CLASS),
        Classification("85203", "Enseignement primaire ordinaire communal subventionné", Category.CLASS),
        Classification("85103", "Enseignement maternel ordinaire communal subventionné", Category.CLASS),
        Classification("85204", "Enseignement primaire ordinaire libre subventionné", Category.CLASS),
        Classification("85104", "Enseignement maternel ordinaire libre subventionné", Category.CLASS),
        Classification("85106", "Enseignement maternel spécialisé libre subventionné", Category.CLASS),
        Classification("85206", "Enseignement primaire spécialisé libre subventionné", Category.CLASS),
        Classification("85209", "Enseignement primaire ordinaire n.c.a.", Category.CLASS),
        Classification("85109", "Enseignement maternel n.c.a.", Category.CLASS),
        Classification("85311", "Enseignement secondaire général ordinaire communautaire", Category.CLASS),
        Classification("85325", "Enseignement secondaire spécialisé organisé par les pouvoirs publics", Category.CLASS),
        Classification("85312", "Enseignement secondaire général ordinaire provincial subventionné", Category.CLASS),
        Classification("85313", "Enseignement secondaire général ordinaire communal subventionné", Category.CLASS),
        Classification("85314", "Enseignement secondaire général ordinaire libre subventionné", Category.CLASS),
        Classification("85326", "Enseignement secondaire spécialisé libre subventionné", Category.CLASS),
        Classification("85319", "Enseignement secondaire ordinaire général n.c.a.", Category.CLASS),
        Classification(
            "85321", "Enseignement secondaire technique et professionnel ordinaire communautaire", Category.CLASS
        ),
        Classification(
            "85322",
            "Enseignement secondaire technique et professionnel ordinaire provincial subventionné",
            Category.CLASS,
        ),
        Classification(
            "85323",
            "Enseignement secondaire technique et professionnel ordinaire communal subventionné",
            Category.CLASS,
        ),
        Classification(
            "85324", "Enseignement secondaire technique et professionnel ordinaire libre subventionné", Category.CLASS
        ),
        Classification("85421", "Enseignement supérieur organisé par les pouvoirs publics", Category.CLASS),
        Classification("85410", "Enseignement post-secondaire non supérieur", Category.CLASS),
        Classification("85422", "Enseignement supérieur libre subventionné", Category.CLASS),
        Classification("85429", "Enseignement supérieur n.c.a.", Category.CLASS),
        Classification("85531", "Enseignement de la conduite de véhicules à moteurs", Category.CLASS),
        Classification("8553101", "Auto-écoles", Category.CLASS),
        Classification("8553102", "Moto-écoles", Category.CLASS),
        Classification("85532", "Enseignement de la conduite d'aéronefs et de bateaux", Category.CLASS),
        Classification("8553201", "Préparation au certificat de pilotage d'avions de tourisme", Category.CLASS),
        Classification("8553202", "Formation aux permis bateaux à voiles et bateaux de plaisance", Category.CLASS),
        Classification("85592", "Formation professionnelle", Category.CLASS),
        Classification("85207", "Alphabétisation des adultes", Category.CLASS),
        Classification("85591", "Enseignement de promotion sociale", Category.CLASS),
        Classification("85520", "Enseignement culturel", Category.CLASS),
        Classification("85599", "Autres formes d'enseignement", Category.CLASS),
        Classification("85593", "Formation socio-culturelle", Category.CLASS),
        Classification("85609", "Autres services de soutien à l'enseignement", Category.CLASS),
        Classification(
            "86101", "Activités des hôpitaux généraux, sauf hôpitaux gériatriques et spécialisés", Category.CLASS
        ),
        Classification("86102", "Activités des hôpitaux gériatriques", Category.CLASS),
        Classification("86103", "Activités des hôpitaux spécialisés", Category.CLASS),
        Classification("86104", "Activités des hôpitaux psychiatriques", Category.CLASS),
        Classification("86109", "Autres activités hospitalières", Category.CLASS),
        Classification("86220", "Activités des médecins spécialistes", Category.CLASS),
        Classification("86210", "Activités des médecins généralistes", Category.CLASS),
        Classification("86230", "Pratique dentaire", Category.CLASS),
        Classification("86901", "Activités des laboratoires médicaux", Category.CLASS),
        Classification("86903", "Transport par ambulance", Category.CLASS),
        Classification("86909", "Autres activités pour la santé humaine n.c.a.", Category.CLASS),
        Classification(
            "86904",
            "Activités relatives à la santé mentale, sauf hôpitaux et maisons de soins psychiatriques",
            Category.CLASS,
        ),
        Classification("86905", "Activités de revalidation ambulatoire", Category.CLASS),
        Classification("86906", "Activités des praticiens de l'art infirmier", Category.CLASS),
        Classification("86907", "Activités des sages-femmes", Category.CLASS),
        Classification(
            "86902", "Activités des centres de collecte de sang, des banques de sang et d'organes", Category.CLASS
        ),
        Classification("75000", "Activités vétérinaires", Category.CLASS),
        Classification("87201", "Activités de soins résidentiels pour mineurs avec un handicap mental", Category.CLASS),
        Classification(
            "87209",
            "Autres activités de soins résidentiels pour personnes avec un handicap mental, un problème psychiatrique ou toxicodépendantes",
            Category.CLASS,
        ),
        Classification("87303", "Activités de soins résidentiels pour mineurs avec un handicap moteur", Category.CLASS),
        Classification(
            "87309",
            "Autres activités de soins résidentiels pour personnes âgées ou avec un handicap moteur",
            Category.CLASS,
        ),
        Classification("87901", "Services d'aide à la jeunesse avec hébergement", Category.CLASS),
        Classification("87202", "Activités de soins résidentiels pour adultes avec un handicap mental", Category.CLASS),
        Classification("87304", "Activités de soins résidentiels pour adultes avec un handicap moteur", Category.CLASS),
        Classification("87301", "Activités des maisons de repos pour personnes âgées (M.R.P.A.)", Category.CLASS),
        Classification("87101", "Activités des maisons de repos et de soins (M.R.S.)", Category.CLASS),
        Classification("87302", "Activités des résidences services pour personnes âgées", Category.CLASS),
        Classification("87909", "Autres activités de soins résidentiels n.c.a.", Category.CLASS),
        Classification("87109", "Autres activités de soins infirmiers résidentiels", Category.CLASS),
        Classification(
            "87203", "Activités de soins résidentiels pour personnes avec un problème psychiatrique", Category.CLASS
        ),
        Classification("87204", "Activités de soins résidentiels pour personnes toxicodépendantes", Category.CLASS),
        Classification(
            "87205", "Activités des habitations protégées pour personnes avec un problème psychiatrique", Category.CLASS
        ),
        Classification("87902", "Services sociaux généraux avec hébergement", Category.CLASS),
        Classification("88911", "Activités des crèches et des garderies d'enfants", Category.CLASS),
        Classification("88912", "Activités des gardiennes d'enfants", Category.CLASS),
        Classification("88919", "Autre action sociale sans hébergement pour jeunes enfants", Category.CLASS),
        Classification("8891101", "Crèches et garderies d'enfants", Category.CLASS),
        Classification("88995", "Activités des entreprises de travail adapté", Category.CLASS),
        Classification(
            "88104",
            "Activités des centres de jour pour adultes avec un handicap moteur, y compris les services ambulatoires",
            Category.CLASS,
        ),
        Classification(
            "88109",
            "Autre action sociale sans hébergement pour personnes âgées et pour personnes avec un handicap moteur",
            Category.CLASS,
        ),
        Classification(
            "88992",
            "Activités des centres de jour pour adultes avec un handicap mental, y compris les services ambulatoires",
            Category.CLASS,
        ),
        Classification("85601", "Activités des Centres Psycho-Médico-Sociaux (P.M.S.)", Category.CLASS),
        Classification("88101", "Activités des aides familiales à domicile, sauf soins à domicile", Category.CLASS),
        Classification("88102", "Activités des centres de jour et de services pour personnes âgées", Category.CLASS),
        Classification(
            "88103",
            "Activités des centres de jour pour mineurs avec un handicap moteur, y compris les services ambulatoires",
            Category.CLASS,
        ),
        Classification(
            "88991",
            "Activités des centres de jour pour mineurs avec un handicap mental, y compris les services ambulatoires",
            Category.CLASS,
        ),
        Classification("88993", "Action sociale ambulatoire pour personnes toxicodépendantes", Category.CLASS),
        Classification("88994", "Services d'aide à la jeunesse sans hébergement", Category.CLASS),
        Classification("88996", "Services sociaux généraux sans hébergement", Category.CLASS),
        Classification("37000", "Collecte et traitement des eaux usées", Category.CLASS),
        Classification(
            "38213",
            "Traitement et élimination des déchets non dangereux, sauf boues et déchets liquides",
            Category.CLASS,
        ),
        Classification("38110", "Collecte des déchets non dangereux", Category.CLASS),
        Classification("39000", "Dépollution et autres services de gestion des déchets", Category.CLASS),
        Classification("38219", "Autre traitement et élimination des déchets non dangereux", Category.CLASS),
        Classification("37000", "", Category.CLASS),
        Classification("94110", "Activités des organisations patronales et économiques", Category.CLASS),
        Classification("94120", "Activités des organisations professionnelles", Category.CLASS),
        Classification("94200", "Activités des syndicats de salariés", Category.CLASS),
        Classification("94910", "Activités des organisations religieuses et philosophiques", Category.CLASS),
        Classification("94910", "Activités des organisations religieuses et philisophiques", Category.CLASS),
        Classification("94920", "Activités des organisations politiques", Category.CLASS),
        Classification("94991", "Associations de jeunesse", Category.CLASS),
        Classification("94992", "Associations et mouvements pour adultes", Category.CLASS),
        Classification("94993", "Associations pour la prévention de la santé", Category.CLASS),
        Classification("94994", "Associations pour l'environnement et la mobilité", Category.CLASS),
        Classification("94995", "Associations pour la coopération au développement", Category.CLASS),
        Classification("59111", "Production de films cinématographiques", Category.CLASS),
        Classification(
            "5911101",
            "Production et réalisation de films d'auteurs, courts ou longs métrages, destinés principalement à la projection dans les salles",
            Category.CLASS,
        ),
        Classification("59112", "Production de films pour la télévision", Category.CLASS),
        Classification(
            "5911201",
            "Production et réalisation de films de tous types (séries, téléfilms, documentaires, etc.) destinés à la diffusion télévisuelle",
            Category.CLASS,
        ),
        Classification(
            "59113", "Production de films autres que cinématographiques et pour la télévision", Category.CLASS
        ),
        Classification(
            "5911301",
            "Production et réalisation de films publicitaires et films promotionnels, films techniques et d'entreprise, films à caractère éducatif ou de formation, clips vidéo",
            Category.CLASS,
        ),
        Classification(
            "5911302", "Production et réalisation de dessins animés par des laboratoires spécialisés", Category.CLASS
        ),
        Classification(
            "59120",
            "Post-production de films cinématographiques, de vidéo et de programmes de télévision",
            Category.CLASS,
        ),
        Classification("59202", "Studios d'enregistrements sonores", Category.CLASS),
        Classification(
            "5912001",
            "Activités connexes à la production de films exercées pour le compte de tiers : postsynchronisation, effets spéciaux, développement, montage, coloriage, doublage, sous-titrage, etc.",
            Category.CLASS,
        ),
        Classification(
            "5912002",
            "Activités des studios de cinéma, y compris la mise à disposition de matériel technique",
            Category.CLASS,
        ),
        Classification(
            "59130", "Distribution de films cinématographiques, de vidéo et de programmes de télévision", Category.CLASS
        ),
        Classification(
            "5913001",
            "Distribution (vente ou location) de films cinématographiques et de bandes de vidéo à d'autres unités, mais non au public général",
            Category.CLASS,
        ),
        Classification(
            "5913002",
            "Activités liées à la distribution telles que la réservation, la livraison et la conservation de films",
            Category.CLASS,
        ),
        Classification(
            "5913003",
            "Edition et distribution de films de tous types sur bandes vidéo à destination du public",
            Category.CLASS,
        ),
        Classification(
            "5913004",
            "Gestion de droits cinématographiques et audiovisuels d'oeuvres réalisées par des tiers",
            Category.CLASS,
        ),
        Classification("59140", "Projection de films cinématographiques", Category.CLASS),
        Classification(
            "5914001",
            "Projection de films cinématographiques ou de bandes de vidéo dans des salles de cinéma, en plein air ou dans d'autres installations de projection",
            Category.CLASS,
        ),
        Classification("5914002", "Activités des ciné-clubs", Category.CLASS),
        Classification("59201", "Production d'enregistrements sonores", Category.CLASS),
        Classification(
            "6010001",
            "Production de programmes de radio, que cette production soit combinée ou non avec des activités de diffusion",
            Category.CLASS,
        ),
        Classification("6010002", "Activités des radios locales et des radios libres", Category.CLASS),
        Classification("59114", "Production de programmes pour la télévision", Category.CLASS),
        Classification(
            "5911401", "Production de programmes de télévision non diffusés par leur producteur", Category.CLASS
        ),
        Classification("5911402", "Activités des maisons de production indépendantes", Category.CLASS),
        Classification(
            "6020001",
            "Emission de programmes de télévision par des chaînes subventionnées ou par des chaînes appartenant au secteur privé, que cette émission soit combinée ou non avec des activités de production",
            Category.CLASS,
        ),
        Classification(
            "6020002",
            "Activités dans la domaine da la production et de l'émission de programmes de télévision exercées par: les chaînes régionales et locales, les chaînes payantes",
            Category.CLASS,
        ),
        Classification("59114", "Production de programmes de télévision", Category.CLASS),
        Classification("90011", "Réalisation de spectacles par des artistes indépendants", Category.CLASS),
        Classification("90029", "Autres activités de soutien au spectacle vivant", Category.CLASS),
        Classification("90031", "Création artistique, sauf activités de soutien", Category.CLASS),
        Classification("90012", "Réalisation de spectacles par des ensembles artistiques", Category.CLASS),
        Classification("90023", "Services spécialisés du son, de l'image et de l'éclairage", Category.CLASS),
        Classification("90021", "Promotion et organisation de spectacles vivants", Category.CLASS),
        Classification("90022", "Conception et réalisation de décors", Category.CLASS),
        Classification("90032", "Activités de soutien à la création artistique", Category.CLASS),
        Classification("90041", "Gestion de salles de théâtre, de concerts et similaires", Category.CLASS),
        Classification(
            "9004101",
            "Exploitation de salles de concert, de théâtre,music-halls, cabarets et autres salles de spectacles",
            Category.CLASS,
        ),
        Classification(
            "7990901", "Exploitation d'agences de vente de billets et de réservations de places", Category.CLASS
        ),
        Classification(
            "9004102", "Exploitation de studios d'enregistrements sonores pour compte de tiers", Category.CLASS
        ),
        Classification(
            "90042",
            "Gestion de centres culturels et de salles multifonctionnelles à vocation culturelle",
            Category.CLASS,
        ),
        Classification("9004201", "Gestion et exploitation de centres culturels", Category.CLASS),
        Classification(
            "9004202",
            "Gestion et exploitation de centres polyvalents, principalement destinés à des activités dans le domaine de l'art dramatique et de la musique",
            Category.CLASS,
        ),
        Classification("93211", "Activités foraines", Category.CLASS),
        Classification("9321101", "Attractions foraines", Category.CLASS),
        Classification("93212", "Activités des parcs d'attractions et des parcs à thèmes", Category.CLASS),
        Classification("9321201", "Exploitation de parcs d'attractions", Category.CLASS),
        Classification("93299", "Autres activités récréatives et de loisirs n.c.a.", Category.CLASS),
        Classification(
            "8552001", "Exploitation d'écoles de danse et les activités des professeurs de danse", Category.CLASS
        ),
        Classification(
            "9329901",
            'Organisation d\'activités récréatives n.d.a.: spectacles de cirque, spectacles de marionnettes, rodéos, spectacles "son et lumière", etc.',
            Category.CLASS,
        ),
        Classification("63910", "Activités des agences de presse", Category.CLASS),
        Classification("74202", "Activités des photographes de presse", Category.CLASS),
        Classification(
            "6391001",
            "Activités des agences de presse, c'est-à-dire la communication aux médias d'informations, de photos",
            Category.CLASS,
        ),
        Classification("7420201", "Activités des photographes de presse indépendants", Category.CLASS),
        Classification("91011", "Gestion des bibliothèques, des médiathèques et des ludothèques", Category.CLASS),
        Classification("9101101", "Recherche et gestion de collections d'ouvrages spécialisés ou non", Category.CLASS),
        Classification("9101201", "Tenue des archives historiques", Category.CLASS),
        Classification("9101102", "Etablissement de catalogues", Category.CLASS),
        Classification(
            "9101103",
            "Prêt à stockage de livres, de cartes, de périodiques, de films, de disques, de bandes magnétiques, d'oeuvres d'art, etc.",
            Category.CLASS,
        ),
        Classification(
            "9101104", "Activités de recherche visant à répondre aux demandes d'information", Category.CLASS
        ),
        Classification(
            "91030",
            "Gestion des sites et monuments historiques et des attractions touristiques similaires",
            Category.CLASS,
        ),
        Classification("91020", "Gestion des musées", Category.CLASS),
        Classification(
            "9103001", "Préservation de sites (y compris les fouilles) et de bâtiments historiques", Category.CLASS
        ),
        Classification("9103002", "Conservation de monuments historiques", Category.CLASS),
        Classification(
            "9102001",
            "Gestion des musées, y compris les musées en plein air: musées d'art, d'orfèvrerie, de meubles, de costumes, de céramiques, d'argenterie, etc.; musées d'histoire naturelle, des sc. et techniques, etc.",
            Category.CLASS,
        ),
        Classification("91042", "Gestion et conservation des sites naturels", Category.CLASS),
        Classification("91041", "Gestion des jardins botaniques et zoologiques", Category.CLASS),
        Classification("9104201", "Conservation du patrimoine naturel", Category.CLASS),
        Classification(
            "9104101",
            "Gestion de jardins botaniques et zoologiques, des zoos pour enfants, des réserves et parcs naturels, y compris la protection de la flore et de la faune",
            Category.CLASS,
        ),
        Classification(
            "9104202", "Exploitation d'autres curiosités touristiques (grottes et similaires)", Category.CLASS
        ),
        Classification("93110", "Gestion d'installations sportives", Category.CLASS),
        Classification(
            "9311001",
            "Gestion et exploitation de centres sportifs destinés à accueillir des événements ou des disciplines sportifs de toute nature",
            Category.CLASS,
        ),
        Classification(
            "9311002",
            "Gestion et exploitation de centres polyvalents, principalement destinés à la pratique du sport",
            Category.CLASS,
        ),
        Classification("93130", "Activités des centres de culture physique", Category.CLASS),
        Classification(
            "9313001",
            "Exploitation de salles de gymnastique et de centres de fitness, de musculation, d'aérobic, de body-building, etc., y compris l'accompagnement de la clientèle sur le plan sportif",
            Category.CLASS,
        ),
        Classification(
            "9311011",
            "Exploitation de stades de football, piscines, stades d'athlétisme, établissements de bowling, terrains de golf, courts de tennis, patinoires, stands de tir, salles et arènes spécialisées, etc.",
            Category.CLASS,
        ),
        Classification("9311012", "Exploitation d'aérodromes de tourisme", Category.CLASS),
        Classification("9311013", "Exploitation de viviers, hippodromes et manèges", Category.CLASS),
        Classification("9311014", "Exploitation de circuits automobiles, vélodromes, etc.", Category.CLASS),
        Classification("93121", "Activités de clubs de football", Category.CLASS),
        Classification("93122", "Activités de clubs de tennis", Category.CLASS),
        Classification("93123", "Activités de clubs d'autres sports de ballon", Category.CLASS),
        Classification("93124", "Activités de clubs cyclistes", Category.CLASS),
        Classification("93125", "Activités de clubs de sports de combat", Category.CLASS),
        Classification("93126", "Activités de clubs de sports nautiques", Category.CLASS),
        Classification("93127", "Activités de clubs équestres", Category.CLASS),
        Classification("93128", "Activités de clubs d'athlétisme", Category.CLASS),
        Classification("93129", "Activités de clubs d'autres sports", Category.CLASS),
        Classification("93191", "Activités des ligues et des fédérations sportives", Category.CLASS),
        Classification(
            "9311021",
            "Organisation et gestion d'activités sportives: clubs de foot., de cyclisme, de bowling, de natation, de golf, de boxe, de lutte et autres arts martiaux, de musculation, assoc. de sports d'hiver, etc.",
            Category.CLASS,
        ),
        Classification(
            "9312901",
            "Activités liées aux courses et concours d'animaux (cheveux, lévriers, pigeons, etc.)",
            Category.CLASS,
        ),
        Classification(
            "9312902", "Activités liées aux sport mécaniques (automobiles, motos, karts, etc.)", Category.CLASS
        ),
        Classification(
            "9312903", "Pratique de la chasse et de la pêche en tant que sports ou activités de loisir", Category.CLASS
        ),
        Classification(
            "9312904",
            "Activités liées aux régates, ski nautique, jetski, deltaplane, vol à voile, vol en ULM, en avion de tourisme ou de sport, etc.",
            Category.CLASS,
        ),
        Classification("85510", "Enseignement de disciplines sportives et d'activités de loisirs", Category.CLASS),
        Classification("93192", "Activités des sportifs indépendants", Category.CLASS),
        Classification("93199", "Autres activités sportives n.c.a.", Category.CLASS),
        Classification(
            "9319901",
            "Promotion et organisation d'événements sportifs tant pour compte propre que pour le compte de tiers",
            Category.CLASS,
        ),
        Classification("9319902", "Activités de services connexes", Category.CLASS),
        Classification("92000", "Organisation de jeux de hasard et d'argent", Category.CLASS),
        Classification("9200001", "Organisation de loteries, lotos, pronostics,paris mutuels, etc.", Category.CLASS),
        Classification("9200002", "Exploitation de casinos et de salles de jeux", Category.CLASS),
        Classification(
            "9200003", "Exploitation de machines à sous basées sur le hasard avec gain d'argent", Category.CLASS
        ),
        Classification(
            "9200004",
            "Activités liées à la vente de billets de loterie, la distribution et la collecte de bulletins de participation, etc.",
            Category.CLASS,
        ),
        Classification("93291", "Exploitation de salles de billard et de snooker", Category.CLASS),
        Classification("9329101", "Exploitation de salles de billards", Category.CLASS),
        Classification("93292", "Exploitation de domaines récréatifs", Category.CLASS),
        Classification(
            "9329201",
            "Exploitation de jeux, automatiques ou non (flippers, jeux électroniques, baby foot, etc.) en principe sans gain d'argent",
            Category.CLASS,
        ),
        Classification(
            "9329911",
            "Exploitation d'infrastructures de plage (location de cabines de bain, paravents, sièges, etc.)",
            Category.CLASS,
        ),
        Classification(
            "9329912",
            "Mise à disposition à des fins récréatives de pédalos, barques, bicyclettes, poneys, etc.",
            Category.CLASS,
        ),
        Classification(
            "7810021",
            "Engagement et placement d'acteurs pour les films cinématographiques, les émissions de télévision et les pièces de théâtre",
            Category.CLASS,
        ),
        Classification("9329921", "Autres activités liées aux loisirs non classées ailleurs", Category.CLASS),
        Classification("96011", "Activités des blanchisseries industrielles", Category.CLASS),
        Classification(
            "9601101",
            "Lavage, blanchissage, nettoyage à sec, repassage, teinture, etc., des habits et textiles pour le compte d'entreprises, utilisateurs professionels ou exploitants de magasins-dépôts",
            Category.CLASS,
        ),
        Classification("9601102", "Ramassage et livraison du linge", Category.CLASS),
        Classification("9601103", "Nettoyage d'articles en cuir ou en fourrure", Category.CLASS),
        Classification("9601104", "Nettoyage des tapis, des moquettes, des tentures et des rideaux", Category.CLASS),
        Classification(
            "9529011",
            "Réparation de vêtements et d'autres articles textiles ou les petites retouches apportées à ces articles lorsqu'elles sont faites en liaison avec le nettoyage",
            Category.CLASS,
        ),
        Classification(
            "9601105",
            "Location, par les blanchisseries, de linge, de vêtements de travail et d'articles similaires",
            Category.CLASS,
        ),
        Classification("96012", "Activités des blanchisseries et des salons-lavoirs pour particuliers", Category.CLASS),
        Classification("9601201", "Service des laveries automatiques en libre service", Category.CLASS),
        Classification(
            "9601202",
            "Traitement (ramassage, lavage, repassage, livraison à domicile, etc.) du linge à une échelle non industrielle et nettoyage d'articles d'habillement pour le compte de particuliers",
            Category.CLASS,
        ),
        Classification(
            "9601211",
            "Exploitants de magasins-dépôts qui n'exercent aucune activité ayant trait au lavage ou nettoyage mais qui confient le traitement du linge et le nettoyage des vêtements aux laveries et blanch. indust.",
            Category.CLASS,
        ),
        Classification("96021", "Coiffure", Category.CLASS),
        Classification(
            "9602101",
            "Coiffure pour hommes, femmes et enfants (coupe, shampooing, soins capillaires, coloration, ondulation, etc.)",
            Category.CLASS,
        ),
        Classification("96022", "Soins de beauté", Category.CLASS),
        Classification(
            "9602201",
            "Conseils en beauté et soins du visage: massages fasciaux, traitement anti-rides, maquillage, etc.",
            Category.CLASS,
        ),
        Classification("9602202", "Soins de la peau et épilation", Category.CLASS),
        Classification("9602203", "Soins de manucure et de pédicure", Category.CLASS),
        Classification("96031", "Soins funéraires", Category.CLASS),
        Classification(
            "9603101",
            "Soins aux défunts: la préparation des corps pour la sépulture ou l'incinération, l'embaumement, etc.",
            Category.CLASS,
        ),
        Classification(
            "9603102",
            "Services connexes à l'inhumation et l'incinération: la location de locaux aménagés dans les funérariums, etc.",
            Category.CLASS,
        ),
        Classification("9603103", "Services d'inhumation et d'incinération des défunts", Category.CLASS),
        Classification("9603104", "Services funéraires aux animaux", Category.CLASS),
        Classification("96032", "Gestion des cimetières et services des crématoriums", Category.CLASS),
        Classification("9603201", "Location ou vente de concessions", Category.CLASS),
        Classification("9603202", "Gestion et entretien des cimetières", Category.CLASS),
        Classification(
            "9603203",
            "Services fournis par les crématoriums (incinération, dispersion des cendres, columbarium, etc.)",
            Category.CLASS,
        ),
        Classification("96040", "Entretien corporel", Category.CLASS),
        Classification(
            "9604001",
            "Services liés au bien-être et confort physique fournis dans les établissements de thalassothérapie, stations thermales, bains turcs, saunas, bains de vapeur, solariums, salons de massages, etc.",
            Category.CLASS,
        ),
        Classification("96091", "Services de rencontres", Category.CLASS),
        Classification(
            "9609101", "Agences matrimoniales, agences de rencontres, services d'escorte et similaires", Category.CLASS
        ),
        Classification("9609901", "Graphologues, astrologues, voyants, radiesthésistes et similaires", Category.CLASS),
        Classification("96092", "Services de tatouage et de piercing", Category.CLASS),
        Classification("96093", "Services de soins pour animaux de compagnie, sauf soins vétérinaires", Category.CLASS),
        Classification("96094", "Activités de dressage pour animaux de compagnie", Category.CLASS),
        Classification("96095", "Hébergement d'animaux de compagnie", Category.CLASS),
        Classification("9609911", "Services de recherche généalogique", Category.CLASS),
        Classification("9609201", "Services de tatouement", Category.CLASS),
        Classification(
            "9609912",
            "Concessions diverses, notamment sur la voie publique cireurs, porteurs, etc.) ou à l'intérieur des bâtiments accessibles au public (vestiaires, toilettes, etc.)",
            Category.CLASS,
        ),
        Classification(
            "9609401", "Dressage et entraînement d'animaux de compagnie et de chiens d'aveugles", Category.CLASS
        ),
        Classification("97000", "Activités des ménages en tant qu'employeurs de personnel domestique", Category.CLASS),
        Classification(
            "98100",
            "Activités indifférenciées des ménages en tant que producteurs de biens pour usage propre",
            Category.CLASS,
        ),
        Classification(
            "98200",
            "Activités indifférenciées des ménages en tant que producteurs de services pour usage propre",
            Category.CLASS,
        ),
        Classification("99000", "Activités des organisations et organismes extraterritoriaux", Category.CLASS),
    ],
)
