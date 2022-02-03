"""`CNAE2 Standard <https://concla.ibge.gov.br/classificacoes/correspondencias/atividades-economicas.html>`_."""

from ...types import Category, Classification, Standard, Standards

CNAE2 = Standard(
    standard=Standards.CNAE2,
    classes=[
        Classification("A", "AGRICULTURA, PECUÁRIA, PRODUÇÃO FLORESTAL, PESCA E AQÜICULTURA", Category.SECTION),
        Classification("01", "AGRICULTURA, PECUÁRIA E SERVIÇOS RELACIONADOS", Category.DIVISION),
        Classification("01.1", "Produção de lavouras temporárias", Category.GROUP),
        Classification("01.11-3", "Cultivo de cereais", Category.CLASS),
        Classification(
            "01.12-1", "Cultivo de algodão herbáceo e de outras fibras de lavoura temporária", Category.CLASS
        ),
        Classification("01.13-0", "Cultivo de cana-de-açúcar", Category.CLASS),
        Classification("01.14-8", "Cultivo de fumo", Category.CLASS),
        Classification("01.15-6", "Cultivo de soja", Category.CLASS),
        Classification("01.16-4", "Cultivo de oleaginosas de lavoura temporária, exceto soja", Category.CLASS),
        Classification(
            "01.19-9", "Cultivo de plantas de lavoura temporária não especificadas anteriormente", Category.CLASS
        ),
        Classification("01.2", "Horticultura e floricultura", Category.GROUP),
        Classification("01.21-1", "Horticultura", Category.CLASS),
        Classification("01.22-9", "Cultivo de flores e plantas ornamentais", Category.CLASS),
        Classification("01.3", "Produção de lavouras permanentes", Category.GROUP),
        Classification("01.31-8", "Cultivo de laranja", Category.CLASS),
        Classification("01.32-6", "Cultivo de uva", Category.CLASS),
        Classification("01.33-4", "Cultivo de frutas de lavoura permanente, exceto laranja e uva", Category.CLASS),
        Classification("01.34-2", "Cultivo de café", Category.CLASS),
        Classification("01.35-1", "Cultivo de cacau", Category.CLASS),
        Classification(
            "01.39-3", "Cultivo de plantas de lavoura permanente não especificadas anteriormente", Category.CLASS
        ),
        Classification("01.4", "Produção de sementes e mudas certificadas", Category.GROUP),
        Classification("01.41-5", "Produção de sementes certificadas", Category.CLASS),
        Classification(
            "01.42-3", "Produção de mudas e outras formas de propagação vegetal, certificadas", Category.CLASS
        ),
        Classification("01.5", "Pecuária", Category.GROUP),
        Classification("01.51-2", "Criação de bovinos", Category.CLASS),
        Classification("01.52-1", "Criação de outros animais de grande porte", Category.CLASS),
        Classification("01.53-9", "Criação de caprinos e ovinos", Category.CLASS),
        Classification("01.54-7", "Criação de suínos", Category.CLASS),
        Classification("01.55-5", "Criação de aves", Category.CLASS),
        Classification("01.59-8", "Criação de animais não especificados anteriormente", Category.CLASS),
        Classification(
            "01.6", "Atividades de apoio à agricultura e à pecuária; atividades de pós-colheita", Category.GROUP
        ),
        Classification("01.61-0", "Atividades de apoio à agricultura", Category.CLASS),
        Classification("01.62-8", "Atividades de apoio à pecuária", Category.CLASS),
        Classification("01.63-6", "Atividades de pós-colheita", Category.CLASS),
        Classification("01.7", "Caça e serviços relacionados", Category.GROUP),
        Classification("01.70-9", "Caça e serviços relacionados", Category.CLASS),
        Classification("02", "PRODUÇÃO FLORESTAL", Category.DIVISION),
        Classification("02.1", "Produção florestal - florestas plantadas", Category.GROUP),
        Classification("02.10-1", "Produção florestal - florestas plantadas", Category.CLASS),
        Classification("02.2", "Produção florestal - florestas nativas", Category.GROUP),
        Classification("02.20-9", "Produção florestal - florestas nativas", Category.CLASS),
        Classification("02.3", "Atividades de apoio à produção florestal", Category.GROUP),
        Classification("02.30-6", "Atividades de apoio à produção florestal", Category.CLASS),
        Classification("03", "PESCA E AQÜICULTURA", Category.DIVISION),
        Classification("03.1", "Pesca", Category.GROUP),
        Classification("03.11-6", "Pesca em água salgada", Category.CLASS),
        Classification("03.12-4", "Pesca em água doce", Category.CLASS),
        Classification("03.2", "Aqüicultura", Category.GROUP),
        Classification("03.21-3", "Aqüicultura em água salgada e salobra", Category.CLASS),
        Classification("03.22-1", "Aqüicultura em água doce", Category.CLASS),
        Classification("B", "INDÚSTRIAS EXTRATIVAS", Category.SECTION),
        Classification("05", "EXTRAÇÃO DE CARVÃO MINERAL", Category.DIVISION),
        Classification("05.0", "Extração de carvão mineral", Category.GROUP),
        Classification("05.00-3", "Extração de carvão mineral", Category.CLASS),
        Classification("06", "EXTRAÇÃO DE PETRÓLEO E GÁS NATURAL", Category.DIVISION),
        Classification("06.0", "Extração de petróleo e gás natural", Category.GROUP),
        Classification("06.00-0", "Extração de petróleo e gás natural", Category.CLASS),
        Classification("07", "EXTRAÇÃO DE MINERAIS METÁLICOS", Category.DIVISION),
        Classification("07.1", "Extração de minério de ferro", Category.GROUP),
        Classification("07.10-3", "Extração de minério de ferro", Category.CLASS),
        Classification("07.2", "Extração de minerais metálicos não-ferrosos", Category.GROUP),
        Classification("07.21-9", "Extração de minério de alumínio", Category.CLASS),
        Classification("07.22-7", "Extração de minério de estanho", Category.CLASS),
        Classification("07.23-5", "Extração de minério de manganês", Category.CLASS),
        Classification("07.24-3", "Extração de minério de metais preciosos", Category.CLASS),
        Classification("07.25-1", "Extração de minerais radioativos", Category.CLASS),
        Classification(
            "07.29-4", "Extração de minerais metálicos não-ferrosos não especificados anteriormente", Category.CLASS
        ),
        Classification("08", "EXTRAÇÃO DE MINERAIS NÃO-METÁLICOS", Category.DIVISION),
        Classification("08.1", "Extração de pedra, areia e argila", Category.GROUP),
        Classification("08.10-0", "Extração de pedra, areia e argila", Category.CLASS),
        Classification("08.9", "Extração de outros minerais não-metálicos", Category.GROUP),
        Classification(
            "08.91-6",
            "Extração de minerais para fabricação de adubos, fertilizantes e outros produtos químicos",
            Category.CLASS,
        ),
        Classification("08.92-4", "Extração e refino de sal marinho e sal-gema", Category.CLASS),
        Classification("08.93-2", "Extração de gemas (pedras preciosas e semipreciosas)", Category.CLASS),
        Classification("08.99-1", "Extração de minerais não-metálicos não especificados anteriormente", Category.CLASS),
        Classification("09", "ATIVIDADES DE APOIO À EXTRAÇÃO DE MINERAIS", Category.DIVISION),
        Classification("09.1", "Atividades de apoio à extração de petróleo e gás natural", Category.GROUP),
        Classification("09.10-6", "Atividades de apoio à extração de petróleo e gás natural", Category.CLASS),
        Classification(
            "09.9", "Atividades de apoio à extração de minerais, exceto petróleo e gás natural", Category.GROUP
        ),
        Classification(
            "09.90-4", "Atividades de apoio à extração de minerais, exceto petróleo e gás natural", Category.CLASS
        ),
        Classification("C", "INDÚSTRIAS DE TRANSFORMAÇÃO", Category.SECTION),
        Classification("10", "FABRICAÇÃO DE PRODUTOS ALIMENTÍCIOS", Category.DIVISION),
        Classification("10.1", "Abate e fabricação de produtos de carne", Category.GROUP),
        Classification("10.11-2", "Abate de reses, exceto suínos", Category.CLASS),
        Classification("10.12-1", "Abate de suínos, aves e outros pequenos animais", Category.CLASS),
        Classification("10.13-9", "Fabricação de produtos de carne", Category.CLASS),
        Classification("10.2", "Preservação do pescado e fabricação de produtos do pescado", Category.GROUP),
        Classification("10.20-1", "Preservação do pescado e fabricação de produtos do pescado", Category.CLASS),
        Classification("10.3", "Fabricação de conservas de frutas, legumes e outros vegetais", Category.GROUP),
        Classification("10.31-7", "Fabricação de conservas de frutas", Category.CLASS),
        Classification("10.32-5", "Fabricação de conservas de legumes e outros vegetais", Category.CLASS),
        Classification("10.33-3", "Fabricação de sucos de frutas, hortaliças e legumes", Category.CLASS),
        Classification("10.4", "Fabricação de óleos e gorduras vegetais e animais", Category.GROUP),
        Classification("10.41-4", "Fabricação de óleos vegetais em bruto, exceto óleo de milho", Category.CLASS),
        Classification("10.42-2", "Fabricação de óleos vegetais refinados, exceto óleo de milho", Category.CLASS),
        Classification(
            "10.43-1",
            "Fabricação de margarina e outras gorduras vegetais e de óleos não-comestíveis de animais",
            Category.CLASS,
        ),
        Classification("10.5", "Laticínios", Category.GROUP),
        Classification("10.51-1", "Preparação do leite", Category.CLASS),
        Classification("10.52-0", "Fabricação de laticínios", Category.CLASS),
        Classification("10.53-8", "Fabricação de sorvetes e outros gelados comestíveis", Category.CLASS),
        Classification("10.6", "Moagem, fabricação de produtos amiláceos e de alimentos para animais", Category.GROUP),
        Classification("10.61-9", "Beneficiamento de arroz e fabricação de produtos do arroz", Category.CLASS),
        Classification("10.62-7", "Moagem de trigo e fabricação de derivados", Category.CLASS),
        Classification("10.63-5", "Fabricação de farinha de mandioca e derivados", Category.CLASS),
        Classification("10.64-3", "Fabricação de farinha de milho e derivados, exceto óleos de milho", Category.CLASS),
        Classification("10.65-1", "Fabricação de amidos e féculas de vegetais e de óleos de milho", Category.CLASS),
        Classification("10.66-0", "Fabricação de alimentos para animais", Category.CLASS),
        Classification(
            "10.69-4",
            "Moagem e fabricação de produtos de origem vegetal não especificados anteriormente",
            Category.CLASS,
        ),
        Classification("10.7", "Fabricação e refino de açúcar", Category.GROUP),
        Classification("10.71-6", "Fabricação de açúcar em bruto", Category.CLASS),
        Classification("10.72-4", "Fabricação de açúcar refinado", Category.CLASS),
        Classification("10.8", "Torrefação e moagem de café", Category.GROUP),
        Classification("10.81-3", "Torrefação e moagem de café", Category.CLASS),
        Classification("10.82-1", "Fabricação de produtos à base de café", Category.CLASS),
        Classification("10.9", "Fabricação de outros produtos alimentícios", Category.GROUP),
        Classification("10.91-1", "Fabricação de produtos de panificação", Category.CLASS),
        Classification("10.92-9", "Fabricação de biscoitos e bolachas", Category.CLASS),
        Classification(
            "10.93-7", "Fabricação de produtos derivados do cacau, de chocolates e confeitos", Category.CLASS
        ),
        Classification("10.94-5", "Fabricação de massas alimentícias", Category.CLASS),
        Classification("10.95-3", "Fabricação de especiarias, molhos, temperos e condimentos", Category.CLASS),
        Classification("10.96-1", "Fabricação de alimentos e pratos prontos", Category.CLASS),
        Classification(
            "10.99-6", "Fabricação de produtos alimentícios não especificados anteriormente", Category.CLASS
        ),
        Classification("11", "FABRICAÇÃO DE BEBIDAS", Category.DIVISION),
        Classification("11.1", "Fabricação de bebidas alcoólicas", Category.GROUP),
        Classification("11.11-9", "Fabricação de aguardentes e outras bebidas destiladas", Category.CLASS),
        Classification("11.12-7", "Fabricação de vinho", Category.CLASS),
        Classification("11.13-5", "Fabricação de malte, cervejas e chopes", Category.CLASS),
        Classification("11.2", "Fabricação de bebidas não-alcoólicas", Category.GROUP),
        Classification("11.21-6", "Fabricação de águas envasadas", Category.CLASS),
        Classification("11.22-4", "Fabricação de refrigerantes e de outras bebidas não-alcoólicas", Category.CLASS),
        Classification("12", "FABRICAÇÃO DE PRODUTOS DO FUMO", Category.DIVISION),
        Classification("12.1", "Processamento industrial do fumo", Category.GROUP),
        Classification("12.10-7", "Processamento industrial do fumo", Category.CLASS),
        Classification("12.2", "Fabricação de produtos do fumo", Category.GROUP),
        Classification("12.20-4", "Fabricação de produtos do fumo", Category.CLASS),
        Classification("13", "FABRICAÇÃO DE PRODUTOS TÊXTEIS", Category.DIVISION),
        Classification("13.1", "Preparação e fiação de fibras têxteis", Category.GROUP),
        Classification("13.11-1", "Preparação e fiação de fibras de algodão", Category.CLASS),
        Classification("13.12-0", "Preparação e fiação de fibras têxteis naturais, exceto algodão", Category.CLASS),
        Classification("13.13-8", "Fiação de fibras artificiais e sintéticas", Category.CLASS),
        Classification("13.14-6", "Fabricação de linhas para costurar e bordar", Category.CLASS),
        Classification("13.2", "Tecelagem, exceto malha", Category.GROUP),
        Classification("13.21-9", "Tecelagem de fios de algodão", Category.CLASS),
        Classification("13.22-7", "Tecelagem de fios de fibras têxteis naturais, exceto algodão", Category.CLASS),
        Classification("13.23-5", "Tecelagem de fios de fibras artificiais e sintéticas", Category.CLASS),
        Classification("13.3", "Fabricação de tecidos de malha", Category.GROUP),
        Classification("13.30-8", "Fabricação de tecidos de malha", Category.CLASS),
        Classification("13.4", "Acabamentos em fios, tecidos e artefatos têxteis", Category.GROUP),
        Classification("13.40-5", "Acabamentos em fios, tecidos e artefatos têxteis", Category.CLASS),
        Classification("13.5", "Fabricação de artefatos têxteis, exceto vestuário", Category.GROUP),
        Classification("13.51-1", "Fabricação de artefatos têxteis para uso doméstico", Category.CLASS),
        Classification("13.52-9", "Fabricação de artefatos de tapeçaria", Category.CLASS),
        Classification("13.53-7", "Fabricação de artefatos de cordoaria", Category.CLASS),
        Classification("13.54-5", "Fabricação de tecidos especiais, inclusive artefatos", Category.CLASS),
        Classification(
            "13.59-6", "Fabricação de outros produtos têxteis não especificados anteriormente", Category.CLASS
        ),
        Classification("14", "CONFECÇÃO DE ARTIGOS DO VESTUÁRIO E ACESSÓRIOS", Category.DIVISION),
        Classification("14.1", "Confecção de artigos do vestuário e acessórios", Category.GROUP),
        Classification("14.11-8", "Confecção de roupas íntimas", Category.CLASS),
        Classification("14.12-6", "Confecção de peças do vestuário, exceto roupas íntimas", Category.CLASS),
        Classification("14.13-4", "Confecção de roupas profissionais", Category.CLASS),
        Classification(
            "14.14-2", "Fabricação de acessórios do vestuário, exceto para segurança e proteção", Category.CLASS
        ),
        Classification("14.2", "Fabricação de artigos de malharia e tricotagem", Category.GROUP),
        Classification("14.21-5", "Fabricação de meias", Category.CLASS),
        Classification(
            "14.22-3",
            "Fabricação de artigos do vestuário, produzidos em malharias e tricotagens, exceto meias",
            Category.CLASS,
        ),
        Classification(
            "15",
            "PREPARAÇÃO DE COUROS E FABRICAÇÃO DE ARTEFATOS DE COURO, ARTIGOS PARA VIAGEM E CALÇADOS",
            Category.DIVISION,
        ),
        Classification("15.1", "Curtimento e outras preparações de couro", Category.GROUP),
        Classification("15.10-6", "Curtimento e outras preparações de couro", Category.CLASS),
        Classification("15.2", "Fabricação de artigos para viagem e de artefatos diversos de couro", Category.GROUP),
        Classification(
            "15.21-1", "Fabricação de artigos para viagem, bolsas e semelhantes de qualquer material", Category.CLASS
        ),
        Classification("15.29-7", "Fabricação de artefatos de couro não especificados anteriormente", Category.CLASS),
        Classification("15.3", "Fabricação de calçados", Category.GROUP),
        Classification("15.31-9", "Fabricação de calçados de couro", Category.CLASS),
        Classification("15.32-7", "Fabricação de tênis de qualquer material", Category.CLASS),
        Classification("15.33-5", "Fabricação de calçados de material sintético", Category.CLASS),
        Classification(
            "15.39-4", "Fabricação de calçados de materiais não especificados anteriormente", Category.CLASS
        ),
        Classification("15.4", "Fabricação de partes para calçados, de qualquer material", Category.GROUP),
        Classification("15.40-8", "Fabricação de partes para calçados, de qualquer material", Category.CLASS),
        Classification("16", "FABRICAÇÃO DE PRODUTOS DE MADEIRA", Category.DIVISION),
        Classification("16.1", "Desdobramento de madeira", Category.GROUP),
        Classification("16.10-2", "Desdobramento de madeira", Category.CLASS),
        Classification(
            "16.2", "Fabricação de produtos de madeira, cortiça e material trançado, exceto móveis", Category.GROUP
        ),
        Classification(
            "16.21-8",
            "Fabricação de madeira laminada e de chapas de madeira compensada, prensada e aglomerada",
            Category.CLASS,
        ),
        Classification(
            "16.22-6", "Fabricação de estruturas de madeira e de artigos de carpintaria para construção", Category.CLASS
        ),
        Classification("16.23-4", "Fabricação de artefatos de tanoaria e de embalagens de madeira", Category.CLASS),
        Classification(
            "16.29-3",
            "Fabricação de artefatos de madeira, palha, cortiça, vime e material trançado não especificados anteriormente, exceto móveis",
            Category.CLASS,
        ),
        Classification("17", "FABRICAÇÃO DE CELULOSE, PAPEL E PRODUTOS DE PAPEL", Category.DIVISION),
        Classification("17.1", "Fabricação de celulose e outras pastas para a fabricação de papel", Category.GROUP),
        Classification("17.10-9", "Fabricação de celulose e outras pastas para a fabricação de papel", Category.CLASS),
        Classification("17.2", "Fabricação de papel, cartolina e papel-cartão", Category.GROUP),
        Classification("17.21-4", "Fabricação de papel", Category.CLASS),
        Classification("17.22-2", "Fabricação de cartolina e papel-cartão", Category.CLASS),
        Classification(
            "17.3", "Fabricação de embalagens de papel, cartolina, papel-cartão e papelão ondulado", Category.GROUP
        ),
        Classification("17.31-1", "Fabricação de embalagens de papel", Category.CLASS),
        Classification("17.32-0", "Fabricação de embalagens de cartolina e papel-cartão", Category.CLASS),
        Classification("17.33-8", "Fabricação de chapas e de embalagens de papelão ondulado", Category.CLASS),
        Classification(
            "17.4",
            "Fabricação de produtos diversos de papel, cartolina, papel-cartão e papelão ondulado",
            Category.GROUP,
        ),
        Classification(
            "17.41-9",
            "Fabricação de produtos de papel, cartolina, papel-cartão e papelão ondulado para uso comercial e de escritório",
            Category.CLASS,
        ),
        Classification(
            "17.42-7", "Fabricação de produtos de papel para usos doméstico e higiênico-sanitário", Category.CLASS
        ),
        Classification(
            "17.49-4",
            "Fabricação de produtos de pastas celulósicas, papel, cartolina, papel-cartão e papelão ondulado não especificados anteriormente",
            Category.CLASS,
        ),
        Classification("18", "IMPRESSÃO E REPRODUÇÃO DE GRAVAÇÕES", Category.DIVISION),
        Classification("18.1", "Atividade de impressão", Category.GROUP),
        Classification(
            "18.11-3", "Impressão de jornais, livros, revistas e outras publicações periódicas", Category.CLASS
        ),
        Classification("18.12-1", "Impressão de material de segurança", Category.CLASS),
        Classification("18.13-0", "Impressão de materiais para outros usos", Category.CLASS),
        Classification("18.2", "Serviços de pré-impressão e acabamentos gráficos", Category.GROUP),
        Classification("18.21-1", "Serviços de pré-impressão", Category.CLASS),
        Classification("18.22-9", "Serviços de acabamentos gráficos", Category.CLASS),
        Classification("18.3", "Reprodução de materiais gravados em qualquer suporte", Category.GROUP),
        Classification("18.30-0", "Reprodução de materiais gravados em qualquer suporte", Category.CLASS),
        Classification(
            "19", "FABRICAÇÃO DE COQUE, DE PRODUTOS DERIVADOS DO PETRÓLEO E DE BIOCOMBUSTÍVEIS", Category.DIVISION
        ),
        Classification("19.1", "Coquerias", Category.GROUP),
        Classification("19.10-1", "Coquerias", Category.CLASS),
        Classification("19.2", "Fabricação de produtos derivados do petróleo", Category.GROUP),
        Classification("19.21-7", "Fabricação de produtos do refino de petróleo", Category.CLASS),
        Classification(
            "19.22-5", "Fabricação de produtos derivados do petróleo, exceto produtos do refino", Category.CLASS
        ),
        Classification("19.3", "Fabricação de biocombustíveis", Category.GROUP),
        Classification("19.31-4", "Fabricação de álcool", Category.CLASS),
        Classification("19.32-2", "Fabricação de biocombustíveis, exceto álcool", Category.CLASS),
        Classification("20", "FABRICAÇÃO DE PRODUTOS QUÍMICOS", Category.DIVISION),
        Classification("20.1", "Fabricação de produtos químicos inorgânicos", Category.GROUP),
        Classification("20.11-8", "Fabricação de cloro e álcalis", Category.CLASS),
        Classification("20.12-6", "Fabricação de intermediários para fertilizantes", Category.CLASS),
        Classification("20.13-4", "Fabricação de adubos e fertilizantes", Category.CLASS),
        Classification("20.14-2", "Fabricação de gases industriais", Category.CLASS),
        Classification(
            "20.19-3", "Fabricação de produtos químicos inorgânicos não especificados anteriormente", Category.CLASS
        ),
        Classification("20.2", "Fabricação de produtos químicos orgânicos", Category.GROUP),
        Classification("20.21-5", "Fabricação de produtos petroquímicos básicos", Category.CLASS),
        Classification("20.22-3", "Fabricação de intermediários para plastificantes, resinas e fibras", Category.CLASS),
        Classification(
            "20.29-1", "Fabricação de produtos químicos orgânicos não especificados anteriormente", Category.CLASS
        ),
        Classification("20.3", "Fabricação de resinas e elastômeros", Category.GROUP),
        Classification("20.31-2", "Fabricação de resinas termoplásticas", Category.CLASS),
        Classification("20.32-1", "Fabricação de resinas termofixas", Category.CLASS),
        Classification("20.33-9", "Fabricação de elastômeros", Category.CLASS),
        Classification("20.4", "Fabricação de fibras artificiais e sintéticas", Category.GROUP),
        Classification("20.40-1", "Fabricação de fibras artificiais e sintéticas", Category.CLASS),
        Classification("20.5", "Fabricação de defensivos agrícolas e desinfestantes domissanitários", Category.GROUP),
        Classification("20.51-7", "Fabricação de defensivos agrícolas", Category.CLASS),
        Classification("20.52-5", "Fabricação de desinfestantes domissanitários", Category.CLASS),
        Classification(
            "20.6",
            "Fabricação de sabões, detergentes, produtos de limpeza, cosméticos, produtos de perfumaria e de higiene pessoal",
            Category.GROUP,
        ),
        Classification("20.61-4", "Fabricação de sabões e detergentes sintéticos", Category.CLASS),
        Classification("20.62-2", "Fabricação de produtos de limpeza e polimento", Category.CLASS),
        Classification(
            "20.63-1", "Fabricação de cosméticos, produtos de perfumaria e de higiene pessoal", Category.CLASS
        ),
        Classification("20.7", "Fabricação de tintas, vernizes, esmaltes, lacas e produtos afins", Category.GROUP),
        Classification("20.71-1", "Fabricação de tintas, vernizes, esmaltes e lacas", Category.CLASS),
        Classification("20.72-0", "Fabricação de tintas de impressão", Category.CLASS),
        Classification("20.73-8", "Fabricação de impermeabilizantes, solventes e produtos afins", Category.CLASS),
        Classification("20.9", "Fabricação de produtos e preparados químicos diversos", Category.GROUP),
        Classification("20.91-6", "Fabricação de adesivos e selantes", Category.CLASS),
        Classification("20.92-4", "Fabricação de explosivos", Category.CLASS),
        Classification("20.93-2", "Fabricação de aditivos de uso industrial", Category.CLASS),
        Classification("20.94-1", "Fabricação de catalisadores", Category.CLASS),
        Classification("20.99-1", "Fabricação de produtos químicos não especificados anteriormente", Category.CLASS),
        Classification("21", "FABRICAÇÃO DE PRODUTOS FARMOQUÍMICOS E FARMACÊUTICOS", Category.DIVISION),
        Classification("21.1", "Fabricação de produtos farmoquímicos", Category.GROUP),
        Classification("21.10-6", "Fabricação de produtos farmoquímicos", Category.CLASS),
        Classification("21.2", "Fabricação de produtos farmacêuticos", Category.GROUP),
        Classification("21.21-1", "Fabricação de medicamentos para uso humano", Category.CLASS),
        Classification("21.22-0", "Fabricação de medicamentos para uso veterinário", Category.CLASS),
        Classification("21.23-8", "Fabricação de preparações farmacêuticas", Category.CLASS),
        Classification("22", "FABRICAÇÃO DE PRODUTOS DE BORRACHA E DE MATERIAL PLÁSTICO", Category.DIVISION),
        Classification("22.1", "Fabricação de produtos de borracha", Category.GROUP),
        Classification("22.11-1", "Fabricação de pneumáticos e de câmaras-de-ar", Category.CLASS),
        Classification("22.12-9", "Reforma de pneumáticos usados", Category.CLASS),
        Classification(
            "22.19-6", "Fabricação de artefatos de borracha não especificados anteriormente", Category.CLASS
        ),
        Classification("22.2", "Fabricação de produtos de material plástico", Category.GROUP),
        Classification("22.21-8", "Fabricação de laminados planos e tubulares de material plástico", Category.CLASS),
        Classification("22.22-6", "Fabricação de embalagens de material plástico", Category.CLASS),
        Classification(
            "22.23-4", "Fabricação de tubos e acessórios de material plástico para uso na construção", Category.CLASS
        ),
        Classification(
            "22.29-3", "Fabricação de artefatos de material plástico não especificados anteriormente", Category.CLASS
        ),
        Classification("23", "FABRICAÇÃO DE PRODUTOS DE MINERAIS NÃO-METÁLICOS", Category.DIVISION),
        Classification("23.1", "Fabricação de vidro e de produtos do vidro", Category.GROUP),
        Classification("23.11-7", "Fabricação de vidro plano e de segurança", Category.CLASS),
        Classification("23.12-5", "Fabricação de embalagens de vidro", Category.CLASS),
        Classification("23.19-2", "Fabricação de artigos de vidro", Category.CLASS),
        Classification("23.2", "Fabricação de cimento", Category.GROUP),
        Classification("23.20-6", "Fabricação de cimento", Category.CLASS),
        Classification(
            "23.3",
            "Fabricação de artefatos de concreto, cimento, fibrocimento, gesso e materiais semelhantes",
            Category.GROUP,
        ),
        Classification(
            "23.30-3",
            "Fabricação de artefatos de concreto, cimento, fibrocimento, gesso e materiais semelhantes",
            Category.CLASS,
        ),
        Classification("23.4", "Fabricação de produtos cerâmicos", Category.GROUP),
        Classification("23.41-9", "Fabricação de produtos cerâmicos refratários", Category.CLASS),
        Classification(
            "23.42-7",
            "Fabricação de produtos cerâmicos não-refratários para uso estrutural na construção",
            Category.CLASS,
        ),
        Classification(
            "23.49-4",
            "Fabricação de produtos cerâmicos não-refratários não especificados anteriormente",
            Category.CLASS,
        ),
        Classification(
            "23.9", "Aparelhamento de pedras e fabricação de outros produtos de minerais não-metálicos", Category.GROUP
        ),
        Classification("23.91-5", "Aparelhamento e outros trabalhos em pedras", Category.CLASS),
        Classification("23.92-3", "Fabricação de cal e gesso", Category.CLASS),
        Classification(
            "23.99-1",
            "Fabricação de produtos de minerais não-metálicos não especificados anteriormente",
            Category.CLASS,
        ),
        Classification("24", "METALURGIA", Category.DIVISION),
        Classification("24.1", "Produção de ferro-gusa e de ferroligas", Category.GROUP),
        Classification("24.11-3", "Produção de ferro-gusa", Category.CLASS),
        Classification("24.12-1", "Produção de ferroligas", Category.CLASS),
        Classification("24.2", "Siderurgia", Category.GROUP),
        Classification("24.21-1", "Produção de semi-acabados de aço", Category.CLASS),
        Classification("24.22-9", "Produção de laminados planos de aço", Category.CLASS),
        Classification("24.23-7", "Produção de laminados longos de aço", Category.CLASS),
        Classification("24.24-5", "Produção de relaminados, trefilados e perfilados de aço", Category.CLASS),
        Classification("24.3", "Produção de tubos de aço, exceto tubos sem costura", Category.GROUP),
        Classification("24.31-8", "Produção de tubos de aço com costura", Category.CLASS),
        Classification("24.39-3", "Produção de outros tubos de ferro e aço", Category.CLASS),
        Classification("24.4", "Metalurgia dos metais não-ferrosos", Category.GROUP),
        Classification("24.41-5", "Metalurgia do alumínio e suas ligas", Category.CLASS),
        Classification("24.42-3", "Metalurgia dos metais preciosos", Category.CLASS),
        Classification("24.43-1", "Metalurgia do cobre", Category.CLASS),
        Classification(
            "24.49-1", "Metalurgia dos metais não-ferrosos e suas ligas não especificados anteriormente", Category.CLASS
        ),
        Classification("24.5", "Fundição", Category.GROUP),
        Classification("24.51-2", "Fundição de ferro e aço", Category.CLASS),
        Classification("24.52-1", "Fundição de metais não-ferrosos e suas ligas", Category.CLASS),
        Classification("25", "FABRICAÇÃO DE PRODUTOS DE METAL, EXCETO MÁQUINAS E EQUIPAMENTOS", Category.DIVISION),
        Classification("25.1", "Fabricação de estruturas metálicas e obras de caldeiraria pesada", Category.GROUP),
        Classification("25.11-0", "Fabricação de estruturas metálicas", Category.CLASS),
        Classification("25.12-8", "Fabricação de esquadrias de metal", Category.CLASS),
        Classification("25.13-6", "Fabricação de obras de caldeiraria pesada", Category.CLASS),
        Classification("25.2", "Fabricação de tanques, reservatórios metálicos e caldeiras", Category.GROUP),
        Classification(
            "25.21-7",
            "Fabricação de tanques, reservatórios metálicos e caldeiras para aquecimento central",
            Category.CLASS,
        ),
        Classification(
            "25.22-5",
            "Fabricação de caldeiras geradoras de vapor, exceto para aquecimento central e para veículos",
            Category.CLASS,
        ),
        Classification(
            "25.3", "Forjaria, estamparia, metalurgia do pó e serviços de tratamento de metais", Category.GROUP
        ),
        Classification("25.31-4", "Produção de forjados de aço e de metais não-ferrosos e suas ligas", Category.CLASS),
        Classification("25.32-2", "Produção de artefatos estampados de metal; metalurgia do pó", Category.CLASS),
        Classification("25.39-0", "Serviços de usinagem, solda, tratamento e revestimento em metais", Category.CLASS),
        Classification("25.4", "Fabricação de artigos de cutelaria, de serralheria e ferramentas", Category.GROUP),
        Classification("25.41-1", "Fabricação de artigos de cutelaria", Category.CLASS),
        Classification("25.42-0", "Fabricação de artigos de serralheria, exceto esquadrias", Category.CLASS),
        Classification("25.43-8", "Fabricação de ferramentas", Category.CLASS),
        Classification("25.5", "Fabricação de equipamento bélico pesado, armas e munições", Category.GROUP),
        Classification("25.50-1", "Fabricação de equipamento bélico pesado, armas e munições", Category.CLASS),
        Classification("25.9", "Fabricação de produtos de metal não especificados anteriormente", Category.GROUP),
        Classification("25.91-8", "Fabricação de embalagens metálicas", Category.CLASS),
        Classification("25.92-6", "Fabricação de produtos de trefilados de metal", Category.CLASS),
        Classification("25.93-4", "Fabricação de artigos de metal para uso doméstico e pessoal", Category.CLASS),
        Classification("25.99-3", "Fabricação de produtos de metal não especificados anteriormente", Category.CLASS),
        Classification(
            "26", "FABRICAÇÃO DE EQUIPAMENTOS DE INFORMÁTICA, PRODUTOS ELETRÔNICOS E ÓPTICOS", Category.DIVISION
        ),
        Classification("26.1", "Fabricação de componentes eletrônicos", Category.GROUP),
        Classification("26.10-8", "Fabricação de componentes eletrônicos", Category.CLASS),
        Classification("26.2", "Fabricação de equipamentos de informática e periféricos", Category.GROUP),
        Classification("26.21-3", "Fabricação de equipamentos de informática", Category.CLASS),
        Classification("26.22-1", "Fabricação de periféricos para equipamentos de informática", Category.CLASS),
        Classification("26.3", "Fabricação de equipamentos de comunicação", Category.GROUP),
        Classification("26.31-1", "Fabricação de equipamentos transmissores de comunicação", Category.CLASS),
        Classification(
            "26.32-9", "Fabricação de aparelhos telefônicos e de outros equipamentos de comunicação", Category.CLASS
        ),
        Classification(
            "26.4",
            "Fabricação de aparelhos de recepção, reprodução, gravação e amplificação de áudio e vídeo",
            Category.GROUP,
        ),
        Classification(
            "26.40-0",
            "Fabricação de aparelhos de recepção, reprodução, gravação e amplificação de áudio e vídeo",
            Category.CLASS,
        ),
        Classification(
            "26.5",
            "Fabricação de aparelhos e instrumentos de medida, teste e controle; cronômetros e relógios",
            Category.GROUP,
        ),
        Classification("26.51-5", "Fabricação de aparelhos e equipamentos de medida, teste e controle", Category.CLASS),
        Classification("26.52-3", "Fabricação de cronômetros e relógios", Category.CLASS),
        Classification(
            "26.6",
            "Fabricação de aparelhos eletromédicos e eletroterapêuticos e equipamentos de irradiação",
            Category.GROUP,
        ),
        Classification(
            "26.60-4",
            "Fabricação de aparelhos eletromédicos e eletroterapêuticos e equipamentos de irradiação",
            Category.CLASS,
        ),
        Classification(
            "26.7", "Fabricação de equipamentos e instrumentos ópticos, fotográficos e cinematográficos", Category.GROUP
        ),
        Classification(
            "26.70-1",
            "Fabricação de equipamentos e instrumentos ópticos, fotográficos e cinematográficos",
            Category.CLASS,
        ),
        Classification("26.8", "Fabricação de mídias virgens, magnéticas e ópticas", Category.GROUP),
        Classification("26.80-9", "Fabricação de mídias virgens, magnéticas e ópticas", Category.CLASS),
        Classification("27", "FABRICAÇÃO DE MÁQUINAS, APARELHOS E MATERIAIS ELÉTRICOS", Category.DIVISION),
        Classification("27.1", "Fabricação de geradores, transformadores e motores elétricos", Category.GROUP),
        Classification("27.10-4", "Fabricação de geradores, transformadores e motores elétricos", Category.CLASS),
        Classification("27.2", "Fabricação de pilhas, baterias e acumuladores elétricos", Category.GROUP),
        Classification(
            "27.21-0",
            "Fabricação de pilhas, baterias e acumuladores elétricos, exceto para veículos automotores",
            Category.CLASS,
        ),
        Classification("27.22-8", "Fabricação de baterias e acumuladores para veículos automotores", Category.CLASS),
        Classification(
            "27.3", "Fabricação de equipamentos para distribuição e controle de energia elétrica", Category.GROUP
        ),
        Classification(
            "27.31-7",
            "Fabricação de aparelhos e equipamentos para distribuição e controle de energia elétrica",
            Category.CLASS,
        ),
        Classification(
            "27.32-5", "Fabricação de material elétrico para instalações em circuito de consumo", Category.CLASS
        ),
        Classification("27.33-3", "Fabricação de fios, cabos e condutores elétricos isolados", Category.CLASS),
        Classification("27.4", "Fabricação de lâmpadas e outros equipamentos de iluminação", Category.GROUP),
        Classification("27.40-6", "Fabricação de lâmpadas e outros equipamentos de iluminação", Category.CLASS),
        Classification("27.5", "Fabricação de eletrodomésticos", Category.GROUP),
        Classification(
            "27.51-1",
            "Fabricação de fogões, refrigeradores e máquinas de lavar e secar para uso doméstico",
            Category.CLASS,
        ),
        Classification(
            "27.59-7", "Fabricação de aparelhos eletrodomésticos não especificados anteriormente", Category.CLASS
        ),
        Classification(
            "27.9", "Fabricação de equipamentos e aparelhos elétricos não especificados anteriormente", Category.GROUP
        ),
        Classification(
            "27.90-2",
            "Fabricação de equipamentos e aparelhos elétricos não especificados anteriormente",
            Category.CLASS,
        ),
        Classification("28", "FABRICAÇÃO DE MÁQUINAS E EQUIPAMENTOS", Category.DIVISION),
        Classification(
            "28.1", "Fabricação de motores, bombas, compressores e equipamentos de transmissão", Category.GROUP
        ),
        Classification(
            "28.11-9", "Fabricação de motores e turbinas, exceto para aviões e veículos rodoviários", Category.CLASS
        ),
        Classification(
            "28.12-7", "Fabricação de equipamentos hidráulicos e pneumáticos, exceto válvulas", Category.CLASS
        ),
        Classification("28.13-5", "Fabricação de válvulas, registros e dispositivos semelhantes", Category.CLASS),
        Classification("28.14-3", "Fabricação de compressores", Category.CLASS),
        Classification("28.15-1", "Fabricação de equipamentos de transmissão para fins industriais", Category.CLASS),
        Classification("28.2", "Fabricação de máquinas e equipamentos de uso geral", Category.GROUP),
        Classification("28.21-6", "Fabricação de aparelhos e equipamentos para instalações térmicas", Category.CLASS),
        Classification(
            "28.22-4",
            "Fabricação de máquinas, equipamentos e aparelhos para transporte e elevação de cargas e pessoas",
            Category.CLASS,
        ),
        Classification(
            "28.23-2",
            "Fabricação de máquinas e aparelhos de refrigeração e ventilação para uso industrial e comercial",
            Category.CLASS,
        ),
        Classification("28.24-1", "Fabricação de aparelhos e equipamentos de ar condicionado", Category.CLASS),
        Classification(
            "28.25-9", "Fabricação de máquinas e equipamentos para saneamento básico e ambiental", Category.CLASS
        ),
        Classification(
            "28.29-1",
            "Fabricação de máquinas e equipamentos de uso geral não especificados anteriormente",
            Category.CLASS,
        ),
        Classification(
            "28.3", "Fabricação de tratores e de máquinas e equipamentos para a agricultura e pecuária", Category.GROUP
        ),
        Classification("28.31-3", "Fabricação de tratores agrícolas", Category.CLASS),
        Classification("28.32-1", "Fabricação de equipamentos para irrigação agrícola", Category.CLASS),
        Classification(
            "28.33-0",
            "Fabricação de máquinas e equipamentos para a agricultura e pecuária, exceto para irrigação",
            Category.CLASS,
        ),
        Classification("28.4", "Fabricação de máquinas-ferramenta", Category.GROUP),
        Classification("28.40-2", "Fabricação de máquinas-ferramenta", Category.CLASS),
        Classification(
            "28.5", "Fabricação de máquinas e equipamentos de uso na extração mineral e na construção", Category.GROUP
        ),
        Classification(
            "28.51-8", "Fabricação de máquinas e equipamentos para a prospecção e extração de petróleo", Category.CLASS
        ),
        Classification(
            "28.52-6",
            "Fabricação de outras máquinas e equipamentos para uso na extração mineral, exceto na extração de petróleo",
            Category.CLASS,
        ),
        Classification("28.53-4", "Fabricação de tratores, exceto agrícolas", Category.CLASS),
        Classification(
            "28.54-2",
            "Fabricação de máquinas e equipamentos para terraplenagem, pavimentação e construção, exceto tratores",
            Category.CLASS,
        ),
        Classification("28.6", "Fabricação de máquinas e equipamentos de uso industrial específico", Category.GROUP),
        Classification(
            "28.61-5", "Fabricação de máquinas para a indústria metalúrgica, exceto máquinas-ferramenta", Category.CLASS
        ),
        Classification(
            "28.62-3",
            "Fabricação de máquinas e equipamentos para as indústrias de alimentos, bebidas e fumo",
            Category.CLASS,
        ),
        Classification("28.63-1", "Fabricação de máquinas e equipamentos para a indústria têxtil", Category.CLASS),
        Classification(
            "28.64-0",
            "Fabricação de máquinas e equipamentos para as indústrias do vestuário, do couro e de calçados",
            Category.CLASS,
        ),
        Classification(
            "28.65-8",
            "Fabricação de máquinas e equipamentos para as indústrias de celulose, papel e papelão e artefatos",
            Category.CLASS,
        ),
        Classification("28.66-6", "Fabricação de máquinas e equipamentos para a indústria do plástico", Category.CLASS),
        Classification(
            "28.69-1",
            "Fabricação de máquinas e equipamentos para uso industrial específico não especificados anteriormente",
            Category.CLASS,
        ),
        Classification("29", "FABRICAÇÃO DE VEÍCULOS AUTOMOTORES, REBOQUES E CARROCERIAS", Category.DIVISION),
        Classification("29.1", "Fabricação de automóveis, camionetas e utilitários", Category.GROUP),
        Classification("29.10-7", "Fabricação de automóveis, camionetas e utilitários", Category.CLASS),
        Classification("29.2", "Fabricação de caminhões e ônibus", Category.GROUP),
        Classification("29.20-4", "Fabricação de caminhões e ônibus", Category.CLASS),
        Classification(
            "29.3", "Fabricação de cabines, carrocerias e reboques para veículos automotores", Category.GROUP
        ),
        Classification(
            "29.30-1", "Fabricação de cabines, carrocerias e reboques para veículos automotores", Category.CLASS
        ),
        Classification("29.4", "Fabricação de peças e acessórios para veículos automotores", Category.GROUP),
        Classification(
            "29.41-7", "Fabricação de peças e acessórios para o sistema motor de veículos automotores", Category.CLASS
        ),
        Classification(
            "29.42-5",
            "Fabricação de peças e acessórios para os sistemas de marcha e transmissão de veículos automotores",
            Category.CLASS,
        ),
        Classification(
            "29.43-3",
            "Fabricação de peças e acessórios para o sistema de freios de veículos automotores",
            Category.CLASS,
        ),
        Classification(
            "29.44-1",
            "Fabricação de peças e acessórios para o sistema de direção e suspensão de veículos automotores",
            Category.CLASS,
        ),
        Classification(
            "29.45-0",
            "Fabricação de material elétrico e eletrônico para veículos automotores, exceto baterias",
            Category.CLASS,
        ),
        Classification(
            "29.49-2",
            "Fabricação de peças e acessórios para veículos automotores não especificados anteriormente",
            Category.CLASS,
        ),
        Classification("29.5", "Recondicionamento e recuperação de motores para veículos automotores", Category.GROUP),
        Classification(
            "29.50-6", "Recondicionamento e recuperação de motores para veículos automotores", Category.CLASS
        ),
        Classification(
            "30", "FABRICAÇÃO DE OUTROS EQUIPAMENTOS DE TRANSPORTE, EXCETO VEÍCULOS AUTOMOTORES", Category.DIVISION
        ),
        Classification("30.1", "Construção de embarcações", Category.GROUP),
        Classification("30.11-3", "Construção de embarcações e estruturas flutuantes", Category.CLASS),
        Classification("30.12-1", "Construção de embarcações para esporte e lazer", Category.CLASS),
        Classification("30.3", "Fabricação de veículos ferroviários", Category.GROUP),
        Classification("30.31-8", "Fabricação de locomotivas, vagões e outros materiais rodantes", Category.CLASS),
        Classification("30.32-6", "Fabricação de peças e acessórios para veículos ferroviários", Category.CLASS),
        Classification("30.4", "Fabricação de aeronaves", Category.GROUP),
        Classification("30.41-5", "Fabricação de aeronaves", Category.CLASS),
        Classification(
            "30.42-3", "Fabricação de turbinas, motores e outros componentes e peças para aeronaves", Category.CLASS
        ),
        Classification("30.5", "Fabricação de veículos militares de combate", Category.GROUP),
        Classification("30.50-4", "Fabricação de veículos militares de combate", Category.CLASS),
        Classification(
            "30.9", "Fabricação de equipamentos de transporte não especificados anteriormente", Category.GROUP
        ),
        Classification("30.91-1", "Fabricação de motocicletas", Category.CLASS),
        Classification("30.92-0", "Fabricação de bicicletas e triciclos não-motorizados", Category.CLASS),
        Classification(
            "30.99-7", "Fabricação de equipamentos de transporte não especificados anteriormente", Category.CLASS
        ),
        Classification("31", "FABRICAÇÃO DE MÓVEIS", Category.DIVISION),
        Classification("31.0", "Fabricação de móveis", Category.GROUP),
        Classification("31.01-2", "Fabricação de móveis com predominância de madeira", Category.CLASS),
        Classification("31.02-1", "Fabricação de móveis com predominância de metal", Category.CLASS),
        Classification("31.03-9", "Fabricação de móveis de outros materiais, exceto madeira e metal", Category.CLASS),
        Classification("31.04-7", "Fabricação de colchões", Category.CLASS),
        Classification("32", "FABRICAÇÃO DE PRODUTOS DIVERSOS", Category.DIVISION),
        Classification("32.1", "Fabricação de artigos de joalheria, bijuteria e semelhantes", Category.GROUP),
        Classification(
            "32.11-6", "Lapidação de gemas e fabricação de artefatos de ourivesaria e joalheria", Category.CLASS
        ),
        Classification("32.12-4", "Fabricação de bijuterias e artefatos semelhantes", Category.CLASS),
        Classification("32.2", "Fabricação de instrumentos musicais", Category.GROUP),
        Classification("32.20-5", "Fabricação de instrumentos musicais", Category.CLASS),
        Classification("32.3", "Fabricação de artefatos para pesca e esporte", Category.GROUP),
        Classification("32.30-2", "Fabricação de artefatos para pesca e esporte", Category.CLASS),
        Classification("32.4", "Fabricação de brinquedos e jogos recreativos", Category.GROUP),
        Classification("32.40-0", "Fabricação de brinquedos e jogos recreativos", Category.CLASS),
        Classification(
            "32.5",
            "Fabricação de instrumentos e materiais para uso médico e odontológico e de artigos ópticos",
            Category.GROUP,
        ),
        Classification(
            "32.50-7",
            "Fabricação de instrumentos e materiais para uso médico e odontológico e de artigos ópticos",
            Category.CLASS,
        ),
        Classification("32.9", "Fabricação de produtos diversos", Category.GROUP),
        Classification("32.91-4", "Fabricação de escovas, pincéis e vassouras", Category.CLASS),
        Classification(
            "32.92-2",
            "Fabricação de equipamentos e acessórios para segurança e proteção pessoal e profissional",
            Category.CLASS,
        ),
        Classification("32.99-0", "Fabricação de produtos diversos não especificados anteriormente", Category.CLASS),
        Classification("33", "MANUTENÇÃO, REPARAÇÃO E INSTALAÇÃO DE MÁQUINAS E EQUIPAMENTOS", Category.DIVISION),
        Classification("33.1", "Manutenção e reparação de máquinas e equipamentos", Category.GROUP),
        Classification(
            "33.11-2",
            "Manutenção e reparação de tanques, reservatórios metálicos e caldeiras, exceto para veículos",
            Category.CLASS,
        ),
        Classification("33.12-1", "Manutenção e reparação de equipamentos eletrônicos e ópticos", Category.CLASS),
        Classification("33.13-9", "Manutenção e reparação de máquinas e equipamentos elétricos", Category.CLASS),
        Classification(
            "33.14-7", "Manutenção e reparação de máquinas e equipamentos da indústria mecânica", Category.CLASS
        ),
        Classification("33.15-5", "Manutenção e reparação de veículos ferroviários", Category.CLASS),
        Classification("33.16-3", "Manutenção e reparação de aeronaves", Category.CLASS),
        Classification("33.17-1", "Manutenção e reparação de embarcações", Category.CLASS),
        Classification(
            "33.19-8",
            "Manutenção e reparação de equipamentos e produtos não especificados anteriormente",
            Category.CLASS,
        ),
        Classification("33.2", "Instalação de máquinas e equipamentos", Category.GROUP),
        Classification("33.21-0", "Instalação de máquinas e equipamentos industriais", Category.CLASS),
        Classification("33.29-5", "Instalação de equipamentos não especificados anteriormente", Category.CLASS),
        Classification("D", "ELETRICIDADE E GÁS", Category.SECTION),
        Classification("35", "ELETRICIDADE, GÁS E OUTRAS UTILIDADES", Category.DIVISION),
        Classification("35.1", "Geração, transmissão e distribuição de energia elétrica", Category.GROUP),
        Classification("35.11-5", "Geração de energia elétrica", Category.CLASS),
        Classification("35.12-3", "Transmissão de energia elétrica", Category.CLASS),
        Classification("35.13-1", "Comércio atacadista de energia elétrica", Category.CLASS),
        Classification("35.14-0", "Distribuição de energia elétrica", Category.CLASS),
        Classification("35.2", "Produção e distribuição de combustíveis gasosos por redes urbanas", Category.GROUP),
        Classification(
            "35.20-4",
            "Produção de gás; processamento de gás natural; distribuição de combustíveis gasosos por redes urbanas",
            Category.CLASS,
        ),
        Classification("35.3", "Produção e distribuição de vapor, água quente e ar condicionado", Category.GROUP),
        Classification("35.30-1", "Produção e distribuição de vapor, água quente e ar condicionado", Category.CLASS),
        Classification("E", "ÁGUA, ESGOTO, ATIVIDADES DE GESTÃO DE RESÍDUOS E DESCONTAMINAÇÃO", Category.SECTION),
        Classification("36", "CAPTAÇÃO, TRATAMENTO E DISTRIBUIÇÃO DE ÁGUA", Category.DIVISION),
        Classification("36.0", "Captação, tratamento e distribuição de água", Category.GROUP),
        Classification("36.00-6", "Captação, tratamento e distribuição de água", Category.CLASS),
        Classification("37", "ESGOTO E ATIVIDADES RELACIONADAS", Category.DIVISION),
        Classification("37.0", "Esgoto e atividades relacionadas", Category.GROUP),
        Classification("37.01-1", "Gestão de redes de esgoto", Category.CLASS),
        Classification("37.02-9", "Atividades relacionadas a esgoto, exceto a gestão de redes", Category.CLASS),
        Classification(
            "38", "COLETA, TRATAMENTO E DISPOSIÇÃO DE RESÍDUOS; RECUPERAÇÃO DE MATERIAIS", Category.DIVISION
        ),
        Classification("38.1", "Coleta de resíduos", Category.GROUP),
        Classification("38.11-4", "Coleta de resíduos não-perigosos", Category.CLASS),
        Classification("38.12-2", "Coleta de resíduos perigosos", Category.CLASS),
        Classification("38.2", "Tratamento e disposição de resíduos", Category.GROUP),
        Classification("38.21-1", "Tratamento e disposição de resíduos não-perigosos", Category.CLASS),
        Classification("38.22-0", "Tratamento e disposição de resíduos perigosos", Category.CLASS),
        Classification("38.3", "Recuperação de materiais", Category.GROUP),
        Classification("38.31-9", "Recuperação de materiais metálicos", Category.CLASS),
        Classification("38.32-7", "Recuperação de materiais plásticos", Category.CLASS),
        Classification("38.39-4", "Recuperação de materiais não especificados anteriormente", Category.CLASS),
        Classification("39", "DESCONTAMINAÇÃO E OUTROS SERVIÇOS DE GESTÃO DE RESÍDUOS", Category.DIVISION),
        Classification("39.0", "Descontaminação e outros serviços de gestão de resíduos", Category.GROUP),
        Classification("39.00-5", "Descontaminação e outros serviços de gestão de resíduos", Category.CLASS),
        Classification("F", "CONSTRUÇÃO", Category.SECTION),
        Classification("41", "CONSTRUÇÃO DE EDIFÍCIOS", Category.DIVISION),
        Classification("41.1", "Incorporação de empreendimentos imobiliários", Category.GROUP),
        Classification("41.10-7", "Incorporação de empreendimentos imobiliários", Category.CLASS),
        Classification("41.2", "Construção de edifícios", Category.GROUP),
        Classification("41.20-4", "Construção de edifícios", Category.CLASS),
        Classification("42", "OBRAS DE INFRA-ESTRUTURA", Category.DIVISION),
        Classification(
            "42.1", "Construção de rodovias, ferrovias, obras urbanas e obras-de-arte especiais", Category.GROUP
        ),
        Classification("42.11-1", "Construção de rodovias e ferrovias", Category.CLASS),
        Classification("42.12-0", "Construção de obras-de-arte especiais", Category.CLASS),
        Classification("42.13-8", "Obras de urbanização - ruas, praças e calçadas", Category.CLASS),
        Classification(
            "42.2",
            "Obras de infra-estrutura para energia elétrica, telecomunicações, água, esgoto e transporte por dutos",
            Category.GROUP,
        ),
        Classification(
            "42.21-9", "Obras para geração e distribuição de energia elétrica e para telecomunicações", Category.CLASS
        ),
        Classification(
            "42.22-7",
            "Construção de redes de abastecimento de água, coleta de esgoto e construções correlatas",
            Category.CLASS,
        ),
        Classification(
            "42.23-5", "Construção de redes de transportes por dutos, exceto para água e esgoto", Category.CLASS
        ),
        Classification("42.9", "Construção de outras obras de infra-estrutura", Category.GROUP),
        Classification("42.91-0", "Obras portuárias, marítimas e fluviais", Category.CLASS),
        Classification("42.92-8", "Montagem de instalações industriais e de estruturas metálicas", Category.CLASS),
        Classification("42.99-5", "Obras de engenharia civil não especificadas anteriormente", Category.CLASS),
        Classification("43", "SERVIÇOS ESPECIALIZADOS PARA CONSTRUÇÃO", Category.DIVISION),
        Classification("43.1", "Demolição e preparação do terreno", Category.GROUP),
        Classification("43.11-8", "Demolição e preparação de canteiros de obras", Category.CLASS),
        Classification("43.12-6", "Perfurações e sondagens", Category.CLASS),
        Classification("43.13-4", "Obras de terraplenagem", Category.CLASS),
        Classification("43.19-3", "Serviços de preparação do terreno não especificados anteriormente", Category.CLASS),
        Classification(
            "43.2", "Instalações elétricas, hidráulicas e outras instalações em construções", Category.GROUP
        ),
        Classification("43.21-5", "Instalações elétricas", Category.CLASS),
        Classification("43.22-3", "Instalações hidráulicas, de sistemas de ventilação e refrigeração", Category.CLASS),
        Classification(
            "43.29-1", "Obras de instalações em construções não especificadas anteriormente", Category.CLASS
        ),
        Classification("43.3", "Obras de acabamento", Category.GROUP),
        Classification("43.30-4", "Obras de acabamento", Category.CLASS),
        Classification("43.9", "Outros serviços especializados para construção", Category.GROUP),
        Classification("43.91-6", "Obras de fundações", Category.CLASS),
        Classification(
            "43.99-1", "Serviços especializados para construção não especificados anteriormente", Category.CLASS
        ),
        Classification("G", "COMÉRCIO; REPARAÇÃO DE VEÍCULOS AUTOMOTORES E MOTOCICLETAS", Category.SECTION),
        Classification("45", "COMÉRCIO E REPARAÇÃO DE VEÍCULOS AUTOMOTORES E MOTOCICLETAS", Category.DIVISION),
        Classification("45.1", "Comércio de veículos automotores", Category.GROUP),
        Classification("45.11-1", "Comércio a varejo e por atacado de veículos automotores", Category.CLASS),
        Classification(
            "45.12-9", "Representantes comerciais e agentes do comércio de veículos automotores", Category.CLASS
        ),
        Classification("45.2", "Manutenção e reparação de veículos automotores", Category.GROUP),
        Classification("45.20-0", "Manutenção e reparação de veículos automotores", Category.CLASS),
        Classification("45.3", "Comércio de peças e acessórios para veículos automotores", Category.GROUP),
        Classification("45.30-7", "Comércio de peças e acessórios para veículos automotores", Category.CLASS),
        Classification("45.4", "Comércio, manutenção e reparação de motocicletas, peças e acessórios", Category.GROUP),
        Classification(
            "45.41-2", "Comércio por atacado e a varejo de motocicletas, peças e acessórios", Category.CLASS
        ),
        Classification(
            "45.42-1",
            "Representantes comerciais e agentes do comércio de motocicletas, peças e acessórios",
            Category.CLASS,
        ),
        Classification("45.43-9", "Manutenção e reparação de motocicletas", Category.CLASS),
        Classification("46", "COMÉRCIO POR ATACADO, EXCETO VEÍCULOS AUTOMOTORES E MOTOCICLETAS", Category.DIVISION),
        Classification(
            "46.1",
            "Representantes comerciais e agentes do comércio, exceto de veículos automotores e motocicletas",
            Category.GROUP,
        ),
        Classification(
            "46.11-7",
            "Representantes comerciais e agentes do comércio de matérias-primas agrícolas e animais vivos",
            Category.CLASS,
        ),
        Classification(
            "46.12-5",
            "Representantes comerciais e agentes do comércio de combustíveis, minerais, produtos siderúrgicos e químicos",
            Category.CLASS,
        ),
        Classification(
            "46.13-3",
            "Representantes comerciais e agentes do comércio de madeira, material de construção e ferragens",
            Category.CLASS,
        ),
        Classification(
            "46.14-1",
            "Representantes comerciais e agentes do comércio de máquinas, equipamentos, embarcações e aeronaves",
            Category.CLASS,
        ),
        Classification(
            "46.15-0",
            "Representantes comerciais e agentes do comércio de eletrodomésticos, móveis e artigos de uso doméstico",
            Category.CLASS,
        ),
        Classification(
            "46.16-8",
            "Representantes comerciais e agentes do comércio de têxteis, vestuário, calçados e artigos de viagem",
            Category.CLASS,
        ),
        Classification(
            "46.17-6",
            "Representantes comerciais e agentes do comércio de produtos alimentícios, bebidas e fumo",
            Category.CLASS,
        ),
        Classification(
            "46.18-4",
            "Representantes comerciais e agentes do comércio especializado em produtos não especificados anteriormente",
            Category.CLASS,
        ),
        Classification(
            "46.19-2",
            "Representantes comerciais e agentes do comércio de mercadorias em geral não especializado",
            Category.CLASS,
        ),
        Classification("46.2", "Comércio atacadista de matérias-primas agrícolas e animais vivos", Category.GROUP),
        Classification("46.21-4", "Comércio atacadista de café em grão", Category.CLASS),
        Classification("46.22-2", "Comércio atacadista de soja", Category.CLASS),
        Classification(
            "46.23-1",
            "Comércio atacadista de animais vivos, alimentos para animais e matérias-primas agrícolas, exceto café e soja",
            Category.CLASS,
        ),
        Classification(
            "46.3", "Comércio atacadista especializado em produtos alimentícios, bebidas e fumo", Category.GROUP
        ),
        Classification("46.31-1", "Comércio atacadista de leite e laticínios", Category.CLASS),
        Classification(
            "46.32-0",
            "Comércio atacadista de cereais e leguminosas beneficiados, farinhas, amidos e féculas",
            Category.CLASS,
        ),
        Classification("46.33-8", "Comércio atacadista de hortifrutigranjeiros", Category.CLASS),
        Classification("46.34-6", "Comércio atacadista de carnes, produtos da carne e pescado", Category.CLASS),
        Classification("46.35-4", "Comércio atacadista de bebidas", Category.CLASS),
        Classification("46.36-2", "Comércio atacadista de produtos do fumo", Category.CLASS),
        Classification(
            "46.37-1",
            "Comércio atacadista especializado em produtos alimentícios não especificados anteriormente",
            Category.CLASS,
        ),
        Classification("46.39-7", "Comércio atacadista de produtos alimentícios em geral", Category.CLASS),
        Classification("46.4", "Comércio atacadista de produtos de consumo não-alimentar", Category.GROUP),
        Classification(
            "46.41-9", "Comércio atacadista de tecidos, artefatos de tecidos e de armarinho", Category.CLASS
        ),
        Classification("46.42-7", "Comércio atacadista de artigos do vestuário e acessórios", Category.CLASS),
        Classification("46.43-5", "Comércio atacadista de calçados e artigos de viagem", Category.CLASS),
        Classification(
            "46.44-3", "Comércio atacadista de produtos farmacêuticos para uso humano e veterinário", Category.CLASS
        ),
        Classification(
            "46.45-1",
            "Comércio atacadista de instrumentos e materiais para uso médico, cirúrgico, ortopédico e odontológico",
            Category.CLASS,
        ),
        Classification(
            "46.46-0", "Comércio atacadista de cosméticos, produtos de perfumaria e de higiene pessoal", Category.CLASS
        ),
        Classification(
            "46.47-8",
            "Comércio atacadista de artigos de escritório e de papelaria; livros, jornais e outras publicações",
            Category.CLASS,
        ),
        Classification(
            "46.49-4",
            "Comércio atacadista de equipamentos e artigos de uso pessoal e doméstico não especificados anteriormente",
            Category.CLASS,
        ),
        Classification(
            "46.5",
            "Comércio atacadista de equipamentos e produtos de tecnologias de informação e comunicação",
            Category.GROUP,
        ),
        Classification(
            "46.51-6", "Comércio atacadista de computadores, periféricos e suprimentos de informática", Category.CLASS
        ),
        Classification(
            "46.52-4",
            "Comércio atacadista de componentes eletrônicos e equipamentos de telefonia e comunicação",
            Category.CLASS,
        ),
        Classification(
            "46.6",
            "Comércio atacadista de máquinas, aparelhos e equipamentos, exceto de tecnologias de informação e comunicação",
            Category.GROUP,
        ),
        Classification(
            "46.61-3",
            "Comércio atacadista de máquinas, aparelhos e equipamentos para uso agropecuário; partes e peças",
            Category.CLASS,
        ),
        Classification(
            "46.62-1",
            "Comércio atacadista de máquinas, equipamentos para terraplenagem, mineração e construção; partes e peças",
            Category.CLASS,
        ),
        Classification(
            "46.63-0",
            "Comércio atacadista de máquinas e equipamentos para uso industrial; partes e peças",
            Category.CLASS,
        ),
        Classification(
            "46.64-8",
            "Comércio atacadista de máquinas, aparelhos e equipamentos para uso odonto-médico-hospitalar; partes e peças",
            Category.CLASS,
        ),
        Classification(
            "46.65-6",
            "Comércio atacadista de máquinas e equipamentos para uso comercial; partes e peças",
            Category.CLASS,
        ),
        Classification(
            "46.69-9",
            "Comércio atacadista de máquinas, aparelhos e equipamentos não especificados anteriormente; partes e peças",
            Category.CLASS,
        ),
        Classification(
            "46.7",
            "Comércio atacadista de madeira, ferragens, ferramentas, material elétrico e material de construção",
            Category.GROUP,
        ),
        Classification("46.71-1", "Comércio atacadista de madeira e produtos derivados", Category.CLASS),
        Classification("46.72-9", "Comércio atacadista de ferragens e ferramentas", Category.CLASS),
        Classification("46.73-7", "Comércio atacadista de material elétrico", Category.CLASS),
        Classification("46.74-5", "Comércio atacadista de cimento", Category.CLASS),
        Classification(
            "46.79-6",
            "Comércio atacadista especializado de materiais de construção não especificados anteriormente e de materiais de construção em geral",
            Category.CLASS,
        ),
        Classification("46.8", "Comércio atacadista especializado em outros produtos", Category.GROUP),
        Classification(
            "46.81-8",
            "Comércio atacadista de combustíveis sólidos, líquidos e gasosos, exceto gás natural e GLP",
            Category.CLASS,
        ),
        Classification("46.82-6", "Comércio atacadista de gás liqüefeito de petróleo (GLP)", Category.CLASS),
        Classification(
            "46.83-4",
            "Comércio atacadista de defensivos agrícolas, adubos, fertilizantes e corretivos do solo",
            Category.CLASS,
        ),
        Classification(
            "46.84-2", "Comércio atacadista de produtos químicos e petroquímicos, exceto agroquímicos", Category.CLASS
        ),
        Classification(
            "46.85-1",
            "Comércio atacadista de produtos siderúrgicos e metalúrgicos, exceto para construção",
            Category.CLASS,
        ),
        Classification("46.86-9", "Comércio atacadista de papel e papelão em bruto e de embalagens", Category.CLASS),
        Classification("46.87-7", "Comércio atacadista de resíduos e sucatas", Category.CLASS),
        Classification(
            "46.89-3",
            "Comércio atacadista especializado de outros produtos intermediários não especificados anteriormente",
            Category.CLASS,
        ),
        Classification("46.9", "Comércio atacadista não-especializado", Category.GROUP),
        Classification(
            "46.91-5",
            "Comércio atacadista de mercadorias em geral, com predominância de produtos alimentícios",
            Category.CLASS,
        ),
        Classification(
            "46.92-3",
            "Comércio atacadista de mercadorias em geral, com predominância de insumos agropecuários",
            Category.CLASS,
        ),
        Classification(
            "46.93-1",
            "Comércio atacadista de mercadorias em geral, sem predominância de alimentos ou de insumos agropecuários",
            Category.CLASS,
        ),
        Classification("47", "COMÉRCIO VAREJISTA", Category.DIVISION),
        Classification("47.1", "Comércio varejista não-especializado", Category.GROUP),
        Classification(
            "47.11-3",
            "Comércio varejista de mercadorias em geral, com predominância de produtos alimentícios - hipermercados e supermercados",
            Category.CLASS,
        ),
        Classification(
            "47.12-1",
            "Comércio varejista de mercadorias em geral, com predominância de produtos alimentícios - minimercados, mercearias e armazéns",
            Category.CLASS,
        ),
        Classification(
            "47.13-0",
            "Comércio varejista de mercadorias em geral, sem predominância de produtos alimentícios",
            Category.CLASS,
        ),
        Classification("47.2", "Comércio varejista de produtos alimentícios, bebidas e fumo", Category.GROUP),
        Classification(
            "47.21-1",
            "Comércio varejista de produtos de padaria, laticínio, doces, balas e semelhantes",
            Category.CLASS,
        ),
        Classification("47.22-9", "Comércio varejista de carnes e pescados - açougues e peixarias", Category.CLASS),
        Classification("47.23-7", "Comércio varejista de bebidas", Category.CLASS),
        Classification("47.24-5", "Comércio varejista de hortifrutigranjeiros", Category.CLASS),
        Classification(
            "47.29-6",
            "Comércio varejista de produtos alimentícios em geral ou especializado em produtos alimentícios não especificados anteriormente; produtos do fumo",
            Category.CLASS,
        ),
        Classification("47.3", "Comércio varejista de combustíveis para veículos automotores", Category.GROUP),
        Classification("47.31-8", "Comércio varejista de combustíveis para veículos automotores", Category.CLASS),
        Classification("47.32-6", "Comércio varejista de lubrificantes", Category.CLASS),
        Classification("47.4", "Comércio varejista de material de construção", Category.GROUP),
        Classification("47.41-5", "Comércio varejista de tintas e materiais para pintura", Category.CLASS),
        Classification("47.42-3", "Comércio varejista de material elétrico", Category.CLASS),
        Classification("47.43-1", "Comércio varejista de vidros", Category.CLASS),
        Classification("47.44-0", "Comércio varejista de ferragens, madeira e materiais de construção", Category.CLASS),
        Classification(
            "47.5",
            "Comércio varejista de equipamentos de informática e comunicação; equipamentos e artigos de uso doméstico",
            Category.GROUP,
        ),
        Classification(
            "47.51-2", "Comércio varejista especializado de equipamentos e suprimentos de informática", Category.CLASS
        ),
        Classification(
            "47.52-1", "Comércio varejista especializado de equipamentos de telefonia e comunicação", Category.CLASS
        ),
        Classification(
            "47.53-9",
            "Comércio varejista especializado de eletrodomésticos e equipamentos de áudio e vídeo",
            Category.CLASS,
        ),
        Classification(
            "47.54-7", "Comércio varejista especializado de móveis, colchoaria e artigos de iluminação", Category.CLASS
        ),
        Classification(
            "47.55-5", "Comércio varejista especializado de tecidos e artigos de cama, mesa e banho", Category.CLASS
        ),
        Classification(
            "47.56-3", "Comércio varejista especializado de instrumentos musicais e acessórios", Category.CLASS
        ),
        Classification(
            "47.57-1",
            "Comércio varejista especializado de peças e acessórios para aparelhos eletroeletrônicos para uso doméstico, exceto informática e comunicação",
            Category.CLASS,
        ),
        Classification(
            "47.59-8", "Comércio varejista de artigos de uso doméstico não especificados anteriormente", Category.CLASS
        ),
        Classification("47.6", "Comércio varejista de artigos culturais, recreativos e esportivos", Category.GROUP),
        Classification("47.61-0", "Comércio varejista de livros, jornais, revistas e papelaria", Category.CLASS),
        Classification("47.62-8", "Comércio varejista de discos, CDs, DVDs e fitas", Category.CLASS),
        Classification("47.63-6", "Comércio varejista de artigos recreativos e esportivos", Category.CLASS),
        Classification(
            "47.7",
            "Comércio varejista de produtos farmacêuticos, perfumaria e cosméticos e artigos médicos, ópticos e ortopédicos",
            Category.GROUP,
        ),
        Classification(
            "47.71-7", "Comércio varejista de produtos farmacêuticos para uso humano e veterinário", Category.CLASS
        ),
        Classification(
            "47.72-5", "Comércio varejista de cosméticos, produtos de perfumaria e de higiene pessoal", Category.CLASS
        ),
        Classification("47.73-3", "Comércio varejista de artigos médicos e ortopédicos", Category.CLASS),
        Classification("47.74-1", "Comércio varejista de artigos de óptica", Category.CLASS),
        Classification(
            "47.8",
            "Comércio varejista de produtos novos não especificados anteriormente e de produtos usados",
            Category.GROUP,
        ),
        Classification("47.81-4", "Comércio varejista de artigos do vestuário e acessórios", Category.CLASS),
        Classification("47.82-2", "Comércio varejista de calçados e artigos de viagem", Category.CLASS),
        Classification("47.83-1", "Comércio varejista de jóias e relógios", Category.CLASS),
        Classification("47.84-9", "Comércio varejista de gás liqüefeito de petróleo (GLP)", Category.CLASS),
        Classification("47.85-7", "Comércio varejista de artigos usados", Category.CLASS),
        Classification(
            "47.89-0", "Comércio varejista de outros produtos novos não especificados anteriormente", Category.CLASS
        ),
        Classification("47.9", "Comércio ambulante e outros tipos de comércio varejista", Category.GROUP),
        Classification("47.90-3", "Comércio ambulante e outros tipos de comércio varejista", Category.CLASS),
        Classification("H", "TRANSPORTE, ARMAZENAGEM E CORREIO", Category.SECTION),
        Classification("49", "TRANSPORTE TERRESTRE", Category.DIVISION),
        Classification("49.1", "Transporte ferroviário e metroferroviário", Category.GROUP),
        Classification("49.11-6", "Transporte ferroviário de carga", Category.CLASS),
        Classification("49.12-4", "Transporte metroferroviário de passageiros", Category.CLASS),
        Classification("49.2", "Transporte rodoviário de passageiros", Category.GROUP),
        Classification(
            "49.21-3",
            "Transporte rodoviário coletivo de passageiros, com itinerário fixo, municipal e em região metropolitana",
            Category.CLASS,
        ),
        Classification(
            "49.22-1",
            "Transporte rodoviário coletivo de passageiros, com itinerário fixo, intermunicipal, interestadual e internacional",
            Category.CLASS,
        ),
        Classification("49.23-0", "Transporte rodoviário de táxi", Category.CLASS),
        Classification("49.24-8", "Transporte escolar", Category.CLASS),
        Classification(
            "49.29-9",
            "Transporte rodoviário coletivo de passageiros, sob regime de fretamento, e outros transportes rodoviários não especificados anteriormente",
            Category.CLASS,
        ),
        Classification("49.3", "Transporte rodoviário de carga", Category.GROUP),
        Classification("49.30-2", "Transporte rodoviário de carga", Category.CLASS),
        Classification("49.4", "Transporte dutoviário", Category.GROUP),
        Classification("49.40-0", "Transporte dutoviário", Category.CLASS),
        Classification("49.5", "Trens turísticos, teleféricos e similares", Category.GROUP),
        Classification("49.50-7", "Trens turísticos, teleféricos e similares", Category.CLASS),
        Classification("50", "TRANSPORTE AQUAVIÁRIO", Category.DIVISION),
        Classification("50.1", "Transporte marítimo de cabotagem e longo curso", Category.GROUP),
        Classification("50.11-4", "Transporte marítimo de cabotagem", Category.CLASS),
        Classification("50.12-2", "Transporte marítimo de longo curso", Category.CLASS),
        Classification("50.2", "Transporte por navegação interior", Category.GROUP),
        Classification("50.21-1", "Transporte por navegação interior de carga", Category.CLASS),
        Classification(
            "50.22-0", "Transporte por navegação interior de passageiros em linhas regulares", Category.CLASS
        ),
        Classification("50.3", "Navegação de apoio", Category.GROUP),
        Classification("50.30-1", "Navegação de apoio", Category.CLASS),
        Classification("50.9", "Outros transportes aquaviários", Category.GROUP),
        Classification("50.91-2", "Transporte por navegação de travessia", Category.CLASS),
        Classification("50.99-8", "Transportes aquaviários não especificados anteriormente", Category.CLASS),
        Classification("51", "TRANSPORTE AÉREO", Category.DIVISION),
        Classification("51.1", "Transporte aéreo de passageiros", Category.GROUP),
        Classification("51.11-1", "Transporte aéreo de passageiros regular", Category.CLASS),
        Classification("51.12-9", "Transporte aéreo de passageiros não-regular", Category.CLASS),
        Classification("51.2", "Transporte aéreo de carga", Category.GROUP),
        Classification("51.20-0", "Transporte aéreo de carga", Category.CLASS),
        Classification("51.3", "Transporte espacial", Category.GROUP),
        Classification("51.30-7", "Transporte espacial", Category.CLASS),
        Classification("52", "ARMAZENAMENTO E ATIVIDADES AUXILIARES DOS TRANSPORTES", Category.DIVISION),
        Classification("52.1", "Armazenamento, carga e descarga", Category.GROUP),
        Classification("52.11-7", "Armazenamento", Category.CLASS),
        Classification("52.12-5", "Carga e descarga", Category.CLASS),
        Classification("52.2", "Atividades auxiliares dos transportes terrestres", Category.GROUP),
        Classification(
            "52.21-4", "Concessionárias de rodovias, pontes, túneis e serviços relacionados", Category.CLASS
        ),
        Classification("52.22-2", "Terminais rodoviários e ferroviários", Category.CLASS),
        Classification("52.23-1", "Estacionamento de veículos", Category.CLASS),
        Classification(
            "52.29-0",
            "Atividades auxiliares dos transportes terrestres não especificadas anteriormente",
            Category.CLASS,
        ),
        Classification("52.3", "Atividades auxiliares dos transportes aquaviários", Category.GROUP),
        Classification("52.31-1", "Gestão de portos e terminais", Category.CLASS),
        Classification("52.32-0", "Atividades de agenciamento marítimo", Category.CLASS),
        Classification(
            "52.39-7",
            "Atividades auxiliares dos transportes aquaviários não especificadas anteriormente",
            Category.CLASS,
        ),
        Classification("52.4", "Atividades auxiliares dos transportes aéreos", Category.GROUP),
        Classification("52.40-1", "Atividades auxiliares dos transportes aéreos", Category.CLASS),
        Classification("52.5", "Atividades relacionadas à organização do transporte de carga", Category.GROUP),
        Classification("52.50-8", "Atividades relacionadas à organização do transporte de carga", Category.CLASS),
        Classification("53", "CORREIO E OUTRAS ATIVIDADES DE ENTREGA", Category.DIVISION),
        Classification("53.1", "Atividades de Correio", Category.GROUP),
        Classification("53.10-5", "Atividades de Correio", Category.CLASS),
        Classification("53.2", "Atividades de malote e de entrega", Category.GROUP),
        Classification("53.20-2", "Atividades de malote e de entrega", Category.CLASS),
        Classification("I", "ALOJAMENTO E ALIMENTAÇÃO", Category.SECTION),
        Classification("55", "ALOJAMENTO", Category.DIVISION),
        Classification("55.1", "Hotéis e similares", Category.GROUP),
        Classification("55.10-8", "Hotéis e similares", Category.CLASS),
        Classification("55.9", "Outros tipos de alojamento não especificados anteriormente", Category.GROUP),
        Classification("55.90-6", "Outros tipos de alojamento não especificados anteriormente", Category.CLASS),
        Classification("56", "ALIMENTAÇÃO", Category.DIVISION),
        Classification("56.1", "Restaurantes e outros serviços de alimentação e bebidas", Category.GROUP),
        Classification(
            "56.11-2", "Restaurantes e outros estabelecimentos de serviços de alimentação e bebidas", Category.CLASS
        ),
        Classification("56.12-1", "Serviços ambulantes de alimentação", Category.CLASS),
        Classification("56.2", "Serviços de catering, bufê e outros serviços de comida preparada", Category.GROUP),
        Classification("56.20-1", "Serviços de catering, bufê e outros serviços de comida preparada", Category.CLASS),
        Classification("J", "INFORMAÇÃO E COMUNICAÇÃO", Category.SECTION),
        Classification("58", "EDIÇÃO E EDIÇÃO INTEGRADA À IMPRESSÃO", Category.DIVISION),
        Classification("58.1", "Edição de livros, jornais, revistas e outras atividades de edição", Category.GROUP),
        Classification("58.11-5", "Edição de livros", Category.CLASS),
        Classification("58.12-3", "Edição de jornais", Category.CLASS),
        Classification("58.13-1", "Edição de revistas", Category.CLASS),
        Classification("58.19-1", "Edição de cadastros, listas e outros produtos gráficos", Category.CLASS),
        Classification(
            "58.2", "Edição integrada à impressão de livros, jornais, revistas e outras publicações", Category.GROUP
        ),
        Classification("58.21-2", "Edição integrada à impressão de livros", Category.CLASS),
        Classification("58.22-1", "Edição integrada à impressão de jornais", Category.CLASS),
        Classification("58.23-9", "Edição integrada à impressão de revistas", Category.CLASS),
        Classification(
            "58.29-8", "Edição integrada à impressão de cadastros, listas e outros produtos gráficos", Category.CLASS
        ),
        Classification(
            "59",
            "ATIVIDADES CINEMATOGRÁFICAS, PRODUÇÃO DE VÍDEOS E DE PROGRAMAS DE TELEVISÃO; GRAVAÇÃO DE SOM E EDIÇÃO DE MÚSICA",
            Category.DIVISION,
        ),
        Classification(
            "59.1", "Atividades cinematográficas, produção de vídeos e de programas de televisão", Category.GROUP
        ),
        Classification(
            "59.11-1", "Atividades de produção cinematográfica, de vídeos e de programas de televisão", Category.CLASS
        ),
        Classification(
            "59.12-0",
            "Atividades de pós-produção cinematográfica, de vídeos e de programas de televisão",
            Category.CLASS,
        ),
        Classification("59.13-8", "Distribuição cinematográfica, de vídeo e de programas de televisão", Category.CLASS),
        Classification("59.14-6", "Atividades de exibição cinematográfica", Category.CLASS),
        Classification("59.2", "Atividades de gravação de som e de edição de música", Category.GROUP),
        Classification("59.20-1", "Atividades de gravação de som e de edição de música", Category.CLASS),
        Classification("60", "ATIVIDADES DE RÁDIO E DE TELEVISÃO", Category.DIVISION),
        Classification("60.1", "Atividades de rádio", Category.GROUP),
        Classification("60.10-1", "Atividades de rádio", Category.CLASS),
        Classification("60.2", "Atividades de televisão", Category.GROUP),
        Classification("60.21-7", "Atividades de televisão aberta", Category.CLASS),
        Classification("60.22-5", "Programadoras e atividades relacionadas à televisão por assinatura", Category.CLASS),
        Classification("61", "TELECOMUNICAÇÕES", Category.DIVISION),
        Classification("61.1", "Telecomunicações por fio", Category.GROUP),
        Classification("61.10-8", "Telecomunicações por fio", Category.CLASS),
        Classification("61.2", "Telecomunicações sem fio", Category.GROUP),
        Classification("61.20-5", "Telecomunicações sem fio", Category.CLASS),
        Classification("61.3", "Telecomunicações por satélite", Category.GROUP),
        Classification("61.30-2", "Telecomunicações por satélite", Category.CLASS),
        Classification("61.4", "Operadoras de televisão por assinatura", Category.GROUP),
        Classification("61.41-8", "Operadoras de televisão por assinatura por cabo", Category.CLASS),
        Classification("61.42-6", "Operadoras de televisão por assinatura por microondas", Category.CLASS),
        Classification("61.43-4", "Operadoras de televisão por assinatura por satélite", Category.CLASS),
        Classification("61.9", "Outras atividades de telecomunicações", Category.GROUP),
        Classification("61.90-6", "Outras atividades de telecomunicações", Category.CLASS),
        Classification("62", "ATIVIDADES DOS SERVIÇOS DE TECNOLOGIA DA INFORMAÇÃO", Category.DIVISION),
        Classification("62.0", "Atividades dos serviços de tecnologia da informação", Category.GROUP),
        Classification("62.01-5", "Desenvolvimento de programas de computador sob encomenda", Category.CLASS),
        Classification(
            "62.02-3", "Desenvolvimento e licenciamento de programas de computador customizáveis", Category.CLASS
        ),
        Classification(
            "62.03-1", "Desenvolvimento e licenciamento de programas de computador não-customizáveis", Category.CLASS
        ),
        Classification("62.04-0", "Consultoria em tecnologia da informação", Category.CLASS),
        Classification(
            "62.09-1", "Suporte técnico, manutenção e outros serviços em tecnologia da informação", Category.CLASS
        ),
        Classification("63", "ATIVIDADES DE PRESTAÇÃO DE SERVIÇOS DE INFORMAÇÃO", Category.DIVISION),
        Classification(
            "63.1", "Tratamento de dados, hospedagem na internet e outras atividades relacionadas", Category.GROUP
        ),
        Classification(
            "63.11-9",
            "Tratamento de dados, provedores de serviços de aplicação e serviços de hospedagem na internet",
            Category.CLASS,
        ),
        Classification(
            "63.19-4", "Portais, provedores de conteúdo e outros serviços de informação na internet", Category.CLASS
        ),
        Classification("63.9", "Outras atividades de prestação de serviços de informação", Category.GROUP),
        Classification("63.91-7", "Agências de notícias", Category.CLASS),
        Classification(
            "63.99-2",
            "Outras atividades de prestação de serviços de informação não especificadas anteriormente",
            Category.CLASS,
        ),
        Classification("K", "ATIVIDADES FINANCEIRAS, DE SEGUROS E SERVIÇOS RELACIONADOS", Category.SECTION),
        Classification("64", "ATIVIDADES DE SERVIÇOS FINANCEIROS", Category.DIVISION),
        Classification("64.1", "Banco Central", Category.GROUP),
        Classification("64.10-7", "Banco Central", Category.CLASS),
        Classification("64.2", "Intermediação monetária - depósitos à vista", Category.GROUP),
        Classification("64.21-2", "Bancos comerciais", Category.CLASS),
        Classification("64.22-1", "Bancos múltiplos, com carteira comercial", Category.CLASS),
        Classification("64.23-9", "Caixas econômicas", Category.CLASS),
        Classification("64.24-7", "Crédito cooperativo", Category.CLASS),
        Classification("64.3", "Intermediação não-monetária - outros instrumentos de captação", Category.GROUP),
        Classification("64.31-0", "Bancos múltiplos, sem carteira comercial", Category.CLASS),
        Classification("64.32-8", "Bancos de investimento", Category.CLASS),
        Classification("64.33-6", "Bancos de desenvolvimento", Category.CLASS),
        Classification("64.34-4", "Agências de fomento", Category.CLASS),
        Classification("64.35-2", "Crédito imobiliário", Category.CLASS),
        Classification("64.36-1", "Sociedades de crédito, financiamento e investimento - financeiras", Category.CLASS),
        Classification("64.37-9", "Sociedades de crédito ao microempreendedor", Category.CLASS),
        Classification("64.4", "Arrendamento mercantil", Category.GROUP),
        Classification("64.40-9", "Arrendamento mercantil", Category.CLASS),
        Classification("64.5", "Sociedades de capitalização", Category.GROUP),
        Classification("64.50-6", "Sociedades de capitalização", Category.CLASS),
        Classification("64.6", "Atividades de sociedades de participação", Category.GROUP),
        Classification("64.61-1", "Holdings de instituições financeiras", Category.CLASS),
        Classification("64.62-0", "Holdings de instituições não-financeiras", Category.CLASS),
        Classification("64.63-8", "Outras sociedades de participação, exceto holdings", Category.CLASS),
        Classification("64.7", "Fundos de investimento", Category.GROUP),
        Classification("64.70-1", "Fundos de investimento", Category.CLASS),
        Classification("64.9", "Atividades de serviços financeiros não especificadas anteriormente", Category.GROUP),
        Classification("64.91-3", "Sociedades de fomento mercantil - factoring", Category.CLASS),
        Classification("64.92-1", "Securitização de créditos", Category.CLASS),
        Classification("64.93-0", "Administração de consórcios para aquisição de bens e direitos", Category.CLASS),
        Classification(
            "64.99-9", "Outras atividades de serviços financeiros não especificadas anteriormente", Category.CLASS
        ),
        Classification("65", "SEGUROS, RESSEGUROS, PREVIDÊNCIA COMPLEMENTAR E PLANOS DE SAÚDE", Category.DIVISION),
        Classification("65.1", "Seguros de vida e não-vida", Category.GROUP),
        Classification("65.11-1", "Seguros de vida", Category.CLASS),
        Classification("65.12-0", "Seguros não-vida", Category.CLASS),
        Classification("65.2", "Seguros-saúde", Category.GROUP),
        Classification("65.20-1", "Seguros-saúde", Category.CLASS),
        Classification("65.3", "Resseguros", Category.GROUP),
        Classification("65.30-8", "Resseguros", Category.CLASS),
        Classification("65.4", "Previdência complementar", Category.GROUP),
        Classification("65.41-3", "Previdência complementar fechada", Category.CLASS),
        Classification("65.42-1", "Previdência complementar aberta", Category.CLASS),
        Classification("65.5", "Planos de saúde", Category.GROUP),
        Classification("65.50-2", "Planos de saúde", Category.CLASS),
        Classification(
            "66",
            "ATIVIDADES AUXILIARES DOS SERVIÇOS FINANCEIROS, SEGUROS, PREVIDÊNCIA COMPLEMENTAR E PLANOS DE SAÚDE",
            Category.DIVISION,
        ),
        Classification("66.1", "Atividades auxiliares dos serviços financeiros", Category.GROUP),
        Classification("66.11-8", "Administração de bolsas e mercados de balcão organizados", Category.CLASS),
        Classification(
            "66.12-6",
            "Atividades de intermediários em transações de títulos, valores mobiliários e mercadorias",
            Category.CLASS,
        ),
        Classification("66.13-4", "Administração de cartões de crédito", Category.CLASS),
        Classification(
            "66.19-3", "Atividades auxiliares dos serviços financeiros não especificadas anteriormente", Category.CLASS
        ),
        Classification(
            "66.2",
            "Atividades auxiliares dos seguros, da previdência complementar e dos planos de saúde",
            Category.GROUP,
        ),
        Classification("66.21-5", "Avaliação de riscos e perdas", Category.CLASS),
        Classification(
            "66.22-3",
            "Corretores e agentes de seguros, de planos de previdência complementar e de saúde",
            Category.CLASS,
        ),
        Classification(
            "66.29-1",
            "Atividades auxiliares dos seguros, da previdência complementar e dos planos de saúde não especificadas anteriormente",
            Category.CLASS,
        ),
        Classification("66.3", "Atividades de administração de fundos por contrato ou comissão", Category.GROUP),
        Classification("66.30-4", "Atividades de administração de fundos por contrato ou comissão", Category.CLASS),
        Classification("L", "ATIVIDADES IMOBILIÁRIAS", Category.SECTION),
        Classification("68", "ATIVIDADES IMOBILIÁRIAS", Category.DIVISION),
        Classification("68.1", "Atividades imobiliárias de imóveis próprios", Category.GROUP),
        Classification("68.10-2", "Atividades imobiliárias de imóveis próprios", Category.CLASS),
        Classification("68.2", "Atividades imobiliárias por contrato ou comissão", Category.GROUP),
        Classification("68.21-8", "Intermediação na compra, venda e aluguel de imóveis", Category.CLASS),
        Classification("68.22-6", "Gestão e administração da propriedade imobiliária", Category.CLASS),
        Classification("M", "ATIVIDADES PROFISSIONAIS, CIENTÍFICAS E TÉCNICAS", Category.SECTION),
        Classification("69", "ATIVIDADES JURÍDICAS, DE CONTABILIDADE E DE AUDITORIA", Category.DIVISION),
        Classification("69.1", "Atividades jurídicas", Category.GROUP),
        Classification("69.11-7", "Atividades jurídicas, exceto cartórios", Category.CLASS),
        Classification("69.12-5", "Cartórios", Category.CLASS),
        Classification(
            "69.2", "Atividades de contabilidade, consultoria e auditoria contábil e tributária", Category.GROUP
        ),
        Classification(
            "69.20-6", "Atividades de contabilidade, consultoria e auditoria contábil e tributária", Category.CLASS
        ),
        Classification(
            "70", "ATIVIDADES DE SEDES DE EMPRESAS E DE CONSULTORIA EM GESTÃO EMPRESARIAL", Category.DIVISION
        ),
        Classification("70.1", "Sedes de empresas e unidades administrativas locais", Category.GROUP),
        Classification("70.10-7", "Sedes de empresas e unidades administrativas locais", Category.CLASS),
        Classification("70.2", "Atividades de consultoria em gestão empresarial", Category.GROUP),
        Classification("70.20-4", "Atividades de consultoria em gestão empresarial", Category.CLASS),
        Classification("71", "SERVIÇOS DE ARQUITETURA E ENGENHARIA; TESTES E ANÁLISES TÉCNICAS", Category.DIVISION),
        Classification(
            "71.1", "Serviços de arquitetura e engenharia e atividades técnicas relacionadas", Category.GROUP
        ),
        Classification("71.11-1", "Serviços de arquitetura", Category.CLASS),
        Classification("71.12-0", "Serviços de engenharia", Category.CLASS),
        Classification("71.19-7", "Atividades técnicas relacionadas à arquitetura e engenharia", Category.CLASS),
        Classification("71.2", "Testes e análises técnicas", Category.GROUP),
        Classification("71.20-1", "Testes e análises técnicas", Category.CLASS),
        Classification("72", "PESQUISA E DESENVOLVIMENTO CIENTÍFICO", Category.DIVISION),
        Classification(
            "72.1", "Pesquisa e desenvolvimento experimental em ciências físicas e naturais", Category.GROUP
        ),
        Classification(
            "72.10-0", "Pesquisa e desenvolvimento experimental em ciências físicas e naturais", Category.CLASS
        ),
        Classification("72.2", "Pesquisa e desenvolvimento experimental em ciências sociais e humanas", Category.GROUP),
        Classification(
            "72.20-7", "Pesquisa e desenvolvimento experimental em ciências sociais e humanas", Category.CLASS
        ),
        Classification("73", "PUBLICIDADE E PESQUISA DE MERCADO", Category.DIVISION),
        Classification("73.1", "Publicidade", Category.GROUP),
        Classification("73.11-4", "Agências de publicidade", Category.CLASS),
        Classification(
            "73.12-2", "Agenciamento de espaços para publicidade, exceto em veículos de comunicação", Category.CLASS
        ),
        Classification("73.19-0", "Atividades de publicidade não especificadas anteriormente", Category.CLASS),
        Classification("73.2", "Pesquisas de mercado e de opinião pública", Category.GROUP),
        Classification("73.20-3", "Pesquisas de mercado e de opinião pública", Category.CLASS),
        Classification("74", "OUTRAS ATIVIDADES PROFISSIONAIS, CIENTÍFICAS E TÉCNICAS", Category.DIVISION),
        Classification("74.1", "Design e decoração de interiores", Category.GROUP),
        Classification("74.10-2", "Design e decoração de interiores", Category.CLASS),
        Classification("74.2", "Atividades fotográficas e similares", Category.GROUP),
        Classification("74.20-0", "Atividades fotográficas e similares", Category.CLASS),
        Classification(
            "74.9", "Atividades profissionais, científicas e técnicas não especificadas anteriormente", Category.GROUP
        ),
        Classification(
            "74.90-1",
            "Atividades profissionais, científicas e técnicas não especificadas anteriormente",
            Category.CLASS,
        ),
        Classification("75", "ATIVIDADES VETERINÁRIAS", Category.DIVISION),
        Classification("75.0", "Atividades veterinárias", Category.GROUP),
        Classification("75.00-1", "Atividades veterinárias", Category.CLASS),
        Classification("N", "ATIVIDADES ADMINISTRATIVAS E SERVIÇOS COMPLEMENTARES", Category.SECTION),
        Classification(
            "77", "ALUGUÉIS NÃO-IMOBILIÁRIOS E GESTÃO DE ATIVOS INTANGÍVEIS NÃO-FINANCEIROS", Category.DIVISION
        ),
        Classification("77.1", "Locação de meios de transporte sem condutor", Category.GROUP),
        Classification("77.11-0", "Locação de automóveis sem condutor", Category.CLASS),
        Classification("77.19-5", "Locação de meios de transporte, exceto automóveis, sem condutor", Category.CLASS),
        Classification("77.2", "Aluguel de objetos pessoais e domésticos", Category.GROUP),
        Classification("77.21-7", "Aluguel de equipamentos recreativos e esportivos", Category.CLASS),
        Classification("77.22-5", "Aluguel de fitas de vídeo, DVDs e similares", Category.CLASS),
        Classification("77.23-3", "Aluguel de objetos do vestuário, jóias e acessórios", Category.CLASS),
        Classification(
            "77.29-2", "Aluguel de objetos pessoais e domésticos não especificados anteriormente", Category.CLASS
        ),
        Classification("77.3", "Aluguel de máquinas e equipamentos sem operador", Category.GROUP),
        Classification("77.31-4", "Aluguel de máquinas e equipamentos agrícolas sem operador", Category.CLASS),
        Classification("77.32-2", "Aluguel de máquinas e equipamentos para construção sem operador", Category.CLASS),
        Classification("77.33-1", "Aluguel de máquinas e equipamentos para escritório", Category.CLASS),
        Classification("77.39-0", "Aluguel de máquinas e equipamentos não especificados anteriormente", Category.CLASS),
        Classification("77.4", "Gestão de ativos intangíveis não-financeiros", Category.GROUP),
        Classification("77.40-3", "Gestão de ativos intangíveis não-financeiros", Category.CLASS),
        Classification("78", "SELEÇÃO, AGENCIAMENTO E LOCAÇÃO DE MÃO-DE-OBRA", Category.DIVISION),
        Classification("78.1", "Seleção e agenciamento de mão-de-obra", Category.GROUP),
        Classification("78.10-8", "Seleção e agenciamento de mão-de-obra", Category.CLASS),
        Classification("78.2", "Locação de mão-de-obra temporária", Category.GROUP),
        Classification("78.20-5", "Locação de mão-de-obra temporária", Category.CLASS),
        Classification("78.3", "Fornecimento e gestão de recursos humanos para terceiros", Category.GROUP),
        Classification("78.30-2", "Fornecimento e gestão de recursos humanos para terceiros", Category.CLASS),
        Classification("79", "AGÊNCIAS DE VIAGENS, OPERADORES TURÍSTICOS E SERVIÇOS DE RESERVAS", Category.DIVISION),
        Classification("79.1", "Agências de viagens e operadores turísticos", Category.GROUP),
        Classification("79.11-2", "Agências de viagens", Category.CLASS),
        Classification("79.12-1", "Operadores turísticos", Category.CLASS),
        Classification(
            "79.9", "Serviços de reservas e outros serviços de turismo não especificados anteriormente", Category.GROUP
        ),
        Classification(
            "79.90-2",
            "Serviços de reservas e outros serviços de turismo não especificados anteriormente",
            Category.CLASS,
        ),
        Classification("80", "ATIVIDADES DE VIGILÂNCIA, SEGURANÇA E INVESTIGAÇÃO", Category.DIVISION),
        Classification("80.1", "Atividades de vigilância, segurança privada e transporte de valores", Category.GROUP),
        Classification("80.11-1", "Atividades de vigilância e segurança privada", Category.CLASS),
        Classification("80.12-9", "Atividades de transporte de valores", Category.CLASS),
        Classification("80.2", "Atividades de monitoramento de sistemas de segurança", Category.GROUP),
        Classification("80.20-0", "Atividades de monitoramento de sistemas de segurança", Category.CLASS),
        Classification("80.3", "Atividades de investigação particular", Category.GROUP),
        Classification("80.30-7", "Atividades de investigação particular", Category.CLASS),
        Classification("81", "SERVIÇOS PARA EDIFÍCIOS E ATIVIDADES PAISAGÍSTICAS", Category.DIVISION),
        Classification("81.1", "Serviços combinados para apoio a edifícios", Category.GROUP),
        Classification(
            "81.11-7", "Serviços combinados para apoio a edifícios, exceto condomínios prediais", Category.CLASS
        ),
        Classification("81.12-5", "Condomínios prediais", Category.CLASS),
        Classification("81.2", "Atividades de limpeza", Category.GROUP),
        Classification("81.21-4", "Limpeza em prédios e em domicílios", Category.CLASS),
        Classification("81.22-2", "Imunização e controle de pragas urbanas", Category.CLASS),
        Classification("81.29-0", "Atividades de limpeza não especificadas anteriormente", Category.CLASS),
        Classification("81.3", "Atividades paisagísticas", Category.GROUP),
        Classification("81.30-3", "Atividades paisagísticas", Category.CLASS),
        Classification(
            "82",
            "SERVIÇOS DE ESCRITÓRIO, DE APOIO ADMINISTRATIVO E OUTROS SERVIÇOS PRESTADOS PRINCIPALMENTE ÀS EMPRESAS",
            Category.DIVISION,
        ),
        Classification("82.1", "Serviços de escritório e apoio administrativo", Category.GROUP),
        Classification("82.11-3", "Serviços combinados de escritório e apoio administrativo", Category.CLASS),
        Classification(
            "82.19-9",
            "Fotocópias, preparação de documentos e outros serviços especializados de apoio administrativo",
            Category.CLASS,
        ),
        Classification("82.2", "Atividades de teleatendimento", Category.GROUP),
        Classification("82.20-2", "Atividades de teleatendimento", Category.CLASS),
        Classification("82.3", "Atividades de organização de eventos, exceto culturais e esportivos", Category.GROUP),
        Classification(
            "82.30-0", "Atividades de organização de eventos, exceto culturais e esportivos", Category.CLASS
        ),
        Classification("82.9", "Outras atividades de serviços prestados principalmente às empresas", Category.GROUP),
        Classification("82.91-1", "Atividades de cobrança e informações cadastrais", Category.CLASS),
        Classification("82.92-0", "Envasamento e empacotamento sob contrato", Category.CLASS),
        Classification(
            "82.99-7",
            "Atividades de serviços prestados principalmente às empresas não especificadas anteriormente",
            Category.CLASS,
        ),
        Classification("O", "ADMINISTRAÇÃO PÚBLICA, DEFESA E SEGURIDADE SOCIAL", Category.SECTION),
        Classification("84", "ADMINISTRAÇÃO PÚBLICA, DEFESA E SEGURIDADE SOCIAL", Category.DIVISION),
        Classification("84.1", "Administração do estado e da política econômica e social", Category.GROUP),
        Classification("84.11-6", "Administração pública em geral", Category.CLASS),
        Classification(
            "84.12-4",
            "Regulação das atividades de saúde, educação, serviços culturais e outros serviços sociais",
            Category.CLASS,
        ),
        Classification("84.13-2", "Regulação das atividades econômicas", Category.CLASS),
        Classification("84.2", "Serviços coletivos prestados pela administração pública", Category.GROUP),
        Classification("84.21-3", "Relações exteriores", Category.CLASS),
        Classification("84.22-1", "Defesa", Category.CLASS),
        Classification("84.23-0", "Justiça", Category.CLASS),
        Classification("84.24-8", "Segurança e ordem pública", Category.CLASS),
        Classification("84.25-6", "Defesa Civil", Category.CLASS),
        Classification("84.3", "Seguridade social obrigatória", Category.GROUP),
        Classification("84.30-2", "Seguridade social obrigatória", Category.CLASS),
        Classification("P", "EDUCAÇÃO", Category.SECTION),
        Classification("85", "EDUCAÇÃO", Category.DIVISION),
        Classification("85.1", "Educação infantil e ensino fundamental", Category.GROUP),
        Classification("85.11-2", "Educação infantil - creche", Category.CLASS),
        Classification("85.12-1", "Educação infantil - pré-escola", Category.CLASS),
        Classification("85.13-9", "Ensino fundamental", Category.CLASS),
        Classification("85.2", "Ensino médio", Category.GROUP),
        Classification("85.20-1", "Ensino médio", Category.CLASS),
        Classification("85.3", "Educação superior", Category.GROUP),
        Classification("85.31-7", "Educação superior - graduação", Category.CLASS),
        Classification("85.32-5", "Educação superior - graduação e pós-graduação", Category.CLASS),
        Classification("85.33-3", "Educação superior - pós-graduação e extensão", Category.CLASS),
        Classification("85.4", "Educação profissional de nível técnico e tecnológico", Category.GROUP),
        Classification("85.41-4", "Educação profissional de nível técnico", Category.CLASS),
        Classification("85.42-2", "Educação profissional de nível tecnológico", Category.CLASS),
        Classification("85.5", "Atividades de apoio à educação", Category.GROUP),
        Classification("85.50-3", "Atividades de apoio à educação", Category.CLASS),
        Classification("85.9", "Outras atividades de ensino", Category.GROUP),
        Classification("85.91-1", "Ensino de esportes", Category.CLASS),
        Classification("85.92-9", "Ensino de arte e cultura", Category.CLASS),
        Classification("85.93-7", "Ensino de idiomas", Category.CLASS),
        Classification("85.99-6", "Atividades de ensino não especificadas anteriormente", Category.CLASS),
        Classification("Q", "SAÚDE HUMANA E SERVIÇOS SOCIAIS", Category.SECTION),
        Classification("86", "ATIVIDADES DE ATENÇÃO À SAÚDE HUMANA", Category.DIVISION),
        Classification("86.1", "Atividades de atendimento hospitalar", Category.GROUP),
        Classification("86.10-1", "Atividades de atendimento hospitalar", Category.CLASS),
        Classification("86.2", "Serviços móveis de atendimento a urgências e de remoção de pacientes", Category.GROUP),
        Classification("86.21-6", "Serviços móveis de atendimento a urgências", Category.CLASS),
        Classification(
            "86.22-4",
            "Serviços de remoção de pacientes, exceto os serviços móveis de atendimento a urgências",
            Category.CLASS,
        ),
        Classification(
            "86.3", "Atividades de atenção ambulatorial executadas por médicos e odontólogos", Category.GROUP
        ),
        Classification(
            "86.30-5", "Atividades de atenção ambulatorial executadas por médicos e odontólogos", Category.CLASS
        ),
        Classification("86.4", "Atividades de serviços de complementação diagnóstica e terapêutica", Category.GROUP),
        Classification("86.40-2", "Atividades de serviços de complementação diagnóstica e terapêutica", Category.CLASS),
        Classification(
            "86.5", "Atividades de profissionais da área de saúde, exceto médicos e odontólogos", Category.GROUP
        ),
        Classification(
            "86.50-0", "Atividades de profissionais da área de saúde, exceto médicos e odontólogos", Category.CLASS
        ),
        Classification("86.6", "Atividades de apoio à gestão de saúde", Category.GROUP),
        Classification("86.60-7", "Atividades de apoio à gestão de saúde", Category.CLASS),
        Classification("86.9", "Atividades de atenção à saúde humana não especificadas anteriormente", Category.GROUP),
        Classification(
            "86.90-9", "Atividades de atenção à saúde humana não especificadas anteriormente", Category.CLASS
        ),
        Classification(
            "87",
            "ATIVIDADES DE ATENÇÃO À SAÚDE HUMANA INTEGRADAS COM ASSISTÊNCIA SOCIAL, PRESTADAS EM RESIDÊNCIAS COLETIVAS E PARTICULARES",
            Category.DIVISION,
        ),
        Classification(
            "87.1",
            "Atividades de assistência a idosos, deficientes físicos, imunodeprimidos e convalescentes, e de infra-estrutura e apoio a pacientes prestadas em residências coletivas e particulares",
            Category.GROUP,
        ),
        Classification(
            "87.11-5",
            "Atividades de assistência a idosos, deficientes físicos, imunodeprimidos e convalescentes prestadas em residências coletivas e particulares",
            Category.CLASS,
        ),
        Classification(
            "87.12-3",
            "Atividades de fornecimento de infra-estrutura de apoio e assistência a paciente no domicílio",
            Category.CLASS,
        ),
        Classification(
            "87.2",
            "Atividades de assistência psicossocial e à saúde a portadores de distúrbios psíquicos, deficiência mental e dependência química",
            Category.GROUP,
        ),
        Classification(
            "87.20-4",
            "Atividades de assistência psicossocial e à saúde a portadores de distúrbios psíquicos, deficiência mental e dependência química",
            Category.CLASS,
        ),
        Classification(
            "87.3", "Atividades de assistência social prestadas em residências coletivas e particulares", Category.GROUP
        ),
        Classification(
            "87.30-1",
            "Atividades de assistência social prestadas em residências coletivas e particulares",
            Category.CLASS,
        ),
        Classification("88", "SERVIÇOS DE ASSISTÊNCIA SOCIAL SEM ALOJAMENTO", Category.DIVISION),
        Classification("88.0", "Serviços de assistência social sem alojamento", Category.GROUP),
        Classification("88.00-6", "Serviços de assistência social sem alojamento", Category.CLASS),
        Classification("R", "ARTES, CULTURA, ESPORTE E RECREAÇÃO", Category.SECTION),
        Classification("90", "ATIVIDADES ARTÍSTICAS, CRIATIVAS E DE ESPETÁCULOS", Category.DIVISION),
        Classification("90.0", "Atividades artísticas, criativas e de espetáculos", Category.GROUP),
        Classification("90.01-9", "Artes cênicas, espetáculos e atividades complementares", Category.CLASS),
        Classification("90.02-7", "Criação artística", Category.CLASS),
        Classification(
            "90.03-5",
            "Gestão de espaços para artes cênicas, espetáculos e outras atividades artísticas",
            Category.CLASS,
        ),
        Classification("91", "ATIVIDADES LIGADAS AO PATRIMÔNIO CULTURAL E AMBIENTAL", Category.DIVISION),
        Classification("91.0", "Atividades ligadas ao patrimônio cultural e ambiental", Category.GROUP),
        Classification("91.01-5", "Atividades de bibliotecas e arquivos", Category.CLASS),
        Classification(
            "91.02-3",
            "Atividades de museus e de exploração, restauração artística e conservação de lugares e prédios históricos e atrações similares",
            Category.CLASS,
        ),
        Classification(
            "91.03-1",
            "Atividades de jardins botânicos, zoológicos, parques nacionais, reservas ecológicas e áreas de proteção ambiental",
            Category.CLASS,
        ),
        Classification("92", "ATIVIDADES DE EXPLORAÇÃO DE JOGOS DE AZAR E APOSTAS", Category.DIVISION),
        Classification("92.0", "Atividades de exploração de jogos de azar e apostas", Category.GROUP),
        Classification("92.00-3", "Atividades de exploração de jogos de azar e apostas", Category.CLASS),
        Classification("93", "ATIVIDADES ESPORTIVAS E DE RECREAÇÃO E LAZER", Category.DIVISION),
        Classification("93.1", "Atividades esportivas", Category.GROUP),
        Classification("93.11-5", "Gestão de instalações de esportes", Category.CLASS),
        Classification("93.12-3", "Clubes sociais, esportivos e similares", Category.CLASS),
        Classification("93.13-1", "Atividades de condicionamento físico", Category.CLASS),
        Classification("93.19-1", "Atividades esportivas não especificadas anteriormente", Category.CLASS),
        Classification("93.2", "Atividades de recreação e lazer", Category.GROUP),
        Classification("93.21-2", "Parques de diversão e parques temáticos", Category.CLASS),
        Classification("93.29-8", "Atividades de recreação e lazer não especificadas anteriormente", Category.CLASS),
        Classification("S", "OUTRAS ATIVIDADES DE SERVIÇOS", Category.SECTION),
        Classification("94", "ATIVIDADES DE ORGANIZAÇÕES ASSOCIATIVAS", Category.DIVISION),
        Classification(
            "94.1", "Atividades de organizações associativas patronais, empresariais e profissionais", Category.GROUP
        ),
        Classification("94.11-1", "Atividades de organizações associativas patronais e empresariais", Category.CLASS),
        Classification("94.12-0", "Atividades de organizações associativas profissionais", Category.CLASS),
        Classification("94.2", "Atividades de organizações sindicais", Category.GROUP),
        Classification("94.20-1", "Atividades de organizações sindicais", Category.CLASS),
        Classification("94.3", "Atividades de associações de defesa de direitos sociais", Category.GROUP),
        Classification("94.30-8", "Atividades de associações de defesa de direitos sociais", Category.CLASS),
        Classification(
            "94.9", "Atividades de organizações associativas não especificadas anteriormente", Category.GROUP
        ),
        Classification("94.91-0", "Atividades de organizações religiosas", Category.CLASS),
        Classification("94.92-8", "Atividades de organizações políticas", Category.CLASS),
        Classification("94.93-6", "Atividades de organizações associativas ligadas à cultura e à arte", Category.CLASS),
        Classification("94.99-5", "Atividades associativas não especificadas anteriormente", Category.CLASS),
        Classification(
            "95",
            "REPARAÇÃO E MANUTENÇÃO DE EQUIPAMENTOS DE INFORMÁTICA E COMUNICAÇÃO E DE OBJETOS PESSOAIS E DOMÉSTICOS",
            Category.DIVISION,
        ),
        Classification("95.1", "Reparação e manutenção de equipamentos de informática e comunicação", Category.GROUP),
        Classification(
            "95.11-8", "Reparação e manutenção de computadores e de equipamentos periféricos", Category.CLASS
        ),
        Classification("95.12-6", "Reparação e manutenção de equipamentos de comunicação", Category.CLASS),
        Classification(
            "95.2", "Reparação e manutenção de objetos e equipamentos pessoais e domésticos", Category.GROUP
        ),
        Classification(
            "95.21-5",
            "Reparação e manutenção de equipamentos eletroeletrônicos de uso pessoal e doméstico",
            Category.CLASS,
        ),
        Classification(
            "95.29-1",
            "Reparação e manutenção de objetos e equipamentos pessoais e domésticos não especificados anteriormente",
            Category.CLASS,
        ),
        Classification("96", "OUTRAS ATIVIDADES DE SERVIÇOS PESSOAIS", Category.DIVISION),
        Classification("96.0", "Outras atividades de serviços pessoais", Category.GROUP),
        Classification("96.01-7", "Lavanderias, tinturarias e toalheiros", Category.CLASS),
        Classification("96.02-5", "Cabeleireiros e outras atividades de tratamento de beleza", Category.CLASS),
        Classification("96.03-3", "Atividades funerárias e serviços relacionados", Category.CLASS),
        Classification("96.09-2", "Atividades de serviços pessoais não especificadas anteriormente", Category.CLASS),
        Classification("T", "SERVIÇOS DOMÉSTICOS", Category.SECTION),
        Classification("97", "SERVIÇOS DOMÉSTICOS", Category.DIVISION),
        Classification("97.0", "Serviços domésticos", Category.GROUP),
        Classification("97.00-5", "Serviços domésticos", Category.CLASS),
        Classification("U", "ORGANISMOS INTERNACIONAIS E OUTRAS INSTITUIÇÕES EXTRATERRITORIAIS", Category.SECTION),
        Classification("99", "ORGANISMOS INTERNACIONAIS E OUTRAS INSTITUIÇÕES EXTRATERRITORIAIS", Category.DIVISION),
        Classification("99.0", "Organismos internacionais e outras instituições extraterritoriais", Category.GROUP),
        Classification("99.00-8", "Organismos internacionais e outras instituições extraterritoriais", Category.CLASS),
    ],
)
