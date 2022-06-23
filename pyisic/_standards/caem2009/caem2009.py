"""`CAEM2009 (CAEM Rev. 2) Standard <https://date.gov.md/ckan/ro/dataset/5188-clasificatorul-activitatilor-din-economia-moldovei-caem>`_."""

from ...types import Category, Classification, Standard, Standards

CAEM2009 = Standard(
    standard=Standards.CAEM2009,
    classes=[
        Classification("A", "AGRICULTURĂ, SILVICULTURĂ ŞI PESCUIT", Category.SECTION),
        Classification("01", "Agricultură, vânătoare şi servicii anexe", Category.DIVISION),
        Classification("01.1", "Cultivarea plantelor din culturi nepermanente", Category.GROUP),
        Classification(
            "01.11",
            "Cultivarea cerealelor (exclusiv orez), plantelor leguminoase şi a plantelor producătoare de seminţe oleaginoase",
            Category.CLASS,
        ),
        Classification("01.12", "Cultivarea orezului", Category.CLASS),
        Classification(
            "01.13", "Cultivarea legumelor şi a pepenilor, a rădăcinoaselor şi tuberculilor", Category.CLASS
        ),
        Classification("01.14", "Cultivarea trestiei de zahăr", Category.CLASS),
        Classification("01.15", "Cultivarea tutunului", Category.CLASS),
        Classification("01.16", "Cultivarea plantelor pentru fibre textile", Category.CLASS),
        Classification("01.19", "Cultivarea altor plante din culturi nepermanente", Category.CLASS),
        Classification("01.2", "Cultivarea plantelor din culturi permanente", Category.GROUP),
        Classification("01.21", "Cultivarea strugurilor", Category.CLASS),
        Classification("01.22", "Cultivarea fructelor tropicale şi subtropicale", Category.CLASS),
        Classification("01.23", "Cultivarea fructelor citrice", Category.CLASS),
        Classification("01.24", "Cultivarea fructelor seminţoase şi sâmburoase", Category.CLASS),
        Classification(
            "01.25",
            "Cultivarea arbuştilor fructiferi, căpşunilor, nuciferilor şi a altor pomi fructiferi",
            Category.CLASS,
        ),
        Classification("01.26", "Cultivarea fructelor oleaginoase", Category.CLASS),
        Classification("01.27", "Cultivarea plantelor pentru prepararea băuturilor", Category.CLASS),
        Classification(
            "01.28",
            "Cultivarea condimentelor, plantelor aromatice, medicinale şi a plantelor de uz farmaceutic",
            Category.CLASS,
        ),
        Classification("01.29", "Cultivarea altor plante din culturi permanente", Category.CLASS),
        Classification("01.3", "Cultivarea plantelor pentru înmulţire", Category.GROUP),
        Classification("01.30", "Cultivarea plantelor pentru înmulţire", Category.CLASS),
        Classification("01.4", "Creşterea animalelor", Category.GROUP),
        Classification("01.41", "Creşterea bovinelor de lapte", Category.CLASS),
        Classification("01.42", "Creşterea altor bovine", Category.CLASS),
        Classification("01.43", "Creşterea cailor şi a altor cabaline", Category.CLASS),
        Classification("01.44", "Creşterea cămilelor şi a camelidelor", Category.CLASS),
        Classification("01.45", "Creşterea ovinelor şi caprinelor", Category.CLASS),
        Classification("01.46", "Creşterea porcinelor", Category.CLASS),
        Classification("01.47", "Creşterea păsărilor", Category.CLASS),
        Classification("01.49", "Creşterea altor specii de animale", Category.CLASS),
        Classification(
            "01.5", "Activităţi în ferme mixte (cultura vegetală combinată cu creşterea animalelor)", Category.GROUP
        ),
        Classification(
            "01.50", "Activităţi în ferme mixte (cultura vegetală combinată cu creşterea animalelor)", Category.CLASS
        ),
        Classification("01.6", "Activităţi auxiliare agriculturii şi activităţi după recoltare", Category.GROUP),
        Classification("01.61", "Activităţi auxiliare pentru producţia vegetală", Category.CLASS),
        Classification("01.62", "Activităţi auxiliare pentru creşterea animalelor", Category.CLASS),
        Classification("01.63", "Activităţi după recoltare", Category.CLASS),
        Classification("01.64", "Pregătirea seminţelor în vederea însămînţării", Category.CLASS),
        Classification(
            "01.7",
            "Vânătoare, capturarea cu capcane a vânatului şi activităţi de servicii anexe vânătorii",
            Category.GROUP,
        ),
        Classification(
            "01.70",
            "Vânătoare, capturarea cu capcane a vânatului şi activităţi de servicii anexe vânătorii",
            Category.CLASS,
        ),
        Classification("02", "Silvicultură şi exploatare forestieră", Category.DIVISION),
        Classification("02.1", "Silvicultură şi alte activităţi forestiere", Category.GROUP),
        Classification("02.10", "Silvicultură şi alte activităţi forestiere", Category.CLASS),
        Classification("02.2", "Exploatarea forestieră", Category.GROUP),
        Classification("02.20", "Exploatarea forestieră", Category.CLASS),
        Classification("02.3", "Colectarea produselor forestiere nelemnoase din flora spontană", Category.GROUP),
        Classification("02.30", "Colectarea produselor forestiere nelemnoase din flora spontană", Category.CLASS),
        Classification("02.4", "Activităţi de servicii anexe silviculturii", Category.GROUP),
        Classification("02.40", "Activităţi de servicii anexe silviculturii", Category.CLASS),
        Classification("03", "Pescuitul şi acvacultura", Category.DIVISION),
        Classification("03.1", "Pescuitul", Category.GROUP),
        Classification("03.11", "Pescuitul maritim", Category.CLASS),
        Classification("03.12", "Pescuitul în ape dulci", Category.CLASS),
        Classification("03.2", "Acvacultura", Category.GROUP),
        Classification("03.21", "Acvacultura  maritimă", Category.CLASS),
        Classification("03.22", "Acvacultura în ape dulci", Category.CLASS),
        Classification("B", "INDUSTRIA EXTRACTIVĂ", Category.SECTION),
        Classification("05", "Extracţia cărbunelui superior şi inferior", Category.DIVISION),
        Classification("05.1", "Extracţia cărbunelui superior (PCS=>23865 kJ/kg)", Category.GROUP),
        Classification("05.10", "Extracţia cărbunelui superior (PCS=>23865 kJ/kg)", Category.CLASS),
        Classification("05.2", "Extracţia cărbunelui inferior (PCS<23865 kJ/kg)", Category.GROUP),
        Classification("05.20", "Extracţia cărbunelui inferior (PCS<23865 kJ/kg)", Category.CLASS),
        Classification("06", "Extracţia petrolului brut şi a gazelor naturale", Category.DIVISION),
        Classification("06.1", "Extracţia petrolului brut", Category.GROUP),
        Classification("06.10", "Extracţia petrolului brut", Category.CLASS),
        Classification("06.2", "Extracţia gazelor naturale", Category.GROUP),
        Classification("06.20", "Extracţia gazelor naturale", Category.CLASS),
        Classification("07", "Extracţia minereurilor metalifere", Category.DIVISION),
        Classification("07.1", "Extracţia minereurilor feroase", Category.GROUP),
        Classification("07.10", "Extracţia minereurilor feroase", Category.CLASS),
        Classification("07.2", "Extracţia minereurilor metalifere neferoase", Category.GROUP),
        Classification("07.21", "Extracţia minereurilor de uraniu şi toriu", Category.CLASS),
        Classification("07.29", "Extracţia altor minereuri metalifere neferoase", Category.CLASS),
        Classification("08", "Alte activităţi extractive", Category.DIVISION),
        Classification("08.1", "Extracţia pietrei, nisipului şi argilei", Category.GROUP),
        Classification(
            "08.11",
            "Extracţia pietrei ornamentale şi a pietrei pentru construcţii; extracţia pietrei calcaroase, ghipsului, cretei şi a ardeziei",
            Category.CLASS,
        ),
        Classification("08.12", "Extracţia pietrişului şi nisipului; extracţia argilei şi caolinului", Category.CLASS),
        Classification("08.9", "Alte activităţi extractive n.c.a.", Category.GROUP),
        Classification(
            "08.91", "Extracţia mineralelor pentru industria chimică şi a îngrăşămintelor naturale", Category.CLASS
        ),
        Classification("08.92", "Extracţia şi aglomerarea turbei", Category.CLASS),
        Classification("08.93", "Extracţia sării", Category.CLASS),
        Classification("08.99", "Alte activităţi extractive n.c.a.", Category.CLASS),
        Classification("09", "Activităţi de servicii anexe extracţiei", Category.DIVISION),
        Classification(
            "09.1", "Activităţi de servicii anexe extracţiei petrolului brut şi gazelor naturale", Category.GROUP
        ),
        Classification(
            "09.10", "Activităţi de servicii anexe extracţiei petrolului brut şi gazelor naturale", Category.CLASS
        ),
        Classification("09.9", "Activităţi de servicii anexe pentru extracţia altor minerale", Category.GROUP),
        Classification("09.90", "Activităţi de servicii anexe pentru extracţia altor minerale", Category.CLASS),
        Classification("C", "INDUSTRIA PRELUCRĂTOARE", Category.SECTION),
        Classification("10", "Industria alimentară", Category.DIVISION),
        Classification(
            "10.1", "Producţia, prelucrarea şi conservarea cărnii şi a produselor din carne", Category.GROUP
        ),
        Classification("10.11", "Producţia, prelucrarea şi conservarea cărnii", Category.CLASS),
        Classification("10.12", "Prelucrarea şi conservarea cărnii de pasăre", Category.CLASS),
        Classification("10.13", "Fabricarea produselor din carne (inclusiv din carne de pasăre)", Category.CLASS),
        Classification("10.2", "Prelucrarea şi conservarea peştelui, crustaceelor şi moluştelor", Category.GROUP),
        Classification("10.20", "Prelucrarea şi conservarea peştelui, crustaceelor şi moluştelor", Category.CLASS),
        Classification("10.3", "Prelucrarea şi conservarea fructelor şi legumelor", Category.GROUP),
        Classification("10.31", "Prelucrarea şi conservarea cartofilor", Category.CLASS),
        Classification("10.32", "Fabricarea sucurilor de fructe şi legume", Category.CLASS),
        Classification(
            "10.39", "Prelucrarea şi conservarea fructelor şi legumelor, cu excepţia cartofilor", Category.CLASS
        ),
        Classification("10.4", "Fabricarea uleiurilor şi a grăsimilor vegetale şi animale", Category.GROUP),
        Classification("10.41", "Fabricarea uleiurilor şi grăsimilor", Category.CLASS),
        Classification("10.42", "Fabricarea margarinei şi a altor produse comestibile similare", Category.CLASS),
        Classification("10.5", "Fabricarea produselor lactate", Category.GROUP),
        Classification("10.51", "Fabricarea produselor lactate şi a brânzeturilor", Category.CLASS),
        Classification("10.52", "Fabricarea îngheţatei", Category.CLASS),
        Classification(
            "10.6", "Fabricarea produselor de morărit, a amidonului şi produselor din amidon", Category.GROUP
        ),
        Classification("10.61", "Fabricarea produselor de morărit", Category.CLASS),
        Classification("10.62", "Fabricarea amidonului şi a produselor din amidon", Category.CLASS),
        Classification("10.7", "Fabricarea produselor de brutărie şi a produselor făinoase", Category.GROUP),
        Classification(
            "10.71", "Fabricarea pâinii; fabricarea prăjiturilor şi a produselor proaspete de patiserie", Category.CLASS
        ),
        Classification(
            "10.72",
            "Fabricarea biscuiţilor şi pişcoturilor; fabricarea prăjiturilor şi a  produselor conservate de patiserie",
            Category.CLASS,
        ),
        Classification(
            "10.73",
            "Fabricarea macaroanelor, tăiţeilor, cuş-cuş-ului şi a altor produse făinoase similare",
            Category.CLASS,
        ),
        Classification("10.8", "Fabricarea altor produse alimentare", Category.GROUP),
        Classification("10.81", "Fabricarea zahărului", Category.CLASS),
        Classification(
            "10.82", "Fabricarea produselor din cacao, a ciocolatei  şi a produselor zaharoase", Category.CLASS
        ),
        Classification("10.83", "Prelucrarea ceaiului şi cafelei", Category.CLASS),
        Classification("10.84", "Fabricarea condimentelor şi ingredientelor", Category.CLASS),
        Classification("10.85", "Fabricarea de mâncăruri preparate", Category.CLASS),
        Classification(
            "10.86", "Fabricarea preparatelor alimentare omogenizate şi alimentelor dietetice", Category.CLASS
        ),
        Classification("10.89", "Fabricarea altor produse alimentare n.c.a.", Category.CLASS),
        Classification("10.9", "Fabricarea preparatelor pentru hrana animalelor", Category.GROUP),
        Classification("10.91", "Fabricarea preparatelor pentru hrana animalelor de fermă", Category.CLASS),
        Classification("10.92", "Fabricarea preparatelor pentru hrana animalelor de companie", Category.CLASS),
        Classification("11", "Fabricarea băuturilor", Category.DIVISION),
        Classification("11.0", "Fabricarea băuturilor", Category.GROUP),
        Classification("11.01", "Distilarea, rafinarea şi mixarea băuturilor alcoolice", Category.CLASS),
        Classification("11.02", "Fabricarea vinurilor din struguri", Category.CLASS),
        Classification("11.03", "Fabricarea cidrului şi a altor vinuri din fructe", Category.CLASS),
        Classification("11.04", "Fabricarea altor băuturi nedistilate, obţinute prin fermentare", Category.CLASS),
        Classification("11.05", "Fabricarea berii", Category.CLASS),
        Classification("11.06", "Fabricarea malţului", Category.CLASS),
        Classification(
            "11.07",
            "Producţia de băuturi răcoritoare nealcoolice; producţia de ape minerale şi alte ape îmbuteliate",
            Category.CLASS,
        ),
        Classification("12", "Fabricarea produselor din tutun", Category.DIVISION),
        Classification("12.0", "Fabricarea produselor din tutun", Category.GROUP),
        Classification("12.00", "Fabricarea produselor din tutun", Category.CLASS),
        Classification("13", "Fabricarea produselor textile", Category.DIVISION),
        Classification("13.1", "Pregătirea fibrelor şi filarea fibrelor textile", Category.GROUP),
        Classification("13.10", "Pregătirea fibrelor şi filarea fibrelor textile", Category.CLASS),
        Classification("13.2", "Producţia de ţesături", Category.GROUP),
        Classification("13.20", "Producţia de ţesături", Category.CLASS),
        Classification("13.3", "Finisarea materialelor textile", Category.GROUP),
        Classification("13.30", "Finisarea materialelor textile", Category.CLASS),
        Classification("13.9", "Fabricarea altor articole textile", Category.GROUP),
        Classification("13.91", "Fabricarea de metraje prin tricotare sau croşetare", Category.CLASS),
        Classification(
            "13.92",
            "Fabricarea de articole confecţionate din textile (cu excepţia îmbrăcămintei şi lenjeriei de corp)",
            Category.CLASS,
        ),
        Classification("13.93", "Fabricarea de covoare şi mochete", Category.CLASS),
        Classification("13.94", "Fabricarea de odgoane, frânghii, sfori şi plase", Category.CLASS),
        Classification(
            "13.95",
            "Fabricarea de textile neţesute şi articole din acestea, cu excepţia confecţiilor de îmbrăcăminte",
            Category.CLASS,
        ),
        Classification("13.96", "Fabricarea altor articole tehnice şi industriale din textile", Category.CLASS),
        Classification("13.99", "Fabricarea altor articole textile n.c.a.", Category.CLASS),
        Classification("14", "Fabricarea articolelor de îmbrăcăminte", Category.DIVISION),
        Classification(
            "14.1", "Fabricarea articolelor de îmbrăcăminte, cu excepţia articolelor din blană", Category.GROUP
        ),
        Classification("14.11", "Fabricarea articolelor de îmbrăcăminte din piele", Category.CLASS),
        Classification("14.12", "Fabricarea articolelor de îmbrăcăminte pentru lucru", Category.CLASS),
        Classification(
            "14.13", "Fabricarea altor articole de îmbrăcăminte (exclusiv lenjeria de corp)", Category.CLASS
        ),
        Classification("14.14", "Fabricarea de articole de lenjerie de corp", Category.CLASS),
        Classification("14.19", "Fabricarea altor articole de îmbrăcăminte şi accesorii n.c.a.", Category.CLASS),
        Classification("14.2", "Fabricarea articolelor din blană", Category.GROUP),
        Classification("14.20", "Fabricarea articolelor din blană", Category.CLASS),
        Classification("14.3", "Fabricarea articolelor de îmbrăcăminte prin tricotare sau croşetare", Category.GROUP),
        Classification(
            "14.31", "Fabricarea prin tricotare sau croşetare a ciorapilor şi articolelor de galanterie", Category.CLASS
        ),
        Classification(
            "14.39", "Fabricarea prin tricotare sau croşetare a altor articole de îmbrăcăminte", Category.CLASS
        ),
        Classification(
            "15",
            "Tăbăcirea şi finisarea pieilor; fabricarea articolelor de voiaj şi marochinărie, harnaşamentelor şi încălţămintei; prepararea şi vopsirea blănurilor",
            Category.DIVISION,
        ),
        Classification(
            "15.1",
            "Tăbăcirea şi finisarea pieilor; fabricarea articolelor de voiaj şi marochinărie şi a articolelor de harnaşament; prepararea şi vopsirea blănurilor",
            Category.GROUP,
        ),
        Classification("15.11", "Tăbăcirea şi finisarea pieilor; prepararea şi vopsirea blănurilor", Category.CLASS),
        Classification(
            "15.12",
            "Fabricarea articolelor de voiaj şi marochinărie, a articolelor de harnaşament şi a altor articole din piele",
            Category.CLASS,
        ),
        Classification("15.2", "Fabricarea încălţămintei", Category.GROUP),
        Classification("15.20", "Fabricarea încălţămintei", Category.CLASS),
        Classification(
            "16",
            "Prelucrarea lemnului, fabricarea  produselor din lemn şi plută, cu excepţia mobilei; fabricarea articolelor din paie şi din alte materiale vegetale împletite",
            Category.DIVISION,
        ),
        Classification("16.1", "Tăierea şi rindeluirea lemnului", Category.GROUP),
        Classification("16.10", "Tăierea şi rindeluirea lemnului", Category.CLASS),
        Classification(
            "16.2",
            "Fabricarea produselor din lemn, plută,  paie şi din alte materiale vegetale împletite",
            Category.GROUP,
        ),
        Classification("16.21", "Fabricarea de furnire şi a panourilor din lemn", Category.CLASS),
        Classification("16.22", "Fabricarea parchetului asamblat în panouri", Category.CLASS),
        Classification(
            "16.23", "Fabricarea altor elemente de dulgherie şi tâmplărie, pentru construcţii", Category.CLASS
        ),
        Classification("16.24", "Fabricarea ambalajelor din lemn", Category.CLASS),
        Classification(
            "16.29",
            "Fabricarea altor produse din lemn; fabricarea articolelor din plută, paie şi din alte materiale vegetale împletite",
            Category.CLASS,
        ),
        Classification("17", "Fabricarea hârtiei şi a produselor din hârtie", Category.DIVISION),
        Classification("17.1", "Fabricarea celulozei, hârtiei şi cartonului", Category.GROUP),
        Classification("17.11", "Fabricarea celulozei", Category.CLASS),
        Classification("17.12", "Fabricarea hârtiei şi cartonului", Category.CLASS),
        Classification("17.2", "Fabricarea articolelor din hârtie şi carton", Category.GROUP),
        Classification(
            "17.21", "Fabricarea hârtiei şi cartonului ondulat şi a ambalajelor din hârtie şi carton", Category.CLASS
        ),
        Classification(
            "17.22", "Fabricarea produselor de uz gospodăresc şi sanitar, din hârtie sau carton", Category.CLASS
        ),
        Classification("17.23", "Fabricarea articolelor de papetărie", Category.CLASS),
        Classification("17.24", "Fabricarea tapetului", Category.CLASS),
        Classification("17.29", "Fabricarea altor articole din hârtie şi carton n.c.a.", Category.CLASS),
        Classification("18", "Tipărire şi reproducerea pe suporţi a înregistrărilor", Category.DIVISION),
        Classification("18.1", "Tipărire şi activităţi de servicii conexe tipăririi", Category.GROUP),
        Classification("18.11", "Tipărirea ziarelor", Category.CLASS),
        Classification("18.12", "Alte activităţi de tipărire n.c.a.", Category.CLASS),
        Classification("18.13", "Servicii pregătitoare pentru tipărire", Category.CLASS),
        Classification("18.14", "Legătorie şi servicii conexe", Category.CLASS),
        Classification("18.2", "Reproducerea înregistrărilor", Category.GROUP),
        Classification("18.20", "Reproducerea înregistrărilor", Category.CLASS),
        Classification(
            "19",
            "Fabricarea produselor de cocserie şi a produselor obţinute din prelucrarea ţiţeiului",
            Category.DIVISION,
        ),
        Classification("19.1", "Fabricarea produselor de cocserie", Category.GROUP),
        Classification("19.10", "Fabricarea produselor de cocserie", Category.CLASS),
        Classification("19.2", "Fabricarea produselor obţinute din prelucrarea ţiţeiului", Category.GROUP),
        Classification("19.20", "Fabricarea produselor obţinute din prelucrarea ţiţeiului", Category.CLASS),
        Classification("20", "Fabricarea substanţelor şi a produselor chimice", Category.DIVISION),
        Classification(
            "20.1",
            "Fabricarea produselor chimice de bază, a îngrăşămintelor şi produselor azotoase; fabricarea materialelor plastice şi a cauciucului sintetic, în forme primare",
            Category.GROUP,
        ),
        Classification("20.11", "Fabricarea gazelor industriale", Category.CLASS),
        Classification("20.12", "Fabricarea coloranţilor şi a pigmenţilor", Category.CLASS),
        Classification("20.13", "Fabricarea altor produse chimice anorganice, de bază", Category.CLASS),
        Classification("20.14", "Fabricarea altor produse chimice organice, de bază", Category.CLASS),
        Classification("20.15", "Fabricarea îngrăşămintelor şi produselor azotoase", Category.CLASS),
        Classification("20.16", "Fabricarea materialelor plastice în forme primare", Category.CLASS),
        Classification("20.17", "Fabricarea cauciucului sintetic în forme primare", Category.CLASS),
        Classification("20.2", "Fabricarea pesticidelor şi a altor produse agrochimice", Category.GROUP),
        Classification("20.20", "Fabricarea pesticidelor şi a altor produse agrochimice", Category.CLASS),
        Classification(
            "20.3", "Fabricarea vopselelor, lacurilor, cernelii tipografice şi masticurilor", Category.GROUP
        ),
        Classification(
            "20.30", "Fabricarea vopselelor, lacurilor, cernelii tipografice şi masticurilor", Category.CLASS
        ),
        Classification(
            "20.4",
            "Fabricarea săpunurilor, detergenţilor şi a produselor de întreţinere, cosmetice şi de parfumerie",
            Category.GROUP,
        ),
        Classification("20.41", "Fabricarea săpunurilor, detergenţilor şi a produselor de întreţinere", Category.CLASS),
        Classification("20.42", "Fabricarea parfumurilor şi a produselor cosmetice (de toaletă)", Category.CLASS),
        Classification("20.5", "Fabricarea altor produse chimice", Category.GROUP),
        Classification("20.51", "Fabricarea explozivilor", Category.CLASS),
        Classification("20.52", "Fabricarea cleiurilor", Category.CLASS),
        Classification("20.53", "Fabricarea uleiurilor esenţiale", Category.CLASS),
        Classification("20.59", "Fabricarea altor produse chimice n.c.a.", Category.CLASS),
        Classification("20.6", "Fabricarea fibrelor sintetice şi artificiale", Category.GROUP),
        Classification("20.60", "Fabricarea fibrelor sintetice şi artificiale", Category.CLASS),
        Classification(
            "21", "Fabricarea produselor farmaceutice de bază şi a preparatelor farmaceutice", Category.DIVISION
        ),
        Classification("21.1", "Fabricarea produselor farmaceutice de bază", Category.GROUP),
        Classification("21.10", "Fabricarea produselor farmaceutice de bază", Category.CLASS),
        Classification("21.2", "Fabricarea preparatelor farmaceutice", Category.GROUP),
        Classification("21.20", "Fabricarea preparatelor farmaceutice", Category.CLASS),
        Classification("22", "Fabricarea produselor din cauciuc şi mase plastice", Category.DIVISION),
        Classification("22.1", "Fabricarea articolelor din cauciuc", Category.GROUP),
        Classification(
            "22.11", "Fabricarea anvelopelor şi a camerelor de aer; reşaparea şi refacerea anvelopelor", Category.CLASS
        ),
        Classification("22.19", "Fabricarea altor produse din cauciuc", Category.CLASS),
        Classification("22.2", "Fabricarea articolelor din material plastic", Category.GROUP),
        Classification(
            "22.21", "Fabricarea plăcilor, foliilor, tuburilor şi profilelor din material plastic", Category.CLASS
        ),
        Classification("22.22", "Fabricarea articolelor de ambalaj din material plastic", Category.CLASS),
        Classification("22.23", "Fabricarea articolelor din material plastic pentru construcţii", Category.CLASS),
        Classification("22.29", "Fabricarea altor produse din material plastic", Category.CLASS),
        Classification("23", "Fabricarea altor produse din minerale nemetalice", Category.DIVISION),
        Classification("23.1", "Fabricarea sticlei şi a articolelor din sticlă", Category.GROUP),
        Classification("23.11", "Fabricarea sticlei plate", Category.CLASS),
        Classification("23.12", "Prelucrarea şi fasonarea sticlei plate", Category.CLASS),
        Classification("23.13", "Fabricarea articolelor din sticlă", Category.CLASS),
        Classification("23.14", "Fabricarea fibrelor din sticlă", Category.CLASS),
        Classification("23.19", "Fabricarea de sticlărie tehnică", Category.CLASS),
        Classification("23.2", "Fabricarea de produse refractare", Category.GROUP),
        Classification("23.20", "Fabricarea de produse refractare", Category.CLASS),
        Classification("23.3", "Fabricarea materialelor de construcţii din argilă", Category.GROUP),
        Classification("23.31", "Fabricarea plăcilor şi dalelor din ceramică", Category.CLASS),
        Classification(
            "23.32",
            "Fabricarea cărămizilor, ţiglelor şi altor produse pentru construcţii, din argilă arsă",
            Category.CLASS,
        ),
        Classification("23.4", "Fabricarea altor articole din ceramică şi porţelan", Category.GROUP),
        Classification("23.41", "Fabricarea articolelor ceramice pentru uz gospodăresc şi ornamental", Category.CLASS),
        Classification("23.42", "Fabricarea de obiecte sanitare din ceramică", Category.CLASS),
        Classification("23.43", "Fabricarea izolatorilor şi pieselor izolante din ceramică", Category.CLASS),
        Classification("23.44", "Fabricarea altor produse tehnice din ceramică", Category.CLASS),
        Classification("23.49", "Fabricarea altor produse ceramice n.c.a.", Category.CLASS),
        Classification("23.5", "Fabricarea cimentului, varului şi ipsosului", Category.GROUP),
        Classification("23.51", "Fabricarea cimentului", Category.CLASS),
        Classification("23.52", "Fabricarea varului şi ipsosului", Category.CLASS),
        Classification("23.6", "Fabricarea articolelor din beton, ciment şi ipsos", Category.GROUP),
        Classification("23.61", "Fabricarea produselor din beton pentru construcţii", Category.CLASS),
        Classification("23.62", "Fabricarea produselor din ipsos pentru construcţii", Category.CLASS),
        Classification("23.63", "Fabricarea betonului", Category.CLASS),
        Classification("23.64", "Fabricarea mortarului", Category.CLASS),
        Classification("23.65", "Fabricarea produselor din azbociment", Category.CLASS),
        Classification("23.69", "Fabricarea altor articole din beton, ciment şi ipsos", Category.CLASS),
        Classification("23.7", "Tăierea, fasonarea şi finisarea pietrei", Category.GROUP),
        Classification("23.70", "Tăierea, fasonarea şi finisarea pietrei", Category.CLASS),
        Classification("23.9", "Fabricarea altor produse din minerale nemetalice n.c.a.", Category.GROUP),
        Classification("23.91", "Fabricarea de produse abrazive", Category.CLASS),
        Classification("23.99", "Fabricarea altor produse din minerale nemetalice, n.c.a.", Category.CLASS),
        Classification("24", "Industria metalurgică", Category.DIVISION),
        Classification("24.1", "Producţia de metale feroase sub forme primare şi de feroaliaje", Category.GROUP),
        Classification("24.10", "Producţia de metale feroase sub forme primare şi de feroaliaje", Category.CLASS),
        Classification(
            "24.2", "Producţia de tuburi, ţevi, profile tubulare şi accesorii pentru acestea, din oţel", Category.GROUP
        ),
        Classification(
            "24.20", "Producţia de tuburi, ţevi, profile tubulare şi accesorii pentru acestea, din oţel", Category.CLASS
        ),
        Classification("24.3", "Fabricarea altor produse prin prelucrarea primară a oţelului", Category.GROUP),
        Classification("24.31", "Tragere la rece a barelor", Category.CLASS),
        Classification("24.32", "Laminare la rece a benzilor înguste", Category.CLASS),
        Classification("24.33", "Producţia de profile obţinute la rece prin ştanţare sau fălţuire", Category.CLASS),
        Classification("24.34", "Trefilarea firelor la rece", Category.CLASS),
        Classification("24.4", "Producţia metalelor preţioase şi a altor metale neferoase", Category.GROUP),
        Classification("24.41", "Producţia metalelor preţioase", Category.CLASS),
        Classification("24.42", "Producţia aluminiului", Category.CLASS),
        Classification("24.43", "Producţia plumbului, zincului şi cositorului", Category.CLASS),
        Classification("24.44", "Producţia cuprului", Category.CLASS),
        Classification("24.45", "Producţia altor metale neferoase", Category.CLASS),
        Classification("24.46", "Prelucrarea combustibililor nucleari", Category.CLASS),
        Classification("24.5", "Turnarea metalelor", Category.GROUP),
        Classification("24.51", "Turnarea fontei", Category.CLASS),
        Classification("24.52", "Turnarea oţelului", Category.CLASS),
        Classification("24.53", "Turnarea metalelor neferoase uşoare", Category.CLASS),
        Classification("24.54", "Turnarea altor metale neferoase", Category.CLASS),
        Classification(
            "25",
            "Industria construcţiilor metalice şi a produselor din metal, exclusiv maşini, utilaje şi instalaţii",
            Category.DIVISION,
        ),
        Classification("25.1", "Fabricarea de construcţii metalice", Category.GROUP),
        Classification(
            "25.11", "Fabricarea de construcţii metalice şi părţi componente ale structurilor metalice", Category.CLASS
        ),
        Classification("25.12", "Fabricarea de uşi şi ferestre din metal", Category.CLASS),
        Classification(
            "25.2",
            "Producţia de rezervoare, cisterne şi containere metalice; producţia de radiatoare şi cazane pentru încălzire centrală",
            Category.GROUP,
        ),
        Classification("25.21", "Producţia de radiatoare şi cazane pentru încălzire centrală", Category.CLASS),
        Classification("25.29", "Producţia de rezervoare, cisterne şi containere metalice", Category.CLASS),
        Classification(
            "25.3",
            "Producţia generatoarelor de aburi (cu excepţia cazanelor pentru încălzire centrală)",
            Category.GROUP,
        ),
        Classification(
            "25.30",
            "Producţia generatoarelor de aburi (cu excepţia cazanelor pentru încălzire centrală)",
            Category.CLASS,
        ),
        Classification("25.4", "Fabricarea armamentului şi muniţiei", Category.GROUP),
        Classification("25.40", "Fabricarea armamentului şi muniţiei", Category.CLASS),
        Classification(
            "25.5",
            "Fabricarea produselor metalice obţinute prin forjare, presare, ştanţare şi laminare; metalurgia pulberilor",
            Category.GROUP,
        ),
        Classification(
            "25.50",
            "Fabricarea produselor metalice obţinute prin forjare, presare, ştanţare şi laminare; metalurgia pulberilor",
            Category.CLASS,
        ),
        Classification("25.6", "Tratarea şi acoperirea metalelor; operaţiuni de mecanică generală", Category.GROUP),
        Classification("25.61", "Tratarea şi acoperirea metalelor", Category.CLASS),
        Classification("25.62", "Operaţiuni de mecanică generală", Category.CLASS),
        Classification("25.7", "Producţia de unelte şi articole de fierărie", Category.GROUP),
        Classification("25.71", "Fabricarea produselor de tăiat", Category.CLASS),
        Classification("25.72", "Fabricarea articolelor de feronerie (lacăte şi balamale)", Category.CLASS),
        Classification("25.73", "Fabricarea uneltelor", Category.CLASS),
        Classification("25.9", "Fabricarea altor produse prelucrate din metal", Category.GROUP),
        Classification(
            "25.91", "Fabricarea de recipiente, containere şi alte produse similare din oţel", Category.CLASS
        ),
        Classification("25.92", "Fabricarea ambalajelor din metale uşoare", Category.CLASS),
        Classification(
            "25.93", "Fabricarea articolelor din fire metalice; fabricarea de lanţuri şi arcuri", Category.CLASS
        ),
        Classification(
            "25.94",
            "Fabricarea de şuruburi, buloane şi alte articole filetate; fabricarea de nituri şi şaibe",
            Category.CLASS,
        ),
        Classification("25.99", "Fabricarea altor articole din metal n.c.a.", Category.CLASS),
        Classification("26", "Fabricarea calculatoarelor şi a produselor electronice şi optice", Category.DIVISION),
        Classification("26.1", "Fabricarea componentelor electronice", Category.GROUP),
        Classification("26.11", "Fabricarea componentelor electronice (module)", Category.CLASS),
        Classification("26.12", "Fabricarea altor componente electronice", Category.CLASS),
        Classification("26.2", "Fabricarea calculatoarelor şi a echipamentelor periferice", Category.GROUP),
        Classification("26.20", "Fabricarea calculatoarelor şi a echipamentelor periferice", Category.CLASS),
        Classification("26.3", "Fabricarea echipamentelor de comunicaţii", Category.GROUP),
        Classification("26.30", "Fabricarea echipamentelor de comunicaţii", Category.CLASS),
        Classification("26.4", "Fabricarea produselor electronice de larg consum", Category.GROUP),
        Classification("26.40", "Fabricarea produselor electronice de larg consum", Category.CLASS),
        Classification(
            "26.5",
            "Fabricarea de echipamente de măsură, verificare, control şi navigaţie; producţia de ceasuri",
            Category.GROUP,
        ),
        Classification(
            "26.51",
            "Fabricarea de instrumente şi dispozitive pentru măsură, verificare, control, navigaţie",
            Category.CLASS,
        ),
        Classification("26.52", "Producţia de ceasuri", Category.CLASS),
        Classification(
            "26.6", "Fabricarea de echipamente pentru radiologie, electrodiagnostic şi electroterapie", Category.GROUP
        ),
        Classification(
            "26.60", "Fabricarea de echipamente pentru radiologie, electrodiagnostic şi electroterapie", Category.CLASS
        ),
        Classification("26.7", "Fabricarea de instrumente optice şi echipamente fotografice", Category.GROUP),
        Classification("26.70", "Fabricarea de instrumente optice şi echipamente fotografice", Category.CLASS),
        Classification("26.8", "Fabricarea suporţilor magnetici şi optici destinaţi înregistrărilor", Category.GROUP),
        Classification("26.80", "Fabricarea suporţilor magnetici şi optici destinaţi înregistrărilor", Category.CLASS),
        Classification("27", "Fabricarea echipamentelor electrice", Category.DIVISION),
        Classification(
            "27.1",
            "Fabricarea motoarelor electrice, generatoarelor şi transformatoarelor electrice şi a aparatelor de distribuţie şi control a electricităţii",
            Category.GROUP,
        ),
        Classification(
            "27.11", "Fabricarea motoarelor, generatoarelor şi transformatoarelor electrice", Category.CLASS
        ),
        Classification("27.12", "Fabricarea aparatelor de distribuţie şi control a electricităţii", Category.CLASS),
        Classification("27.2", "Fabricarea de acumulatori şi baterii", Category.GROUP),
        Classification("27.20", "Fabricarea de acumulatori şi baterii", Category.CLASS),
        Classification(
            "27.3",
            "Fabricarea de fire şi cabluri; fabricarea dispozitivelor de conexiune pentru acestea",
            Category.GROUP,
        ),
        Classification("27.31", "Fabricarea de cabluri cu fibră optică", Category.CLASS),
        Classification("27.32", "Fabricarea altor fire şi cabluri electrice şi electronice", Category.CLASS),
        Classification(
            "27.33",
            "Fabricarea dispozitivelor de conexiune pentru fire şi cabluri electrice şi electronice",
            Category.CLASS,
        ),
        Classification("27.4", "Fabricarea de echipamente electrice de iluminat", Category.GROUP),
        Classification("27.40", "Fabricarea de echipamente electrice de iluminat", Category.CLASS),
        Classification("27.5", "Fabricarea de echipamente casnice", Category.GROUP),
        Classification("27.51", "Fabricarea de aparate electrocasnice", Category.CLASS),
        Classification("27.52", "Fabricarea de echipamente casnice neelectrice", Category.CLASS),
        Classification("27.9", "Fabricarea altor echipamente electrice", Category.GROUP),
        Classification("27.90", "Fabricarea altor echipamente electrice", Category.CLASS),
        Classification("28", "Fabricarea de maşini, utilaje şi echipamente n.c.a.", Category.DIVISION),
        Classification("28.1", "Fabricarea de maşini şi utilaje de utilizare generală", Category.GROUP),
        Classification(
            "28.11",
            "Fabricarea de motoare şi turbine (cu excepţia celor pentru avioane, autovehicule şi motociclete)",
            Category.CLASS,
        ),
        Classification("28.12", "Fabricarea de echipamente hidraulice", Category.CLASS),
        Classification("28.13", "Fabricarea de alte pompe şi compresoare", Category.CLASS),
        Classification("28.14", "Fabricarea de alte robinete şi valve", Category.CLASS),
        Classification(
            "28.15",
            "Fabricarea lagărelor, angrenajelor, cutiilor de viteză şi a elementelor mecanice de transmisie",
            Category.CLASS,
        ),
        Classification("28.2", "Fabricarea altor maşini şi utilaje de utilizare generală", Category.GROUP),
        Classification("28.21", "Fabricarea cuptoarelor, furnalelor şi arzătoarelor", Category.CLASS),
        Classification("28.22", "Fabricarea echipamentelor de ridicat şi manipulat", Category.CLASS),
        Classification(
            "28.23",
            "Fabricarea maşinilor şi echipamentelor de birou (exclusiv fabricarea calculatoarelor şi a echipamentelor periferice)",
            Category.CLASS,
        ),
        Classification("28.24", "Fabricarea maşinilor-unelte portabile acţionate mecanic", Category.CLASS),
        Classification(
            "28.25",
            "Fabricarea echipamentelor de ventilaţie şi frigorifice, exclusiv a echipamentelor de uz casnic",
            Category.CLASS,
        ),
        Classification("28.29", "Fabricarea altor maşini şi utilaje de utilizare generală n.c.a.", Category.CLASS),
        Classification(
            "28.3", "Fabricarea maşinilor şi utilajelor pentru agricultură şi exploatări forestiere", Category.GROUP
        ),
        Classification(
            "28.30", "Fabricarea maşinilor şi utilajelor pentru agricultură şi exploatări forestiere", Category.CLASS
        ),
        Classification(
            "28.4", "Fabricarea utilajelor şi a maşinilor-unelte pentru prelucrarea metalelor", Category.GROUP
        ),
        Classification(
            "28.41", "Fabricarea utilajelor şi a maşinilor-unelte pentru prelucrarea metalelor", Category.CLASS
        ),
        Classification("28.49", "Fabricarea altor maşini-unelte n.c.a.", Category.CLASS),
        Classification("28.9", "Fabricarea altor maşini şi utilaje cu destinaţie specifică", Category.GROUP),
        Classification("28.91", "Fabricarea utilajelor pentru metalurgie", Category.CLASS),
        Classification("28.92", "Fabricarea utilajelor pentru extracţie şi construcţii", Category.CLASS),
        Classification(
            "28.93",
            "Fabricarea utilajelor pentru prelucrarea produselor alimentare, băuturilor şi tutunului",
            Category.CLASS,
        ),
        Classification(
            "28.94", "Fabricarea utilajelor pentru industria textilă, a îmbrăcămintei şi a pielăriei", Category.CLASS
        ),
        Classification("28.95", "Fabricarea utilajelor pentru industria hârtiei şi cartonului", Category.CLASS),
        Classification(
            "28.96", "Fabricarea utilajelor pentru prelucrarea maselor plastice şi a cauciucului", Category.CLASS
        ),
        Classification("28.99", "Fabricarea altor maşini şi utilaje specifice n.c.a.", Category.CLASS),
        Classification("29", "Fabricarea autovehiculelor, a remorcilor şi semiremorcilor", Category.DIVISION),
        Classification("29.1", "Fabricarea autovehiculelor de transport rutier", Category.GROUP),
        Classification("29.10", "Fabricarea autovehiculelor de transport rutier", Category.CLASS),
        Classification(
            "29.2", "Producţia de caroserii pentru autovehicule; fabricarea de  remorci şi semiremorci", Category.GROUP
        ),
        Classification(
            "29.20", "Producţia de caroserii pentru autovehicule; fabricarea de  remorci şi semiremorci", Category.CLASS
        ),
        Classification(
            "29.3",
            "Producţia de piese şi accesorii pentru autovehicule şi pentru motoare de autovehicule",
            Category.GROUP,
        ),
        Classification(
            "29.31", "Fabricarea de echipamente electrice şi electronice pentru autovehicule", Category.CLASS
        ),
        Classification("29.32", "Fabricarea altor piese şi accesorii pentru autovehicule", Category.CLASS),
        Classification("30", "Fabricarea altor mijloace de transport", Category.DIVISION),
        Classification("30.1", "Construcţia de nave şi bărci", Category.GROUP),
        Classification("30.11", "Construcţia de nave şi structuri plutitoare", Category.CLASS),
        Classification("30.12", "Construcţia de ambarcaţiuni sportive şi de agrement", Category.CLASS),
        Classification("30.2", "Fabricarea materialului rulant", Category.GROUP),
        Classification("30.20", "Fabricarea materialului rulant", Category.CLASS),
        Classification("30.3", "Fabricarea de aeronave şi nave spaţiale", Category.GROUP),
        Classification("30.30", "Fabricarea de aeronave şi nave spaţiale", Category.CLASS),
        Classification("30.4", "Fabricarea vehiculelor militare de luptă", Category.GROUP),
        Classification("30.40", "Fabricarea vehiculelor militare de luptă", Category.CLASS),
        Classification("30.9", "Fabricarea altor echipamente de transport n.c.a.", Category.GROUP),
        Classification("30.91", "Fabricarea de motociclete", Category.CLASS),
        Classification("30.92", "Fabricarea de biciclete şi de vehicule pentru invalizi", Category.CLASS),
        Classification("30.99", "Fabricarea altor mijloace de transport n.c.a.", Category.CLASS),
        Classification("31", "Fabricarea de mobilă", Category.DIVISION),
        Classification("31.0", "Fabricarea de mobilă", Category.GROUP),
        Classification("31.01", "Fabricarea de mobilă pentru birouri şi magazine", Category.CLASS),
        Classification("31.02", "Fabricarea de mobilă pentru bucătării", Category.CLASS),
        Classification("31.03", "Fabricarea de saltele", Category.CLASS),
        Classification("31.09", "Fabricarea de mobilă n.c.a.", Category.CLASS),
        Classification("32", "Alte activităţi industriale n.c.a.", Category.DIVISION),
        Classification(
            "32.1", "Fabricarea bijuteriilor, imitaţiilor de bijuterii şi articolelor similare", Category.GROUP
        ),
        Classification("32.11", "Baterea monedelor", Category.CLASS),
        Classification(
            "32.12", "Fabricarea bijuteriilor şi articolelor similare din metale şi pietre preţioase", Category.CLASS
        ),
        Classification("32.13", "Fabricarea imitaţiilor de bijuterii şi articole similare", Category.CLASS),
        Classification("32.2", "Fabricarea instrumentelor muzicale", Category.GROUP),
        Classification("32.20", "Fabricarea instrumentelor muzicale", Category.CLASS),
        Classification("32.3", "Fabricarea articolelor pentru sport", Category.GROUP),
        Classification("32.30", "Fabricarea articolelor pentru sport", Category.CLASS),
        Classification("32.4", "Fabricarea jocurilor şi jucăriilor", Category.GROUP),
        Classification("32.40", "Fabricarea jocurilor şi jucăriilor", Category.CLASS),
        Classification(
            "32.5", "Fabricarea de dispozitive, aparate şi instrumente medicale şi stomatologice", Category.GROUP
        ),
        Classification(
            "32.50", "Fabricarea de dispozitive, aparate şi instrumente medicale stomatologice", Category.CLASS
        ),
        Classification("32.9", "Alte activităţi industriale n.c.a.", Category.GROUP),
        Classification("32.91", "Fabricarea măturilor şi periilor", Category.CLASS),
        Classification("32.99", "Fabricarea altor produse manufacturiere n.c.a.", Category.CLASS),
        Classification("33", "Repararea, întreţinerea şi instalarea maşinilor şi echipamentelor", Category.DIVISION),
        Classification(
            "33.1", "Repararea articolelor fabricate din metal, maşinilor şi echipamentelor", Category.GROUP
        ),
        Classification("33.11", "Repararea articolelor fabricate din metal", Category.CLASS),
        Classification("33.12", "Repararea maşinilor", Category.CLASS),
        Classification("33.13", "Repararea echipamentelor electronice şi optice", Category.CLASS),
        Classification("33.14", "Repararea echipamentelor electrice", Category.CLASS),
        Classification("33.15", "Repararea şi întreţinerea navelor şi bărcilor", Category.CLASS),
        Classification("33.16", "Repararea şi întreţinerea aeronavelor şi navelor spaţiale", Category.CLASS),
        Classification("33.17", "Repararea şi întreţinerea altor echipamente de transport", Category.CLASS),
        Classification("33.19", "Repararea altor echipamente", Category.CLASS),
        Classification("33.2", "Instalarea maşinilor şi echipamentelor industriale", Category.GROUP),
        Classification("33.20", "Instalarea maşinilor şi echipamentelor industriale", Category.CLASS),
        Classification(
            "D",
            "PRODUCŢIA ŞI FURNIZAREA DE ENERGIE ELECTRICĂ ŞI TERMICĂ, GAZE, APĂ CALDĂ ŞI AER CONDIŢIONAT",
            Category.SECTION,
        ),
        Classification(
            "35",
            "Producţia şi furnizarea de energie electrică şi termică, gaze, apă caldă şi aer condiţionat",
            Category.DIVISION,
        ),
        Classification("35.1", "Producţia, transportul şi distribuţia energiei electrice", Category.GROUP),
        Classification("35.11", "Producţia de energie electrică", Category.CLASS),
        Classification("35.12", "Transportul energiei electrice", Category.CLASS),
        Classification("35.13", "Distribuţia energiei electrice", Category.CLASS),
        Classification("35.14", "Comercializarea energiei electrice", Category.CLASS),
        Classification("35.2", "Producţia gazelor; distribuţia combustibililor gazoşi prin conducte", Category.GROUP),
        Classification("35.21", "Producţia gazelor", Category.CLASS),
        Classification("35.22", "Distribuţia combustibililor gazoşi prin conducte", Category.CLASS),
        Classification("35.23", "Comercializarea combustibililor gazoşi, prin conducte", Category.CLASS),
        Classification("35.3", "Furnizarea de abur şi aer condiţionat", Category.GROUP),
        Classification("35.30", "Furnizarea de abur şi aer condiţionat", Category.CLASS),
        Classification(
            "E", "DISTRIBUŢIA APEI; SALUBRITATE, GESTIONAREA DEŞEURILOR, ACTIVITĂŢI DE DECONTAMINARE", Category.SECTION
        ),
        Classification("36", "Captarea, tratarea şi distribuţia apei", Category.DIVISION),
        Classification("36.0", "Captarea, tratarea şi distribuţia apei", Category.GROUP),
        Classification("36.00", "Captarea, tratarea şi distribuţia apei", Category.CLASS),
        Classification("37", "Colectarea şi epurarea apelor uzate", Category.DIVISION),
        Classification("37.0", "Colectarea şi epurarea apelor uzate", Category.GROUP),
        Classification("37.00", "Colectarea şi epurarea apelor uzate", Category.CLASS),
        Classification(
            "38",
            "Colectarea, tratarea şi eliminarea deşeurilor; activităţi de recuperare a materialelor  reciclabile",
            Category.DIVISION,
        ),
        Classification("38.1", "Colectarea deşeurilor", Category.GROUP),
        Classification("38.11", "Colectarea deşeurilor nepericuloase", Category.CLASS),
        Classification("38.12", "Colectarea deşeurilor periculoase", Category.CLASS),
        Classification("38.2", "Tratarea şi eliminarea deşeurilor", Category.GROUP),
        Classification("38.21", "Tratarea şi eliminarea deşeurilor nepericuloase", Category.CLASS),
        Classification("38.22", "Tratarea şi eliminarea deşeurilor periculoase", Category.CLASS),
        Classification("38.3", "Recuperareа materialelor reciclabile", Category.GROUP),
        Classification(
            "38.31",
            "Demontarea (dezasamblarea) maşinilor şi a echipamentelor scoase din uz pentru recuperarea materialelor",
            Category.CLASS,
        ),
        Classification("38.32", "Recuperarea materialelor reciclabile sortate", Category.CLASS),
        Classification("39", "Activităţi şi servicii de decontaminare", Category.DIVISION),
        Classification("39.0", "Activităţi şi servicii de decontaminare", Category.GROUP),
        Classification("39.00", "Activităţi şi servicii de decontaminare", Category.CLASS),
        Classification("F", "CONSTRUCŢII", Category.SECTION),
        Classification("41", "Construcţii de clădiri", Category.DIVISION),
        Classification("41.1", "Dezvoltare (promovare) imobiliară", Category.GROUP),
        Classification("41.10", "Dezvoltare (promovare) imobiliară", Category.CLASS),
        Classification("41.2", "Lucrări de construcţii a clădirilor rezidenţiale şi nerezidenţiale", Category.GROUP),
        Classification("41.20", "Lucrări de construcţii a clădirilor rezidenţiale şi nerezidenţiale", Category.CLASS),
        Classification("42", "Lucrări de construcţii civile", Category.DIVISION),
        Classification("42.1", "Lucrări de construcţii a drumurilor şi a căilor ferate", Category.GROUP),
        Classification("42.11", "Lucrări de construcţii a drumurilor şi autostrăzilor", Category.CLASS),
        Classification("42.12", "Lucrări de construcţii a căilor ferate de suprafaţă şi subterane", Category.CLASS),
        Classification("42.13", "Construcţia de poduri şi tuneluri", Category.CLASS),
        Classification("42.2", "Lucrări de construcţii a proiectelor utilitare", Category.GROUP),
        Classification("42.21", "Lucrări de construcţii a proiectelor utilitare pentru fluide", Category.CLASS),
        Classification(
            "42.22",
            "Lucrări de construcţii a proiectelor utilitare pentru electricitate şi telecomunicaţii",
            Category.CLASS,
        ),
        Classification("42.9", "Lucrări de construcţii a altor proiecte inginereşti", Category.GROUP),
        Classification("42.91", "Construcţii hidrotehnice", Category.CLASS),
        Classification("42.99", "Lucrări de construcţii a altor proiecte inginereşti n.c.a.", Category.CLASS),
        Classification("43", "Lucrări speciale de construcţii", Category.DIVISION),
        Classification("43.1", "Lucrări de demolare şi de pregătire a terenului", Category.GROUP),
        Classification("43.11", "Lucrări de demolare a construcţiilor", Category.CLASS),
        Classification("43.12", "Lucrări de pregătire a terenului de construcţii", Category.CLASS),
        Classification("43.13", "Lucrări de foraj şi sondaj pentru construcţii", Category.CLASS),
        Classification(
            "43.2",
            "Lucrări de instalaţii electrice şi tehnico-sanitare şi alte lucrări de instalaţii pentru construcţii",
            Category.GROUP,
        ),
        Classification("43.21", "Lucrări de instalaţii electrice", Category.CLASS),
        Classification(
            "43.22",
            "Lucrări de instalaţii tehnico-sanitare, de alimentare cu gaze, de încălzire şi de aer condiţionat",
            Category.CLASS,
        ),
        Classification("43.29", "Alte lucrări de instalaţii pentru construcţii", Category.CLASS),
        Classification("43.3", "Lucrări de finisare", Category.GROUP),
        Classification("43.31", "Lucrări de tencuire", Category.CLASS),
        Classification("43.32", "Lucrări de tâmplărie şi dulgherie", Category.CLASS),
        Classification("43.33", "Lucrări de pardosire şi placare a pereţilor", Category.CLASS),
        Classification("43.34", "Lucrări de vopsitorie, zugrăveli şi  montări de geamuri", Category.CLASS),
        Classification("43.39", "Alte lucrări de finisare", Category.CLASS),
        Classification("43.9", "Alte lucrări speciale de construcţii", Category.GROUP),
        Classification("43.91", "Lucrări de învelitori, şarpante şi terase la construcţii", Category.CLASS),
        Classification("43.99", "Alte lucrări speciale de construcţii n.c.a.", Category.CLASS),
        Classification(
            "G",
            "COMERŢ CU RIDICATA ŞI CU AMĂNUNTUL; ÎNTREŢINEREA ŞI REPARAREA AUTOVEHICULELOR ŞI A MOTOCICLETELOR",
            Category.SECTION,
        ),
        Classification(
            "45",
            "Comerţ cu ridicata şi cu amănuntul; întreţinerea şi repararea autovehiculelor şi a motocicletelor",
            Category.DIVISION,
        ),
        Classification("45.1", "Comerţ cu autovehicule", Category.GROUP),
        Classification("45.11", "Comerţ cu  autoturisme şi autovehicule uşoare (sub 3,5 tone)", Category.CLASS),
        Classification("45.19", "Comerţ cu alte autovehicule", Category.CLASS),
        Classification("45.2", "Întreţinerea şi repararea autovehiculelor", Category.GROUP),
        Classification("45.20", "Întreţinerea şi repararea autovehiculelor", Category.CLASS),
        Classification("45.3", "Comerţ cu piese şi accesorii pentru autovehicule", Category.GROUP),
        Classification("45.31", "Comerţ cu ridicata de piese şi accesorii pentru autovehicule", Category.CLASS),
        Classification("45.32", "Comerţ cu amănuntul de piese şi accesorii pentru autovehicule", Category.CLASS),
        Classification(
            "45.4",
            "Comerţ cu motociclete, piese şi accesorii aferente; întreţinerea şi repararea motocicletelor",
            Category.GROUP,
        ),
        Classification(
            "45.40",
            "Comerţ cu motociclete, piese şi accesorii aferente; întreţinerea şi repararea motocicletelor",
            Category.CLASS,
        ),
        Classification(
            "46", "Comerţ cu ridicata, cu excepţia comerţului cu autovehicule şi motociclete", Category.DIVISION
        ),
        Classification("46.1", "Activităţi de intermediere în comerţul cu ridicata", Category.GROUP),
        Classification(
            "46.11",
            "Intermedieri în comerţul cu materii prime agricole, animale vii, materii prime textile şi cu semifabricate",
            Category.CLASS,
        ),
        Classification(
            "46.12",
            "Intermedieri în comerţul cu combustibili, minereuri, metale şi produse chimice pentru industrie",
            Category.CLASS,
        ),
        Classification(
            "46.13", "Intermedieri în comerţul cu material lemnos şi materiale de construcţii", Category.CLASS
        ),
        Classification(
            "46.14", "Intermedieri în comerţul cu maşini, echipamente industriale, nave şi avioane", Category.CLASS
        ),
        Classification("46.15", "Intermedieri în comerţul cu mobilă, articole de menaj şi de fierărie", Category.CLASS),
        Classification(
            "46.16",
            "Intermedieri în comerţul cu textile, confecţii din blană, încălţăminte şi articole din piele",
            Category.CLASS,
        ),
        Classification(
            "46.17", "Intermedieri în comerţul cu produse alimentare, inclusiv băuturi, şi tutun", Category.CLASS
        ),
        Classification(
            "46.18",
            "Intermedieri în comerţul specializat în vânzarea produselor cu caracter specific, n.c.a.",
            Category.CLASS,
        ),
        Classification("46.19", "Intermedieri în comerţul cu produse diverse", Category.CLASS),
        Classification("46.2", "Comerţ cu ridicata al produselor agricole brute şi al animalelor vii", Category.GROUP),
        Classification(
            "46.21", "Comerţ cu ridicata al cerealelor, seminţelor, furajelor şi tutunului neprelucrat", Category.CLASS
        ),
        Classification("46.22", "Comerţ cu ridicata al florilor şi al plantelor", Category.CLASS),
        Classification("46.23", "Comerţ cu  ridicata al animalelor vii", Category.CLASS),
        Classification(
            "46.24", "Comerţ cu ridicata al blănurilor, pieilor brute şi al pieilor prelucrate", Category.CLASS
        ),
        Classification(
            "46.3", "Comerţ cu ridicata al produselor alimentare, al băuturilor şi al tutunului", Category.GROUP
        ),
        Classification("46.31", "Comerţ cu ridicata al fructelor şi legumelor", Category.CLASS),
        Classification("46.32", "Comerţ cu ridicata al cărnii şi produselor din carne", Category.CLASS),
        Classification(
            "46.33",
            "Comerţ cu ridicata al produselor lactate, ouălor, uleiurilor şi grăsimilor comestibile",
            Category.CLASS,
        ),
        Classification("46.34", "Comerţ cu ridicata al băuturilor", Category.CLASS),
        Classification("46.35", "Comerţ cu ridicata al produselor din tutun", Category.CLASS),
        Classification("46.36", "Comerţ cu ridicata al zahărului, ciocolatei şi produselor zaharoase", Category.CLASS),
        Classification("46.37", "Comerţ cu ridicata cu cafea, ceai, cacao şi condimente", Category.CLASS),
        Classification(
            "46.38",
            "Comerţ cu ridicata specializat al altor alimente, inclusiv peşte, crustacee şi moluşte",
            Category.CLASS,
        ),
        Classification(
            "46.39", "Comerţ cu ridicata nespecializat de produse alimentare, băuturi şi tutun", Category.CLASS
        ),
        Classification("46.4", "Comerţ cu ridicata al bunurilor de consum", Category.GROUP),
        Classification("46.41", "Comerţ cu ridicata al produselor textile", Category.CLASS),
        Classification("46.42", "Comerţ cu ridicata al îmbrăcămintei şi încălţămintei", Category.CLASS),
        Classification(
            "46.43",
            "Comerţ cu ridicata al aparatelor electrice de uz gospodăresc, al aparatelor de radio şi televizoarelor",
            Category.CLASS,
        ),
        Classification(
            "46.44",
            "Comerţ cu ridicata al produselor din ceramică, sticlărie şi al produselor de întreţinere",
            Category.CLASS,
        ),
        Classification("46.45", "Comerţ cu ridicata al produselor cosmetice şi de parfumerie", Category.CLASS),
        Classification("46.46", "Comerţ cu ridicata al produselor farmaceutice", Category.CLASS),
        Classification(
            "46.47", "Comerţ cu ridicata al mobilei, covoarelor şi a articolelor de iluminat", Category.CLASS
        ),
        Classification("46.48", "Comerţ cu ridicata al ceasurilor şi bijuteriilor", Category.CLASS),
        Classification("46.49", "Comerţ cu ridicata al altor bunuri de uz gospodăresc", Category.CLASS),
        Classification("46.5", "Comerţ cu ridicata al echipamentului informatic şi de telecomunicaţii", Category.GROUP),
        Classification(
            "46.51", "Comerţ cu ridicata al calculatoarelor, echipamentelor periferice şi software-lui", Category.CLASS
        ),
        Classification(
            "46.52", "Comerţ cu ridicata de componente şi echipamente electronice şi de telecomunicaţii", Category.CLASS
        ),
        Classification("46.6", "Comerţ cu ridicata al altor maşini, echipamente şi furnituri", Category.GROUP),
        Classification(
            "46.61", "Comerţ cu ridicata al maşinilor agricole, echipamentelor şi furniturilor", Category.CLASS
        ),
        Classification("46.62", "Comerţ cu ridicata al maşinilor-unelte", Category.CLASS),
        Classification(
            "46.63", "Comerţ cu ridicata al maşinilor pentru industria minieră şi construcţii", Category.CLASS
        ),
        Classification(
            "46.64",
            "Comerţ cu ridicata al maşinilor pentru industria textilă şi al maşinilor de cusut şi de tricotat",
            Category.CLASS,
        ),
        Classification("46.65", "Comerţ cu ridicata al mobilei de birou", Category.CLASS),
        Classification("46.66", "Comerţ cu ridicata al altor maşini şi echipamente de birou", Category.CLASS),
        Classification("46.69", "Comerţ cu ridicata al altor maşini şi echipamente", Category.CLASS),
        Classification("46.7", "Comerţ cu ridicata specializat al altor produse", Category.GROUP),
        Classification(
            "46.71",
            "Comerţ cu ridicata al combustibililor solizi, lichizi şi gazoşi şi al produselor derivate",
            Category.CLASS,
        ),
        Classification("46.72", "Comerţ cu ridicata al metalelor şi minereurilor metalice", Category.CLASS),
        Classification(
            "46.73",
            "Comerţ cu ridicata al materialului lemnos şi al materialelor de construcţie şi echipamentelor sanitare",
            Category.CLASS,
        ),
        Classification(
            "46.74",
            "Comerţ cu ridicata al echipamentelor şi furniturilor de fierărie pentru instalaţii sanitare şi de încălzire",
            Category.CLASS,
        ),
        Classification("46.75", "Comerţ cu ridicata al produselor chimice", Category.CLASS),
        Classification("46.76", "Comerţ cu ridicata al altor produse intermediare", Category.CLASS),
        Classification("46.77", "Comerţ cu ridicata al deşeurilor şi resturilor", Category.CLASS),
        Classification("46.9", "Comerţ cu ridicata nespecializat", Category.GROUP),
        Classification("46.90", "Comerţ cu ridicata nespecializat", Category.CLASS),
        Classification("47", "Comerţ cu amănuntul, cu excepţia autovehiculelor şi motocicletelor", Category.DIVISION),
        Classification("47.1", "Comerţ cu amănuntul în magazine nespecializate", Category.GROUP),
        Classification(
            "47.11",
            "Comerţ cu amănuntul în magazine nespecializate, cu vânzare predominantă de produse alimentare, băuturi şi tutun",
            Category.CLASS,
        ),
        Classification(
            "47.19",
            "Comerţ cu amănuntul în magazine nespecializate, cu vânzare predominantă de produse nealimentare",
            Category.CLASS,
        ),
        Classification(
            "47.2",
            "Comerţ cu amănuntul al produselor alimentare, băuturilor şi al produselor din tutun, în magazine specializate",
            Category.GROUP,
        ),
        Classification(
            "47.21", "Comerţ cu amănuntul al fructelor şi legumelor proaspete, în magazine specializate", Category.CLASS
        ),
        Classification(
            "47.22",
            "Comerţ cu amănuntul al cărnii şi al produselor din carne, în magazine specializate",
            Category.CLASS,
        ),
        Classification(
            "47.23",
            "Comerţ cu amănuntul al peştelui, crustaceelor şi moluştelor, în magazine specializate",
            Category.CLASS,
        ),
        Classification(
            "47.24",
            "Comerţ cu amănuntul al pâinii, produselor de patiserie şi produselor zaharoase, în magazine specializate",
            Category.CLASS,
        ),
        Classification("47.25", "Comerţ cu amănuntul al băuturilor, în magazine specializate", Category.CLASS),
        Classification(
            "47.26", "Comerţ cu amănuntul al produselor din tutun, în magazine specializate", Category.CLASS
        ),
        Classification(
            "47.29", "Comerţ cu amănuntul al altor produse alimentare, în magazine specializate", Category.CLASS
        ),
        Classification(
            "47.3", "Comerţ cu amănuntul al carburanţilor pentru autovehicule în magazine specializate", Category.GROUP
        ),
        Classification(
            "47.30", "Comerţ cu amănuntul al carburanţilor pentru autovehicule în magazine specializate", Category.CLASS
        ),
        Classification(
            "47.4",
            "Comerţ cu amănuntul al echipamentului informatic şi de telecomunicaţii în magazine specializate",
            Category.GROUP,
        ),
        Classification(
            "47.41",
            "Comerţ cu amănuntul al calculatoarelor, unităţilor periferice şi software-lui în magazine specializate",
            Category.CLASS,
        ),
        Classification(
            "47.42",
            "Comerţ cu amănuntul al echipamentului pentru  telecomunicaţii în magazine specializate",
            Category.CLASS,
        ),
        Classification(
            "47.43", "Comerţ cu amănuntul al echipamentelor audio/video în magazine specializate", Category.CLASS
        ),
        Classification(
            "47.5", "Comerţ cu amănuntul al altor produse casnice, în magazine specializate", Category.GROUP
        ),
        Classification("47.51", "Comerţ cu amănuntul al textilelor, în magazine specializate", Category.CLASS),
        Classification(
            "47.52",
            "Comerţ cu amănuntul al articolelor de fierărie, al articolelor din sticlă şi a celor pentru vopsit, în magazine specializate",
            Category.CLASS,
        ),
        Classification(
            "47.53",
            "Comerţ cu amănuntul al covoarelor, carpetelor, tapetelor şi a altor acoperitoare de podea, în magazine specializate",
            Category.CLASS,
        ),
        Classification(
            "47.54",
            "Comerţ cu amănuntul al articolelor şi aparatelor electrocasnice, în magazine specializate",
            Category.CLASS,
        ),
        Classification(
            "47.59",
            "Comerţ cu amănuntul al mobilei, al articolelor de iluminat şi al articolelor de uz casnic n.c.a., în magazine specializate",
            Category.CLASS,
        ),
        Classification(
            "47.6", "Comerţ cu amănuntul de bunuri culturale şi recreative, în magazine specializate", Category.GROUP
        ),
        Classification("47.61", "Comerţ cu amănuntul al cărţilor, în magazine specializate", Category.CLASS),
        Classification(
            "47.62",
            "Comerţ cu amănuntul al ziarelor şi articolelor de papetărie, în magazine specializate",
            Category.CLASS,
        ),
        Classification(
            "47.63",
            "Comerţ cu amănuntul al înregistrărilor muzicale şi video, în magazine specializate",
            Category.CLASS,
        ),
        Classification(
            "47.64", "Comerţ cu amănuntul al echipamentelor sportive, în magazine specializate", Category.CLASS
        ),
        Classification(
            "47.65", "Comerţ cu amănuntul al jocurilor şi jucăriilor, în magazine specializate", Category.CLASS
        ),
        Classification("47.7", "Comerţ cu amănuntul al altor bunuri, în magazine specializate", Category.GROUP),
        Classification("47.71", "Comerţ cu amănuntul al îmbrăcămintei, în magazine specializate", Category.CLASS),
        Classification(
            "47.72",
            "Comerţ cu amănuntul al încălţămintei şi articolelor din piele, în magazine specializate",
            Category.CLASS,
        ),
        Classification(
            "47.73", "Comerţ cu amănuntul al produselor farmaceutice, în magazine specializate", Category.CLASS
        ),
        Classification(
            "47.74",
            "Comerţ cu amănuntul al articolelor medicale şi ortopedice, în magazine specializate",
            Category.CLASS,
        ),
        Classification(
            "47.75",
            "Comerţ cu amănuntul al produselor cosmetice şi de parfumerie, în magazine specializate",
            Category.CLASS,
        ),
        Classification(
            "47.76",
            "Comerţ cu amănuntul al florilor, plantelor şi seminţelor; comerţ cu amănuntul al animalelor de companie şi a hranei pentru acestea, în magazine specializate",
            Category.CLASS,
        ),
        Classification(
            "47.77", "Comerţ cu amănuntul al ceasurilor şi bijuteriilor, în magazine specializate", Category.CLASS
        ),
        Classification("47.78", "Comerţ cu amănuntul al altor bunuri noi, în magazine specializate", Category.CLASS),
        Classification("47.79", "Comerţ cu amănuntul al bunurilor de ocazie vândute prin magazine", Category.CLASS),
        Classification("47.8", "Comerţ cu amănuntul efectuat prin standuri, chioşcuri şi pieţe", Category.GROUP),
        Classification(
            "47.81",
            "Comerţ cu amănuntul al produselor alimentare, băuturilor şi produselor din tutun efectuat prin standuri, chioşcuri şi pieţe",
            Category.CLASS,
        ),
        Classification(
            "47.82",
            "Comerţ cu amănuntul al textilelor, îmbrăcămintei şi încălţămintei efectuat prin standuri, chioşcuri şi pieţe",
            Category.CLASS,
        ),
        Classification(
            "47.89", "Comerţ cu amănuntul prin standuri, chioşcuri şi pieţe al altor produse", Category.CLASS
        ),
        Classification(
            "47.9",
            "Comerţ cu amănuntul care nu se efectuează prin magazine, standuri, chioşcuri şi pieţe",
            Category.GROUP,
        ),
        Classification(
            "47.91", "Comerţ cu amănuntul prin intermediul caselor de comenzi sau prin Internet", Category.CLASS
        ),
        Classification(
            "47.99",
            "Comerţ cu amănuntul efectuat în afara magazinelor, standurilor, chioşcurilor şi pieţelor",
            Category.CLASS,
        ),
        Classification("H", "TRANSPORT ŞI DEPOZITARE", Category.SECTION),
        Classification("49", "Transporturi terestre şi transporturi prin conducte", Category.DIVISION),
        Classification("49.1", "Transporturi interurbane de călători pe calea ferată", Category.GROUP),
        Classification("49.10", "Transporturi interurbane de călători pe calea ferată", Category.CLASS),
        Classification("49.2", "Transporturi de marfă pe calea ferată", Category.GROUP),
        Classification("49.20", "Transporturi de marfă pe calea ferată", Category.CLASS),
        Classification("49.3", "Alte transporturi terestre de călători", Category.GROUP),
        Classification("49.31", "Transporturi urbane terestre şi suburbane de călători", Category.CLASS),
        Classification("49.32", "Transporturi cu taxiuri", Category.CLASS),
        Classification("49.39", "Alte transporturi terestre de călători n.c.a.", Category.CLASS),
        Classification("49.4", "Transporturi rutiere de mărfuri şi servicii de mutare", Category.GROUP),
        Classification("49.41", "Transporturi rutiere de mărfuri", Category.CLASS),
        Classification("49.42", "Servicii de mutare", Category.CLASS),
        Classification("49.5", "Transporturi prin conducte", Category.GROUP),
        Classification("49.50", "Transporturi prin conducte", Category.CLASS),
        Classification("50", "Transporturi pe apă", Category.DIVISION),
        Classification("50.1", "Transporturi maritime şi costiere de pasageri", Category.GROUP),
        Classification("50.10", "Transporturi maritime şi costiere de pasageri", Category.CLASS),
        Classification("50.2", "Transporturi maritime şi costiere de marfă", Category.GROUP),
        Classification("50.20", "Transporturi maritime şi costiere de marfă", Category.CLASS),
        Classification("50.3", "Transporturi de pasageri pe căi navigabile interioare", Category.GROUP),
        Classification("50.30", "Transportul de pasageri pe căi navigabile interioare", Category.CLASS),
        Classification("50.4", "Transportul de marfă pe căi navigabile interioare", Category.GROUP),
        Classification("50.40", "Transportul de marfă pe căi navigabile interioare", Category.CLASS),
        Classification("51", "Transporturi aeriene", Category.DIVISION),
        Classification("51.1", "Transporturi aeriene de pasageri", Category.GROUP),
        Classification("51.10", "Transporturi aeriene de pasageri", Category.CLASS),
        Classification("51.2", "Transporturi aeriene de marfă şi transporturi spaţiale", Category.GROUP),
        Classification("51.21", "Transporturi aeriene de marfă", Category.CLASS),
        Classification("51.22", "Transporturi spaţiale", Category.CLASS),
        Classification("52", "Depozitare şi activităţi auxiliare pentru transporturi", Category.DIVISION),
        Classification("52.1", "Depozitări", Category.GROUP),
        Classification("52.10", "Depozitări", Category.CLASS),
        Classification("52.2", "Activităţi anexe pentru transporturi", Category.GROUP),
        Classification("52.21", "Activităţi de servicii anexe pentru transporturi terestre", Category.CLASS),
        Classification("52.22", "Activităţi de servicii anexe transporturilor pe apă", Category.CLASS),
        Classification("52.23", "Activităţi de servicii anexe transporturilor aeriene", Category.CLASS),
        Classification("52.24", "Manipulări", Category.CLASS),
        Classification("52.29", "Alte activităţi anexe transporturilor", Category.CLASS),
        Classification("53", "Activităţi de poştă şi de curier", Category.DIVISION),
        Classification(
            "53.1", "Activităţi poştale desfăşurate sub obligativitatea serviciului universal", Category.GROUP
        ),
        Classification(
            "53.10", "Activităţi poştale desfăşurate sub obligativitatea serviciului universal", Category.CLASS
        ),
        Classification("53.2", "Alte activităţi poştale şi de curier", Category.GROUP),
        Classification("53.20", "Alte activităţi poştale şi de curier", Category.CLASS),
        Classification("I", "ACTIVITĂŢI DE CAZARE ŞI ALIMENTAŢIE PUBLICĂ", Category.SECTION),
        Classification("55", "Hoteluri şi alte facilităţi de cazare", Category.DIVISION),
        Classification("55.1", "Hoteluri şi alte facilităţi de cazare similare", Category.GROUP),
        Classification("55.10", "Hoteluri şi alte facilităţi de cazare similare", Category.CLASS),
        Classification("55.2", "Facilităţi de cazare pentru vacanţe şi perioade de scurtă durată", Category.GROUP),
        Classification("55.20", "Facilităţi de cazare pentru vacanţe şi perioade de scurtă durată", Category.CLASS),
        Classification("55.3", "Parcuri pentru rulote, campinguri şi tabere", Category.GROUP),
        Classification("55.30", "Parcuri pentru rulote, campinguri şi  tabere", Category.CLASS),
        Classification("55.9", "Alte servicii de cazare", Category.GROUP),
        Classification("55.90", "Alte servicii de cazare", Category.CLASS),
        Classification("56", "Restaurante şi alte activităţi de servicii de alimentaţie", Category.DIVISION),
        Classification("56.1", "Restaurante", Category.GROUP),
        Classification("56.10", "Restaurante", Category.CLASS),
        Classification(
            "56.2",
            "Activităţi de alimentaţie (catering) pentru evenimente şi alte servicii de alimentaţie",
            Category.GROUP,
        ),
        Classification("56.21", "Activităţi de alimentaţie (catering) pentru evenimente", Category.CLASS),
        Classification("56.29", "Alte activităţi de alimentaţie", Category.CLASS),
        Classification("56.3", "Baruri şi alte activităţi de servire a băuturilor", Category.GROUP),
        Classification("56.30", "Baruri şi alte activităţi de servire a băuturilor", Category.CLASS),
        Classification("J", "INFORMAŢII ŞI COMUNICAŢII", Category.SECTION),
        Classification("58", "Activităţi de editare", Category.DIVISION),
        Classification(
            "58.1",
            "Activităţi de editare a cărţilor, ziarelor, revistelor şi alte activităţi de editare",
            Category.GROUP,
        ),
        Classification("58.11", "Activităţi de editare a cărţilor", Category.CLASS),
        Classification("58.12", "Activităţi de editare de ghiduri, liste de adrese şi similare", Category.CLASS),
        Classification("58.13", "Activităţi de editare a ziarelor", Category.CLASS),
        Classification("58.14", "Activităţi de editare a revistelor şi periodicelor", Category.CLASS),
        Classification("58.19", "Alte activităţi de editare", Category.CLASS),
        Classification("58.2", "Activităţi de editare a produselor software", Category.GROUP),
        Classification("58.21", "Activităţi de editare a jocurilor de calculator", Category.CLASS),
        Classification("58.29", "Activităţi de editare a altor produse software", Category.CLASS),
        Classification(
            "59",
            "Activităţi de producţie cinematografică, video şi de programe de televiziune; înregistrări audio şi activităţi de editare muzicală",
            Category.DIVISION,
        ),
        Classification(
            "59.1", "Activităţi de producţie cinematografică, video şi de programe de televiziune", Category.GROUP
        ),
        Classification(
            "59.11", "Activităţi de producţie cinematografică, video şi de programe de televiziune", Category.CLASS
        ),
        Classification(
            "59.12", "Activităţi de post-producţie cinematografică, video şi de programe de televiziune", Category.CLASS
        ),
        Classification(
            "59.13",
            "Activităţi de distribuţie a filmelor cinematografice, video şi a programelor de televiziune",
            Category.CLASS,
        ),
        Classification("59.14", "Proiecţia de filme cinematografice", Category.CLASS),
        Classification(
            "59.2", "Activităţi de realizare a înregistrărilor audio şi activităţi de editare muzicală", Category.GROUP
        ),
        Classification(
            "59.20", "Activităţi de realizare a înregistrărilor audio şi activităţi de editare muzicală", Category.CLASS
        ),
        Classification("60", "Activităţi de producere şi difuzare de programe", Category.DIVISION),
        Classification("60.1", "Activităţi de difuzare a programelor de radio", Category.GROUP),
        Classification("60.10", "Activităţi de difuzare a programelor de radio", Category.CLASS),
        Classification("60.2", "Activităţi de producere şi difuzare a programelor de televiziune", Category.GROUP),
        Classification("60.20", "Activităţi de producere şi difuzare a programelor de televiziune", Category.CLASS),
        Classification("61", "Comunicaţii electronice", Category.DIVISION),
        Classification("61.1", "Activităţi de comunicaţii electronice prin reţele cu cablu", Category.GROUP),
        Classification("61.10", "Activităţi de comunicaţii electronice prin reţele cu cablu", Category.CLASS),
        Classification("61.2", "Activităţi de comunicaţii electronice prin reţele fără cablu", Category.GROUP),
        Classification(
            "61.20",
            "Activităţi de comunicaţii electronice prin reţele fără cablu (exclusiv prin satelit)",
            Category.CLASS,
        ),
        Classification("61.3", "Activităţi de comunicaţii electronice prin satelit", Category.GROUP),
        Classification("61.30", "Activităţi de comunicaţii electronice prin satelit", Category.CLASS),
        Classification("61.9", "Alte activităţi de comunicaţii electronice", Category.GROUP),
        Classification("61.90", "Alte activităţi de comunicaţii electronice", Category.CLASS),
        Classification("62", "Activităţi de servicii în tehnologia informaţiei", Category.DIVISION),
        Classification("62.0", "Activităţi de servicii în tehnologia informaţiei", Category.GROUP),
        Classification(
            "62.01", "Activităţi de realizare a soft-ului la comandă (software orientat client)", Category.CLASS
        ),
        Classification("62.02", "Activităţi de consultanţă în tehnologia informaţiei", Category.CLASS),
        Classification(
            "62.03", "Activităţi de management (gestiune şi exploatare) a mijloacelor de calcul", Category.CLASS
        ),
        Classification("62.09", "Alte activităţi de servicii privind tehnologia informaţiei", Category.CLASS),
        Classification("63", "Activităţi de servicii informatice", Category.DIVISION),
        Classification(
            "63.1",
            "Activităţi ale portalurilor web, prelucrarea datelor, administrarea paginilor web şi activităţi conexe",
            Category.GROUP,
        ),
        Classification(
            "63.11", "Prelucrarea datelor, administrarea paginilor web şi activităţi conexe", Category.CLASS
        ),
        Classification("63.12", "Activităţi ale portalurilor web", Category.CLASS),
        Classification("63.9", "Alte activităţi de servicii informaţionale", Category.GROUP),
        Classification("63.91", "Activităţi ale agenţiilor de ştiri", Category.CLASS),
        Classification("63.99", "Alte activităţi de servicii informaţionale n.c.a", Category.CLASS),
        Classification("K", "ACTIVITĂŢI FINANCIARE ŞI ASIGURĂRI", Category.SECTION),
        Classification(
            "64",
            "Intermedieri financiare, cu excepţia activităţilor de asigurări şi ale fondurilor de pensii",
            Category.DIVISION,
        ),
        Classification("64.1", "Intermediere monetară", Category.GROUP),
        Classification("64.11", "Activităţi ale Băncii Naţionale (centrale)", Category.CLASS),
        Classification("64.19", "Alte activităţi de intermedieri monetare", Category.CLASS),
        Classification("64.2", "Activităţi ale holdingurilor", Category.GROUP),
        Classification("64.20", "Activităţi ale holdingurilor", Category.CLASS),
        Classification("64.3", "Fonduri mutuale şi alte entităţi financiare similare", Category.GROUP),
        Classification("64.30", "Fonduri mutuale şi alte entităţi financiare similare", Category.CLASS),
        Classification(
            "64.9",
            "Alte activităţi de intermedieri financiare, exclusiv activităţi de asigurări şi fonduri de pensii",
            Category.GROUP,
        ),
        Classification("64.91", "Leasing financiar", Category.CLASS),
        Classification("64.92", "Alte activităţi de creditare", Category.CLASS),
        Classification("64.99", "Alte intermedieri financiare n.c.a.", Category.CLASS),
        Classification(
            "65",
            "Activităţi de asigurări, reasigurări şi ale fondurilor de pensii, cu excepţia celor din sistemul public de asigurări sociale",
            Category.DIVISION,
        ),
        Classification("65.1", "Activităţi de asigurări", Category.GROUP),
        Classification("65.11", "Activităţi de asigurări de viaţă", Category.CLASS),
        Classification("65.12", "Alte activităţi de asigurări (exceptând asigurările de viaţă)", Category.CLASS),
        Classification("65.2", "Activităţi de reasigurare", Category.GROUP),
        Classification("65.20", "Activităţi de reasigurare", Category.CLASS),
        Classification(
            "65.3",
            "Activităţi ale fondurilor de pensii, cu excepţia celor din sistemul public de asigurări sociale",
            Category.GROUP,
        ),
        Classification(
            "65.30",
            "Activităţi ale fondurilor de pensii, cu excepţia celor din sistemul public de asigurări sociale",
            Category.CLASS,
        ),
        Classification(
            "66", "Activităţi auxiliare pentru intermedieri financiare şi activităţi de asigurare", Category.DIVISION
        ),
        Classification(
            "66.1",
            "Activităţi auxiliare intermedierilor financiare, cu excepţia activităţilor de asigurări şi fonduri de pensii",
            Category.GROUP,
        ),
        Classification("66.11", "Administrarea pieţelor financiare", Category.CLASS),
        Classification("66.12", "Activităţi de intermediere (brokeraj) a tranzacţiilor financiare", Category.CLASS),
        Classification(
            "66.19",
            "Activităţi auxiliare intermedierilor financiare, exclusiv activităţi de asigurări şi fonduri de pensii",
            Category.CLASS,
        ),
        Classification("66.2", "Activităţi auxiliare de asigurări şi fonduri de pensii", Category.GROUP),
        Classification("66.21", "Activităţi de evaluare a riscului de asigurare şi a pagubelor", Category.CLASS),
        Classification("66.22", "Activităţi ale agenţilor şi broker-ilor de asigurări", Category.CLASS),
        Classification("66.29", "Alte activităţi auxiliare de asigurări şi fonduri de pensii", Category.CLASS),
        Classification("66.3", "Activităţi de administrare a fondurilor", Category.GROUP),
        Classification("66.30", "Activităţi de administrare a fondurilor", Category.CLASS),
        Classification("L", "TRANZACŢII IMOBILIARE", Category.SECTION),
        Classification("68", "Tranzacţii imobiliare", Category.DIVISION),
        Classification("68.1", "Cumpărarea şi vânzarea de bunuri imobiliare proprii", Category.GROUP),
        Classification("68.10", "Cumpărarea şi vânzarea de bunuri imobiliare proprii", Category.CLASS),
        Classification(
            "68.2", "Închirierea şi exploatarea bunurilor imobiliare proprii sau închiriate", Category.GROUP
        ),
        Classification(
            "68.20", "Închirierea şi exploatarea bunurilor imobiliare proprii sau închiriate", Category.CLASS
        ),
        Classification("68.3", "Activităţi imobiliare pe bază de tarife sau contract", Category.GROUP),
        Classification("68.31", "Activităţi ale agenţiilor imobiliare", Category.CLASS),
        Classification("68.32", "Administrarea imobilelor pe bază de tarife sau contract", Category.CLASS),
        Classification("M", "ACTIVITĂŢI PROFESIONALE, ŞTIINŢIFICE ŞI TEHNICE", Category.SECTION),
        Classification("69", "Activităţi juridice şi de contabilitate", Category.DIVISION),
        Classification("69.1", "Activităţi juridice", Category.GROUP),
        Classification("69.10", "Activităţi juridice", Category.CLASS),
        Classification(
            "69.2", "Activităţi de contabilitate şi audit financiar; consultanţă în domeniul fiscal", Category.GROUP
        ),
        Classification(
            "69.20", "Activităţi de contabilitate şi audit financiar; consultanţă în domeniul fiscal", Category.CLASS
        ),
        Classification(
            "70",
            "Activităţi ale direcţiilor administrative centralizate; activităţi de management şi de consultanţă în management",
            Category.DIVISION,
        ),
        Classification("70.1", "Activităţi ale direcţiilor administrative centralizate", Category.GROUP),
        Classification("70.10", "Activităţi ale direcţiilor administrative centralizate", Category.CLASS),
        Classification("70.2", "Activităţi de consultanţă în management", Category.GROUP),
        Classification(
            "70.21", "Activităţi de consultanţă în domeniul relaţiilor publice şi al comunicării", Category.CLASS
        ),
        Classification("70.22", "Activităţi de consultanţă pentru afaceri şi management", Category.CLASS),
        Classification(
            "71", "Activităţi de arhitectură şi inginerie; activităţi de testări şi analiză tehnică", Category.DIVISION
        ),
        Classification(
            "71.1",
            "Activităţi de arhitectură, inginerie şi servicii de consultanţă tehnică legate de acestea",
            Category.GROUP,
        ),
        Classification("71.11", "Activităţi de arhitectură", Category.CLASS),
        Classification("71.12", "Activităţi de inginerie şi consultanţă tehnică legate de acestea", Category.CLASS),
        Classification("71.2", "Activităţi de testare şi analize tehnice", Category.GROUP),
        Classification("71.20", "Activităţi de testare şi analize tehnice", Category.CLASS),
        Classification("72", "Cercetare-dezvoltare", Category.DIVISION),
        Classification("72.1", "Cercetare-dezvoltare în ştiinţe naturale şi inginerie", Category.GROUP),
        Classification("72.11", "Cercetare-dezvoltare în biotehnologie", Category.CLASS),
        Classification("72.19", "Cercetare-dezvoltare în alte ştiinţe naturale şi inginerie", Category.CLASS),
        Classification("72.2", "Cercetare-dezvoltare în ştiinţe sociale şi umaniste", Category.GROUP),
        Classification("72.20", "Cercetare-dezvoltare în ştiinţe sociale şi umaniste", Category.CLASS),
        Classification("73", "Publicitate şi activităţi de studiere a pieţei", Category.DIVISION),
        Classification("73.1", "Publicitate", Category.GROUP),
        Classification("73.11", "Activităţi ale agenţiilor de publicitate", Category.CLASS),
        Classification("73.12", "Servicii de reprezentare media", Category.CLASS),
        Classification("73.2", "Activităţi de studiere a pieţei şi de sondare a opiniei publice", Category.GROUP),
        Classification("73.20", "Activităţi de studiere a pieţei şi de sondare a opiniei publice", Category.CLASS),
        Classification("74", "Alte activităţi profesionale, ştiinţifice şi tehnice", Category.DIVISION),
        Classification("74.1", "Activităţi de design specializat", Category.GROUP),
        Classification("74.10", "Activităţi de design specializat", Category.CLASS),
        Classification("74.2", "Activităţi fotografice", Category.GROUP),
        Classification("74.20", "Activităţi fotografice", Category.CLASS),
        Classification("74.3", "Activităţi de traducere scrisă şi orală (interpreţi)", Category.GROUP),
        Classification("74.30", "Activităţi de traducere scrisă şi orală (interpreţi)", Category.CLASS),
        Classification("74.9", "Alte activităţi profesionale, ştiinţifice şi tehnice n.c.a.", Category.GROUP),
        Classification("74.90", "Alte activităţi profesionale, ştiinţifice şi tehnice n.c.a.", Category.CLASS),
        Classification("75", "Activităţi veterinare", Category.DIVISION),
        Classification("75.0", "Activităţi veterinare", Category.GROUP),
        Classification("75.00", "Activităţi veterinare", Category.CLASS),
        Classification("N", "ACTIVITĂŢI DE SERVICII ADMINISTRATIVE ŞI ACTIVITĂŢI DE SERVICII SUPORT", Category.SECTION),
        Classification("77", "Activităţi de închiriere şi leasing", Category.DIVISION),
        Classification("77.1", "Activităţi de închiriere şi leasing de autovehicule", Category.GROUP),
        Classification(
            "77.11", "Activităţi de închiriere şi leasing de autoturisme şi autovehicule rutiere uşoare", Category.CLASS
        ),
        Classification("77.12", "Activităţi de închiriere şi leasing de autovehicule rutiere grele", Category.CLASS),
        Classification(
            "77.2", "Activităţi de închiriere şi leasing de bunuri personale şi gospodăreşti", Category.GROUP
        ),
        Classification(
            "77.21", "Activităţi de închiriere şi leasing de bunuri recreaţionale şi echipament sportiv", Category.CLASS
        ),
        Classification("77.22", "Închirierea de casete video şi discuri (CD-uri, DVD-uri)", Category.CLASS),
        Classification(
            "77.29",
            "Activităţi de închiriere şi leasing de alte bunuri personale şi gospodăreşti n.c.a.",
            Category.CLASS,
        ),
        Classification(
            "77.3",
            "Activităţi de închiriere şi leasing de alte maşini,  echipamente şi bunuri tangibile",
            Category.GROUP,
        ),
        Classification(
            "77.31", "Activităţi de închiriere şi leasing de maşini şi echipamente agricole", Category.CLASS
        ),
        Classification(
            "77.32", "Activităţi de închiriere şi leasing de maşini şi echipamente pentru construcţii", Category.CLASS
        ),
        Classification(
            "77.33",
            "Activităţi de închiriere şi leasing de maşini şi echipamente de birou (inclusiv calculatoare)",
            Category.CLASS,
        ),
        Classification(
            "77.34", "Activităţi de închiriere şi leasing de echipamente de transport pe apă", Category.CLASS
        ),
        Classification(
            "77.35", "Activităţi de închiriere şi leasing de echipamente de transport aerian", Category.CLASS
        ),
        Classification(
            "77.39",
            "Activităţi de închirierea şi leasing de alte maşini,  echipamente şi bunuri tangibile n.c.a.",
            Category.CLASS,
        ),
        Classification(
            "77.4",
            "Leasing de proprietăţi intelectuale şi producţie similară (exclusiv bunuri cu drept de autor)",
            Category.GROUP,
        ),
        Classification(
            "77.40",
            "Leasing de proprietăţi intelectuale şi producţie similară (exclusiv bunuri cu drept de autor)",
            Category.CLASS,
        ),
        Classification("78", "Activităţi de servicii privind forţa de muncă", Category.DIVISION),
        Classification("78.1", "Activităţi ale agenţiilor de plasare a forţei de muncă", Category.GROUP),
        Classification("78.10", "Activităţi ale agenţiilor de plasare a forţei de muncă", Category.CLASS),
        Classification("78.2", "Activităţi de contractare, pe baze temporare, a personalului", Category.GROUP),
        Classification("78.20", "Activităţi de contractare, pe baze temporare, a personalului", Category.CLASS),
        Classification("78.3", "Alte servicii de furnizare a forţei de muncă", Category.GROUP),
        Classification("78.30", "Alte servicii de furnizare a forţei de muncă", Category.CLASS),
        Classification(
            "79",
            "Activităţi ale agenţiilor turistice şi ale tur-operatorilor; alte servicii de rezervare şi asistenţă turistică",
            Category.DIVISION,
        ),
        Classification("79.1", "Activităţi ale agenţiilor turistice şi ale tur-operatorilor", Category.GROUP),
        Classification("79.11", "Activităţi ale agenţiilor turistice", Category.CLASS),
        Classification("79.12", "Activităţi ale tur-operatorilor", Category.CLASS),
        Classification("79.9", "Alte servicii de rezervare şi asistenţă turistică", Category.GROUP),
        Classification("79.90", "Alte servicii de rezervare şi asistenţă turistică", Category.CLASS),
        Classification("80", "Activităţi de investigaţii şi protecţie", Category.DIVISION),
        Classification("80.1", "Activităţi de securitate privată", Category.GROUP),
        Classification("80.10", "Activităţi de securitate privată", Category.CLASS),
        Classification("80.2", "Activităţi de servicii privind sistemele de securizare", Category.GROUP),
        Classification("80.20", "Activităţi de servicii privind sistemele de securizare", Category.CLASS),
        Classification("80.3", "Activităţi de investigaţii", Category.GROUP),
        Classification("80.30", "Activităţi de investigaţii", Category.CLASS),
        Classification("81", "Activităţi de peisagistică şi servicii pentru clădiri", Category.DIVISION),
        Classification("81.1", "Activităţi de servicii suport combinate", Category.GROUP),
        Classification("81.10", "Activităţi de servicii suport combinate", Category.CLASS),
        Classification("81.2", "Activităţi de curăţenie", Category.GROUP),
        Classification(
            "81.21", "Activităţi generale (nespecializate) de curăţenie interioară a clădirilor", Category.CLASS
        ),
        Classification(
            "81.22",
            "Activităţi specializate de curăţenie a clădirilor, mijloacelor de transport, maşinilor şi utilajelor",
            Category.CLASS,
        ),
        Classification("81.29", "Alte activităţi de curăţenie n.c.a.", Category.CLASS),
        Classification("81.3", "Activităţi de întreţinere peisagistică", Category.GROUP),
        Classification("81.30", "Activităţi de întreţinere peisagistică", Category.CLASS),
        Classification(
            "82",
            "Servicii administrative, servicii suport şi alte activităţi de servicii prestate în principal întreprinderilor",
            Category.DIVISION,
        ),
        Classification("82.1", "Activităţi administrative şi servicii suport", Category.GROUP),
        Classification("82.11", "Activităţi combinate de secretariat", Category.CLASS),
        Classification(
            "82.19",
            "Activităţi de fotocopiere, de pregătire a documentelor şi alte activităţi specializate de secretariat",
            Category.CLASS,
        ),
        Classification("82.2", "Activităţi ale centrelor de intermediere telefonică (call center)", Category.GROUP),
        Classification("82.20", "Activităţi ale centrelor de intermediere telefonică (call center)", Category.CLASS),
        Classification("82.3", "Activităţi de organizare a expoziţiilor, târgurilor şi congreselor", Category.GROUP),
        Classification("82.30", "Activităţi de organizare a expoziţiilor, târgurilor şi congreselor", Category.CLASS),
        Classification("82.9", "Activităţi de servicii suport pentru întreprinderi n.c.a.", Category.GROUP),
        Classification(
            "82.91",
            "Activităţi ale agenţiilor de colectare a plăţilor şi a birourilor (oficiilor) de raportare a creditului",
            Category.CLASS,
        ),
        Classification("82.92", "Activităţi de ambalare", Category.CLASS),
        Classification("82.99", "Alte activităţi de servicii suport pentru întreprinderi n.c.a.", Category.CLASS),
        Classification("O", "ADMINISTRAŢIE PUBLICĂ ŞI APĂRARE; ASIGURĂRI SOCIALE OBLIGATORII", Category.SECTION),
        Classification("84", "Administraţie publică şi apărare; asigurări sociale obligatorii", Category.DIVISION),
        Classification("84.1", "Administraţie publică generală, economică şi socială", Category.GROUP),
        Classification("84.11", "Servicii de administraţie publică generală", Category.CLASS),
        Classification(
            "84.12",
            "Reglementarea activităţilor organismelor care prestează servicii în domeniul îngrijirii sănătăţii, învăţământului, culturii şi al altor activităţi sociale, exclusiv protecţia socială",
            Category.CLASS,
        ),
        Classification("84.13", "Reglementarea şi eficientizarea activităţilor economice", Category.CLASS),
        Classification("84.2", "Activităţi de servicii pentru societate", Category.GROUP),
        Classification("84.21", "Activităţi de afaceri externe", Category.CLASS),
        Classification("84.22", "Activităţi de apărare naţională", Category.CLASS),
        Classification("84.23", "Activităţi de justiţie", Category.CLASS),
        Classification("84.24", "Activităţi de ordine publică şi de protecţie civilă", Category.CLASS),
        Classification("84.25", "Activităţi de luptă împotriva incendiilor şi de prevenire a acestora", Category.CLASS),
        Classification("84.3", "Activităţi de protecţie socială obligatorie", Category.GROUP),
        Classification("84.30", "Activităţi de protecţie socială obligatorie", Category.CLASS),
        Classification("P", "ÎNVĂŢĂMÂNT", Category.SECTION),
        Classification("85", "Învăţământ", Category.DIVISION),
        Classification("85.1", "Învăţământ preşcolar", Category.GROUP),
        Classification("85.10", "Învăţământ preşcolar", Category.CLASS),
        Classification("85.2", "Învăţământ primar", Category.GROUP),
        Classification("85.20", "Învăţământ primar", Category.CLASS),
        Classification("85.3", "Învăţământ secundar", Category.GROUP),
        Classification("85.31", "Învăţământ secundar general", Category.CLASS),
        Classification("85.32", "Învăţământ secundar, tehnic sau profesional", Category.CLASS),
        Classification("85.4", "Învăţământ superior", Category.GROUP),
        Classification("85.41", "Învăţământ superior non-universitar", Category.CLASS),
        Classification("85.42", "Învăţământ superior universitar", Category.CLASS),
        Classification("85.5", "Alte forme de învăţământ", Category.GROUP),
        Classification("85.51", "Învăţământ în domeniul sportiv şi recreaţional", Category.CLASS),
        Classification(
            "85.52", "Învăţământ artistic (muzică, teatru, coreografie, arte plastice şi altele)", Category.CLASS
        ),
        Classification("85.53", "Şcoli de conducere (pilotaj)", Category.CLASS),
        Classification("85.59", "Alte forme de învăţământ n.c.a.", Category.CLASS),
        Classification("85.6", "Activităţi de servicii suport pentru învăţământ", Category.GROUP),
        Classification("85.60", "Activităţi de servicii suport pentru învăţământ", Category.CLASS),
        Classification("Q", "SĂNĂTATE ŞI ASISTENŢĂ SOCIALĂ", Category.SECTION),
        Classification("86", "Activităţi referitoare la sănătatea umană", Category.DIVISION),
        Classification("86.1", "Activităţi de asistenţă spitalicească", Category.GROUP),
        Classification("86.10", "Activităţi de asistenţă spitalicească", Category.CLASS),
        Classification("86.2", "Activităţi de asistenţă medicală ambulatorie şi stomatologică", Category.GROUP),
        Classification("86.21", "Activităţi de asistenţă medicală generală", Category.CLASS),
        Classification("86.22", "Activităţi de asistenţă medicală specializată", Category.CLASS),
        Classification("86.23", "Activităţi de asistenţă stomatologică", Category.CLASS),
        Classification("86.9", "Alte activităţi referitoare la sănătatea umană", Category.GROUP),
        Classification("86.90", "Alte activităţi referitoare la sănătatea umană", Category.CLASS),
        Classification(
            "87", "Servicii combinate de îngrijire medicală şi asistenţă socială, cu cazare", Category.DIVISION
        ),
        Classification("87.1", "Activităţi ale centrelor de îngrijire medicală", Category.GROUP),
        Classification("87.10", "Activităţi ale centrelor de îngrijire medicală", Category.CLASS),
        Classification(
            "87.2",
            "Activităţi ale centrelor de recuperare psihică şi de dezintoxicare, exclusiv spitale",
            Category.GROUP,
        ),
        Classification(
            "87.20",
            "Activităţi ale centrelor de recuperare psihică şi de dezintoxicare, exclusiv spitale",
            Category.CLASS,
        ),
        Classification(
            "87.3",
            "Activităţi ale căminelor de bătrâni şi ale căminelor pentru persoane aflate în incapacitate de a se îngriji singure",
            Category.GROUP,
        ),
        Classification(
            "87.30",
            "Activităţi ale căminelor de bătrâni şi ale căminelor pentru persoane aflate în incapacitate de a se îngriji singure",
            Category.CLASS,
        ),
        Classification("87.9", "Alte activităţi de asistenţă socială, cu cazare n.c.a.", Category.GROUP),
        Classification("87.90", "Alte activităţi de asistenţă socială, cu cazare n.c.a.", Category.CLASS),
        Classification("88", "Activităţi de asistenţă socială, fără cazare", Category.DIVISION),
        Classification(
            "88.1",
            "Activităţi de asistenţă socială, fără cazare, pentru bătrâni şi pentru persoane cu dizabilităţi",
            Category.GROUP,
        ),
        Classification(
            "88.10",
            "Activităţi de asistenţă socială, fără cazare, pentru bătrâni şi pentru persoane cu dizabilităţi",
            Category.CLASS,
        ),
        Classification("88.9", "Alte activităţi de asistenţă socială, fără cazare", Category.GROUP),
        Classification("88.91", "Activităţi de îngrijire zilnică pentru copii", Category.CLASS),
        Classification("88.99", "Alte activităţi de asistenţă socială, fără cazare, n.c.a.", Category.CLASS),
        Classification("R", "ARTĂ, ACTIVITĂŢI DE RECREERE ŞI DE AGREMENT", Category.SECTION),
        Classification("90", "Activităţi de creaţie şi interpretare artistică", Category.DIVISION),
        Classification("90.0", "Activităţi de creaţie şi interpretare artistică", Category.GROUP),
        Classification("90.01", "Activităţi de interpretare artistică (spectacole)", Category.CLASS),
        Classification("90.02", "Activităţi suport pentru interpretarea artistică (spectacole)", Category.CLASS),
        Classification("90.03", "Activităţi de creaţie artistică", Category.CLASS),
        Classification("90.04", "Activităţi de gestionare a sălilor de spectacole", Category.CLASS),
        Classification(
            "91", "Activităţi ale bibliotecilor, arhivelor, muzeelor şi alte activităţi culturale", Category.DIVISION
        ),
        Classification(
            "91.0", "Activităţi ale bibliotecilor, arhivelor, muzeelor şi alte activităţi culturale", Category.GROUP
        ),
        Classification("91.01", "Activităţi ale bibliotecilor şi arhivelor", Category.CLASS),
        Classification("91.02", "Activităţi ale muzeelor", Category.CLASS),
        Classification(
            "91.03",
            "Gestionarea monumentelor, clădirilor istorice şi a altor obiective de interes turistic",
            Category.CLASS,
        ),
        Classification(
            "91.04", "Activităţi ale grădinilor zoologice, botanice şi ale rezervaţiilor naturale", Category.CLASS
        ),
        Classification("92", "Activităţi de jocuri de noroc şi pariuri", Category.DIVISION),
        Classification("92.0", "Activităţi de jocuri de noroc şi pariuri", Category.GROUP),
        Classification("92.00", "Activităţi de jocuri de noroc şi pariuri", Category.CLASS),
        Classification("93", "Activităţi sportive, recreative şi distractive", Category.DIVISION),
        Classification("93.1", "Activităţi sportive", Category.GROUP),
        Classification("93.11", "Activităţi ale bazelor sportive", Category.CLASS),
        Classification("93.12", "Activităţi ale cluburilor sportive", Category.CLASS),
        Classification("93.13", "Activităţi ale centrelor de fitness", Category.CLASS),
        Classification("93.19", "Alte activităţi sportive", Category.CLASS),
        Classification("93.2", "Alte activităţi recreative şi distractive", Category.GROUP),
        Classification("93.21", "Parcuri tematice (bâlciuri) şi parcuri de distracţii", Category.CLASS),
        Classification("93.29", "Alte activităţi recreative şi distractive n.c.a.", Category.CLASS),
        Classification("S", "ALTE ACTIVITĂŢI DE SERVICII", Category.SECTION),
        Classification("94", "Activităţi ale organizaţiilor asociative", Category.DIVISION),
        Classification("94.1", "Activităţi ale organizaţiilor economice, patronale şi profesionale", Category.GROUP),
        Classification("94.11", "Activităţi ale organizaţiilor economice şi patronale", Category.CLASS),
        Classification("94.12", "Activităţi ale organizaţiilor profesionale", Category.CLASS),
        Classification("94.2", "Activităţi ale sindicatelor salariaţilor", Category.GROUP),
        Classification("94.20", "Activităţi ale sindicatelor salariaţilor", Category.CLASS),
        Classification("94.9", "Alte activităţi ale organizaţiilor asociative", Category.GROUP),
        Classification("94.91", "Activităţi ale organizaţiilor religioase", Category.CLASS),
        Classification("94.92", "Activităţi ale organizaţiilor politice", Category.CLASS),
        Classification("94.99", "Activităţi ale altor organizaţii n.c.a.", Category.CLASS),
        Classification(
            "95", "Reparaţii de calculatoare, de articole personale şi de uz gospodăresc", Category.DIVISION
        ),
        Classification("95.1", "Repararea calculatoarelor şi a echipamentelor de comunicaţii", Category.GROUP),
        Classification("95.11", "Repararea calculatoarelor şi a echipamentelor periferice", Category.CLASS),
        Classification("95.12", "Repararea echipamentelor de comunicaţii", Category.CLASS),
        Classification("95.2", "Reparaţii de articole personale şi de uz gospodăresc", Category.GROUP),
        Classification("95.21", "Repararea aparatelor electronice de uz casnic", Category.CLASS),
        Classification(
            "95.22",
            "Repararea dispozitivelor de uz gospodăresc şi a echipamentelor pentru casă şi grădină",
            Category.CLASS,
        ),
        Classification("95.23", "Repararea încălţămintei şi a articolelor din piele", Category.CLASS),
        Classification("95.24", "Repararea mobilei şi a furniturilor casnice", Category.CLASS),
        Classification("95.25", "Repararea ceasurilor şi a bijuteriilor", Category.CLASS),
        Classification("95.29", "Repararea articolelor de uz personal şi gospodăresc n.c.a.", Category.CLASS),
        Classification("96", "Alte activităţi de servicii personale", Category.DIVISION),
        Classification("96.0", "Alte activităţi de servicii personale", Category.GROUP),
        Classification(
            "96.01", "Spălarea şi curăţarea (uscată) articolelor textile şi a produselor din  blană", Category.CLASS
        ),
        Classification("96.02", "Coafură şi alte activităţi de înfrumuseţare", Category.CLASS),
        Classification("96.03", "Activităţi de pompe funebre şi similare", Category.CLASS),
        Classification("96.04", "Activităţi de întreţinere corporală", Category.CLASS),
        Classification("96.09", "Alte activităţi de servicii personale n.c.a.", Category.CLASS),
        Classification(
            "T",
            "ACTIVITĂŢI ALE GOSPODĂRIILOR PRIVATE ÎN CALITATE DE ANGAJATOR DE PERSONAL CASNIC; ACTIVITĂŢI ALE GOSPODĂRIILOR PRIVATE DE PRODUCERE DE BUNURI ŞI SERVICII DESTINATE CONSUMULUI PROPRIU",
            Category.SECTION,
        ),
        Classification(
            "97", "Activităţi ale gospodăriilor private în calitate de angajator de personal casnic", Category.DIVISION
        ),
        Classification(
            "97.0", "Activităţi ale gospodăriilor private în calitate de angajator de personal casnic", Category.GROUP
        ),
        Classification(
            "97.00", "Activităţi ale gospodăriilor private în calitate de angajator de personal casnic", Category.CLASS
        ),
        Classification(
            "98",
            "Activităţi ale gospodăriilor private de producere de bunuri şi servicii destinate consumului propriu",
            Category.DIVISION,
        ),
        Classification(
            "98.1",
            "Activităţi ale gospodăriilor private de producere de bunuri destinate consumului propriu",
            Category.GROUP,
        ),
        Classification(
            "98.10",
            "Activităţi ale gospodăriilor private de producere de bunuri destinate consumului propriu",
            Category.CLASS,
        ),
        Classification(
            "98.2",
            "Activităţi ale gospodăriilor private de producere de servicii pentru scopuri proprii",
            Category.GROUP,
        ),
        Classification(
            "98.20",
            "Activităţi ale gospodăriilor private de producere de servicii pentru scopuri proprii",
            Category.CLASS,
        ),
        Classification("U", "ACTIVITĂŢI ALE ORGANIZAŢIILOR ŞI ORGANISMELOR EXTRATERITORIALE", Category.SECTION),
        Classification("99", "Activităţi ale organizaţiilor şi organismelor extrateritoriale", Category.DIVISION),
        Classification("99.0", "Activităţi ale organizaţiilor şi organismelor extrateritoriale", Category.GROUP),
        Classification("99.00", "Activităţi ale organizaţiilor şi organismelor extrateritoriale", Category.CLASS),
    ],
)
