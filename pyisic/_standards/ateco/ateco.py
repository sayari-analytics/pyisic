"""`ATECO Standard <https://www.istat.it/classificazione/documenti-ateco/>`_."""

from ...types import Category, Classification, Standard, Standards

ATECO = Standard(
    standard=Standards.ATECO,
    classes=[
        Classification("A", "AGRICOLTURA, SILVICOLTURA E PESCA", Category.SECTION),
        Classification("01", "Produzioni vegetali e animali, caccia e servizi connessi", Category.DIVISION),
        Classification("01.1", "Coltivazione di colture agricole non permanenti", Category.GROUP),
        Classification(
            "01.11", "Coltivazione di cereali, legumi da granella e semi oleosi, escluso il riso", Category.CLASS
        ),
        Classification(
            "01.11.0", "Coltivazione di cereali, legumi da granella e semi oleosi, escluso il riso", Category.SUBCLASS
        ),
        Classification(
            "01.11.00", "Coltivazione di cereali, legumi da granella e semi oleosi, escluso il riso", Category.SUBCLASS
        ),
        Classification("01.12", "Coltivazione di riso", Category.CLASS),
        Classification("01.12.0", "Coltivazione di riso", Category.SUBCLASS),
        Classification("01.12.00", "Coltivazione di riso", Category.SUBCLASS),
        Classification("01.13", "Coltivazione di ortaggi e meloni, radici e tuberi", Category.CLASS),
        Classification("01.13.1", "Coltivazione di ortaggi e meloni", Category.SUBCLASS),
        Classification("01.13.11", "Coltivazione di ortaggi e meloni in piena aria", Category.SUBCLASS),
        Classification(
            "01.13.12", "Coltivazione di ortaggi e meloni in colture protette fuori suolo", Category.SUBCLASS
        ),
        Classification(
            "01.13.13",
            "Coltivazione di ortaggi e meloni in altre colture protette, escluse colture fuori suolo",
            Category.SUBCLASS,
        ),
        Classification("01.13.2", "Coltivazione di radici, incluse barbabietole da zucchero", Category.SUBCLASS),
        Classification("01.13.20", "Coltivazione di radici, incluse barbabietole da zucchero", Category.SUBCLASS),
        Classification("01.13.3", "Coltivazione di tuberi, incluse patate", Category.SUBCLASS),
        Classification("01.13.30", "Coltivazione di tuberi, incluse patate", Category.SUBCLASS),
        Classification("01.14", "Coltivazione di canna da zucchero", Category.CLASS),
        Classification("01.14.0", "Coltivazione di canna da zucchero", Category.SUBCLASS),
        Classification("01.14.00", "Coltivazione di canna da zucchero", Category.SUBCLASS),
        Classification("01.15", "Coltivazione di tabacco", Category.CLASS),
        Classification("01.15.0", "Coltivazione di tabacco", Category.SUBCLASS),
        Classification("01.15.00", "Coltivazione di tabacco", Category.SUBCLASS),
        Classification("01.16", "Coltivazione di piante tessili", Category.CLASS),
        Classification("01.16.0", "Coltivazione di piante tessili", Category.SUBCLASS),
        Classification("01.16.00", "Coltivazione di piante tessili", Category.SUBCLASS),
        Classification("01.19", "Coltivazione di altre colture agricole non permanenti", Category.CLASS),
        Classification("01.19.1", "Coltivazione di fiori", Category.SUBCLASS),
        Classification("01.19.11", "Coltivazione di fiori in piena aria", Category.SUBCLASS),
        Classification("01.19.12", "Coltivazione di fiori in colture protette fuori suolo", Category.SUBCLASS),
        Classification(
            "01.19.13",
            "Coltivazione di fiori in altre colture protette, escluse colture fuori suolo",
            Category.SUBCLASS,
        ),
        Classification(
            "01.19.9",
            "Coltivazione di piante da foraggio e di altre colture agricole non permanenti n.c.a.",
            Category.SUBCLASS,
        ),
        Classification(
            "01.19.90",
            "Coltivazione di piante da foraggio e di altre colture agricole non permanenti n.c.a.",
            Category.SUBCLASS,
        ),
        Classification("01.2", "Coltivazione di colture agricole permanenti", Category.GROUP),
        Classification("01.21", "Coltivazione di uva", Category.CLASS),
        Classification("01.21.0", "Coltivazione di uva", Category.SUBCLASS),
        Classification("01.21.00", "Coltivazione di uva", Category.SUBCLASS),
        Classification("01.22", "Coltivazione di frutta di origine tropicale e subtropicale", Category.CLASS),
        Classification("01.22.0", "Coltivazione di frutta di origine tropicale e subtropicale", Category.SUBCLASS),
        Classification("01.22.00", "Coltivazione di frutta di origine tropicale e subtropicale", Category.SUBCLASS),
        Classification("01.23", "Coltivazione di agrumi", Category.CLASS),
        Classification("01.23.0", "Coltivazione di agrumi", Category.SUBCLASS),
        Classification("01.23.00", "Coltivazione di agrumi", Category.SUBCLASS),
        Classification("01.24", "Coltivazione di pomacee e frutta a nocciolo", Category.CLASS),
        Classification("01.24.0", "Coltivazione di pomacee e frutta a nocciolo", Category.SUBCLASS),
        Classification("01.24.00", "Coltivazione di pomacee e frutta a nocciolo", Category.SUBCLASS),
        Classification(
            "01.25", "Coltivazione di altri alberi da frutto, frutti di bosco e frutta in guscio", Category.CLASS
        ),
        Classification(
            "01.25.0", "Coltivazione di altri alberi da frutto, frutti di bosco e frutta in guscio", Category.SUBCLASS
        ),
        Classification(
            "01.25.00", "Coltivazione di altri alberi da frutto, frutti di bosco e frutta in guscio", Category.SUBCLASS
        ),
        Classification("01.26", "Coltivazione di frutti oleosi", Category.CLASS),
        Classification("01.26.0", "Coltivazione di frutti oleosi", Category.SUBCLASS),
        Classification("01.26.00", "Coltivazione di frutti oleosi", Category.SUBCLASS),
        Classification("01.27", "Coltivazione di piante per la produzione di bevande", Category.CLASS),
        Classification("01.27.0", "Coltivazione di piante per la produzione di bevande", Category.SUBCLASS),
        Classification("01.27.00", "Coltivazione di piante per la produzione di bevande", Category.SUBCLASS),
        Classification("01.28", "Coltivazione di spezie, piante aromatiche e farmaceutiche", Category.CLASS),
        Classification("01.28.0", "Coltivazione di spezie, piante aromatiche e farmaceutiche", Category.SUBCLASS),
        Classification("01.28.00", "Coltivazione di spezie, piante aromatiche e farmaceutiche", Category.SUBCLASS),
        Classification("01.29", "Coltivazione di altre colture agricole permanenti", Category.CLASS),
        Classification("01.29.0", "Coltivazione di altre colture agricole permanenti", Category.SUBCLASS),
        Classification("01.29.00", "Coltivazione di altre colture agricole permanenti", Category.SUBCLASS),
        Classification("01.3", "Riproduzione delle piante", Category.GROUP),
        Classification("01.30", "Riproduzione delle piante", Category.CLASS),
        Classification("01.30.0", "Riproduzione delle piante", Category.SUBCLASS),
        Classification("01.30.00", "Riproduzione delle piante", Category.SUBCLASS),
        Classification("01.4", "Allevamento di animali", Category.GROUP),
        Classification("01.41", "Allevamento di bovini da latte", Category.CLASS),
        Classification("01.41.0", "Allevamento di bovini da latte", Category.SUBCLASS),
        Classification("01.41.00", "Allevamento di bovini da latte", Category.SUBCLASS),
        Classification("01.42", "Allevamento di altri bovini e bufalini", Category.CLASS),
        Classification("01.42.0", "Allevamento di altri bovini e bufalini", Category.SUBCLASS),
        Classification("01.42.00", "Allevamento di altri bovini e bufalini", Category.SUBCLASS),
        Classification("01.43", "Allevamento di cavalli e altri equini", Category.CLASS),
        Classification("01.43.0", "Allevamento di cavalli e altri equini", Category.SUBCLASS),
        Classification("01.43.00", "Allevamento di cavalli e altri equini", Category.SUBCLASS),
        Classification("01.44", "Allevamento di cammelli e camelidi", Category.CLASS),
        Classification("01.44.0", "Allevamento di cammelli e camelidi", Category.SUBCLASS),
        Classification("01.44.00", "Allevamento di cammelli e camelidi", Category.SUBCLASS),
        Classification("01.45", "Allevamento di ovini e caprini", Category.CLASS),
        Classification("01.45.0", "Allevamento di ovini e caprini", Category.SUBCLASS),
        Classification("01.45.00", "Allevamento di ovini e caprini", Category.SUBCLASS),
        Classification("01.46", "Allevamento di suini", Category.CLASS),
        Classification("01.46.0", "Allevamento di suini", Category.SUBCLASS),
        Classification("01.46.00", "Allevamento di suini", Category.SUBCLASS),
        Classification("01.47", "Allevamento di pollame", Category.CLASS),
        Classification("01.47.0", "Allevamento di pollame", Category.SUBCLASS),
        Classification("01.47.00", "Allevamento di pollame", Category.SUBCLASS),
        Classification("01.48", "Allevamento di altri animali", Category.CLASS),
        Classification("01.48.1", "Allevamento di conigli", Category.SUBCLASS),
        Classification("01.48.10", "Allevamento di conigli", Category.SUBCLASS),
        Classification("01.48.2", "Allevamento di altri animali da pelliccia", Category.SUBCLASS),
        Classification("01.48.20", "Allevamento di altri animali da pelliccia", Category.SUBCLASS),
        Classification("01.48.3", "Apicoltura", Category.SUBCLASS),
        Classification("01.48.30", "Apicoltura", Category.SUBCLASS),
        Classification("01.48.4", "Bachicoltura", Category.SUBCLASS),
        Classification("01.48.40", "Bachicoltura", Category.SUBCLASS),
        Classification("01.48.9", "Allevamento di altri animali n.c.a.", Category.SUBCLASS),
        Classification("01.48.91", "Allevamento di insetti", Category.SUBCLASS),
        Classification("01.48.99", "Allevamento di altri animali vari n.c.a.", Category.SUBCLASS),
        Classification(
            "01.5", "Coltivazioni agricole associate all'allevamento di animali: attività mista", Category.GROUP
        ),
        Classification(
            "01.50", "Coltivazioni agricole associate all'allevamento di animali: attività mista", Category.CLASS
        ),
        Classification(
            "01.50.0", "Coltivazioni agricole associate all'allevamento di animali: attività mista", Category.SUBCLASS
        ),
        Classification(
            "01.50.00", "Coltivazioni agricole associate all'allevamento di animali: attività mista", Category.SUBCLASS
        ),
        Classification(
            "01.6", "Attività di supporto all'agricoltura e attività successive alla raccolta", Category.GROUP
        ),
        Classification("01.61", "Attività di supporto alla produzione vegetale", Category.CLASS),
        Classification("01.61.1", "Manutenzione del terreno per mantenerlo in buone condizioni", Category.SUBCLASS),
        Classification("01.61.10", "Manutenzione del terreno per mantenerlo in buone condizioni", Category.SUBCLASS),
        Classification("01.61.9", "Attività di supporto alla produzione vegetale n.c.a.", Category.SUBCLASS),
        Classification("01.61.91", "Trattamenti fitosanitari", Category.SUBCLASS),
        Classification("01.61.99", "Altre attività di supporto alla produzione vegetale n.c.a.", Category.SUBCLASS),
        Classification("01.62", "Attività di supporto alla produzione animale", Category.CLASS),
        Classification("01.62.0", "Attività di supporto alla produzione animale", Category.SUBCLASS),
        Classification("01.62.01", "Attività di maniscalchi", Category.SUBCLASS),
        Classification("01.62.09", "Altre attività di supporto alla produzione animale", Category.SUBCLASS),
        Classification(
            "01.63", "Attività successive alla raccolta e lavorazione delle sementi per la semina", Category.CLASS
        ),
        Classification("01.63.1", "Attività successive alla raccolta", Category.SUBCLASS),
        Classification("01.63.10", "Attività successive alla raccolta", Category.SUBCLASS),
        Classification("01.63.2", "Lavorazione delle sementi per la semina", Category.SUBCLASS),
        Classification("01.63.20", "Lavorazione delle sementi per la semina", Category.SUBCLASS),
        Classification("01.7", "Caccia, cattura di animali e servizi connessi", Category.GROUP),
        Classification("01.70", "Caccia, cattura di animali e servizi connessi", Category.CLASS),
        Classification("01.70.0", "Caccia, cattura di animali e servizi connessi", Category.SUBCLASS),
        Classification("01.70.00", "Caccia, cattura di animali e servizi connessi", Category.SUBCLASS),
        Classification("02", "Silvicoltura e utilizzo di aree forestali", Category.DIVISION),
        Classification("02.1", "Silvicoltura e altre attività forestali", Category.GROUP),
        Classification("02.10", "Silvicoltura e altre attività forestali", Category.CLASS),
        Classification("02.10.0", "Silvicoltura e altre attività forestali", Category.SUBCLASS),
        Classification("02.10.00", "Silvicoltura e altre attività forestali", Category.SUBCLASS),
        Classification("02.2", "Utilizzo di aree forestali", Category.GROUP),
        Classification("02.20", "Utilizzo di aree forestali", Category.CLASS),
        Classification("02.20.0", "Utilizzo di aree forestali", Category.SUBCLASS),
        Classification("02.20.00", "Utilizzo di aree forestali", Category.SUBCLASS),
        Classification("02.3", "Raccolta di prodotti selvatici non legnosi", Category.GROUP),
        Classification("02.30", "Raccolta di prodotti selvatici non legnosi", Category.CLASS),
        Classification("02.30.0", "Raccolta di prodotti selvatici non legnosi", Category.SUBCLASS),
        Classification("02.30.00", "Raccolta di prodotti selvatici non legnosi", Category.SUBCLASS),
        Classification("02.4", "Servizi di supporto per la silvicoltura", Category.GROUP),
        Classification("02.40", "Servizi di supporto per la silvicoltura", Category.CLASS),
        Classification("02.40.0", "Servizi di supporto per la silvicoltura", Category.SUBCLASS),
        Classification("02.40.00", "Servizi di supporto per la silvicoltura", Category.SUBCLASS),
        Classification("03", "Pesca e acquacoltura", Category.DIVISION),
        Classification("03.1", "Pesca", Category.GROUP),
        Classification("03.11", "Pesca marina", Category.CLASS),
        Classification("03.11.0", "Pesca marina", Category.SUBCLASS),
        Classification("03.11.00", "Pesca marina", Category.SUBCLASS),
        Classification("03.12", "Pesca in acque dolci", Category.CLASS),
        Classification("03.12.0", "Pesca in acque dolci", Category.SUBCLASS),
        Classification("03.12.00", "Pesca in acque dolci", Category.SUBCLASS),
        Classification("03.2", "Acquacoltura", Category.GROUP),
        Classification("03.21", "Acquacoltura marina", Category.CLASS),
        Classification("03.21.0", "Acquacoltura marina", Category.SUBCLASS),
        Classification("03.21.01", "Coltivazione di alghe marine", Category.SUBCLASS),
        Classification("03.21.09", "Altre attività di acquacoltura marina", Category.SUBCLASS),
        Classification("03.22", "Acquacoltura in acque dolci", Category.CLASS),
        Classification("03.22.0", "Acquacoltura in acque dolci", Category.SUBCLASS),
        Classification("03.22.01", "Coltivazione di alghe in acque dolci", Category.SUBCLASS),
        Classification("03.22.09", "Altre attività di acquacoltura in acque dolci", Category.SUBCLASS),
        Classification("03.3", "Attività di supporto alla pesca e all'acquacoltura", Category.GROUP),
        Classification("03.30", "Attività di supporto alla pesca e all'acquacoltura", Category.CLASS),
        Classification("03.30.0", "Attività di supporto alla pesca e all'acquacoltura", Category.SUBCLASS),
        Classification("03.30.00", "Attività di supporto alla pesca e all'acquacoltura", Category.SUBCLASS),
        Classification("B", "ATTIVITÀ ESTRATTIVE", Category.SECTION),
        Classification("05", "Estrazione di carbone e lignite", Category.DIVISION),
        Classification("05.1", "Estrazione di antracite", Category.GROUP),
        Classification("05.10", "Estrazione di antracite", Category.CLASS),
        Classification("05.10.0", "Estrazione di antracite", Category.SUBCLASS),
        Classification("05.10.00", "Estrazione di antracite", Category.SUBCLASS),
        Classification("05.2", "Estrazione di lignite", Category.GROUP),
        Classification("05.20", "Estrazione di lignite", Category.CLASS),
        Classification("05.20.0", "Estrazione di lignite", Category.SUBCLASS),
        Classification("05.20.00", "Estrazione di lignite", Category.SUBCLASS),
        Classification("06", "Estrazione di petrolio greggio e gas naturale", Category.DIVISION),
        Classification("06.1", "Estrazione di petrolio greggio", Category.GROUP),
        Classification("06.10", "Estrazione di petrolio greggio", Category.CLASS),
        Classification("06.10.0", "Estrazione di petrolio greggio", Category.SUBCLASS),
        Classification("06.10.00", "Estrazione di petrolio greggio", Category.SUBCLASS),
        Classification("06.2", "Estrazione di gas naturale", Category.GROUP),
        Classification("06.20", "Estrazione di gas naturale", Category.CLASS),
        Classification("06.20.0", "Estrazione di gas naturale", Category.SUBCLASS),
        Classification("06.20.00", "Estrazione di gas naturale", Category.SUBCLASS),
        Classification("07", "Estrazione di minerali metalliferi", Category.DIVISION),
        Classification("07.1", "Estrazione di minerali metalliferi ferrosi", Category.GROUP),
        Classification("07.10", "Estrazione di minerali metalliferi ferrosi", Category.CLASS),
        Classification("07.10.0", "Estrazione di minerali metalliferi ferrosi", Category.SUBCLASS),
        Classification("07.10.00", "Estrazione di minerali metalliferi ferrosi", Category.SUBCLASS),
        Classification("07.2", "Estrazione di minerali metalliferi non ferrosi", Category.GROUP),
        Classification("07.21", "Estrazione di minerali di uranio e torio", Category.CLASS),
        Classification("07.21.0", "Estrazione di minerali di uranio e torio", Category.SUBCLASS),
        Classification("07.21.00", "Estrazione di minerali di uranio e torio", Category.SUBCLASS),
        Classification("07.29", "Estrazione di altri minerali metalliferi non ferrosi", Category.CLASS),
        Classification("07.29.0", "Estrazione di altri minerali metalliferi non ferrosi", Category.SUBCLASS),
        Classification("07.29.00", "Estrazione di altri minerali metalliferi non ferrosi", Category.SUBCLASS),
        Classification("08", "Altre attività estrattive", Category.DIVISION),
        Classification("08.1", "Estrazione di pietra, sabbia e argilla", Category.GROUP),
        Classification(
            "08.11",
            "Estrazione di pietre ornamentali, calcare, pietra di gesso, ardesia e altre pietre",
            Category.CLASS,
        ),
        Classification(
            "08.11.0",
            "Estrazione di pietre ornamentali, calcare, pietra di gesso, ardesia e altre pietre",
            Category.SUBCLASS,
        ),
        Classification(
            "08.11.00",
            "Estrazione di pietre ornamentali, calcare, pietra di gesso, ardesia e altre pietre",
            Category.SUBCLASS,
        ),
        Classification("08.12", "Estrazione di ghiaia, sabbia, argilla e caolino", Category.CLASS),
        Classification("08.12.0", "Estrazione di ghiaia, sabbia, argilla e caolino", Category.SUBCLASS),
        Classification("08.12.00", "Estrazione di ghiaia, sabbia, argilla e caolino", Category.SUBCLASS),
        Classification("08.9", "Attività estrattive n.c.a.", Category.GROUP),
        Classification(
            "08.91",
            "Estrazione di minerali per l'industria chimica e per la produzione di fertilizzanti",
            Category.CLASS,
        ),
        Classification(
            "08.91.0",
            "Estrazione di minerali per l'industria chimica e per la produzione di fertilizzanti",
            Category.SUBCLASS,
        ),
        Classification(
            "08.91.00",
            "Estrazione di minerali per l'industria chimica e per la produzione di fertilizzanti",
            Category.SUBCLASS,
        ),
        Classification("08.92", "Estrazione di torba", Category.CLASS),
        Classification("08.92.0", "Estrazione di torba", Category.SUBCLASS),
        Classification("08.92.00", "Estrazione di torba", Category.SUBCLASS),
        Classification("08.93", "Estrazione di sale", Category.CLASS),
        Classification("08.93.0", "Estrazione di sale", Category.SUBCLASS),
        Classification("08.93.01", "Estrazione di sale dal sottosuolo", Category.SUBCLASS),
        Classification("08.93.02", "Salicoltura marina", Category.SUBCLASS),
        Classification("08.93.03", "Produzione di sale da salamoia", Category.SUBCLASS),
        Classification("08.99", "Altre attività estrattive n.c.a.", Category.CLASS),
        Classification("08.99.0", "Altre attività estrattive n.c.a.", Category.SUBCLASS),
        Classification("08.99.01", "Estrazione di asfalto e bitume naturale", Category.SUBCLASS),
        Classification("08.99.09", "Altre attività estrattive varie n.c.a.", Category.SUBCLASS),
        Classification("09", "Attività dei servizi di supporto all'estrazione", Category.DIVISION),
        Classification("09.1", "Attività di supporto all'estrazione di petrolio e gas naturale", Category.GROUP),
        Classification("09.10", "Attività di supporto all'estrazione di petrolio e gas naturale", Category.CLASS),
        Classification("09.10.0", "Attività di supporto all'estrazione di petrolio e gas naturale", Category.SUBCLASS),
        Classification("09.10.00", "Attività di supporto all'estrazione di petrolio e gas naturale", Category.SUBCLASS),
        Classification("09.9", "Attività di supporto ad altre attività estrattive", Category.GROUP),
        Classification("09.90", "Attività di supporto ad altre attività estrattive", Category.CLASS),
        Classification("09.90.0", "Attività di supporto ad altre attività estrattive", Category.SUBCLASS),
        Classification("09.90.00", "Attività di supporto ad altre attività estrattive", Category.SUBCLASS),
        Classification("C", "ATTIVITÀ MANIFATTURIERE", Category.SECTION),
        Classification("10", "Produzione di prodotti alimentari", Category.DIVISION),
        Classification(
            "10.1", "Lavorazione e conservazione di carne e produzione di prodotti a base di carne", Category.GROUP
        ),
        Classification("10.11", "Lavorazione e conservazione di carne, esclusa la carne di volatili", Category.CLASS),
        Classification(
            "10.11.0", "Lavorazione e conservazione di carne, esclusa la carne di volatili", Category.SUBCLASS
        ),
        Classification(
            "10.11.00", "Lavorazione e conservazione di carne, esclusa la carne di volatili", Category.SUBCLASS
        ),
        Classification("10.12", "Lavorazione e conservazione di carne di volatili", Category.CLASS),
        Classification("10.12.0", "Lavorazione e conservazione di carne di volatili", Category.SUBCLASS),
        Classification("10.12.00", "Lavorazione e conservazione di carne di volatili", Category.SUBCLASS),
        Classification(
            "10.13",
            "Produzione di prodotti a base di carne, inclusi prodotti a base di carne di volatili",
            Category.CLASS,
        ),
        Classification(
            "10.13.0",
            "Produzione di prodotti a base di carne, inclusi prodotti a base di carne di volatili",
            Category.SUBCLASS,
        ),
        Classification(
            "10.13.00",
            "Produzione di prodotti a base di carne, inclusi prodotti a base di carne di volatili",
            Category.SUBCLASS,
        ),
        Classification("10.2", "Lavorazione e conservazione di pesce, crostacei e molluschi", Category.GROUP),
        Classification("10.20", "Lavorazione e conservazione di pesce, crostacei e molluschi", Category.CLASS),
        Classification("10.20.0", "Lavorazione e conservazione di pesce, crostacei e molluschi", Category.SUBCLASS),
        Classification("10.20.01", "Lavorazione di alghe", Category.SUBCLASS),
        Classification(
            "10.20.09",
            "Altre attività di lavorazione e conservazione di pesce, crostacei e molluschi",
            Category.SUBCLASS,
        ),
        Classification("10.3", "Lavorazione e conservazione di frutta e ortaggi", Category.GROUP),
        Classification("10.31", "Lavorazione e conservazione di patate", Category.CLASS),
        Classification("10.31.0", "Lavorazione e conservazione di patate", Category.SUBCLASS),
        Classification("10.31.00", "Lavorazione e conservazione di patate", Category.SUBCLASS),
        Classification("10.32", "Produzione di succhi a base di frutta e ortaggi", Category.CLASS),
        Classification("10.32.0", "Produzione di succhi a base di frutta e ortaggi", Category.SUBCLASS),
        Classification("10.32.00", "Produzione di succhi a base di frutta e ortaggi", Category.SUBCLASS),
        Classification("10.39", "Altre attività di lavorazione e conservazione di frutta e ortaggi", Category.CLASS),
        Classification(
            "10.39.0", "Altre attività di lavorazione e conservazione di frutta e ortaggi", Category.SUBCLASS
        ),
        Classification(
            "10.39.00", "Altre attività di lavorazione e conservazione di frutta e ortaggi", Category.SUBCLASS
        ),
        Classification("10.4", "Produzione di oli e grassi vegetali e animali", Category.GROUP),
        Classification("10.41", "Produzione di oli e grassi", Category.CLASS),
        Classification("10.41.1", "Produzione di olio di oliva", Category.SUBCLASS),
        Classification("10.41.10", "Produzione di olio di oliva", Category.SUBCLASS),
        Classification("10.41.2", "Produzione di altri oli vegetali", Category.SUBCLASS),
        Classification("10.41.20", "Produzione di altri oli vegetali", Category.SUBCLASS),
        Classification("10.41.3", "Produzione di oli e grassi animali", Category.SUBCLASS),
        Classification("10.41.30", "Produzione di oli e grassi animali", Category.SUBCLASS),
        Classification("10.42", "Produzione di margarina e di grassi alimentari simili", Category.CLASS),
        Classification("10.42.0", "Produzione di margarina e di grassi alimentari simili", Category.SUBCLASS),
        Classification("10.42.00", "Produzione di margarina e di grassi alimentari simili", Category.SUBCLASS),
        Classification("10.5", "Produzione di prodotti lattiero-caseari e gelati", Category.GROUP),
        Classification("10.51", "Produzione di prodotti lattiero-caseari", Category.CLASS),
        Classification("10.51.1", "Trattamento igienico del latte", Category.SUBCLASS),
        Classification("10.51.10", "Trattamento igienico del latte", Category.SUBCLASS),
        Classification("10.51.2", "Produzione di derivati del latte", Category.SUBCLASS),
        Classification("10.51.20", "Produzione di derivati del latte", Category.SUBCLASS),
        Classification("10.52", "Produzione di gelati", Category.CLASS),
        Classification("10.52.0", "Produzione di gelati", Category.SUBCLASS),
        Classification("10.52.00", "Produzione di gelati", Category.SUBCLASS),
        Classification("10.6", "Lavorazione di granaglie, produzione di amidi e di prodotti amidacei", Category.GROUP),
        Classification("10.61", "Lavorazione di granaglie", Category.CLASS),
        Classification("10.61.1", "Lavorazione di frumento e altri cereali", Category.SUBCLASS),
        Classification("10.61.11", "Lavorazione di frumento", Category.SUBCLASS),
        Classification("10.61.19", "Lavorazione di altri cereali", Category.SUBCLASS),
        Classification("10.61.2", "Lavorazione del riso", Category.SUBCLASS),
        Classification("10.61.20", "Lavorazione del riso", Category.SUBCLASS),
        Classification("10.61.9", "Lavorazioni di altre granaglie", Category.SUBCLASS),
        Classification("10.61.90", "Lavorazioni di altre granaglie", Category.SUBCLASS),
        Classification("10.62", "Produzione di amidi e di prodotti amidacei", Category.CLASS),
        Classification("10.62.0", "Produzione di amidi e di prodotti amidacei", Category.SUBCLASS),
        Classification("10.62.00", "Produzione di amidi e di prodotti amidacei", Category.SUBCLASS),
        Classification("10.7", "Produzione di prodotti da forno e farinacei", Category.GROUP),
        Classification("10.71", "Produzione di pane; produzione di prodotti di pasticceria freschi", Category.CLASS),
        Classification("10.71.1", "Produzione di pane e prodotti di panetteria simili", Category.SUBCLASS),
        Classification("10.71.10", "Produzione di pane e prodotti di panetteria simili", Category.SUBCLASS),
        Classification("10.71.2", "Produzione di prodotti di pasticceria freschi", Category.SUBCLASS),
        Classification("10.71.20", "Produzione di prodotti di pasticceria freschi", Category.SUBCLASS),
        Classification(
            "10.72", "Produzione di fette biscottate, biscotti, prodotti di pasticceria conservati", Category.CLASS
        ),
        Classification(
            "10.72.0", "Produzione di fette biscottate, biscotti, prodotti di pasticceria conservati", Category.SUBCLASS
        ),
        Classification(
            "10.72.00",
            "Produzione di fette biscottate, biscotti, prodotti di pasticceria conservati",
            Category.SUBCLASS,
        ),
        Classification("10.73", "Produzione di prodotti farinacei", Category.CLASS),
        Classification("10.73.0", "Produzione di prodotti farinacei", Category.SUBCLASS),
        Classification("10.73.01", "Produzione di prodotti farinacei freschi", Category.SUBCLASS),
        Classification("10.73.02", "Produzione di prodotti farinacei conservati", Category.SUBCLASS),
        Classification("10.8", "Produzione di altri prodotti alimentari", Category.GROUP),
        Classification("10.81", "Produzione di zucchero", Category.CLASS),
        Classification("10.81.0", "Produzione di zucchero", Category.SUBCLASS),
        Classification("10.81.00", "Produzione di zucchero", Category.SUBCLASS),
        Classification("10.82", "Produzione di cacao, cioccolato, caramelle e confetterie", Category.CLASS),
        Classification("10.82.0", "Produzione di cacao, cioccolato, caramelle e confetterie", Category.SUBCLASS),
        Classification("10.82.00", "Produzione di cacao, cioccolato, caramelle e confetterie", Category.SUBCLASS),
        Classification("10.83", "Lavorazione di tè e caffè", Category.CLASS),
        Classification("10.83.0", "Lavorazione di tè e caffè", Category.SUBCLASS),
        Classification("10.83.01", "Lavorazione di tè e di altri preparati per infusi", Category.SUBCLASS),
        Classification("10.83.02", "Lavorazione di caffè", Category.SUBCLASS),
        Classification("10.84", "Produzione di condimenti e spezie", Category.CLASS),
        Classification("10.84.0", "Produzione di condimenti e spezie", Category.SUBCLASS),
        Classification("10.84.00", "Produzione di condimenti e spezie", Category.SUBCLASS),
        Classification("10.85", "Produzione di pasti e piatti preparati", Category.CLASS),
        Classification("10.85.0", "Produzione di pasti e piatti preparati", Category.SUBCLASS),
        Classification(
            "10.85.01",
            "Produzione di pasti e piatti preparati a base di carne, inclusi pasti e piatti preparati a base di carne di volatili",
            Category.SUBCLASS,
        ),
        Classification("10.85.02", "Produzione di pasti e piatti preparati a base di pesce", Category.SUBCLASS),
        Classification("10.85.03", "Produzione di pasti e piatti preparati a base di ortaggi", Category.SUBCLASS),
        Classification("10.85.04", "Produzione di pizza surgelata o altrimenti conservata", Category.SUBCLASS),
        Classification("10.85.05", "Produzione di pasti e piatti preparati a base di pasta", Category.SUBCLASS),
        Classification("10.85.09", "Produzione di altri pasti e piatti preparati", Category.SUBCLASS),
        Classification("10.86", "Produzione di preparati omogeneizzati e di alimenti dietetici", Category.CLASS),
        Classification("10.86.0", "Produzione di preparati omogeneizzati e di alimenti dietetici", Category.SUBCLASS),
        Classification("10.86.00", "Produzione di preparati omogeneizzati e di alimenti dietetici", Category.SUBCLASS),
        Classification("10.89", "Produzione di altri prodotti alimentari n.c.a.", Category.CLASS),
        Classification("10.89.0", "Produzione di altri prodotti alimentari n.c.a.", Category.SUBCLASS),
        Classification("10.89.01", "Produzione di integratori alimentari", Category.SUBCLASS),
        Classification("10.89.09", "Produzione di altri prodotti alimentari vari n.c.a.", Category.SUBCLASS),
        Classification("10.9", "Produzione di prodotti per l'alimentazione degli animali", Category.GROUP),
        Classification(
            "10.91", "Produzione di mangimi per l'alimentazione degli animali da allevamento", Category.CLASS
        ),
        Classification(
            "10.91.0", "Produzione di mangimi per l'alimentazione degli animali da allevamento", Category.SUBCLASS
        ),
        Classification(
            "10.91.00", "Produzione di mangimi per l'alimentazione degli animali da allevamento", Category.SUBCLASS
        ),
        Classification(
            "10.92", "Produzione di prodotti per l'alimentazione degli animali da compagnia", Category.CLASS
        ),
        Classification(
            "10.92.0", "Produzione di prodotti per l'alimentazione degli animali da compagnia", Category.SUBCLASS
        ),
        Classification(
            "10.92.00", "Produzione di prodotti per l'alimentazione degli animali da compagnia", Category.SUBCLASS
        ),
        Classification("11", "Produzione di bevande", Category.DIVISION),
        Classification("11.0", "Produzione di bevande", Category.GROUP),
        Classification("11.01", "Distillazione, rettifica e miscelatura di alcolici", Category.CLASS),
        Classification("11.01.0", "Distillazione, rettifica e miscelatura di alcolici", Category.SUBCLASS),
        Classification("11.01.00", "Distillazione, rettifica e miscelatura di alcolici", Category.SUBCLASS),
        Classification("11.02", "Produzione di vini da uve", Category.CLASS),
        Classification("11.02.1", "Produzione di vini, esclusi vini spumanti e altri vini speciali", Category.SUBCLASS),
        Classification(
            "11.02.10", "Produzione di vini, esclusi vini spumanti e altri vini speciali", Category.SUBCLASS
        ),
        Classification("11.02.2", "Produzione di vini spumanti e altri vini speciali", Category.SUBCLASS),
        Classification("11.02.20", "Produzione di vini spumanti e altri vini speciali", Category.SUBCLASS),
        Classification("11.03", "Produzione di sidro e di altre bevande fermentate a base di frutta", Category.CLASS),
        Classification(
            "11.03.0", "Produzione di sidro e di altre bevande fermentate a base di frutta", Category.SUBCLASS
        ),
        Classification(
            "11.03.00", "Produzione di sidro e di altre bevande fermentate a base di frutta", Category.SUBCLASS
        ),
        Classification("11.04", "Produzione di altre bevande fermentate non distillate", Category.CLASS),
        Classification("11.04.0", "Produzione di altre bevande fermentate non distillate", Category.SUBCLASS),
        Classification("11.04.00", "Produzione di altre bevande fermentate non distillate", Category.SUBCLASS),
        Classification("11.05", "Produzione di birra", Category.CLASS),
        Classification("11.05.0", "Produzione di birra", Category.SUBCLASS),
        Classification("11.05.00", "Produzione di birra", Category.SUBCLASS),
        Classification("11.06", "Produzione di malto", Category.CLASS),
        Classification("11.06.0", "Produzione di malto", Category.SUBCLASS),
        Classification("11.06.00", "Produzione di malto", Category.SUBCLASS),
        Classification("11.07", "Produzione di bibite analcoliche e di acque in bottiglia", Category.CLASS),
        Classification("11.07.0", "Produzione di bibite analcoliche e di acque in bottiglia", Category.SUBCLASS),
        Classification("11.07.01", "Produzione di bibite analcoliche", Category.SUBCLASS),
        Classification("11.07.02", "Produzione di acque in bottiglia", Category.SUBCLASS),
        Classification("12", "Produzione di prodotti del tabacco", Category.DIVISION),
        Classification("12.0", "Produzione di prodotti del tabacco", Category.GROUP),
        Classification("12.00", "Produzione di prodotti del tabacco", Category.CLASS),
        Classification("12.00.0", "Produzione di prodotti del tabacco", Category.SUBCLASS),
        Classification("12.00.00", "Produzione di prodotti del tabacco", Category.SUBCLASS),
        Classification("13", "Fabbricazione di tessili", Category.DIVISION),
        Classification("13.1", "Preparazione e filatura di fibre tessili", Category.GROUP),
        Classification("13.10", "Preparazione e filatura di fibre tessili", Category.CLASS),
        Classification("13.10.0", "Preparazione e filatura di fibre tessili", Category.SUBCLASS),
        Classification("13.10.00", "Preparazione e filatura di fibre tessili", Category.SUBCLASS),
        Classification("13.2", "Tessitura", Category.GROUP),
        Classification("13.20", "Tessitura", Category.CLASS),
        Classification("13.20.0", "Tessitura", Category.SUBCLASS),
        Classification("13.20.00", "Tessitura", Category.SUBCLASS),
        Classification("13.3", "Finissaggio dei tessili", Category.GROUP),
        Classification("13.30", "Finissaggio dei tessili", Category.CLASS),
        Classification("13.30.0", "Finissaggio dei tessili", Category.SUBCLASS),
        Classification("13.30.00", "Finissaggio dei tessili", Category.SUBCLASS),
        Classification("13.9", "Altre fabbricazioni tessili", Category.GROUP),
        Classification("13.91", "Fabbricazione di tessuti a maglia e all'uncinetto", Category.CLASS),
        Classification("13.91.0", "Fabbricazione di tessuti a maglia e all'uncinetto", Category.SUBCLASS),
        Classification("13.91.00", "Fabbricazione di tessuti a maglia e all'uncinetto", Category.SUBCLASS),
        Classification("13.92", "Fabbricazione di tessili per la casa e l'arredo", Category.CLASS),
        Classification("13.92.1", "Fabbricazione di tessili per la casa", Category.SUBCLASS),
        Classification("13.92.10", "Fabbricazione di tessili per la casa", Category.SUBCLASS),
        Classification("13.92.2", "Fabbricazione di tessili per l'arredo", Category.SUBCLASS),
        Classification("13.92.20", "Fabbricazione di tessili per l'arredo", Category.SUBCLASS),
        Classification("13.93", "Fabbricazione di tappeti e moquette", Category.CLASS),
        Classification("13.93.0", "Fabbricazione di tappeti e moquette", Category.SUBCLASS),
        Classification("13.93.00", "Fabbricazione di tappeti e moquette", Category.SUBCLASS),
        Classification("13.94", "Fabbricazione di spago, corde, funi e reti", Category.CLASS),
        Classification("13.94.0", "Fabbricazione di spago, corde, funi e reti", Category.SUBCLASS),
        Classification("13.94.00", "Fabbricazione di spago, corde, funi e reti", Category.SUBCLASS),
        Classification(
            "13.95", "Fabbricazione di tessuti non-tessuti e di articoli in tessuto non-tessuto", Category.CLASS
        ),
        Classification(
            "13.95.0", "Fabbricazione di tessuti non-tessuti e di articoli in tessuto non-tessuto", Category.SUBCLASS
        ),
        Classification(
            "13.95.00", "Fabbricazione di tessuti non-tessuti e di articoli in tessuto non-tessuto", Category.SUBCLASS
        ),
        Classification("13.96", "Fabbricazione di altri tessuti per uso tecnico e industriale", Category.CLASS),
        Classification("13.96.0", "Fabbricazione di altri tessuti per uso tecnico e industriale", Category.SUBCLASS),
        Classification("13.96.00", "Fabbricazione di altri tessuti per uso tecnico e industriale", Category.SUBCLASS),
        Classification("13.99", "Fabbricazione di altri prodotti tessili n.c.a.", Category.CLASS),
        Classification("13.99.1", "Fabbricazione di ricami, tulle, pizzi e merletti", Category.SUBCLASS),
        Classification("13.99.10", "Fabbricazione di ricami, tulle, pizzi e merletti", Category.SUBCLASS),
        Classification("13.99.9", "Fabbricazione di feltro e altri prodotti tessili diversi n.c.a.", Category.SUBCLASS),
        Classification(
            "13.99.90", "Fabbricazione di feltro e altri prodotti tessili diversi n.c.a.", Category.SUBCLASS
        ),
        Classification("14", "Fabbricazione di articoli di abbigliamento", Category.DIVISION),
        Classification("14.1", "Fabbricazione di articoli a maglia e all'uncinetto", Category.GROUP),
        Classification("14.10", "Fabbricazione di articoli a maglia e all'uncinetto", Category.CLASS),
        Classification(
            "14.10.1", "Fabbricazione di articoli di calzetteria a maglia e all'uncinetto", Category.SUBCLASS
        ),
        Classification(
            "14.10.10", "Fabbricazione di articoli di calzetteria a maglia e all'uncinetto", Category.SUBCLASS
        ),
        Classification(
            "14.10.2", "Fabbricazione di maglioni e altri articoli a maglia e all'uncinetto", Category.SUBCLASS
        ),
        Classification(
            "14.10.20", "Fabbricazione di maglioni e altri articoli a maglia e all'uncinetto", Category.SUBCLASS
        ),
        Classification("14.2", "Fabbricazione di altri articoli di abbigliamento e accessori", Category.GROUP),
        Classification("14.21", "Fabbricazione di abbigliamento esterno", Category.CLASS),
        Classification("14.21.1", "Fabbricazione in serie di abbigliamento esterno", Category.SUBCLASS),
        Classification("14.21.10", "Fabbricazione in serie di abbigliamento esterno", Category.SUBCLASS),
        Classification("14.21.2", "Sartoria e confezione su misura di abbigliamento esterno", Category.SUBCLASS),
        Classification("14.21.20", "Sartoria e confezione su misura di abbigliamento esterno", Category.SUBCLASS),
        Classification("14.22", "Fabbricazione di biancheria intima", Category.CLASS),
        Classification("14.22.0", "Fabbricazione di biancheria intima", Category.SUBCLASS),
        Classification("14.22.00", "Fabbricazione di biancheria intima", Category.SUBCLASS),
        Classification("14.23", "Fabbricazione di indumenti da lavoro", Category.CLASS),
        Classification("14.23.0", "Fabbricazione di indumenti da lavoro", Category.SUBCLASS),
        Classification("14.23.00", "Fabbricazione di indumenti da lavoro", Category.SUBCLASS),
        Classification("14.24", "Fabbricazione di abbigliamento in pelle e in pelliccia", Category.CLASS),
        Classification("14.24.0", "Fabbricazione di abbigliamento in pelle e in pelliccia", Category.SUBCLASS),
        Classification("14.24.00", "Fabbricazione di abbigliamento in pelle e in pelliccia", Category.SUBCLASS),
        Classification("14.29", "Fabbricazione di altri articoli di abbigliamento e accessori n.c.a.", Category.CLASS),
        Classification(
            "14.29.0", "Fabbricazione di altri articoli di abbigliamento e accessori n.c.a.", Category.SUBCLASS
        ),
        Classification(
            "14.29.00", "Fabbricazione di altri articoli di abbigliamento e accessori n.c.a.", Category.SUBCLASS
        ),
        Classification(
            "15", "Fabbricazione di pelli e cuoi e articoli in pelle e simili di altri materiali", Category.DIVISION
        ),
        Classification(
            "15.1",
            "Concia, tintura e rifinizione di pelli, cuoi e pellicce; fabbricazione di articoli da viaggio, borse, pelletteria e selleria",
            Category.GROUP,
        ),
        Classification("15.11", "Concia, tintura e rifinizione di pelli, cuoi e pellicce", Category.CLASS),
        Classification("15.11.0", "Concia, tintura e rifinizione di pelli, cuoi e pellicce", Category.SUBCLASS),
        Classification("15.11.00", "Concia, tintura e rifinizione di pelli, cuoi e pellicce", Category.SUBCLASS),
        Classification(
            "15.12",
            "Fabbricazione di articoli da viaggio, borse, pelletteria e selleria di qualsiasi materiale",
            Category.CLASS,
        ),
        Classification(
            "15.12.0",
            "Fabbricazione di articoli da viaggio, borse, pelletteria e selleria di qualsiasi materiale",
            Category.SUBCLASS,
        ),
        Classification(
            "15.12.00",
            "Fabbricazione di articoli da viaggio, borse, pelletteria e selleria di qualsiasi materiale",
            Category.SUBCLASS,
        ),
        Classification("15.2", "Fabbricazione di calzature", Category.GROUP),
        Classification("15.20", "Fabbricazione di calzature", Category.CLASS),
        Classification(
            "15.20.1", "Fabbricazione di calzature, escluse parti in cuoio per calzature", Category.SUBCLASS
        ),
        Classification(
            "15.20.10", "Fabbricazione di calzature, escluse parti in cuoio per calzature", Category.SUBCLASS
        ),
        Classification("15.20.2", "Fabbricazione di parti in cuoio per calzature", Category.SUBCLASS),
        Classification("15.20.20", "Fabbricazione di parti in cuoio per calzature", Category.SUBCLASS),
        Classification(
            "16",
            "Produzione e lavorazione del legno e dei prodotti a base di legno e sughero, esclusi i mobili; fabbricazione di articoli in paglia e materiale da intreccio",
            Category.DIVISION,
        ),
        Classification("16.1", "Taglio e piallatura del legno; lavorazione e finitura del legno", Category.GROUP),
        Classification("16.11", "Taglio e piallatura del legno", Category.CLASS),
        Classification("16.11.0", "Taglio e piallatura del legno", Category.SUBCLASS),
        Classification("16.11.00", "Taglio e piallatura del legno", Category.SUBCLASS),
        Classification("16.12", "Lavorazione e finitura del legno", Category.CLASS),
        Classification("16.12.0", "Lavorazione e finitura del legno", Category.SUBCLASS),
        Classification("16.12.00", "Lavorazione e finitura del legno", Category.SUBCLASS),
        Classification(
            "16.2", "Fabbricazione di prodotti in legno, sughero, paglia e materiali da intreccio", Category.GROUP
        ),
        Classification(
            "16.21", "Fabbricazione di fogli da impiallacciatura e di pannelli a base di legno", Category.CLASS
        ),
        Classification(
            "16.21.0", "Fabbricazione di fogli da impiallacciatura e di pannelli a base di legno", Category.SUBCLASS
        ),
        Classification(
            "16.21.00", "Fabbricazione di fogli da impiallacciatura e di pannelli a base di legno", Category.SUBCLASS
        ),
        Classification("16.22", "Fabbricazione di pavimenti di legno con elementi pre-assemblati", Category.CLASS),
        Classification("16.22.0", "Fabbricazione di pavimenti di legno con elementi pre-assemblati", Category.SUBCLASS),
        Classification(
            "16.22.00", "Fabbricazione di pavimenti di legno con elementi pre-assemblati", Category.SUBCLASS
        ),
        Classification(
            "16.23",
            "Fabbricazione di altri prodotti di carpenteria in legno e falegnameria per l'edilizia",
            Category.CLASS,
        ),
        Classification(
            "16.23.0",
            "Fabbricazione di altri prodotti di carpenteria in legno e falegnameria per l'edilizia",
            Category.SUBCLASS,
        ),
        Classification(
            "16.23.01", "Fabbricazione di stand e strutture simili in legno per convegni e fiere", Category.SUBCLASS
        ),
        Classification(
            "16.23.09",
            "Fabbricazione di altri prodotti di carpenteria in legno e falegnameria per l'edilizia n.c.a.",
            Category.SUBCLASS,
        ),
        Classification("16.24", "Fabbricazione di imballaggi in legno", Category.CLASS),
        Classification("16.24.0", "Fabbricazione di imballaggi in legno", Category.SUBCLASS),
        Classification("16.24.00", "Fabbricazione di imballaggi in legno", Category.SUBCLASS),
        Classification("16.25", "Fabbricazione di porte e finestre in legno", Category.CLASS),
        Classification("16.25.0", "Fabbricazione di porte e finestre in legno", Category.SUBCLASS),
        Classification("16.25.00", "Fabbricazione di porte e finestre in legno", Category.SUBCLASS),
        Classification("16.26", "Produzione di combustibili solidi da biomassa vegetale", Category.CLASS),
        Classification("16.26.0", "Produzione di combustibili solidi da biomassa vegetale", Category.SUBCLASS),
        Classification("16.26.00", "Produzione di combustibili solidi da biomassa vegetale", Category.SUBCLASS),
        Classification("16.27", "Finitura di prodotti in legno", Category.CLASS),
        Classification("16.27.0", "Finitura di prodotti in legno", Category.SUBCLASS),
        Classification("16.27.00", "Finitura di prodotti in legno", Category.SUBCLASS),
        Classification(
            "16.28",
            "Fabbricazione di altri prodotti in legno e articoli in sughero, paglia e materiali da intreccio",
            Category.CLASS,
        ),
        Classification("16.28.1", "Fabbricazione di altri prodotti in legno", Category.SUBCLASS),
        Classification("16.28.11", "Fabbricazione di cornici", Category.SUBCLASS),
        Classification("16.28.19", "Fabbricazione di altri prodotti in legno n.c.a.", Category.SUBCLASS),
        Classification("16.28.2", "Fabbricazione di articoli in sughero", Category.SUBCLASS),
        Classification("16.28.20", "Fabbricazione di articoli in sughero", Category.SUBCLASS),
        Classification("16.28.3", "Fabbricazione di articoli in paglia e materiali da intreccio", Category.SUBCLASS),
        Classification("16.28.30", "Fabbricazione di articoli in paglia e materiali da intreccio", Category.SUBCLASS),
        Classification("17", "Fabbricazione di carta e di prodotti di carta", Category.DIVISION),
        Classification("17.1", "Fabbricazione di pasta-carta, carta e cartone", Category.GROUP),
        Classification("17.11", "Fabbricazione di pasta-carta", Category.CLASS),
        Classification("17.11.0", "Fabbricazione di pasta-carta", Category.SUBCLASS),
        Classification("17.11.00", "Fabbricazione di pasta-carta", Category.SUBCLASS),
        Classification("17.12", "Fabbricazione di carta e cartone", Category.CLASS),
        Classification("17.12.0", "Fabbricazione di carta e cartone", Category.SUBCLASS),
        Classification("17.12.00", "Fabbricazione di carta e cartone", Category.SUBCLASS),
        Classification("17.2", "Fabbricazione di articoli di carta e cartone", Category.GROUP),
        Classification(
            "17.21", "Fabbricazione di carta, cartone ondulato e di imballaggi di carta e cartone", Category.CLASS
        ),
        Classification(
            "17.21.0", "Fabbricazione di carta, cartone ondulato e di imballaggi di carta e cartone", Category.SUBCLASS
        ),
        Classification(
            "17.21.00", "Fabbricazione di carta, cartone ondulato e di imballaggi di carta e cartone", Category.SUBCLASS
        ),
        Classification(
            "17.22",
            "Fabbricazione di prodotti igienico-sanitari e per uso domestico in carta e ovatta di cellulosa",
            Category.CLASS,
        ),
        Classification(
            "17.22.0",
            "Fabbricazione di prodotti igienico-sanitari e per uso domestico in carta e ovatta di cellulosa",
            Category.SUBCLASS,
        ),
        Classification(
            "17.22.00",
            "Fabbricazione di prodotti igienico-sanitari e per uso domestico in carta e ovatta di cellulosa",
            Category.SUBCLASS,
        ),
        Classification("17.23", "Fabbricazione di prodotti cartotecnici", Category.CLASS),
        Classification("17.23.0", "Fabbricazione di prodotti cartotecnici", Category.SUBCLASS),
        Classification(
            "17.23.01", "Fabbricazione di prodotti cartotecnici scolastici e commerciali", Category.SUBCLASS
        ),
        Classification("17.23.09", "Fabbricazione di altri prodotti cartotecnici", Category.SUBCLASS),
        Classification("17.24", "Fabbricazione di carta da parati", Category.CLASS),
        Classification("17.24.0", "Fabbricazione di carta da parati", Category.SUBCLASS),
        Classification("17.24.00", "Fabbricazione di carta da parati", Category.SUBCLASS),
        Classification("17.25", "Fabbricazione di altri articoli di carta e cartone", Category.CLASS),
        Classification("17.25.0", "Fabbricazione di altri articoli di carta e cartone", Category.SUBCLASS),
        Classification("17.25.00", "Fabbricazione di altri articoli di carta e cartone", Category.SUBCLASS),
        Classification("18", "Stampa e riproduzione di supporti registrati", Category.DIVISION),
        Classification("18.1", "Stampa e servizi connessi alla stampa", Category.GROUP),
        Classification("18.11", "Stampa di giornali", Category.CLASS),
        Classification("18.11.0", "Stampa di giornali", Category.SUBCLASS),
        Classification("18.11.00", "Stampa di giornali", Category.SUBCLASS),
        Classification("18.12", "Altra stampa", Category.CLASS),
        Classification("18.12.0", "Altra stampa", Category.SUBCLASS),
        Classification("18.12.00", "Altra stampa", Category.SUBCLASS),
        Classification("18.13", "Lavorazioni preliminari alla stampa e ai media", Category.CLASS),
        Classification("18.13.0", "Lavorazioni preliminari alla stampa e ai media", Category.SUBCLASS),
        Classification("18.13.00", "Lavorazioni preliminari alla stampa e ai media", Category.SUBCLASS),
        Classification("18.14", "Legatoria e servizi connessi", Category.CLASS),
        Classification("18.14.0", "Legatoria e servizi connessi", Category.SUBCLASS),
        Classification("18.14.00", "Legatoria e servizi connessi", Category.SUBCLASS),
        Classification("18.2", "Riproduzione di supporti registrati", Category.GROUP),
        Classification("18.20", "Riproduzione di supporti registrati", Category.CLASS),
        Classification("18.20.0", "Riproduzione di supporti registrati", Category.SUBCLASS),
        Classification("18.20.00", "Riproduzione di supporti registrati", Category.SUBCLASS),
        Classification(
            "19", "Fabbricazione di coke e prodotti derivanti dalla raffinazione del petrolio", Category.DIVISION
        ),
        Classification("19.1", "Fabbricazione di prodotti di cokeria", Category.GROUP),
        Classification("19.10", "Fabbricazione di prodotti di cokeria", Category.CLASS),
        Classification("19.10.0", "Fabbricazione di prodotti di cokeria", Category.SUBCLASS),
        Classification("19.10.00", "Fabbricazione di prodotti di cokeria", Category.SUBCLASS),
        Classification(
            "19.2",
            "Fabbricazione di prodotti derivanti dalla raffinazione del petrolio e prodotti da combustibili fossili",
            Category.GROUP,
        ),
        Classification(
            "19.20",
            "Fabbricazione di prodotti derivanti dalla raffinazione del petrolio e prodotti da combustibili fossili",
            Category.CLASS,
        ),
        Classification("19.20.1", "Raffinazione di petrolio", Category.SUBCLASS),
        Classification("19.20.10", "Raffinazione di petrolio", Category.SUBCLASS),
        Classification("19.20.2", "Fabbricazione di derivati del petrolio", Category.SUBCLASS),
        Classification("19.20.20", "Fabbricazione di derivati del petrolio", Category.SUBCLASS),
        Classification(
            "19.20.3", "Miscelazione di gas petroliferi liquefatti (GPL) e loro imbottigliamento", Category.SUBCLASS
        ),
        Classification(
            "19.20.30", "Miscelazione di gas petroliferi liquefatti (GPL) e loro imbottigliamento", Category.SUBCLASS
        ),
        Classification("19.20.4", "Fabbricazione di prodotti di base per la copertura stradale", Category.SUBCLASS),
        Classification("19.20.40", "Fabbricazione di prodotti di base per la copertura stradale", Category.SUBCLASS),
        Classification(
            "19.20.9",
            "Fabbricazione di altri prodotti derivanti dalla raffinazione del petrolio e prodotti da combustibili fossili",
            Category.SUBCLASS,
        ),
        Classification(
            "19.20.90",
            "Fabbricazione di altri prodotti derivanti dalla raffinazione del petrolio e prodotti da combustibili fossili",
            Category.SUBCLASS,
        ),
        Classification("20", "Fabbricazione di prodotti chimici", Category.DIVISION),
        Classification(
            "20.1",
            "Fabbricazione di prodotti chimici di base, di fertilizzanti e composti azotati, di materie plastiche e gomma sintetica in forme primarie",
            Category.GROUP,
        ),
        Classification("20.11", "Fabbricazione di gas industriali", Category.CLASS),
        Classification("20.11.0", "Fabbricazione di gas industriali", Category.SUBCLASS),
        Classification("20.11.00", "Fabbricazione di gas industriali", Category.SUBCLASS),
        Classification("20.12", "Fabbricazione di coloranti e pigmenti", Category.CLASS),
        Classification("20.12.0", "Fabbricazione di coloranti e pigmenti", Category.SUBCLASS),
        Classification("20.12.00", "Fabbricazione di coloranti e pigmenti", Category.SUBCLASS),
        Classification("20.13", "Fabbricazione di altri prodotti chimici di base inorganici", Category.CLASS),
        Classification("20.13.0", "Fabbricazione di altri prodotti chimici di base inorganici", Category.SUBCLASS),
        Classification("20.13.00", "Fabbricazione di altri prodotti chimici di base inorganici", Category.SUBCLASS),
        Classification("20.14", "Fabbricazione di altri prodotti chimici di base organici", Category.CLASS),
        Classification("20.14.0", "Fabbricazione di altri prodotti chimici di base organici", Category.SUBCLASS),
        Classification("20.14.00", "Fabbricazione di altri prodotti chimici di base organici", Category.SUBCLASS),
        Classification("20.15", "Fabbricazione di fertilizzanti e composti azotati", Category.CLASS),
        Classification("20.15.0", "Fabbricazione di fertilizzanti e composti azotati", Category.SUBCLASS),
        Classification("20.15.00", "Fabbricazione di fertilizzanti e composti azotati", Category.SUBCLASS),
        Classification("20.16", "Fabbricazione di materie plastiche in forme primarie", Category.CLASS),
        Classification("20.16.0", "Fabbricazione di materie plastiche in forme primarie", Category.SUBCLASS),
        Classification("20.16.00", "Fabbricazione di materie plastiche in forme primarie", Category.SUBCLASS),
        Classification("20.17", "Fabbricazione di gomma sintetica in forme primarie", Category.CLASS),
        Classification("20.17.0", "Fabbricazione di gomma sintetica in forme primarie", Category.SUBCLASS),
        Classification("20.17.00", "Fabbricazione di gomma sintetica in forme primarie", Category.SUBCLASS),
        Classification(
            "20.2",
            "Fabbricazione di fitofarmaci, disinfettanti e altri prodotti chimici per l'agricoltura",
            Category.GROUP,
        ),
        Classification(
            "20.20",
            "Fabbricazione di fitofarmaci, disinfettanti e altri prodotti chimici per l'agricoltura",
            Category.CLASS,
        ),
        Classification(
            "20.20.0",
            "Fabbricazione di fitofarmaci, disinfettanti e altri prodotti chimici per l'agricoltura",
            Category.SUBCLASS,
        ),
        Classification(
            "20.20.00",
            "Fabbricazione di fitofarmaci, disinfettanti e altri prodotti chimici per l'agricoltura",
            Category.SUBCLASS,
        ),
        Classification(
            "20.3",
            "Fabbricazione di pitture, vernici e smalti, inchiostri da stampa e adesivi sintetici",
            Category.GROUP,
        ),
        Classification(
            "20.30",
            "Fabbricazione di pitture, vernici e smalti, inchiostri da stampa e adesivi sintetici",
            Category.CLASS,
        ),
        Classification(
            "20.30.0",
            "Fabbricazione di pitture, vernici e smalti, inchiostri da stampa e adesivi sintetici",
            Category.SUBCLASS,
        ),
        Classification(
            "20.30.00",
            "Fabbricazione di pitture, vernici e smalti, inchiostri da stampa e adesivi sintetici",
            Category.SUBCLASS,
        ),
        Classification("20.4", "Fabbricazione di prodotti per il lavaggio, la pulizia e la lucidatura", Category.GROUP),
        Classification(
            "20.41", "Fabbricazione di saponi e detergenti, di prodotti per la pulizia e la lucidatura", Category.CLASS
        ),
        Classification("20.41.1", "Fabbricazione di saponi, detergenti e preparazioni tensioattive", Category.SUBCLASS),
        Classification(
            "20.41.10", "Fabbricazione di saponi, detergenti e preparazioni tensioattive", Category.SUBCLASS
        ),
        Classification(
            "20.41.2", "Fabbricazione di glicerina e altri prodotti per la pulizia e la lucidatura", Category.SUBCLASS
        ),
        Classification(
            "20.41.20", "Fabbricazione di glicerina e altri prodotti per la pulizia e la lucidatura", Category.SUBCLASS
        ),
        Classification("20.42", "Fabbricazione di profumi e cosmetici", Category.CLASS),
        Classification("20.42.0", "Fabbricazione di profumi e cosmetici", Category.SUBCLASS),
        Classification("20.42.00", "Fabbricazione di profumi e cosmetici", Category.SUBCLASS),
        Classification("20.5", "Fabbricazione di altri prodotti chimici", Category.GROUP),
        Classification("20.51", "Produzione di biocarburanti liquidi", Category.CLASS),
        Classification("20.51.0", "Produzione di biocarburanti liquidi", Category.SUBCLASS),
        Classification("20.51.00", "Produzione di biocarburanti liquidi", Category.SUBCLASS),
        Classification("20.59", "Fabbricazione di altri prodotti chimici n.c.a.", Category.CLASS),
        Classification("20.59.1", "Fabbricazione di fiammiferi e articoli esplosivi", Category.SUBCLASS),
        Classification("20.59.11", "Fabbricazione di fiammiferi", Category.SUBCLASS),
        Classification("20.59.12", "Fabbricazione di articoli esplosivi", Category.SUBCLASS),
        Classification("20.59.2", "Fabbricazione di colle", Category.SUBCLASS),
        Classification("20.59.20", "Fabbricazione di colle", Category.SUBCLASS),
        Classification("20.59.3", "Fabbricazione di oli essenziali", Category.SUBCLASS),
        Classification("20.59.30", "Fabbricazione di oli essenziali", Category.SUBCLASS),
        Classification("20.59.9", "Fabbricazione di altri prodotti chimici vari n.c.a.", Category.SUBCLASS),
        Classification(
            "20.59.91", "Fabbricazione di liquidi per inalazione per sigarette elettroniche", Category.SUBCLASS
        ),
        Classification("20.59.99", "Fabbricazione di tutti gli altri prodotti chimici vari n.c.a.", Category.SUBCLASS),
        Classification("20.6", "Fabbricazione di fibre sintetiche e artificiali", Category.GROUP),
        Classification("20.60", "Fabbricazione di fibre sintetiche e artificiali", Category.CLASS),
        Classification("20.60.0", "Fabbricazione di fibre sintetiche e artificiali", Category.SUBCLASS),
        Classification("20.60.00", "Fabbricazione di fibre sintetiche e artificiali", Category.SUBCLASS),
        Classification(
            "21", "Fabbricazione di prodotti farmaceutici di base e di preparati farmaceutici", Category.DIVISION
        ),
        Classification("21.1", "Fabbricazione di prodotti farmaceutici di base", Category.GROUP),
        Classification("21.10", "Fabbricazione di prodotti farmaceutici di base", Category.CLASS),
        Classification("21.10.0", "Fabbricazione di prodotti farmaceutici di base", Category.SUBCLASS),
        Classification("21.10.00", "Fabbricazione di prodotti farmaceutici di base", Category.SUBCLASS),
        Classification("21.2", "Fabbricazione di medicinali e preparati farmaceutici", Category.GROUP),
        Classification("21.20", "Fabbricazione di medicinali e preparati farmaceutici", Category.CLASS),
        Classification("21.20.0", "Fabbricazione di medicinali e preparati farmaceutici", Category.SUBCLASS),
        Classification("21.20.01", "Fabbricazione di sostanze diagnostiche radioattive in vivo", Category.SUBCLASS),
        Classification("21.20.09", "Fabbricazione di medicinali e altri preparati farmaceutici", Category.SUBCLASS),
        Classification("22", "Fabbricazione di prodotti in gomma e in materie plastiche", Category.DIVISION),
        Classification("22.1", "Fabbricazione di prodotti in gomma", Category.GROUP),
        Classification(
            "22.11",
            "Fabbricazione, rigenerazione e ricostruzione di pneumatici e fabbricazione di camere d'aria",
            Category.CLASS,
        ),
        Classification("22.11.1", "Fabbricazione di pneumatici e camere d'aria", Category.SUBCLASS),
        Classification("22.11.10", "Fabbricazione di pneumatici e camere d'aria", Category.SUBCLASS),
        Classification("22.11.2", "Rigenerazione e ricostruzione di pneumatici", Category.SUBCLASS),
        Classification("22.11.20", "Rigenerazione e ricostruzione di pneumatici", Category.SUBCLASS),
        Classification("22.12", "Fabbricazione di altri prodotti in gomma", Category.CLASS),
        Classification("22.12.0", "Fabbricazione di altri prodotti in gomma", Category.SUBCLASS),
        Classification("22.12.00", "Fabbricazione di altri prodotti in gomma", Category.SUBCLASS),
        Classification("22.2", "Fabbricazione di prodotti in materie plastiche", Category.GROUP),
        Classification(
            "22.21", "Fabbricazione di lastre, fogli, tubi e profilati in materie plastiche", Category.CLASS
        ),
        Classification(
            "22.21.0", "Fabbricazione di lastre, fogli, tubi e profilati in materie plastiche", Category.SUBCLASS
        ),
        Classification(
            "22.21.00", "Fabbricazione di lastre, fogli, tubi e profilati in materie plastiche", Category.SUBCLASS
        ),
        Classification("22.22", "Fabbricazione di imballaggi in materie plastiche", Category.CLASS),
        Classification("22.22.0", "Fabbricazione di imballaggi in materie plastiche", Category.SUBCLASS),
        Classification("22.22.00", "Fabbricazione di imballaggi in materie plastiche", Category.SUBCLASS),
        Classification("22.23", "Fabbricazione di porte e finestre in materie plastiche", Category.CLASS),
        Classification("22.23.0", "Fabbricazione di porte e finestre in materie plastiche", Category.SUBCLASS),
        Classification("22.23.00", "Fabbricazione di porte e finestre in materie plastiche", Category.SUBCLASS),
        Classification("22.24", "Fabbricazione di articoli in materie plastiche per l'edilizia", Category.CLASS),
        Classification("22.24.0", "Fabbricazione di articoli in materie plastiche per l'edilizia", Category.SUBCLASS),
        Classification(
            "22.24.01", "Fabbricazione di rivestimenti per pareti e pavimenti in materie plastiche", Category.SUBCLASS
        ),
        Classification(
            "22.24.09", "Fabbricazione di altri articoli in materie plastiche per l'edilizia", Category.SUBCLASS
        ),
        Classification("22.25", "Lavorazione e finitura di prodotti in materie plastiche", Category.CLASS),
        Classification("22.25.0", "Lavorazione e finitura di prodotti in materie plastiche", Category.SUBCLASS),
        Classification("22.25.00", "Lavorazione e finitura di prodotti in materie plastiche", Category.SUBCLASS),
        Classification("22.26", "Fabbricazione di altri prodotti in materie plastiche", Category.CLASS),
        Classification(
            "22.26.1", "Fabbricazione di articoli e attrezzature per la pulizia in materie plastiche", Category.SUBCLASS
        ),
        Classification(
            "22.26.11",
            "Fabbricazione di articoli e attrezzature per la pulizia per uso domestico in materie plastiche",
            Category.SUBCLASS,
        ),
        Classification(
            "22.26.12",
            "Fabbricazione di articoli e attrezzature per la pulizia per uso non domestico in materie plastiche",
            Category.SUBCLASS,
        ),
        Classification("22.26.9", "Fabbricazione di altri prodotti in materie plastiche n.c.a.", Category.SUBCLASS),
        Classification(
            "22.26.91", "Fabbricazione di articoli per l'ufficio e la scuola in materie plastiche", Category.SUBCLASS
        ),
        Classification(
            "22.26.99", "Fabbricazione di altri prodotti vari in materie plastiche n.c.a.", Category.SUBCLASS
        ),
        Classification(
            "23", "Fabbricazione di altri prodotti della lavorazione di minerali non metalliferi", Category.DIVISION
        ),
        Classification("23.1", "Fabbricazione di vetro e di prodotti in vetro", Category.GROUP),
        Classification("23.11", "Fabbricazione di vetro piano", Category.CLASS),
        Classification("23.11.0", "Fabbricazione di vetro piano", Category.SUBCLASS),
        Classification("23.11.00", "Fabbricazione di vetro piano", Category.SUBCLASS),
        Classification("23.12", "Lavorazione e trasformazione del vetro piano", Category.CLASS),
        Classification("23.12.0", "Lavorazione e trasformazione del vetro piano", Category.SUBCLASS),
        Classification("23.12.00", "Lavorazione e trasformazione del vetro piano", Category.SUBCLASS),
        Classification("23.13", "Fabbricazione di vetro cavo", Category.CLASS),
        Classification("23.13.0", "Fabbricazione di vetro cavo", Category.SUBCLASS),
        Classification("23.13.00", "Fabbricazione di vetro cavo", Category.SUBCLASS),
        Classification("23.14", "Fabbricazione di fibre di vetro", Category.CLASS),
        Classification("23.14.0", "Fabbricazione di fibre di vetro", Category.SUBCLASS),
        Classification("23.14.00", "Fabbricazione di fibre di vetro", Category.SUBCLASS),
        Classification(
            "23.15", "Fabbricazione e lavorazione di altro vetro incluso il vetro per usi tecnici", Category.CLASS
        ),
        Classification("23.15.1", "Lavorazione di vetro a mano e a soffio artistico", Category.SUBCLASS),
        Classification("23.15.10", "Lavorazione di vetro a mano e a soffio artistico", Category.SUBCLASS),
        Classification(
            "23.15.9",
            "Altre attività di fabbricazione e lavorazione di altro vetro incluso il vetro per usi tecnici",
            Category.SUBCLASS,
        ),
        Classification(
            "23.15.90",
            "Altre attività di fabbricazione e lavorazione di altro vetro incluso il vetro per usi tecnici",
            Category.SUBCLASS,
        ),
        Classification("23.2", "Fabbricazione di prodotti refrattari", Category.GROUP),
        Classification("23.20", "Fabbricazione di prodotti refrattari", Category.CLASS),
        Classification("23.20.0", "Fabbricazione di prodotti refrattari", Category.SUBCLASS),
        Classification("23.20.00", "Fabbricazione di prodotti refrattari", Category.SUBCLASS),
        Classification("23.3", "Fabbricazione di materiali da costruzione in terracotta", Category.GROUP),
        Classification("23.31", "Fabbricazione di piastrelle in ceramica per pavimenti e rivestimenti", Category.CLASS),
        Classification(
            "23.31.0", "Fabbricazione di piastrelle in ceramica per pavimenti e rivestimenti", Category.SUBCLASS
        ),
        Classification(
            "23.31.00", "Fabbricazione di piastrelle in ceramica per pavimenti e rivestimenti", Category.SUBCLASS
        ),
        Classification(
            "23.32", "Fabbricazione di mattoni, tegole e altri prodotti per l'edilizia in terracotta", Category.CLASS
        ),
        Classification(
            "23.32.0",
            "Fabbricazione di mattoni, tegole e altri prodotti per l'edilizia in terracotta",
            Category.SUBCLASS,
        ),
        Classification(
            "23.32.00",
            "Fabbricazione di mattoni, tegole e altri prodotti per l'edilizia in terracotta",
            Category.SUBCLASS,
        ),
        Classification("23.4", "Fabbricazione di altri prodotti in porcellana e in ceramica", Category.GROUP),
        Classification(
            "23.41", "Fabbricazione di prodotti in ceramica per usi domestici e ornamentali", Category.CLASS
        ),
        Classification(
            "23.41.0", "Fabbricazione di prodotti in ceramica per usi domestici e ornamentali", Category.SUBCLASS
        ),
        Classification(
            "23.41.00", "Fabbricazione di prodotti in ceramica per usi domestici e ornamentali", Category.SUBCLASS
        ),
        Classification("23.42", "Fabbricazione di articoli sanitari in ceramica", Category.CLASS),
        Classification("23.42.0", "Fabbricazione di articoli sanitari in ceramica", Category.SUBCLASS),
        Classification("23.42.00", "Fabbricazione di articoli sanitari in ceramica", Category.SUBCLASS),
        Classification("23.43", "Fabbricazione di isolatori e di pezzi isolanti in ceramica", Category.CLASS),
        Classification("23.43.0", "Fabbricazione di isolatori e di pezzi isolanti in ceramica", Category.SUBCLASS),
        Classification("23.43.00", "Fabbricazione di isolatori e di pezzi isolanti in ceramica", Category.SUBCLASS),
        Classification(
            "23.44", "Fabbricazione di altri prodotti in ceramica per uso tecnico e industriale", Category.CLASS
        ),
        Classification(
            "23.44.0", "Fabbricazione di altri prodotti in ceramica per uso tecnico e industriale", Category.SUBCLASS
        ),
        Classification(
            "23.44.00", "Fabbricazione di altri prodotti in ceramica per uso tecnico e industriale", Category.SUBCLASS
        ),
        Classification("23.45", "Fabbricazione di altri prodotti in ceramica", Category.CLASS),
        Classification("23.45.0", "Fabbricazione di altri prodotti in ceramica", Category.SUBCLASS),
        Classification("23.45.00", "Fabbricazione di altri prodotti in ceramica", Category.SUBCLASS),
        Classification("23.5", "Produzione di cemento, calce e gesso", Category.GROUP),
        Classification("23.51", "Produzione di cemento", Category.CLASS),
        Classification("23.51.0", "Produzione di cemento", Category.SUBCLASS),
        Classification("23.51.00", "Produzione di cemento", Category.SUBCLASS),
        Classification("23.52", "Produzione di calce e gesso", Category.CLASS),
        Classification("23.52.1", "Produzione di calce", Category.SUBCLASS),
        Classification("23.52.10", "Produzione di calce", Category.SUBCLASS),
        Classification("23.52.2", "Produzione di gesso", Category.SUBCLASS),
        Classification("23.52.20", "Produzione di gesso", Category.SUBCLASS),
        Classification("23.6", "Fabbricazione di prodotti in calcestruzzo, cemento e gesso", Category.GROUP),
        Classification("23.61", "Fabbricazione di prodotti in calcestruzzo per l'edilizia", Category.CLASS),
        Classification("23.61.0", "Fabbricazione di prodotti in calcestruzzo per l'edilizia", Category.SUBCLASS),
        Classification(
            "23.61.01", "Fabbricazione di tubi prefabbricati in calcestruzzo per acqua potabile", Category.SUBCLASS
        ),
        Classification("23.61.02", "Fabbricazione di caminetti prefabbricati in calcestruzzo", Category.SUBCLASS),
        Classification(
            "23.61.03", "Fabbricazione di elementi prefabbricati in calcestruzzo per l'edilizia", Category.SUBCLASS
        ),
        Classification(
            "23.61.04", "Fabbricazione di strutture prefabbricate in calcestruzzo per l'edilizia", Category.SUBCLASS
        ),
        Classification(
            "23.61.09", "Fabbricazione di prodotti in calcestruzzo per l'edilizia n.c.a.", Category.SUBCLASS
        ),
        Classification("23.62", "Fabbricazione di prodotti in gesso per l'edilizia", Category.CLASS),
        Classification("23.62.0", "Fabbricazione di prodotti in gesso per l'edilizia", Category.SUBCLASS),
        Classification("23.62.00", "Fabbricazione di prodotti in gesso per l'edilizia", Category.SUBCLASS),
        Classification("23.63", "Produzione di calcestruzzo pronto per l'uso", Category.CLASS),
        Classification("23.63.0", "Produzione di calcestruzzo pronto per l'uso", Category.SUBCLASS),
        Classification("23.63.00", "Produzione di calcestruzzo pronto per l'uso", Category.SUBCLASS),
        Classification("23.64", "Produzione di malta", Category.CLASS),
        Classification("23.64.0", "Produzione di malta", Category.SUBCLASS),
        Classification("23.64.00", "Produzione di malta", Category.SUBCLASS),
        Classification("23.65", "Fabbricazione di prodotti in fibrocemento", Category.CLASS),
        Classification("23.65.0", "Fabbricazione di prodotti in fibrocemento", Category.SUBCLASS),
        Classification(
            "23.65.01",
            "Fabbricazione di prodotti in sostanze vegetali agglomerate con cemento, gesso o altri leganti minerali",
            Category.SUBCLASS,
        ),
        Classification(
            "23.65.02", "Fabbricazione di prodotti in asbesto-cemento o cellulosa fibrocemento", Category.SUBCLASS
        ),
        Classification("23.66", "Fabbricazione di altri prodotti in calcestruzzo, cemento e gesso", Category.CLASS),
        Classification(
            "23.66.0", "Fabbricazione di altri prodotti in calcestruzzo, cemento e gesso", Category.SUBCLASS
        ),
        Classification(
            "23.66.01", "Fabbricazione di statue, bassorilievi e altorilievi, vasi e fioriere", Category.SUBCLASS
        ),
        Classification(
            "23.66.09", "Fabbricazione di altri prodotti in calcestruzzo, cemento e gesso n.c.a.", Category.SUBCLASS
        ),
        Classification("23.7", "Taglio, modellatura e finitura di pietre", Category.GROUP),
        Classification("23.70", "Taglio, modellatura e finitura di pietre", Category.CLASS),
        Classification("23.70.1", "Taglio e lavorazione di pietre e di marmo", Category.SUBCLASS),
        Classification("23.70.10", "Taglio e lavorazione di pietre e di marmo", Category.SUBCLASS),
        Classification("23.70.2", "Lavorazione artistica di marmo e di altre pietre affini", Category.SUBCLASS),
        Classification("23.70.20", "Lavorazione artistica di marmo e di altre pietre affini", Category.SUBCLASS),
        Classification("23.70.3", "Frantumazione di pietre", Category.SUBCLASS),
        Classification("23.70.30", "Frantumazione di pietre", Category.SUBCLASS),
        Classification(
            "23.9", "Fabbricazione di prodotti abrasivi e in minerali non metalliferi n.c.a.", Category.GROUP
        ),
        Classification("23.91", "Fabbricazione di prodotti abrasivi", Category.CLASS),
        Classification("23.91.0", "Fabbricazione di prodotti abrasivi", Category.SUBCLASS),
        Classification("23.91.00", "Fabbricazione di prodotti abrasivi", Category.SUBCLASS),
        Classification("23.99", "Fabbricazione di altri prodotti in minerali non metalliferi n.c.a.", Category.CLASS),
        Classification(
            "23.99.0", "Fabbricazione di altri prodotti in minerali non metalliferi n.c.a.", Category.SUBCLASS
        ),
        Classification(
            "23.99.00", "Fabbricazione di altri prodotti in minerali non metalliferi n.c.a.", Category.SUBCLASS
        ),
        Classification("24", "Fabbricazione di metalli di base", Category.DIVISION),
        Classification("24.1", "Fabbricazione di ferro, acciaio e ferroleghe", Category.GROUP),
        Classification("24.10", "Fabbricazione di ferro, acciaio e ferroleghe", Category.CLASS),
        Classification("24.10.0", "Fabbricazione di ferro, acciaio e ferroleghe", Category.SUBCLASS),
        Classification("24.10.00", "Fabbricazione di ferro, acciaio e ferroleghe", Category.SUBCLASS),
        Classification(
            "24.2", "Fabbricazione di tubi, condotti, profilati cavi e relativi raccordi in acciaio", Category.GROUP
        ),
        Classification(
            "24.20", "Fabbricazione di tubi, condotti, profilati cavi e relativi raccordi in acciaio", Category.CLASS
        ),
        Classification(
            "24.20.1",
            "Fabbricazione di tubi, condotti, profilati cavi non saldati e relativi raccordi in acciaio",
            Category.SUBCLASS,
        ),
        Classification(
            "24.20.10",
            "Fabbricazione di tubi, condotti, profilati cavi non saldati e relativi raccordi in acciaio",
            Category.SUBCLASS,
        ),
        Classification(
            "24.20.2",
            "Fabbricazione di tubi, condotti, profilati cavi saldati e relativi raccordi in acciaio",
            Category.SUBCLASS,
        ),
        Classification(
            "24.20.20",
            "Fabbricazione di tubi, condotti, profilati cavi saldati e relativi raccordi in acciaio",
            Category.SUBCLASS,
        ),
        Classification(
            "24.3", "Fabbricazione di altri prodotti della prima trasformazione dell'acciaio", Category.GROUP
        ),
        Classification("24.31", "Trafilatura a freddo di barre", Category.CLASS),
        Classification("24.31.0", "Trafilatura a freddo di barre", Category.SUBCLASS),
        Classification("24.31.00", "Trafilatura a freddo di barre", Category.SUBCLASS),
        Classification("24.32", "Laminazione a freddo di nastri", Category.CLASS),
        Classification("24.32.0", "Laminazione a freddo di nastri", Category.SUBCLASS),
        Classification("24.32.00", "Laminazione a freddo di nastri", Category.SUBCLASS),
        Classification("24.33", "Profilatura mediante formatura o piegatura a freddo", Category.CLASS),
        Classification("24.33.0", "Profilatura mediante formatura o piegatura a freddo", Category.SUBCLASS),
        Classification(
            "24.33.01",
            "Profilatura mediante formatura o piegatura a freddo di profilati aperti e lamiere grecate",
            Category.SUBCLASS,
        ),
        Classification(
            "24.33.02",
            "Profilatura mediante formatura o piegatura a freddo di pannelli stratificati",
            Category.SUBCLASS,
        ),
        Classification(
            "24.33.03", "Presagomatura dell'acciaio per cemento armato e attività simili", Category.SUBCLASS
        ),
        Classification("24.34", "Trafilatura a freddo di fili", Category.CLASS),
        Classification("24.34.0", "Trafilatura a freddo di fili", Category.SUBCLASS),
        Classification("24.34.00", "Trafilatura a freddo di fili", Category.SUBCLASS),
        Classification("24.4", "Produzione di metalli preziosi di base e di altri metalli non ferrosi", Category.GROUP),
        Classification("24.41", "Produzione di metalli preziosi", Category.CLASS),
        Classification("24.41.0", "Produzione di metalli preziosi", Category.SUBCLASS),
        Classification("24.41.00", "Produzione di metalli preziosi", Category.SUBCLASS),
        Classification("24.42", "Produzione di alluminio", Category.CLASS),
        Classification("24.42.0", "Produzione di alluminio", Category.SUBCLASS),
        Classification("24.42.00", "Produzione di alluminio", Category.SUBCLASS),
        Classification("24.43", "Produzione di piombo, zinco e stagno", Category.CLASS),
        Classification("24.43.0", "Produzione di piombo, zinco e stagno", Category.SUBCLASS),
        Classification("24.43.00", "Produzione di piombo, zinco e stagno", Category.SUBCLASS),
        Classification("24.44", "Produzione di rame", Category.CLASS),
        Classification("24.44.0", "Produzione di rame", Category.SUBCLASS),
        Classification("24.44.00", "Produzione di rame", Category.SUBCLASS),
        Classification("24.45", "Produzione di altri metalli non ferrosi", Category.CLASS),
        Classification("24.45.0", "Produzione di altri metalli non ferrosi", Category.SUBCLASS),
        Classification("24.45.00", "Produzione di altri metalli non ferrosi", Category.SUBCLASS),
        Classification("24.46", "Trattamento di combustibili nucleari", Category.CLASS),
        Classification("24.46.0", "Trattamento di combustibili nucleari", Category.SUBCLASS),
        Classification("24.46.00", "Trattamento di combustibili nucleari", Category.SUBCLASS),
        Classification("24.5", "Fusione di getti in metallo", Category.GROUP),
        Classification("24.51", "Fusione di getti in ghisa", Category.CLASS),
        Classification("24.51.0", "Fusione di getti in ghisa", Category.SUBCLASS),
        Classification("24.51.01", "Fusione di getti in ghisa grigia o lamellare", Category.SUBCLASS),
        Classification("24.51.02", "Fusione di getti in ghisa duttile", Category.SUBCLASS),
        Classification("24.51.09", "Fusione di getti in ghisa n.c.a.", Category.SUBCLASS),
        Classification("24.52", "Fusione di getti in acciaio", Category.CLASS),
        Classification("24.52.0", "Fusione di getti in acciaio", Category.SUBCLASS),
        Classification("24.52.00", "Fusione di getti in acciaio", Category.SUBCLASS),
        Classification("24.53", "Fusione di getti in metalli leggeri", Category.CLASS),
        Classification("24.53.0", "Fusione di getti in metalli leggeri", Category.SUBCLASS),
        Classification("24.53.01", "Fusione di getti in alluminio", Category.SUBCLASS),
        Classification("24.53.02", "Fusione di getti in magnesio", Category.SUBCLASS),
        Classification("24.53.03", "Fusione di getti in superleghe a base cobalto", Category.SUBCLASS),
        Classification("24.53.09", "Fusione di getti in metalli leggeri n.c.a.", Category.SUBCLASS),
        Classification("24.54", "Fusione di getti in altri metalli non ferrosi", Category.CLASS),
        Classification("24.54.0", "Fusione di getti in altri metalli non ferrosi", Category.SUBCLASS),
        Classification("24.54.01", "Fusione di getti in rame", Category.SUBCLASS),
        Classification("24.54.02", "Fusione di getti in zinco", Category.SUBCLASS),
        Classification("24.54.03", "Fusione di getti in nichel", Category.SUBCLASS),
        Classification("24.54.09", "Fusione di getti in altri metalli non ferrosi n.c.a.", Category.SUBCLASS),
        Classification(
            "25", "Fabbricazione di prodotti in metallo, esclusi macchinari e attrezzature", Category.DIVISION
        ),
        Classification("25.1", "Fabbricazione di elementi da costruzione in metallo", Category.GROUP),
        Classification(
            "25.11", "Fabbricazione di strutture metalliche e di parti di strutture metalliche", Category.CLASS
        ),
        Classification(
            "25.11.0", "Fabbricazione di strutture metalliche e di parti di strutture metalliche", Category.SUBCLASS
        ),
        Classification(
            "25.11.00", "Fabbricazione di strutture metalliche e di parti di strutture metalliche", Category.SUBCLASS
        ),
        Classification("25.12", "Fabbricazione di porte e finestre in metallo", Category.CLASS),
        Classification(
            "25.12.1", "Fabbricazione di porte, finestre e loro telai, imposte e cancelli in metallo", Category.SUBCLASS
        ),
        Classification(
            "25.12.10",
            "Fabbricazione di porte, finestre e loro telai, imposte e cancelli in metallo",
            Category.SUBCLASS,
        ),
        Classification("25.12.2", "Fabbricazione di tende in metallo e prodotti simili", Category.SUBCLASS),
        Classification("25.12.20", "Fabbricazione di tende in metallo e prodotti simili", Category.SUBCLASS),
        Classification("25.2", "Fabbricazione di cisterne, serbatoi e contenitori in metallo", Category.GROUP),
        Classification(
            "25.21",
            "Fabbricazione di radiatori, generatori di vapore e contenitori in metallo per caldaie per il riscaldamento centrale",
            Category.CLASS,
        ),
        Classification(
            "25.21.1",
            "Fabbricazione di radiatori e contenitori in metallo per caldaie per il riscaldamento centrale",
            Category.SUBCLASS,
        ),
        Classification(
            "25.21.10",
            "Fabbricazione di radiatori e contenitori in metallo per caldaie per il riscaldamento centrale",
            Category.SUBCLASS,
        ),
        Classification("25.21.2", "Fabbricazione di generatori di vapore", Category.SUBCLASS),
        Classification("25.21.20", "Fabbricazione di generatori di vapore", Category.SUBCLASS),
        Classification("25.22", "Fabbricazione di altre cisterne, serbatoi e contenitori in metallo", Category.CLASS),
        Classification(
            "25.22.0", "Fabbricazione di altre cisterne, serbatoi e contenitori in metallo", Category.SUBCLASS
        ),
        Classification(
            "25.22.00", "Fabbricazione di altre cisterne, serbatoi e contenitori in metallo", Category.SUBCLASS
        ),
        Classification("25.3", "Fabbricazione di armi e munizioni", Category.GROUP),
        Classification("25.30", "Fabbricazione di armi e munizioni", Category.CLASS),
        Classification("25.30.1", "Fabbricazione di armi e munizioni per uso militare", Category.SUBCLASS),
        Classification("25.30.10", "Fabbricazione di armi e munizioni per uso militare", Category.SUBCLASS),
        Classification("25.30.2", "Fabbricazione di armi e munizioni per uso sportivo e civile", Category.SUBCLASS),
        Classification("25.30.20", "Fabbricazione di armi e munizioni per uso sportivo e civile", Category.SUBCLASS),
        Classification("25.4", "Fucinatura e formatura dei metalli e metallurgia delle polveri", Category.GROUP),
        Classification("25.40", "Fucinatura e formatura dei metalli e metallurgia delle polveri", Category.CLASS),
        Classification("25.40.0", "Fucinatura e formatura dei metalli e metallurgia delle polveri", Category.SUBCLASS),
        Classification("25.40.00", "Fucinatura e formatura dei metalli e metallurgia delle polveri", Category.SUBCLASS),
        Classification("25.5", "Trattamento e rivestimento dei metalli; lavori di meccanica generale", Category.GROUP),
        Classification("25.51", "Rivestimento dei metalli", Category.CLASS),
        Classification("25.51.0", "Rivestimento dei metalli", Category.SUBCLASS),
        Classification("25.51.00", "Rivestimento dei metalli", Category.SUBCLASS),
        Classification("25.52", "Trattamento termico dei metalli", Category.CLASS),
        Classification("25.52.0", "Trattamento termico dei metalli", Category.SUBCLASS),
        Classification("25.52.00", "Trattamento termico dei metalli", Category.SUBCLASS),
        Classification("25.53", "Lavori di meccanica generale dei metalli", Category.CLASS),
        Classification("25.53.0", "Lavori di meccanica generale dei metalli", Category.SUBCLASS),
        Classification("25.53.00", "Lavori di meccanica generale dei metalli", Category.SUBCLASS),
        Classification(
            "25.6",
            "Fabbricazione di articoli di coltelleria e posateria, utensili e oggetti di ferramenta",
            Category.GROUP,
        ),
        Classification("25.61", "Fabbricazione di articoli di coltelleria e posateria", Category.CLASS),
        Classification("25.61.0", "Fabbricazione di articoli di coltelleria e posateria", Category.SUBCLASS),
        Classification("25.61.00", "Fabbricazione di articoli di coltelleria e posateria", Category.SUBCLASS),
        Classification("25.62", "Fabbricazione di serrature e cerniere", Category.CLASS),
        Classification("25.62.0", "Fabbricazione di serrature e cerniere", Category.SUBCLASS),
        Classification("25.62.00", "Fabbricazione di serrature e cerniere", Category.SUBCLASS),
        Classification("25.63", "Fabbricazione di utensileria", Category.CLASS),
        Classification(
            "25.63.1",
            "Fabbricazione di utensileria ad azionamento manuale e di parti intercambiabili per macchine utensili",
            Category.SUBCLASS,
        ),
        Classification("25.63.11", "Fabbricazione di utensileria ad azionamento manuale", Category.SUBCLASS),
        Classification("25.63.12", "Fabbricazione di parti intercambiabili per macchine utensili", Category.SUBCLASS),
        Classification(
            "25.63.2", "Fabbricazione di stampi, portastampi, sagome, forme per macchine", Category.SUBCLASS
        ),
        Classification(
            "25.63.20", "Fabbricazione di stampi, portastampi, sagome, forme per macchine", Category.SUBCLASS
        ),
        Classification("25.9", "Fabbricazione di altri prodotti in metallo", Category.GROUP),
        Classification("25.91", "Fabbricazione di bidoni in acciaio e di contenitori simili", Category.CLASS),
        Classification("25.91.0", "Fabbricazione di bidoni in acciaio e di contenitori simili", Category.SUBCLASS),
        Classification("25.91.00", "Fabbricazione di bidoni in acciaio e di contenitori simili", Category.SUBCLASS),
        Classification("25.92", "Fabbricazione di imballaggi in metallo leggero", Category.CLASS),
        Classification("25.92.0", "Fabbricazione di imballaggi in metallo leggero", Category.SUBCLASS),
        Classification("25.92.00", "Fabbricazione di imballaggi in metallo leggero", Category.SUBCLASS),
        Classification(
            "25.93", "Fabbricazione di prodotti fabbricati con fili metallici, catene e molle", Category.CLASS
        ),
        Classification("25.93.1", "Fabbricazione di prodotti fabbricati con fili metallici", Category.SUBCLASS),
        Classification("25.93.10", "Fabbricazione di prodotti fabbricati con fili metallici", Category.SUBCLASS),
        Classification("25.93.2", "Fabbricazione di catene", Category.SUBCLASS),
        Classification("25.93.20", "Fabbricazione di catene", Category.SUBCLASS),
        Classification("25.93.3", "Fabbricazione di molle", Category.SUBCLASS),
        Classification("25.93.30", "Fabbricazione di molle", Category.SUBCLASS),
        Classification("25.94", "Fabbricazione di articoli di bulloneria", Category.CLASS),
        Classification("25.94.0", "Fabbricazione di articoli di bulloneria", Category.SUBCLASS),
        Classification("25.94.00", "Fabbricazione di articoli di bulloneria", Category.SUBCLASS),
        Classification("25.99", "Fabbricazione di altri prodotti in metallo n.c.a.", Category.CLASS),
        Classification(
            "25.99.1",
            "Fabbricazione di articoli domestici in metallo per la cucina e le stanze da bagno",
            Category.SUBCLASS,
        ),
        Classification(
            "25.99.10",
            "Fabbricazione di articoli domestici in metallo per la cucina e le stanze da bagno",
            Category.SUBCLASS,
        ),
        Classification(
            "25.99.2",
            "Fabbricazione di casseforti, cassette di sicurezza e porte metalliche blindate",
            Category.SUBCLASS,
        ),
        Classification(
            "25.99.20",
            "Fabbricazione di casseforti, cassette di sicurezza e porte metalliche blindate",
            Category.SUBCLASS,
        ),
        Classification("25.99.9", "Fabbricazione di altri prodotti vari in metallo n.c.a.", Category.SUBCLASS),
        Classification("25.99.90", "Fabbricazione di altri prodotti vari in metallo n.c.a.", Category.SUBCLASS),
        Classification("26", "Fabbricazione di computer e prodotti di elettronica e ottica", Category.DIVISION),
        Classification("26.1", "Fabbricazione di componenti elettronici e schede elettroniche", Category.GROUP),
        Classification("26.11", "Fabbricazione di componenti elettronici", Category.CLASS),
        Classification("26.11.0", "Fabbricazione di componenti elettronici", Category.SUBCLASS),
        Classification("26.11.00", "Fabbricazione di componenti elettronici", Category.SUBCLASS),
        Classification("26.12", "Fabbricazione di schede elettroniche integrate", Category.CLASS),
        Classification("26.12.0", "Fabbricazione di schede elettroniche integrate", Category.SUBCLASS),
        Classification("26.12.00", "Fabbricazione di schede elettroniche integrate", Category.SUBCLASS),
        Classification("26.2", "Fabbricazione di computer e unità periferiche", Category.GROUP),
        Classification("26.20", "Fabbricazione di computer e unità periferiche", Category.CLASS),
        Classification("26.20.0", "Fabbricazione di computer e unità periferiche", Category.SUBCLASS),
        Classification("26.20.00", "Fabbricazione di computer e unità periferiche", Category.SUBCLASS),
        Classification("26.3", "Fabbricazione di apparecchiature per le comunicazioni", Category.GROUP),
        Classification("26.30", "Fabbricazione di apparecchiature per le comunicazioni", Category.CLASS),
        Classification("26.30.0", "Fabbricazione di apparecchiature per le comunicazioni", Category.SUBCLASS),
        Classification("26.30.01", "Fabbricazione di apparecchiature trasmittenti radiotelevisive", Category.SUBCLASS),
        Classification("26.30.09", "Fabbricazione di altre apparecchiature per le comunicazioni", Category.SUBCLASS),
        Classification("26.4", "Fabbricazione di prodotti di elettronica di consumo", Category.GROUP),
        Classification("26.40", "Fabbricazione di prodotti di elettronica di consumo", Category.CLASS),
        Classification("26.40.0", "Fabbricazione di prodotti di elettronica di consumo", Category.SUBCLASS),
        Classification("26.40.01", "Fabbricazione di console per videogiochi", Category.SUBCLASS),
        Classification("26.40.09", "Fabbricazione di altri prodotti di elettronica di consumo", Category.SUBCLASS),
        Classification("26.5", "Fabbricazione di strumenti di misurazione e prova e di orologi", Category.GROUP),
        Classification(
            "26.51", "Fabbricazione di strumenti e apparecchi di misurazione, prova e navigazione", Category.CLASS
        ),
        Classification(
            "26.51.1",
            "Fabbricazione di strumenti per navigazione, idrologia, geofisica e meteorologia",
            Category.SUBCLASS,
        ),
        Classification(
            "26.51.10",
            "Fabbricazione di strumenti per navigazione, idrologia, geofisica e meteorologia",
            Category.SUBCLASS,
        ),
        Classification(
            "26.51.2", "Fabbricazione di altri strumenti e apparecchi di misurazione e prova", Category.SUBCLASS
        ),
        Classification("26.51.21", "Fabbricazione di sistemi antifurto e antincendio", Category.SUBCLASS),
        Classification(
            "26.51.29", "Fabbricazione di altri strumenti e apparecchi di misurazione e prova n.c.a.", Category.SUBCLASS
        ),
        Classification("26.52", "Fabbricazione di orologi", Category.CLASS),
        Classification("26.52.0", "Fabbricazione di orologi", Category.SUBCLASS),
        Classification("26.52.00", "Fabbricazione di orologi", Category.SUBCLASS),
        Classification(
            "26.6",
            "Fabbricazione di apparecchiature per irradiazione, elettromedicali ed elettroterapeutiche",
            Category.GROUP,
        ),
        Classification(
            "26.60",
            "Fabbricazione di apparecchiature per irradiazione, elettromedicali ed elettroterapeutiche",
            Category.CLASS,
        ),
        Classification(
            "26.60.0",
            "Fabbricazione di apparecchiature per irradiazione, elettromedicali ed elettroterapeutiche",
            Category.SUBCLASS,
        ),
        Classification(
            "26.60.01",
            "Fabbricazione di apparecchiature per irradiazione, elettromedicali ed elettroterapeutiche per usi medici",
            Category.SUBCLASS,
        ),
        Classification(
            "26.60.02",
            "Fabbricazione di apparecchiature per irradiazione, elettromedicali ed elettroterapeutiche per usi non medici",
            Category.SUBCLASS,
        ),
        Classification(
            "26.7",
            "Fabbricazione di strumenti ottici, supporti magnetici e ottici e apparecchiature fotografiche",
            Category.GROUP,
        ),
        Classification(
            "26.70",
            "Fabbricazione di strumenti ottici, supporti magnetici e ottici e apparecchiature fotografiche",
            Category.CLASS,
        ),
        Classification(
            "26.70.1",
            "Fabbricazione di strumenti ottici, strumenti ottici di precisione, misurazione e controllo",
            Category.SUBCLASS,
        ),
        Classification(
            "26.70.11", "Fabbricazione di strumenti ottici e strumenti ottici di precisione", Category.SUBCLASS
        ),
        Classification("26.70.12", "Fabbricazione di strumenti ottici di misurazione e controllo", Category.SUBCLASS),
        Classification("26.70.2", "Fabbricazione di supporti magnetici e ottici", Category.SUBCLASS),
        Classification("26.70.20", "Fabbricazione di supporti magnetici e ottici", Category.SUBCLASS),
        Classification("26.70.3", "Fabbricazione di apparecchiature fotografiche", Category.SUBCLASS),
        Classification("26.70.30", "Fabbricazione di apparecchiature fotografiche", Category.SUBCLASS),
        Classification("27", "Fabbricazione di apparecchiature elettriche", Category.DIVISION),
        Classification(
            "27.1",
            "Fabbricazione di motori, generatori e trasformatori elettrici e di apparecchiature per la distribuzione e il controllo dell'elettricità",
            Category.GROUP,
        ),
        Classification("27.11", "Fabbricazione di motori, generatori e trasformatori elettrici", Category.CLASS),
        Classification("27.11.0", "Fabbricazione di motori, generatori e trasformatori elettrici", Category.SUBCLASS),
        Classification("27.11.00", "Fabbricazione di motori, generatori e trasformatori elettrici", Category.SUBCLASS),
        Classification(
            "27.12",
            "Fabbricazione di apparecchiature per la distribuzione e il controllo dell'elettricità",
            Category.CLASS,
        ),
        Classification(
            "27.12.0",
            "Fabbricazione di apparecchiature per la distribuzione e il controllo dell'elettricità",
            Category.SUBCLASS,
        ),
        Classification(
            "27.12.00",
            "Fabbricazione di apparecchiature per la distribuzione e il controllo dell'elettricità",
            Category.SUBCLASS,
        ),
        Classification("27.2", "Fabbricazione di batterie e accumulatori", Category.GROUP),
        Classification("27.20", "Fabbricazione di batterie e accumulatori", Category.CLASS),
        Classification("27.20.0", "Fabbricazione di batterie e accumulatori", Category.SUBCLASS),
        Classification("27.20.00", "Fabbricazione di batterie e accumulatori", Category.SUBCLASS),
        Classification("27.3", "Fabbricazione di cablaggi e attrezzature per cablaggio", Category.GROUP),
        Classification("27.31", "Fabbricazione di cavi in fibra ottica", Category.CLASS),
        Classification("27.31.0", "Fabbricazione di cavi in fibra ottica", Category.SUBCLASS),
        Classification("27.31.00", "Fabbricazione di cavi in fibra ottica", Category.SUBCLASS),
        Classification("27.32", "Fabbricazione di altri fili e cavi elettronici ed elettrici", Category.CLASS),
        Classification("27.32.0", "Fabbricazione di altri fili e cavi elettronici ed elettrici", Category.SUBCLASS),
        Classification("27.32.00", "Fabbricazione di altri fili e cavi elettronici ed elettrici", Category.SUBCLASS),
        Classification("27.33", "Fabbricazione di attrezzature per cablaggio", Category.CLASS),
        Classification("27.33.0", "Fabbricazione di attrezzature per cablaggio", Category.SUBCLASS),
        Classification("27.33.00", "Fabbricazione di attrezzature per cablaggio", Category.SUBCLASS),
        Classification("27.4", "Fabbricazione di apparecchiature per l'illuminazione", Category.GROUP),
        Classification("27.40", "Fabbricazione di apparecchiature per l'illuminazione", Category.CLASS),
        Classification("27.40.0", "Fabbricazione di apparecchiature per l'illuminazione", Category.SUBCLASS),
        Classification(
            "27.40.01", "Fabbricazione di apparecchiature per l'illuminazione per mezzi di trasporto", Category.SUBCLASS
        ),
        Classification("27.40.02", "Fabbricazione di luminarie per feste", Category.SUBCLASS),
        Classification("27.40.09", "Fabbricazione di altre apparecchiature per l'illuminazione", Category.SUBCLASS),
        Classification("27.5", "Fabbricazione di apparecchi per uso domestico", Category.GROUP),
        Classification("27.51", "Fabbricazione di elettrodomestici", Category.CLASS),
        Classification("27.51.0", "Fabbricazione di elettrodomestici", Category.SUBCLASS),
        Classification("27.51.00", "Fabbricazione di elettrodomestici", Category.SUBCLASS),
        Classification("27.52", "Fabbricazione di apparecchi non elettrici per uso domestico", Category.CLASS),
        Classification("27.52.0", "Fabbricazione di apparecchi non elettrici per uso domestico", Category.SUBCLASS),
        Classification("27.52.00", "Fabbricazione di apparecchi non elettrici per uso domestico", Category.SUBCLASS),
        Classification("27.9", "Fabbricazione di altre apparecchiature elettriche", Category.GROUP),
        Classification("27.90", "Fabbricazione di altre apparecchiature elettriche", Category.CLASS),
        Classification("27.90.0", "Fabbricazione di altre apparecchiature elettriche", Category.SUBCLASS),
        Classification(
            "27.90.01", "Fabbricazione di apparecchiature elettriche per saldatura e brasatura", Category.SUBCLASS
        ),
        Classification(
            "27.90.02",
            "Fabbricazione di insegne elettriche e apparecchiature elettriche di segnalazione",
            Category.SUBCLASS,
        ),
        Classification(
            "27.90.03", "Fabbricazione di capacitori, resistenze, condensatori elettrici e simili", Category.SUBCLASS
        ),
        Classification(
            "27.90.04",
            "Fabbricazione di apparecchiature elettriche per parrucchieri, solarium e centri estetici",
            Category.SUBCLASS,
        ),
        Classification("27.90.09", "Fabbricazione di altre apparecchiature elettriche n.c.a.", Category.SUBCLASS),
        Classification("28", "Fabbricazione di macchinari e apparecchiature n.c.a.", Category.DIVISION),
        Classification("28.1", "Fabbricazione di macchine di impiego generale", Category.GROUP),
        Classification(
            "28.11",
            "Fabbricazione di motori e turbine, esclusi i motori per aeromobili, veicoli e motocicli",
            Category.CLASS,
        ),
        Classification(
            "28.11.1", "Fabbricazione di motori, esclusi motori per aeromobili, veicoli e motocicli", Category.SUBCLASS
        ),
        Classification(
            "28.11.10", "Fabbricazione di motori, esclusi motori per aeromobili, veicoli e motocicli", Category.SUBCLASS
        ),
        Classification("28.11.2", "Fabbricazione di turbine", Category.SUBCLASS),
        Classification("28.11.20", "Fabbricazione di turbine", Category.SUBCLASS),
        Classification("28.12", "Fabbricazione di apparecchiature fluidodinamiche", Category.CLASS),
        Classification("28.12.0", "Fabbricazione di apparecchiature fluidodinamiche", Category.SUBCLASS),
        Classification("28.12.00", "Fabbricazione di apparecchiature fluidodinamiche", Category.SUBCLASS),
        Classification("28.13", "Fabbricazione di altre pompe e compressori", Category.CLASS),
        Classification("28.13.0", "Fabbricazione di altre pompe e compressori", Category.SUBCLASS),
        Classification("28.13.00", "Fabbricazione di altre pompe e compressori", Category.SUBCLASS),
        Classification("28.14", "Fabbricazione di altri rubinetti e valvole", Category.CLASS),
        Classification("28.14.0", "Fabbricazione di altri rubinetti e valvole", Category.SUBCLASS),
        Classification("28.14.00", "Fabbricazione di altri rubinetti e valvole", Category.SUBCLASS),
        Classification("28.15", "Fabbricazione di cuscinetti, ingranaggi e organi di trasmissione", Category.CLASS),
        Classification(
            "28.15.0", "Fabbricazione di cuscinetti, ingranaggi e organi di trasmissione", Category.SUBCLASS
        ),
        Classification(
            "28.15.00", "Fabbricazione di cuscinetti, ingranaggi e organi di trasmissione", Category.SUBCLASS
        ),
        Classification("28.2", "Fabbricazione di altre macchine di impiego generale", Category.GROUP),
        Classification(
            "28.21",
            "Fabbricazione di forni, caldaie e apparecchiature fisse per il riscaldamento domestico",
            Category.CLASS,
        ),
        Classification("28.21.1", "Fabbricazione di forni", Category.SUBCLASS),
        Classification("28.21.10", "Fabbricazione di forni", Category.SUBCLASS),
        Classification(
            "28.21.2",
            "Fabbricazione di caldaie e apparecchiature fisse per il riscaldamento domestico",
            Category.SUBCLASS,
        ),
        Classification(
            "28.21.20",
            "Fabbricazione di caldaie e apparecchiature fisse per il riscaldamento domestico",
            Category.SUBCLASS,
        ),
        Classification("28.22", "Fabbricazione di apparecchi di sollevamento e movimentazione", Category.CLASS),
        Classification("28.22.0", "Fabbricazione di apparecchi di sollevamento e movimentazione", Category.SUBCLASS),
        Classification("28.22.01", "Fabbricazione di ascensori, scale mobili e tappeti mobili", Category.SUBCLASS),
        Classification(
            "28.22.09", "Fabbricazione di altri apparecchi di sollevamento e movimentazione", Category.SUBCLASS
        ),
        Classification(
            "28.23",
            "Fabbricazione di macchine e attrezzature per ufficio, esclusi computer e unità periferiche",
            Category.CLASS,
        ),
        Classification(
            "28.23.0",
            "Fabbricazione di macchine e attrezzature per ufficio, esclusi computer e unità periferiche",
            Category.SUBCLASS,
        ),
        Classification(
            "28.23.00",
            "Fabbricazione di macchine e attrezzature per ufficio, esclusi computer e unità periferiche",
            Category.SUBCLASS,
        ),
        Classification("28.24", "Fabbricazione di utensili portatili a motore", Category.CLASS),
        Classification("28.24.0", "Fabbricazione di utensili portatili a motore", Category.SUBCLASS),
        Classification("28.24.00", "Fabbricazione di utensili portatili a motore", Category.SUBCLASS),
        Classification(
            "28.25", "Fabbricazione di apparecchiature di climatizzazione per uso non domestico", Category.CLASS
        ),
        Classification(
            "28.25.0", "Fabbricazione di apparecchiature di climatizzazione per uso non domestico", Category.SUBCLASS
        ),
        Classification(
            "28.25.00", "Fabbricazione di apparecchiature di climatizzazione per uso non domestico", Category.SUBCLASS
        ),
        Classification("28.29", "Fabbricazione di altre macchine di impiego generale n.c.a.", Category.CLASS),
        Classification("28.29.1", "Fabbricazione di bilance e distributori automatici", Category.SUBCLASS),
        Classification("28.29.10", "Fabbricazione di bilance e distributori automatici", Category.SUBCLASS),
        Classification(
            "28.29.2",
            "Fabbricazione di impianti di distillazione o rettificazione per raffinerie di petrolio e industrie chimiche",
            Category.SUBCLASS,
        ),
        Classification(
            "28.29.20",
            "Fabbricazione di impianti di distillazione o rettificazione per raffinerie di petrolio e industrie chimiche",
            Category.SUBCLASS,
        ),
        Classification(
            "28.29.3", "Fabbricazione di macchine per la dosatura, la confezione e per l'imballaggio", Category.SUBCLASS
        ),
        Classification(
            "28.29.30",
            "Fabbricazione di macchine per la dosatura, la confezione e per l'imballaggio",
            Category.SUBCLASS,
        ),
        Classification("28.29.4", "Fabbricazione di macchine per la pulizia per uso non domestico", Category.SUBCLASS),
        Classification(
            "28.29.41",
            "Fabbricazione di macchine per la pulizia di pavimenti, superfici e ambienti per uso non domestico",
            Category.SUBCLASS,
        ),
        Classification(
            "28.29.49", "Fabbricazione di altre macchine per la pulizia per uso non domestico", Category.SUBCLASS
        ),
        Classification("28.29.9", "Fabbricazione di altre macchine varie di impiego generale", Category.SUBCLASS),
        Classification("28.29.91", "Fabbricazione di apparecchi per depurare e filtrare liquidi", Category.SUBCLASS),
        Classification(
            "28.29.92",
            "Fabbricazione di livelle, metri doppi a nastro e utensili simili, strumenti di precisione per meccanica",
            Category.SUBCLASS,
        ),
        Classification(
            "28.29.99", "Fabbricazione di altre macchine varie di impiego generale n.c.a.", Category.SUBCLASS
        ),
        Classification("28.3", "Fabbricazione di macchine per l'agricoltura e la silvicoltura", Category.GROUP),
        Classification("28.30", "Fabbricazione di macchine per l'agricoltura e la silvicoltura", Category.CLASS),
        Classification("28.30.1", "Fabbricazione di trattori per l'agricoltura e la silvicoltura", Category.SUBCLASS),
        Classification("28.30.10", "Fabbricazione di trattori per l'agricoltura e la silvicoltura", Category.SUBCLASS),
        Classification(
            "28.30.9", "Fabbricazione di altre macchine per l'agricoltura e la silvicoltura", Category.SUBCLASS
        ),
        Classification(
            "28.30.91", "Fabbricazione di macchine per il giardinaggio e la cura del verde", Category.SUBCLASS
        ),
        Classification(
            "28.30.99", "Fabbricazione di altre macchine per l'agricoltura e la silvicoltura n.c.a.", Category.SUBCLASS
        ),
        Classification(
            "28.4",
            "Fabbricazione di macchine per la deformazione dei metalli e di altre macchine utensili",
            Category.GROUP,
        ),
        Classification(
            "28.41",
            "Fabbricazione di macchine per la deformazione dei metalli e di altre macchine utensili per la lavorazione dei metalli",
            Category.CLASS,
        ),
        Classification(
            "28.41.0",
            "Fabbricazione di macchine per la deformazione dei metalli e di altre macchine utensili per la lavorazione dei metalli",
            Category.SUBCLASS,
        ),
        Classification(
            "28.41.00",
            "Fabbricazione di macchine per la deformazione dei metalli e di altre macchine utensili per la lavorazione dei metalli",
            Category.SUBCLASS,
        ),
        Classification("28.42", "Fabbricazione di altre macchine utensili", Category.CLASS),
        Classification("28.42.0", "Fabbricazione di altre macchine utensili", Category.SUBCLASS),
        Classification("28.42.00", "Fabbricazione di altre macchine utensili", Category.SUBCLASS),
        Classification("28.9", "Fabbricazione di altre macchine per impieghi speciali", Category.GROUP),
        Classification("28.91", "Fabbricazione di macchine per la metallurgia", Category.CLASS),
        Classification("28.91.0", "Fabbricazione di macchine per la metallurgia", Category.SUBCLASS),
        Classification("28.91.00", "Fabbricazione di macchine per la metallurgia", Category.SUBCLASS),
        Classification("28.92", "Fabbricazione di macchine da miniera, cava e cantiere", Category.CLASS),
        Classification("28.92.0", "Fabbricazione di macchine da miniera, cava e cantiere", Category.SUBCLASS),
        Classification("28.92.00", "Fabbricazione di macchine da miniera, cava e cantiere", Category.SUBCLASS),
        Classification(
            "28.93", "Fabbricazione di macchine per l'industria alimentare, delle bevande e del tabacco", Category.CLASS
        ),
        Classification(
            "28.93.0",
            "Fabbricazione di macchine per l'industria alimentare, delle bevande e del tabacco",
            Category.SUBCLASS,
        ),
        Classification(
            "28.93.00",
            "Fabbricazione di macchine per l'industria alimentare, delle bevande e del tabacco",
            Category.SUBCLASS,
        ),
        Classification(
            "28.94", "Fabbricazione di macchine per l'industria tessile, dell'abbigliamento e del cuoio", Category.CLASS
        ),
        Classification("28.94.1", "Fabbricazione di macchine tessili", Category.SUBCLASS),
        Classification("28.94.10", "Fabbricazione di macchine tessili", Category.SUBCLASS),
        Classification(
            "28.94.2", "Fabbricazione di macchine per la lavorazione delle pelli e del cuoio", Category.SUBCLASS
        ),
        Classification(
            "28.94.20", "Fabbricazione di macchine per la lavorazione delle pelli e del cuoio", Category.SUBCLASS
        ),
        Classification("28.94.3", "Fabbricazione di macchine per lavanderie e stirerie", Category.SUBCLASS),
        Classification("28.94.30", "Fabbricazione di macchine per lavanderie e stirerie", Category.SUBCLASS),
        Classification("28.95", "Fabbricazione di macchine per l'industria della carta e del cartone", Category.CLASS),
        Classification(
            "28.95.0", "Fabbricazione di macchine per l'industria della carta e del cartone", Category.SUBCLASS
        ),
        Classification(
            "28.95.00", "Fabbricazione di macchine per l'industria della carta e del cartone", Category.SUBCLASS
        ),
        Classification(
            "28.96", "Fabbricazione di macchine per l'industria delle materie plastiche e della gomma", Category.CLASS
        ),
        Classification(
            "28.96.0",
            "Fabbricazione di macchine per l'industria delle materie plastiche e della gomma",
            Category.SUBCLASS,
        ),
        Classification(
            "28.96.00",
            "Fabbricazione di macchine per l'industria delle materie plastiche e della gomma",
            Category.SUBCLASS,
        ),
        Classification("28.97", "Fabbricazione di macchine per la produzione additiva", Category.CLASS),
        Classification("28.97.0", "Fabbricazione di macchine per la produzione additiva", Category.SUBCLASS),
        Classification(
            "28.97.01",
            "Fabbricazione di macchine per la produzione additiva per deposizione di materiali metallici",
            Category.SUBCLASS,
        ),
        Classification(
            "28.97.02",
            "Fabbricazione di macchine per la produzione additiva per deposizione di materie plastiche o di gomma",
            Category.SUBCLASS,
        ),
        Classification("28.97.09", "Fabbricazione di macchine per la produzione additiva n.c.a.", Category.SUBCLASS),
        Classification("28.99", "Fabbricazione di altre macchine per impieghi speciali n.c.a.", Category.CLASS),
        Classification("28.99.1", "Fabbricazione di macchine per la stampa e la legatoria", Category.SUBCLASS),
        Classification("28.99.10", "Fabbricazione di macchine per la stampa e la legatoria", Category.SUBCLASS),
        Classification(
            "28.99.2", "Fabbricazione di robot industriali con compiti multipli per scopi speciali", Category.SUBCLASS
        ),
        Classification(
            "28.99.20", "Fabbricazione di robot industriali con compiti multipli per scopi speciali", Category.SUBCLASS
        ),
        Classification(
            "28.99.9", "Fabbricazione di altre macchine varie per impieghi speciali n.c.a.", Category.SUBCLASS
        ),
        Classification(
            "28.99.91",
            "Fabbricazione di apparecchiature per il lancio di aeromobili, catapulte per portaerei e relative attrezzature",
            Category.SUBCLASS,
        ),
        Classification(
            "28.99.92", "Fabbricazione di giostre, altalene e altre attrazioni di divertimento", Category.SUBCLASS
        ),
        Classification(
            "28.99.93",
            "Fabbricazione di apparecchiature per l'allineamento e il bilanciamento delle ruote e altre apparecchiature per il bilanciamento",
            Category.SUBCLASS,
        ),
        Classification(
            "28.99.99", "Fabbricazione di tutte le altre macchine varie per impieghi speciali n.c.a.", Category.SUBCLASS
        ),
        Classification("29", "Fabbricazione di autoveicoli, rimorchi e semirimorchi", Category.DIVISION),
        Classification("29.1", "Fabbricazione di autoveicoli", Category.GROUP),
        Classification("29.10", "Fabbricazione di autoveicoli", Category.CLASS),
        Classification("29.10.0", "Fabbricazione di autoveicoli", Category.SUBCLASS),
        Classification("29.10.00", "Fabbricazione di autoveicoli", Category.SUBCLASS),
        Classification(
            "29.2",
            "Fabbricazione di carrozzerie per autoveicoli; fabbricazione di rimorchi e semirimorchi",
            Category.GROUP,
        ),
        Classification(
            "29.20",
            "Fabbricazione di carrozzerie per autoveicoli; fabbricazione di rimorchi e semirimorchi",
            Category.CLASS,
        ),
        Classification(
            "29.20.0",
            "Fabbricazione di carrozzerie per autoveicoli; fabbricazione di rimorchi e semirimorchi",
            Category.SUBCLASS,
        ),
        Classification(
            "29.20.00",
            "Fabbricazione di carrozzerie per autoveicoli; fabbricazione di rimorchi e semirimorchi",
            Category.SUBCLASS,
        ),
        Classification("29.3", "Fabbricazione di parti e accessori per autoveicoli", Category.GROUP),
        Classification(
            "29.31", "Fabbricazione di apparecchiature elettriche ed elettroniche per autoveicoli", Category.CLASS
        ),
        Classification(
            "29.31.0", "Fabbricazione di apparecchiature elettriche ed elettroniche per autoveicoli", Category.SUBCLASS
        ),
        Classification(
            "29.31.00", "Fabbricazione di apparecchiature elettriche ed elettroniche per autoveicoli", Category.SUBCLASS
        ),
        Classification("29.32", "Fabbricazione di altre parti e accessori per autoveicoli", Category.CLASS),
        Classification("29.32.0", "Fabbricazione di altre parti e accessori per autoveicoli", Category.SUBCLASS),
        Classification("29.32.00", "Fabbricazione di altre parti e accessori per autoveicoli", Category.SUBCLASS),
        Classification("30", "Fabbricazione di altri mezzi di trasporto", Category.DIVISION),
        Classification("30.1", "Costruzione di navi e imbarcazioni", Category.GROUP),
        Classification("30.11", "Costruzione di navi e di strutture galleggianti per scopi civili", Category.CLASS),
        Classification(
            "30.11.0", "Costruzione di navi e di strutture galleggianti per scopi civili", Category.SUBCLASS
        ),
        Classification(
            "30.11.00", "Costruzione di navi e di strutture galleggianti per scopi civili", Category.SUBCLASS
        ),
        Classification("30.12", "Costruzione di imbarcazioni da diporto e sportive", Category.CLASS),
        Classification("30.12.0", "Costruzione di imbarcazioni da diporto e sportive", Category.SUBCLASS),
        Classification("30.12.00", "Costruzione di imbarcazioni da diporto e sportive", Category.SUBCLASS),
        Classification("30.13", "Costruzione di navi e imbarcazioni per scopi militari", Category.CLASS),
        Classification("30.13.0", "Costruzione di navi e imbarcazioni per scopi militari", Category.SUBCLASS),
        Classification("30.13.00", "Costruzione di navi e imbarcazioni per scopi militari", Category.SUBCLASS),
        Classification("30.2", "Costruzione di locomotive e di materiale rotabile ferro-tranviario", Category.GROUP),
        Classification("30.20", "Costruzione di locomotive e di materiale rotabile ferro-tranviario", Category.CLASS),
        Classification(
            "30.20.0", "Costruzione di locomotive e di materiale rotabile ferro-tranviario", Category.SUBCLASS
        ),
        Classification(
            "30.20.00", "Costruzione di locomotive e di materiale rotabile ferro-tranviario", Category.SUBCLASS
        ),
        Classification(
            "30.3", "Fabbricazione di aeromobili, veicoli spaziali e relativi equipaggiamenti", Category.GROUP
        ),
        Classification(
            "30.31",
            "Fabbricazione di aeromobili, veicoli spaziali e relativi equipaggiamenti per scopi civili",
            Category.CLASS,
        ),
        Classification(
            "30.31.0",
            "Fabbricazione di aeromobili, veicoli spaziali e relativi equipaggiamenti per scopi civili",
            Category.SUBCLASS,
        ),
        Classification(
            "30.31.00",
            "Fabbricazione di aeromobili, veicoli spaziali e relativi equipaggiamenti per scopi civili",
            Category.SUBCLASS,
        ),
        Classification(
            "30.32",
            "Fabbricazione di aeromobili, veicoli spaziali e relativi equipaggiamenti per scopi militari",
            Category.CLASS,
        ),
        Classification(
            "30.32.0",
            "Fabbricazione di aeromobili, veicoli spaziali e relativi equipaggiamenti per scopi militari",
            Category.SUBCLASS,
        ),
        Classification(
            "30.32.00",
            "Fabbricazione di aeromobili, veicoli spaziali e relativi equipaggiamenti per scopi militari",
            Category.SUBCLASS,
        ),
        Classification("30.4", "Fabbricazione di veicoli militari da combattimento", Category.GROUP),
        Classification("30.40", "Fabbricazione di veicoli militari da combattimento", Category.CLASS),
        Classification("30.40.0", "Fabbricazione di veicoli militari da combattimento", Category.SUBCLASS),
        Classification("30.40.00", "Fabbricazione di veicoli militari da combattimento", Category.SUBCLASS),
        Classification("30.9", "Fabbricazione di mezzi di trasporto n.c.a.", Category.GROUP),
        Classification("30.91", "Fabbricazione di motocicli", Category.CLASS),
        Classification("30.91.1", "Fabbricazione di motocicli, escluse parti e accessori", Category.SUBCLASS),
        Classification("30.91.11", "Fabbricazione di motori per motocicli", Category.SUBCLASS),
        Classification("30.91.12", "Fabbricazione di motocicli, esclusi motori", Category.SUBCLASS),
        Classification("30.91.2", "Fabbricazione di parti e accessori per motocicli", Category.SUBCLASS),
        Classification("30.91.20", "Fabbricazione di parti e accessori per motocicli", Category.SUBCLASS),
        Classification("30.92", "Fabbricazione di biciclette e veicoli per disabili", Category.CLASS),
        Classification("30.92.1", "Fabbricazione di biciclette, escluse parti e accessori", Category.SUBCLASS),
        Classification("30.92.10", "Fabbricazione di biciclette, escluse parti e accessori", Category.SUBCLASS),
        Classification("30.92.2", "Fabbricazione di parti e accessori per biciclette", Category.SUBCLASS),
        Classification("30.92.20", "Fabbricazione di parti e accessori per biciclette", Category.SUBCLASS),
        Classification("30.92.3", "Fabbricazione di veicoli per disabili", Category.SUBCLASS),
        Classification("30.92.30", "Fabbricazione di veicoli per disabili", Category.SUBCLASS),
        Classification("30.92.4", "Fabbricazione di carrozzine e passeggini", Category.SUBCLASS),
        Classification("30.92.40", "Fabbricazione di carrozzine e passeggini", Category.SUBCLASS),
        Classification("30.99", "Fabbricazione di altri mezzi di trasporto n.c.a.", Category.CLASS),
        Classification("30.99.0", "Fabbricazione di altri mezzi di trasporto n.c.a.", Category.SUBCLASS),
        Classification("30.99.00", "Fabbricazione di altri mezzi di trasporto n.c.a.", Category.SUBCLASS),
        Classification("31", "Fabbricazione di mobili", Category.DIVISION),
        Classification("31.0", "Fabbricazione di mobili", Category.GROUP),
        Classification("31.00", "Fabbricazione di mobili", Category.CLASS),
        Classification(
            "31.00.1", "Fabbricazione di mobili per negozi, uffici e altri spazi per collettività", Category.SUBCLASS
        ),
        Classification(
            "31.00.11",
            "Fabbricazione di moduli dedicati al comfort acustico per negozi, uffici e altri spazi per collettività",
            Category.SUBCLASS,
        ),
        Classification("31.00.12", "Fabbricazione di sedie e poltrone per negozi", Category.SUBCLASS),
        Classification("31.00.13", "Fabbricazione di altri mobili per negozi", Category.SUBCLASS),
        Classification(
            "31.00.14", "Fabbricazione di sedie e poltrone per uffici e altri spazi per collettività", Category.SUBCLASS
        ),
        Classification(
            "31.00.15", "Fabbricazione di altri mobili per uffici e altri spazi per collettività", Category.SUBCLASS
        ),
        Classification("31.00.2", "Fabbricazione di mobili da cucina", Category.SUBCLASS),
        Classification("31.00.20", "Fabbricazione di mobili da cucina", Category.SUBCLASS),
        Classification("31.00.3", "Fabbricazione di altri mobili per la casa", Category.SUBCLASS),
        Classification(
            "31.00.31",
            "Fabbricazione di mobili per arredo interno, esclusi mobili da cucina, sedie, divani e prodotti simili",
            Category.SUBCLASS,
        ),
        Classification("31.00.32", "Fabbricazione di mobili per arredo esterno", Category.SUBCLASS),
        Classification("31.00.33", "Fabbricazione di sedie e sedili", Category.SUBCLASS),
        Classification("31.00.34", "Fabbricazione di divani, divani letto e poltrone", Category.SUBCLASS),
        Classification("31.00.35", "Fabbricazione di materassi", Category.SUBCLASS),
        Classification("31.00.36", "Fabbricazione di parti e accessori di mobili", Category.SUBCLASS),
        Classification("31.00.37", "Finitura di mobili", Category.SUBCLASS),
        Classification("31.00.39", "Fabbricazione di altri mobili n.c.a.", Category.SUBCLASS),
        Classification("32", "Altre attività manifatturiere", Category.DIVISION),
        Classification("32.1", "Fabbricazione di gioielleria, bigiotteria e articoli connessi", Category.GROUP),
        Classification("32.11", "Coniazione di monete", Category.CLASS),
        Classification("32.11.0", "Coniazione di monete", Category.SUBCLASS),
        Classification("32.11.00", "Coniazione di monete", Category.SUBCLASS),
        Classification("32.12", "Fabbricazione di gioielli e articoli simili", Category.CLASS),
        Classification("32.12.1", "Lavorazione di pietre preziose e semipreziose", Category.SUBCLASS),
        Classification("32.12.10", "Lavorazione di pietre preziose e semipreziose", Category.SUBCLASS),
        Classification(
            "32.12.2", "Fabbricazione di gioielli e articoli di oreficeria in metalli preziosi", Category.SUBCLASS
        ),
        Classification(
            "32.12.20", "Fabbricazione di gioielli e articoli di oreficeria in metalli preziosi", Category.SUBCLASS
        ),
        Classification("32.13", "Fabbricazione di bigiotteria e articoli simili", Category.CLASS),
        Classification("32.13.0", "Fabbricazione di bigiotteria e articoli simili", Category.SUBCLASS),
        Classification("32.13.00", "Fabbricazione di bigiotteria e articoli simili", Category.SUBCLASS),
        Classification("32.2", "Fabbricazione di strumenti musicali", Category.GROUP),
        Classification("32.20", "Fabbricazione di strumenti musicali", Category.CLASS),
        Classification("32.20.0", "Fabbricazione di strumenti musicali", Category.SUBCLASS),
        Classification("32.20.00", "Fabbricazione di strumenti musicali", Category.SUBCLASS),
        Classification("32.3", "Fabbricazione di articoli sportivi", Category.GROUP),
        Classification("32.30", "Fabbricazione di articoli sportivi", Category.CLASS),
        Classification("32.30.0", "Fabbricazione di articoli sportivi", Category.SUBCLASS),
        Classification(
            "32.30.01",
            "Fabbricazione di attrezzature da palestra, per centri di fitness e per atletica",
            Category.SUBCLASS,
        ),
        Classification("32.30.09", "Fabbricazione di altri articoli sportivi", Category.SUBCLASS),
        Classification("32.4", "Fabbricazione di giochi e giocattoli", Category.GROUP),
        Classification("32.40", "Fabbricazione di giochi e giocattoli", Category.CLASS),
        Classification("32.40.1", "Fabbricazione di giochi", Category.SUBCLASS),
        Classification("32.40.10", "Fabbricazione di giochi", Category.SUBCLASS),
        Classification("32.40.2", "Fabbricazione di giocattoli", Category.SUBCLASS),
        Classification("32.40.20", "Fabbricazione di giocattoli", Category.SUBCLASS),
        Classification("32.5", "Fabbricazione di strumenti e forniture mediche e dentistiche", Category.GROUP),
        Classification("32.50", "Fabbricazione di strumenti e forniture mediche e dentistiche", Category.CLASS),
        Classification("32.50.1", "Fabbricazione di protesi dentarie", Category.SUBCLASS),
        Classification("32.50.10", "Fabbricazione di protesi dentarie", Category.SUBCLASS),
        Classification("32.50.2", "Fabbricazione di altre protesi e ausili", Category.SUBCLASS),
        Classification("32.50.20", "Fabbricazione di altre protesi e ausili", Category.SUBCLASS),
        Classification("32.50.3", "Fabbricazione di lenti oftalmiche", Category.SUBCLASS),
        Classification("32.50.30", "Fabbricazione di lenti oftalmiche", Category.SUBCLASS),
        Classification("32.50.4", "Fabbricazione di montature per occhiali", Category.SUBCLASS),
        Classification("32.50.40", "Fabbricazione di montature per occhiali", Category.SUBCLASS),
        Classification(
            "32.50.5", "Fabbricazione di altri strumenti e forniture mediche e dentistiche", Category.SUBCLASS
        ),
        Classification(
            "32.50.51", "Fabbricazione di strumenti e apparecchiature mediche e dentistiche", Category.SUBCLASS
        ),
        Classification("32.50.52", "Fabbricazione di forniture mediche e dentistiche", Category.SUBCLASS),
        Classification("32.50.53", "Fabbricazione di mobili per uso medico e dentistico", Category.SUBCLASS),
        Classification("32.9", "Attività manifatturiere n.c.a.", Category.GROUP),
        Classification("32.91", "Fabbricazione di scope e spazzole", Category.CLASS),
        Classification("32.91.0", "Fabbricazione di scope e spazzole", Category.SUBCLASS),
        Classification("32.91.00", "Fabbricazione di scope e spazzole", Category.SUBCLASS),
        Classification("32.99", "Altre attività manifatturiere n.c.a.", Category.CLASS),
        Classification("32.99.1", "Fabbricazione di dispositivi protettivi di sicurezza", Category.SUBCLASS),
        Classification("32.99.10", "Fabbricazione di dispositivi protettivi di sicurezza", Category.SUBCLASS),
        Classification(
            "32.99.2", "Fabbricazione di ombrelli, bottoni, chiusure lampo, parrucche e affini", Category.SUBCLASS
        ),
        Classification(
            "32.99.20", "Fabbricazione di ombrelli, bottoni, chiusure lampo, parrucche e affini", Category.SUBCLASS
        ),
        Classification("32.99.3", "Fabbricazione di articoli di cancelleria", Category.SUBCLASS),
        Classification("32.99.30", "Fabbricazione di articoli di cancelleria", Category.SUBCLASS),
        Classification("32.99.4", "Fabbricazione di casse funebri", Category.SUBCLASS),
        Classification("32.99.40", "Fabbricazione di casse funebri", Category.SUBCLASS),
        Classification("32.99.9", "Fabbricazione di altri articoli n.c.a.", Category.SUBCLASS),
        Classification("32.99.91", "Fabbricazione di sigarette elettroniche", Category.SUBCLASS),
        Classification("32.99.99", "Fabbricazione di altri articoli vari n.c.a.", Category.SUBCLASS),
        Classification(
            "33", "Riparazione, manutenzione e installazione di macchine e apparecchiature", Category.DIVISION
        ),
        Classification(
            "33.1", "Riparazione e manutenzione di prodotti in metallo, macchine e apparecchiature", Category.GROUP
        ),
        Classification("33.11", "Riparazione e manutenzione di prodotti in metallo", Category.CLASS),
        Classification("33.11.0", "Riparazione e manutenzione di prodotti in metallo", Category.SUBCLASS),
        Classification(
            "33.11.01", "Riparazione e manutenzione di cisterne, serbatoi e contenitori in metallo", Category.SUBCLASS
        ),
        Classification(
            "33.11.02", "Riparazione e manutenzione di utensileria ad azionamento manuale", Category.SUBCLASS
        ),
        Classification(
            "33.11.03",
            "Riparazione e manutenzione di stampi, portastampi, sagome, forme per macchine",
            Category.SUBCLASS,
        ),
        Classification(
            "33.11.04",
            "Riparazione e manutenzione di casseforti, cassette di sicurezza, porte metalliche blindate",
            Category.SUBCLASS,
        ),
        Classification(
            "33.11.05",
            "Riparazione e manutenzione di armi da fuoco militari, di ordinanza e artiglieria",
            Category.SUBCLASS,
        ),
        Classification("33.11.06", "Riparazione e manutenzione di armi per uso sportivo e civile", Category.SUBCLASS),
        Classification("33.11.09", "Riparazione e manutenzione di altri prodotti in metallo", Category.SUBCLASS),
        Classification("33.12", "Riparazione e manutenzione di macchinari", Category.CLASS),
        Classification(
            "33.12.1",
            "Riparazione e manutenzione di motori, turbine, pompe, compressori e altri elementi simili",
            Category.SUBCLASS,
        ),
        Classification(
            "33.12.10",
            "Riparazione e manutenzione di motori, turbine, pompe, compressori e altri elementi simili",
            Category.SUBCLASS,
        ),
        Classification("33.12.2", "Riparazione e manutenzione di caldaie per processi industriali", Category.SUBCLASS),
        Classification("33.12.20", "Riparazione e manutenzione di caldaie per processi industriali", Category.SUBCLASS),
        Classification(
            "33.12.3", "Riparazione e manutenzione di apparecchi di sollevamento e movimentazione", Category.SUBCLASS
        ),
        Classification(
            "33.12.30", "Riparazione e manutenzione di apparecchi di sollevamento e movimentazione", Category.SUBCLASS
        ),
        Classification(
            "33.12.4",
            "Riparazione e manutenzione di impianti di refrigerazione industriale e di depurazione dell'aria",
            Category.SUBCLASS,
        ),
        Classification(
            "33.12.40",
            "Riparazione e manutenzione di impianti di refrigerazione industriale e di depurazione dell'aria",
            Category.SUBCLASS,
        ),
        Classification(
            "33.12.5", "Riparazione e manutenzione di altre macchine di impiego generale", Category.SUBCLASS
        ),
        Classification(
            "33.12.51", "Riparazione e manutenzione di macchine e attrezzature per ufficio", Category.SUBCLASS
        ),
        Classification(
            "33.12.52", "Riparazione e manutenzione di bilance e distributori automatici", Category.SUBCLASS
        ),
        Classification(
            "33.12.53",
            "Riparazione e manutenzione di impianti di distillazione o rettificazione per raffinerie di petrolio e industrie chimiche",
            Category.SUBCLASS,
        ),
        Classification(
            "33.12.54", "Riparazione e manutenzione di macchine per impacchettare e imballare", Category.SUBCLASS
        ),
        Classification(
            "33.12.59", "Riparazione e manutenzione di altre macchine di impiego generale n.c.a.", Category.SUBCLASS
        ),
        Classification("33.12.6", "Riparazione e manutenzione di trattori agricoli", Category.SUBCLASS),
        Classification("33.12.60", "Riparazione e manutenzione di trattori agricoli", Category.SUBCLASS),
        Classification(
            "33.12.7",
            "Riparazione e manutenzione di altre macchine per l'agricoltura e la silvicoltura",
            Category.SUBCLASS,
        ),
        Classification(
            "33.12.70",
            "Riparazione e manutenzione di altre macchine per l'agricoltura e la silvicoltura",
            Category.SUBCLASS,
        ),
        Classification(
            "33.12.9", "Riparazione e manutenzione di altre macchine per impieghi speciali", Category.SUBCLASS
        ),
        Classification("33.12.91", "Affilatura di lame e seghe per macchinari", Category.SUBCLASS),
        Classification(
            "33.12.92",
            "Riparazione e manutenzione di giostre, altalene e altre attrazioni di divertimento",
            Category.SUBCLASS,
        ),
        Classification(
            "33.12.99", "Riparazione e manutenzione di altre macchine per impieghi speciali n.c.a.", Category.SUBCLASS
        ),
        Classification("33.13", "Riparazione e manutenzione di apparecchiature elettroniche e ottiche", Category.CLASS),
        Classification(
            "33.13.0", "Riparazione e manutenzione di apparecchiature elettroniche e ottiche", Category.SUBCLASS
        ),
        Classification(
            "33.13.01",
            "Riparazione e manutenzione di apparecchiature per irradiazione, elettromedicali ed elettroterapeutiche",
            Category.SUBCLASS,
        ),
        Classification(
            "33.13.02", "Riparazione e manutenzione di strumenti e apparecchiature ottiche", Category.SUBCLASS
        ),
        Classification(
            "33.13.09", "Riparazione e manutenzione di altre apparecchiature elettroniche e ottiche", Category.SUBCLASS
        ),
        Classification("33.14", "Riparazione e manutenzione di apparecchiature elettriche", Category.CLASS),
        Classification("33.14.0", "Riparazione e manutenzione di apparecchiature elettriche", Category.SUBCLASS),
        Classification("33.14.00", "Riparazione e manutenzione di apparecchiature elettriche", Category.SUBCLASS),
        Classification("33.15", "Riparazione e manutenzione di navi e imbarcazioni per scopi civili", Category.CLASS),
        Classification(
            "33.15.0", "Riparazione e manutenzione di navi e imbarcazioni per scopi civili", Category.SUBCLASS
        ),
        Classification(
            "33.15.00", "Riparazione e manutenzione di navi e imbarcazioni per scopi civili", Category.SUBCLASS
        ),
        Classification(
            "33.16", "Riparazione e manutenzione di aeromobili e veicoli spaziali per scopi civili", Category.CLASS
        ),
        Classification(
            "33.16.0", "Riparazione e manutenzione di aeromobili e veicoli spaziali per scopi civili", Category.SUBCLASS
        ),
        Classification(
            "33.16.00",
            "Riparazione e manutenzione di aeromobili e veicoli spaziali per scopi civili",
            Category.SUBCLASS,
        ),
        Classification(
            "33.17", "Riparazione e manutenzione di altri mezzi di trasporto per scopi civili", Category.CLASS
        ),
        Classification(
            "33.17.0", "Riparazione e manutenzione di altri mezzi di trasporto per scopi civili", Category.SUBCLASS
        ),
        Classification(
            "33.17.00", "Riparazione e manutenzione di altri mezzi di trasporto per scopi civili", Category.SUBCLASS
        ),
        Classification(
            "33.18",
            "Riparazione e manutenzione di veicoli da combattimento, navi, imbarcazioni, aeromobili e veicoli spaziali per scopi militari",
            Category.CLASS,
        ),
        Classification(
            "33.18.1", "Riparazione e manutenzione di veicoli da combattimento per scopi militari", Category.SUBCLASS
        ),
        Classification(
            "33.18.10", "Riparazione e manutenzione di veicoli da combattimento per scopi militari", Category.SUBCLASS
        ),
        Classification(
            "33.18.2", "Riparazione e manutenzione di navi e imbarcazioni per scopi militari", Category.SUBCLASS
        ),
        Classification(
            "33.18.20", "Riparazione e manutenzione di navi e imbarcazioni per scopi militari", Category.SUBCLASS
        ),
        Classification(
            "33.18.3",
            "Riparazione e manutenzione di aeromobili e veicoli spaziali per scopi militari",
            Category.SUBCLASS,
        ),
        Classification(
            "33.18.30",
            "Riparazione e manutenzione di aeromobili e veicoli spaziali per scopi militari",
            Category.SUBCLASS,
        ),
        Classification("33.19", "Riparazione e manutenzione di altre apparecchiature", Category.CLASS),
        Classification("33.19.0", "Riparazione e manutenzione di altre apparecchiature", Category.SUBCLASS),
        Classification("33.19.00", "Riparazione e manutenzione di altre apparecchiature", Category.SUBCLASS),
        Classification("33.2", "Installazione di macchine e apparecchiature industriali", Category.GROUP),
        Classification("33.20", "Installazione di macchine e apparecchiature industriali", Category.CLASS),
        Classification("33.20.0", "Installazione di macchine e apparecchiature industriali", Category.SUBCLASS),
        Classification(
            "33.20.01",
            "Installazione di motori, generatori e trasformatori elettrici e di apparecchiature per la distribuzione e il controllo della elettricità",
            Category.SUBCLASS,
        ),
        Classification(
            "33.20.02",
            "Installazione di apparecchiature per le comunicazioni e di apparecchiature radiotelevisive",
            Category.SUBCLASS,
        ),
        Classification(
            "33.20.03", "Installazione di strumenti e apparecchi di misurazione e controllo", Category.SUBCLASS
        ),
        Classification("33.20.04", "Installazione di cisterne, serbatoi e contenitori in metallo", Category.SUBCLASS),
        Classification("33.20.05", "Installazione di generatori di vapore", Category.SUBCLASS),
        Classification("33.20.06", "Installazione di macchinari e attrezzature per ufficio", Category.SUBCLASS),
        Classification(
            "33.20.07", "Installazione di strumenti e apparecchiature mediche e dentistiche", Category.SUBCLASS
        ),
        Classification("33.20.09", "Installazione di altre macchine e apparecchiature industriali", Category.SUBCLASS),
        Classification("D", "FORNITURA DI ENERGIA ELETTRICA, GAS, VAPORE E ARIA CONDIZIONATA", Category.SECTION),
        Classification("35", "Fornitura di energia elettrica, gas, vapore e aria condizionata", Category.DIVISION),
        Classification("35.1", "Produzione, trasmissione e distribuzione di energia elettrica", Category.GROUP),
        Classification("35.11", "Produzione di energia elettrica da fonti non rinnovabili", Category.CLASS),
        Classification("35.11.0", "Produzione di energia elettrica da fonti non rinnovabili", Category.SUBCLASS),
        Classification("35.11.00", "Produzione di energia elettrica da fonti non rinnovabili", Category.SUBCLASS),
        Classification("35.12", "Produzione di energia elettrica da fonti rinnovabili", Category.CLASS),
        Classification("35.12.0", "Produzione di energia elettrica da fonti rinnovabili", Category.SUBCLASS),
        Classification("35.12.00", "Produzione di energia elettrica da fonti rinnovabili", Category.SUBCLASS),
        Classification("35.13", "Trasmissione di energia elettrica", Category.CLASS),
        Classification("35.13.0", "Trasmissione di energia elettrica", Category.SUBCLASS),
        Classification("35.13.00", "Trasmissione di energia elettrica", Category.SUBCLASS),
        Classification("35.14", "Distribuzione di energia elettrica", Category.CLASS),
        Classification("35.14.0", "Distribuzione di energia elettrica", Category.SUBCLASS),
        Classification("35.14.00", "Distribuzione di energia elettrica", Category.SUBCLASS),
        Classification("35.15", "Commercio di energia elettrica", Category.CLASS),
        Classification("35.15.0", "Commercio di energia elettrica", Category.SUBCLASS),
        Classification("35.15.00", "Commercio di energia elettrica", Category.SUBCLASS),
        Classification("35.16", "Stoccaggio di energia elettrica", Category.CLASS),
        Classification("35.16.0", "Stoccaggio di energia elettrica", Category.SUBCLASS),
        Classification("35.16.00", "Stoccaggio di energia elettrica", Category.SUBCLASS),
        Classification(
            "35.2", "Produzione di gas e distribuzione di combustibili gassosi mediante condotte", Category.GROUP
        ),
        Classification("35.21", "Produzione di gas", Category.CLASS),
        Classification("35.21.0", "Produzione di gas", Category.SUBCLASS),
        Classification("35.21.00", "Produzione di gas", Category.SUBCLASS),
        Classification("35.22", "Distribuzione di combustibili gassosi mediante condotte", Category.CLASS),
        Classification("35.22.0", "Distribuzione di combustibili gassosi mediante condotte", Category.SUBCLASS),
        Classification("35.22.00", "Distribuzione di combustibili gassosi mediante condotte", Category.SUBCLASS),
        Classification("35.23", "Commercio di gas distribuito mediante condotte", Category.CLASS),
        Classification("35.23.0", "Commercio di gas distribuito mediante condotte", Category.SUBCLASS),
        Classification("35.23.00", "Commercio di gas distribuito mediante condotte", Category.SUBCLASS),
        Classification("35.24", "Stoccaggio di gas nell'ambito dei servizi di fornitura della rete", Category.CLASS),
        Classification(
            "35.24.0", "Stoccaggio di gas nell'ambito dei servizi di fornitura della rete", Category.SUBCLASS
        ),
        Classification(
            "35.24.00", "Stoccaggio di gas nell'ambito dei servizi di fornitura della rete", Category.SUBCLASS
        ),
        Classification("35.3", "Fornitura di vapore e aria condizionata", Category.GROUP),
        Classification("35.30", "Fornitura di vapore e aria condizionata", Category.CLASS),
        Classification("35.30.0", "Fornitura di vapore e aria condizionata", Category.SUBCLASS),
        Classification("35.30.00", "Fornitura di vapore e aria condizionata", Category.SUBCLASS),
        Classification(
            "35.4", "Attività di servizi di intermediazione per l'energia elettrica e il gas naturale", Category.GROUP
        ),
        Classification(
            "35.40", "Attività di servizi di intermediazione per l'energia elettrica e il gas naturale", Category.CLASS
        ),
        Classification(
            "35.40.0",
            "Attività di servizi di intermediazione per l'energia elettrica e il gas naturale",
            Category.SUBCLASS,
        ),
        Classification(
            "35.40.00",
            "Attività di servizi di intermediazione per l'energia elettrica e il gas naturale",
            Category.SUBCLASS,
        ),
        Classification(
            "E",
            "FORNITURA DI ACQUA; GESTIONE DI RETI FOGNARIE, ATTIVITÀ DI TRATTAMENTO DEI RIFIUTI E RISANAMENTO",
            Category.SECTION,
        ),
        Classification("36", "Raccolta, trattamento e fornitura di acqua", Category.DIVISION),
        Classification("36.0", "Raccolta, trattamento e fornitura di acqua", Category.GROUP),
        Classification("36.00", "Raccolta, trattamento e fornitura di acqua", Category.CLASS),
        Classification("36.00.0", "Raccolta, trattamento e fornitura di acqua", Category.SUBCLASS),
        Classification("36.00.00", "Raccolta, trattamento e fornitura di acqua", Category.SUBCLASS),
        Classification("37", "Gestione delle reti fognarie", Category.DIVISION),
        Classification("37.0", "Gestione delle reti fognarie", Category.GROUP),
        Classification("37.00", "Gestione delle reti fognarie", Category.CLASS),
        Classification("37.00.0", "Gestione delle reti fognarie", Category.SUBCLASS),
        Classification("37.00.00", "Gestione delle reti fognarie", Category.SUBCLASS),
        Classification("38", "Attività di raccolta, recupero e smaltimento dei rifiuti", Category.DIVISION),
        Classification("38.1", "Raccolta dei rifiuti", Category.GROUP),
        Classification("38.11", "Raccolta di rifiuti non pericolosi", Category.CLASS),
        Classification("38.11.0", "Raccolta di rifiuti non pericolosi", Category.SUBCLASS),
        Classification("38.11.00", "Raccolta di rifiuti non pericolosi", Category.SUBCLASS),
        Classification("38.12", "Raccolta di rifiuti pericolosi", Category.CLASS),
        Classification("38.12.0", "Raccolta di rifiuti pericolosi", Category.SUBCLASS),
        Classification("38.12.00", "Raccolta di rifiuti pericolosi", Category.SUBCLASS),
        Classification("38.2", "Recupero dei rifiuti", Category.GROUP),
        Classification("38.21", "Recupero dei materiali", Category.CLASS),
        Classification("38.21.1", "Smantellamento di carcasse", Category.SUBCLASS),
        Classification(
            "38.21.11", "Smantellamento di carcasse di navi per il recupero dei materiali", Category.SUBCLASS
        ),
        Classification("38.21.12", "Smantellamento di altre carcasse", Category.SUBCLASS),
        Classification("38.21.2", "Recupero dei materiali da rifiuti metallici", Category.SUBCLASS),
        Classification("38.21.20", "Recupero dei materiali da rifiuti metallici", Category.SUBCLASS),
        Classification("38.21.3", "Recupero dei materiali da rifiuti plastici", Category.SUBCLASS),
        Classification("38.21.30", "Recupero dei materiali da rifiuti plastici", Category.SUBCLASS),
        Classification("38.21.4", "Recupero dei materiali da altri rifiuti", Category.SUBCLASS),
        Classification("38.21.40", "Recupero dei materiali da altri rifiuti", Category.SUBCLASS),
        Classification("38.22", "Recupero di energia", Category.CLASS),
        Classification("38.22.0", "Recupero di energia", Category.SUBCLASS),
        Classification("38.22.00", "Recupero di energia", Category.SUBCLASS),
        Classification("38.23", "Altre attività di recupero dei rifiuti", Category.CLASS),
        Classification("38.23.0", "Altre attività di recupero dei rifiuti", Category.SUBCLASS),
        Classification("38.23.00", "Altre attività di recupero dei rifiuti", Category.SUBCLASS),
        Classification("38.3", "Smaltimento dei rifiuti senza recupero", Category.GROUP),
        Classification("38.31", "Incenerimento senza recupero di energia", Category.CLASS),
        Classification("38.31.0", "Incenerimento senza recupero di energia", Category.SUBCLASS),
        Classification("38.31.00", "Incenerimento senza recupero di energia", Category.SUBCLASS),
        Classification("38.32", "Conferimento in discarica o stoccaggio permanente", Category.CLASS),
        Classification("38.32.0", "Conferimento in discarica o stoccaggio permanente", Category.SUBCLASS),
        Classification("38.32.00", "Conferimento in discarica o stoccaggio permanente", Category.SUBCLASS),
        Classification("38.33", "Altre attività di smaltimento dei rifiuti", Category.CLASS),
        Classification("38.33.0", "Altre attività di smaltimento dei rifiuti", Category.SUBCLASS),
        Classification("38.33.00", "Altre attività di smaltimento dei rifiuti", Category.SUBCLASS),
        Classification("39", "Attività di risanamento e altri servizi di gestione dei rifiuti", Category.DIVISION),
        Classification("39.0", "Attività di risanamento e altri servizi di gestione dei rifiuti", Category.GROUP),
        Classification("39.00", "Attività di risanamento e altri servizi di gestione dei rifiuti", Category.CLASS),
        Classification("39.00.0", "Attività di risanamento e altri servizi di gestione dei rifiuti", Category.SUBCLASS),
        Classification(
            "39.00.01",
            "Attività di rimozione di amianto, vernici a base di piombo e altri materiali tossici",
            Category.SUBCLASS,
        ),
        Classification(
            "39.00.09", "Attività di risanamento e altri servizi di gestione dei rifiuti n.c.a.", Category.SUBCLASS
        ),
        Classification("F", "COSTRUZIONI", Category.SECTION),
        Classification("41", "Costruzione di edifici residenziali e non residenziali", Category.DIVISION),
        Classification("41.0", "Costruzione di edifici residenziali e non residenziali", Category.GROUP),
        Classification("41.00", "Costruzione di edifici residenziali e non residenziali", Category.CLASS),
        Classification("41.00.0", "Costruzione di edifici residenziali e non residenziali", Category.SUBCLASS),
        Classification("41.00.00", "Costruzione di edifici residenziali e non residenziali", Category.SUBCLASS),
        Classification("42", "Ingegneria civile", Category.DIVISION),
        Classification("42.1", "Costruzione di strade e linee ferroviarie", Category.GROUP),
        Classification("42.11", "Costruzione di strade e autostrade", Category.CLASS),
        Classification("42.11.0", "Costruzione di strade e autostrade", Category.SUBCLASS),
        Classification("42.11.00", "Costruzione di strade e autostrade", Category.SUBCLASS),
        Classification("42.12", "Costruzione di linee ferroviarie e metropolitane", Category.CLASS),
        Classification("42.12.0", "Costruzione di linee ferroviarie e metropolitane", Category.SUBCLASS),
        Classification("42.12.00", "Costruzione di linee ferroviarie e metropolitane", Category.SUBCLASS),
        Classification("42.13", "Costruzione di ponti e gallerie", Category.CLASS),
        Classification("42.13.0", "Costruzione di ponti e gallerie", Category.SUBCLASS),
        Classification("42.13.00", "Costruzione di ponti e gallerie", Category.SUBCLASS),
        Classification("42.2", "Costruzione di opere di pubblica utilità", Category.GROUP),
        Classification("42.21", "Costruzione di opere di pubblica utilità per il trasporto dei fluidi", Category.CLASS),
        Classification(
            "42.21.0", "Costruzione di opere di pubblica utilità per il trasporto dei fluidi", Category.SUBCLASS
        ),
        Classification(
            "42.21.00", "Costruzione di opere di pubblica utilità per il trasporto dei fluidi", Category.SUBCLASS
        ),
        Classification(
            "42.22",
            "Costruzione di opere di pubblica utilità per l'energia elettrica e le telecomunicazioni",
            Category.CLASS,
        ),
        Classification(
            "42.22.0",
            "Costruzione di opere di pubblica utilità per l'energia elettrica e le telecomunicazioni",
            Category.SUBCLASS,
        ),
        Classification(
            "42.22.00",
            "Costruzione di opere di pubblica utilità per l'energia elettrica e le telecomunicazioni",
            Category.SUBCLASS,
        ),
        Classification("42.9", "Costruzione di altre opere di ingegneria civile", Category.GROUP),
        Classification("42.91", "Costruzione di opere idrauliche", Category.CLASS),
        Classification("42.91.0", "Costruzione di opere idrauliche", Category.SUBCLASS),
        Classification("42.91.00", "Costruzione di opere idrauliche", Category.SUBCLASS),
        Classification("42.99", "Costruzione di altre opere di ingegneria civile n.c.a.", Category.CLASS),
        Classification("42.99.0", "Costruzione di altre opere di ingegneria civile n.c.a.", Category.SUBCLASS),
        Classification("42.99.00", "Costruzione di altre opere di ingegneria civile n.c.a.", Category.SUBCLASS),
        Classification("43", "Lavori di costruzione specializzati", Category.DIVISION),
        Classification("43.1", "Demolizione e preparazione del cantiere edile", Category.GROUP),
        Classification("43.11", "Demolizione", Category.CLASS),
        Classification("43.11.0", "Demolizione", Category.SUBCLASS),
        Classification("43.11.00", "Demolizione", Category.SUBCLASS),
        Classification("43.12", "Preparazione del cantiere edile", Category.CLASS),
        Classification("43.12.0", "Preparazione del cantiere edile", Category.SUBCLASS),
        Classification("43.12.01", "Preparazione del sito per scavi archeologici", Category.SUBCLASS),
        Classification("43.12.09", "Altre attività di preparazione del cantiere edile", Category.SUBCLASS),
        Classification("43.13", "Trivellazioni e perforazioni", Category.CLASS),
        Classification("43.13.0", "Trivellazioni e perforazioni", Category.SUBCLASS),
        Classification("43.13.00", "Trivellazioni e perforazioni", Category.SUBCLASS),
        Classification(
            "43.2",
            "Installazione di impianti elettrici, idraulici e altri lavori di installazione edili",
            Category.GROUP,
        ),
        Classification("43.21", "Installazione di impianti elettrici", Category.CLASS),
        Classification("43.21.0", "Installazione di impianti elettrici", Category.SUBCLASS),
        Classification(
            "43.21.01", "Installazione di impianti di illuminazione e fotovoltaici in edifici", Category.SUBCLASS
        ),
        Classification("43.21.02", "Installazione di cablaggi per telecomunicazioni e altre reti", Category.SUBCLASS),
        Classification(
            "43.21.03", "Installazione di impianti di illuminazione stradale e di piste aeroportuali", Category.SUBCLASS
        ),
        Classification("43.21.04", "Installazione di insegne elettriche e luminarie per feste", Category.SUBCLASS),
        Classification(
            "43.21.05", "Installazione di impianti di illuminazione elettrica votiva e cimiteriale", Category.SUBCLASS
        ),
        Classification(
            "43.22",
            "Installazione di impianti idraulici, di riscaldamento e di condizionamento dell'aria",
            Category.CLASS,
        ),
        Classification(
            "43.22.0",
            "Installazione di impianti idraulici, di riscaldamento e di condizionamento dell'aria",
            Category.SUBCLASS,
        ),
        Classification("43.22.01", "Installazione di impianti geotermici", Category.SUBCLASS),
        Classification("43.22.02", "Installazione di impianti di depurazione per piscine", Category.SUBCLASS),
        Classification("43.22.03", "Installazione di impianti di spegnimento di incendi", Category.SUBCLASS),
        Classification("43.22.04", "Installazione di impianti di irrigazione per giardini", Category.SUBCLASS),
        Classification("43.22.05", "Installazione di altri impianti termo-idraulici", Category.SUBCLASS),
        Classification("43.22.06", "Installazione di impianti per la distribuzione del gas", Category.SUBCLASS),
        Classification(
            "43.22.07", "Installazione di impianti di riscaldamento e di condizionamento dell'aria", Category.SUBCLASS
        ),
        Classification("43.23", "Installazione di sistemi per l'isolamento", Category.CLASS),
        Classification("43.23.0", "Installazione di sistemi per l'isolamento", Category.SUBCLASS),
        Classification("43.23.00", "Installazione di sistemi per l'isolamento", Category.SUBCLASS),
        Classification("43.24", "Altri lavori di installazione edili", Category.CLASS),
        Classification("43.24.0", "Altri lavori di installazione edili", Category.SUBCLASS),
        Classification("43.24.01", "Installazione di ascensori e scale mobili", Category.SUBCLASS),
        Classification("43.24.02", "Installazione di insegne non elettriche", Category.SUBCLASS),
        Classification("43.24.09", "Altri lavori di installazione edili n.c.a.", Category.SUBCLASS),
        Classification("43.3", "Completamento e finitura di edifici", Category.GROUP),
        Classification("43.31", "Intonacatura", Category.CLASS),
        Classification("43.31.0", "Intonacatura", Category.SUBCLASS),
        Classification("43.31.01", "Posa in opera di cartongesso", Category.SUBCLASS),
        Classification("43.31.02", "Altri lavori di intonacatura", Category.SUBCLASS),
        Classification("43.32", "Posa in opera di infissi", Category.CLASS),
        Classification("43.32.0", "Posa in opera di infissi", Category.SUBCLASS),
        Classification("43.32.01", "Posa in opera di porte blindate", Category.SUBCLASS),
        Classification(
            "43.32.02",
            "Posa in opera di porte non blindate, finestre, arredi, controsoffitti, pareti mobili e simili",
            Category.SUBCLASS,
        ),
        Classification("43.33", "Rivestimento di pavimenti e di pareti", Category.CLASS),
        Classification("43.33.0", "Rivestimento di pavimenti e di pareti", Category.SUBCLASS),
        Classification("43.33.00", "Rivestimento di pavimenti e di pareti", Category.SUBCLASS),
        Classification("43.34", "Tinteggiatura e posa in opera di vetri", Category.CLASS),
        Classification("43.34.0", "Tinteggiatura e posa in opera di vetri", Category.SUBCLASS),
        Classification("43.34.01", "Tinteggiatura", Category.SUBCLASS),
        Classification("43.34.02", "Posa in opera di vetri", Category.SUBCLASS),
        Classification("43.35", "Altri lavori di completamento e finitura degli edifici", Category.CLASS),
        Classification("43.35.0", "Altri lavori di completamento e finitura degli edifici", Category.SUBCLASS),
        Classification("43.35.00", "Altri lavori di completamento e finitura degli edifici", Category.SUBCLASS),
        Classification("43.4", "Lavori di costruzione specializzati nella costruzione di edifici", Category.GROUP),
        Classification("43.41", "Realizzazione di coperture", Category.CLASS),
        Classification("43.41.0", "Realizzazione di coperture", Category.SUBCLASS),
        Classification("43.41.00", "Realizzazione di coperture", Category.SUBCLASS),
        Classification(
            "43.42", "Altri lavori di costruzione specializzati nella costruzione di edifici", Category.CLASS
        ),
        Classification(
            "43.42.0", "Altri lavori di costruzione specializzati nella costruzione di edifici", Category.SUBCLASS
        ),
        Classification(
            "43.42.00", "Altri lavori di costruzione specializzati nella costruzione di edifici", Category.SUBCLASS
        ),
        Classification("43.5", "Lavori di costruzione specializzati nell'ingegneria civile", Category.GROUP),
        Classification("43.50", "Lavori di costruzione specializzati nell'ingegneria civile", Category.CLASS),
        Classification("43.50.0", "Lavori di costruzione specializzati nell'ingegneria civile", Category.SUBCLASS),
        Classification("43.50.00", "Lavori di costruzione specializzati nell'ingegneria civile", Category.SUBCLASS),
        Classification(
            "43.6", "Attività di servizi di intermediazione per servizi di costruzione specializzati", Category.GROUP
        ),
        Classification(
            "43.60", "Attività di servizi di intermediazione per servizi di costruzione specializzati", Category.CLASS
        ),
        Classification(
            "43.60.0",
            "Attività di servizi di intermediazione per servizi di costruzione specializzati",
            Category.SUBCLASS,
        ),
        Classification(
            "43.60.00",
            "Attività di servizi di intermediazione per servizi di costruzione specializzati",
            Category.SUBCLASS,
        ),
        Classification("43.9", "Altri lavori di costruzione specializzati", Category.GROUP),
        Classification("43.91", "Lavori di muratura", Category.CLASS),
        Classification("43.91.0", "Lavori di muratura", Category.SUBCLASS),
        Classification("43.91.00", "Lavori di muratura", Category.SUBCLASS),
        Classification("43.99", "Altri lavori di costruzione specializzati n.c.a.", Category.CLASS),
        Classification("43.99.0", "Altri lavori di costruzione specializzati n.c.a.", Category.SUBCLASS),
        Classification("43.99.01", "Noleggio di gru e altre attrezzature edili con operatore", Category.SUBCLASS),
        Classification("43.99.02", "Interventi su siti ed edifici storici e archeologici", Category.SUBCLASS),
        Classification("43.99.09", "Altri lavori vari di costruzione specializzati n.c.a.", Category.SUBCLASS),
        Classification("G", "COMMERCIO ALL'INGROSSO E AL DETTAGLIO", Category.SECTION),
        Classification("46", "Commercio all'ingrosso", Category.DIVISION),
        Classification("46.1", "Attività di servizi di intermediazione per il commercio all'ingrosso", Category.GROUP),
        Classification(
            "46.11",
            "Attività di intermediari del commercio all'ingrosso di materie prime agricole, animali vivi, materie prime tessili e semilavorati",
            Category.CLASS,
        ),
        Classification(
            "46.11.0",
            "Attività di intermediari del commercio all'ingrosso di materie prime agricole, animali vivi, materie prime tessili e semilavorati",
            Category.SUBCLASS,
        ),
        Classification(
            "46.11.01",
            "Attività di intermediari del commercio all'ingrosso di materie prime agricole",
            Category.SUBCLASS,
        ),
        Classification(
            "46.11.02", "Attività di intermediari del commercio all'ingrosso di fiori e piante", Category.SUBCLASS
        ),
        Classification(
            "46.11.03", "Attività di intermediari del commercio all'ingrosso di animali vivi", Category.SUBCLASS
        ),
        Classification(
            "46.11.04",
            "Attività di intermediari del commercio all'ingrosso di materie prime tessili e semilavorati",
            Category.SUBCLASS,
        ),
        Classification(
            "46.12",
            "Attività di intermediari del commercio all'ingrosso di combustibili, minerali, metalli e prodotti chimici per l'industria",
            Category.CLASS,
        ),
        Classification(
            "46.12.0",
            "Attività di intermediari del commercio all'ingrosso di combustibili, minerali, metalli e prodotti chimici per l'industria",
            Category.SUBCLASS,
        ),
        Classification(
            "46.12.01",
            "Attività di intermediari del commercio all'ingrosso di combustibili liquidi e gassosi",
            Category.SUBCLASS,
        ),
        Classification(
            "46.12.02", "Attività di intermediari del commercio all'ingrosso di combustibili solidi", Category.SUBCLASS
        ),
        Classification(
            "46.12.03", "Attività di intermediari del commercio all'ingrosso di minerali e metalli", Category.SUBCLASS
        ),
        Classification(
            "46.12.04",
            "Attività di intermediari del commercio all'ingrosso di fertilizzanti e altri prodotti chimici per l'agricoltura",
            Category.SUBCLASS,
        ),
        Classification(
            "46.12.05",
            "Attività di intermediari del commercio all'ingrosso di prodotti chimici per l'industria",
            Category.SUBCLASS,
        ),
        Classification(
            "46.13",
            "Attività di intermediari del commercio all'ingrosso di legname e materiali da costruzione",
            Category.CLASS,
        ),
        Classification(
            "46.13.0",
            "Attività di intermediari del commercio all'ingrosso di legname e materiali da costruzione",
            Category.SUBCLASS,
        ),
        Classification("46.13.01", "Attività di intermediari del commercio all'ingrosso di legname", Category.SUBCLASS),
        Classification(
            "46.13.02",
            "Attività di intermediari del commercio all'ingrosso di pitture, vernici e lacche",
            Category.SUBCLASS,
        ),
        Classification(
            "46.13.03",
            "Attività di intermediari del commercio all'ingrosso di altri materiali da costruzione",
            Category.SUBCLASS,
        ),
        Classification(
            "46.14",
            "Attività di intermediari del commercio all'ingrosso di macchine e attrezzature industriali, navi e aeromobili",
            Category.CLASS,
        ),
        Classification(
            "46.14.0",
            "Attività di intermediari del commercio all'ingrosso di macchine e attrezzature industriali, navi e aeromobili",
            Category.SUBCLASS,
        ),
        Classification(
            "46.14.01",
            "Attività di intermediari del commercio all'ingrosso di macchine e attrezzature per l'industria e il commercio",
            Category.SUBCLASS,
        ),
        Classification(
            "46.14.02",
            "Attività di intermediari del commercio all'ingrosso di macchine e attrezzature per l'edilizia",
            Category.SUBCLASS,
        ),
        Classification(
            "46.14.03",
            "Attività di intermediari del commercio all'ingrosso di macchine per ufficio, computer e apparecchiature per le comunicazioni",
            Category.SUBCLASS,
        ),
        Classification(
            "46.14.04",
            "Attività di intermediari del commercio all'ingrosso di attrezzature agricole",
            Category.SUBCLASS,
        ),
        Classification(
            "46.14.05", "Attività di intermediari del commercio all'ingrosso di navi e aeromobili", Category.SUBCLASS
        ),
        Classification(
            "46.15",
            "Attività di intermediari del commercio all'ingrosso di mobili, articoli per la casa e ferramenta",
            Category.CLASS,
        ),
        Classification(
            "46.15.0",
            "Attività di intermediari del commercio all'ingrosso di mobili, articoli per la casa e ferramenta",
            Category.SUBCLASS,
        ),
        Classification(
            "46.15.01",
            "Attività di intermediari del commercio all'ingrosso di mobili in legno, metallo e materie plastiche",
            Category.SUBCLASS,
        ),
        Classification(
            "46.15.02",
            "Attività di intermediari del commercio all'ingrosso di altri mobili e oggetti di arredamento per la casa",
            Category.SUBCLASS,
        ),
        Classification(
            "46.15.03",
            "Attività di intermediari del commercio all'ingrosso di apparecchiature di riscaldamento, ventilazione e condizionamento domestico",
            Category.SUBCLASS,
        ),
        Classification(
            "46.15.04",
            "Attività di intermediari del commercio all'ingrosso di altri articoli per la casa",
            Category.SUBCLASS,
        ),
        Classification(
            "46.15.05", "Attività di intermediari del commercio all'ingrosso di ferramenta", Category.SUBCLASS
        ),
        Classification(
            "46.16",
            "Attività di intermediari del commercio all'ingrosso di prodotti tessili, abbigliamento, pellicce, calzature e articoli in pelle",
            Category.CLASS,
        ),
        Classification(
            "46.16.0",
            "Attività di intermediari del commercio all'ingrosso di prodotti tessili, abbigliamento, pellicce, calzature e articoli in pelle",
            Category.SUBCLASS,
        ),
        Classification(
            "46.16.01",
            "Attività di intermediari del commercio all'ingrosso di tessuti per l'abbigliamento e l'arredamento",
            Category.SUBCLASS,
        ),
        Classification(
            "46.16.02",
            "Attività di intermediari del commercio all'ingrosso di prodotti tessili per la casa e tappeti",
            Category.SUBCLASS,
        ),
        Classification(
            "46.16.03",
            "Attività di intermediari del commercio all'ingrosso di camicie, biancheria intima e articoli simili",
            Category.SUBCLASS,
        ),
        Classification(
            "46.16.04",
            "Attività di intermediari del commercio all'ingrosso di altri articoli di abbigliamento e accessori per l'abbigliamento",
            Category.SUBCLASS,
        ),
        Classification(
            "46.16.05", "Attività di intermediari del commercio all'ingrosso di pellicce", Category.SUBCLASS
        ),
        Classification(
            "46.16.06", "Attività di intermediari del commercio all'ingrosso di calzature", Category.SUBCLASS
        ),
        Classification(
            "46.16.07",
            "Attività di intermediari del commercio all'ingrosso di articoli in pelle e articoli da viaggio",
            Category.SUBCLASS,
        ),
        Classification(
            "46.17",
            "Attività di intermediari del commercio all'ingrosso di prodotti alimentari, bevande e tabacchi",
            Category.CLASS,
        ),
        Classification(
            "46.17.0",
            "Attività di intermediari del commercio all'ingrosso di prodotti alimentari, bevande e tabacchi",
            Category.SUBCLASS,
        ),
        Classification(
            "46.17.01", "Attività di intermediari del commercio all'ingrosso di frutta e ortaggi", Category.SUBCLASS
        ),
        Classification(
            "46.17.02",
            "Attività di intermediari del commercio all'ingrosso di carne e prodotti a base di carne",
            Category.SUBCLASS,
        ),
        Classification(
            "46.17.03",
            "Attività di intermediari del commercio all'ingrosso di pesce e prodotti a base di pesce",
            Category.SUBCLASS,
        ),
        Classification(
            "46.17.04",
            "Attività di intermediari del commercio all'ingrosso di latte e prodotti lattiero-caseari",
            Category.SUBCLASS,
        ),
        Classification(
            "46.17.05",
            "Attività di intermediari del commercio all'ingrosso di oli e grassi alimentari",
            Category.SUBCLASS,
        ),
        Classification("46.17.06", "Attività di intermediari del commercio all'ingrosso di bevande", Category.SUBCLASS),
        Classification(
            "46.17.07",
            "Attività di intermediari del commercio all'ingrosso di altri prodotti alimentari e tabacchi",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18", "Attività di intermediari del commercio all'ingrosso di altri prodotti specifici", Category.CLASS
        ),
        Classification(
            "46.18.1",
            "Attività di intermediari del commercio all'ingrosso di prodotti farmaceutici e articoli medicali, profumi e articoli di profumeria e prodotti per la pulizia",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.11",
            "Attività di intermediari del commercio all'ingrosso di prodotti farmaceutici",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.12", "Attività di intermediari del commercio all'ingrosso di articoli medicali", Category.SUBCLASS
        ),
        Classification(
            "46.18.13",
            "Attività di intermediari del commercio all'ingrosso di profumi e articoli di profumeria",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.14",
            "Attività di intermediari del commercio all'ingrosso di prodotti per la pulizia",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.2",
            "Attività di intermediari del commercio all'ingrosso di giochi e giocattoli, attrezzature sportive, orologi e gioielli, apparecchiature fotografiche e strumenti ottici",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.21", "Attività di intermediari del commercio all'ingrosso di giochi e giocattoli", Category.SUBCLASS
        ),
        Classification(
            "46.18.22", "Attività di intermediari del commercio all'ingrosso di biciclette", Category.SUBCLASS
        ),
        Classification(
            "46.18.23",
            "Attività di intermediari del commercio all'ingrosso di altre attrezzature sportive",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.24", "Attività di intermediari del commercio all'ingrosso di orologi e gioielli", Category.SUBCLASS
        ),
        Classification(
            "46.18.25",
            "Attività di intermediari del commercio all'ingrosso di oggetti di bigiotteria",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.26",
            "Attività di intermediari del commercio all'ingrosso di apparecchiature fotografiche e strumenti ottici",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.3",
            "Attività di intermediari del commercio all'ingrosso di libri, giornali, riviste e articoli di cancelleria",
            Category.SUBCLASS,
        ),
        Classification("46.18.31", "Attività di intermediari del commercio all'ingrosso di libri", Category.SUBCLASS),
        Classification(
            "46.18.32", "Attività di intermediari del commercio all'ingrosso di giornali e riviste", Category.SUBCLASS
        ),
        Classification(
            "46.18.33",
            "Attività di intermediari del commercio all'ingrosso di articoli di cancelleria",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.4",
            "Attività di intermediari del commercio all'ingrosso di automobili, altri autoveicoli e motocicli",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.41",
            "Attività di intermediari del commercio all'ingrosso di automobili e autoveicoli leggeri",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.42", "Attività di intermediari del commercio all'ingrosso di altri autoveicoli", Category.SUBCLASS
        ),
        Classification(
            "46.18.43",
            "Attività di intermediari del commercio all'ingrosso di parti e accessori di autoveicoli",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.44", "Attività di intermediari del commercio all'ingrosso di motocicli", Category.SUBCLASS
        ),
        Classification(
            "46.18.45",
            "Attività di intermediari del commercio all'ingrosso di parti e accessori di motocicli",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.46",
            "Attività di intermediari del commercio all'ingrosso di materiale rotabile e di parti e accessori per materiale rotabile",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.5",
            "Attività di intermediari del commercio all'ingrosso di apparecchiature audio e video",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.50",
            "Attività di intermediari del commercio all'ingrosso di apparecchiature audio e video",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.9",
            "Attività di intermediari del commercio all'ingrosso di altri prodotti specifici n.c.a.",
            Category.SUBCLASS,
        ),
        Classification("46.18.91", "Attività di intermediari del commercio all'ingrosso di rifiuti", Category.SUBCLASS),
        Classification(
            "46.18.92",
            "Attività di intermediari del commercio all'ingrosso di rivestimenti per pareti e per pavimenti",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18.93", "Attività di intermediari del commercio all'ingrosso di strumenti musicali", Category.SUBCLASS
        ),
        Classification(
            "46.18.99",
            "Attività di intermediari del commercio all'ingrosso di altri prodotti specifici vari n.c.a.",
            Category.SUBCLASS,
        ),
        Classification(
            "46.19", "Attività di intermediari del commercio all'ingrosso non specializzato", Category.CLASS
        ),
        Classification(
            "46.19.0", "Attività di intermediari del commercio all'ingrosso non specializzato", Category.SUBCLASS
        ),
        Classification(
            "46.19.00", "Attività di intermediari del commercio all'ingrosso non specializzato", Category.SUBCLASS
        ),
        Classification("46.2", "Commercio all'ingrosso di materie prime agricole e animali vivi", Category.GROUP),
        Classification(
            "46.21",
            "Commercio all'ingrosso di cereali, tabacco grezzo, sementi e alimenti per il bestiame",
            Category.CLASS,
        ),
        Classification("46.21.1", "Commercio all'ingrosso di cereali", Category.SUBCLASS),
        Classification("46.21.10", "Commercio all'ingrosso di cereali", Category.SUBCLASS),
        Classification(
            "46.21.2", "Commercio all'ingrosso di tabacco grezzo, sementi e alimenti per il bestiame", Category.SUBCLASS
        ),
        Classification("46.21.21", "Commercio all'ingrosso di tabacco grezzo", Category.SUBCLASS),
        Classification("46.21.22", "Commercio all'ingrosso di sementi e alimenti per il bestiame", Category.SUBCLASS),
        Classification("46.22", "Commercio all'ingrosso di fiori e piante", Category.CLASS),
        Classification("46.22.0", "Commercio all'ingrosso di fiori e piante", Category.SUBCLASS),
        Classification("46.22.00", "Commercio all'ingrosso di fiori e piante", Category.SUBCLASS),
        Classification("46.23", "Commercio all'ingrosso di animali vivi", Category.CLASS),
        Classification("46.23.0", "Commercio all'ingrosso di animali vivi", Category.SUBCLASS),
        Classification("46.23.00", "Commercio all'ingrosso di animali vivi", Category.SUBCLASS),
        Classification("46.24", "Commercio all'ingrosso di pelli e cuoio", Category.CLASS),
        Classification("46.24.0", "Commercio all'ingrosso di pelli e cuoio", Category.SUBCLASS),
        Classification("46.24.01", "Commercio all'ingrosso di pelli per pellicceria", Category.SUBCLASS),
        Classification("46.24.02", "Commercio all'ingrosso di pelli non per pellicceria e cuoio", Category.SUBCLASS),
        Classification("46.3", "Commercio all'ingrosso di prodotti alimentari, bevande e tabacchi", Category.GROUP),
        Classification("46.31", "Commercio all'ingrosso di frutta e ortaggi", Category.CLASS),
        Classification("46.31.1", "Commercio all'ingrosso di frutta e ortaggi freschi", Category.SUBCLASS),
        Classification("46.31.10", "Commercio all'ingrosso di frutta e ortaggi freschi", Category.SUBCLASS),
        Classification(
            "46.31.2", "Commercio all'ingrosso di frutta e ortaggi conservati o surgelati", Category.SUBCLASS
        ),
        Classification(
            "46.31.20", "Commercio all'ingrosso di frutta e ortaggi conservati o surgelati", Category.SUBCLASS
        ),
        Classification(
            "46.32",
            "Commercio all'ingrosso di carne, prodotti a base di carne, pesce e prodotti a base di pesce",
            Category.CLASS,
        ),
        Classification("46.32.1", "Commercio all'ingrosso di carne", Category.SUBCLASS),
        Classification("46.32.11", "Commercio all'ingrosso di carni fresche", Category.SUBCLASS),
        Classification("46.32.12", "Commercio all'ingrosso di carni conservate o surgelate", Category.SUBCLASS),
        Classification(
            "46.32.2", "Commercio all'ingrosso di salumi e di altri prodotti a base di carne", Category.SUBCLASS
        ),
        Classification(
            "46.32.20", "Commercio all'ingrosso di salumi e di altri prodotti a base di carne", Category.SUBCLASS
        ),
        Classification("46.32.3", "Commercio all'ingrosso di pesce", Category.SUBCLASS),
        Classification("46.32.31", "Commercio all'ingrosso di pesci freschi", Category.SUBCLASS),
        Classification(
            "46.32.32",
            "Commercio all'ingrosso di pesci conservati o surgelati e di prodotti a base di pesce",
            Category.SUBCLASS,
        ),
        Classification(
            "46.33",
            "Commercio all'ingrosso di prodotti lattiero-caseari, uova, oli e grassi alimentari",
            Category.CLASS,
        ),
        Classification("46.33.1", "Commercio all'ingrosso di prodotti lattiero-caseari e uova", Category.SUBCLASS),
        Classification("46.33.10", "Commercio all'ingrosso di prodotti lattiero-caseari e uova", Category.SUBCLASS),
        Classification("46.33.2", "Commercio all'ingrosso di oli e grassi alimentari", Category.SUBCLASS),
        Classification("46.33.20", "Commercio all'ingrosso di oli e grassi alimentari", Category.SUBCLASS),
        Classification("46.34", "Commercio all'ingrosso di bevande", Category.CLASS),
        Classification("46.34.1", "Commercio all'ingrosso di bevande alcoliche", Category.SUBCLASS),
        Classification("46.34.10", "Commercio all'ingrosso di bevande alcoliche", Category.SUBCLASS),
        Classification("46.34.2", "Commercio all'ingrosso di bevande analcoliche", Category.SUBCLASS),
        Classification("46.34.20", "Commercio all'ingrosso di bevande analcoliche", Category.SUBCLASS),
        Classification("46.35", "Commercio all'ingrosso di prodotti del tabacco", Category.CLASS),
        Classification("46.35.0", "Commercio all'ingrosso di prodotti del tabacco", Category.SUBCLASS),
        Classification("46.35.01", "Commercio all'ingrosso di sigarette elettroniche", Category.SUBCLASS),
        Classification("46.35.09", "Commercio all'ingrosso di prodotti del tabacco n.c.a.", Category.SUBCLASS),
        Classification("46.36", "Commercio all'ingrosso di zucchero, cioccolato e dolciumi", Category.CLASS),
        Classification("46.36.0", "Commercio all'ingrosso di zucchero, cioccolato e dolciumi", Category.SUBCLASS),
        Classification("46.36.00", "Commercio all'ingrosso di zucchero, cioccolato e dolciumi", Category.SUBCLASS),
        Classification("46.37", "Commercio all'ingrosso di caffè, tè, cacao e spezie", Category.CLASS),
        Classification("46.37.0", "Commercio all'ingrosso di caffè, tè, cacao e spezie", Category.SUBCLASS),
        Classification("46.37.01", "Commercio all'ingrosso di caffè", Category.SUBCLASS),
        Classification("46.37.02", "Commercio all'ingrosso di tè, cacao e spezie", Category.SUBCLASS),
        Classification("46.38", "Commercio all'ingrosso di altri prodotti alimentari", Category.CLASS),
        Classification("46.38.0", "Commercio all'ingrosso di altri prodotti alimentari", Category.SUBCLASS),
        Classification("46.38.00", "Commercio all'ingrosso di altri prodotti alimentari", Category.SUBCLASS),
        Classification(
            "46.39",
            "Commercio all'ingrosso non specializzato di prodotti alimentari, bevande e tabacchi",
            Category.CLASS,
        ),
        Classification(
            "46.39.0",
            "Commercio all'ingrosso non specializzato di prodotti alimentari, bevande e tabacchi",
            Category.SUBCLASS,
        ),
        Classification(
            "46.39.00",
            "Commercio all'ingrosso non specializzato di prodotti alimentari, bevande e tabacchi",
            Category.SUBCLASS,
        ),
        Classification("46.4", "Commercio all'ingrosso di beni di consumo", Category.GROUP),
        Classification("46.41", "Commercio all'ingrosso di prodotti tessili", Category.CLASS),
        Classification("46.41.1", "Commercio all'ingrosso di tessuti", Category.SUBCLASS),
        Classification("46.41.10", "Commercio all'ingrosso di tessuti", Category.SUBCLASS),
        Classification("46.41.2", "Commercio all'ingrosso di filati e articoli di merceria", Category.SUBCLASS),
        Classification("46.41.20", "Commercio all'ingrosso di filati e articoli di merceria", Category.SUBCLASS),
        Classification("46.41.9", "Commercio all'ingrosso di altri prodotti tessili", Category.SUBCLASS),
        Classification("46.41.90", "Commercio all'ingrosso di altri prodotti tessili", Category.SUBCLASS),
        Classification("46.42", "Commercio all'ingrosso di abbigliamento e di calzature", Category.CLASS),
        Classification(
            "46.42.1", "Commercio all'ingrosso di abbigliamento e di accessori per l'abbigliamento", Category.SUBCLASS
        ),
        Classification(
            "46.42.10", "Commercio all'ingrosso di abbigliamento e di accessori per l'abbigliamento", Category.SUBCLASS
        ),
        Classification("46.42.2", "Commercio all'ingrosso di articoli in pelliccia", Category.SUBCLASS),
        Classification("46.42.20", "Commercio all'ingrosso di articoli in pelliccia", Category.SUBCLASS),
        Classification("46.42.3", "Commercio all'ingrosso di calzature", Category.SUBCLASS),
        Classification("46.42.30", "Commercio all'ingrosso di calzature", Category.SUBCLASS),
        Classification("46.43", "Commercio all'ingrosso di elettrodomestici", Category.CLASS),
        Classification("46.43.1", "Commercio all'ingrosso di articoli per fotografia e ottica", Category.SUBCLASS),
        Classification("46.43.10", "Commercio all'ingrosso di articoli per fotografia e ottica", Category.SUBCLASS),
        Classification("46.43.2", "Commercio all'ingrosso di apparecchiature radiotelevisive", Category.SUBCLASS),
        Classification("46.43.20", "Commercio all'ingrosso di apparecchiature radiotelevisive", Category.SUBCLASS),
        Classification("46.43.3", "Commercio all'ingrosso di altri elettrodomestici", Category.SUBCLASS),
        Classification("46.43.30", "Commercio all'ingrosso di altri elettrodomestici", Category.SUBCLASS),
        Classification(
            "46.44",
            "Commercio all'ingrosso di articoli di porcellana, di vetro e di prodotti per la pulizia",
            Category.CLASS,
        ),
        Classification("46.44.1", "Commercio all'ingrosso di articoli di porcellana", Category.SUBCLASS),
        Classification("46.44.10", "Commercio all'ingrosso di articoli di porcellana", Category.SUBCLASS),
        Classification("46.44.2", "Commercio all'ingrosso di articoli di vetro", Category.SUBCLASS),
        Classification("46.44.20", "Commercio all'ingrosso di articoli di vetro", Category.SUBCLASS),
        Classification(
            "46.44.3", "Commercio all'ingrosso di altri utensili per la casa, stoviglie e vasellame", Category.SUBCLASS
        ),
        Classification(
            "46.44.30", "Commercio all'ingrosso di altri utensili per la casa, stoviglie e vasellame", Category.SUBCLASS
        ),
        Classification("46.44.4", "Commercio all'ingrosso di prodotti per la pulizia", Category.SUBCLASS),
        Classification("46.44.40", "Commercio all'ingrosso di prodotti per la pulizia", Category.SUBCLASS),
        Classification("46.45", "Commercio all'ingrosso di profumi e cosmetici", Category.CLASS),
        Classification("46.45.0", "Commercio all'ingrosso di profumi e cosmetici", Category.SUBCLASS),
        Classification("46.45.00", "Commercio all'ingrosso di profumi e cosmetici", Category.SUBCLASS),
        Classification("46.46", "Commercio all'ingrosso di prodotti farmaceutici e medicali", Category.CLASS),
        Classification(
            "46.46.1",
            "Commercio all'ingrosso di prodotti farmaceutici di base e di preparati farmaceutici",
            Category.SUBCLASS,
        ),
        Classification(
            "46.46.10",
            "Commercio all'ingrosso di prodotti farmaceutici di base e di preparati farmaceutici",
            Category.SUBCLASS,
        ),
        Classification("46.46.2", "Commercio all'ingrosso di rimedi erboristici", Category.SUBCLASS),
        Classification("46.46.20", "Commercio all'ingrosso di rimedi erboristici", Category.SUBCLASS),
        Classification("46.46.3", "Commercio all'ingrosso di prodotti medicali e ortopedici", Category.SUBCLASS),
        Classification("46.46.31", "Commercio all'ingrosso di occhiali e lenti", Category.SUBCLASS),
        Classification(
            "46.46.39", "Commercio all'ingrosso di prodotti medicali e ortopedici n.c.a.", Category.SUBCLASS
        ),
        Classification(
            "46.47",
            "Commercio all'ingrosso di mobili, tappeti e articoli per l'illuminazione per la casa, l'ufficio e i negozi",
            Category.CLASS,
        ),
        Classification(
            "46.47.1", "Commercio all'ingrosso di mobili per la casa, l'ufficio e i negozi", Category.SUBCLASS
        ),
        Classification(
            "46.47.10", "Commercio all'ingrosso di mobili per la casa, l'ufficio e i negozi", Category.SUBCLASS
        ),
        Classification(
            "46.47.2", "Commercio all'ingrosso di tappeti per la casa, l'ufficio e i negozi", Category.SUBCLASS
        ),
        Classification(
            "46.47.20", "Commercio all'ingrosso di tappeti per la casa, l'ufficio e i negozi", Category.SUBCLASS
        ),
        Classification(
            "46.47.3",
            "Commercio all'ingrosso di articoli per l'illuminazione per la casa, l'ufficio e i negozi",
            Category.SUBCLASS,
        ),
        Classification(
            "46.47.30",
            "Commercio all'ingrosso di articoli per l'illuminazione per la casa, l'ufficio e i negozi",
            Category.SUBCLASS,
        ),
        Classification("46.48", "Commercio all'ingrosso di orologi e di gioielleria", Category.CLASS),
        Classification("46.48.0", "Commercio all'ingrosso di orologi e di gioielleria", Category.SUBCLASS),
        Classification("46.48.00", "Commercio all'ingrosso di orologi e di gioielleria", Category.SUBCLASS),
        Classification("46.49", "Commercio all'ingrosso di altri beni di consumo", Category.CLASS),
        Classification(
            "46.49.1", "Commercio all'ingrosso di carta, cartone e articoli di cartoleria", Category.SUBCLASS
        ),
        Classification(
            "46.49.10", "Commercio all'ingrosso di carta, cartone e articoli di cartoleria", Category.SUBCLASS
        ),
        Classification("46.49.2", "Commercio all'ingrosso di libri, riviste e giornali", Category.SUBCLASS),
        Classification("46.49.21", "Commercio all'ingrosso di libri", Category.SUBCLASS),
        Classification("46.49.22", "Commercio all'ingrosso di riviste e giornali", Category.SUBCLASS),
        Classification(
            "46.49.3", "Commercio all'ingrosso di giochi, giocattoli e attrezzature per bambini", Category.SUBCLASS
        ),
        Classification(
            "46.49.30", "Commercio all'ingrosso di giochi, giocattoli e attrezzature per bambini", Category.SUBCLASS
        ),
        Classification(
            "46.49.4",
            "Commercio all'ingrosso di biciclette e altre attrezzature e articoli sportivi",
            Category.SUBCLASS,
        ),
        Classification("46.49.41", "Commercio all'ingrosso di biciclette", Category.SUBCLASS),
        Classification(
            "46.49.49", "Commercio all'ingrosso di altre attrezzature e articoli sportivi", Category.SUBCLASS
        ),
        Classification(
            "46.49.5", "Commercio all'ingrosso di articoli in pelle e articoli da viaggio", Category.SUBCLASS
        ),
        Classification(
            "46.49.50", "Commercio all'ingrosso di articoli in pelle e articoli da viaggio", Category.SUBCLASS
        ),
        Classification("46.49.9", "Commercio all'ingrosso di altri beni di consumo n.c.a.", Category.SUBCLASS),
        Classification("46.49.91", "Commercio all'ingrosso di articoli promozionali", Category.SUBCLASS),
        Classification("46.49.92", "Commercio all'ingrosso di bomboniere", Category.SUBCLASS),
        Classification("46.49.99", "Commercio all'ingrosso di altri beni di consumo vari n.c.a.", Category.SUBCLASS),
        Classification(
            "46.5", "Commercio all'ingrosso di apparecchiature informatiche e di comunicazione", Category.GROUP
        ),
        Classification(
            "46.50", "Commercio all'ingrosso di apparecchiature informatiche e di comunicazione", Category.CLASS
        ),
        Classification(
            "46.50.1", "Commercio all'ingrosso di computer, unità periferiche e software", Category.SUBCLASS
        ),
        Classification(
            "46.50.10", "Commercio all'ingrosso di computer, unità periferiche e software", Category.SUBCLASS
        ),
        Classification("46.50.2", "Commercio all'ingrosso di apparecchiature per telecomunicazioni", Category.SUBCLASS),
        Classification(
            "46.50.20", "Commercio all'ingrosso di apparecchiature per telecomunicazioni", Category.SUBCLASS
        ),
        Classification(
            "46.50.3", "Commercio all'ingrosso di altre macchine e attrezzature per ufficio", Category.SUBCLASS
        ),
        Classification(
            "46.50.30", "Commercio all'ingrosso di altre macchine e attrezzature per ufficio", Category.SUBCLASS
        ),
        Classification("46.6", "Commercio all'ingrosso di altri macchinari, attrezzature e forniture", Category.GROUP),
        Classification(
            "46.61", "Commercio all'ingrosso di macchinari, attrezzature e forniture agricole", Category.CLASS
        ),
        Classification(
            "46.61.0", "Commercio all'ingrosso di macchinari, attrezzature e forniture agricole", Category.SUBCLASS
        ),
        Classification(
            "46.61.00", "Commercio all'ingrosso di macchinari, attrezzature e forniture agricole", Category.SUBCLASS
        ),
        Classification("46.62", "Commercio all'ingrosso di macchine utensili", Category.CLASS),
        Classification("46.62.0", "Commercio all'ingrosso di macchine utensili", Category.SUBCLASS),
        Classification("46.62.00", "Commercio all'ingrosso di macchine utensili", Category.SUBCLASS),
        Classification(
            "46.63",
            "Commercio all'ingrosso di macchinari per l'estrazione, l'edilizia e l'ingegneria civile",
            Category.CLASS,
        ),
        Classification(
            "46.63.0",
            "Commercio all'ingrosso di macchinari per l'estrazione, l'edilizia e l'ingegneria civile",
            Category.SUBCLASS,
        ),
        Classification(
            "46.63.00",
            "Commercio all'ingrosso di macchinari per l'estrazione, l'edilizia e l'ingegneria civile",
            Category.SUBCLASS,
        ),
        Classification("46.64", "Commercio all'ingrosso di altri macchinari e attrezzature", Category.CLASS),
        Classification("46.64.1", "Commercio all'ingrosso di mezzi di trasporto", Category.SUBCLASS),
        Classification("46.64.11", "Commercio all'ingrosso di navi e imbarcazioni", Category.SUBCLASS),
        Classification("46.64.19", "Commercio all'ingrosso di altri mezzi di trasporto", Category.SUBCLASS),
        Classification(
            "46.64.2", "Commercio all'ingrosso di materiale elettrico per impianti industriali", Category.SUBCLASS
        ),
        Classification(
            "46.64.20", "Commercio all'ingrosso di materiale elettrico per impianti industriali", Category.SUBCLASS
        ),
        Classification(
            "46.64.3",
            "Commercio all'ingrosso di attrezzature per parrucchieri, palestre, solarium e centri estetici",
            Category.SUBCLASS,
        ),
        Classification(
            "46.64.30",
            "Commercio all'ingrosso di attrezzature per parrucchieri, palestre, solarium e centri estetici",
            Category.SUBCLASS,
        ),
        Classification(
            "46.64.4",
            "Commercio all'ingrosso di macchine tessili, per la lavorazione delle pelli e del cuoio, per lavanderie e stirerie",
            Category.SUBCLASS,
        ),
        Classification(
            "46.64.40",
            "Commercio all'ingrosso di macchine tessili, per la lavorazione delle pelli e del cuoio, per lavanderie e stirerie",
            Category.SUBCLASS,
        ),
        Classification(
            "46.64.5",
            "Commercio all'ingrosso di macchinari per l'industria alimentare e delle bevande",
            Category.SUBCLASS,
        ),
        Classification(
            "46.64.51", "Commercio all'ingrosso di macchine e attrezzature per ristoranti e bar", Category.SUBCLASS
        ),
        Classification(
            "46.64.59",
            "Commercio all'ingrosso di altri macchinari per l'industria alimentare e delle bevande",
            Category.SUBCLASS,
        ),
        Classification(
            "46.64.6", "Commercio all'ingrosso di macchinari e attrezzature per la pulizia", Category.SUBCLASS
        ),
        Classification(
            "46.64.60", "Commercio all'ingrosso di macchinari e attrezzature per la pulizia", Category.SUBCLASS
        ),
        Classification(
            "46.64.9", "Commercio all'ingrosso di altri macchinari e attrezzature n.c.a.", Category.SUBCLASS
        ),
        Classification(
            "46.64.91", "Commercio all'ingrosso di strumenti e apparecchiature di misurazione", Category.SUBCLASS
        ),
        Classification(
            "46.64.92",
            "Commercio all'ingrosso di attrazioni per parchi divertimento e parchi tematici e videogiochi",
            Category.SUBCLASS,
        ),
        Classification(
            "46.64.99", "Commercio all'ingrosso di altri macchinari e attrezzature varie n.c.a.", Category.SUBCLASS
        ),
        Classification(
            "46.7", "Commercio all'ingrosso di autoveicoli, motocicli e relative parti e accessori", Category.GROUP
        ),
        Classification("46.71", "Commercio all'ingrosso di autoveicoli", Category.CLASS),
        Classification("46.71.1", "Commercio all'ingrosso di automobili e autoveicoli leggeri", Category.SUBCLASS),
        Classification("46.71.10", "Commercio all'ingrosso di automobili e autoveicoli leggeri", Category.SUBCLASS),
        Classification("46.71.2", "Commercio all'ingrosso di altri autoveicoli", Category.SUBCLASS),
        Classification("46.71.20", "Commercio all'ingrosso di altri autoveicoli", Category.SUBCLASS),
        Classification("46.72", "Commercio all'ingrosso di parti e accessori di autoveicoli", Category.CLASS),
        Classification("46.72.0", "Commercio all'ingrosso di parti e accessori di autoveicoli", Category.SUBCLASS),
        Classification("46.72.00", "Commercio all'ingrosso di parti e accessori di autoveicoli", Category.SUBCLASS),
        Classification("46.73", "Commercio all'ingrosso di motocicli, parti e accessori di motocicli", Category.CLASS),
        Classification("46.73.1", "Commercio all'ingrosso di motocicli", Category.SUBCLASS),
        Classification("46.73.10", "Commercio all'ingrosso di motocicli", Category.SUBCLASS),
        Classification("46.73.2", "Commercio all'ingrosso di parti e accessori di motocicli", Category.SUBCLASS),
        Classification("46.73.20", "Commercio all'ingrosso di parti e accessori di motocicli", Category.SUBCLASS),
        Classification("46.8", "Commercio all'ingrosso specializzato di altri prodotti", Category.GROUP),
        Classification(
            "46.81",
            "Commercio all'ingrosso di combustibili solidi, liquidi, gassosi e di prodotti derivati",
            Category.CLASS,
        ),
        Classification(
            "46.81.0",
            "Commercio all'ingrosso di combustibili solidi, liquidi, gassosi e di prodotti derivati",
            Category.SUBCLASS,
        ),
        Classification(
            "46.81.00",
            "Commercio all'ingrosso di combustibili solidi, liquidi, gassosi e di prodotti derivati",
            Category.SUBCLASS,
        ),
        Classification("46.82", "Commercio all'ingrosso di metalli e minerali metalliferi", Category.CLASS),
        Classification(
            "46.82.1", "Commercio all'ingrosso di metalli e minerali metalliferi ferrosi", Category.SUBCLASS
        ),
        Classification(
            "46.82.10", "Commercio all'ingrosso di metalli e minerali metalliferi ferrosi", Category.SUBCLASS
        ),
        Classification(
            "46.82.2", "Commercio all'ingrosso di metalli e minerali metalliferi non ferrosi", Category.SUBCLASS
        ),
        Classification("46.82.21", "Attività di compro oro", Category.SUBCLASS),
        Classification(
            "46.82.29", "Commercio all'ingrosso di altri metalli e minerali metalliferi non ferrosi", Category.SUBCLASS
        ),
        Classification(
            "46.83",
            "Commercio all'ingrosso di legname, materiali da costruzione e articoli igienico-sanitari",
            Category.CLASS,
        ),
        Classification("46.83.1", "Commercio all'ingrosso di legname", Category.SUBCLASS),
        Classification("46.83.10", "Commercio all'ingrosso di legname", Category.SUBCLASS),
        Classification("46.83.2", "Commercio all'ingrosso di materiali da costruzione", Category.SUBCLASS),
        Classification("46.83.21", "Commercio all'ingrosso di pitture, vernici e lacche", Category.SUBCLASS),
        Classification(
            "46.83.22", "Commercio all'ingrosso di carta da parati e rivestimenti per pavimenti", Category.SUBCLASS
        ),
        Classification("46.83.23", "Commercio all'ingrosso di porte, finestre e persiane", Category.SUBCLASS),
        Classification("46.83.29", "Commercio all'ingrosso di altri materiali da costruzione", Category.SUBCLASS),
        Classification("46.83.3", "Commercio all'ingrosso di articoli igienico-sanitari", Category.SUBCLASS),
        Classification("46.83.30", "Commercio all'ingrosso di articoli igienico-sanitari", Category.SUBCLASS),
        Classification(
            "46.84",
            "Commercio all'ingrosso di ferramenta, di apparecchi e accessori per impianti idraulici e di riscaldamento",
            Category.CLASS,
        ),
        Classification("46.84.1", "Commercio all'ingrosso di ferramenta", Category.SUBCLASS),
        Classification("46.84.10", "Commercio all'ingrosso di ferramenta", Category.SUBCLASS),
        Classification(
            "46.84.2",
            "Commercio all'ingrosso di apparecchi e accessori per impianti idraulici e di riscaldamento",
            Category.SUBCLASS,
        ),
        Classification(
            "46.84.20",
            "Commercio all'ingrosso di apparecchi e accessori per impianti idraulici e di riscaldamento",
            Category.SUBCLASS,
        ),
        Classification("46.85", "Commercio all'ingrosso di prodotti chimici", Category.CLASS),
        Classification("46.85.0", "Commercio all'ingrosso di prodotti chimici", Category.SUBCLASS),
        Classification(
            "46.85.01",
            "Commercio all'ingrosso di fertilizzanti e altri prodotti chimici per l'agricoltura",
            Category.SUBCLASS,
        ),
        Classification(
            "46.85.02", "Commercio all'ingrosso di liquidi per inalazione per sigarette elettroniche", Category.SUBCLASS
        ),
        Classification("46.85.09", "Commercio all'ingrosso di altri prodotti chimici", Category.SUBCLASS),
        Classification("46.86", "Commercio all'ingrosso di altri prodotti intermedi", Category.CLASS),
        Classification(
            "46.86.1", "Commercio all'ingrosso di materie plastiche in forme primarie e gomma", Category.SUBCLASS
        ),
        Classification(
            "46.86.10", "Commercio all'ingrosso di materie plastiche in forme primarie e gomma", Category.SUBCLASS
        ),
        Classification("46.86.2", "Commercio all'ingrosso di fibre tessili", Category.SUBCLASS),
        Classification("46.86.20", "Commercio all'ingrosso di fibre tessili", Category.SUBCLASS),
        Classification("46.86.3", "Commercio all'ingrosso di articoli per imballaggio", Category.SUBCLASS),
        Classification("46.86.30", "Commercio all'ingrosso di articoli per imballaggio", Category.SUBCLASS),
        Classification("46.86.9", "Commercio all'ingrosso di altri prodotti intermedi n.c.a.", Category.SUBCLASS),
        Classification("46.86.90", "Commercio all'ingrosso di altri prodotti intermedi n.c.a.", Category.SUBCLASS),
        Classification("46.87", "Commercio all'ingrosso di rottami e cascami", Category.CLASS),
        Classification("46.87.1", "Commercio all'ingrosso di rottami e cascami metallici", Category.SUBCLASS),
        Classification("46.87.10", "Commercio all'ingrosso di rottami e cascami metallici", Category.SUBCLASS),
        Classification("46.87.9", "Commercio all'ingrosso di altri rottami e cascami", Category.SUBCLASS),
        Classification("46.87.90", "Commercio all'ingrosso di altri rottami e cascami", Category.SUBCLASS),
        Classification("46.89", "Commercio all'ingrosso specializzato di altri prodotti n.c.a.", Category.CLASS),
        Classification("46.89.0", "Commercio all'ingrosso specializzato di altri prodotti n.c.a.", Category.SUBCLASS),
        Classification("46.89.00", "Commercio all'ingrosso specializzato di altri prodotti n.c.a.", Category.SUBCLASS),
        Classification("46.9", "Commercio all'ingrosso non specializzato", Category.GROUP),
        Classification("46.90", "Commercio all'ingrosso non specializzato", Category.CLASS),
        Classification("46.90.0", "Commercio all'ingrosso non specializzato", Category.SUBCLASS),
        Classification("46.90.00", "Commercio all'ingrosso non specializzato", Category.SUBCLASS),
        Classification("47", "Commercio al dettaglio", Category.DIVISION),
        Classification("47.1", "Commercio al dettaglio non specializzato", Category.GROUP),
        Classification(
            "47.11",
            "Commercio al dettaglio non specializzato con prevalenza di prodotti alimentari, bevande o tabacchi",
            Category.CLASS,
        ),
        Classification(
            "47.11.0",
            "Commercio al dettaglio non specializzato con prevalenza di prodotti alimentari, bevande o tabacchi",
            Category.SUBCLASS,
        ),
        Classification(
            "47.11.01",
            "Commercio al dettaglio non specializzato con prevalenza di prodotti alimentari surgelati",
            Category.SUBCLASS,
        ),
        Classification(
            "47.11.02",
            "Commercio al dettaglio non specializzato con prevalenza di altri prodotti alimentari, bevande o tabacchi",
            Category.SUBCLASS,
        ),
        Classification("47.12", "Commercio al dettaglio non specializzato di altri prodotti", Category.CLASS),
        Classification(
            "47.12.1",
            "Commercio al dettaglio non specializzato con prevalenza di apparecchiature informatiche ed elettrodomestici",
            Category.SUBCLASS,
        ),
        Classification(
            "47.12.10",
            "Commercio al dettaglio non specializzato con prevalenza di apparecchiature informatiche ed elettrodomestici",
            Category.SUBCLASS,
        ),
        Classification(
            "47.12.2",
            "Commercio al dettaglio non specializzato con prevalenza di mobili e articoli per uso domestico",
            Category.SUBCLASS,
        ),
        Classification(
            "47.12.20",
            "Commercio al dettaglio non specializzato con prevalenza di mobili e articoli per uso domestico",
            Category.SUBCLASS,
        ),
        Classification(
            "47.12.3",
            "Commercio al dettaglio non specializzato con prevalenza di ferramenta, materiali da costruzione e piante",
            Category.SUBCLASS,
        ),
        Classification(
            "47.12.30",
            "Commercio al dettaglio non specializzato con prevalenza di ferramenta, materiali da costruzione e piante",
            Category.SUBCLASS,
        ),
        Classification(
            "47.12.4",
            "Commercio al dettaglio non specializzato con prevalenza di cosmetici, articoli di profumeria e detersivi, articoli di cancelleria e giochi",
            Category.SUBCLASS,
        ),
        Classification(
            "47.12.40",
            "Commercio al dettaglio non specializzato con prevalenza di cosmetici, articoli di profumeria e detersivi, articoli di cancelleria e giochi",
            Category.SUBCLASS,
        ),
        Classification(
            "47.12.5",
            "Commercio al dettaglio non specializzato con prevalenza di articoli di abbigliamento e calzature",
            Category.SUBCLASS,
        ),
        Classification(
            "47.12.50",
            "Commercio al dettaglio non specializzato con prevalenza di articoli di abbigliamento e calzature",
            Category.SUBCLASS,
        ),
        Classification(
            "47.12.9", "Commercio al dettaglio non specializzato di altri prodotti n.c.a.", Category.SUBCLASS
        ),
        Classification(
            "47.12.90", "Commercio al dettaglio non specializzato di altri prodotti n.c.a.", Category.SUBCLASS
        ),
        Classification("47.2", "Commercio al dettaglio di prodotti alimentari, bevande e tabacchi", Category.GROUP),
        Classification("47.21", "Commercio al dettaglio di frutta e verdura", Category.CLASS),
        Classification("47.21.0", "Commercio al dettaglio di frutta e verdura", Category.SUBCLASS),
        Classification("47.21.01", "Commercio al dettaglio di frutta e verdura fresca", Category.SUBCLASS),
        Classification("47.21.02", "Commercio al dettaglio di frutta e verdura secca e conservata", Category.SUBCLASS),
        Classification("47.22", "Commercio al dettaglio di carne e di prodotti a base di carne", Category.CLASS),
        Classification("47.22.0", "Commercio al dettaglio di carne e di prodotti a base di carne", Category.SUBCLASS),
        Classification("47.22.00", "Commercio al dettaglio di carne e di prodotti a base di carne", Category.SUBCLASS),
        Classification("47.23", "Commercio al dettaglio di pesce, crostacei e molluschi", Category.CLASS),
        Classification("47.23.0", "Commercio al dettaglio di pesce, crostacei e molluschi", Category.SUBCLASS),
        Classification("47.23.00", "Commercio al dettaglio di pesce, crostacei e molluschi", Category.SUBCLASS),
        Classification("47.24", "Commercio al dettaglio di pane, pasticceria e dolciumi", Category.CLASS),
        Classification("47.24.1", "Commercio al dettaglio di pane", Category.SUBCLASS),
        Classification("47.24.10", "Commercio al dettaglio di pane", Category.SUBCLASS),
        Classification("47.24.2", "Commercio al dettaglio di pasticceria e dolciumi", Category.SUBCLASS),
        Classification("47.24.20", "Commercio al dettaglio di pasticceria e dolciumi", Category.SUBCLASS),
        Classification("47.25", "Commercio al dettaglio di bevande", Category.CLASS),
        Classification("47.25.0", "Commercio al dettaglio di bevande", Category.SUBCLASS),
        Classification("47.25.00", "Commercio al dettaglio di bevande", Category.SUBCLASS),
        Classification("47.26", "Commercio al dettaglio di prodotti del tabacco", Category.CLASS),
        Classification("47.26.0", "Commercio al dettaglio di prodotti del tabacco", Category.SUBCLASS),
        Classification("47.26.01", "Commercio al dettaglio di tabacco in qualsiasi forma", Category.SUBCLASS),
        Classification(
            "47.26.02",
            "Commercio al dettaglio di sigarette elettroniche e di liquidi per inalazione per sigarette elettroniche",
            Category.SUBCLASS,
        ),
        Classification("47.26.09", "Commercio al dettaglio di altri accessori per fumatori", Category.SUBCLASS),
        Classification("47.27", "Commercio al dettaglio di altri prodotti alimentari", Category.CLASS),
        Classification("47.27.1", "Commercio al dettaglio di latte e prodotti lattiero-caseari", Category.SUBCLASS),
        Classification("47.27.10", "Commercio al dettaglio di latte e prodotti lattiero-caseari", Category.SUBCLASS),
        Classification("47.27.2", "Commercio al dettaglio di caffè", Category.SUBCLASS),
        Classification("47.27.20", "Commercio al dettaglio di caffè", Category.SUBCLASS),
        Classification(
            "47.27.3", "Commercio al dettaglio di integratori alimentari e prodotti dietetici", Category.SUBCLASS
        ),
        Classification(
            "47.27.30", "Commercio al dettaglio di integratori alimentari e prodotti dietetici", Category.SUBCLASS
        ),
        Classification("47.27.9", "Commercio al dettaglio di altri prodotti alimentari n.c.a.", Category.SUBCLASS),
        Classification("47.27.90", "Commercio al dettaglio di altri prodotti alimentari n.c.a.", Category.SUBCLASS),
        Classification("47.3", "Commercio al dettaglio di carburanti per autotrazione", Category.GROUP),
        Classification("47.30", "Commercio al dettaglio di carburanti per autotrazione", Category.CLASS),
        Classification("47.30.0", "Commercio al dettaglio di carburanti per autotrazione", Category.SUBCLASS),
        Classification("47.30.00", "Commercio al dettaglio di carburanti per autotrazione", Category.SUBCLASS),
        Classification(
            "47.4", "Commercio al dettaglio di apparecchiature informatiche e di comunicazione", Category.GROUP
        ),
        Classification(
            "47.40", "Commercio al dettaglio di apparecchiature informatiche e di comunicazione", Category.CLASS
        ),
        Classification(
            "47.40.1", "Commercio al dettaglio di computer, unità periferiche e software", Category.SUBCLASS
        ),
        Classification(
            "47.40.10", "Commercio al dettaglio di computer, unità periferiche e software", Category.SUBCLASS
        ),
        Classification("47.40.2", "Commercio al dettaglio di apparecchiature per telecomunicazioni", Category.SUBCLASS),
        Classification(
            "47.40.20", "Commercio al dettaglio di apparecchiature per telecomunicazioni", Category.SUBCLASS
        ),
        Classification("47.40.3", "Commercio al dettaglio di apparecchiature radiotelevisive", Category.SUBCLASS),
        Classification("47.40.30", "Commercio al dettaglio di apparecchiature radiotelevisive", Category.SUBCLASS),
        Classification("47.5", "Commercio al dettaglio di altre attrezzature per uso domestico", Category.GROUP),
        Classification("47.51", "Commercio al dettaglio di prodotti tessili", Category.CLASS),
        Classification(
            "47.51.1", "Commercio al dettaglio di tessuti per abbigliamento e arredamento", Category.SUBCLASS
        ),
        Classification(
            "47.51.10", "Commercio al dettaglio di tessuti per abbigliamento e arredamento", Category.SUBCLASS
        ),
        Classification("47.51.2", "Commercio al dettaglio di filati per maglieria e merceria", Category.SUBCLASS),
        Classification("47.51.20", "Commercio al dettaglio di filati per maglieria e merceria", Category.SUBCLASS),
        Classification(
            "47.52", "Commercio al dettaglio di ferramenta, materiali da costruzione, vernici e vetro", Category.CLASS
        ),
        Classification(
            "47.52.1",
            "Commercio al dettaglio di ferramenta, vernici, vetro e materiale elettrico e termoidraulico",
            Category.SUBCLASS,
        ),
        Classification(
            "47.52.10",
            "Commercio al dettaglio di ferramenta, vernici, vetro e materiale elettrico e termoidraulico",
            Category.SUBCLASS,
        ),
        Classification(
            "47.52.2", "Commercio al dettaglio di articoli igienico-sanitari e per riscaldamento", Category.SUBCLASS
        ),
        Classification(
            "47.52.20", "Commercio al dettaglio di articoli igienico-sanitari e per riscaldamento", Category.SUBCLASS
        ),
        Classification(
            "47.52.3",
            "Commercio al dettaglio di altri materiali da costruzione, mattoni e piastrelle",
            Category.SUBCLASS,
        ),
        Classification("47.52.31", "Commercio al dettaglio di porte e finestre", Category.SUBCLASS),
        Classification(
            "47.52.32",
            "Commercio al dettaglio di altri materiali da costruzione, mattoni e piastrelle n.c.a.",
            Category.SUBCLASS,
        ),
        Classification(
            "47.52.4",
            "Commercio al dettaglio di attrezzature per il giardinaggio e la paesaggistica",
            Category.SUBCLASS,
        ),
        Classification(
            "47.52.40",
            "Commercio al dettaglio di attrezzature per il giardinaggio e la paesaggistica",
            Category.SUBCLASS,
        ),
        Classification(
            "47.53", "Commercio al dettaglio di tappeti, moquette, rivestimenti per pareti e pavimenti", Category.CLASS
        ),
        Classification("47.53.1", "Commercio al dettaglio di tappeti e tende", Category.SUBCLASS),
        Classification("47.53.11", "Commercio al dettaglio di tappeti e moquette", Category.SUBCLASS),
        Classification("47.53.12", "Commercio al dettaglio di tende", Category.SUBCLASS),
        Classification("47.53.2", "Commercio al dettaglio di rivestimenti per pareti e pavimenti", Category.SUBCLASS),
        Classification("47.53.20", "Commercio al dettaglio di rivestimenti per pareti e pavimenti", Category.SUBCLASS),
        Classification("47.54", "Commercio al dettaglio di elettrodomestici", Category.CLASS),
        Classification("47.54.0", "Commercio al dettaglio di elettrodomestici", Category.SUBCLASS),
        Classification("47.54.00", "Commercio al dettaglio di elettrodomestici", Category.SUBCLASS),
        Classification(
            "47.55",
            "Commercio al dettaglio di mobili, di articoli per l'illuminazione, articoli per la tavola e altri articoli per la casa",
            Category.CLASS,
        ),
        Classification("47.55.1", "Commercio al dettaglio di mobili per la casa", Category.SUBCLASS),
        Classification("47.55.10", "Commercio al dettaglio di mobili per la casa", Category.SUBCLASS),
        Classification("47.55.2", "Commercio al dettaglio di altri mobili", Category.SUBCLASS),
        Classification("47.55.20", "Commercio al dettaglio di altri mobili", Category.SUBCLASS),
        Classification("47.55.3", "Commercio al dettaglio di articoli per l'illuminazione", Category.SUBCLASS),
        Classification("47.55.30", "Commercio al dettaglio di articoli per l'illuminazione", Category.SUBCLASS),
        Classification("47.55.4", "Commercio al dettaglio di articoli per la tavola e la cucina", Category.SUBCLASS),
        Classification("47.55.40", "Commercio al dettaglio di articoli per la tavola e la cucina", Category.SUBCLASS),
        Classification(
            "47.55.9",
            "Commercio al dettaglio di attrezzature per bambini e altri articoli per la casa",
            Category.SUBCLASS,
        ),
        Classification(
            "47.55.90",
            "Commercio al dettaglio di attrezzature per bambini e altri articoli per la casa",
            Category.SUBCLASS,
        ),
        Classification("47.6", "Commercio al dettaglio di articoli culturali e ricreativi", Category.GROUP),
        Classification("47.61", "Commercio al dettaglio di libri", Category.CLASS),
        Classification("47.61.0", "Commercio al dettaglio di libri", Category.SUBCLASS),
        Classification("47.61.00", "Commercio al dettaglio di libri", Category.SUBCLASS),
        Classification(
            "47.62",
            "Commercio al dettaglio di giornali, altre pubblicazioni periodiche e articoli di cancelleria",
            Category.CLASS,
        ),
        Classification(
            "47.62.1", "Commercio al dettaglio di giornali e altre pubblicazioni periodiche", Category.SUBCLASS
        ),
        Classification(
            "47.62.10", "Commercio al dettaglio di giornali e altre pubblicazioni periodiche", Category.SUBCLASS
        ),
        Classification("47.62.2", "Commercio al dettaglio di articoli di cancelleria", Category.SUBCLASS),
        Classification("47.62.20", "Commercio al dettaglio di articoli di cancelleria", Category.SUBCLASS),
        Classification("47.63", "Commercio al dettaglio di attrezzature sportive", Category.CLASS),
        Classification("47.63.1", "Commercio al dettaglio di imbarcazioni", Category.SUBCLASS),
        Classification("47.63.10", "Commercio al dettaglio di imbarcazioni", Category.SUBCLASS),
        Classification(
            "47.63.2", "Commercio al dettaglio di biciclette e altre attrezzature sportive", Category.SUBCLASS
        ),
        Classification("47.63.21", "Commercio al dettaglio di biciclette", Category.SUBCLASS),
        Classification("47.63.29", "Commercio al dettaglio di altre attrezzature sportive", Category.SUBCLASS),
        Classification("47.64", "Commercio al dettaglio di giochi e giocattoli", Category.CLASS),
        Classification("47.64.0", "Commercio al dettaglio di giochi e giocattoli", Category.SUBCLASS),
        Classification("47.64.00", "Commercio al dettaglio di giochi e giocattoli", Category.SUBCLASS),
        Classification("47.69", "Commercio al dettaglio di articoli culturali e ricreativi n.c.a.", Category.CLASS),
        Classification(
            "47.69.1", "Commercio al dettaglio di supporti registrati e strumenti musicali", Category.SUBCLASS
        ),
        Classification("47.69.11", "Commercio al dettaglio di supporti registrati", Category.SUBCLASS),
        Classification("47.69.12", "Commercio al dettaglio di strumenti musicali", Category.SUBCLASS),
        Classification(
            "47.69.2",
            "Commercio al dettaglio di articoli di filatelia, numismatica e da collezionismo",
            Category.SUBCLASS,
        ),
        Classification(
            "47.69.20",
            "Commercio al dettaglio di articoli di filatelia, numismatica e da collezionismo",
            Category.SUBCLASS,
        ),
        Classification(
            "47.69.3", "Commercio al dettaglio di articoli per disegno, pittura e scultura", Category.SUBCLASS
        ),
        Classification(
            "47.69.30", "Commercio al dettaglio di articoli per disegno, pittura e scultura", Category.SUBCLASS
        ),
        Classification(
            "47.69.9", "Commercio al dettaglio di altri articoli culturali e ricreativi n.c.a.", Category.SUBCLASS
        ),
        Classification("47.69.91", "Commercio al dettaglio di opere d'arte", Category.SUBCLASS),
        Classification(
            "47.69.99", "Commercio al dettaglio di altri articoli vari culturali e ricreativi n.c.a.", Category.SUBCLASS
        ),
        Classification(
            "47.7", "Commercio al dettaglio di altri prodotti, esclusi autoveicoli e motocicli", Category.GROUP
        ),
        Classification("47.71", "Commercio al dettaglio di articoli di abbigliamento", Category.CLASS),
        Classification("47.71.1", "Commercio al dettaglio di articoli di abbigliamento per adulti", Category.SUBCLASS),
        Classification("47.71.10", "Commercio al dettaglio di articoli di abbigliamento per adulti", Category.SUBCLASS),
        Classification(
            "47.71.2", "Commercio al dettaglio di articoli di abbigliamento per neonati e bambini", Category.SUBCLASS
        ),
        Classification(
            "47.71.20", "Commercio al dettaglio di articoli di abbigliamento per neonati e bambini", Category.SUBCLASS
        ),
        Classification("47.71.3", "Commercio al dettaglio di articoli di biancheria intima", Category.SUBCLASS),
        Classification("47.71.30", "Commercio al dettaglio di articoli di biancheria intima", Category.SUBCLASS),
        Classification(
            "47.71.4", "Commercio al dettaglio di articoli di abbigliamento in pelle e pelliccia", Category.SUBCLASS
        ),
        Classification(
            "47.71.40", "Commercio al dettaglio di articoli di abbigliamento in pelle e pelliccia", Category.SUBCLASS
        ),
        Classification("47.71.5", "Commercio al dettaglio di accessori per l'abbigliamento", Category.SUBCLASS),
        Classification("47.71.50", "Commercio al dettaglio di accessori per l'abbigliamento", Category.SUBCLASS),
        Classification("47.72", "Commercio al dettaglio di calzature e articoli in pelle", Category.CLASS),
        Classification("47.72.1", "Commercio al dettaglio di calzature e accessori per calzature", Category.SUBCLASS),
        Classification(
            "47.72.11", "Commercio al dettaglio di calzature e accessori per calzature per adulti", Category.SUBCLASS
        ),
        Classification(
            "47.72.12",
            "Commercio al dettaglio di calzature e accessori per calzature per neonati e bambini",
            Category.SUBCLASS,
        ),
        Classification(
            "47.72.2", "Commercio al dettaglio di articoli in pelle e articoli da viaggio", Category.SUBCLASS
        ),
        Classification(
            "47.72.20", "Commercio al dettaglio di articoli in pelle e articoli da viaggio", Category.SUBCLASS
        ),
        Classification("47.73", "Commercio al dettaglio di prodotti farmaceutici", Category.CLASS),
        Classification(
            "47.73.1", "Commercio al dettaglio di medicinali soggetti a prescrizione medica", Category.SUBCLASS
        ),
        Classification(
            "47.73.10", "Commercio al dettaglio di medicinali soggetti a prescrizione medica", Category.SUBCLASS
        ),
        Classification("47.73.2", "Commercio al dettaglio di rimedi erboristici", Category.SUBCLASS),
        Classification("47.73.20", "Commercio al dettaglio di rimedi erboristici", Category.SUBCLASS),
        Classification("47.73.9", "Commercio al dettaglio di altri prodotti farmaceutici", Category.SUBCLASS),
        Classification("47.73.90", "Commercio al dettaglio di altri prodotti farmaceutici", Category.SUBCLASS),
        Classification("47.74", "Commercio al dettaglio di articoli medicali e ortopedici", Category.CLASS),
        Classification("47.74.0", "Commercio al dettaglio di articoli medicali e ortopedici", Category.SUBCLASS),
        Classification("47.74.01", "Commercio al dettaglio di occhiali e lenti", Category.SUBCLASS),
        Classification("47.74.09", "Commercio al dettaglio di altri articoli medicali e ortopedici", Category.SUBCLASS),
        Classification("47.75", "Commercio al dettaglio di cosmetici e di articoli di profumeria", Category.CLASS),
        Classification("47.75.0", "Commercio al dettaglio di cosmetici e di articoli di profumeria", Category.SUBCLASS),
        Classification(
            "47.75.00", "Commercio al dettaglio di cosmetici e di articoli di profumeria", Category.SUBCLASS
        ),
        Classification(
            "47.76",
            "Commercio al dettaglio di fiori, piante, fertilizzanti, animali da compagnia e alimenti per animali da compagnia",
            Category.CLASS,
        ),
        Classification("47.76.1", "Commercio al dettaglio di fiori, piante e fertilizzanti", Category.SUBCLASS),
        Classification("47.76.10", "Commercio al dettaglio di fiori, piante e fertilizzanti", Category.SUBCLASS),
        Classification(
            "47.76.2",
            "Commercio al dettaglio di animali da compagnia e alimenti per animali da compagnia",
            Category.SUBCLASS,
        ),
        Classification(
            "47.76.20",
            "Commercio al dettaglio di animali da compagnia e alimenti per animali da compagnia",
            Category.SUBCLASS,
        ),
        Classification("47.77", "Commercio al dettaglio di orologi e articoli di gioielleria", Category.CLASS),
        Classification("47.77.0", "Commercio al dettaglio di orologi e articoli di gioielleria", Category.SUBCLASS),
        Classification("47.77.00", "Commercio al dettaglio di orologi e articoli di gioielleria", Category.SUBCLASS),
        Classification("47.78", "Commercio al dettaglio di altri prodotti non di seconda mano", Category.CLASS),
        Classification("47.78.1", "Commercio al dettaglio di articoli per fotografia e ottica", Category.SUBCLASS),
        Classification("47.78.10", "Commercio al dettaglio di articoli per fotografia e ottica", Category.SUBCLASS),
        Classification(
            "47.78.2",
            "Commercio al dettaglio di souvenir, articoli di artigianato, articoli religiosi, bigiotteria e bomboniere",
            Category.SUBCLASS,
        ),
        Classification("47.78.21", "Commercio al dettaglio di souvenir", Category.SUBCLASS),
        Classification("47.78.22", "Commercio al dettaglio di articoli di artigianato", Category.SUBCLASS),
        Classification("47.78.23", "Commercio al dettaglio di articoli religiosi", Category.SUBCLASS),
        Classification("47.78.24", "Commercio al dettaglio di bigiotteria", Category.SUBCLASS),
        Classification("47.78.25", "Commercio al dettaglio di bomboniere", Category.SUBCLASS),
        Classification(
            "47.78.3",
            "Commercio al dettaglio di combustibile per uso domestico, bombole di gas, carbone e legna da ardere",
            Category.SUBCLASS,
        ),
        Classification(
            "47.78.30",
            "Commercio al dettaglio di combustibile per uso domestico, bombole di gas, carbone e legna da ardere",
            Category.SUBCLASS,
        ),
        Classification("47.78.4", "Commercio al dettaglio di prodotti per la pulizia", Category.SUBCLASS),
        Classification("47.78.40", "Commercio al dettaglio di prodotti per la pulizia", Category.SUBCLASS),
        Classification(
            "47.78.9", "Commercio al dettaglio di altri prodotti non di seconda mano n.c.a.", Category.SUBCLASS
        ),
        Classification("47.78.91", "Commercio al dettaglio di articoli per imballaggio", Category.SUBCLASS),
        Classification("47.78.92", "Commercio al dettaglio di articoli funerari e cimiteriali", Category.SUBCLASS),
        Classification("47.78.93", "Commercio al dettaglio di articoli per adulti", Category.SUBCLASS),
        Classification(
            "47.78.99", "Commercio al dettaglio di altri prodotti vari non di seconda mano n.c.a.", Category.SUBCLASS
        ),
        Classification("47.79", "Commercio al dettaglio di articoli di seconda mano", Category.CLASS),
        Classification("47.79.1", "Commercio al dettaglio di libri di seconda mano", Category.SUBCLASS),
        Classification("47.79.10", "Commercio al dettaglio di libri di seconda mano", Category.SUBCLASS),
        Classification(
            "47.79.2", "Commercio al dettaglio di oggetti di antiquariato e mobili di seconda mano", Category.SUBCLASS
        ),
        Classification(
            "47.79.20", "Commercio al dettaglio di oggetti di antiquariato e mobili di seconda mano", Category.SUBCLASS
        ),
        Classification(
            "47.79.3",
            "Commercio al dettaglio di articoli di abbigliamento e altri articoli di seconda mano",
            Category.SUBCLASS,
        ),
        Classification(
            "47.79.31", "Commercio al dettaglio di articoli di abbigliamento di seconda mano", Category.SUBCLASS
        ),
        Classification(
            "47.79.32", "Commercio al dettaglio di orologi e articoli di gioielleria di seconda mano", Category.SUBCLASS
        ),
        Classification(
            "47.79.39", "Commercio al dettaglio di altri articoli di seconda mano n.c.a.", Category.SUBCLASS
        ),
        Classification(
            "47.8", "Commercio al dettaglio di autoveicoli, motocicli e relative parti e accessori", Category.GROUP
        ),
        Classification("47.81", "Commercio al dettaglio di autoveicoli", Category.CLASS),
        Classification("47.81.1", "Commercio al dettaglio di automobili e autoveicoli leggeri", Category.SUBCLASS),
        Classification("47.81.10", "Commercio al dettaglio di automobili e autoveicoli leggeri", Category.SUBCLASS),
        Classification("47.81.2", "Commercio al dettaglio di altri autoveicoli", Category.SUBCLASS),
        Classification("47.81.20", "Commercio al dettaglio di altri autoveicoli", Category.SUBCLASS),
        Classification("47.82", "Commercio al dettaglio di parti e accessori di autoveicoli", Category.CLASS),
        Classification("47.82.0", "Commercio al dettaglio di parti e accessori di autoveicoli", Category.SUBCLASS),
        Classification("47.82.00", "Commercio al dettaglio di parti e accessori di autoveicoli", Category.SUBCLASS),
        Classification("47.83", "Commercio al dettaglio di motocicli, parti e accessori di motocicli", Category.CLASS),
        Classification("47.83.1", "Commercio al dettaglio di motocicli", Category.SUBCLASS),
        Classification("47.83.10", "Commercio al dettaglio di motocicli", Category.SUBCLASS),
        Classification("47.83.2", "Commercio al dettaglio di parti e accessori di motocicli", Category.SUBCLASS),
        Classification("47.83.20", "Commercio al dettaglio di parti e accessori di motocicli", Category.SUBCLASS),
        Classification("47.9", "Attività di servizi di intermediazione per il commercio al dettaglio", Category.GROUP),
        Classification(
            "47.91",
            "Attività di servizi di intermediazione per il commercio al dettaglio non specializzato",
            Category.CLASS,
        ),
        Classification(
            "47.91.1",
            "Attività di servizi di intermediazione per il commercio al dettaglio non specializzato di articoli di seconda mano",
            Category.SUBCLASS,
        ),
        Classification(
            "47.91.10",
            "Attività di servizi di intermediazione per il commercio al dettaglio non specializzato di articoli di seconda mano",
            Category.SUBCLASS,
        ),
        Classification(
            "47.91.2",
            "Attività di servizi di intermediazione per il commercio al dettaglio non specializzato di prodotti nuovi",
            Category.SUBCLASS,
        ),
        Classification(
            "47.91.20",
            "Attività di servizi di intermediazione per il commercio al dettaglio non specializzato di prodotti nuovi",
            Category.SUBCLASS,
        ),
        Classification(
            "47.92",
            "Attività di servizi di intermediazione per il commercio al dettaglio specializzato",
            Category.CLASS,
        ),
        Classification(
            "47.92.1",
            "Attività di servizi di intermediazione per il commercio al dettaglio specializzato di prodotti alimentari e bevande",
            Category.SUBCLASS,
        ),
        Classification(
            "47.92.10",
            "Attività di servizi di intermediazione per il commercio al dettaglio specializzato di prodotti alimentari e bevande",
            Category.SUBCLASS,
        ),
        Classification(
            "47.92.2",
            "Attività di servizi di intermediazione per il commercio al dettaglio specializzato di articoli di seconda mano",
            Category.SUBCLASS,
        ),
        Classification(
            "47.92.21",
            "Attività di servizi di intermediazione per il commercio al dettaglio specializzato di autoveicoli e motocicli di seconda mano",
            Category.SUBCLASS,
        ),
        Classification(
            "47.92.22",
            "Attività di servizi di intermediazione per il commercio al dettaglio specializzato di parti e accessori di autoveicoli e motocicli di seconda mano",
            Category.SUBCLASS,
        ),
        Classification(
            "47.92.29",
            "Attività di servizi di intermediazione per il commercio al dettaglio specializzato di altri articoli di seconda mano",
            Category.SUBCLASS,
        ),
        Classification(
            "47.92.3",
            "Attività di servizi di intermediazione per il commercio al dettaglio specializzato di prodotti nuovi",
            Category.SUBCLASS,
        ),
        Classification(
            "47.92.31",
            "Attività di servizi di intermediazione per il commercio al dettaglio specializzato di autoveicoli, esclusi articoli di seconda mano",
            Category.SUBCLASS,
        ),
        Classification(
            "47.92.32",
            "Attività di servizi di intermediazione per il commercio al dettaglio specializzato di parti e accessori di autoveicoli, esclusi articoli di seconda mano",
            Category.SUBCLASS,
        ),
        Classification(
            "47.92.33",
            "Attività di servizi di intermediazione per il commercio al dettaglio specializzato di motocicli, parti e accessori di motocicli, esclusi articoli di seconda mano",
            Category.SUBCLASS,
        ),
        Classification(
            "47.92.34",
            "Attività di servizi di intermediazione per il commercio al dettaglio specializzato di elettrodomestici e altri articoli per la casa, esclusi articoli di seconda mano",
            Category.SUBCLASS,
        ),
        Classification(
            "47.92.35",
            "Attività di servizi di intermediazione per il commercio al dettaglio specializzato di prodotti tessili, articoli di abbigliamento e calzature, esclusi articoli di seconda mano",
            Category.SUBCLASS,
        ),
        Classification(
            "47.92.36",
            "Attività di servizi di intermediazione per il commercio al dettaglio specializzato di cosmetici e di articoli di profumeria, esclusi articoli di seconda mano",
            Category.SUBCLASS,
        ),
        Classification(
            "47.92.39",
            "Attività di servizi di intermediazione per il commercio al dettaglio specializzato di prodotti nuovi n.c.a.",
            Category.SUBCLASS,
        ),
        Classification("H", "TRASPORTO E MAGAZZINAGGIO", Category.SECTION),
        Classification("49", "Trasporto terrestre e trasporto mediante condotte", Category.DIVISION),
        Classification("49.1", "Trasporto ferroviario di passeggeri", Category.GROUP),
        Classification("49.11", "Trasporto di passeggeri su ferrovia pesante", Category.CLASS),
        Classification("49.11.0", "Trasporto di passeggeri su ferrovia pesante", Category.SUBCLASS),
        Classification("49.11.00", "Trasporto di passeggeri su ferrovia pesante", Category.SUBCLASS),
        Classification("49.12", "Altri trasporti ferroviari di passeggeri", Category.CLASS),
        Classification("49.12.0", "Altri trasporti ferroviari di passeggeri", Category.SUBCLASS),
        Classification("49.12.00", "Altri trasporti ferroviari di passeggeri", Category.SUBCLASS),
        Classification("49.2", "Trasporto ferroviario di merci", Category.GROUP),
        Classification("49.20", "Trasporto ferroviario di merci", Category.CLASS),
        Classification("49.20.0", "Trasporto ferroviario di merci", Category.SUBCLASS),
        Classification("49.20.00", "Trasporto ferroviario di merci", Category.SUBCLASS),
        Classification("49.3", "Altri trasporti terrestri di passeggeri", Category.GROUP),
        Classification("49.31", "Trasporto di linea di passeggeri su strada", Category.CLASS),
        Classification("49.31.0", "Trasporto di linea di passeggeri su strada", Category.SUBCLASS),
        Classification(
            "49.31.01",
            "Trasporto di linea di passeggeri su strada specializzato per visite turistiche",
            Category.SUBCLASS,
        ),
        Classification("49.31.02", "Altri trasporti di linea di passeggeri su strada", Category.SUBCLASS),
        Classification("49.32", "Trasporto non di linea di passeggeri su strada", Category.CLASS),
        Classification("49.32.0", "Trasporto non di linea di passeggeri su strada", Category.SUBCLASS),
        Classification(
            "49.32.01",
            "Trasporto non di linea di passeggeri su strada specializzato per visite turistiche",
            Category.SUBCLASS,
        ),
        Classification("49.32.02", "Altri trasporti non di linea di passeggeri su strada", Category.SUBCLASS),
        Classification("49.33", "Trasporto di passeggeri a richiesta su veicoli con conducente", Category.CLASS),
        Classification("49.33.1", "Trasporto su taxi", Category.SUBCLASS),
        Classification("49.33.10", "Trasporto su taxi", Category.SUBCLASS),
        Classification("49.33.2", "Trasporto su veicoli a noleggio con conducente", Category.SUBCLASS),
        Classification("49.33.20", "Trasporto su veicoli a noleggio con conducente", Category.SUBCLASS),
        Classification("49.34", "Trasporto di passeggeri mediante funivie e sciovie", Category.CLASS),
        Classification("49.34.0", "Trasporto di passeggeri mediante funivie e sciovie", Category.SUBCLASS),
        Classification("49.34.00", "Trasporto di passeggeri mediante funivie e sciovie", Category.SUBCLASS),
        Classification("49.39", "Altri trasporti terrestri di passeggeri n.c.a.", Category.CLASS),
        Classification("49.39.0", "Altri trasporti terrestri di passeggeri n.c.a.", Category.SUBCLASS),
        Classification("49.39.00", "Altri trasporti terrestri di passeggeri n.c.a.", Category.SUBCLASS),
        Classification("49.4", "Trasporto di merci su strada e servizi di trasloco", Category.GROUP),
        Classification("49.41", "Trasporto di merci su strada", Category.CLASS),
        Classification("49.41.0", "Trasporto di merci su strada", Category.SUBCLASS),
        Classification("49.41.00", "Trasporto di merci su strada", Category.SUBCLASS),
        Classification("49.42", "Servizi di trasloco", Category.CLASS),
        Classification("49.42.0", "Servizi di trasloco", Category.SUBCLASS),
        Classification("49.42.00", "Servizi di trasloco", Category.SUBCLASS),
        Classification("49.5", "Trasporto mediante condotte", Category.GROUP),
        Classification("49.50", "Trasporto mediante condotte", Category.CLASS),
        Classification("49.50.1", "Trasporto mediante condotte di gas", Category.SUBCLASS),
        Classification("49.50.10", "Trasporto mediante condotte di gas", Category.SUBCLASS),
        Classification("49.50.2", "Trasporto mediante condotte di liquidi", Category.SUBCLASS),
        Classification("49.50.20", "Trasporto mediante condotte di liquidi", Category.SUBCLASS),
        Classification("50", "Trasporto marittimo e per vie d'acqua interne", Category.DIVISION),
        Classification("50.1", "Trasporto marittimo e costiero di passeggeri", Category.GROUP),
        Classification("50.10", "Trasporto marittimo e costiero di passeggeri", Category.CLASS),
        Classification("50.10.0", "Trasporto marittimo e costiero di passeggeri", Category.SUBCLASS),
        Classification("50.10.00", "Trasporto marittimo e costiero di passeggeri", Category.SUBCLASS),
        Classification("50.2", "Trasporto marittimo e costiero di merci", Category.GROUP),
        Classification("50.20", "Trasporto marittimo e costiero di merci", Category.CLASS),
        Classification("50.20.0", "Trasporto marittimo e costiero di merci", Category.SUBCLASS),
        Classification("50.20.00", "Trasporto marittimo e costiero di merci", Category.SUBCLASS),
        Classification("50.3", "Trasporto per vie d'acqua interne di passeggeri", Category.GROUP),
        Classification("50.30", "Trasporto per vie d'acqua interne di passeggeri", Category.CLASS),
        Classification("50.30.0", "Trasporto per vie d'acqua interne di passeggeri", Category.SUBCLASS),
        Classification("50.30.00", "Trasporto per vie d'acqua interne di passeggeri", Category.SUBCLASS),
        Classification("50.4", "Trasporto per vie d'acqua interne di merci", Category.GROUP),
        Classification("50.40", "Trasporto per vie d'acqua interne di merci", Category.CLASS),
        Classification("50.40.0", "Trasporto per vie d'acqua interne di merci", Category.SUBCLASS),
        Classification("50.40.00", "Trasporto per vie d'acqua interne di merci", Category.SUBCLASS),
        Classification("51", "Trasporto aereo", Category.DIVISION),
        Classification("51.1", "Trasporto aereo di passeggeri", Category.GROUP),
        Classification("51.10", "Trasporto aereo di passeggeri", Category.CLASS),
        Classification("51.10.1", "Trasporto aereo di linea di passeggeri", Category.SUBCLASS),
        Classification("51.10.10", "Trasporto aereo di linea di passeggeri", Category.SUBCLASS),
        Classification("51.10.2", "Trasporto aereo non di linea di passeggeri", Category.SUBCLASS),
        Classification("51.10.20", "Trasporto aereo non di linea di passeggeri", Category.SUBCLASS),
        Classification("51.2", "Trasporto aereo di merci e trasporto spaziale", Category.GROUP),
        Classification("51.21", "Trasporto aereo di merci", Category.CLASS),
        Classification("51.21.0", "Trasporto aereo di merci", Category.SUBCLASS),
        Classification("51.21.00", "Trasporto aereo di merci", Category.SUBCLASS),
        Classification("51.22", "Trasporto spaziale", Category.CLASS),
        Classification("51.22.0", "Trasporto spaziale", Category.SUBCLASS),
        Classification("51.22.00", "Trasporto spaziale", Category.SUBCLASS),
        Classification("52", "Magazzinaggio, deposito e attività di supporto ai trasporti", Category.DIVISION),
        Classification("52.1", "Magazzinaggio e deposito", Category.GROUP),
        Classification("52.10", "Magazzinaggio e deposito", Category.CLASS),
        Classification("52.10.1", "Magazzinaggio e deposito non refrigerato", Category.SUBCLASS),
        Classification("52.10.10", "Magazzinaggio e deposito non refrigerato", Category.SUBCLASS),
        Classification("52.10.2", "Magazzinaggio e deposito refrigerato", Category.SUBCLASS),
        Classification("52.10.20", "Magazzinaggio e deposito refrigerato", Category.SUBCLASS),
        Classification("52.2", "Attività di supporto ai trasporti", Category.GROUP),
        Classification("52.21", "Servizi di supporto al trasporto terrestre", Category.CLASS),
        Classification("52.21.1", "Gestione di infrastrutture ferroviarie", Category.SUBCLASS),
        Classification("52.21.10", "Gestione di infrastrutture ferroviarie", Category.SUBCLASS),
        Classification("52.21.2", "Gestione e manutenzione di strade", Category.SUBCLASS),
        Classification("52.21.20", "Gestione e manutenzione di strade", Category.SUBCLASS),
        Classification("52.21.3", "Gestione di stazioni per autobus", Category.SUBCLASS),
        Classification("52.21.30", "Gestione di stazioni per autobus", Category.SUBCLASS),
        Classification("52.21.4", "Gestione di centri di movimentazione merci", Category.SUBCLASS),
        Classification("52.21.40", "Gestione di centri di movimentazione merci", Category.SUBCLASS),
        Classification("52.21.5", "Gestione di parcheggi e autorimesse", Category.SUBCLASS),
        Classification("52.21.50", "Gestione di parcheggi e autorimesse", Category.SUBCLASS),
        Classification("52.21.6", "Attività di traino e soccorso stradale", Category.SUBCLASS),
        Classification("52.21.60", "Attività di traino e soccorso stradale", Category.SUBCLASS),
        Classification("52.21.9", "Altri servizi di supporto al trasporto terrestre", Category.SUBCLASS),
        Classification("52.21.90", "Altri servizi di supporto al trasporto terrestre", Category.SUBCLASS),
        Classification("52.22", "Servizi di supporto al trasporto marittimo e per vie d'acqua interne", Category.CLASS),
        Classification(
            "52.22.0", "Servizi di supporto al trasporto marittimo e per vie d'acqua interne", Category.SUBCLASS
        ),
        Classification(
            "52.22.01",
            "Liquefazione e rigassificazione di gas a scopo di trasporto marittimo e per vie d'acqua interne",
            Category.SUBCLASS,
        ),
        Classification(
            "52.22.09", "Altri servizi di supporto al trasporto marittimo e per vie d'acqua interne", Category.SUBCLASS
        ),
        Classification("52.23", "Servizi di supporto al trasporto aereo", Category.CLASS),
        Classification("52.23.0", "Servizi di supporto al trasporto aereo", Category.SUBCLASS),
        Classification("52.23.00", "Servizi di supporto al trasporto aereo", Category.SUBCLASS),
        Classification("52.24", "Movimentazione merci", Category.CLASS),
        Classification("52.24.1", "Movimentazione merci relativa a trasporti aerei", Category.SUBCLASS),
        Classification("52.24.10", "Movimentazione merci relativa a trasporti aerei", Category.SUBCLASS),
        Classification(
            "52.24.2",
            "Movimentazione merci relativa a trasporti marittimi e per vie d'acqua interne",
            Category.SUBCLASS,
        ),
        Classification(
            "52.24.20",
            "Movimentazione merci relativa a trasporti marittimi e per vie d'acqua interne",
            Category.SUBCLASS,
        ),
        Classification("52.24.3", "Movimentazione merci relativa a trasporti ferroviari", Category.SUBCLASS),
        Classification("52.24.30", "Movimentazione merci relativa a trasporti ferroviari", Category.SUBCLASS),
        Classification("52.24.4", "Movimentazione merci relativa ad altri trasporti terrestri", Category.SUBCLASS),
        Classification("52.24.40", "Movimentazione merci relativa ad altri trasporti terrestri", Category.SUBCLASS),
        Classification("52.25", "Servizi di logistica", Category.CLASS),
        Classification("52.25.0", "Servizi di logistica", Category.SUBCLASS),
        Classification("52.25.01", "Servizi di logistica per opere d'arte", Category.SUBCLASS),
        Classification("52.25.09", "Altri servizi di logistica", Category.SUBCLASS),
        Classification("52.26", "Altre attività di supporto ai trasporti", Category.CLASS),
        Classification("52.26.0", "Altre attività di supporto ai trasporti", Category.SUBCLASS),
        Classification("52.26.01", "Attività di agenti e agenzie di dogana", Category.SUBCLASS),
        Classification("52.26.02", "Attività di spedizione merci", Category.SUBCLASS),
        Classification("52.3", "Attività di servizi di intermediazione per il trasporto", Category.GROUP),
        Classification("52.31", "Attività di servizi di intermediazione per il trasporto di merci", Category.CLASS),
        Classification(
            "52.31.0", "Attività di servizi di intermediazione per il trasporto di merci", Category.SUBCLASS
        ),
        Classification(
            "52.31.00", "Attività di servizi di intermediazione per il trasporto di merci", Category.SUBCLASS
        ),
        Classification(
            "52.32", "Attività di servizi di intermediazione per il trasporto di passeggeri", Category.CLASS
        ),
        Classification(
            "52.32.0", "Attività di servizi di intermediazione per il trasporto di passeggeri", Category.SUBCLASS
        ),
        Classification(
            "52.32.00", "Attività di servizi di intermediazione per il trasporto di passeggeri", Category.SUBCLASS
        ),
        Classification("53", "Attività postali e di corriere", Category.DIVISION),
        Classification("53.1", "Attività postali con obbligo di servizio universale", Category.GROUP),
        Classification("53.10", "Attività postali con obbligo di servizio universale", Category.CLASS),
        Classification("53.10.0", "Attività postali con obbligo di servizio universale", Category.SUBCLASS),
        Classification("53.10.00", "Attività postali con obbligo di servizio universale", Category.SUBCLASS),
        Classification("53.2", "Altre attività postali e di corriere", Category.GROUP),
        Classification("53.20", "Altre attività postali e di corriere", Category.CLASS),
        Classification("53.20.0", "Altre attività postali e di corriere", Category.SUBCLASS),
        Classification("53.20.00", "Altre attività postali e di corriere", Category.SUBCLASS),
        Classification(
            "53.3", "Attività di servizi di intermediazione per attività postali e di corriere", Category.GROUP
        ),
        Classification(
            "53.30", "Attività di servizi di intermediazione per attività postali e di corriere", Category.CLASS
        ),
        Classification(
            "53.30.0", "Attività di servizi di intermediazione per attività postali e di corriere", Category.SUBCLASS
        ),
        Classification(
            "53.30.00", "Attività di servizi di intermediazione per attività postali e di corriere", Category.SUBCLASS
        ),
        Classification("I", "ATTIVITÀ DEI SERVIZI DI ALLOGGIO E DI RISTORAZIONE", Category.SECTION),
        Classification("55", "Servizi di alloggio", Category.DIVISION),
        Classification("55.1", "Servizi di alloggio di alberghi e simili", Category.GROUP),
        Classification("55.10", "Servizi di alloggio di alberghi e simili", Category.CLASS),
        Classification("55.10.0", "Servizi di alloggio di alberghi e simili", Category.SUBCLASS),
        Classification("55.10.00", "Servizi di alloggio di alberghi e simili", Category.SUBCLASS),
        Classification("55.2", "Servizi di alloggio per vacanze e altri soggiorni di breve durata", Category.GROUP),
        Classification("55.20", "Servizi di alloggio per vacanze e altri soggiorni di breve durata", Category.CLASS),
        Classification("55.20.1", "Ostelli", Category.SUBCLASS),
        Classification("55.20.10", "Ostelli", Category.SUBCLASS),
        Classification("55.20.2", "Rifugi e baite di montagna", Category.SUBCLASS),
        Classification("55.20.20", "Rifugi e baite di montagna", Category.SUBCLASS),
        Classification("55.20.3", "Case religiose e sociali di ospitalità", Category.SUBCLASS),
        Classification("55.20.31", "Case religiose di ospitalità", Category.SUBCLASS),
        Classification("55.20.32", "Altre case sociali di ospitalità", Category.SUBCLASS),
        Classification(
            "55.20.4",
            "Bed and breakfast, servizi di alloggio in camere, case e appartamenti per vacanze",
            Category.SUBCLASS,
        ),
        Classification("55.20.41", "Bed and breakfast", Category.SUBCLASS),
        Classification("55.20.42", "Servizi di alloggio in camere, case e appartamenti per vacanze", Category.SUBCLASS),
        Classification("55.20.5", "Servizi di alloggio in aziende agricole e ittiche", Category.SUBCLASS),
        Classification("55.20.51", "Servizi di alloggio in aziende agricole", Category.SUBCLASS),
        Classification("55.20.52", "Servizi di alloggio in aziende ittiche", Category.SUBCLASS),
        Classification(
            "55.3", "Servizi di aree di campeggio e aree attrezzate per veicoli ricreazionali", Category.GROUP
        ),
        Classification(
            "55.30", "Servizi di aree di campeggio e aree attrezzate per veicoli ricreazionali", Category.CLASS
        ),
        Classification(
            "55.30.0", "Servizi di aree di campeggio e aree attrezzate per veicoli ricreazionali", Category.SUBCLASS
        ),
        Classification("55.30.01", "Campeggi", Category.SUBCLASS),
        Classification("55.30.02", "Villaggi turistici e alloggi glamping", Category.SUBCLASS),
        Classification("55.30.03", "Aree attrezzate per veicoli ricreazionali", Category.SUBCLASS),
        Classification("55.30.04", "Marina resort", Category.SUBCLASS),
        Classification("55.4", "Attività di servizi di intermediazione per servizi di alloggio", Category.GROUP),
        Classification("55.40", "Attività di servizi di intermediazione per servizi di alloggio", Category.CLASS),
        Classification("55.40.0", "Attività di servizi di intermediazione per servizi di alloggio", Category.SUBCLASS),
        Classification("55.40.00", "Attività di servizi di intermediazione per servizi di alloggio", Category.SUBCLASS),
        Classification("55.9", "Altri servizi di alloggio", Category.GROUP),
        Classification("55.90", "Altri servizi di alloggio", Category.CLASS),
        Classification("55.90.0", "Altri servizi di alloggio", Category.SUBCLASS),
        Classification("55.90.00", "Altri servizi di alloggio", Category.SUBCLASS),
        Classification("56", "Attività di servizi di ristorazione", Category.DIVISION),
        Classification("56.1", "Attività di ristoranti e di servizi di ristorazione mobile", Category.GROUP),
        Classification("56.11", "Attività di ristoranti", Category.CLASS),
        Classification("56.11.1", "Attività di ristoranti, escluse gelaterie e pasticcerie", Category.SUBCLASS),
        Classification(
            "56.11.11",
            "Attività di ristoranti con servizio al tavolo, escluse gelaterie e pasticcerie ",
            Category.SUBCLASS,
        ),
        Classification(
            "56.11.12",
            "Attività di ristoranti senza servizio al tavolo o da asporto, escluse gelaterie e pasticcerie",
            Category.SUBCLASS,
        ),
        Classification("56.11.2", "Attività di gelaterie e pasticcerie", Category.SUBCLASS),
        Classification("56.11.21", "Attività di gelaterie con servizio al tavolo", Category.SUBCLASS),
        Classification("56.11.22", "Attività di gelaterie senza servizio al tavolo o da asporto", Category.SUBCLASS),
        Classification("56.11.23", "Attività di pasticcerie con servizio al tavolo", Category.SUBCLASS),
        Classification("56.11.24", "Attività di pasticcerie senza servizio al tavolo o da asporto", Category.SUBCLASS),
        Classification("56.11.9", "Attività di ristoranti n.c.a.", Category.SUBCLASS),
        Classification("56.11.91", "Attività di ristoranti connesse alle aziende agricole", Category.SUBCLASS),
        Classification("56.11.92", "Attività di ristoranti connesse alle aziende ittiche", Category.SUBCLASS),
        Classification("56.11.93", "Attività di ristoranti a bordo di mezzi di trasporto", Category.SUBCLASS),
        Classification("56.12", "Attività di servizi di ristorazione mobile", Category.CLASS),
        Classification("56.12.0", "Attività di servizi di ristorazione mobile", Category.SUBCLASS),
        Classification(
            "56.12.01",
            "Attività di servizi di ristorazione mobile di ristoranti e altri esercizi di ristorazione simili",
            Category.SUBCLASS,
        ),
        Classification("56.12.02", "Attività di servizi di ristorazione mobile di gelaterie", Category.SUBCLASS),
        Classification("56.12.03", "Attività di servizi di ristorazione mobile di pasticcerie", Category.SUBCLASS),
        Classification(
            "56.2",
            "Attività di servizi di catering per eventi, catering su base contrattuale e altri servizi di ristorazione",
            Category.GROUP,
        ),
        Classification("56.21", "Attività di catering per eventi", Category.CLASS),
        Classification("56.21.0", "Attività di catering per eventi", Category.SUBCLASS),
        Classification("56.21.01", "Attività di catering per eventi presso location dei clienti", Category.SUBCLASS),
        Classification("56.21.02", "Attività di catering per eventi presso sale per banchetti", Category.SUBCLASS),
        Classification(
            "56.22",
            "Attività di servizi di catering su base contrattuale e altri servizi di ristorazione",
            Category.CLASS,
        ),
        Classification(
            "56.22.0",
            "Attività di servizi di catering su base contrattuale e altri servizi di ristorazione",
            Category.SUBCLASS,
        ),
        Classification("56.22.01", "Attività di servizi di catering su base contrattuale", Category.SUBCLASS),
        Classification("56.22.02", "Altri servizi di ristorazione", Category.SUBCLASS),
        Classification("56.3", "Attività di somministrazione di bevande", Category.GROUP),
        Classification("56.30", "Attività di somministrazione di bevande", Category.CLASS),
        Classification("56.30.0", "Attività di somministrazione di bevande", Category.SUBCLASS),
        Classification("56.30.01", "Attività di somministrazione di bevande in bar e caffetterie", Category.SUBCLASS),
        Classification("56.30.02", "Attività di somministrazione di bevande in lounge cocktail bar", Category.SUBCLASS),
        Classification("56.30.03", "Attività di somministrazione mobile di bevande", Category.SUBCLASS),
        Classification(
            "56.30.04", "Attività di somministrazione di bevande a bordo di mezzi di trasporto", Category.SUBCLASS
        ),
        Classification("56.4", "Attività di servizi di intermediazione per servizi di ristorazione", Category.GROUP),
        Classification("56.40", "Attività di servizi di intermediazione per servizi di ristorazione", Category.CLASS),
        Classification(
            "56.40.0", "Attività di servizi di intermediazione per servizi di ristorazione", Category.SUBCLASS
        ),
        Classification(
            "56.40.00", "Attività di servizi di intermediazione per servizi di ristorazione", Category.SUBCLASS
        ),
        Classification(
            "J",
            "ATTIVITÀ EDITORIALI, TRASMISSIONI RADIOFONICHE E PRODUZIONE E DISTRIBUZIONE DI CONTENUTI",
            Category.SECTION,
        ),
        Classification("58", "Attività editoriali", Category.DIVISION),
        Classification(
            "58.1",
            "Edizione di libri, quotidiani e altre attività editoriali, esclusa l'edizione di software",
            Category.GROUP,
        ),
        Classification("58.11", "Edizione di libri", Category.CLASS),
        Classification("58.11.0", "Edizione di libri", Category.SUBCLASS),
        Classification("58.11.00", "Edizione di libri", Category.SUBCLASS),
        Classification("58.12", "Edizione di quotidiani", Category.CLASS),
        Classification("58.12.0", "Edizione di quotidiani", Category.SUBCLASS),
        Classification("58.12.00", "Edizione di quotidiani", Category.SUBCLASS),
        Classification("58.13", "Edizione di riviste e periodici", Category.CLASS),
        Classification("58.13.0", "Edizione di riviste e periodici", Category.SUBCLASS),
        Classification("58.13.00", "Edizione di riviste e periodici", Category.SUBCLASS),
        Classification("58.19", "Altre attività editoriali, esclusa l'edizione di software", Category.CLASS),
        Classification("58.19.0", "Altre attività editoriali, esclusa l'edizione di software", Category.SUBCLASS),
        Classification("58.19.00", "Altre attività editoriali, esclusa l'edizione di software", Category.SUBCLASS),
        Classification("58.2", "Edizione di software", Category.GROUP),
        Classification("58.21", "Edizione di videogiochi", Category.CLASS),
        Classification("58.21.0", "Edizione di videogiochi", Category.SUBCLASS),
        Classification("58.21.00", "Edizione di videogiochi", Category.SUBCLASS),
        Classification("58.29", "Edizione di altri software", Category.CLASS),
        Classification("58.29.0", "Edizione di altri software", Category.SUBCLASS),
        Classification("58.29.00", "Edizione di altri software", Category.SUBCLASS),
        Classification(
            "59",
            "Attività di produzione, post-produzione e distribuzione cinematografica, di video e programmi televisivi, di registrazioni musicali e sonore",
            Category.DIVISION,
        ),
        Classification(
            "59.1",
            "Attività di produzione, post-produzione e distribuzione cinematografica, di video e programmi televisivi",
            Category.GROUP,
        ),
        Classification(
            "59.11", "Attività di produzione cinematografica, di video e programmi televisivi", Category.CLASS
        ),
        Classification(
            "59.11.0", "Attività di produzione cinematografica, di video e programmi televisivi", Category.SUBCLASS
        ),
        Classification(
            "59.11.00", "Attività di produzione cinematografica, di video e programmi televisivi", Category.SUBCLASS
        ),
        Classification(
            "59.12", "Attività di post-produzione cinematografica, di video e programmi televisivi", Category.CLASS
        ),
        Classification(
            "59.12.0", "Attività di post-produzione cinematografica, di video e programmi televisivi", Category.SUBCLASS
        ),
        Classification(
            "59.12.00",
            "Attività di post-produzione cinematografica, di video e programmi televisivi",
            Category.SUBCLASS,
        ),
        Classification(
            "59.13", "Attività di distribuzione cinematografica, di video e programmi televisivi", Category.CLASS
        ),
        Classification(
            "59.13.0", "Attività di distribuzione cinematografica, di video e programmi televisivi", Category.SUBCLASS
        ),
        Classification(
            "59.13.00", "Attività di distribuzione cinematografica, di video e programmi televisivi", Category.SUBCLASS
        ),
        Classification("59.14", "Attività di proiezione cinematografica", Category.CLASS),
        Classification("59.14.0", "Attività di proiezione cinematografica", Category.SUBCLASS),
        Classification("59.14.00", "Attività di proiezione cinematografica", Category.SUBCLASS),
        Classification("59.2", "Attività di registrazione sonora e dell'editoria musicale", Category.GROUP),
        Classification("59.20", "Attività di registrazione sonora e dell'editoria musicale", Category.CLASS),
        Classification("59.20.1", "Attività di registrazione sonora", Category.SUBCLASS),
        Classification("59.20.10", "Attività di registrazione sonora", Category.SUBCLASS),
        Classification("59.20.2", "Editoria musicale", Category.SUBCLASS),
        Classification("59.20.20", "Editoria musicale", Category.SUBCLASS),
        Classification(
            "60",
            "Attività di programmazione, trasmissione, agenzie di stampa e altre attività di distribuzione di contenuti",
            Category.DIVISION,
        ),
        Classification("60.1", "Attività di trasmissione radiofonica e distribuzione di audio", Category.GROUP),
        Classification("60.10", "Attività di trasmissione radiofonica e distribuzione di audio", Category.CLASS),
        Classification("60.10.0", "Attività di trasmissione radiofonica e distribuzione di audio", Category.SUBCLASS),
        Classification("60.10.00", "Attività di trasmissione radiofonica e distribuzione di audio", Category.SUBCLASS),
        Classification(
            "60.2", "Attività di programmazione e trasmissione televisive e di distribuzione di video", Category.GROUP
        ),
        Classification(
            "60.20", "Attività di programmazione e trasmissione televisive e di distribuzione di video", Category.CLASS
        ),
        Classification(
            "60.20.0",
            "Attività di programmazione e trasmissione televisive e di distribuzione di video",
            Category.SUBCLASS,
        ),
        Classification(
            "60.20.00",
            "Attività di programmazione e trasmissione televisive e di distribuzione di video",
            Category.SUBCLASS,
        ),
        Classification(
            "60.3", "Attività delle agenzie di stampa e altre attività di distribuzione di contenuti", Category.GROUP
        ),
        Classification("60.31", "Attività delle agenzie di stampa", Category.CLASS),
        Classification("60.31.0", "Attività delle agenzie di stampa", Category.SUBCLASS),
        Classification("60.31.00", "Attività delle agenzie di stampa", Category.SUBCLASS),
        Classification("60.39", "Altre attività di distribuzione di contenuti", Category.CLASS),
        Classification("60.39.0", "Altre attività di distribuzione di contenuti", Category.SUBCLASS),
        Classification("60.39.00", "Altre attività di distribuzione di contenuti", Category.SUBCLASS),
        Classification(
            "K",
            "TELECOMUNICAZIONI, PROGRAMMAZIONE E CONSULENZA INFORMATICA, INFRASTRUTTURE INFORMATICHE E ALTRE ATTIVITÀ DEI SERVIZI D'INFORMAZIONE",
            Category.SECTION,
        ),
        Classification("61", "Telecomunicazioni", Category.DIVISION),
        Classification("61.1", "Attività di telecomunicazioni fisse, mobili e satellitari", Category.GROUP),
        Classification("61.10", "Attività di telecomunicazioni fisse, mobili e satellitari", Category.CLASS),
        Classification("61.10.0", "Attività di telecomunicazioni fisse, mobili e satellitari", Category.SUBCLASS),
        Classification("61.10.01", "Attività di telecomunicazioni fisse", Category.SUBCLASS),
        Classification("61.10.02", "Attività di telecomunicazioni mobili", Category.SUBCLASS),
        Classification("61.10.03", "Attività di telecomunicazioni satellitari", Category.SUBCLASS),
        Classification(
            "61.2",
            "Attività di rivendita di telecomunicazioni e attività di servizi di intermediazione per telecomunicazioni",
            Category.GROUP,
        ),
        Classification(
            "61.20",
            "Attività di rivendita di telecomunicazioni e attività di servizi di intermediazione per telecomunicazioni",
            Category.CLASS,
        ),
        Classification(
            "61.20.0",
            "Attività di rivendita di telecomunicazioni e attività di servizi di intermediazione per telecomunicazioni",
            Category.SUBCLASS,
        ),
        Classification(
            "61.20.00",
            "Attività di rivendita di telecomunicazioni e attività di servizi di intermediazione per telecomunicazioni",
            Category.SUBCLASS,
        ),
        Classification("61.9", "Altre attività di telecomunicazioni", Category.GROUP),
        Classification("61.90", "Altre attività di telecomunicazioni", Category.CLASS),
        Classification("61.90.1", "Erogazione di servizi di accesso a Internet", Category.SUBCLASS),
        Classification("61.90.10", "Erogazione di servizi di accesso a Internet", Category.SUBCLASS),
        Classification("61.90.2", "Erogazione di servizi di messaggistica e di notifica", Category.SUBCLASS),
        Classification("61.90.20", "Erogazione di servizi di messaggistica e di notifica", Category.SUBCLASS),
        Classification("61.90.9", "Altre attività di telecomunicazioni n.c.a.", Category.SUBCLASS),
        Classification("61.90.90", "Altre attività di telecomunicazioni n.c.a.", Category.SUBCLASS),
        Classification(
            "62", "Attività di programmazione, consulenza informatica e attività connesse", Category.DIVISION
        ),
        Classification("62.1", "Attività di programmazione informatica", Category.GROUP),
        Classification("62.10", "Attività di programmazione informatica", Category.CLASS),
        Classification("62.10.0", "Attività di programmazione informatica", Category.SUBCLASS),
        Classification("62.10.00", "Attività di programmazione informatica", Category.SUBCLASS),
        Classification(
            "62.2", "Attività di consulenza informatica e di gestione di strutture informatiche", Category.GROUP
        ),
        Classification(
            "62.20", "Attività di consulenza informatica e di gestione di strutture informatiche", Category.CLASS
        ),
        Classification("62.20.1", "Attività di consulenza informatica", Category.SUBCLASS),
        Classification("62.20.10", "Attività di consulenza informatica", Category.SUBCLASS),
        Classification("62.20.2", "Attività di gestione di strutture informatiche", Category.SUBCLASS),
        Classification("62.20.20", "Attività di gestione di strutture informatiche", Category.SUBCLASS),
        Classification(
            "62.9",
            "Altre attività dei servizi connessi alle tecnologie dell'informazione e dell'informatica",
            Category.GROUP,
        ),
        Classification(
            "62.90",
            "Altre attività dei servizi connessi alle tecnologie dell'informazione e dell'informatica",
            Category.CLASS,
        ),
        Classification(
            "62.90.0",
            "Altre attività dei servizi connessi alle tecnologie dell'informazione e dell'informatica",
            Category.SUBCLASS,
        ),
        Classification("62.90.01", "Configurazione di personal computer", Category.SUBCLASS),
        Classification(
            "62.90.09",
            "Altre attività dei servizi connessi alle tecnologie dell'informazione e dell'informatica n.c.a.",
            Category.SUBCLASS,
        ),
        Classification(
            "63",
            "Infrastrutture informatiche, elaborazione dati, hosting e altri servizi di informazione",
            Category.DIVISION,
        ),
        Classification(
            "63.1", "Infrastrutture informatiche, elaborazione dati, hosting e attività connesse", Category.GROUP
        ),
        Classification(
            "63.10", "Infrastrutture informatiche, elaborazione dati, hosting e attività connesse", Category.CLASS
        ),
        Classification(
            "63.10.1", "Fornitura di infrastrutture informatiche, hosting e attività connesse", Category.SUBCLASS
        ),
        Classification(
            "63.10.10", "Fornitura di infrastrutture informatiche, hosting e attività connesse", Category.SUBCLASS
        ),
        Classification("63.10.2", "Elaborazione dati", Category.SUBCLASS),
        Classification("63.10.21", "Elaborazione dati contabili", Category.SUBCLASS),
        Classification("63.10.29", "Elaborazione altri dati", Category.SUBCLASS),
        Classification(
            "63.9", "Attività dei portali di ricerca web e altre attività dei servizi di informazione", Category.GROUP
        ),
        Classification("63.91", "Attività dei portali di ricerca sul web", Category.CLASS),
        Classification("63.91.0", "Attività dei portali di ricerca sul web", Category.SUBCLASS),
        Classification("63.91.00", "Attività dei portali di ricerca sul web", Category.SUBCLASS),
        Classification("63.92", "Altre attività dei servizi di informazione", Category.CLASS),
        Classification("63.92.0", "Altre attività dei servizi di informazione", Category.SUBCLASS),
        Classification("63.92.00", "Altre attività dei servizi di informazione", Category.SUBCLASS),
        Classification("L", "ATTIVITÀ FINANZIARIE E ASSICURATIVE", Category.SECTION),
        Classification(
            "64", "Attività dei servizi finanziari, escluse le assicurazioni e i fondi pensione", Category.DIVISION
        ),
        Classification("64.1", "Intermediazione monetaria", Category.GROUP),
        Classification("64.11", "Attività delle banche centrali", Category.CLASS),
        Classification("64.11.0", "Attività delle banche centrali", Category.SUBCLASS),
        Classification("64.11.00", "Attività delle banche centrali", Category.SUBCLASS),
        Classification("64.19", "Altre intermediazioni monetarie", Category.CLASS),
        Classification(
            "64.19.1",
            "Altre intermediazioni monetarie fornite da istituti monetari diversi dalla banca centrale",
            Category.SUBCLASS,
        ),
        Classification(
            "64.19.10",
            "Altre intermediazioni monetarie fornite da istituti monetari diversi dalla banca centrale",
            Category.SUBCLASS,
        ),
        Classification(
            "64.19.2", "Altre intermediazioni monetarie fornite da istituti di moneta elettronica", Category.SUBCLASS
        ),
        Classification(
            "64.19.20", "Altre intermediazioni monetarie fornite da istituti di moneta elettronica", Category.SUBCLASS
        ),
        Classification(
            "64.19.3", "Altre intermediazioni monetarie fornite da Cassa Depositi e Prestiti (CDP)", Category.SUBCLASS
        ),
        Classification(
            "64.19.30", "Altre intermediazioni monetarie fornite da Cassa Depositi e Prestiti (CDP)", Category.SUBCLASS
        ),
        Classification(
            "64.2", "Attività delle società di partecipazione (holding) e dei conduit di finanziamento", Category.GROUP
        ),
        Classification("64.21", "Attività delle società di partecipazione (holding)", Category.CLASS),
        Classification("64.21.0", "Attività delle società di partecipazione (holding)", Category.SUBCLASS),
        Classification("64.21.00", "Attività delle società di partecipazione (holding)", Category.SUBCLASS),
        Classification("64.22", "Attività dei conduit di finanziamento", Category.CLASS),
        Classification("64.22.0", "Attività dei conduit di finanziamento", Category.SUBCLASS),
        Classification("64.22.00", "Attività dei conduit di finanziamento", Category.SUBCLASS),
        Classification("64.3", "Attività delle società fiduciarie, dei fondi e altre entità simili", Category.GROUP),
        Classification(
            "64.31",
            "Attività dei fondi di investimento del mercato monetario e del mercato non monetario",
            Category.CLASS,
        ),
        Classification(
            "64.31.0",
            "Attività dei fondi di investimento del mercato monetario e del mercato non monetario",
            Category.SUBCLASS,
        ),
        Classification(
            "64.31.00",
            "Attività dei fondi di investimento del mercato monetario e del mercato non monetario",
            Category.SUBCLASS,
        ),
        Classification(
            "64.32", "Attività di conti fiduciari, per la gestione dell'eredità e di agenzia", Category.CLASS
        ),
        Classification(
            "64.32.0", "Attività di conti fiduciari, per la gestione dell'eredità e di agenzia", Category.SUBCLASS
        ),
        Classification(
            "64.32.00", "Attività di conti fiduciari, per la gestione dell'eredità e di agenzia", Category.SUBCLASS
        ),
        Classification(
            "64.9",
            "Altre attività di servizi finanziari, ad esclusione di assicurazioni e fondi pensione",
            Category.GROUP,
        ),
        Classification("64.91", "Leasing finanziario", Category.CLASS),
        Classification("64.91.0", "Leasing finanziario", Category.SUBCLASS),
        Classification("64.91.00", "Leasing finanziario", Category.SUBCLASS),
        Classification("64.92", "Altre attività creditizie", Category.CLASS),
        Classification("64.92.1", "Attività di factoring", Category.SUBCLASS),
        Classification("64.92.10", "Attività di factoring", Category.SUBCLASS),
        Classification("64.92.9", "Altre attività di concessione del credito n.c.a.", Category.SUBCLASS),
        Classification(
            "64.92.91",
            "Altre attività di concessione del credito fornite dai consorzi di garanzia collettiva fidi",
            Category.SUBCLASS,
        ),
        Classification("64.92.99", "Altre attività varie di concessione del credito n.c.a.", Category.SUBCLASS),
        Classification(
            "64.99",
            "Altre attività di servizi finanziari, ad esclusione di assicurazioni e fondi pensione n.c.a.",
            Category.CLASS,
        ),
        Classification(
            "64.99.0",
            "Altre attività di servizi finanziari, ad esclusione di assicurazioni e fondi pensione n.c.a.",
            Category.SUBCLASS,
        ),
        Classification(
            "64.99.00",
            "Altre attività di servizi finanziari, ad esclusione di assicurazioni e fondi pensione n.c.a.",
            Category.SUBCLASS,
        ),
        Classification(
            "65",
            "Assicurazioni, riassicurazioni e fondi pensione, escluse le assicurazioni sociali obbligatorie",
            Category.DIVISION,
        ),
        Classification("65.1", "Assicurazioni", Category.GROUP),
        Classification("65.11", "Assicurazioni sulla vita", Category.CLASS),
        Classification("65.11.0", "Assicurazioni sulla vita", Category.SUBCLASS),
        Classification("65.11.00", "Assicurazioni sulla vita", Category.SUBCLASS),
        Classification("65.12", "Assicurazioni diverse da quelle sulla vita", Category.CLASS),
        Classification("65.12.0", "Assicurazioni diverse da quelle sulla vita", Category.SUBCLASS),
        Classification("65.12.00", "Assicurazioni diverse da quelle sulla vita", Category.SUBCLASS),
        Classification("65.2", "Riassicurazioni", Category.GROUP),
        Classification("65.20", "Riassicurazioni", Category.CLASS),
        Classification("65.20.0", "Riassicurazioni", Category.SUBCLASS),
        Classification("65.20.00", "Riassicurazioni", Category.SUBCLASS),
        Classification("65.3", "Fondi pensione", Category.GROUP),
        Classification("65.30", "Fondi pensione", Category.CLASS),
        Classification("65.30.0", "Fondi pensione", Category.SUBCLASS),
        Classification("65.30.00", "Fondi pensione", Category.SUBCLASS),
        Classification(
            "66", "Attività ausiliarie dei servizi finanziari e delle attività assicurative", Category.DIVISION
        ),
        Classification(
            "66.1",
            "Attività ausiliarie dei servizi finanziari, escluse le assicurazioni e i fondi pensione",
            Category.GROUP,
        ),
        Classification("66.11", "Amministrazione di mercati finanziari", Category.CLASS),
        Classification("66.11.0", "Amministrazione di mercati finanziari", Category.SUBCLASS),
        Classification("66.11.00", "Amministrazione di mercati finanziari", Category.SUBCLASS),
        Classification("66.12", "Attività di negoziazione di contratti relativi a titoli e merci", Category.CLASS),
        Classification("66.12.0", "Attività di negoziazione di contratti relativi a titoli e merci", Category.SUBCLASS),
        Classification(
            "66.12.00", "Attività di negoziazione di contratti relativi a titoli e merci", Category.SUBCLASS
        ),
        Classification(
            "66.19",
            "Altre attività ausiliarie dei servizi finanziari, escluse le assicurazioni e i fondi pensione",
            Category.CLASS,
        ),
        Classification(
            "66.19.1",
            "Attività di elaborazione e liquidazione delle transazioni finanziarie tramite carta di credito",
            Category.SUBCLASS,
        ),
        Classification(
            "66.19.10",
            "Attività di elaborazione e liquidazione delle transazioni finanziarie tramite carta di credito",
            Category.SUBCLASS,
        ),
        Classification("66.19.2", "Attività di consulenza finanziaria", Category.SUBCLASS),
        Classification(
            "66.19.21",
            "Attività di consulenza finanziaria fornite da consulenti finanziari abilitati all'offerta fuori sede",
            Category.SUBCLASS,
        ),
        Classification("66.19.22", "Altre attività di consulenza finanziaria", Category.SUBCLASS),
        Classification(
            "66.19.9",
            "Altre attività ausiliarie dei servizi finanziari n.c.a., escluse assicurazioni e fondi pensione",
            Category.SUBCLASS,
        ),
        Classification(
            "66.19.90",
            "Altre attività ausiliarie dei servizi finanziari n.c.a., escluse assicurazioni e fondi pensione",
            Category.SUBCLASS,
        ),
        Classification("66.2", "Attività ausiliarie delle assicurazioni e dei fondi pensione", Category.GROUP),
        Classification("66.21", "Valutazione dei rischi e dei danni", Category.CLASS),
        Classification("66.21.0", "Valutazione dei rischi e dei danni", Category.SUBCLASS),
        Classification("66.21.00", "Valutazione dei rischi e dei danni", Category.SUBCLASS),
        Classification("66.22", "Attività di agenti e intermediari delle assicurazioni", Category.CLASS),
        Classification("66.22.0", "Attività di agenti e intermediari delle assicurazioni", Category.SUBCLASS),
        Classification("66.22.00", "Attività di agenti e intermediari delle assicurazioni", Category.SUBCLASS),
        Classification("66.29", "Attività ausiliarie delle assicurazioni e dei fondi pensione n.c.a.", Category.CLASS),
        Classification(
            "66.29.0", "Attività ausiliarie delle assicurazioni e dei fondi pensione n.c.a.", Category.SUBCLASS
        ),
        Classification("66.29.01", "Attività di vigilanza su assicurazioni e fondi pensione", Category.SUBCLASS),
        Classification(
            "66.29.09", "Altre attività ausiliarie delle assicurazioni e dei fondi pensione n.c.a.", Category.SUBCLASS
        ),
        Classification("66.3", "Attività di gestione di fondi", Category.GROUP),
        Classification("66.30", "Attività di gestione di fondi", Category.CLASS),
        Classification("66.30.0", "Attività di gestione di fondi", Category.SUBCLASS),
        Classification(
            "66.30.01",
            "Gestione di organismi di investimento collettivo del risparmio, fondi pensione e portafogli",
            Category.SUBCLASS,
        ),
        Classification("66.30.02", "Servizi di gestione di trust", Category.SUBCLASS),
        Classification("66.30.03", "Servizi fiduciari e di custodia", Category.SUBCLASS),
        Classification("M", "ATTIVITÀ IMMOBILIARI", Category.SECTION),
        Classification("68", "Attività immobiliari", Category.DIVISION),
        Classification(
            "68.1", "Attività immobiliari su beni propri e sviluppo di progetti immobiliari", Category.GROUP
        ),
        Classification("68.11", "Compravendita di beni immobili effettuata su beni propri", Category.CLASS),
        Classification("68.11.0", "Compravendita di beni immobili effettuata su beni propri", Category.SUBCLASS),
        Classification("68.11.00", "Compravendita di beni immobili effettuata su beni propri", Category.SUBCLASS),
        Classification("68.12", "Sviluppo di progetti immobiliari", Category.CLASS),
        Classification("68.12.0", "Sviluppo di progetti immobiliari", Category.SUBCLASS),
        Classification("68.12.00", "Sviluppo di progetti immobiliari", Category.SUBCLASS),
        Classification("68.2", "Affitto e gestione di beni immobili propri o in locazione", Category.GROUP),
        Classification("68.20", "Affitto e gestione di beni immobili propri o in locazione", Category.CLASS),
        Classification("68.20.0", "Affitto e gestione di beni immobili propri o in locazione", Category.SUBCLASS),
        Classification(
            "68.20.01", "Affitto e gestione di terreni per telecomunicazioni propri o in locazione", Category.SUBCLASS
        ),
        Classification(
            "68.20.02",
            "Affitto e gestione di altri terreni ed edifici non residenziali, impianti e fabbriche propri o in locazione",
            Category.SUBCLASS,
        ),
        Classification(
            "68.20.09", "Affitto e gestione di beni immobili propri o in locazione n.c.a.", Category.SUBCLASS
        ),
        Classification("68.3", "Attività immobiliari per conto terzi", Category.GROUP),
        Classification("68.31", "Attività di servizi di intermediazione per attività immobiliari", Category.CLASS),
        Classification("68.31.0", "Attività di servizi di intermediazione per attività immobiliari", Category.SUBCLASS),
        Classification(
            "68.31.00", "Attività di servizi di intermediazione per attività immobiliari", Category.SUBCLASS
        ),
        Classification("68.32", "Altre attività immobiliari per conto terzi", Category.CLASS),
        Classification("68.32.0", "Altre attività immobiliari per conto terzi", Category.SUBCLASS),
        Classification("68.32.01", "Gestione di beni immobili per conto terzi", Category.SUBCLASS),
        Classification("68.32.09", "Altre attività immobiliari per conto terzi n.c.a.", Category.SUBCLASS),
        Classification("N", "ATTIVITÀ PROFESSIONALI, SCIENTIFICHE E TECNICHE", Category.SECTION),
        Classification("69", "Attività legali e di contabilità", Category.DIVISION),
        Classification("69.1", "Attività legali, giuridiche e notarili", Category.GROUP),
        Classification("69.10", "Attività legali, giuridiche e notarili", Category.CLASS),
        Classification("69.10.1", "Attività legali e giuridiche", Category.SUBCLASS),
        Classification("69.10.10", "Attività legali e giuridiche", Category.SUBCLASS),
        Classification("69.10.2", "Attività notarili", Category.SUBCLASS),
        Classification("69.10.20", "Attività notarili", Category.SUBCLASS),
        Classification(
            "69.10.3", "Attività di supporto alle attività legali, giuridiche e notarili", Category.SUBCLASS
        ),
        Classification(
            "69.10.30", "Attività di supporto alle attività legali, giuridiche e notarili", Category.SUBCLASS
        ),
        Classification(
            "69.2", "Attività di contabilità, controllo e revisione contabile; consulenza fiscale", Category.GROUP
        ),
        Classification(
            "69.20", "Attività di contabilità, controllo e revisione contabile; consulenza fiscale", Category.CLASS
        ),
        Classification(
            "69.20.0", "Attività di contabilità, controllo e revisione contabile; consulenza fiscale", Category.SUBCLASS
        ),
        Classification("69.20.01", "Attività di commercialisti", Category.SUBCLASS),
        Classification("69.20.02", "Attività di revisori legali in ambito contabile", Category.SUBCLASS),
        Classification("69.20.03", "Attività di esperti contabili", Category.SUBCLASS),
        Classification("69.20.04", "Attività di consulenti del lavoro", Category.SUBCLASS),
        Classification(
            "69.20.05",
            "Attività di altri soggetti simili in materia di contabilità delle retribuzioni e buste paga",
            Category.SUBCLASS,
        ),
        Classification(
            "69.20.06",
            "Attività di altri consulenti, periti e altri soggetti simili in ambito tributario e contabile",
            Category.SUBCLASS,
        ),
        Classification("69.20.07", "Attività di centri di assistenza fiscale", Category.SUBCLASS),
        Classification("70", "Attività di sedi centrali e consulenza gestionale", Category.DIVISION),
        Classification("70.1", "Attività di sedi centrali", Category.GROUP),
        Classification("70.10", "Attività di sedi centrali", Category.CLASS),
        Classification("70.10.0", "Attività di sedi centrali", Category.SUBCLASS),
        Classification("70.10.00", "Attività di sedi centrali", Category.SUBCLASS),
        Classification("70.2", "Consulenza imprenditoriale e altre attività di consulenza gestionale", Category.GROUP),
        Classification("70.20", "Consulenza imprenditoriale e altre attività di consulenza gestionale", Category.CLASS),
        Classification(
            "70.20.0", "Consulenza imprenditoriale e altre attività di consulenza gestionale", Category.SUBCLASS
        ),
        Classification("70.20.01", "Attività di consulenza in materia di logistica", Category.SUBCLASS),
        Classification("70.20.02", "Attività di certificazione di processi", Category.SUBCLASS),
        Classification(
            "70.20.09", "Consulenza imprenditoriale e altre attività di consulenza gestionale n.c.a.", Category.SUBCLASS
        ),
        Classification("71", "Attività di architettura e ingegneria; collaudi e analisi tecniche", Category.DIVISION),
        Classification(
            "71.1", "Attività di architettura, di ingegneria e altre consulenze tecniche connesse", Category.GROUP
        ),
        Classification("71.11", "Attività di architettura", Category.CLASS),
        Classification("71.11.0", "Attività di architettura", Category.SUBCLASS),
        Classification(
            "71.11.01", "Progettazione, pianificazione e supervisione di scavi archeologici", Category.SUBCLASS
        ),
        Classification("71.11.09", "Attività di architettura n.c.a.", Category.SUBCLASS),
        Classification("71.12", "Attività di ingegneria e altre consulenze tecniche connesse", Category.CLASS),
        Classification("71.12.1", "Attività di ingegneria", Category.SUBCLASS),
        Classification("71.12.10", "Attività di ingegneria", Category.SUBCLASS),
        Classification("71.12.2", "Gestione di progetti relativi a opere di ingegneria integrata", Category.SUBCLASS),
        Classification("71.12.20", "Gestione di progetti relativi a opere di ingegneria integrata", Category.SUBCLASS),
        Classification("71.12.3", "Elaborazione e supervisione di progetti da parte di geometri", Category.SUBCLASS),
        Classification("71.12.30", "Elaborazione e supervisione di progetti da parte di geometri", Category.SUBCLASS),
        Classification("71.12.4", "Attività di cartografia e aerofotogrammetria", Category.SUBCLASS),
        Classification("71.12.40", "Attività di cartografia e aerofotogrammetria", Category.SUBCLASS),
        Classification("71.12.5", "Attività di geologia, di prospezione geognostica e mineraria", Category.SUBCLASS),
        Classification("71.12.50", "Attività di geologia, di prospezione geognostica e mineraria", Category.SUBCLASS),
        Classification("71.2", "Collaudi e analisi tecniche", Category.GROUP),
        Classification("71.20", "Collaudi e analisi tecniche", Category.CLASS),
        Classification("71.20.1", "Collaudi e analisi tecniche di prodotti", Category.SUBCLASS),
        Classification("71.20.11", "Collaudi e analisi tecniche per indagini archeologiche", Category.SUBCLASS),
        Classification("71.20.19", "Altri collaudi e analisi tecniche di prodotti", Category.SUBCLASS),
        Classification("71.20.2", "Attività di controllo di qualità e certificazione di prodotti", Category.SUBCLASS),
        Classification("71.20.21", "Attività di riconoscimento dell'origine dei prodotti", Category.SUBCLASS),
        Classification(
            "71.20.22",
            "Revisione periodica a norma di legge dell'idoneità alla circolazione di autoveicoli e motocicli",
            Category.SUBCLASS,
        ),
        Classification(
            "71.20.29", "Altre attività di controllo di qualità e certificazione di prodotti", Category.SUBCLASS
        ),
        Classification("72", "Ricerca scientifica e sviluppo", Category.DIVISION),
        Classification(
            "72.1", "Ricerca e sviluppo sperimentale nel campo delle scienze naturali e dell'ingegneria", Category.GROUP
        ),
        Classification(
            "72.10",
            "Ricerca e sviluppo sperimentale nel campo delle scienze naturali e dell'ingegneria",
            Category.CLASS,
        ),
        Classification("72.10.1", "Ricerca e sviluppo sperimentale nel campo delle biotecnologie", Category.SUBCLASS),
        Classification("72.10.10", "Ricerca e sviluppo sperimentale nel campo delle biotecnologie", Category.SUBCLASS),
        Classification(
            "72.10.2",
            "Ricerca e sviluppo sperimentale nel campo delle altre scienze naturali e dell'ingegneria",
            Category.SUBCLASS,
        ),
        Classification("72.10.21", "Ricerca e sviluppo sperimentale nel campo della geologia", Category.SUBCLASS),
        Classification(
            "72.10.22",
            "Ricerca e sviluppo sperimentale nel campo della diagnostica per la conservazione dei beni culturali",
            Category.SUBCLASS,
        ),
        Classification(
            "72.10.29",
            "Ricerca e sviluppo sperimentale nel campo delle altre scienze naturali e dell'ingegneria n.c.a.",
            Category.SUBCLASS,
        ),
        Classification(
            "72.2", "Ricerca e sviluppo sperimentale nel campo delle scienze sociali e umanistiche", Category.GROUP
        ),
        Classification(
            "72.20", "Ricerca e sviluppo sperimentale nel campo delle scienze sociali e umanistiche", Category.CLASS
        ),
        Classification(
            "72.20.0",
            "Ricerca e sviluppo sperimentale nel campo delle scienze sociali e umanistiche",
            Category.SUBCLASS,
        ),
        Classification("72.20.01", "Ricerca e sviluppo sperimentale nel campo dell'archeologia", Category.SUBCLASS),
        Classification(
            "72.20.09",
            "Ricerca e sviluppo sperimentale nel campo delle altre scienze sociali e umanistiche",
            Category.SUBCLASS,
        ),
        Classification("73", "Attività di pubblicità, ricerche di mercato e pubbliche relazioni", Category.DIVISION),
        Classification("73.1", "Pubblicità", Category.GROUP),
        Classification("73.11", "Attività di agenzie pubblicitarie", Category.CLASS),
        Classification("73.11.0", "Attività di agenzie pubblicitarie", Category.SUBCLASS),
        Classification("73.11.01", "Ideazione di campagne pubblicitarie", Category.SUBCLASS),
        Classification(
            "73.11.02", "Conduzione di campagne di marketing e altri servizi pubblicitari", Category.SUBCLASS
        ),
        Classification("73.11.03", "Attività di influencer marketing", Category.SUBCLASS),
        Classification("73.12", "Attività di concessionarie pubblicitarie", Category.CLASS),
        Classification("73.12.0", "Attività di concessionarie pubblicitarie", Category.SUBCLASS),
        Classification("73.12.00", "Attività di concessionarie pubblicitarie", Category.SUBCLASS),
        Classification("73.2", "Ricerche di mercato e sondaggi di opinione", Category.GROUP),
        Classification("73.20", "Ricerche di mercato e sondaggi di opinione", Category.CLASS),
        Classification("73.20.0", "Ricerche di mercato e sondaggi di opinione", Category.SUBCLASS),
        Classification("73.20.00", "Ricerche di mercato e sondaggi di opinione", Category.SUBCLASS),
        Classification("73.3", "Pubbliche relazioni e comunicazione", Category.GROUP),
        Classification("73.30", "Pubbliche relazioni e comunicazione", Category.CLASS),
        Classification("73.30.0", "Pubbliche relazioni e comunicazione", Category.SUBCLASS),
        Classification("73.30.01", "Attività di rappresentanza di interessi", Category.SUBCLASS),
        Classification(
            "73.30.02",
            "Attività di informazione scientifica inerente prodotti farmaceutici e articoli medicali per scopi promozionali",
            Category.SUBCLASS,
        ),
        Classification("73.30.03", "Attività di promozione di altri prodotti", Category.SUBCLASS),
        Classification("73.30.09", "Pubbliche relazioni e comunicazione n.c.a.", Category.SUBCLASS),
        Classification("74", "Altre attività professionali, scientifiche e tecniche", Category.DIVISION),
        Classification("74.1", "Attività di progettazione specializzata", Category.GROUP),
        Classification("74.11", "Attività di progettazione di prodotti industriali e di moda", Category.CLASS),
        Classification("74.11.1", "Attività di progettazione di prodotti industriali", Category.SUBCLASS),
        Classification("74.11.10", "Attività di progettazione di prodotti industriali", Category.SUBCLASS),
        Classification("74.11.2", "Attività di progettazione di moda", Category.SUBCLASS),
        Classification("74.11.20", "Attività di progettazione di moda", Category.SUBCLASS),
        Classification("74.12", "Attività di progettazione grafica e di comunicazione visiva", Category.CLASS),
        Classification("74.12.0", "Attività di progettazione grafica e di comunicazione visiva", Category.SUBCLASS),
        Classification("74.12.01", "Grafica di pagine web", Category.SUBCLASS),
        Classification(
            "74.12.09", "Altre attività di progettazione grafica e di comunicazione visiva", Category.SUBCLASS
        ),
        Classification("74.13", "Attività di progettazione di interni", Category.CLASS),
        Classification("74.13.0", "Attività di progettazione di interni", Category.SUBCLASS),
        Classification("74.13.00", "Attività di progettazione di interni", Category.SUBCLASS),
        Classification("74.14", "Altre attività di progettazione specializzata", Category.CLASS),
        Classification("74.14.0", "Altre attività di progettazione specializzata", Category.SUBCLASS),
        Classification(
            "74.14.01", "Attività di progettazione specializzata fornite da disegnatori tecnici", Category.SUBCLASS
        ),
        Classification("74.14.09", "Altre attività di progettazione specializzata n.c.a.", Category.SUBCLASS),
        Classification("74.2", "Attività fotografiche", Category.GROUP),
        Classification("74.20", "Attività fotografiche", Category.CLASS),
        Classification("74.20.1", "Attività fotografiche specializzate", Category.SUBCLASS),
        Classification("74.20.11", "Attività fotografiche fornite da fotoreporter", Category.SUBCLASS),
        Classification("74.20.12", "Attività fotografiche aeree e subacquee", Category.SUBCLASS),
        Classification("74.20.19", "Altre attività fotografiche specializzate", Category.SUBCLASS),
        Classification("74.20.2", "Attività di sviluppo e stampa e altre attività fotografiche", Category.SUBCLASS),
        Classification("74.20.20", "Attività di sviluppo e stampa e altre attività fotografiche", Category.SUBCLASS),
        Classification("74.3", "Attività di traduzione e interpretariato", Category.GROUP),
        Classification("74.30", "Attività di traduzione e interpretariato", Category.CLASS),
        Classification("74.30.0", "Attività di traduzione e interpretariato", Category.SUBCLASS),
        Classification("74.30.00", "Attività di traduzione e interpretariato", Category.SUBCLASS),
        Classification("74.9", "Altre attività professionali, scientifiche e tecniche n.c.a.", Category.GROUP),
        Classification("74.91", "Attività di servizi di intermediazione e marketing di brevetti", Category.CLASS),
        Classification("74.91.0", "Attività di servizi di intermediazione e marketing di brevetti", Category.SUBCLASS),
        Classification("74.91.00", "Attività di servizi di intermediazione e marketing di brevetti", Category.SUBCLASS),
        Classification(
            "74.99", "Tutte le altre attività professionali, scientifiche e tecniche n.c.a.", Category.CLASS
        ),
        Classification("74.99.1", "Attività di consulenza agraria", Category.SUBCLASS),
        Classification("74.99.11", "Attività di consulenza agraria fornite da agronomi", Category.SUBCLASS),
        Classification("74.99.12", "Attività di consulenza agraria fornite da agrotecnici", Category.SUBCLASS),
        Classification("74.99.13", "Attività di consulenza agraria fornite da periti agrari", Category.SUBCLASS),
        Classification(
            "74.99.14",
            "Attività di consulenza agraria fornite da altri economisti specializzati in agricoltura",
            Category.SUBCLASS,
        ),
        Classification(
            "74.99.15", "Attività di consulenza agraria viticolo enologica fornite da enologi", Category.SUBCLASS
        ),
        Classification(
            "74.99.16", "Attività di consulenza agraria viticolo enologica fornite da enotecnici", Category.SUBCLASS
        ),
        Classification("74.99.19", "Altre attività di consulenza agraria n.c.a.", Category.SUBCLASS),
        Classification("74.99.2", "Attività di consulenza in materia di sicurezza", Category.SUBCLASS),
        Classification(
            "74.99.21", "Attività di consulenza in materia di sicurezza e salute dei posti di lavoro", Category.SUBCLASS
        ),
        Classification("74.99.29", "Altre attività di consulenza in materia di sicurezza", Category.SUBCLASS),
        Classification("74.99.3", "Attività di consulenza ambientale e di risparmio energetico", Category.SUBCLASS),
        Classification(
            "74.99.31",
            "Attività di consulenza in materia di prevenzione e riduzione dell'inquinamento e di gestione dei rifiuti",
            Category.SUBCLASS,
        ),
        Classification(
            "74.99.32",
            "Attività di consulenza in materia di gestione delle risorse energetiche, energie rinnovabili ed efficienza energetica",
            Category.SUBCLASS,
        ),
        Classification(
            "74.99.33",
            "Attività di consulenza in materia di gestione delle risorse idriche, minerali e altre risorse naturali per usi differenti da quelli energetici",
            Category.SUBCLASS,
        ),
        Classification("74.99.4", "Attività di consulenza in enogastronomia", Category.SUBCLASS),
        Classification("74.99.41", "Attività di consulenza fornite da enotecari e sommelier", Category.SUBCLASS),
        Classification("74.99.42", "Attività di consulenza in gastronomia", Category.SUBCLASS),
        Classification(
            "74.99.9", "Altre attività varie professionali, scientifiche e tecniche n.c.a.", Category.SUBCLASS
        ),
        Classification("74.99.91", "Attività tecniche svolte da periti industriali", Category.SUBCLASS),
        Classification("74.99.92", "Attività di previsione meteorologica", Category.SUBCLASS),
        Classification(
            "74.99.93", "Attività di agenzie, agenti e procuratori per lo spettacolo e lo sport", Category.SUBCLASS
        ),
        Classification("74.99.94", "Attività di consulenza tecnica in ambito grafologico", Category.SUBCLASS),
        Classification(
            "74.99.99", "Tutte le altre attività varie professionali, scientifiche e tecniche n.c.a.", Category.SUBCLASS
        ),
        Classification("75", "Servizi veterinari", Category.DIVISION),
        Classification("75.0", "Servizi veterinari", Category.GROUP),
        Classification("75.00", "Servizi veterinari", Category.CLASS),
        Classification("75.00.0", "Servizi veterinari", Category.SUBCLASS),
        Classification("75.00.00", "Servizi veterinari", Category.SUBCLASS),
        Classification("O", "ATTIVITÀ AMMINISTRATIVE E DI SERVIZI DI SUPPORTO", Category.SECTION),
        Classification("77", "Attività di noleggio e leasing operativo", Category.DIVISION),
        Classification("77.1", "Noleggio e leasing operativo di autoveicoli", Category.GROUP),
        Classification("77.11", "Noleggio e leasing operativo di automobili e autoveicoli leggeri", Category.CLASS),
        Classification(
            "77.11.0", "Noleggio e leasing operativo di automobili e autoveicoli leggeri", Category.SUBCLASS
        ),
        Classification(
            "77.11.00", "Noleggio e leasing operativo di automobili e autoveicoli leggeri", Category.SUBCLASS
        ),
        Classification("77.12", "Noleggio e leasing operativo di autocarri", Category.CLASS),
        Classification("77.12.0", "Noleggio e leasing operativo di autocarri", Category.SUBCLASS),
        Classification("77.12.00", "Noleggio e leasing operativo di autocarri", Category.SUBCLASS),
        Classification("77.2", "Noleggio e leasing operativo di beni per uso personale e per la casa", Category.GROUP),
        Classification(
            "77.21", "Noleggio e leasing operativo di attrezzature e articoli sportivi e ricreativi", Category.CLASS
        ),
        Classification(
            "77.21.0",
            "Noleggio e leasing operativo di attrezzature e articoli sportivi e ricreativi",
            Category.SUBCLASS,
        ),
        Classification("77.21.01", "Noleggio e leasing operativo di biciclette", Category.SUBCLASS),
        Classification(
            "77.21.02", "Noleggio e leasing operativo di imbarcazioni da diporto senza operatore", Category.SUBCLASS
        ),
        Classification(
            "77.21.09",
            "Noleggio e leasing operativo di altre attrezzature e articoli sportivi e ricreativi",
            Category.SUBCLASS,
        ),
        Classification(
            "77.22", "Noleggio e leasing operativo di altri beni per uso personale e per la casa", Category.CLASS
        ),
        Classification(
            "77.22.1",
            "Noleggio e leasing operativo di tessili, articoli di abbigliamento e calzature",
            Category.SUBCLASS,
        ),
        Classification(
            "77.22.10",
            "Noleggio e leasing operativo di tessili, articoli di abbigliamento e calzature",
            Category.SUBCLASS,
        ),
        Classification(
            "77.22.9",
            "Noleggio e leasing operativo di altri beni per uso personale e per la casa n.c.a.",
            Category.SUBCLASS,
        ),
        Classification(
            "77.22.90",
            "Noleggio e leasing operativo di altri beni per uso personale e per la casa n.c.a.",
            Category.SUBCLASS,
        ),
        Classification(
            "77.3", "Noleggio e leasing operativo di altre macchine, attrezzature e beni materiali", Category.GROUP
        ),
        Classification("77.31", "Noleggio e leasing operativo di macchine e attrezzature agricole", Category.CLASS),
        Classification(
            "77.31.0", "Noleggio e leasing operativo di macchine e attrezzature agricole", Category.SUBCLASS
        ),
        Classification(
            "77.31.00", "Noleggio e leasing operativo di macchine e attrezzature agricole", Category.SUBCLASS
        ),
        Classification(
            "77.32",
            "Noleggio e leasing operativo di macchine e attrezzature per lavori edili e di ingegneria civile",
            Category.CLASS,
        ),
        Classification(
            "77.32.0",
            "Noleggio e leasing operativo di macchine e attrezzature per lavori edili e di ingegneria civile",
            Category.SUBCLASS,
        ),
        Classification(
            "77.32.00",
            "Noleggio e leasing operativo di macchine e attrezzature per lavori edili e di ingegneria civile",
            Category.SUBCLASS,
        ),
        Classification(
            "77.33", "Noleggio e leasing operativo di macchine, attrezzature e computer per ufficio", Category.CLASS
        ),
        Classification(
            "77.33.0",
            "Noleggio e leasing operativo di macchine, attrezzature e computer per ufficio",
            Category.SUBCLASS,
        ),
        Classification(
            "77.33.00",
            "Noleggio e leasing operativo di macchine, attrezzature e computer per ufficio",
            Category.SUBCLASS,
        ),
        Classification(
            "77.34", "Noleggio e leasing operativo di mezzi di trasporto marittimi, fluviali e lacustri", Category.CLASS
        ),
        Classification(
            "77.34.0",
            "Noleggio e leasing operativo di mezzi di trasporto marittimi, fluviali e lacustri",
            Category.SUBCLASS,
        ),
        Classification(
            "77.34.00",
            "Noleggio e leasing operativo di mezzi di trasporto marittimi, fluviali e lacustri",
            Category.SUBCLASS,
        ),
        Classification("77.35", "Noleggio e leasing operativo di mezzi di trasporto aereo", Category.CLASS),
        Classification("77.35.0", "Noleggio e leasing operativo di mezzi di trasporto aereo", Category.SUBCLASS),
        Classification("77.35.00", "Noleggio e leasing operativo di mezzi di trasporto aereo", Category.SUBCLASS),
        Classification(
            "77.39",
            "Noleggio e leasing operativo di altre macchine, attrezzature e beni materiali n.c.a.",
            Category.CLASS,
        ),
        Classification(
            "77.39.1", "Noleggio e leasing operativo di altri mezzi di trasporto terrestre", Category.SUBCLASS
        ),
        Classification(
            "77.39.10", "Noleggio e leasing operativo di altri mezzi di trasporto terrestre", Category.SUBCLASS
        ),
        Classification(
            "77.39.9",
            "Noleggio e leasing operativo di altre macchine, attrezzature e beni materiali n.c.a., esclusi altri mezzi di trasporto terrestre",
            Category.SUBCLASS,
        ),
        Classification(
            "77.39.91",
            "Noleggio e leasing operativo di apparecchi di sollevamento e movimentazione merci",
            Category.SUBCLASS,
        ),
        Classification(
            "77.39.92",
            "Noleggio e leasing operativo di strutture e attrezzature per manifestazioni e spettacoli",
            Category.SUBCLASS,
        ),
        Classification(
            "77.39.99",
            "Noleggio e leasing operativo di altre macchine, attrezzature e beni materiali vari n.c.a.",
            Category.SUBCLASS,
        ),
        Classification(
            "77.4",
            "Concessione dei diritti di sfruttamento di proprietà intellettuale, escluse le opere soggette a diritto d'autore",
            Category.GROUP,
        ),
        Classification(
            "77.40",
            "Concessione dei diritti di sfruttamento di proprietà intellettuale, escluse le opere soggette a diritto d'autore",
            Category.CLASS,
        ),
        Classification(
            "77.40.0",
            "Concessione dei diritti di sfruttamento di proprietà intellettuale, escluse le opere soggette a diritto d'autore",
            Category.SUBCLASS,
        ),
        Classification(
            "77.40.00",
            "Concessione dei diritti di sfruttamento di proprietà intellettuale, escluse le opere soggette a diritto d'autore",
            Category.SUBCLASS,
        ),
        Classification(
            "77.5",
            "Attività di servizi di intermediazione per il noleggio e il leasing operativo di beni materiali e beni immateriali non finanziari",
            Category.GROUP,
        ),
        Classification(
            "77.51",
            "Attività di servizi di intermediazione per il noleggio e il leasing operativo di automobili, autocaravan e rimorchi",
            Category.CLASS,
        ),
        Classification(
            "77.51.0",
            "Attività di servizi di intermediazione per il noleggio e il leasing operativo di automobili, autocaravan e rimorchi",
            Category.SUBCLASS,
        ),
        Classification(
            "77.51.00",
            "Attività di servizi di intermediazione per il noleggio e il leasing operativo di automobili, autocaravan e rimorchi",
            Category.SUBCLASS,
        ),
        Classification(
            "77.52",
            "Attività di servizi di intermediazione per il noleggio e il leasing operativo di altri beni materiali e beni immateriali non finanziari",
            Category.CLASS,
        ),
        Classification(
            "77.52.0",
            "Attività di servizi di intermediazione per il noleggio e il leasing operativo di altri beni materiali e beni immateriali non finanziari",
            Category.SUBCLASS,
        ),
        Classification(
            "77.52.00",
            "Attività di servizi di intermediazione per il noleggio e il leasing operativo di altri beni materiali e beni immateriali non finanziari",
            Category.SUBCLASS,
        ),
        Classification("78", "Attività di ricerca, selezione, fornitura di risorse umane", Category.DIVISION),
        Classification("78.1", "Attività di agenzie di collocamento", Category.GROUP),
        Classification("78.10", "Attività di agenzie di collocamento", Category.CLASS),
        Classification("78.10.0", "Attività di agenzie di collocamento", Category.SUBCLASS),
        Classification("78.10.00", "Attività di agenzie di collocamento", Category.SUBCLASS),
        Classification(
            "78.2",
            "Attività di agenzie di lavoro interinale e altre attività di fornitura di risorse umane",
            Category.GROUP,
        ),
        Classification(
            "78.20",
            "Attività di agenzie di lavoro interinale e altre attività di fornitura di risorse umane",
            Category.CLASS,
        ),
        Classification(
            "78.20.0",
            "Attività di agenzie di lavoro interinale e altre attività di fornitura di risorse umane",
            Category.SUBCLASS,
        ),
        Classification(
            "78.20.00",
            "Attività di agenzie di lavoro interinale e altre attività di fornitura di risorse umane",
            Category.SUBCLASS,
        ),
        Classification(
            "79",
            "Attività di agenzie di viaggio, tour operator e altri servizi di prenotazione e attività connesse",
            Category.DIVISION,
        ),
        Classification("79.1", "Attività di agenzie di viaggio e tour operator", Category.GROUP),
        Classification("79.11", "Attività di agenzie di viaggio", Category.CLASS),
        Classification("79.11.0", "Attività di agenzie di viaggio", Category.SUBCLASS),
        Classification("79.11.00", "Attività di agenzie di viaggio", Category.SUBCLASS),
        Classification("79.12", "Attività di tour operator", Category.CLASS),
        Classification("79.12.0", "Attività di tour operator", Category.SUBCLASS),
        Classification("79.12.00", "Attività di tour operator", Category.SUBCLASS),
        Classification("79.9", "Altri servizi di prenotazione e attività connesse", Category.GROUP),
        Classification("79.90", "Altri servizi di prenotazione e attività connesse", Category.CLASS),
        Classification("79.90.0", "Altri servizi di prenotazione e attività connesse", Category.SUBCLASS),
        Classification("79.90.01", "Servizi di guida turistica", Category.SUBCLASS),
        Classification("79.90.02", "Servizi di accompagnamento in ambiente naturale", Category.SUBCLASS),
        Classification("79.90.03", "Altri servizi di accompagnamento turistico", Category.SUBCLASS),
        Classification("79.90.04", "Altre attività di assistenza turistica", Category.SUBCLASS),
        Classification("80", "Attività di investigazione e vigilanza", Category.DIVISION),
        Classification("80.0", "Attività di investigazione e vigilanza", Category.GROUP),
        Classification("80.01", "Attività di investigazione e vigilanza privata", Category.CLASS),
        Classification("80.01.1", "Attività di investigazione", Category.SUBCLASS),
        Classification("80.01.11", "Attività di investigazione in ambito privato", Category.SUBCLASS),
        Classification("80.01.12", "Attività di investigazione in ambito aziendale e commerciale", Category.SUBCLASS),
        Classification("80.01.13", "Attività di investigazione in ambito assicurativo", Category.SUBCLASS),
        Classification("80.01.14", "Attività di investigazione in ambito legale", Category.SUBCLASS),
        Classification("80.01.2", "Attività di vigilanza privata", Category.SUBCLASS),
        Classification("80.01.21", "Attività di vigilanza privata non armata", Category.SUBCLASS),
        Classification("80.01.29", "Altre attività di vigilanza privata", Category.SUBCLASS),
        Classification("80.09", "Attività di vigilanza n.c.a.", Category.CLASS),
        Classification("80.09.0", "Attività di vigilanza n.c.a.", Category.SUBCLASS),
        Classification("80.09.00", "Attività di vigilanza n.c.a.", Category.SUBCLASS),
        Classification("81", "Attività di servizi per edifici e per la cura del paesaggio", Category.DIVISION),
        Classification("81.1", "Attività di servizi integrati agli edifici", Category.GROUP),
        Classification("81.10", "Attività di servizi integrati agli edifici", Category.CLASS),
        Classification("81.10.0", "Attività di servizi integrati agli edifici", Category.SUBCLASS),
        Classification("81.10.00", "Attività di servizi integrati agli edifici", Category.SUBCLASS),
        Classification("81.2", "Attività di pulizia", Category.GROUP),
        Classification("81.21", "Attività di pulizia generale di edifici", Category.CLASS),
        Classification("81.21.0", "Attività di pulizia generale di edifici", Category.SUBCLASS),
        Classification("81.21.00", "Attività di pulizia generale di edifici", Category.SUBCLASS),
        Classification("81.22", "Altre attività di pulizia di edifici e pulizia industriale", Category.CLASS),
        Classification("81.22.0", "Altre attività di pulizia di edifici e pulizia industriale", Category.SUBCLASS),
        Classification("81.22.01", "Attività di sterilizzazione di attrezzature mediche", Category.SUBCLASS),
        Classification(
            "81.22.09", "Altre attività di pulizia di edifici e pulizia industriale n.c.a.", Category.SUBCLASS
        ),
        Classification("81.23", "Altre attività di pulizia", Category.CLASS),
        Classification("81.23.1", "Attività di sanificazione, disinfezione e disinfestazione", Category.SUBCLASS),
        Classification("81.23.10", "Attività di sanificazione, disinfezione e disinfestazione", Category.SUBCLASS),
        Classification("81.23.9", "Altre attività di pulizia n.c.a.", Category.SUBCLASS),
        Classification("81.23.91", "Pulitura delle strade e rimozione di neve e ghiaccio", Category.SUBCLASS),
        Classification("81.23.99", "Altre attività di pulizia varie n.c.a.", Category.SUBCLASS),
        Classification("81.3", "Attività di servizi per la cura del paesaggio", Category.GROUP),
        Classification("81.30", "Attività di servizi per la cura del paesaggio", Category.CLASS),
        Classification("81.30.0", "Attività di servizi per la cura del paesaggio", Category.SUBCLASS),
        Classification("81.30.00", "Attività di servizi per la cura del paesaggio", Category.SUBCLASS),
        Classification(
            "82",
            "Attività amministrative, di supporto per le funzioni di ufficio e altri servizi di supporto alle imprese",
            Category.DIVISION,
        ),
        Classification("82.1", "Attività amministrative e di supporto per le funzioni di ufficio", Category.GROUP),
        Classification("82.10", "Attività amministrative e di supporto per le funzioni di ufficio", Category.CLASS),
        Classification(
            "82.10.0", "Attività amministrative e di supporto per le funzioni di ufficio", Category.SUBCLASS
        ),
        Classification(
            "82.10.00", "Attività amministrative e di supporto per le funzioni di ufficio", Category.SUBCLASS
        ),
        Classification("82.2", "Attività dei call center", Category.GROUP),
        Classification("82.20", "Attività dei call center", Category.CLASS),
        Classification("82.20.0", "Attività dei call center", Category.SUBCLASS),
        Classification("82.20.00", "Attività dei call center", Category.SUBCLASS),
        Classification("82.3", "Organizzazione di convegni e fiere", Category.GROUP),
        Classification("82.30", "Organizzazione di convegni e fiere", Category.CLASS),
        Classification("82.30.0", "Organizzazione di convegni e fiere", Category.SUBCLASS),
        Classification("82.30.01", "Organizzazione di conferenze e congressi", Category.SUBCLASS),
        Classification("82.30.02", "Organizzazione di fiere commerciali e di affari", Category.SUBCLASS),
        Classification("82.30.03", "Organizzazione di convegni ed eventi aziendali", Category.SUBCLASS),
        Classification("82.30.04", "Organizzazione di mercati agricoli e fiere dell'artigianato", Category.SUBCLASS),
        Classification("82.30.09", "Organizzazione di altri eventi", Category.SUBCLASS),
        Classification(
            "82.4", "Attività di servizi di intermediazione per servizi di supporto alle imprese n.c.a.", Category.GROUP
        ),
        Classification(
            "82.40",
            "Attività di servizi di intermediazione per servizi di supporto alle imprese n.c.a.",
            Category.CLASS,
        ),
        Classification(
            "82.40.0",
            "Attività di servizi di intermediazione per servizi di supporto alle imprese n.c.a.",
            Category.SUBCLASS,
        ),
        Classification(
            "82.40.01",
            "Attività di servizi di prenotazione di biglietti per spettacoli teatrali, sportivi e altri spettacoli di intrattenimento e divertimento",
            Category.SUBCLASS,
        ),
        Classification(
            "82.40.09",
            "Altre attività di servizi di intermediazione per servizi di supporto alle imprese n.c.a.",
            Category.SUBCLASS,
        ),
        Classification("82.9", "Servizi di supporto alle imprese n.c.a.", Category.GROUP),
        Classification(
            "82.91", "Attività di recupero crediti, di informazioni commerciali e di rating", Category.CLASS
        ),
        Classification("82.91.1", "Attività di recupero crediti", Category.SUBCLASS),
        Classification("82.91.10", "Attività di recupero crediti", Category.SUBCLASS),
        Classification(
            "82.91.2", "Attività di raccolta e fornitura di informazioni commerciali e di rating", Category.SUBCLASS
        ),
        Classification(
            "82.91.20", "Attività di raccolta e fornitura di informazioni commerciali e di rating", Category.SUBCLASS
        ),
        Classification("82.92", "Attività di imballaggio", Category.CLASS),
        Classification("82.92.1", "Attività di imballaggio di generi alimentari", Category.SUBCLASS),
        Classification("82.92.10", "Attività di imballaggio di generi alimentari", Category.SUBCLASS),
        Classification("82.92.2", "Attività di imballaggio di generi non alimentari", Category.SUBCLASS),
        Classification("82.92.20", "Attività di imballaggio di generi non alimentari", Category.SUBCLASS),
        Classification("82.99", "Altri servizi di supporto alle imprese n.c.a.", Category.CLASS),
        Classification("82.99.1", "Richiesta certificati e disbrigo pratiche", Category.SUBCLASS),
        Classification("82.99.11", "Fornitura di assistenza per la registrazione di autoveicoli", Category.SUBCLASS),
        Classification("82.99.19", "Richiesta certificati e disbrigo pratiche n.c.a.", Category.SUBCLASS),
        Classification("82.99.9", "Altri servizi vari di supporto alle imprese n.c.a.", Category.SUBCLASS),
        Classification("82.99.91", "Rilevamento del consumo di calore e acqua calda", Category.SUBCLASS),
        Classification("82.99.99", "Tutti gli altri servizi vari di supporto alle imprese n.c.a.", Category.SUBCLASS),
        Classification("P", "AMMINISTRAZIONE PUBBLICA E DIFESA; ASSICURAZIONE SOCIALE OBBLIGATORIA", Category.SECTION),
        Classification(
            "84", "Amministrazione pubblica e difesa; assicurazione sociale obbligatoria", Category.DIVISION
        ),
        Classification(
            "84.1",
            "Amministrazione dello Stato e delle politiche economiche, sociali e ambientali della comunità",
            Category.GROUP,
        ),
        Classification("84.11", "Attività generali di amministrazione pubblica", Category.CLASS),
        Classification(
            "84.11.1",
            "Attività degli organi legislativi ed esecutivi e delle amministrazioni centrali e locali",
            Category.SUBCLASS,
        ),
        Classification(
            "84.11.10",
            "Attività degli organi legislativi ed esecutivi e delle amministrazioni centrali e locali",
            Category.SUBCLASS,
        ),
        Classification("84.11.2", "Servizi di gestione esattoriale per conto terzi", Category.SUBCLASS),
        Classification("84.11.20", "Servizi di gestione esattoriale per conto terzi", Category.SUBCLASS),
        Classification(
            "84.11.3", "Attività di pianificazione generale e servizi statistici generali", Category.SUBCLASS
        ),
        Classification(
            "84.11.30", "Attività di pianificazione generale e servizi statistici generali", Category.SUBCLASS
        ),
        Classification(
            "84.12",
            "Regolamentazione dei servizi di assistenza sanitaria, istruzione, servizi culturali e di altri servizi sociali",
            Category.CLASS,
        ),
        Classification("84.12.1", "Regolamentazione dei servizi di assistenza sanitaria", Category.SUBCLASS),
        Classification("84.12.10", "Regolamentazione dei servizi di assistenza sanitaria", Category.SUBCLASS),
        Classification("84.12.2", "Regolamentazione dei servizi di istruzione", Category.SUBCLASS),
        Classification("84.12.20", "Regolamentazione dei servizi di istruzione", Category.SUBCLASS),
        Classification(
            "84.12.3",
            "Regolamentazione dei servizi per l'edilizia abitativa e la tutela dell'ambiente",
            Category.SUBCLASS,
        ),
        Classification(
            "84.12.30",
            "Regolamentazione dei servizi per l'edilizia abitativa e la tutela dell'ambiente",
            Category.SUBCLASS,
        ),
        Classification(
            "84.12.4", "Regolamentazione dei servizi culturali e di altri servizi sociali", Category.SUBCLASS
        ),
        Classification(
            "84.12.40", "Regolamentazione dei servizi culturali e di altri servizi sociali", Category.SUBCLASS
        ),
        Classification(
            "84.13",
            "Regolamentazione delle attività che contribuiscono a una più efficiente gestione delle attività economiche",
            Category.CLASS,
        ),
        Classification(
            "84.13.1",
            "Regolamentazione dei servizi connessi a agricoltura, silvicoltura, caccia e pesca",
            Category.SUBCLASS,
        ),
        Classification(
            "84.13.10",
            "Regolamentazione dei servizi connessi a agricoltura, silvicoltura, caccia e pesca",
            Category.SUBCLASS,
        ),
        Classification("84.13.2", "Regolamentazione dei servizi connessi a combustibili ed energia", Category.SUBCLASS),
        Classification(
            "84.13.20", "Regolamentazione dei servizi connessi a combustibili ed energia", Category.SUBCLASS
        ),
        Classification(
            "84.13.3",
            "Regolamentazione dei servizi connessi a industrie estrattive e risorse minerarie, industrie manifatturiere e di costruzione",
            Category.SUBCLASS,
        ),
        Classification(
            "84.13.30",
            "Regolamentazione dei servizi connessi a industrie estrattive e risorse minerarie, industrie manifatturiere e di costruzione",
            Category.SUBCLASS,
        ),
        Classification(
            "84.13.4", "Regolamentazione dei servizi connessi a trasporti e comunicazioni", Category.SUBCLASS
        ),
        Classification(
            "84.13.40", "Regolamentazione dei servizi connessi a trasporti e comunicazioni", Category.SUBCLASS
        ),
        Classification(
            "84.13.5",
            "Regolamentazione dei servizi connessi a commercio, servizi di alloggio e ristorazione",
            Category.SUBCLASS,
        ),
        Classification(
            "84.13.50",
            "Regolamentazione dei servizi connessi a commercio, servizi di alloggio e ristorazione",
            Category.SUBCLASS,
        ),
        Classification("84.13.6", "Regolamentazione dei servizi connessi al turismo", Category.SUBCLASS),
        Classification("84.13.60", "Regolamentazione dei servizi connessi al turismo", Category.SUBCLASS),
        Classification("84.13.9", "Regolamentazione di altri servizi", Category.SUBCLASS),
        Classification("84.13.90", "Regolamentazione di altri servizi", Category.SUBCLASS),
        Classification("84.2", "Erogazione di servizi collettivi", Category.GROUP),
        Classification("84.21", "Affari esteri", Category.CLASS),
        Classification("84.21.0", "Affari esteri", Category.SUBCLASS),
        Classification("84.21.00", "Affari esteri", Category.SUBCLASS),
        Classification("84.22", "Difesa nazionale", Category.CLASS),
        Classification("84.22.0", "Difesa nazionale", Category.SUBCLASS),
        Classification("84.22.00", "Difesa nazionale", Category.SUBCLASS),
        Classification("84.23", "Giustizia e attività giudiziarie", Category.CLASS),
        Classification("84.23.0", "Giustizia e attività giudiziarie", Category.SUBCLASS),
        Classification("84.23.00", "Giustizia e attività giudiziarie", Category.SUBCLASS),
        Classification("84.24", "Ordine pubblico e sicurezza nazionale", Category.CLASS),
        Classification("84.24.1", "Ordine pubblico e sicurezza nazionale delle Forze dell'Ordine", Category.SUBCLASS),
        Classification("84.24.10", "Ordine pubblico e sicurezza nazionale delle Forze dell'Ordine", Category.SUBCLASS),
        Classification(
            "84.24.2",
            "Attività di supporto all'ordine pubblico e alla sicurezza nazionale fornite dalla Protezione Civile",
            Category.SUBCLASS,
        ),
        Classification(
            "84.24.20",
            "Attività di supporto all'ordine pubblico e alla sicurezza nazionale fornite dalla Protezione Civile",
            Category.SUBCLASS,
        ),
        Classification("84.25", "Servizi antincendio", Category.CLASS),
        Classification("84.25.0", "Servizi antincendio", Category.SUBCLASS),
        Classification("84.25.00", "Servizi antincendio", Category.SUBCLASS),
        Classification("84.3", "Assicurazione sociale obbligatoria", Category.GROUP),
        Classification("84.30", "Assicurazione sociale obbligatoria", Category.CLASS),
        Classification("84.30.0", "Assicurazione sociale obbligatoria", Category.SUBCLASS),
        Classification("84.30.00", "Assicurazione sociale obbligatoria", Category.SUBCLASS),
        Classification("Q", "ISTRUZIONE E FORMAZIONE", Category.SECTION),
        Classification("85", "Istruzione e formazione", Category.DIVISION),
        Classification("85.1", "Istruzione prescolastica", Category.GROUP),
        Classification("85.10", "Istruzione prescolastica", Category.CLASS),
        Classification("85.10.0", "Istruzione prescolastica", Category.SUBCLASS),
        Classification("85.10.00", "Istruzione prescolastica", Category.SUBCLASS),
        Classification("85.2", "Istruzione primaria", Category.GROUP),
        Classification("85.20", "Istruzione primaria", Category.CLASS),
        Classification("85.20.0", "Istruzione primaria", Category.SUBCLASS),
        Classification("85.20.00", "Istruzione primaria", Category.SUBCLASS),
        Classification("85.3", "Istruzione secondaria e post-secondaria non terziaria", Category.GROUP),
        Classification("85.31", "Istruzione secondaria di formazione generale", Category.CLASS),
        Classification("85.31.1", "Istruzione secondaria di formazione generale di primo grado", Category.SUBCLASS),
        Classification("85.31.10", "Istruzione secondaria di formazione generale di primo grado", Category.SUBCLASS),
        Classification("85.31.2", "Istruzione secondaria di formazione generale di secondo grado", Category.SUBCLASS),
        Classification("85.31.20", "Istruzione secondaria di formazione generale di secondo grado", Category.SUBCLASS),
        Classification("85.32", "Istruzione secondaria professionale", Category.CLASS),
        Classification("85.32.0", "Istruzione secondaria professionale", Category.SUBCLASS),
        Classification(
            "85.32.01", "Istruzione secondaria professionale erogata da scuole di vela e navigazione", Category.SUBCLASS
        ),
        Classification("85.32.02", "Istruzione secondaria professionale erogata da scuole di volo", Category.SUBCLASS),
        Classification("85.32.03", "Istruzione secondaria professionale erogata da scuole di guida", Category.SUBCLASS),
        Classification("85.32.09", "Altra istruzione secondaria professionale n.c.a.", Category.SUBCLASS),
        Classification("85.33", "Istruzione post-secondaria non terziaria", Category.CLASS),
        Classification("85.33.0", "Istruzione post-secondaria non terziaria", Category.SUBCLASS),
        Classification("85.33.00", "Istruzione post-secondaria non terziaria", Category.SUBCLASS),
        Classification("85.4", "Istruzione terziaria", Category.GROUP),
        Classification("85.40", "Istruzione terziaria", Category.CLASS),
        Classification("85.40.1", "Istruzione terziaria non universitaria professionale", Category.SUBCLASS),
        Classification("85.40.10", "Istruzione terziaria non universitaria professionale", Category.SUBCLASS),
        Classification(
            "85.40.2",
            "Istruzione terziaria universitaria di primo, secondo e terzo ciclo e a ciclo unico",
            Category.SUBCLASS,
        ),
        Classification(
            "85.40.20",
            "Istruzione terziaria universitaria di primo, secondo e terzo ciclo e a ciclo unico",
            Category.SUBCLASS,
        ),
        Classification("85.5", "Altri servizi di istruzione e formazione", Category.GROUP),
        Classification("85.51", "Formazione sportiva e ricreativa", Category.CLASS),
        Classification("85.51.0", "Formazione sportiva e ricreativa", Category.SUBCLASS),
        Classification(
            "85.51.01", "Insegnamento di pilates fornito da insegnanti e istruttori indipendenti", Category.SUBCLASS
        ),
        Classification("85.51.09", "Formazione sportiva e ricreativa n.c.a.", Category.SUBCLASS),
        Classification("85.52", "Formazione culturale", Category.CLASS),
        Classification("85.52.0", "Formazione culturale", Category.SUBCLASS),
        Classification("85.52.01", "Corsi di danza", Category.SUBCLASS),
        Classification("85.52.02", "Attività di educazione al patrimonio culturale", Category.SUBCLASS),
        Classification("85.52.09", "Altra formazione culturale", Category.SUBCLASS),
        Classification("85.53", "Attività di scuole guida", Category.CLASS),
        Classification("85.53.0", "Attività di scuole guida", Category.SUBCLASS),
        Classification("85.53.00", "Attività di scuole guida", Category.SUBCLASS),
        Classification("85.59", "Altri servizi di istruzione e formazione n.c.a.", Category.CLASS),
        Classification("85.59.1", "Corsi di lingua straniera", Category.SUBCLASS),
        Classification("85.59.10", "Corsi di lingua straniera", Category.SUBCLASS),
        Classification("85.59.2", "Corsi di formazione e corsi di aggiornamento professionale", Category.SUBCLASS),
        Classification("85.59.20", "Corsi di formazione e corsi di aggiornamento professionale", Category.SUBCLASS),
        Classification(
            "85.59.3",
            "Altri servizi di istruzione e formazione n.c.a. forniti da università popolari",
            Category.SUBCLASS,
        ),
        Classification(
            "85.59.30",
            "Altri servizi di istruzione e formazione n.c.a. forniti da università popolari",
            Category.SUBCLASS,
        ),
        Classification("85.59.9", "Altri servizi vari di istruzione e formazione n.c.a.", Category.SUBCLASS),
        Classification("85.59.91", "Corsi di educazione consapevole attraverso il movimento", Category.SUBCLASS),
        Classification("85.59.99", "Tutti gli altri servizi vari di istruzione e formazione n.c.a.", Category.SUBCLASS),
        Classification("85.6", "Servizi di supporto all'istruzione e formazione", Category.GROUP),
        Classification("85.61", "Attività di servizi di intermediazione per corsi e tutor", Category.CLASS),
        Classification("85.61.0", "Attività di servizi di intermediazione per corsi e tutor", Category.SUBCLASS),
        Classification("85.61.00", "Attività di servizi di intermediazione per corsi e tutor", Category.SUBCLASS),
        Classification("85.69", "Altri servizi di supporto all'istruzione e formazione n.c.a.", Category.CLASS),
        Classification("85.69.0", "Altri servizi di supporto all'istruzione e formazione n.c.a.", Category.SUBCLASS),
        Classification("85.69.01", "Consulenza scolastica e servizi di orientamento scolastico", Category.SUBCLASS),
        Classification(
            "85.69.09", "Altri servizi vari di supporto all'istruzione e formazione n.c.a.", Category.SUBCLASS
        ),
        Classification("R", "ATTIVITÀ PER LA SALUTE UMANA E DI ASSISTENZA SOCIALE", Category.SECTION),
        Classification("86", "Attività per la salute umana", Category.DIVISION),
        Classification("86.1", "Attività ospedaliere", Category.GROUP),
        Classification("86.10", "Attività ospedaliere", Category.CLASS),
        Classification("86.10.0", "Attività ospedaliere", Category.SUBCLASS),
        Classification("86.10.00", "Attività ospedaliere", Category.SUBCLASS),
        Classification("86.2", "Attività mediche e odontoiatriche", Category.GROUP),
        Classification("86.21", "Attività di medicina generale", Category.CLASS),
        Classification("86.21.0", "Attività di medicina generale", Category.SUBCLASS),
        Classification("86.21.00", "Attività di medicina generale", Category.SUBCLASS),
        Classification("86.22", "Attività di medicina specialistica", Category.CLASS),
        Classification("86.22.0", "Attività di medicina specialistica", Category.SUBCLASS),
        Classification("86.22.01", "Trattamenti di chirurgia estetica", Category.SUBCLASS),
        Classification(
            "86.22.02",
            "Altre attività di medicina specialistica svolte da medici specialisti indipendenti",
            Category.SUBCLASS,
        ),
        Classification(
            "86.22.03",
            "Altre attività di medicina specialistica svolte presso cliniche e centri specialistici",
            Category.SUBCLASS,
        ),
        Classification("86.23", "Attività odontoiatriche", Category.CLASS),
        Classification("86.23.0", "Attività odontoiatriche", Category.SUBCLASS),
        Classification("86.23.00", "Attività odontoiatriche", Category.SUBCLASS),
        Classification("86.9", "Altre attività per la salute umana", Category.GROUP),
        Classification("86.91", "Attività di diagnostica per immagini e di laboratorio medico", Category.CLASS),
        Classification("86.91.0", "Attività di diagnostica per immagini e di laboratorio medico", Category.SUBCLASS),
        Classification("86.91.01", "Attività di diagnostica per immagini", Category.SUBCLASS),
        Classification("86.91.02", "Attività di laboratorio medico", Category.SUBCLASS),
        Classification("86.92", "Trasporto di pazienti in ambulanza", Category.CLASS),
        Classification("86.92.0", "Trasporto di pazienti in ambulanza", Category.SUBCLASS),
        Classification("86.92.00", "Trasporto di pazienti in ambulanza", Category.SUBCLASS),
        Classification("86.93", "Attività di psicologi e psicoterapeuti, esclusi i medici", Category.CLASS),
        Classification("86.93.0", "Attività di psicologi e psicoterapeuti, esclusi i medici", Category.SUBCLASS),
        Classification("86.93.00", "Attività di psicologi e psicoterapeuti, esclusi i medici", Category.SUBCLASS),
        Classification("86.94", "Attività infermieristiche e ostetriche", Category.CLASS),
        Classification("86.94.0", "Attività infermieristiche e ostetriche", Category.SUBCLASS),
        Classification("86.94.01", "Attività infermieristiche", Category.SUBCLASS),
        Classification("86.94.02", "Attività ostetriche", Category.SUBCLASS),
        Classification("86.95", "Attività di fisioterapia", Category.CLASS),
        Classification("86.95.0", "Attività di fisioterapia", Category.SUBCLASS),
        Classification("86.95.00", "Attività di fisioterapia", Category.SUBCLASS),
        Classification("86.96", "Attività di medicine complementari e alternative", Category.CLASS),
        Classification("86.96.0", "Attività di medicine complementari e alternative", Category.SUBCLASS),
        Classification("86.96.01", "Chinesiologia", Category.SUBCLASS),
        Classification("86.96.09", "Attività di medicine complementari e alternative n.c.a.", Category.SUBCLASS),
        Classification(
            "86.97",
            "Attività di servizi di intermediazione per attività mediche, odontoiatriche e altri servizi per la salute umana",
            Category.CLASS,
        ),
        Classification(
            "86.97.0",
            "Attività di servizi di intermediazione per attività mediche, odontoiatriche e altri servizi per la salute umana",
            Category.SUBCLASS,
        ),
        Classification(
            "86.97.00",
            "Attività di servizi di intermediazione per attività mediche, odontoiatriche e altri servizi per la salute umana",
            Category.SUBCLASS,
        ),
        Classification("86.99", "Altre attività per la salute umana n.c.a.", Category.CLASS),
        Classification("86.99.0", "Altre attività per la salute umana n.c.a.", Category.SUBCLASS),
        Classification("86.99.01", "Tecniche di trattamento del corpo", Category.SUBCLASS),
        Classification("86.99.02", "Danza-movimento terapia", Category.SUBCLASS),
        Classification("86.99.03", "Attività di psicomotricità", Category.SUBCLASS),
        Classification("86.99.09", "Altre attività varie per la salute umana n.c.a.", Category.SUBCLASS),
        Classification("87", "Attività di assistenza residenziale", Category.DIVISION),
        Classification("87.1", "Attività di assistenza infermieristica residenziale", Category.GROUP),
        Classification("87.10", "Attività di assistenza infermieristica residenziale", Category.CLASS),
        Classification("87.10.0", "Attività di assistenza infermieristica residenziale", Category.SUBCLASS),
        Classification("87.10.00", "Attività di assistenza infermieristica residenziale", Category.SUBCLASS),
        Classification(
            "87.2",
            "Attività di assistenza residenziale per persone affette da disturbi mentali o abuso di sostanze",
            Category.GROUP,
        ),
        Classification(
            "87.20",
            "Attività di assistenza residenziale per persone affette da disturbi mentali o abuso di sostanze",
            Category.CLASS,
        ),
        Classification(
            "87.20.0",
            "Attività di assistenza residenziale per persone affette da disturbi mentali o abuso di sostanze",
            Category.SUBCLASS,
        ),
        Classification(
            "87.20.00",
            "Attività di assistenza residenziale per persone affette da disturbi mentali o abuso di sostanze",
            Category.SUBCLASS,
        ),
        Classification(
            "87.3", "Attività di assistenza residenziale per anziani o persone con disabilità fisiche", Category.GROUP
        ),
        Classification(
            "87.30", "Attività di assistenza residenziale per anziani o persone con disabilità fisiche", Category.CLASS
        ),
        Classification(
            "87.30.0",
            "Attività di assistenza residenziale per anziani o persone con disabilità fisiche",
            Category.SUBCLASS,
        ),
        Classification(
            "87.30.00",
            "Attività di assistenza residenziale per anziani o persone con disabilità fisiche",
            Category.SUBCLASS,
        ),
        Classification("87.9", "Altre attività di assistenza residenziale", Category.GROUP),
        Classification(
            "87.91", "Attività di servizi di intermediazione per attività di assistenza residenziale", Category.CLASS
        ),
        Classification(
            "87.91.0",
            "Attività di servizi di intermediazione per attività di assistenza residenziale",
            Category.SUBCLASS,
        ),
        Classification(
            "87.91.00",
            "Attività di servizi di intermediazione per attività di assistenza residenziale",
            Category.SUBCLASS,
        ),
        Classification("87.99", "Altre attività di assistenza residenziale n.c.a.", Category.CLASS),
        Classification("87.99.0", "Altre attività di assistenza residenziale n.c.a.", Category.SUBCLASS),
        Classification("87.99.00", "Altre attività di assistenza residenziale n.c.a.", Category.SUBCLASS),
        Classification("88", "Attività di assistenza sociale non residenziale", Category.DIVISION),
        Classification(
            "88.1",
            "Attività di assistenza sociale non residenziale per anziani o persone con disabilità",
            Category.GROUP,
        ),
        Classification(
            "88.10",
            "Attività di assistenza sociale non residenziale per anziani o persone con disabilità",
            Category.CLASS,
        ),
        Classification(
            "88.10.0",
            "Attività di assistenza sociale non residenziale per anziani o persone con disabilità",
            Category.SUBCLASS,
        ),
        Classification(
            "88.10.00",
            "Attività di assistenza sociale non residenziale per anziani o persone con disabilità",
            Category.SUBCLASS,
        ),
        Classification("88.9", "Altre attività di assistenza sociale non residenziale", Category.GROUP),
        Classification("88.91", "Attività di assistenza diurna per l'infanzia", Category.CLASS),
        Classification("88.91.0", "Attività di assistenza diurna per l'infanzia", Category.SUBCLASS),
        Classification("88.91.00", "Attività di assistenza diurna per l'infanzia", Category.SUBCLASS),
        Classification("88.99", "Altre attività di assistenza sociale non residenziale n.c.a.", Category.CLASS),
        Classification("88.99.0", "Altre attività di assistenza sociale non residenziale n.c.a.", Category.SUBCLASS),
        Classification("88.99.01", "Servizi di counselling", Category.SUBCLASS),
        Classification("88.99.02", "Consulenza familiare", Category.SUBCLASS),
        Classification("88.99.03", "Mediazione culturale e interculturale", Category.SUBCLASS),
        Classification(
            "88.99.04",
            "Altre attività di assistenza sociale non residenziale fornite da pedagogisti",
            Category.SUBCLASS,
        ),
        Classification(
            "88.99.09", "Altre attività varie di assistenza sociale non residenziale n.c.a.", Category.SUBCLASS
        ),
        Classification("S", "ATTIVITÀ ARTISTICHE, SPORTIVE E DI DIVERTIMENTO", Category.SECTION),
        Classification("90", "Attività di creazione artistica e rappresentazioni artistiche", Category.DIVISION),
        Classification("90.1", "Attività di creazione artistica", Category.GROUP),
        Classification("90.11", "Attività di creazione letteraria e composizione musicale", Category.CLASS),
        Classification("90.11.0", "Attività di creazione letteraria e composizione musicale", Category.SUBCLASS),
        Classification("90.11.01", "Attività di giornalisti indipendenti", Category.SUBCLASS),
        Classification("90.11.02", "Attività di blogger indipendenti", Category.SUBCLASS),
        Classification("90.11.09", "Altre attività di creazione letteraria e composizione musicale", Category.SUBCLASS),
        Classification("90.12", "Attività di creazione di arti visive", Category.CLASS),
        Classification("90.12.0", "Attività di creazione di arti visive", Category.SUBCLASS),
        Classification("90.12.00", "Attività di creazione di arti visive", Category.SUBCLASS),
        Classification("90.13", "Altre attività di creazione artistica", Category.CLASS),
        Classification("90.13.0", "Altre attività di creazione artistica", Category.SUBCLASS),
        Classification("90.13.00", "Altre attività di creazione artistica", Category.SUBCLASS),
        Classification("90.2", "Attività di arti performative e rappresentazioni artistiche", Category.GROUP),
        Classification("90.20", "Attività di arti performative e rappresentazioni artistiche", Category.CLASS),
        Classification("90.20.0", "Attività di arti performative e rappresentazioni artistiche", Category.SUBCLASS),
        Classification("90.20.01", "Attività nel campo della recitazione", Category.SUBCLASS),
        Classification(
            "90.20.09", "Altre attività di arti performative e rappresentazioni artistiche", Category.SUBCLASS
        ),
        Classification(
            "90.3",
            "Attività di supporto alle creazioni e alle arti performative e rappresentazioni artistiche",
            Category.GROUP,
        ),
        Classification("90.31", "Gestione di strutture e spazi per le arti", Category.CLASS),
        Classification("90.31.0", "Gestione di strutture e spazi per le arti", Category.SUBCLASS),
        Classification("90.31.00", "Gestione di strutture e spazi per le arti", Category.SUBCLASS),
        Classification(
            "90.39",
            "Altre attività di supporto alle arti performative e alle rappresentazioni artistiche",
            Category.CLASS,
        ),
        Classification(
            "90.39.0",
            "Altre attività di supporto alle arti performative e alle rappresentazioni artistiche",
            Category.SUBCLASS,
        ),
        Classification("90.39.01", "Attività nel campo della regia", Category.SUBCLASS),
        Classification(
            "90.39.09",
            "Altre attività di supporto alle arti performative e alle rappresentazioni artistiche n.c.a.",
            Category.SUBCLASS,
        ),
        Classification("91", "Attività di biblioteche, archivi, musei e altre attività culturali", Category.DIVISION),
        Classification("91.1", "Attività di biblioteche e archivi", Category.GROUP),
        Classification("91.11", "Attività di biblioteche", Category.CLASS),
        Classification("91.11.0", "Attività di biblioteche", Category.SUBCLASS),
        Classification("91.11.00", "Attività di biblioteche", Category.SUBCLASS),
        Classification("91.12", "Attività di archivi", Category.CLASS),
        Classification("91.12.0", "Attività di archivi", Category.SUBCLASS),
        Classification("91.12.00", "Attività di archivi", Category.SUBCLASS),
        Classification("91.2", "Attività di musei, collezioni, luoghi e monumenti storici", Category.GROUP),
        Classification("91.21", "Attività di musei e collezioni", Category.CLASS),
        Classification("91.21.0", "Attività di musei e collezioni", Category.SUBCLASS),
        Classification("91.21.00", "Attività di musei e collezioni", Category.SUBCLASS),
        Classification("91.22", "Attività di luoghi e monumenti storici", Category.CLASS),
        Classification("91.22.0", "Attività di luoghi e monumenti storici", Category.SUBCLASS),
        Classification("91.22.00", "Attività di luoghi e monumenti storici", Category.SUBCLASS),
        Classification(
            "91.3", "Conservazione, restauro e altre attività di supporto al patrimonio culturale", Category.GROUP
        ),
        Classification(
            "91.30", "Conservazione, restauro e altre attività di supporto al patrimonio culturale", Category.CLASS
        ),
        Classification(
            "91.30.0", "Conservazione, restauro e altre attività di supporto al patrimonio culturale", Category.SUBCLASS
        ),
        Classification("91.30.01", "Conservazione e restauro del patrimonio culturale", Category.SUBCLASS),
        Classification(
            "91.30.02",
            "Creazione e gestione di apparecchiature multimediali per l'accompagnamento alle visite in musei e altri siti culturali",
            Category.SUBCLASS,
        ),
        Classification("91.30.09", "Altre attività di supporto al patrimonio culturale", Category.SUBCLASS),
        Classification(
            "91.4", "Attività di orti botanici, giardini zoologici e riserve e parchi naturali", Category.GROUP
        ),
        Classification("91.41", "Attività di orti botanici e giardini zoologici", Category.CLASS),
        Classification("91.41.0", "Attività di orti botanici e giardini zoologici", Category.SUBCLASS),
        Classification("91.41.00", "Attività di orti botanici e giardini zoologici", Category.SUBCLASS),
        Classification("91.42", "Attività di riserve e parchi naturali", Category.CLASS),
        Classification("91.42.0", "Attività di riserve e parchi naturali", Category.SUBCLASS),
        Classification("91.42.00", "Attività di riserve e parchi naturali", Category.SUBCLASS),
        Classification("92", "Attività di scommesse, lotterie e altri giochi d'azzardo", Category.DIVISION),
        Classification("92.0", "Attività di scommesse, lotterie e altri giochi d'azzardo", Category.GROUP),
        Classification("92.00", "Attività di scommesse, lotterie e altri giochi d'azzardo", Category.CLASS),
        Classification("92.00.0", "Attività di scommesse, lotterie e altri giochi d'azzardo", Category.SUBCLASS),
        Classification(
            "92.00.01",
            "Gestione di apparecchi che consentono vincite in denaro funzionanti a moneta o a gettone",
            Category.SUBCLASS,
        ),
        Classification("92.00.09", "Altre attività di scommesse, lotterie e altri giochi d'azzardo", Category.SUBCLASS),
        Classification("93", "Attività sportive, di intrattenimento e divertimento", Category.DIVISION),
        Classification("93.1", "Attività sportive", Category.GROUP),
        Classification("93.11", "Gestione di impianti sportivi", Category.CLASS),
        Classification("93.11.1", "Gestione di piscine", Category.SUBCLASS),
        Classification("93.11.10", "Gestione di piscine", Category.SUBCLASS),
        Classification("93.11.9", "Gestione di altri impianti sportivi", Category.SUBCLASS),
        Classification("93.11.90", "Gestione di altri impianti sportivi", Category.SUBCLASS),
        Classification("93.12", "Attività dei club sportivi", Category.CLASS),
        Classification("93.12.0", "Attività dei club sportivi", Category.SUBCLASS),
        Classification("93.12.00", "Attività dei club sportivi", Category.SUBCLASS),
        Classification("93.13", "Attività dei centri di fitness", Category.CLASS),
        Classification("93.13.0", "Attività dei centri di fitness", Category.SUBCLASS),
        Classification("93.13.01", "Attività di studi di yoga, pilates e Tai Chi", Category.SUBCLASS),
        Classification("93.13.09", "Altre attività dei centri di fitness", Category.SUBCLASS),
        Classification("93.19", "Attività sportive n.c.a.", Category.CLASS),
        Classification(
            "93.19.1", "Attività di organizzazioni ed enti sportivi e promozione di eventi sportivi", Category.SUBCLASS
        ),
        Classification(
            "93.19.10", "Attività di organizzazioni ed enti sportivi e promozione di eventi sportivi", Category.SUBCLASS
        ),
        Classification("93.19.9", "Altre attività sportive n.c.a.", Category.SUBCLASS),
        Classification("93.19.91", "Attività di ricarica di bombole per attività subacquee", Category.SUBCLASS),
        Classification("93.19.92", "Attività di guida alpina", Category.SUBCLASS),
        Classification("93.19.93", "Attività di guida di pesca", Category.SUBCLASS),
        Classification("93.19.99", "Altre attività sportive varie n.c.a.", Category.SUBCLASS),
        Classification("93.2", "Attività di intrattenimento e divertimento", Category.GROUP),
        Classification("93.21", "Attività dei parchi di divertimento e dei parchi tematici", Category.CLASS),
        Classification("93.21.0", "Attività dei parchi di divertimento e dei parchi tematici", Category.SUBCLASS),
        Classification("93.21.00", "Attività dei parchi di divertimento e dei parchi tematici", Category.SUBCLASS),
        Classification("93.29", "Attività di intrattenimento e divertimento n.c.a.", Category.CLASS),
        Classification("93.29.1", "Gestione di piste e sale da ballo", Category.SUBCLASS),
        Classification("93.29.10", "Gestione di piste e sale da ballo", Category.SUBCLASS),
        Classification("93.29.2", "Gestione di stabilimenti balneari", Category.SUBCLASS),
        Classification("93.29.20", "Gestione di stabilimenti balneari", Category.SUBCLASS),
        Classification(
            "93.29.3",
            "Gestione di apparecchi da intrattenimento che non consentono vincite in denaro funzionanti a moneta o a gettone",
            Category.SUBCLASS,
        ),
        Classification(
            "93.29.30",
            "Gestione di apparecchi da intrattenimento che non consentono vincite in denaro funzionanti a moneta o a gettone",
            Category.SUBCLASS,
        ),
        Classification("93.29.9", "Altre attività di intrattenimento e divertimento n.c.a.", Category.SUBCLASS),
        Classification(
            "93.29.91", "Gestione di attrazioni e attività di spettacolo in forma itinerante", Category.SUBCLASS
        ),
        Classification("93.29.99", "Altre attività varie di intrattenimento e divertimento n.c.a.", Category.SUBCLASS),
        Classification("T", "ALTRE ATTIVITÀ DI SERVIZI", Category.SECTION),
        Classification("94", "Attività delle organizzazioni associative", Category.DIVISION),
        Classification(
            "94.1", "Attività di organizzazioni di imprese, dei datori di lavoro e professionali", Category.GROUP
        ),
        Classification("94.11", "Attività di organizzazioni di imprese e dei datori di lavoro", Category.CLASS),
        Classification("94.11.0", "Attività di organizzazioni di imprese e dei datori di lavoro", Category.SUBCLASS),
        Classification("94.11.00", "Attività di organizzazioni di imprese e dei datori di lavoro", Category.SUBCLASS),
        Classification("94.12", "Attività delle organizzazioni professionali", Category.CLASS),
        Classification("94.12.1", "Attività di ordini e collegi professionali", Category.SUBCLASS),
        Classification("94.12.10", "Attività di ordini e collegi professionali", Category.SUBCLASS),
        Classification("94.12.2", "Attività di associazioni professionali", Category.SUBCLASS),
        Classification("94.12.20", "Attività di associazioni professionali", Category.SUBCLASS),
        Classification("94.2", "Attività dei sindacati di lavoratori", Category.GROUP),
        Classification("94.20", "Attività dei sindacati di lavoratori", Category.CLASS),
        Classification("94.20.0", "Attività dei sindacati di lavoratori", Category.SUBCLASS),
        Classification("94.20.00", "Attività dei sindacati di lavoratori", Category.SUBCLASS),
        Classification("94.9", "Attività di altre organizzazioni associative", Category.GROUP),
        Classification("94.91", "Attività delle organizzazioni religiose", Category.CLASS),
        Classification("94.91.0", "Attività delle organizzazioni religiose", Category.SUBCLASS),
        Classification("94.91.00", "Attività delle organizzazioni religiose", Category.SUBCLASS),
        Classification("94.92", "Attività delle organizzazioni politiche", Category.CLASS),
        Classification("94.92.0", "Attività delle organizzazioni politiche", Category.SUBCLASS),
        Classification("94.92.00", "Attività delle organizzazioni politiche", Category.SUBCLASS),
        Classification("94.99", "Attività di altre organizzazioni associative n.c.a.", Category.CLASS),
        Classification(
            "94.99.1",
            "Attività di organizzazioni associative per la tutela degli interessi e dei diritti dei cittadini",
            Category.SUBCLASS,
        ),
        Classification(
            "94.99.10",
            "Attività di organizzazioni associative per la tutela degli interessi e dei diritti dei cittadini",
            Category.SUBCLASS,
        ),
        Classification("94.99.2", "Attività di organizzazioni associative culturali e ricreative", Category.SUBCLASS),
        Classification("94.99.20", "Attività di organizzazioni associative culturali e ricreative", Category.SUBCLASS),
        Classification("94.99.3", "Attività di organizzazioni associative a scopo patriottico", Category.SUBCLASS),
        Classification("94.99.30", "Attività di organizzazioni associative a scopo patriottico", Category.SUBCLASS),
        Classification(
            "94.99.4", "Attività di organizzazioni associative per la cooperazione internazionale", Category.SUBCLASS
        ),
        Classification(
            "94.99.40", "Attività di organizzazioni associative per la cooperazione internazionale", Category.SUBCLASS
        ),
        Classification("94.99.5", "Attività di organizzazioni associative filantropiche", Category.SUBCLASS),
        Classification("94.99.50", "Attività di organizzazioni associative filantropiche", Category.SUBCLASS),
        Classification(
            "94.99.6",
            "Attività di organizzazioni associative per la promozione e la difesa degli animali e dell'ambiente",
            Category.SUBCLASS,
        ),
        Classification(
            "94.99.60",
            "Attività di organizzazioni associative per la promozione e la difesa degli animali e dell'ambiente",
            Category.SUBCLASS,
        ),
        Classification("94.99.9", "Attività di altre organizzazioni associative varie n.c.a.", Category.SUBCLASS),
        Classification("94.99.90", "Attività di altre organizzazioni associative varie n.c.a.", Category.SUBCLASS),
        Classification(
            "95",
            "Riparazione e manutenzione di computer, beni per uso personale e per la casa, autoveicoli e motocicli",
            Category.DIVISION,
        ),
        Classification(
            "95.1", "Riparazione e manutenzione di computer e di apparecchiature per le comunicazioni", Category.GROUP
        ),
        Classification(
            "95.10", "Riparazione e manutenzione di computer e di apparecchiature per le comunicazioni", Category.CLASS
        ),
        Classification("95.10.1", "Riparazione e manutenzione di computer e periferiche", Category.SUBCLASS),
        Classification("95.10.10", "Riparazione e manutenzione di computer e periferiche", Category.SUBCLASS),
        Classification(
            "95.10.2", "Riparazione e manutenzione di apparecchiature per le comunicazioni", Category.SUBCLASS
        ),
        Classification("95.10.21", "Riparazione e manutenzione di telefoni e tablet", Category.SUBCLASS),
        Classification(
            "95.10.29", "Riparazione e manutenzione di altre apparecchiature per le comunicazioni", Category.SUBCLASS
        ),
        Classification("95.2", "Riparazione e manutenzione di beni per uso personale e per la casa", Category.GROUP),
        Classification("95.21", "Riparazione e manutenzione di prodotti di elettronica di consumo", Category.CLASS),
        Classification(
            "95.21.0", "Riparazione e manutenzione di prodotti di elettronica di consumo", Category.SUBCLASS
        ),
        Classification(
            "95.21.00", "Riparazione e manutenzione di prodotti di elettronica di consumo", Category.SUBCLASS
        ),
        Classification(
            "95.22",
            "Riparazione e manutenzione di elettrodomestici e di articoli per la casa e il giardinaggio",
            Category.CLASS,
        ),
        Classification(
            "95.22.0",
            "Riparazione e manutenzione di elettrodomestici e di articoli per la casa e il giardinaggio",
            Category.SUBCLASS,
        ),
        Classification("95.22.01", "Riparazione e manutenzione di elettrodomestici", Category.SUBCLASS),
        Classification(
            "95.22.02", "Riparazione e manutenzione di articoli per la casa e il giardinaggio", Category.SUBCLASS
        ),
        Classification("95.23", "Riparazione e manutenzione di calzature e articoli in pelle", Category.CLASS),
        Classification("95.23.0", "Riparazione e manutenzione di calzature e articoli in pelle", Category.SUBCLASS),
        Classification("95.23.00", "Riparazione e manutenzione di calzature e articoli in pelle", Category.SUBCLASS),
        Classification(
            "95.24", "Riparazione e manutenzione di mobili e di oggetti di arredamento per la casa", Category.CLASS
        ),
        Classification(
            "95.24.0", "Riparazione e manutenzione di mobili e di oggetti di arredamento per la casa", Category.SUBCLASS
        ),
        Classification(
            "95.24.01", "Rivestimento di mobili e oggetti di arredamento per la casa imbottiti", Category.SUBCLASS
        ),
        Classification(
            "95.24.09",
            "Altre attività di riparazione e manutenzione di mobili e di oggetti di arredamento per la casa",
            Category.SUBCLASS,
        ),
        Classification("95.25", "Riparazione e manutenzione di orologi e gioielli", Category.CLASS),
        Classification("95.25.0", "Riparazione e manutenzione di orologi e gioielli", Category.SUBCLASS),
        Classification("95.25.00", "Riparazione e manutenzione di orologi e gioielli", Category.SUBCLASS),
        Classification(
            "95.29", "Riparazione e manutenzione di beni per uso personale e per la casa n.c.a.", Category.CLASS
        ),
        Classification("95.29.1", "Riparazione e accordatura di strumenti musicali non storici", Category.SUBCLASS),
        Classification("95.29.10", "Riparazione e accordatura di strumenti musicali non storici", Category.SUBCLASS),
        Classification(
            "95.29.2",
            "Riparazione e manutenzione di biciclette, articoli sportivi e attrezzature da campeggio",
            Category.SUBCLASS,
        ),
        Classification("95.29.21", "Riparazione e manutenzione di biciclette", Category.SUBCLASS),
        Classification(
            "95.29.22", "Riparazione e manutenzione di articoli sportivi e attrezzature da campeggio", Category.SUBCLASS
        ),
        Classification("95.29.3", "Riparazione e modifica di articoli di abbigliamento", Category.SUBCLASS),
        Classification("95.29.30", "Riparazione e modifica di articoli di abbigliamento", Category.SUBCLASS),
        Classification(
            "95.29.9",
            "Riparazione e manutenzione di altri beni per uso personale e per la casa n.c.a.",
            Category.SUBCLASS,
        ),
        Classification(
            "95.29.91",
            "Affilatura di coltelli, servizi di duplicazione di chiavi e di incisione rapida",
            Category.SUBCLASS,
        ),
        Classification(
            "95.29.99",
            "Riparazione e manutenzione di altri beni vari per uso personale e per la casa n.c.a.",
            Category.SUBCLASS,
        ),
        Classification("95.3", "Riparazione e manutenzione di autoveicoli e motocicli", Category.GROUP),
        Classification("95.31", "Riparazione e manutenzione di autoveicoli", Category.CLASS),
        Classification(
            "95.31.1",
            "Riparazione e manutenzione meccanica, elettrica ed elettronica di autoveicoli",
            Category.SUBCLASS,
        ),
        Classification(
            "95.31.10",
            "Riparazione e manutenzione meccanica, elettrica ed elettronica di autoveicoli",
            Category.SUBCLASS,
        ),
        Classification("95.31.2", "Riparazione e manutenzione di carrozzerie di autoveicoli", Category.SUBCLASS),
        Classification("95.31.20", "Riparazione e manutenzione di carrozzerie di autoveicoli", Category.SUBCLASS),
        Classification(
            "95.31.3",
            "Riparazione, montaggio o sostituzione di pneumatici e camere d'aria di autoveicoli",
            Category.SUBCLASS,
        ),
        Classification(
            "95.31.30",
            "Riparazione, montaggio o sostituzione di pneumatici e camere d'aria di autoveicoli",
            Category.SUBCLASS,
        ),
        Classification(
            "95.31.9", "Lavaggio e altre attività di riparazione e manutenzione di autoveicoli", Category.SUBCLASS
        ),
        Classification("95.31.91", "Lavaggio di autoveicoli", Category.SUBCLASS),
        Classification(
            "95.31.92", "Riparazione e manutenzione di cellule abitative per caravan e autocaravan", Category.SUBCLASS
        ),
        Classification(
            "95.31.99", "Altre attività di riparazione e manutenzione di autoveicoli n.c.a.", Category.SUBCLASS
        ),
        Classification("95.32", "Riparazione e manutenzione di motocicli", Category.CLASS),
        Classification("95.32.0", "Riparazione e manutenzione di motocicli", Category.SUBCLASS),
        Classification("95.32.00", "Riparazione e manutenzione di motocicli", Category.SUBCLASS),
        Classification(
            "95.4",
            "Attività di servizi di intermediazione per la riparazione e la manutenzione di computer, beni per uso personale e per la casa, autoveicoli e motocicli",
            Category.GROUP,
        ),
        Classification(
            "95.40",
            "Attività di servizi di intermediazione per la riparazione e la manutenzione di computer, beni per uso personale e per la casa, autoveicoli e motocicli",
            Category.CLASS,
        ),
        Classification(
            "95.40.0",
            "Attività di servizi di intermediazione per la riparazione e la manutenzione di computer, beni per uso personale e per la casa, autoveicoli e motocicli",
            Category.SUBCLASS,
        ),
        Classification(
            "95.40.00",
            "Attività di servizi di intermediazione per la riparazione e la manutenzione di computer, beni per uso personale e per la casa, autoveicoli e motocicli",
            Category.SUBCLASS,
        ),
        Classification("96", "Attività di servizi alla persona", Category.DIVISION),
        Classification("96.1", "Servizi di lavaggio e pulitura di prodotti tessili e pellicce", Category.GROUP),
        Classification("96.10", "Servizi di lavaggio e pulitura di prodotti tessili e pellicce", Category.CLASS),
        Classification(
            "96.10.1", "Lavaggio e pulitura di prodotti tessili forniti da lavanderie industriali", Category.SUBCLASS
        ),
        Classification(
            "96.10.11",
            "Lavaggio e pulitura di prodotti tessili forniti da lavanderie industriali per industrie, ospedali e altre strutture simili",
            Category.SUBCLASS,
        ),
        Classification(
            "96.10.12",
            "Lavaggio e pulitura di prodotti tessili forniti da lavanderie industriali per ristorazione, alberghi e altri servizi di alloggio",
            Category.SUBCLASS,
        ),
        Classification(
            "96.10.2",
            "Lavaggio e pulitura di prodotti tessili e pellicce forniti da lavanderie e tintorie non industriali",
            Category.SUBCLASS,
        ),
        Classification(
            "96.10.21",
            "Lavaggio e pulitura di prodotti tessili e pellicce forniti da lavanderie e tintorie tradizionali",
            Category.SUBCLASS,
        ),
        Classification(
            "96.10.22",
            "Lavaggio e pulitura di prodotti tessili e pellicce forniti da lavanderie self-service",
            Category.SUBCLASS,
        ),
        Classification(
            "96.2",
            "Servizi di parrucchieri e barbieri, trattamenti di bellezza, centri benessere e attività simili",
            Category.GROUP,
        ),
        Classification("96.21", "Servizi di parrucchieri e barbieri", Category.CLASS),
        Classification("96.21.0", "Servizi di parrucchieri e barbieri", Category.SUBCLASS),
        Classification("96.21.00", "Servizi di parrucchieri e barbieri", Category.SUBCLASS),
        Classification("96.22", "Servizi di cura della bellezza e altri trattamenti di bellezza", Category.CLASS),
        Classification("96.22.0", "Servizi di cura della bellezza e altri trattamenti di bellezza", Category.SUBCLASS),
        Classification("96.22.01", "Servizi di manicure e pedicure", Category.SUBCLASS),
        Classification(
            "96.22.09", "Altri servizi di cura della bellezza e altri trattamenti di bellezza n.c.a.", Category.SUBCLASS
        ),
        Classification("96.23", "Servizi di centri benessere, sauna e bagno di vapore", Category.CLASS),
        Classification("96.23.1", "Servizi di centri termali", Category.SUBCLASS),
        Classification("96.23.10", "Servizi di centri termali", Category.SUBCLASS),
        Classification("96.23.9", "Altri servizi di centri benessere, sauna e bagno di vapore", Category.SUBCLASS),
        Classification("96.23.91", "Terapia del sale", Category.SUBCLASS),
        Classification(
            "96.23.99", "Altri servizi di centri benessere, sauna e bagno di vapore n.c.a.", Category.SUBCLASS
        ),
        Classification("96.3", "Servizi funerari e attività connesse", Category.GROUP),
        Classification("96.30", "Servizi funerari e attività connesse", Category.CLASS),
        Classification("96.30.0", "Servizi funerari e attività connesse", Category.SUBCLASS),
        Classification("96.30.01", "Servizi di pompe funebri", Category.SUBCLASS),
        Classification("96.30.02", "Servizi di sepoltura", Category.SUBCLASS),
        Classification("96.30.09", "Servizi funerari e attività connesse n.c.a.", Category.SUBCLASS),
        Classification("96.4", "Attività di servizi di intermediazione per servizi alla persona", Category.GROUP),
        Classification("96.40", "Attività di servizi di intermediazione per servizi alla persona", Category.CLASS),
        Classification("96.40.0", "Attività di servizi di intermediazione per servizi alla persona", Category.SUBCLASS),
        Classification(
            "96.40.00", "Attività di servizi di intermediazione per servizi alla persona", Category.SUBCLASS
        ),
        Classification("96.9", "Altre attività di servizi alla persona", Category.GROUP),
        Classification("96.91", "Fornitura di servizi domestici", Category.CLASS),
        Classification("96.91.0", "Fornitura di servizi domestici", Category.SUBCLASS),
        Classification("96.91.00", "Fornitura di servizi domestici", Category.SUBCLASS),
        Classification("96.99", "Altre attività di servizi alla persona n.c.a.", Category.CLASS),
        Classification("96.99.1", "Servizi di cura per animali da compagnia", Category.SUBCLASS),
        Classification(
            "96.99.11", "Servizi di presa in pensione e custodia per animali da compagnia", Category.SUBCLASS
        ),
        Classification("96.99.12", "Servizi di toelettatura per animali da compagnia", Category.SUBCLASS),
        Classification("96.99.13", "Servizi di addestramento per animali da compagnia", Category.SUBCLASS),
        Classification("96.99.14", "Gestione di rifugi per animali", Category.SUBCLASS),
        Classification("96.99.19", "Servizi di cura per animali da compagnia n.c.a.", Category.SUBCLASS),
        Classification("96.99.9", "Altre attività varie di servizi alla persona n.c.a.", Category.SUBCLASS),
        Classification("96.99.91", "Attività di studi di tatuaggi e piercing", Category.SUBCLASS),
        Classification("96.99.92", "Servizi di incontro ed eventi simili", Category.SUBCLASS),
        Classification("96.99.93", "Servizi di organizzazione di feste e cerimonie", Category.SUBCLASS),
        Classification("96.99.94", "Servizi di consulenza di immagine", Category.SUBCLASS),
        Classification("96.99.99", "Tutte le altre attività varie di servizi alla persona n.c.a.", Category.SUBCLASS),
        Classification(
            "U",
            "ATTIVITÀ DI FAMIGLIE E CONVIVENZE COME DATORI DI LAVORO PER PERSONALE DOMESTICO E PRODUZIONE DI BENI E SERVIZI INDIFFERENZIATI PER USO PROPRIO DA PARTE DI FAMIGLIE E CONVIVENZE",
            Category.SECTION,
        ),
        Classification(
            "97", "Attività di famiglie e convivenze come datori di lavoro per personale domestico", Category.DIVISION
        ),
        Classification(
            "97.0", "Attività di famiglie e convivenze come datori di lavoro per personale domestico", Category.GROUP
        ),
        Classification(
            "97.00", "Attività di famiglie e convivenze come datori di lavoro per personale domestico", Category.CLASS
        ),
        Classification(
            "97.00.1", "Attività di condomini come datori di lavoro per personale domestico", Category.SUBCLASS
        ),
        Classification(
            "97.00.10", "Attività di condomini come datori di lavoro per personale domestico", Category.SUBCLASS
        ),
        Classification(
            "97.00.9",
            "Attività di famiglie e convivenze come datori di lavoro per personale domestico n.c.a.",
            Category.SUBCLASS,
        ),
        Classification(
            "97.00.90",
            "Attività di famiglie e convivenze come datori di lavoro per personale domestico n.c.a.",
            Category.SUBCLASS,
        ),
        Classification(
            "98",
            "Produzione di beni e di servizi indifferenziati per uso proprio da parte di famiglie e convivenze",
            Category.DIVISION,
        ),
        Classification(
            "98.1",
            "Produzione di beni indifferenziati per uso proprio da parte di famiglie e convivenze",
            Category.GROUP,
        ),
        Classification(
            "98.10",
            "Produzione di beni indifferenziati per uso proprio da parte di famiglie e convivenze",
            Category.CLASS,
        ),
        Classification(
            "98.10.0",
            "Produzione di beni indifferenziati per uso proprio da parte di famiglie e convivenze",
            Category.SUBCLASS,
        ),
        Classification(
            "98.10.00",
            "Produzione di beni indifferenziati per uso proprio da parte di famiglie e convivenze",
            Category.SUBCLASS,
        ),
        Classification(
            "98.2",
            "Produzione di servizi indifferenziati per uso proprio da parte di famiglie e convivenze",
            Category.GROUP,
        ),
        Classification(
            "98.20",
            "Produzione di servizi indifferenziati per uso proprio da parte di famiglie e convivenze",
            Category.CLASS,
        ),
        Classification(
            "98.20.0",
            "Produzione di servizi indifferenziati per uso proprio da parte di famiglie e convivenze",
            Category.SUBCLASS,
        ),
        Classification(
            "98.20.00",
            "Produzione di servizi indifferenziati per uso proprio da parte di famiglie e convivenze",
            Category.SUBCLASS,
        ),
        Classification("V", "ATTIVITÀ DI ORGANIZZAZIONI E ORGANISMI EXTRATERRITORIALI", Category.SECTION),
        Classification("99", "Attività di organizzazioni e organismi extraterritoriali", Category.DIVISION),
        Classification("99.0", "Attività di organizzazioni e organismi extraterritoriali", Category.GROUP),
        Classification("99.00", "Attività di organizzazioni e organismi extraterritoriali", Category.CLASS),
        Classification("99.00.0", "Attività di organizzazioni e organismi extraterritoriali", Category.SUBCLASS),
        Classification("99.00.00", "Attività di organizzazioni e organismi extraterritoriali", Category.SUBCLASS),
    ],
)
