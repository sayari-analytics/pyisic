"""`GCED2011 Standard <http://www.stat.kg/stat.files/class.files/%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%20%D0%93%D0%9A%D0%AD%D0%94-3.pdf>_`.
"""
from ...types import Category, Classification, Standard, Standards

GCED2011 = Standard(
    standard=Standards.GCED2011,
    classes=[
        Classification("A", "СЕЛЬСКОЕ ХОЗЯЙСТВО, ЛЕСНОЕ ХОЗЯЙСТВО И РЫБОЛОВСТВО", Category.SECTION),
        Classification("01", "Сельское хозяйство, охота и предоставление услуг в этих областях", Category.DIVISION),
        Classification("01.1", "Выращивание немноголетних культур", Category.GROUP),
        Classification("01.11", "Выращивание зерновых (кроме риса), бобовых и масличных культур", Category.CLASS),
        Classification("01.11.1", "Выращивание зерновых культур (кроме риса и гречихи)", Category.SUBCLASS),
        Classification("01.11.2", "Выращивание бобовых культур", Category.SUBCLASS),
        Classification("01.11.9", "Выращивание масличных культур и их семян", Category.SUBCLASS),
        Classification("01.12", "Выращивание риса", Category.CLASS),
        Classification("01.12.0", "Выращивание риса", Category.SUBCLASS),
        Classification("01.13", "Выращивание овощей, бахчевых, корне- и клубнеплодов", Category.CLASS),
        Classification("01.13.1", "Выращивание сахарной свеклы и ее семян", Category.SUBCLASS),
        Classification(
            "01.13.2",
            "Выращивание корне- и клубнеплодов с высоким содержанием крахмала и инулина и их семян",
            Category.SUBCLASS,
        ),
        Classification("01.13.3", "Выращивание грибов и трюфелей", Category.SUBCLASS),
        Classification(
            "01.13.9",
            "Выращивание прочих овощных, бахчевых, корне и клубнеплодовых культур и их семян",
            Category.SUBCLASS,
        ),
        Classification("01.14", "Выращивание сахарного тростника", Category.CLASS),
        Classification("01.14.0", "Выращивание сахарного тростника", Category.SUBCLASS),
        Classification("01.15", "Выращивание табака", Category.CLASS),
        Classification("01.15.0", "Выращивание табака", Category.SUBCLASS),
        Classification("01.16", "Выращивание прядильных (лубяных) культур", Category.CLASS),
        Classification("01.16.1", "Выращивание хлопчатника", Category.SUBCLASS),
        Classification("01.16.2", "Выращивание льна", Category.SUBCLASS),
        Classification("01.16.9", "Выращивание прочих прядильных (лубяных) культур", Category.SUBCLASS),
        Classification("01.19", "Выращивание прочих немноголетних культур", Category.CLASS),
        Classification("01.19.1", "Выращивание кормовых культур и их семян", Category.SUBCLASS),
        Classification("01.19.2", "Выращивание цветов и их семян", Category.SUBCLASS),
        Classification(
            "01.19.9", "Выращивание прочих немноголетних культур, не включенных в другие группировки", Category.SUBCLASS
        ),
        Classification("01.2", "Выращивание многолетних культур", Category.GROUP),
        Classification("01.21", "Выращивание винограда", Category.CLASS),
        Classification("01.21.0", "Выращивание винограда", Category.SUBCLASS),
        Classification("01.22", "Выращивание тропических и субтропических плодов", Category.CLASS),
        Classification("01.22.0", "Выращивание тропических и субтропических плодов", Category.SUBCLASS),
        Classification("01.23", "Выращивание цитрусовых плодов", Category.CLASS),
        Classification("01.23.0", "Выращивание цитрусовых плодов", Category.SUBCLASS),
        Classification("01.24", "Выращивание косточковых и семечковых плодов", Category.CLASS),
        Classification("01.24.1", "Выращивание яблок", Category.SUBCLASS),
        Classification("01.24.9", "Выращивание прочих косточковых и семечковых плодов", Category.SUBCLASS),
        Classification("01.25", "Выращивание прочих плодов ягод и орехов", Category.CLASS),
        Classification("01.25.1", "Выращивание ягод и плодов прочих фруктовых деревьев", Category.SUBCLASS),
        Classification(
            "01.25.9",
            "Выращивание орехов (кроме диких, или несъедобных, орехов земляного ореха и кокосовых орехов)",
            Category.SUBCLASS,
        ),
        Classification("01.26", "Выращивание маслосодержащих плодов", Category.CLASS),
        Classification("01.26.0", "Выращивание маслосодержащих плодов", Category.SUBCLASS),
        Classification("01.27", "Выращивание культур для производства напитков", Category.CLASS),
        Classification("01.27.0", "Выращивание культур для производства напитков", Category.SUBCLASS),
        Classification(
            "01.28",
            "Выращивание специй (пряностей), лекарственных и используемых в парфюмерии растений",
            Category.CLASS,
        ),
        Classification("01.28.1", "Выращивание пряных культур (специй)", Category.SUBCLASS),
        Classification("01.28.2", "Выращивание шишек хмеля", Category.SUBCLASS),
        Classification(
            "01.28.9",
            "Выращивание прочих, растений используемых в парфюмерии, фармацевтике или в качестве инсектицидов фунгицидов или для аналогичных целей",
            Category.SUBCLASS,
        ),
        Classification("01.29", "Выращивание прочих многолетних растений", Category.CLASS),
        Classification("01.29.1", "Выращивание новогодних елок", Category.SUBCLASS),
        Classification(
            "01.29.9", "Выращивание прочих многолетних культур, не включенных в другие группировки", Category.SUBCLASS
        ),
        Classification("01.3", "Воспроизводство (посадка) растений", Category.GROUP),
        Classification("01.30", "Воспроизводство (посадка) растений", Category.CLASS),
        Classification("01.30.0", "Воспроизводство (посадка) растений", Category.SUBCLASS),
        Classification("01.4", "Животноводство", Category.GROUP),
        Classification("01.41", "Разведение крупного рогатого скота молочного направления", Category.CLASS),
        Classification("01.41.0", "Разведение крупного рогатого скота молочного направления", Category.SUBCLASS),
        Classification("01.42", "Разведение прочего крупного рогатого скота", Category.CLASS),
        Classification("01.42.0", "Разведение прочего крупного рогатого скота", Category.SUBCLASS),
        Classification("01.43", "Разведение лошадей, ослов, мулов и лошаков", Category.CLASS),
        Classification("01.43.0", "Разведение лошадей, ослов, мулов и лошаков", Category.SUBCLASS),
        Classification("01.44", "Разведение верблюдов и верблюдиц", Category.CLASS),
        Classification("01.44.0", "Разведение верблюдов и верблюдиц", Category.SUBCLASS),
        Classification("01.45", "Разведение овец и коз", Category.CLASS),
        Classification("01.45.0", "Разведение овец и коз", Category.SUBCLASS),
        Classification("01.46", "Разведение свиней", Category.CLASS),
        Classification("01.46.0", "Разведение свиней", Category.SUBCLASS),
        Classification("01.47", "Разведение сельскохозяйственной птицы", Category.CLASS),
        Classification("01.47.0", "Разведение сельскохозяйственной птицы", Category.SUBCLASS),
        Classification("01.49", "Разведение прочих животных", Category.CLASS),
        Classification("01.49.0", "Разведение прочих животных", Category.SUBCLASS),
        Classification("01.5", "Растениеводство в сочетании с животноводством", Category.GROUP),
        Classification("01.50", "Растениеводство в сочетании с животноводством", Category.CLASS),
        Classification("01.50.0", "Растениеводство в сочетании с животноводством", Category.SUBCLASS),
        Classification("01.6", "Предоставление услуг в области сельского хозяйства и животноводства", Category.GROUP),
        Classification("01.61", "Предоставление услуг в области растениеводства", Category.CLASS),
        Classification("01.61.1", "Эксплуатация ирригационных систем", Category.SUBCLASS),
        Classification(
            "01.61.2", "Услуги по выращиванию сельскохозяйственных культур в теплицах, парниках", Category.SUBCLASS
        ),
        Classification("01.61.9", "Предоставление прочих услуг в области растениеводства", Category.SUBCLASS),
        Classification("01.62", "Предоставление услуг в области животноводства", Category.CLASS),
        Classification("01.62.0", "Предоставление услуг в области животноводства", Category.SUBCLASS),
        Classification(
            "01.63", "Предоставление услуг по обработке урожая сельскохозяйственных культур", Category.CLASS
        ),
        Classification(
            "01.63.0", "Предоставление услуг по обработке урожая сельскохозяйственных культур", Category.SUBCLASS
        ),
        Classification(
            "01.64", "Предоставление услуг по подготовке семян к посадке (формирование семенного фонда)", Category.CLASS
        ),
        Classification(
            "01.64.0",
            "Предоставление услуг по подготовке семян к посадке (формирование семенного фонда)",
            Category.SUBCLASS,
        ),
        Classification(
            "01.7", "Охота, разведение диких животных и предоставление услуг в этих областях", Category.GROUP
        ),
        Classification(
            "01.70", "Охота, разведение диких животных и предоставление услуг в этих областях", Category.CLASS
        ),
        Classification(
            "01.70.0", "Охота, разведение диких животных и предоставление услуг в этих областях", Category.SUBCLASS
        ),
        Classification("02", "Лесное хозяйство и предоставление услуг в этой области", Category.DIVISION),
        Classification(
            "02.1", "Лесоводство и прочая деятельность в области лесоразведения и лесовосстановления", Category.GROUP
        ),
        Classification(
            "02.10", "Лесоводство и прочая деятельность в области лесоразведения и лесовосстановления", Category.CLASS
        ),
        Classification(
            "02.10.0",
            "Лесоводство и прочая деятельность в области лесоразведения и лесовосстановления",
            Category.SUBCLASS,
        ),
        Classification("02.2", "Лесозаготовки", Category.GROUP),
        Classification("02.20", "Лесозаготовки", Category.CLASS),
        Classification("02.20.0", "Лесозаготовки", Category.SUBCLASS),
        Classification("02.3", "Сбор дикорастущих недревесных лесопродуктов", Category.GROUP),
        Classification("02.30", "Сбор дикорастущих недревесных лесопродуктов", Category.CLASS),
        Classification(
            "02.30.1",
            "Сбор дикорастущих лесных грибов и трюфелей, плодов, ягод, орехов и прочих съедобных лесопродуктов",
            Category.SUBCLASS,
        ),
        Classification(
            "02.30.9", "Сбор прочих дикорастущих недревесных лесопродуктов (кроме съедобных)", Category.SUBCLASS
        ),
        Classification("02.4", "Предоставление услуг в области лесного хозяйства", Category.GROUP),
        Classification(
            "02.40", "Предоставление услуг в области лесного хозяйства (лесоразведения и лесозаготовок)", Category.CLASS
        ),
        Classification(
            "02.40.0",
            "Предоставление услуг в области лесного хозяйства (лесоразведения и лесозаготовок)",
            Category.SUBCLASS,
        ),
        Classification("03", "Рыболовство и рыбоводство", Category.DIVISION),
        Classification("03.1", "Рыболовство", Category.GROUP),
        Classification(
            "03.12", "Рыболовство в реках, озерах, водохранилищах (Рыболовство пресноводное)", Category.CLASS
        ),
        Classification(
            "03.12.0", "Рыболовство в реках, озерах, водохранилищах (Рыболовство пресноводное)", Category.SUBCLASS
        ),
        Classification("03.2", "Рыбоводство", Category.GROUP),
        Classification("03.22", "Рыбоводство пресноводное", Category.CLASS),
        Classification("03.22.0", "Рыбоводство пресноводное", Category.SUBCLASS),
        Classification("B", "ДОБЫЧА ПОЛЕЗНЫХ ИСКОПАЕМЫХ", Category.SECTION),
        Classification("05", "Добыча каменного угля и бурого угля (лигнита)", Category.DIVISION),
        Classification("05.1", "Добыча каменного угля", Category.GROUP),
        Classification("05.10", "Добыча каменного угля", Category.CLASS),
        Classification("05.10.0", "Добыча каменного угля", Category.SUBCLASS),
        Classification("05.2", "Добыча бурого угля (лигнита)", Category.GROUP),
        Classification("05.20", "Добыча бурого угля (лигнита)", Category.CLASS),
        Classification("05.20.0", "Добыча бурого угля (лигнита)", Category.SUBCLASS),
        Classification("06", "Добыча сырой нефти и природного газа", Category.DIVISION),
        Classification("06.1", "Добыча сырой нефти", Category.GROUP),
        Classification("06.10", "Добыча сырой нефти", Category.CLASS),
        Classification("06.10.0", "Добыча сырой нефти", Category.SUBCLASS),
        Classification("06.2", "Добыча природного (горючего) газа", Category.GROUP),
        Classification("06.20", "Добыча природного (горючего) газа", Category.CLASS),
        Classification("06.20.0", "Добыча природного (горючего) газа", Category.SUBCLASS),
        Classification("07", "Добыча металлических руд", Category.DIVISION),
        Classification("07.1", "Добыча железных руд", Category.GROUP),
        Classification("07.10", "Добыча железных руд", Category.CLASS),
        Classification("07.10.0", "Добыча железных руд", Category.SUBCLASS),
        Classification("07.2", "Добыча руд цветных металлов", Category.GROUP),
        Classification("07.21", "Добыча урановой и ториевой руд", Category.CLASS),
        Classification("07.21.0", "Добыча урановой и ториевой руд", Category.SUBCLASS),
        Classification("07.29", "Добыча руд прочих цветных металлов", Category.CLASS),
        Classification("07.29.1", "Добыча и обогащение медной руды", Category.SUBCLASS),
        Classification("07.29.2", "Добыча и обогащение никелевых руд", Category.SUBCLASS),
        Classification("07.29.3", "Добыча и обогащение алюминий содержащего сырья", Category.SUBCLASS),
        Classification("07.29.4", "Добыча и обогащение руд драгоценных (благородных) металлов", Category.SUBCLASS),
        Classification("07.29.5", "Добыча и обогащение свинцовых, цинковых и оловянных руд", Category.SUBCLASS),
        Classification(
            "07.29.9",
            "Добыча и обогащение прочих руд цветных металлов, не включенных в другие группировки",
            Category.SUBCLASS,
        ),
        Classification("08", "Добыча прочих полезных ископаемых", Category.DIVISION),
        Classification("08.1", "Добыча камня для строительства, песков, глины", Category.GROUP),
        Classification(
            "08.11", "Добыча отделочного и строительного камня, известняка, гипса, мела и сланца", Category.CLASS
        ),
        Classification("08.11.1", "Добыча отделочного и строительного камня", Category.SUBCLASS),
        Classification("08.11.2", "Добыча известняка и гипса", Category.SUBCLASS),
        Classification("08.11.3", "Добыча мела и некальционированного доломита", Category.SUBCLASS),
        Classification("08.11.9", "Добыча сланцев", Category.SUBCLASS),
        Classification("08.12", "Разработка гравийных и песчаных карьеров, добыча глины и каолина", Category.CLASS),
        Classification("08.12.1", "Добыча гравия и песка", Category.SUBCLASS),
        Classification("08.12.9", "Добыча глины и каолина", Category.SUBCLASS),
        Classification("08.9", "Добыча полезных ископаемых, не включенных в другие группировки", Category.GROUP),
        Classification(
            "08.91", "Добыча минерального сырья для химической промышленности и производства удобрений", Category.CLASS
        ),
        Classification("08.91.1", "Добыча природных фосфатов калийных солей", Category.SUBCLASS),
        Classification("08.91.2", "Добыча природной серы", Category.SUBCLASS),
        Classification(
            "08.91.9",
            "Добыча прочего минерального сырья для химической промышленности и производства удобрений",
            Category.SUBCLASS,
        ),
        Classification("08.92", "Добыча торфа", Category.CLASS),
        Classification("08.92.0", "Добыча торфа", Category.SUBCLASS),
        Classification("08.93", "Добыча соли", Category.CLASS),
        Classification("08.93.0", "Добыча соли", Category.SUBCLASS),
        Classification(
            "08.99", "Добыча прочих полезных ископаемых, не включенных в другие группировки", Category.CLASS
        ),
        Classification("08.99.1", "Добыча природного асфальта и битума", Category.SUBCLASS),
        Classification("08.99.2", "Добыча природных драгоценных и полудрагоценных камней", Category.SUBCLASS),
        Classification("08.99.3", "Добыча природных алмазов", Category.SUBCLASS),
        Classification("08.99.4", "Добыча пемзы и природных абразивных материалов", Category.SUBCLASS),
        Classification("08.99.9", "Добыча прочих природных минералов и горных пород", Category.SUBCLASS),
        Classification("09", "Предоставление услуг по добыче полезных ископаемых", Category.DIVISION),
        Classification("09.1", "Предоставление услуг по добыче нефти и природного газа", Category.GROUP),
        Classification("09.10", "Предоставление услуг по добыче нефти и природного газа", Category.CLASS),
        Classification("09.10.1", "Бурение скважин для добычи нефти и природного газа", Category.SUBCLASS),
        Classification(
            "09.10.2", "Сжижение и повторная газификация для транспортирования природного газа", Category.SUBCLASS
        ),
        Classification("09.10.9", "Предоставление прочих услуг по добыче нефти и природного газа", Category.SUBCLASS),
        Classification("09.9", "Предоставление услуг по добыче прочих полезных ископаемых", Category.GROUP),
        Classification("09.90", "Предоставление услуг по добыче прочих полезных ископаемых", Category.CLASS),
        Classification("09.90.1", "Предоставление услуг по добыче и обогащению каменного угля", Category.SUBCLASS),
        Classification(
            "09.90.9",
            "Предоставление услуг по добыче прочего минерального сырья и строительного камня",
            Category.SUBCLASS,
        ),
        Classification("C", "ОБРАБАТЫВАЮЩИЕ ПРОИЗВОДСТВА (ОБРАБАТЫВАЮЩАЯ ПРОМЫШЛЕННОСТЬ)", Category.SECTION),
        Classification("CA", "ПРОИЗВОДСТВО ПИЩЕВЫХ ПРОДУКТОВ, (ВКЛЮЧАЯ НАПИТКИ), И ТАБАЧНЫХ ИЗДЕЛИЙ", Category.SECTION),
        Classification("10", "Производство пищевых продуктов", Category.DIVISION),
        Classification("10.1", "Производство мясных продуктов", Category.GROUP),
        Classification("10.11", "Производство (переработка и сохранение) мяса, кроме мяса птицы", Category.CLASS),
        Classification(
            "10.11.1",
            "Производство свежего, охлажденного и замороженного мяса и пищевых субпродуктов",
            Category.SUBCLASS,
        ),
        Classification("10.11.9", "Производство прочих продуктов убоя животных, включая диких", Category.SUBCLASS),
        Classification(
            "10.12", "Производство (переработка и сохранение) мяса сельскохозяйст- венной птицы", Category.CLASS
        ),
        Classification(
            "10.12.1",
            "Производство свежего, охлажденного и замороженного мяса птицы и пищевых субпродуктов",
            Category.SUBCLASS,
        ),
        Classification("10.12.9", "Производство прочих продуктов убоя птицы", Category.SUBCLASS),
        Classification("10.13", "Производство продуктов (изделий) из мяса и мяса птицы", Category.CLASS),
        Classification(
            "10.13.1",
            "Производство соленых, в рассоле, сушеных или копченых мяса, мяса птицы и пищевых субпродуктов",
            Category.SUBCLASS,
        ),
        Classification(
            "10.13.9",
            "Производство колбасных и прочих изделий из мяса, мясных субпродуктов или крови животных",
            Category.SUBCLASS,
        ),
        Classification("10.2", "Переработка и консервирование рыбы, ракообразных и моллюсков", Category.GROUP),
        Classification("10.20", "Переработка и консервирование рыбы, ракообразных и моллюсков", Category.CLASS),
        Classification(
            "10.20.1",
            "Охлаждение, замораживание рыбы, ракообразных моллюсков или сохранение их в свежем виде",
            Category.SUBCLASS,
        ),
        Classification(
            "10.20.9",
            "Переработка рыбы, ракообразных и моллюсков прочими способами и производство из них пищевых и непищевых продуктов",
            Category.SUBCLASS,
        ),
        Classification("10.3", "Переработка и консервирование фруктов и овощей", Category.GROUP),
        Classification("10.31", "Переработка и консервирование картофеля", Category.CLASS),
        Classification("10.31.0", "Переработка и консервирование картофеля", Category.SUBCLASS),
        Classification("10.32", "Производство фруктовых и овощных соков", Category.CLASS),
        Classification("10.32.0", "Производство фруктовых и овощных соков", Category.SUBCLASS),
        Classification("10.39", "Прочие способы переработки и консервирования фруктов и овощей", Category.CLASS),
        Classification("10.39.0", "Прочие способы переработки и консервирования фруктов и овощей", Category.SUBCLASS),
        Classification("10.4", "Производство растительных и животных масел и жиров", Category.GROUP),
        Classification("10.41", "Производство растительных и животных масел и жиров", Category.CLASS),
        Classification(
            "10.41.1",
            "Производство нерафинированных (неочищенных) растительных и животных масел и жиров",
            Category.SUBCLASS,
        ),
        Classification(
            "10.41.9", "Производство рафинированных (чищенных) растительных и животных масел и жиров", Category.SUBCLASS
        ),
        Classification("10.42", "Производство маргарина и смешанных пищевых жиров", Category.CLASS),
        Classification("10.42.0", "Производство маргарина и смешанных пищевых жиров", Category.SUBCLASS),
        Classification("10.5", "Производство молочных продуктов", Category.GROUP),
        Classification("10.51", "Переработка молока и производство сыров (сыроварение)", Category.CLASS),
        Classification("10.51.1", "Производство жидкого молока и сливок", Category.SUBCLASS),
        Classification("10.51.9", "Производство сыров и прочих молочных и кисломолочных продуктов", Category.SUBCLASS),
        Classification("10.52", "Производство мороженого", Category.CLASS),
        Classification("10.52.0", "Производство мороженого", Category.SUBCLASS),
        Classification("10.6", "Производство муки и круп, крахмалов и крахмалопродуктов", Category.GROUP),
        Classification("10.61", "Производство муки и круп", Category.CLASS),
        Classification("10.61.1", "Обработка риса и производство рисовой муки", Category.SUBCLASS),
        Classification(
            "10.61.2", "Производство муки из зерновых (кроме риса), овощных культур и орехов", Category.SUBCLASS
        ),
        Classification(
            "10.61.9",
            "Производство круп, гранул и хлопьев для завтрака и прочих аналогичных продуктов",
            Category.SUBCLASS,
        ),
        Classification("10.62", "Производство крахмалов и крахмалопродуктов", Category.CLASS),
        Classification("10.62.0", "Производство крахмалов и крахмалопродуктов", Category.SUBCLASS),
        Classification("10.7", "Производство хлебобулочных изделий и выпечки", Category.GROUP),
        Classification(
            "10.71", "Производство хлеба и мучных кондитерских изделий недлительного хранения", Category.CLASS
        ),
        Classification(
            "10.71.0", "Производство хлеба и мучных кондитерских изделий недлительного хранения", Category.SUBCLASS
        ),
        Classification(
            "10.72", "Производство сухарей и печенья, мучных кондитерских изделий длительного хранения", Category.CLASS
        ),
        Classification(
            "10.72.0",
            "Производство сухарей и печенья, мучных кондитерских изделий длительного хранения",
            Category.SUBCLASS,
        ),
        Classification(
            "10.73",
            "Производство макаронных изделий (макарон, лапши, кускуса и аналогичных мучных продуктов)",
            Category.CLASS,
        ),
        Classification(
            "10.73.0",
            "Производство макаронных изделий (макарон, лапши, кускуса и аналогичных мучных продуктов)",
            Category.SUBCLASS,
        ),
        Classification("10.8", "Производство прочих пищевых продуктов", Category.GROUP),
        Classification("10.81", "Производство сахара", Category.CLASS),
        Classification("10.81.0", "Производство сахара", Category.SUBCLASS),
        Classification("10.82", "Производство какао, шоколада и кондитерских изделий из сахара", Category.CLASS),
        Classification("10.82.0", "Производство какао, шоколада и кондитерских изделий из сахара", Category.SUBCLASS),
        Classification("10.83", "Производство (переработка) чая и кофе", Category.CLASS),
        Classification("10.83.0", "Производство (переработка) чая и кофе", Category.SUBCLASS),
        Classification("10.84", "Производство пряностей и приправ", Category.CLASS),
        Classification("10.84.0", "Производство пряностей и приправ", Category.SUBCLASS),
        Classification("10.85", "Производство готовых блюд", Category.CLASS),
        Classification("10.85.0", "Производство готовых блюд", Category.SUBCLASS),
        Classification(
            "10.86", "Производство гомогенизированных (детского питания) и диетических продуктов", Category.CLASS
        ),
        Classification(
            "10.86.0", "Производство гомогенизированных (детского питания) и диетических продуктов", Category.SUBCLASS
        ),
        Classification(
            "10.89", "Производство прочих пищевых продуктов, не включенных в другие группировки", Category.CLASS
        ),
        Classification("10.89.1", "Производство супов, бульонов и яйцепродуктов", Category.SUBCLASS),
        Classification("10.89.2", "Производство дрожжей", Category.SUBCLASS),
        Classification(
            "10.89.9", "Производство прочих пищевых продуктов, не включенных в другие группировки", Category.SUBCLASS
        ),
        Classification("10.9", "Производство готовых кормов для животных", Category.GROUP),
        Classification("10.91", "Производство готовых кормов для животных, содержащихся на фермах", Category.CLASS),
        Classification(
            "10.91.0", "Производство готовых кормов для животных, содержащихся на фермах", Category.SUBCLASS
        ),
        Classification("10.92", "Производство готовых кормов для домашних животных (питомцев)", Category.CLASS),
        Classification("10.92.0", "Производство готовых кормов для домашних животных (питомцев)", Category.SUBCLASS),
        Classification("11", "Производство напитков", Category.DIVISION),
        Classification("11.0", "Производство напитков", Category.GROUP),
        Classification("11.01", "Очистка ректификация и купажирование спиртов", Category.CLASS),
        Classification("11.01.0", "Очистка ректификация и купажирование спиртов", Category.SUBCLASS),
        Classification("11.02", "Производство вина из винограда", Category.CLASS),
        Classification("11.02.0", "Производство вина из винограда", Category.SUBCLASS),
        Classification("11.03", "Производство сидра и прочих плодово-ягодных вин", Category.CLASS),
        Classification("11.03.0", "Производство сидра и прочих плодово-ягодных вин", Category.SUBCLASS),
        Classification(
            "11.04", "Производство прочих недистиллированных напитков из сброженного материала", Category.CLASS
        ),
        Classification(
            "11.04.0", "Производство прочих недистиллированных напитков из сброженного материала", Category.SUBCLASS
        ),
        Classification("11.05", "Производство пива", Category.CLASS),
        Classification("11.05.0", "Производство пива", Category.SUBCLASS),
        Classification("11.06", "Производство солода", Category.CLASS),
        Classification("11.06.0", "Производство солода", Category.SUBCLASS),
        Classification(
            "11.07",
            "Производство безалкогольных напитков; производство минеральных вод и других вод в бутылках",
            Category.CLASS,
        ),
        Classification(
            "11.07.1",
            "Розлив минеральных вод по бутылкам, включая производство натуральных минеральных вод",
            Category.SUBCLASS,
        ),
        Classification("11.07.2", "Производство национальных напитков (максым, чалап, жарма, бозо)", Category.SUBCLASS),
        Classification(
            "11.07.3",
            "Производство безалкогольных напитков, ароматизированных и/или с добавками сахара (лимонад, оранжад, кола, фруктовые напитки, тоник и т.п.)",
            Category.SUBCLASS,
        ),
        Classification(
            "11.07.9",
            "Производство прочих безалкогольных напитков, не включенных в другие группировки",
            Category.SUBCLASS,
        ),
        Classification("12", "Производство табачных изделий", Category.DIVISION),
        Classification("12.0", "Производство табачных изделий", Category.GROUP),
        Classification("12.00", "Производство табачных изделий", Category.CLASS),
        Classification("12.00.0", "Производство табачных изделий", Category.SUBCLASS),
        Classification(
            "CB",
            "ТЕКСТИЛЬНОЕ ПРОИЗВОДСТВО; ПРОИЗВОДСТВО ОДЕЖДЫ И ОБУВИ, КОЖИ И ПРОЧИХ КОЖАНЫХ ИЗДЕЛИЙ",
            Category.SECTION,
        ),
        Classification("13", "Текстильное производство", Category.DIVISION),
        Classification("13.1", "Подготовка текстильных волокон и пряжи", Category.GROUP),
        Classification("13.10", "Подготовка и прядение текстильных волокон и пряжи", Category.CLASS),
        Classification("13.10.1", "Подготовка и прядение хлопковых волокон", Category.SUBCLASS),
        Classification("13.10.2", "Подготовка и прядение шерстяных волокон", Category.SUBCLASS),
        Classification("13.10.3", "Подготовка и прядение шелковых волокон", Category.SUBCLASS),
        Classification("13.10.4", "Подготовка и прядение льняных волокон", Category.SUBCLASS),
        Classification("13.10.5", "Производство швейных ниток", Category.SUBCLASS),
        Classification("13.10.9", "Подготовка и прядение прочих волокон", Category.SUBCLASS),
        Classification("13.2", "Ткацкое производство", Category.GROUP),
        Classification("13.20", "Ткацкое производство", Category.CLASS),
        Classification("13.20.1", "Производство хлопчатобумажных тканей", Category.SUBCLASS),
        Classification("13.20.2", "Производство шерстяных тканей", Category.SUBCLASS),
        Classification("13.20.3", "Производство шелковых тканей", Category.SUBCLASS),
        Classification("13.20.4", "Производство льняных тканей", Category.SUBCLASS),
        Classification("13.20.9", "Производство прочих тканей", Category.SUBCLASS),
        Classification("13.3", "Отделка тканей и текстильных изделий", Category.GROUP),
        Classification("13.30", "Отделка тканей и текстильных изделий", Category.CLASS),
        Classification("13.30.0", "Отделка тканей и текстильных изделий", Category.SUBCLASS),
        Classification("13.9", "Производство прочих текстильных изделий", Category.GROUP),
        Classification("13.91", "Производство трикотажного полотна машинного или ручного вязания", Category.CLASS),
        Classification("13.91.0", "Производство трикотажного полотна машинного или ручного вязания", Category.SUBCLASS),
        Classification("13.92", "Производство готовых текстильных изделий, кроме одежды", Category.CLASS),
        Classification("13.92.0", "Производство готовых текстильных изделий, кроме одежды", Category.SUBCLASS),
        Classification("13.93", "Производство ковров и ковровых изделий", Category.CLASS),
        Classification("13.93.0", "Производство ковров и ковровых изделий", Category.SUBCLASS),
        Classification("13.94", "Производство канатов, веревок, шпагата и сетей", Category.CLASS),
        Classification("13.94.0", "Производство канатов, веревок, шпагата и сетей", Category.SUBCLASS),
        Classification("13.95", "Производство нетканых текстильных материалов и изделий из них", Category.CLASS),
        Classification("13.95.0", "Производство нетканых текстильных материалов и изделий из них", Category.SUBCLASS),
        Classification(
            "13.96",
            "Производство прочих текстильных изделий технического и производственного назначении",
            Category.CLASS,
        ),
        Classification(
            "13.96.0",
            "Производство прочих текстильных изделий технического и производственного назначения",
            Category.SUBCLASS,
        ),
        Classification(
            "13.99", "Производство прочих текстильных изделий, не включенных в другие группировки", Category.CLASS
        ),
        Classification(
            "13.99.0", "Производство прочих текстильных изделий, не включенных в другие группировки", Category.SUBCLASS
        ),
        Classification("14", "Производство одежды", Category.DIVISION),
        Classification("14.1", "Производство одежды, кроме одежды из меха", Category.GROUP),
        Classification("14.11", "Производство одежды из кожи", Category.CLASS),
        Classification("14.11.0", "Производство одежды из кожи", Category.SUBCLASS),
        Classification("14.12", "Производство рабочей одежды", Category.CLASS),
        Classification("14.12.0", "Производство рабочей одежды", Category.SUBCLASS),
        Classification("14.13", "Производство прочей верхней одежды", Category.CLASS),
        Classification("14.13.0", "Производство прочей верхней одежды", Category.SUBCLASS),
        Classification("14.14", "Производство нижнего белья", Category.CLASS),
        Classification("14.14.0", "Производство нижнего белья", Category.SUBCLASS),
        Classification("14.19", "Производство прочей одежды и аксессуаров", Category.CLASS),
        Classification("14.19.1", "Производство головных уборов", Category.SUBCLASS),
        Classification(
            "14.19.9", "Производство прочей одежды и аксессуаров, не включенных в другие группировки", Category.SUBCLASS
        ),
        Classification("14.2", "Производство меховых изделий", Category.GROUP),
        Classification("14.20", "Производство меховых изделий", Category.CLASS),
        Classification("14.20.0", "Производство меховых изделий", Category.SUBCLASS),
        Classification("14.3", "Производство трикотажных изделий", Category.GROUP),
        Classification("14.31", "Производство трикотажных чулочно-носочных изделий", Category.CLASS),
        Classification("14.31.0", "Производство трикотажных чулочно-носочных изделий", Category.SUBCLASS),
        Classification("14.39", "Производство прочих трикотажных изделий", Category.CLASS),
        Classification("14.39.0", "Производство прочих трикотажных изделий", Category.SUBCLASS),
        Classification("15", "Производство кожи, изделий из кожи, производство обуви", Category.DIVISION),
        Classification(
            "15.1",
            "Дубление и выделка кож; производство чемоданов и аналогичных изделий, шорно-седельных изделий и упряжи; выделка и окраска меха",
            Category.GROUP,
        ),
        Classification("15.11", "Дубление и выделка кожи; выделка и окраска меха", Category.CLASS),
        Classification("15.11.1", "Выделка и окраска меховых шкур (меха)", Category.SUBCLASS),
        Classification(
            "15.11.9",
            "Дубление и выделка прочих шкур и кож; производство натуральной и композиционной кожи",
            Category.SUBCLASS,
        ),
        Classification("15.12", "Производство чемоданов, сумок и других изделий из кожи", Category.CLASS),
        Classification(
            "15.12.1", "Производство чемоданов, сумок, аналогичных изделий и мелкой кожгалантереи", Category.SUBCLASS
        ),
        Classification("15.12.9", "Производство изделий шорно-седельных", Category.SUBCLASS),
        Classification("15.2", "Производство обуви", Category.GROUP),
        Classification("15.20", "Производство обуви", Category.CLASS),
        Classification("15.20.0", "Производство обуви", Category.SUBCLASS),
        Classification(
            "CC", "ПРОИЗВОДСТВО ДЕРЕВЯННЫХ И БУМАЖНЫХ ИЗДЕЛИЙ; ПОЛИГРАФИЧЕСКАЯ ДЕЯТЕЛЬНОСТЬ", Category.SECTION
        ),
        Classification(
            "16",
            "Обработка древесины и производство изделий из дерева и пробки (кроме мебели), плетенных изделий",
            Category.DIVISION,
        ),
        Classification("16.1", "Распиловка и строгание древесины", Category.GROUP),
        Classification("16.10", "Распиловка и строгание древесины", Category.CLASS),
        Classification("16.10.0", "Распиловка и строгание древесины", Category.SUBCLASS),
        Classification("16.2", "Производство изделий из дерева и пробки, плетенных изделий", Category.GROUP),
        Classification("16.21", "Производство шпона, фанеры, плит и панелей из древесины", Category.CLASS),
        Classification("16.21.0", "Производство шпона, фанеры, плит и панелей из древесины", Category.SUBCLASS),
        Classification("16.22", "Производство щитового паркета в сборе", Category.CLASS),
        Classification("16.22.0", "Производство щитового паркета в сборе", Category.SUBCLASS),
        Classification("16.23", "Производство деревянных строительных конструкций и столярных изделий", Category.CLASS),
        Classification("16.23.1", "Производство деревянных сборно-разборных домов", Category.SUBCLASS),
        Classification(
            "16.23.9", "Производство прочих деревянных строительных конструкций и столярных изделий", Category.SUBCLASS
        ),
        Classification("16.24", "Производство деревянной тары", Category.CLASS),
        Classification("16.24.0", "Производство деревянной тары и прочих деревянных изделий", Category.SUBCLASS),
        Classification(
            "16.29",
            "Производство прочих деревянных изделий, изделий из пробки, соломки и растительных материалов для плетения",
            Category.CLASS,
        ),
        Classification(
            "16.29.1",
            "Производство изделий из пробки, соломки и растительных материалов для плетения",
            Category.SUBCLASS,
        ),
        Classification(
            "16.29.9", "Производство прочих деревянных изделий, не включенных в другие группировки", Category.SUBCLASS
        ),
        Classification("17", "Производство бумаги и картона", Category.DIVISION),
        Classification("17.1", "Производство бумажной массы, бумаги и картона", Category.GROUP),
        Classification("17.11", "Производство бумажной массы", Category.CLASS),
        Classification("17.11.0", "Производство бумажной массы", Category.SUBCLASS),
        Classification("17.12", "Производство бумаги и картона", Category.CLASS),
        Classification("17.12.0", "Производство бумаги и картона", Category.SUBCLASS),
        Classification("17.2", "Производство изделий из бумаги и картона", Category.GROUP),
        Classification(
            "17.21", "Производство гофрированного бумаги и картона, бумажной и картонной тары", Category.CLASS
        ),
        Classification("17.21.1", "Производство гофрированных бумаги и картона", Category.SUBCLASS),
        Classification("17.21.9", "Производство бумажной и картонной тары", Category.SUBCLASS),
        Classification(
            "17.22",
            "Производство бумажных изделий хозяйственно-бытового и санитарно-гигиенического назначения",
            Category.CLASS,
        ),
        Classification(
            "17.22.0",
            "Производство бумажных изделий хозяйственно-бытового и санитарно-гигиенического назначения",
            Category.SUBCLASS,
        ),
        Classification("17.23", "Производство писчебумажных изделий", Category.CLASS),
        Classification("17.23.0", "Производство писчебумажных изделий", Category.SUBCLASS),
        Classification("17.24", "Производство обоев", Category.CLASS),
        Classification("17.24.0", "Производство обоев", Category.SUBCLASS),
        Classification("17.29", "Производство прочих изделий из бумаги и картона", Category.CLASS),
        Classification("17.29.0", "Производство прочих изделий из бумаги и картона", Category.SUBCLASS),
        Classification(
            "18", "Полиграфическая деятельность и тиражирование записанных носителей информации", Category.DIVISION
        ),
        Classification("18.1", "Полиграфическая деятельность и предоставление услуг в этой области", Category.GROUP),
        Classification("18.11", "Печатание газет", Category.CLASS),
        Classification("18.11.0", "Печатание газет", Category.SUBCLASS),
        Classification("18.12", "Печатание прочей полиграфической продукции (кроме газет)", Category.CLASS),
        Classification("18.12.0", "Печатание прочей полиграфической продукции (кроме газет)", Category.SUBCLASS),
        Classification("18.13", "Предоставление услуг по подготовке к печати и тиражированию", Category.CLASS),
        Classification("18.13.0", "Предоставление услуг по подготовке к печати и тиражированию", Category.SUBCLASS),
        Classification("18.14", "Переплетная и отделочная деятельность", Category.CLASS),
        Classification("18.14.0", "Переплетная и отделочная деятельность", Category.SUBCLASS),
        Classification(
            "18.2", "Воспроизведение (копирование), тиражирование записанных носителей информации", Category.GROUP
        ),
        Classification(
            "18.20", "Воспроизведение (копирование), тиражирование записанных носителей информации", Category.CLASS
        ),
        Classification(
            "18.20.0", "Воспроизведение (копирование), тиражирование записанных носителей информации", Category.SUBCLASS
        ),
        Classification("CD", "ПРОИЗВОДСТВО КОКСА И ОЧИЩЕННЫХ НЕФТЕПРОДУКТОВ", Category.SECTION),
        Classification("19", "Производство кокса и очищенных нефтепродуктов", Category.DIVISION),
        Classification("19.1", "Производство кокса", Category.GROUP),
        Classification("19.10", "Производство кокса", Category.CLASS),
        Classification("19.10.0", "Производство кокса", Category.SUBCLASS),
        Classification("19.2", "Производство очищенных нефтепродуктов", Category.GROUP),
        Classification("19.20", "Производство очищенных нефтепродуктов", Category.CLASS),
        Classification(
            "19.20.1",
            "Производство очищенных нефтепродуктов, в том числе брикетов из нефтепродуктов",
            Category.SUBCLASS,
        ),
        Classification("19.20.9", "Производство топливных брикетов из угля и торфа", Category.SUBCLASS),
        Classification("CE", "ПРОИЗВОДСТВО ХИМИЧЕСКОЙ ПРОДУКЦИИ", Category.SECTION),
        Classification("20", "Производство химической продукции", Category.DIVISION),
        Classification(
            "20.1",
            "Производство основных химических веществ, удобрений и азотных соединений, пластмасс и синтетического каучука (резины) в первичных формах",
            Category.GROUP,
        ),
        Classification("20.11", "Производство промышленных газов", Category.CLASS),
        Classification("20.11.0", "Производство промышленных газов", Category.SUBCLASS),
        Classification("20.12", "Производство красителей и пигментов", Category.CLASS),
        Classification("20.12.0", "Производство красителей и пигментов", Category.SUBCLASS),
        Classification("20.13", "Производство прочих основных неорганических химических веществ", Category.CLASS),
        Classification("20.13.1", "Производство обогащенного урана", Category.SUBCLASS),
        Classification(
            "20.13.9",
            "Производство прочих основных неорганических химических веществ, не включенных в другие группировки",
            Category.SUBCLASS,
        ),
        Classification("20.14", "Производство прочих органических основных химических веществ", Category.CLASS),
        Classification("20.14.1", "Производство углеводородов и их производных", Category.SUBCLASS),
        Classification("20.14.2", "Производство нециклических и циклических спиртов", Category.SUBCLASS),
        Classification(
            "20.14.9",
            "Производство прочих основных органических химических веществ, не включенных в другие группировки",
            Category.SUBCLASS,
        ),
        Classification("20.15", "Производство удобрений и азотных соединений", Category.CLASS),
        Classification("20.15.0", "Производство удобрений и азотных соединений", Category.SUBCLASS),
        Classification("20.16", "Производство пластмасс в первичных формах", Category.CLASS),
        Classification("20.16.0", "Производство пластмасс в первичных формах", Category.SUBCLASS),
        Classification("20.17", "Производство синтетического каучука в первичных формах", Category.CLASS),
        Classification("20.17.0", "Производство синтетического каучука в первичных формах", Category.SUBCLASS),
        Classification("20.2", "Производство пестицидов и прочих агрохимических продуктов", Category.GROUP),
        Classification("20.20", "Производство пестицидов и прочих агрохимических продуктов", Category.CLASS),
        Classification("20.20.0", "Производство пестицидов и прочих агрохимических продуктов", Category.SUBCLASS),
        Classification(
            "20.3", "Производство красок, лаков и аналогичных покрытий, типографских красок и мастик", Category.GROUP
        ),
        Classification(
            "20.30", "Производство красок, лаков и аналогичных покрытий, типографских красок и мастик", Category.CLASS
        ),
        Classification("20.30.1", "Производство красок, эмалей и лаков на основе полимеров", Category.SUBCLASS),
        Classification(
            "20.30.9",
            "Производство прочих красок (в т.ч. типографских), эмалей, мастик и связанных с ними продуктов (разбавителей, растворителей и т.п.)",
            Category.SUBCLASS,
        ),
        Classification(
            "20.4",
            "Производство мыла и моющих, чистящих и полирующих средств, парфюмерных и косметических средств",
            Category.GROUP,
        ),
        Classification("20.41", "Производство мыла и моющих, чистящих и полирующих средств", Category.CLASS),
        Classification("20.41.0", "Производство мыла и моющих, чистящих и полирующих средств", Category.SUBCLASS),
        Classification("20.42", "Производство парфюмерных и косметических средств", Category.CLASS),
        Classification("20.42.0", "Производство парфюмерных и косметических средств", Category.SUBCLASS),
        Classification("20.5", "Производство прочих химических продуктов", Category.GROUP),
        Classification("20.51", "Производство взрывчатых веществ", Category.CLASS),
        Classification("20.51.0", "Производство взрывчатых веществ", Category.SUBCLASS),
        Classification("20.52", "Производство клеев", Category.CLASS),
        Classification("20.52.0", "Производство клеев", Category.SUBCLASS),
        Classification("20.53", "Производство эфирных масел", Category.CLASS),
        Classification("20.53.0", "Производство эфирных масел", Category.SUBCLASS),
        Classification(
            "20.59", "Производство прочих химических продуктов, не включенных в другие группировки", Category.CLASS
        ),
        Classification("20.59.1", "Производство фотохимических материалов", Category.SUBCLASS),
        Classification("20.59.2", "Производство желатина и его производных", Category.SUBCLASS),
        Classification(
            "20.59.9",
            "Производство различных химических продуктов, не включенных в другие группировки",
            Category.SUBCLASS,
        ),
        Classification("20.6", "Производство химических (искусственных и синтетических) волокон", Category.GROUP),
        Classification("20.60", "Производство химических (искусственных и синтетических) волокон", Category.CLASS),
        Classification("20.60.0", "Производство химических (искусственных и синтетических) волокон", Category.SUBCLASS),
        Classification("CF", "ПРОИЗВОДСТВО ФАРМАЦЕВТИЧЕСКОЙ ПРОДУКЦИИ", Category.SECTION),
        Classification("21", "Производство фармацевтической продукции", Category.DIVISION),
        Classification("21.1", "Производство основных фармацевтических продуктов", Category.GROUP),
        Classification("21.10", "Производство основных фармацевтических продуктов", Category.CLASS),
        Classification("21.10.0", "Производство основных фармацевтических продуктов", Category.SUBCLASS),
        Classification("21.2", "Производство фармацевтических препаратов и материалов", Category.GROUP),
        Classification("21.20", "Производство фармацевтических препаратов и материалов", Category.CLASS),
        Classification("21.20.1", "Производство радиоактивных веществ дли диагностики", Category.SUBCLASS),
        Classification(
            "21.20.9", "Производство прочих медикаментов, фармацевтических препаратов и материалов", Category.SUBCLASS
        ),
        Classification(
            "CG",
            "ПРОИЗВОДСТВО РЕЗИНОВЫХ И ПЛАСТМАССОВЫХ ИЗДЕЛИЙ, ПРОЧИХ НЕМЕТАЛЛИЧЕСКИХ МИНЕРАЛЬНЫХ ПРОДУКТОВ",
            Category.SECTION,
        ),
        Classification("22", "Производство резиновых и пластмассовых изделий", Category.DIVISION),
        Classification("22.1", "Производство резиновых изделий", Category.GROUP),
        Classification("22.11", "Производство резиновых шин, покрышек и камер", Category.CLASS),
        Classification("22.11.1", "Производство резиновых шин, покрышек и камер", Category.SUBCLASS),
        Classification("22.11.9", "Восстановление резиновых шин и покрышек", Category.SUBCLASS),
        Classification("22.19", "Производство прочих резиновых изделий", Category.CLASS),
        Classification("22.2", "Производство пластмассовых изделий", Category.GROUP),
        Classification("22.21", "Производство пластмассовых плит, полос, труб и профилей", Category.CLASS),
        Classification("22.21.0", "Производство пластмассовых плит, полос, труб и профилей", Category.SUBCLASS),
        Classification("22.22", "Производство пластмассовых изделий для упаковывания товаров", Category.CLASS),
        Classification("22.22.0", "Производство пластмассовых изделий для упаковывания товаров", Category.SUBCLASS),
        Classification("22.23", "Производство пластмассовых изделий, используемых в строительстве", Category.CLASS),
        Classification(
            "22.23.0", "Производство пластмассовых изделий, используемых в строительстве", Category.SUBCLASS
        ),
        Classification("22.29", "Производство прочих пластмассовых изделий", Category.CLASS),
        Classification("22.29.0", "Производство прочих пластмассовых изделий", Category.SUBCLASS),
        Classification("23", "Производство прочих неметаллических минеральных продуктов", Category.DIVISION),
        Classification("23.1", "Производство стекла и изделий из стекла", Category.GROUP),
        Classification("23.11", "Производство листового стекла", Category.CLASS),
        Classification("23.11.0", "Производство листового стекла", Category.SUBCLASS),
        Classification("23.12", "Формование и обработка листового стекла", Category.CLASS),
        Classification("23.12.0", "Формование и обработка листового стекла", Category.SUBCLASS),
        Classification("23.13", "Производство полых стеклянных изделий", Category.CLASS),
        Classification("23.13.0", "Производство полых стеклянных изделий", Category.SUBCLASS),
        Classification("23.14", "Производство стекловолокна", Category.CLASS),
        Classification("23.14.0", "Производство стекловолокна", Category.SUBCLASS),
        Classification("23.19", "Производство и обработка прочих стеклянных изделий", Category.CLASS),
        Classification(
            "23.19.1",
            "Производство лабораторных, гигиенических и фармацевтических стеклянных изделий",
            Category.SUBCLASS,
        ),
        Classification(
            "23.19.9",
            "Производство технического и прочего стекла и стеклянных изделий, не включенных в другие группировки",
            Category.SUBCLASS,
        ),
        Classification("23.2", "Производство огнеупоров", Category.GROUP),
        Classification("23.20", "Производство огнеупоров", Category.CLASS),
        Classification("23.20.0", "Производство огнеупоров", Category.SUBCLASS),
        Classification("23.3", "Производство прочих строительных изделий из глины", Category.GROUP),
        Classification("23.31", "Производство керамических плиток и плит", Category.CLASS),
        Classification("23.31.0", "Производство керамических плиток и плит", Category.SUBCLASS),
        Classification(
            "23.32", "Производство кирпича, черепицы и прочих строительных изделий из обожженной глины", Category.CLASS
        ),
        Classification(
            "23.32.0",
            "Производство кирпича, черепицы и прочих строительных изделий из обожженной глины",
            Category.SUBCLASS,
        ),
        Classification("23.4", "Производство прочих изделий из керамики и фарфора", Category.GROUP),
        Classification("23.41", "Производство керамических хозяйственных и декоративных изделий", Category.CLASS),
        Classification("23.41.0", "Производство керамических хозяйственных и декоративных изделий", Category.SUBCLASS),
        Classification("23.42", "Производство керамических санитарно-технических изделий", Category.CLASS),
        Classification("23.42.0", "Производство керамических санитарно-технических изделий", Category.SUBCLASS),
        Classification("23.43", "Производство керамических электроизоляторов и изолирующей арматуры", Category.CLASS),
        Classification(
            "23.43.0", "Производство керамических электроизоляторов и изолирующей арматуры", Category.SUBCLASS
        ),
        Classification("23.44", "Производство прочих керамических технических изделий", Category.CLASS),
        Classification("23.44.0", "Производство прочих керамических технических изделий", Category.SUBCLASS),
        Classification("23.49", "Производство прочих керамических изделий", Category.CLASS),
        Classification("23.49.0", "Производство прочих керамических изделий", Category.SUBCLASS),
        Classification("23.5", "Производство цемента, извести и гипса", Category.GROUP),
        Classification("23.51", "Производство цемента", Category.CLASS),
        Classification("23.51.0", "Производство цемента", Category.SUBCLASS),
        Classification("23.52", "Производство извести и гипса", Category.CLASS),
        Classification("23.52.0", "Производство извести и гипса", Category.SUBCLASS),
        Classification("23.6", "Производство изделий из бетона, гипса и цемента", Category.GROUP),
        Classification("23.61", "Производство изделий из бетона для использования в строительстве", Category.CLASS),
        Classification(
            "23.61.0", "Производство изделий из бетона для использования в строительстве", Category.SUBCLASS
        ),
        Classification("23.62", "Производство изделий из гипса для использования в строительстве", Category.CLASS),
        Classification("23.62.0", "Производство изделий из гипса для использования в строительстве", Category.SUBCLASS),
        Classification("23.63", "Производство товарного бетона (готовой бетонной смеси)", Category.CLASS),
        Classification("23.63.0", "Производство товарного бетона (готовой бетонной смеси)", Category.SUBCLASS),
        Classification("23.64", "Производство сухих бетонных смесей", Category.CLASS),
        Classification("23.64.0", "Производство сухих бетонных смесей", Category.SUBCLASS),
        Classification("23.65", "Производство изделий из асбестоцемента (волокнистого цемента)", Category.CLASS),
        Classification("23.65.0", "Производство изделий из асбестоцемента (волокнистого цемента)", Category.SUBCLASS),
        Classification("23.69", "Производство прочих изделий из бетона, гипса и цемента", Category.CLASS),
        Classification("23.69.0", "Производство прочих изделий из бетона, гипса и цемента", Category.SUBCLASS),
        Classification("23.7", "Резка, обработка и отделка декоративного и строительного камня", Category.GROUP),
        Classification("23.70", "Резка, обработка и отделка декоративного и строительного камня", Category.CLASS),
        Classification("23.70.0", "Резка, обработка и отделка декоративного и строительного камня", Category.SUBCLASS),
        Classification(
            "23.9",
            "Производство абразивных изделий и прочей неметаллической минеральной продукции, не включенной в другие группировки",
            Category.GROUP,
        ),
        Classification("23.91", "Производство абразивных изделий", Category.CLASS),
        Classification("23.91.0", "Производство абразивных изделий", Category.SUBCLASS),
        Classification(
            "23.99",
            "Производство прочей неметаллической минеральной продукции, не включенной в другие группировки",
            Category.CLASS,
        ),
        Classification("23.99.1", "Производство асбестовых технических изделий", Category.SUBCLASS),
        Classification(
            "23.99.9",
            "Производство прочей неметаллической минеральной продукции, в другом месте непоименованной",
            Category.SUBCLASS,
        ),
        Classification(
            "CH",
            "ПРОИЗВОДСТВО ОСНОВНЫХ МЕТАЛЛОВ И ГОТОВЫХ МЕТАЛЛИЧЕСКИХ ИЗДЕЛИЙ, КРОМЕ МАШИН И ОБОРУДОВАНИЯ",
            Category.SECTION,
        ),
        Classification("24", "Производство основных металлов", Category.DIVISION),
        Classification("24.1", "Производство чугуна, стали и ферросплавов", Category.GROUP),
        Classification("24.10", "Производство чугуна, стали и ферросплавов", Category.CLASS),
        Classification("24.10.0", "Производство чугуна, стали и ферросплавов", Category.SUBCLASS),
        Classification("24.2", "Производство стальных труб, полых профилей и фитингов", Category.GROUP),
        Classification("24.20", "Производство стальных труб, полых профилей и фитингов", Category.CLASS),
        Classification("24.20.0", "Производство стальных труб, полых профилей и фитингов", Category.SUBCLASS),
        Classification("24.3", "Прочая первичная обработка чугуна и стали", Category.GROUP),
        Classification("24.31", "Холодное волочение", Category.CLASS),
        Classification("24.31.0", "Холодное волочение", Category.SUBCLASS),
        Classification("24.32", "Холодная прокатка лент и узких полос", Category.CLASS),
        Classification("24.32.0", "Холодная прокатка лент и узких полос", Category.SUBCLASS),
        Classification("24.33", "Холодная штамповка и гибка", Category.CLASS),
        Classification("24.33.0", "Холодная штамповка и гибка", Category.SUBCLASS),
        Classification("24.34", "Производство проволоки", Category.CLASS),
        Classification("24.34.0", "Производство проволоки", Category.SUBCLASS),
        Classification("24.4", "Производство цветных металлов", Category.GROUP),
        Classification("24.41", "Производство благородных (драгоценных) металлов", Category.CLASS),
        Classification("24.41.0", "Производство благородных (драгоценных) металлов", Category.SUBCLASS),
        Classification("24.42", "Производство алюминия", Category.CLASS),
        Classification("24.42.0", "Производство алюминия", Category.SUBCLASS),
        Classification("24.43", "Производство свинца, цинка и олова", Category.CLASS),
        Classification("24.43.0", "Производство свинца, цинка и олова", Category.SUBCLASS),
        Classification("24.44", "Производство меди", Category.CLASS),
        Classification("24.44.0", "Производство меди", Category.SUBCLASS),
        Classification("24.45", "Производство прочих цветных металлов", Category.CLASS),
        Classification("24.45.1", "Производство никеля и изделий из него", Category.SUBCLASS),
        Classification(
            "24.45.9",
            "Производство прочих цветных металлов, не включенных в другие группировки, и изделия из них",
            Category.SUBCLASS,
        ),
        Classification("24.46", "Производство ядерных материалов (ядерного топлива)", Category.CLASS),
        Classification("24.46.0", "Производство ядерных материалов (ядерного топлива)", Category.SUBCLASS),
        Classification("24.5", "Литье металлов", Category.GROUP),
        Classification("24.51", "Литье чугуна", Category.CLASS),
        Classification("24.51.0", "Литье чугуна", Category.SUBCLASS),
        Classification("24.52", "Литье стали", Category.CLASS),
        Classification("24.52.0", "Литье стали", Category.SUBCLASS),
        Classification("24.53", "Литье легких металлов", Category.CLASS),
        Classification("24.53.0", "Литье легких металлов", Category.SUBCLASS),
        Classification("24.54", "Литье прочих цветных металлов", Category.CLASS),
        Classification("24.54.0", "Литье прочих цветных металлов", Category.SUBCLASS),
        Classification(
            "25", "Производство готовых металлических изделий, кроме машин и оборудования", Category.DIVISION
        ),
        Classification("25.1", "Производство строительных металлических конструкций и изделий", Category.GROUP),
        Classification("25.11", "Производство строительных металлических конструкций", Category.CLASS),
        Classification("25.11.0", "Производство строительных металлических конструкций", Category.SUBCLASS),
        Classification("25.12", "Производство металлических дверей и оконных рам", Category.CLASS),
        Classification("25.12.0", "Производство металлических дверей и оконных рам", Category.SUBCLASS),
        Classification(
            "25.2", "Производство металлических резервуаров, радиаторов и котлов центрального отопления", Category.GROUP
        ),
        Classification("25.21", "Производство радиаторов и котлов центрального отопления", Category.CLASS),
        Classification("25.21.0", "Производство радиаторов и котлов центрального отопления", Category.SUBCLASS),
        Classification("25.29", "Производство прочих металлических цистерн, резервуаров и контейнеров", Category.CLASS),
        Classification(
            "25.29.0", "Производство прочих металлических цистерн, резервуаров и контейнеров", Category.SUBCLASS
        ),
        Classification("25.3", "Производство паровых котлов, кроме котлов центрального отопления", Category.GROUP),
        Classification("25.30", "Производство паровых котлов, кроме котлов центрального отопления", Category.CLASS),
        Classification(
            "25.30.0", "Производство паровых котлов, кроме котлов центрального отопления", Category.SUBCLASS
        ),
        Classification("25.4", "Производство оружия и боеприпасов", Category.GROUP),
        Classification("25.40", "Производство оружия и боеприпасов", Category.CLASS),
        Classification("25.40.0", "Производство оружия и боеприпасов", Category.SUBCLASS),
        Classification("25.5", "Ковка, прессование, штамповка, прокатка; порошковая металлургия", Category.GROUP),
        Classification("25.50", "Ковка, прессование, штамповка, прокатка; порошковая металлургия", Category.CLASS),
        Classification("25.50.1", "Ковка, прессование, штамповка, прокатка", Category.SUBCLASS),
        Classification(
            "25.50.9", "Изготовление металлических изделий методом порошковой металлургии", Category.SUBCLASS
        ),
        Classification(
            "25.6",
            "Обработка металлов и нанесение покрытий на металлы; основные технологические процессы машиностроения",
            Category.GROUP,
        ),
        Classification("25.61", "Обработка металлов и нанесение покрытий на металлы", Category.CLASS),
        Classification("25.61.0", "Обработка металлов и нанесение покрытий на металлы", Category.SUBCLASS),
        Classification("25.62", "Основные технологические процессы машиностроения", Category.CLASS),
        Classification("25.62.0", "Основные технологические процессы машиностроения", Category.SUBCLASS),
        Classification("25.7", "Производство ножевых изделий, инструментов и скобяных изделий", Category.GROUP),
        Classification("25.71", "Производство ножевых изделий", Category.CLASS),
        Classification("25.71.0", "Производство ножевых изделий", Category.SUBCLASS),
        Classification("25.72", "Производство замков и петель", Category.CLASS),
        Classification("25.72.0", "Производство замков и петель", Category.SUBCLASS),
        Classification("25.73", "Производство инструментов", Category.CLASS),
        Classification(
            "25.73.1",
            "Производство ручных инструментов для использования в сельском хозяйстве, садоводстве или лесном хозяйстве",
            Category.SUBCLASS,
        ),
        Classification("25.73.9", "Производство прочих инструментов", Category.SUBCLASS),
        Classification("25.9", "Производство прочих готовых металлических изделий", Category.GROUP),
        Classification("25.91", "Производство металлических бочек и аналогичных емкостей", Category.CLASS),
        Classification("25.91.0", "Производство металлических бочек и аналогичных емкостей", Category.SUBCLASS),
        Classification("25.92", "Производство упаковки из легких металлов", Category.CLASS),
        Classification("25.92.0", "Производство упаковки из легких металлов", Category.SUBCLASS),
        Classification("25.93", "Производство изделий из проволоки, цепей и пружин", Category.CLASS),
        Classification("25.93.1", "Производство изделий из проволоки", Category.SUBCLASS),
        Classification("25.93.9", "Производство цепей и пружин", Category.SUBCLASS),
        Classification("25.94", "Производство крепежных изделий, резьбовых изделий", Category.CLASS),
        Classification("25.94.0", "Производство крепежных изделий, резьбовых изделий", Category.SUBCLASS),
        Classification(
            "25.99",
            "Производство прочих готовых металлических изделий, не включенных в другие группировки",
            Category.CLASS,
        ),
        Classification(
            "25.99.1",
            "Производство металлических изделий санитарно-технического и хозяйственно-бытового назначения",
            Category.SUBCLASS,
        ),
        Classification(
            "25.99.9",
            "Производство прочих готовых металлических изделий, в другом месте непоименованных",
            Category.SUBCLASS,
        ),
        Classification("CI", "ПРОИЗВОДСТВО КОМПЬЮТЕРОВ, ЭЛЕКТРОННОГО И ОПТИЧЕСКОГО ОБОРУДОВАНИЯ", Category.SECTION),
        Classification("26", "Производство компьютеров, электронного и оптического оборудования", Category.DIVISION),
        Classification("26.1", "Производство электронных компонентов и плат (схем)", Category.GROUP),
        Classification("26.11", "Производство электронных компонентов", Category.CLASS),
        Classification("26.11.0", "Производство электронных компонентов", Category.SUBCLASS),
        Classification("26.12", "Производство электронных плат (схем)", Category.CLASS),
        Classification("26.12.0", "Производство электронных плат (схем)", Category.SUBCLASS),
        Classification("26.2", "Производство компьютеров и периферийных устройств", Category.GROUP),
        Classification("26.20", "Производство компьютеров и периферийных устройств", Category.CLASS),
        Classification("26.20.0", "Производство компьютеров и периферийных устройств", Category.SUBCLASS),
        Classification("26.3", "Производство телекоммуникационного оборудования (оборудования связи)", Category.GROUP),
        Classification("26.30", "Производство телекоммуникационного оборудования (оборудования связи)", Category.CLASS),
        Classification(
            "26.30.1", "Производство теле- и радиоаппаратуры производственного назначения", Category.SUBCLASS
        ),
        Classification(
            "26.30.2", "Производство аппаратуры для проводной телефонной или телеграфной связи", Category.SUBCLASS
        ),
        Classification("26.30.9", "Производство электросигнального и прочего оборудования связи", Category.SUBCLASS),
        Classification("26.4", "Производство бытовой электронной аппаратуры", Category.GROUP),
        Classification("26.40", "Производство бытовой электронной аппаратуры", Category.CLASS),
        Classification("26.40.0", "Производство бытовой электронной аппаратуры", Category.SUBCLASS),
        Classification(
            "26.5",
            "Производство приборов и инструментов для измерения, контроля, испытаний и навигации; производство часов всех типов",
            Category.GROUP,
        ),
        Classification(
            "26.51",
            "Производство приборов и инструментов для измерения, контроля, испытаний, навигации",
            Category.CLASS,
        ),
        Classification(
            "26.51.1",
            "Производство навигационных, метеорологических, геофизических и аналогических приборов и инструментов",
            Category.SUBCLASS,
        ),
        Classification("26.51.9", "Производство прочих контрольно-измерительных приборов", Category.SUBCLASS),
        Classification("26.52", "Производство часов всех типов", Category.CLASS),
        Classification("26.52.1", "Производство наручных и прочих часов", Category.SUBCLASS),
        Classification(
            "26.52.9",
            "Производство деталей и принадлежностей для часов; производство прочих приборов для регистрации времени",
            Category.SUBCLASS,
        ),
        Classification(
            "26.6",
            "Производство рентгеновского, электромедицинского и электротерапевтического оборудования",
            Category.GROUP,
        ),
        Classification(
            "26.60",
            "Производство рентгеновского, электромедицинского и электротерапевтического оборудования",
            Category.CLASS,
        ),
        Classification(
            "26.60.0",
            "Производство рентгеновского, электромедицинского и электротерапевтического оборудования",
            Category.SUBCLASS,
        ),
        Classification("26.7", "Производство оптических приборов и фотооборудования", Category.GROUP),
        Classification("26.70", "Производство оптических приборов и фотооборудования", Category.CLASS),
        Classification("26.70.1", "Производство фото- и кинооборудования и их частей", Category.SUBCLASS),
        Classification(
            "26.70.9",
            "Производство очков, линз, оптических микроскопов, биноклей и прочих оптических приборов и их частей",
            Category.SUBCLASS,
        ),
        Classification("26.8", "Производство магнитных и оптических носителей информации", Category.GROUP),
        Classification("26.80", "Производство магнитных и оптических носителей информации", Category.CLASS),
        Classification("26.80.0", "Производство магнитных и оптических носителей информации", Category.SUBCLASS),
        Classification("CJ", "ПРОИЗВОДСТВО ЭЛЕКТРИЧЕСКОГО ОБОРУДОВАНИЯ", Category.SECTION),
        Classification("27", "Производство электрического оборудования", Category.DIVISION),
        Classification(
            "27.1",
            "Производство электродвигателей, генераторов и трансформаторов, электрораспределительной и регулирующей аппаратуры",
            Category.GROUP,
        ),
        Classification("27.11", "Производство электродвигателей, генераторов и трансформаторов", Category.CLASS),
        Classification("27.11.0", "Производство электродвигателей, генераторов и трансформаторов", Category.SUBCLASS),
        Classification("27.12", "Производство электрораспределительной и регулирующей аппаратуры", Category.CLASS),
        Classification("27.12.0", "Производство электрораспределительной и регулирующей аппаратуры", Category.SUBCLASS),
        Classification(
            "27.2", "Производство первичных элементов, батарей первичных элементов и их частей", Category.GROUP
        ),
        Classification(
            "27.20", "Производство первичных элементов, батарей первичных элементов и их частей", Category.CLASS
        ),
        Classification(
            "27.20.0", "Производство первичных элементов, батарей первичных элементов и их частей", Category.SUBCLASS
        ),
        Classification("27.3", "Производство проводов и кабелей и приспособлений для электропроводки", Category.GROUP),
        Classification("27.31", "Производство волоконно-оптических кабелей", Category.CLASS),
        Classification("27.31.0", "Производство волоконно-оптических кабелей", Category.SUBCLASS),
        Classification("27.32", "Производство прочих изолированных проводов и кабелей", Category.CLASS),
        Classification("27.32.0", "Производство прочих изолированных проводов и кабелей", Category.SUBCLASS),
        Classification("27.33", "Производство приспособлений для электропроводки", Category.CLASS),
        Classification("27.33.0", "Производство приспособлений для электропроводки", Category.SUBCLASS),
        Classification("27.4", "Производство электрического осветительного оборудования", Category.GROUP),
        Classification("27.40", "Производство электрического осветительного оборудования", Category.CLASS),
        Classification("27.40.0", "Производство электрического осветительного оборудования", Category.SUBCLASS),
        Classification("27.5", "Производство бытовых приборов", Category.GROUP),
        Classification("27.51", "Производство бытовых электрических приборов", Category.CLASS),
        Classification("27.51.1", "Производство бытовых холодильников и морозильников", Category.SUBCLASS),
        Classification("27.51.9", "Производство прочих бытовых электроприборов", Category.SUBCLASS),
        Classification("27.52", "Производство бытовых неэлектрических приборов", Category.CLASS),
        Classification("27.52.0", "Производство бытовых неэлектрических приборов", Category.SUBCLASS),
        Classification("27.9", "Производство прочего электрического оборудования", Category.GROUP),
        Classification("27.90", "Производство прочего электрического оборудования", Category.CLASS),
        Classification("27.90.1", "Производство электросварочного оборудования", Category.SUBCLASS),
        Classification("27.90.2", "Производство электродной продукции", Category.SUBCLASS),
        Classification(
            "27.90.9",
            "Производство прочего электрического оборудования, не включенного в другие группировки",
            Category.SUBCLASS,
        ),
        Classification("CK", "ПРОИЗВОДСТВО МАШИН И ОБОРУДОВАНИЯ, НЕ ВКЛЮЧЕННЫХ В ДРУГИЕ ГРУППИРОВКИ", Category.SECTION),
        Classification(
            "28", "Производство машин и оборудования, не включенных в другие группировки", Category.DIVISION
        ),
        Classification("28.1", "Производство машин и оборудования общего назначения", Category.GROUP),
        Classification(
            "28.11",
            "Производство двигателей и турбин, кроме авиационных, автомобильных и мотоциклетных двигателей",
            Category.CLASS,
        ),
        Classification(
            "28.11.1",
            "Производство двигателей и их частей кроме авиационных, автомобильных, и мотоциклетных двигателей",
            Category.SUBCLASS,
        ),
        Classification("28.11.9", "Производство турбин и их частей", Category.SUBCLASS),
        Classification("28.12", "Производство гидравлического и пневматического силового оборудования", Category.CLASS),
        Classification(
            "28.12.0", "Производство гидравлического и пневматического силового оборудования", Category.SUBCLASS
        ),
        Classification("28.13", "Производство прочих насосов и компрессоров", Category.CLASS),
        Classification(
            "28.13.1", "Производство насосов для перекачки жидкостей и подъемников жидкостей", Category.SUBCLASS
        ),
        Classification(
            "28.13.9",
            "Производство воздушных или вакуумных насосов, воздушных или прочих газовых компрессоров",
            Category.SUBCLASS,
        ),
        Classification("28.14", "Производство кранов и клапанов", Category.CLASS),
        Classification("28.14.0", "Производство кранов и клапанов", Category.SUBCLASS),
        Classification(
            "28.15",
            "Производство подшипников, зубчатых передач, элементов механических передач и приводов",
            Category.CLASS,
        ),
        Classification("28.15.1", "Производство подшипников", Category.SUBCLASS),
        Classification("28.15.9", "Производство прочих общемашиностроительных узлов и деталей", Category.SUBCLASS),
        Classification("28.2", "Производство прочих машин и оборудования общего назначения", Category.GROUP),
        Classification("28.21", "Производство печей и печных горелок", Category.CLASS),
        Classification("28.21.1", "Производство электрических печей и печных грелок", Category.SUBCLASS),
        Classification("28.21.9", "Производство прочих (неэлектрических) печей и печных грелок", Category.SUBCLASS),
        Classification("28.22", "Производство подъемно-транспортного оборудования", Category.CLASS),
        Classification("28.22.1", "Производство подъемных кранов и их частей", Category.SUBCLASS),
        Classification("28.22.2", "Производство оборудования непрерывного транспорта и его части", Category.SUBCLASS),
        Classification(
            "28.22.9",
            "Производство прочего подъемно-транспортного, погрузочно-разгрузочного оборудования и его частей",
            Category.SUBCLASS,
        ),
        Classification(
            "28.23",
            "Производство офисного оборудования (кроме компьютеров и периферийного оборудования)",
            Category.CLASS,
        ),
        Classification(
            "28.23.0",
            "Производство офисного оборудования (кроме компьютеров и периферийного оборудования)",
            Category.SUBCLASS,
        ),
        Classification("28.24", "Производство ручных механизированных инструментов", Category.CLASS),
        Classification("28.24.0", "Производство ручных механизированных инструментов", Category.SUBCLASS),
        Classification(
            "28.25", "Производство промышленного холодильного и вентиляционного оборудования", Category.CLASS
        ),
        Classification(
            "28.25.0", "Производство промышленного холодильного и вентиляционного оборудования", Category.SUBCLASS
        ),
        Classification(
            "28.29",
            "Производство прочих машин и оборудования общего назначения, не включенных в другие группировки",
            Category.CLASS,
        ),
        Classification("28.29.1", "Производство фильтрующего и очистительного оборудования", Category.SUBCLASS),
        Classification(
            "28.29.2",
            "Производство машин и оборудования для распыления и разбрызгивания жидкостей или порошков, упаковочных и оберточных машин",
            Category.SUBCLASS,
        ),
        Classification(
            "28.29.3",
            "Производство весоизмерительного оборудования (кроме прецизионных лабораторных весов)",
            Category.SUBCLASS,
        ),
        Classification(
            "28.29.9",
            "Производство прочих машин и оборудования общего назначения деталей и узлов к ним, в другом месте не поименованных",
            Category.SUBCLASS,
        ),
        Classification("28.3", "Производство машин и оборудования для сельского и лесного хозяйства", Category.GROUP),
        Classification("28.30", "Производство машин и оборудования для сельского и лесного хозяйства", Category.CLASS),
        Classification(
            "28.30.1", "Производство тракторов для сельского и лесного хозяйства и частей к ним", Category.SUBCLASS
        ),
        Classification(
            "28.30.2", "Производство прочих машин и оборудования для растениеводства и частей к ним", Category.SUBCLASS
        ),
        Classification(
            "28.30.3",
            "Производство прочих машин и оборудования для животноводства и приготовления кормов и частей к ним",
            Category.SUBCLASS,
        ),
        Classification(
            "28.30.9", "Производство прочих машин и оборудования для лесозаготовок и мелиорации", Category.SUBCLASS
        ),
        Classification("28.4", "Производство станков", Category.GROUP),
        Classification("28.41", "Производство металлорежущих станков", Category.CLASS),
        Classification("28.41.0", "Производство металлорежущих станков", Category.SUBCLASS),
        Classification("28.49", "Производство прочих станков", Category.CLASS),
        Classification(
            "28.49.1",
            "Производство станков для обработки камня, дерева, керамики и аналогичных твердых материалов",
            Category.SUBCLASS,
        ),
        Classification(
            "28.49.9",
            "Производство прочих станков и оборудования, не включенных в другие группировки",
            Category.SUBCLASS,
        ),
        Classification("28.9", "Производство прочих машин и оборудования специального назначения", Category.GROUP),
        Classification("28.91", "Производство машин и оборудования для металлургии", Category.CLASS),
        Classification("28.91.0", "Производство машин и оборудования для металлургии", Category.SUBCLASS),
        Classification(
            "28.92", "Производство машин и оборудования для добычи полезных ископаемых и строительства", Category.CLASS
        ),
        Classification(
            "28.92.0",
            "Производство машин и оборудования для добычи полезных ископаемых и строительства",
            Category.SUBCLASS,
        ),
        Classification(
            "28.93",
            "Производство машин и оборудования для изготовления пищевых продуктов, включая напитки, и табачных изделий",
            Category.CLASS,
        ),
        Classification(
            "28.93.0",
            "Производство машин и оборудования для изготовления пищевых продуктов, включая напитки, и табачных изделий",
            Category.SUBCLASS,
        ),
        Classification(
            "28.94",
            "Производство машин и оборудования для изготовления текстильных, швейных, меховых и кожаных изделий",
            Category.CLASS,
        ),
        Classification(
            "28.94.1", "Производство машин и оборудования для изготовления текстильных изделий", Category.SUBCLASS
        ),
        Classification(
            "28.94.2",
            "Производство машин и оборудований для изготовления швейных и трикотажных изделий",
            Category.SUBCLASS,
        ),
        Classification("28.94.3", "Производство бытовых швейных машин", Category.SUBCLASS),
        Classification(
            "28.94.4",
            "Производство машин и оборудования для обработки кожи и меха и производства обуви и прочих кожаных и меховых изделий",
            Category.SUBCLASS,
        ),
        Classification(
            "28.94.9",
            "Производство машин и оборудования для прачечных и прочих предприятий бытового обслуживания",
            Category.SUBCLASS,
        ),
        Classification("28.95", "Производство машин и оборудования для изготовления бумаги и картона", Category.CLASS),
        Classification(
            "28.95.0", "Производство машин и оборудования для изготовления бумаги и картона", Category.SUBCLASS
        ),
        Classification(
            "28.96", "Производство машин и оборудования для обработки мягкой резины или пластмасс", Category.CLASS
        ),
        Classification(
            "28.96.0", "Производство машин и оборудования для обработки мягкой резины или пластмасс", Category.SUBCLASS
        ),
        Classification(
            "28.99",
            "Производство прочих машин и оборудования специального назначения, не включенных в другие группировки",
            Category.CLASS,
        ),
        Classification(
            "28.99.1", "Производство печатных и брошюровочно-переплетных машин и оборудования", Category.SUBCLASS
        ),
        Classification(
            "28.99.9",
            "Производство прочих машин и оборудования специального назначения в другом месте не поименованных",
            Category.SUBCLASS,
        ),
        Classification("CL", "ПРОИЗВОДСТВО ТРАНСПОРТНЫХ СРЕДСТВ", Category.SECTION),
        Classification("29", "Производство автомобилей", Category.DIVISION),
        Classification("29.1", "Производство автомобилей", Category.GROUP),
        Classification("29.10", "Производство автомобилей", Category.CLASS),
        Classification("29.10.1", "Производство автомобилей", Category.SUBCLASS),
        Classification("29.10.9", "Производство автомобильных двигателей", Category.SUBCLASS),
        Classification("29.2", "Производство автомобильных кузовов; производство прицепов", Category.GROUP),
        Classification("29.20", "Производство автомобильных кузовов; производство прицепов", Category.CLASS),
        Classification("29.20.1", "Производство автомобильных кузовов", Category.SUBCLASS),
        Classification("29.20.2", "Производство прицепов, полуприцепов, контейнеров и их частей", Category.SUBCLASS),
        Classification("29.3", "Производство частей и принадлежностей автомобилей", Category.GROUP),
        Classification("29.31", "Производство электрооборудования для автомобилей", Category.CLASS),
        Classification("29.31.0", "Производство электрооборудования для автомобилей", Category.SUBCLASS),
        Classification("29.32", "Производство прочих частей и принадлежностей автомобилей", Category.CLASS),
        Classification("29.32.0", "Производство прочих частей и принадлежностей автомобилей", Category.SUBCLASS),
        Classification("30", "Производство прочих транспортных средств", Category.DIVISION),
        Classification("30.1", "Строительство судов", Category.GROUP),
        Classification("30.11", "Строительство судов и плавучих средств", Category.CLASS),
        Classification("30.11.0", "Строительство судов и плавучих средств", Category.SUBCLASS),
        Classification("30.12", "Строительство спортивных судов", Category.CLASS),
        Classification("30.12.0", "Строительство спортивных судов", Category.SUBCLASS),
        Classification("30.2", "Производство железнодорожного подвижного состава", Category.GROUP),
        Classification("30.20", "Производство железнодорожного подвижного состава", Category.CLASS),
        Classification("30.20.0", "Производство железнодорожного подвижного состава", Category.SUBCLASS),
        Classification("30.3", "Производство летательных аппаратов, включая космические", Category.GROUP),
        Classification("30.30", "Производство летательных аппаратов, включая космические", Category.CLASS),
        Classification("30.30.1", "Производство межконтинентальных баллистических ракет", Category.SUBCLASS),
        Classification("30.30.2", "Производство космических летательных аппаратов и их частей", Category.SUBCLASS),
        Classification("30.30.9", "Производство прочих летательных аппаратов и их частей", Category.SUBCLASS),
        Classification("30.4", "Производство военных боевых машин", Category.GROUP),
        Classification("30.40", "Производство военных боевых машин", Category.CLASS),
        Classification("30.40.0", "Производство военных боевых машин", Category.SUBCLASS),
        Classification(
            "30.9", "Производство прочих транспортных средств, не включенных в другие группировки", Category.GROUP
        ),
        Classification("30.91", "Производство мотоциклов", Category.CLASS),
        Classification("30.91.0", "Производство мотоциклов", Category.SUBCLASS),
        Classification("30.92", "Производство велосипедов и инвалидных колясок", Category.CLASS),
        Classification("30.92.1", "Производство велосипедов и их частей", Category.SUBCLASS),
        Classification("30.92.2", "Производство инвалидных колясок и их частей", Category.SUBCLASS),
        Classification("30.92.9", "Производство детских колясок и их частей", Category.SUBCLASS),
        Classification(
            "30.99",
            "Производство прочих транспортных средств и оборудования, не включенных в другие группировки",
            Category.CLASS,
        ),
        Classification(
            "30.99.0",
            "Производство прочих транспортных средств и оборудования, не включенных в другие группировки",
            Category.SUBCLASS,
        ),
        Classification("CM", "ПРОЧИЕ ПРОИЗВОДСТВА, РЕМОНТ И УСТАНОВКА МАШИН И ОБОРУДОВАНИЯ", Category.SECTION),
        Classification("31", "Производство мебели", Category.DIVISION),
        Classification("31.0", "Производство мебели", Category.GROUP),
        Classification("31.01", "Производство мебели для офисов и предприятий торговли", Category.CLASS),
        Classification("31.01.0", "Производство мебели для офисов и предприятий торговли", Category.SUBCLASS),
        Classification("31.02", "Производство кухонной мебели", Category.CLASS),
        Classification("31.02.0", "Производство кухонной мебели", Category.SUBCLASS),
        Classification("31.03", "Производство матрасов", Category.CLASS),
        Classification("31.03.0", "Производство матрасов", Category.SUBCLASS),
        Classification("31.09", "Производство прочей мебели", Category.CLASS),
        Classification("31.09.0", "Производство прочей мебели", Category.SUBCLASS),
        Classification("32", "Производство прочей продукции", Category.DIVISION),
        Classification("32.1", "Производство ювелирных изделий, монет и медалей", Category.GROUP),
        Classification("32.11", "Чеканка монет и медалей", Category.CLASS),
        Classification("32.11.0", "Чеканка монет и медалей", Category.SUBCLASS),
        Classification("32.12", "Производство ювелирных изделий", Category.CLASS),
        Classification("32.12.0", "Производство ювелирных изделий", Category.SUBCLASS),
        Classification("32.13", "Производство бижутерии и аналогичных изделий", Category.CLASS),
        Classification("32.13.0", "Производство бижутерии и аналогичных изделий", Category.SUBCLASS),
        Classification("32.2", "Производство музыкальных инструментов", Category.GROUP),
        Classification("32.20", "Производство музыкальных инструментов", Category.CLASS),
        Classification("32.20.0", "Производство музыкальных инструментов", Category.SUBCLASS),
        Classification("32.3", "Производство спортивных товаров", Category.GROUP),
        Classification("32.30", "Производство спортивных товаров", Category.CLASS),
        Classification("32.30.0", "Производство спортивных товаров", Category.SUBCLASS),
        Classification("32.4", "Производство игр и игрушек", Category.GROUP),
        Classification("32.40", "Производство игр и игрушек", Category.CLASS),
        Classification("32.40.0", "Производство игр и игрушек", Category.SUBCLASS),
        Classification(
            "32.5", "Производство инструментов и приспособлений, используемых в медицине и стоматологии", Category.GROUP
        ),
        Classification(
            "32.50",
            "Производство инструментов и приспособлений, используемых в медицине и стоматологии",
            Category.CLASS,
        ),
        Classification(
            "32.50.0",
            "Производство инструментов и приспособлений, используемых в медицине и стоматологии",
            Category.SUBCLASS,
        ),
        Classification("32.9", "Производство прочей продукции, не включенной в другие группировки", Category.GROUP),
        Classification("32.91", "Производство метел и щеток", Category.CLASS),
        Classification("32.91.0", "Производство метел и щеток", Category.SUBCLASS),
        Classification("32.99", "Производство различной продукции, не включенной в другие группировки", Category.CLASS),
        Classification(
            "32.99.1", "Производство защитных головных уборов, одежды и прочих защитных средств", Category.SUBCLASS
        ),
        Classification(
            "32.99.2", "Производство наборов пишущих принадлежностей и прочих канцелярских изделий", Category.SUBCLASS
        ),
        Classification(
            "32.99.9",
            "Производство прочей продукции, в другом месте не поименованной (включая набивку чучел)",
            Category.SUBCLASS,
        ),
        Classification("33", "Ремонт и установка машин и оборудования", Category.DIVISION),
        Classification("33.1", "Ремонт готовых металлических изделий, машин и оборудования", Category.GROUP),
        Classification("33.11", "Ремонт готовых металлических изделий", Category.CLASS),
        Classification("33.11.1", "Ремонт и техническое обслуживание металлоконструкций", Category.SUBCLASS),
        Classification(
            "33.11.2",
            "Ремонт и техническое обслуживание металлических цистерн, баков, резервуаров и емкостей",
            Category.SUBCLASS,
        ),
        Classification(
            "33.11.3", "Ремонт и техническое обслуживание радиаторов и котлов центрального отопления", Category.SUBCLASS
        ),
        Classification(
            "33.11.4", "Ремонт и техническое обслуживание парогенераторов и прочих водяных котлов", Category.SUBCLASS
        ),
        Classification("33.11.5", "Ремонт и техническое обслуживание оружия и систем вооружения", Category.SUBCLASS),
        Classification("33.11.9", "Ремонт прочих готовых металлических изделий", Category.SUBCLASS),
        Classification("33.12", "Ремонт продукции машиностроения", Category.CLASS),
        Classification(
            "33.12.1", "Ремонт и техническое обслуживание оборудования общего назначения", Category.SUBCLASS
        ),
        Classification(
            "33.12.9", "Ремонт и техническое обслуживание оборудования специального назначения", Category.SUBCLASS
        ),
        Classification("33.13", "Ремонт электронного и оптического оборудования", Category.CLASS),
        Classification(
            "33.13.1",
            "Ремонт и техническое обслуживание приборов и инструментов для измерения контроля испытаний и навигации группы 26.5",
            Category.SUBCLASS,
        ),
        Classification(
            "33.13.2",
            "Ремонт и техническое обслуживание медицинских инструментов, рентгеновского, электромедицинского и электротерапевтического оборудования группы 26.6",
            Category.SUBCLASS,
        ),
        Classification(
            "33.13.9",
            "Ремонт и техническое обслуживание профессиональных оптических приборов и фотооборудования группы 26.7",
            Category.SUBCLASS,
        ),
        Classification("33.14", "Ремонт электрического оборудования", Category.CLASS),
        Classification(
            "33.14.1",
            "Ремонт и техническое обслуживание электродвигателей, генераторов и трансформаторов, электрораспределительной и регулирующей аппаратуры группы 27.1",
            Category.SUBCLASS,
        ),
        Classification(
            "33.14.9",
            "Ремонт и техническое обслуживание прочего электрического оборудования раздела 27, кроме группы 27.1",
            Category.SUBCLASS,
        ),
        Classification("33.15", "Ремонт и техническое обслуживание водного транспорта", Category.CLASS),
        Classification("33.15.0", "Ремонт и техническое обслуживание водного транспорта", Category.SUBCLASS),
        Classification(
            "33.16", "Ремонт и техническое обслуживание летательных аппаратов и космических аппаратов", Category.CLASS
        ),
        Classification(
            "33.16.0",
            "Ремонт и техническое обслуживание летательных аппаратов и космических аппаратов",
            Category.SUBCLASS,
        ),
        Classification("33.17", "Ремонт и техническое обслуживание прочего транспортного оборудования", Category.CLASS),
        Classification(
            "33.17.1",
            "Ремонт и техническое обслуживание железнодорожных локомотивов и подвижного состава, в том числе трамваев, вагонов метро и троллейбусов",
            Category.SUBCLASS,
        ),
        Classification(
            "33.17.9",
            "Ремонт и техническое обслуживание прочего транспортного оборудования, не включенного в другие группировки",
            Category.SUBCLASS,
        ),
        Classification("33.19", "Ремонт прочего оборудования", Category.CLASS),
        Classification("33.19.0", "Ремонт прочего оборудования", Category.SUBCLASS),
        Classification("33.2", "Установка промышленных машин и оборудования", Category.GROUP),
        Classification("33.20", "Установка промышленных машин и оборудования", Category.CLASS),
        Classification(
            "33.20.1", "Установка готовых металлических изделий (кроме машин и оборудования)", Category.SUBCLASS
        ),
        Classification("33.20.2", "Установка машин и оборудования общего назначения", Category.SUBCLASS),
        Classification("33.20.3", "Установка машин и оборудования специального назначения", Category.SUBCLASS),
        Classification("33.20.4", "Установка электронного и оптического оборудования", Category.SUBCLASS),
        Classification("33.20.5", "Установка электрического оборудования", Category.SUBCLASS),
        Classification("33.20.6", "Установка оборудования контроля за технологическими процессами", Category.SUBCLASS),
        Classification(
            "33.20.9", "Установка прочего оборудования, не включенного в другие группировки", Category.SUBCLASS
        ),
        Classification(
            "D", "ОБЕСПЕЧЕНИЕ (СНАБЖЕНИЕ) ЭЛЕКТРОЭНЕРГИЕЙ, ГАЗОМ, ПАРОМ И КОНДИЦИОНИРОВАННЫМ ВОЗДУХОМ", Category.SECTION
        ),
        Classification(
            "35",
            "Обеспечение (снабжение) электроэнергией, газом, паром и кондиционированным воздухом",
            Category.DIVISION,
        ),
        Classification("35.1", "Производство (выработка) электроэнергии, ее передача и распределение", Category.GROUP),
        Classification("35.11", "Производство электроэнергии", Category.CLASS),
        Classification("35.11.1", "Производство электроэнергии тепловыми электростанциями", Category.SUBCLASS),
        Classification("35.11.2", "Производство электроэнергии гидроэлектростанциями", Category.SUBCLASS),
        Classification(
            "35.11.3", "Производство электроэнергии ядерными (атомными) электростанциями", Category.SUBCLASS
        ),
        Classification("35.11.9", "Производство электроэнергии прочими электростанциями", Category.SUBCLASS),
        Classification("35.12", "Передача электроэнергии", Category.CLASS),
        Classification("35.12.0", "Передача электроэнергии", Category.SUBCLASS),
        Classification("35.13", "Распределение электроэнергии", Category.CLASS),
        Classification("35.13.0", "Распределение электроэнергии", Category.SUBCLASS),
        Classification("35.14", "Продажа электроэнергии", Category.CLASS),
        Classification("35.14.0", "Продажа электроэнергии", Category.SUBCLASS),
        Classification(
            "35.2", "Производство газа; распределение газообразного топлива через системы газоснабжения", Category.GROUP
        ),
        Classification("35.21", "Производство газообразного топлива", Category.CLASS),
        Classification("35.21.0", "Производство газообразного топлива", Category.SUBCLASS),
        Classification("35.22", "Распределение газообразного топлива через системы газоснабжения", Category.CLASS),
        Classification("35.22.0", "Распределение газообразного топлива через системы газоснабжения", Category.SUBCLASS),
        Classification(
            "35.23", "Продажа газообразного топлива, поступающего через системы газоснабжения", Category.CLASS
        ),
        Classification(
            "35.23.0", "Продажа газообразного топлива, поступающего через системы газоснабжения", Category.SUBCLASS
        ),
        Classification("35.3", "Обеспечение (снабжение) паром и кондиционированным воздухом", Category.GROUP),
        Classification("35.30", "Обеспечение (снабжение) паром и кондиционированным воздухом", Category.CLASS),
        Classification("35.30.0", "Обеспечение (снабжение) паром и кондиционированным воздухом", Category.SUBCLASS),
        Classification("E", "ВОДОСНАБЖЕНИЕ, ОЧИСТКА, ОБРАБОТКА ОТХОДОВ И ПОЛУЧЕНИЕ ВТОРИЧНОГО СЫРЬЯ", Category.SECTION),
        Classification("36", "Сбор, обработка и распределение воды (водоснабжение)", Category.DIVISION),
        Classification("36.0", "Сбор, обработка и распределение воды (водоснабжение)", Category.GROUP),
        Classification("36.00", "Сбор, обработка и распределение воды (водоснабжение)", Category.CLASS),
        Classification("36.00.0", "Сбор, обработка и распределение воды (водоснабжение)", Category.SUBCLASS),
        Classification("37", "Сбор и обработка сточных вод", Category.DIVISION),
        Classification("37.0", "Сбор и обработка сточных вод", Category.GROUP),
        Classification("37.00", "Сбор и обработка сточных вод", Category.CLASS),
        Classification("37.00.0", "Сбор и обработка сточных вод", Category.SUBCLASS),
        Classification("38", "Сбор, обработка и уничтожение отходов, получение вторичного сырья", Category.DIVISION),
        Classification("38.1", "Сбор отходов", Category.GROUP),
        Classification("38.11", "Сбор безопасных отходов", Category.CLASS),
        Classification("38.11.0", "Сбор безопасных отходов", Category.SUBCLASS),
        Classification("38.12", "Сбор опасных отходов", Category.CLASS),
        Classification("38.12.0", "Сбор опасных отходов", Category.SUBCLASS),
        Classification("38.2", "Обработка и уничтожение отходов", Category.GROUP),
        Classification("38.21", "Обработка и уничтожение безопасных отходов", Category.CLASS),
        Classification("38.21.0", "Обработка и уничтожение безопасных отходов", Category.SUBCLASS),
        Classification("38.22", "Обработка и уничтожение опасных отходов", Category.CLASS),
        Classification("38.22.0", "Обработка и уничтожение опасных отходов", Category.SUBCLASS),
        Classification("38.3", "Получение вторичного сырья", Category.GROUP),
        Classification("38.31", "Разрезка и разбор остатков судов, машин и прочего оборудования", Category.CLASS),
        Classification("38.31.0", "Разрезка и разбор остатков судов, машин и прочего оборудования", Category.SUBCLASS),
        Classification("38.32", "Сортировка и переработка отходов для получения вторичного сырья", Category.CLASS),
        Classification("38.32.0", "Сортировка и переработка отходов для получения вторичного сырья", Category.SUBCLASS),
        Classification("39", "Обеззараживание и прочая обработка отходов", Category.DIVISION),
        Classification("39.0", "Обеззараживание и прочая обработка отходов", Category.GROUP),
        Classification("39.00", "Обеззараживание и прочая обработка отходов", Category.CLASS),
        Classification("39.00.0", "Обеззараживание и прочая обработка отходов", Category.SUBCLASS),
        Classification("F", "СТРОИТЕЛЬСТВО", Category.SECTION),
        Classification("41", "Строительство зданий", Category.DIVISION),
        Classification("41.1", "Разработка строительных проектов", Category.GROUP),
        Classification("41.10", "Разработка строительных проектов", Category.CLASS),
        Classification("41.10.0", "Разработка строительных проектов", Category.SUBCLASS),
        Classification("41.2", "Строительство жилых и нежилых зданий", Category.GROUP),
        Classification("41.20", "Строительство жилых и нежилых зданий", Category.CLASS),
        Classification("41.20.0", "Строительство жилых и нежилых зданий", Category.SUBCLASS),
        Classification("42", "Строительство объектов гражданского назначения", Category.DIVISION),
        Classification("42.1", "Строительство автомобильных и железных дорог", Category.GROUP),
        Classification("42.11", "Строительство шоссе и автомагистралей", Category.CLASS),
        Classification("42.11.0", "Строительство шоссе и автомагистралей", Category.SUBCLASS),
        Classification("42.12", "Строительство железных дорог", Category.CLASS),
        Classification("42.12.0", "Строительство железных дорог", Category.SUBCLASS),
        Classification("42.13", "Строительство мостов и туннелей", Category.CLASS),
        Classification("42.13.0", "Строительство мостов и туннелей", Category.SUBCLASS),
        Classification("42.2", "Строительство прочих объектов гражданского назначения", Category.GROUP),
        Classification("42.21", "Строительство трубопроводов", Category.CLASS),
        Classification("42.21.0", "Строительство трубопроводов", Category.SUBCLASS),
        Classification("42.22", "Строительство линий электропередач и телекоммуникаций", Category.CLASS),
        Classification("42.22.0", "Строительство линий электропередач и телекоммуникаций", Category.SUBCLASS),
        Classification(
            "42.9",
            "Строительство прочих объектов гражданского назначения, не включенных в другие группировки",
            Category.GROUP,
        ),
        Classification("42.91", "Строительство водных сооружений", Category.CLASS),
        Classification("42.91.0", "Строительство водных сооружений", Category.SUBCLASS),
        Classification(
            "42.99",
            "Строительство прочих объектов гражданского назначения, в другом месте не поименованных",
            Category.CLASS,
        ),
        Classification(
            "42.99.0",
            "Строительство прочих объектов гражданского назначения, в другом месте не поименованных",
            Category.SUBCLASS,
        ),
        Classification("43", "Специальные строительные работы", Category.DIVISION),
        Classification("43.1", "Снос зданий и подготовка строительного участка", Category.GROUP),
        Classification("43.11", "Снос зданий", Category.CLASS),
        Classification("43.11.0", "Снос зданий", Category.SUBCLASS),
        Classification("43.12", "Подготовка строительного участка", Category.CLASS),
        Classification("43.12.0", "Подготовка строительного участка", Category.SUBCLASS),
        Classification("43.13", "Разведочное бурение", Category.CLASS),
        Classification("43.13.0", "Разведочное бурение", Category.SUBCLASS),
        Classification(
            "43.2",
            "Монтаж (установка) электрических и водопроводных систем и прочие строительно-монтажные работы",
            Category.GROUP,
        ),
        Classification("43.21", "Электромонтажные работы", Category.CLASS),
        Classification("43.21.0", "Электромонтажные работы", Category.SUBCLASS),
        Classification(
            "43.22",
            "Монтаж (установка) водопроводных систем, систем отопления, вентиляции, кондиционирования воздуха",
            Category.CLASS,
        ),
        Classification(
            "43.22.0",
            "Монтаж (установка) водопроводных систем, систем отопления, вентиляции, кондиционирования воздуха",
            Category.SUBCLASS,
        ),
        Classification("43.29", "Прочие строительно-монтажные работы", Category.CLASS),
        Classification("43.29.1", "Изоляционные работы", Category.SUBCLASS),
        Classification(
            "43.29.9", "Прочие строительно-монтажные работы, не включенные в другие группировки", Category.SUBCLASS
        ),
        Classification("43.3", "Работы по завершению строительства и отделочные работы", Category.GROUP),
        Classification("43.31", "Штукатурные работы", Category.CLASS),
        Classification("43.31.0", "Штукатурные работы", Category.SUBCLASS),
        Classification("43.32", "Столярные и плотницкие работы", Category.CLASS),
        Classification("43.32.0", "Столярные и плотницкие работы", Category.SUBCLASS),
        Classification("43.33", "Покрытие полов и облицовка стен", Category.CLASS),
        Classification("43.33.0", "Покрытие полов и облицовка стен", Category.SUBCLASS),
        Classification("43.34", "Малярные и стекольные работы", Category.CLASS),
        Classification("43.34.0", "Малярные и стекольные работы", Category.SUBCLASS),
        Classification("43.39", "Прочие отделочные и завершающие работы", Category.CLASS),
        Classification("43.39.0", "Прочие отделочные и завершающие работы", Category.SUBCLASS),
        Classification("43.9", "Прочие специальные строительные работы", Category.GROUP),
        Classification("43.91", "Кровельные работы", Category.CLASS),
        Classification("43.91.0", "Кровельные работы", Category.SUBCLASS),
        Classification(
            "43.99", "Прочие специальные строительные работы, не включенные в другие группировки", Category.CLASS
        ),
        Classification("43.99.1", "Закладка фундамента, включая забивку свай", Category.SUBCLASS),
        Classification("43.99.2", "Бурение и постройка водяных колодцев, артезианских скважин", Category.SUBCLASS),
        Classification("43.99.3", "Кладка кирпичей и камней", Category.SUBCLASS),
        Classification(
            "43.99.9", "Прочие специальные строительные работы, в другом месте не поименованные", Category.SUBCLASS
        ),
        Classification("G", "ОПТОВАЯ И РОЗНИЧНАЯ ТОРГОВЛЯ; РЕМОНТ АВТОМОБИЛЕЙ И МОТОЦИКЛОВ", Category.SECTION),
        Classification(
            "45",
            "Оптовая и розничная торговля автомобилями и мотоциклами; ремонт автомобилей и мотоциклов",
            Category.DIVISION,
        ),
        Classification("45.1", "Торговля автомобилями", Category.GROUP),
        Classification("45.11", "Торговля автомобилями и легкими автотранспортными средствами", Category.CLASS),
        Classification(
            "45.11.1", "Оптовая торговля автомобилями и легкими автотранспортными средствами", Category.SUBCLASS
        ),
        Classification(
            "45.11.9", "Розничная торговля автомобилями и легкими автотранспортными средствами", Category.SUBCLASS
        ),
        Classification("45.19", "Торговля прочими автотранспортными средствами", Category.CLASS),
        Classification("45.19.1", "Оптовая торговля прочими автотранспортными средствами", Category.SUBCLASS),
        Classification("45.19.9", "Розничная торговля прочими автотранспортными средствами", Category.SUBCLASS),
        Classification("45.2", "Техническое обслуживание и ремонт автомобилей", Category.GROUP),
        Classification("45.20", "Техническое обслуживание и ремонт автомобилей", Category.CLASS),
        Classification("45.20.1", "Техническое обслуживание и ремонт легковых автомобилей", Category.SUBCLASS),
        Classification("45.20.9", "Техническое обслуживание и ремонт прочих автомобилей", Category.SUBCLASS),
        Classification("45.3", "Торговля автомобильными деталями, узлами и принадлежностями", Category.GROUP),
        Classification("45.31", "Оптовая торговля автомобильными деталями, узлами и принадлежностями", Category.CLASS),
        Classification(
            "45.31.0", "Оптовая торговля автомобильными деталями, узлами и принадлежностями", Category.SUBCLASS
        ),
        Classification(
            "45.32", "Розничная торговля автомобильными деталями, узлами и принадлежностями", Category.CLASS
        ),
        Classification(
            "45.32.0", "Розничная торговля автомобильными деталями, узлами и принадлежностями", Category.SUBCLASS
        ),
        Classification(
            "45.4",
            "Торговля мотоциклами, их деталями, узлами и принадлежностями; техническое обслуживание и ремонт мотоциклов",
            Category.GROUP,
        ),
        Classification(
            "45.40",
            "Торговля мотоциклами, их деталями, узлами и принадлежностями; техническое обслуживание и ремонт мотоциклов",
            Category.CLASS,
        ),
        Classification(
            "45.40.1", "Оптовая торговля мотоциклами, их деталями, узлами и принадлежностями", Category.SUBCLASS
        ),
        Classification(
            "45.40.2", "Розничная торговля мотоциклами, их деталями, узлами и принадлежностями", Category.SUBCLASS
        ),
        Classification("45.40.9", "Техническое обслуживание и ремонт мотоциклов", Category.SUBCLASS),
        Classification("46", "Оптовая торговля, кроме торговли автомобилями и мотоциклами", Category.DIVISION),
        Classification(
            "46.1", "Оптовая торговля через агентов (за вознаграждение или на договорной основе)", Category.GROUP
        ),
        Classification(
            "46.11",
            "Деятельность агентов по оптовой торговле сельскохозяйственным сырьем, живыми животными, текстильным сырьем и полуфабрикатами",
            Category.CLASS,
        ),
        Classification(
            "46.11.0",
            "Деятельность агентов по оптовой торговле сельскохозяйственным сырьем, живыми животными, текстильным сырьем и полуфабрикатами",
            Category.SUBCLASS,
        ),
        Classification(
            "46.12",
            "Деятельность агентов по оптовой торговле топливом, рудами, металлами и химическими веществами",
            Category.CLASS,
        ),
        Classification(
            "46.12.0",
            "Деятельность агентов по оптовой торговле топливом, рудами, металлами и химическими веществами",
            Category.SUBCLASS,
        ),
        Classification(
            "46.13", "Деятельность агентов по оптовой торговле древесиной и строительными материалами", Category.CLASS
        ),
        Classification(
            "46.13.0",
            "Деятельность агентов по оптовой торговле древесиной и строительными материалами",
            Category.SUBCLASS,
        ),
        Classification(
            "46.14",
            "Деятельность агентов по оптовой торговле машинами, оборудованием, судами и летательными аппаратами",
            Category.CLASS,
        ),
        Classification(
            "46.14.0",
            "Деятельность агентов по оптовой торговле машинами, оборудованием, судами и летательными аппаратами",
            Category.SUBCLASS,
        ),
        Classification(
            "46.15",
            "Деятельность агентов по оптовой торговле мебелью, бытовыми товарами, скобяными и прочими металлическими изделиями",
            Category.CLASS,
        ),
        Classification(
            "46.15.0",
            "Деятельность агентов по оптовой торговле мебелью, бытовыми товарами, скобяными и прочими металлическими изделиями",
            Category.SUBCLASS,
        ),
        Classification(
            "46.16",
            "Деятельность агентов по оптовой торговле текстильными изделиями, одеждой, обувью, изделиями из кожи и меха",
            Category.CLASS,
        ),
        Classification(
            "46.16.0",
            "Деятельность агентов по оптовой торговле текстильными изделиями, одеждой, обувью, изделиями из кожи и меха",
            Category.SUBCLASS,
        ),
        Classification(
            "46.17",
            "Деятельность агентов по оптовой торговле пищевыми продуктами, включая напитки, и табачными изделиями",
            Category.CLASS,
        ),
        Classification(
            "46.17.0",
            "Деятельность агентов по оптовой торговле пищевыми продуктами, включая напитки, и табачными изделиями",
            Category.SUBCLASS,
        ),
        Classification(
            "46.18",
            "Деятельность агентов, специализирующихся на оптовой торговле отдельными видами товаров или группами товаров, не включенными в другие группировки",
            Category.CLASS,
        ),
        Classification(
            "46.18.0",
            "Деятельность агентов, специализирующихся на оптовой торговле отдельными видами товаров или группами товаров, не включенными в другие группировки",
            Category.SUBCLASS,
        ),
        Classification(
            "46.19", "Деятельность агентов по оптовой торговле товарами широкого ассортимента", Category.CLASS
        ),
        Classification(
            "46.19.0", "Деятельность агентов по оптовой торговле товарами широкого ассортимента", Category.SUBCLASS
        ),
        Classification("46.2", "Оптовая торговля сельскохозяйственным сырьем и живыми животными", Category.GROUP),
        Classification(
            "46.21", "Оптовая торговля зерном, необработанным табаком, семенами и кормами для животных", Category.CLASS
        ),
        Classification("46.21.1", "Оптовая торговля зерном, семенами и кормами для животных", Category.SUBCLASS),
        Classification("46.21.9", "Оптовая торговля необработанным табаком", Category.SUBCLASS),
        Classification("46.22", "Оптовая торговля цветами и другими растениями", Category.CLASS),
        Classification("46.22.0", "Оптовая торговля цветами и другими растениями", Category.SUBCLASS),
        Classification("46.23", "Оптовая торговля живыми животными", Category.CLASS),
        Classification("46.23.0", "Оптовая торговля живыми животными", Category.SUBCLASS),
        Classification("46.24", "Оптовая торговля шкурами и кожей", Category.CLASS),
        Classification("46.24.0", "Оптовая торговля шкурами и кожей", Category.SUBCLASS),
        Classification(
            "46.3", "Оптовая торговля пищевыми продуктами, включая напитки, и табачными изделиями", Category.GROUP
        ),
        Classification("46.31", "Оптовая торговля фруктами и овощами", Category.CLASS),
        Classification("46.31.0", "Оптовая торговля фруктами и овощами", Category.SUBCLASS),
        Classification("46.32", "Оптовая торговля мясом и мясными продуктами", Category.CLASS),
        Classification("46.32.0", "Оптовая торговля мясом и мясными продуктами", Category.SUBCLASS),
        Classification(
            "46.33", "Оптовая торговля молочными продуктами, яйцами, пищевыми маслами и жирами", Category.CLASS
        ),
        Classification(
            "46.33.0", "Оптовая торговля молочными продуктами, яйцами, пищевыми маслами и жирами", Category.SUBCLASS
        ),
        Classification("46.34", "Оптовая торговля алкогольными и другими напитками", Category.CLASS),
        Classification("46.34.0", "Оптовая торговля алкогольными и другими напитками", Category.SUBCLASS),
        Classification("46.35", "Оптовая торговля табачными изделиями", Category.CLASS),
        Classification("46.35.0", "Оптовая торговля табачными изделиями", Category.SUBCLASS),
        Classification(
            "46.36", "Оптовая торговля сахаром, шоколадом и кондитерскими изделиями из сахара", Category.CLASS
        ),
        Classification(
            "46.36.0", "Оптовая торговля сахаром, шоколадом и кондитерскими изделиями из сахара", Category.SUBCLASS
        ),
        Classification("46.37", "Оптовая торговля кофе, чаем, какао и пряностями", Category.CLASS),
        Classification("46.37.0", "Оптовая торговля кофе, чаем, какао и пряностями", Category.SUBCLASS),
        Classification(
            "46.38",
            "Оптовая торговля прочими пищевыми продуктами, в том числе рыбой, ракообразными и моллюсками",
            Category.CLASS,
        ),
        Classification("46.38.1", "Оптовая торговля мукой.", Category.SUBCLASS),
        Classification(
            "46.38.2",
            "Оптовая торговля кормами для собак, кошек и других домашних животных (домашних питомцев)",
            Category.SUBCLASS,
        ),
        Classification(
            "46.38.9",
            "Оптовая торговля прочими пищевыми продуктами, в том числе рыбой, ракообразными и моллюсками",
            Category.SUBCLASS,
        ),
        Classification(
            "46.39",
            "Неспециализированная оптовая торговля пищевыми продуктами, включая напитки, и табачными изделиями",
            Category.CLASS,
        ),
        Classification(
            "46.39.0",
            "Неспециализированная оптовая торговля пищевыми продуктами, включая напитки, и табачными изделиями",
            Category.SUBCLASS,
        ),
        Classification(
            "46.4", "Оптовая торговля непродовольственными товарами потребительского назначения", Category.GROUP
        ),
        Classification("46.41", "Оптовая торговля текстильными товарами", Category.CLASS),
        Classification("46.41.0", "Оптовая торговля текстильными товарами", Category.SUBCLASS),
        Classification("46.42", "Оптовая торговля одеждой и обувью", Category.CLASS),
        Classification("46.42.1", "Оптовая торговля одеждой", Category.SUBCLASS),
        Classification("46.42.9", "Оптовая торговля обувью", Category.SUBCLASS),
        Classification("46.43", "Оптовая торговля бытовыми электротоварами, радио- и телеаппаратурой", Category.CLASS),
        Classification("46.43.1", "Оптовая торговля бытовой радио- и телеаппаратурой", Category.SUBCLASS),
        Classification(
            "46.43.2",
            "Оптовая торговля грампластинками, магнитными лентами, компакт-дисками, видеокассетами, DVD-дисками записанными",
            Category.SUBCLASS,
        ),
        Classification(
            "46.43.9",
            "Оптовая торговля прочими бытовыми электротоварами, кроме осветительного оборудования",
            Category.SUBCLASS,
        ),
        Classification(
            "46.44", "Оптовая торговля изделиями из фарфора и стекла, обоями и чистящими средствами", Category.CLASS
        ),
        Classification(
            "46.44.0",
            "Оптовая торговля изделиями из фарфора и стекла, обоями и чистящими средствами",
            Category.SUBCLASS,
        ),
        Classification(
            "46.45", "Оптовая торговля парфюмерными и косметическими товарами (включая мыло)", Category.CLASS
        ),
        Classification(
            "46.45.0", "Оптовая торговля парфюмерными и косметическими товарами (включая мыло)", Category.SUBCLASS
        ),
        Classification("46.46", "Оптовая торговля фармацевтическими товарами", Category.CLASS),
        Classification("46.46.0", "Оптовая торговля фармацевтическими товарами", Category.SUBCLASS),
        Classification("46.47", "Оптовая торговля бытовой мебелью, коврами и осветительными приборами", Category.CLASS),
        Classification("46.47.1", "Оптовая торговля бытовой мебелью и коврами", Category.SUBCLASS),
        Classification("46.47.9", "Оптовая торговля осветительными приборами", Category.SUBCLASS),
        Classification("46.48", "Оптовая торговля часами и ювелирными изделиями", Category.CLASS),
        Classification("46.48.0", "Оптовая торговля часами и ювелирными изделиями", Category.SUBCLASS),
        Classification(
            "46.49",
            "Оптовая торговля прочими непродовольственными товарами потребительского назначения",
            Category.CLASS,
        ),
        Classification(
            "46.49.0",
            "Оптовая торговля прочими непродовольственными товарами потребительского назначения",
            Category.SUBCLASS,
        ),
        Classification("46.5", "Оптовая торговля компьютерами и телекоммуникационным оборудованием", Category.GROUP),
        Classification(
            "46.51",
            "Оптовая торговля компьютерами (ЭВМ), периферийными устройствами и программным обеспечением",
            Category.CLASS,
        ),
        Classification(
            "46.51.0",
            "Оптовая торговля компьютерами (ЭВМ), переферийными устройствами и программным обеспечением",
            Category.SUBCLASS,
        ),
        Classification(
            "46.52",
            "Оптовая торговля компонентами электронного оборудования и телекоммуникационного оборудования",
            Category.CLASS,
        ),
        Classification(
            "46.52.1",
            "Оптовая торговля компонентами электронного оборудования и телекоммуникационного оборудования",
            Category.SUBCLASS,
        ),
        Classification(
            "46.52.9",
            "Оптовая торговля грампластинками, магнитными лентами, компакт-дисками, видеокассетами, DVD-дисками чистыми",
            Category.SUBCLASS,
        ),
        Classification("46.6", "Оптовая торговля машинами и оборудованием", Category.GROUP),
        Classification("46.61", "Оптовая торговля сельскохозяйственными машинами", Category.CLASS),
        Classification("46.61.0", "Оптовая торговля сельскохозяйственными машинами", Category.SUBCLASS),
        Classification("46.62", "Оптовая торговля станками", Category.CLASS),
        Classification("46.62.0", "Оптовая торговля станками", Category.SUBCLASS),
        Classification(
            "46.63",
            "Оптовая торговля машинами и оборудованием для горнодобывающей промышленности, строительства, в том числе гражданского строительства",
            Category.CLASS,
        ),
        Classification(
            "46.63.0",
            "Оптовая торговля машинами и оборудованием для горнодобывающей промышленности, строительства, в том числе гражданского строительства",
            Category.SUBCLASS,
        ),
        Classification(
            "46.64",
            "Оптовая торговля машинами для текстильной промышленности, швейными и вязальными машинами",
            Category.CLASS,
        ),
        Classification(
            "46.64.0",
            "Оптовая торговля машинами для текстильной промышленности, швейными и вязальными машинами",
            Category.SUBCLASS,
        ),
        Classification("46.65", "Оптовая торговля офисной мебелью", Category.CLASS),
        Classification("46.65.0", "Оптовая торговля офисной мебелью", Category.SUBCLASS),
        Classification("46.66", "Оптовая торговля офисными машинами и оборудованием", Category.CLASS),
        Classification("46.66.0", "Оптовая торговля офисными машинами и оборудованием", Category.SUBCLASS),
        Classification("46.69", "Оптовая торговля прочими машинами и оборудованием", Category.CLASS),
        Classification("46.69.0", "Оптовая торговля прочими машинами и оборудованием", Category.SUBCLASS),
        Classification("46.7", "Оптовая торговля прочими товарами", Category.GROUP),
        Classification("46.71", "Оптовая торговля топливом", Category.CLASS),
        Classification("46.71.1", "Оптовая торговля сырой нефтью и попутным газом", Category.SUBCLASS),
        Classification("46.71.2", "Оптовая торговля природным (горючим) газом", Category.SUBCLASS),
        Classification("46.71.3", "Оптовая торговля каменным углем и лигнитом (бурым углем)", Category.SUBCLASS),
        Classification("46.71.4", "Оптовая торговля авиационным и автомобильным топливом", Category.SUBCLASS),
        Classification(
            "46.71.9",
            "Оптовая торговля прочим топливом, смазочными материалами, техническими маслами и т.п.",
            Category.SUBCLASS,
        ),
        Classification("46.72", "Оптовая торговля металлами и металлическими рудами", Category.CLASS),
        Classification("46.72.1", "Оптовая торговля рудами черных и цветных металлов", Category.SUBCLASS),
        Classification("46.72.2", "Оптовая торговля чугуном, сталью и отливками из них", Category.SUBCLASS),
        Classification("46.72.3", "Оптовая торговля цветными металлами и отливками из них", Category.SUBCLASS),
        Classification("46.72.4", "Оптовая торговля драгоценными металлами", Category.SUBCLASS),
        Classification("46.72.9", "Оптовая торговля прочими металлами и отливками из них", Category.SUBCLASS),
        Classification(
            "46.73",
            "Оптовая торговля лесоматериалами, строительными материалами и санитарно-техническим оборудованием",
            Category.CLASS,
        ),
        Classification("46.73.1", "Оптовая торговля лесоматериалами", Category.SUBCLASS),
        Classification("46.73.2", "Оптовая торговля обоями и напольными покрытиями", Category.SUBCLASS),
        Classification(
            "46.73.9",
            "Оптовая торговля прочими строительными материалами и санитарно-техническим оборудованием",
            Category.SUBCLASS,
        ),
        Classification(
            "46.74", "Оптовая торговля скобяными изделиями, водопроводным и отопительным оборудованием", Category.CLASS
        ),
        Classification(
            "46.74.0",
            "Оптовая торговля скобяными изделиями, водопроводным и отопительным оборудованием",
            Category.SUBCLASS,
        ),
        Classification("46.75", "Оптовая торговля химическими продуктами", Category.CLASS),
        Classification("46.75.0", "Оптовая торговля химическими продуктами", Category.SUBCLASS),
        Classification("46.76", "Оптовая торговля прочими промежуточными продуктами", Category.CLASS),
        Classification("46.76.0", "Оптовая торговля прочими промежуточными продуктами", Category.SUBCLASS),
        Classification("46.77", "Оптовая торговля отходами и ломом", Category.CLASS),
        Classification("46.77.1", "Оптовая торговля отходами и ломом черных и цветных металлов", Category.SUBCLASS),
        Classification(
            "46.77.2", "Оптовая торговля отходами и ломом драгоценных металлов и драгоценных камней", Category.SUBCLASS
        ),
        Classification(
            "46.77.9", "Оптовая торговля прочими неметаллическими отходами и неметаллическим ломом", Category.SUBCLASS
        ),
        Classification("46.9", "Оптовая неспециализированная торговля", Category.GROUP),
        Classification("46.90", "Оптовая неспециализированная торговля", Category.CLASS),
        Classification("46.90.0", "Оптовая неспециализированная торговля", Category.SUBCLASS),
        Classification("47", "Розничная торговля, кроме торговли автомобилями и мотоциклами", Category.DIVISION),
        Classification("47.1", "Розничная торговля в неспециализированных магазинах", Category.GROUP),
        Classification(
            "47.11",
            "Розничная торговля в неспециализированных магазинах преимущественно пищевыми продуктами, включая напитки, и табачными изделиями",
            Category.CLASS,
        ),
        Classification(
            "47.11.0",
            "Розничная торговля в неспециализированных магазинах преимущественно пищевыми продуктами, включая напитки, и табачными изделиями",
            Category.SUBCLASS,
        ),
        Classification("47.19", "Розничная торговля в неспециализированных магазинах прочими товарами", Category.CLASS),
        Classification(
            "47.19.0", "Розничная торговля в неспециализированных магазинах прочими товарами", Category.SUBCLASS
        ),
        Classification(
            "47.2",
            "Розничная торговля в специализированных магазинах пищевыми продуктами, включая напитки, и табачными изделиями",
            Category.GROUP,
        ),
        Classification("47.21", "Розничная торговля в специализированных магазинах фруктами и овощами", Category.CLASS),
        Classification(
            "47.21.0", "Розничная торговля в специализированных магазинах фруктами и овощами", Category.SUBCLASS
        ),
        Classification(
            "47.22", "Розничная торговля в специализированных магазинах мясом и мясными продуктами", Category.CLASS
        ),
        Classification(
            "47.22.1",
            "Розничная торговля в специализированных магазинах домашней птицей, дичью и изделиями из них",
            Category.SUBCLASS,
        ),
        Classification(
            "47.22.9", "Розничная торговля в специализированных магазинах мясом и мясными продуктами", Category.SUBCLASS
        ),
        Classification(
            "47.23",
            "Розничная торговля в специализированных магазинах рыбой, ракообразными и моллюсками",
            Category.CLASS,
        ),
        Classification(
            "47.23.0",
            "Розничная торговля в специализированных магазинах рыбой, ракообразными и моллюсками",
            Category.SUBCLASS,
        ),
        Classification(
            "47.24",
            "Розничная торговля в специализированных магазинах хлебобулочными изделиями, мучными и кондитерскими изделиями из сахара",
            Category.CLASS,
        ),
        Classification(
            "47.24.0",
            "Розничная торговля в специализированных магазинах хлебобулочными изделиями, мучными и кондитерскими изделиями из сахара",
            Category.SUBCLASS,
        ),
        Classification(
            "47.25",
            "Розничная торговля в специализированных магазинах алкогольными и другими напитками",
            Category.CLASS,
        ),
        Classification(
            "47.25.0",
            "Розничная торговля в специализированных магазинах алкогольными и другими напитками",
            Category.SUBCLASS,
        ),
        Classification(
            "47.26", "Розничная торговля в специализированных магазинах табачными изделиями", Category.CLASS
        ),
        Classification(
            "47.26.0", "Розничная торговля в специализированных магазинах табачными изделиями", Category.SUBCLASS
        ),
        Classification(
            "47.29", "Розничная торговля в специализированных магазинах прочими пищевыми продуктами", Category.CLASS
        ),
        Classification(
            "47.29.0",
            "Розничная торговля в специализированных магазинах прочими пищевыми продуктами",
            Category.SUBCLASS,
        ),
        Classification("47.3", "Розничная торговля в специализированных магазинах моторным топливом", Category.GROUP),
        Classification("47.30", "Розничная торговля в специализированных магазинах моторным топливом", Category.CLASS),
        Classification(
            "47.30.0", "Розничная торговля в специализированных магазинах моторным топливом", Category.SUBCLASS
        ),
        Classification(
            "47.4",
            "Розничная торговля в специализированных магазинах информационным и телекоммуникационным оборудованием",
            Category.GROUP,
        ),
        Classification(
            "47.41",
            "Розничная торговля в специализированных магазинах компьютерами и программным обеспечением",
            Category.CLASS,
        ),
        Classification(
            "47.41.0",
            "Розничная торговля в специализированных магазинах компьютерами и программным обеспечением",
            Category.SUBCLASS,
        ),
        Classification(
            "47.42",
            "Розничная торговля в специализированных магазинах телекоммуникационным оборудованием",
            Category.CLASS,
        ),
        Classification(
            "47.42.0",
            "Розничная торговля в специализированных магазинах телекоммуникационным оборудованием",
            Category.SUBCLASS,
        ),
        Classification(
            "47.43", "Розничная торговля в специализированных магазинах аудио- и видеоаппаратурой", Category.CLASS
        ),
        Classification(
            "47.43.0", "Розничная торговля в специализированных магазинах аудио- и видеоаппаратурой", Category.SUBCLASS
        ),
        Classification(
            "47.5", "Розничная торговля в специализированных магазинах прочим оборудованием для дома", Category.GROUP
        ),
        Classification(
            "47.51", "Розничная торговля в специализированных магазинах текстильными изделиями", Category.CLASS
        ),
        Classification(
            "47.51.0", "Розничная торговля в специализированных магазинах текстильными изделиями", Category.SUBCLASS
        ),
        Classification(
            "47.52",
            "Розничная торговля в специализированных магазинах скобяными изделиями, лакокрасочными материалами и стеклом",
            Category.CLASS,
        ),
        Classification(
            "47.52.0",
            "Розничная торговля в специализированных магазинах скобяными изделиями, лакокрасочными материалами и стеклом",
            Category.SUBCLASS,
        ),
        Classification(
            "47.53",
            "Розничная торговля в специализированных магазинах коврами, настенными напольными покрытиями",
            Category.CLASS,
        ),
        Classification(
            "47.53.1",
            "Розничная торговля в специализированных магазинах коврами и ковровыми изделиями",
            Category.SUBCLASS,
        ),
        Classification(
            "47.53.9",
            "Розничная торговля в специализированных магазинах прочими настенными и напольными покрытиями",
            Category.SUBCLASS,
        ),
        Classification(
            "47.54", "Розничная торговля в специализированных магазинах бытовыми электротоварами", Category.CLASS
        ),
        Classification(
            "47.54.0", "Розничная торговля в специализированных магазинах бытовыми электротоварами", Category.SUBCLASS
        ),
        Classification(
            "47.59",
            "Розничная торговля в специализированных магазинах мебелью, осветительными приборами и прочими бытовыми товарами",
            Category.CLASS,
        ),
        Classification("47.59.1", "Розничная торговля в специализированных магазинах мебелью", Category.SUBCLASS),
        Classification(
            "47.59.9",
            "Розничная торговля в специализированных магазинах осветительными приборами и прочими бытовыми товарами",
            Category.SUBCLASS,
        ),
        Classification(
            "47.6",
            "Розничная торговля в специализированных магазинах товарами для культурных развлечений, спорта и отдыха",
            Category.GROUP,
        ),
        Classification("47.61", "Розничная торговля в специализированных магазинах книгами", Category.CLASS),
        Classification("47.61.0", "Розничная торговля в специализированных магазинах книгами", Category.SUBCLASS),
        Classification(
            "47.62",
            "Розничная торговля в специализированных магазинах журналами и канцелярскими товарами",
            Category.CLASS,
        ),
        Classification(
            "47.62.0",
            "Розничная торговля в специализированных магазинах журналами и канцелярскими товарами",
            Category.SUBCLASS,
        ),
        Classification(
            "47.63", "Розничная торговля в специализированных магазинах видео и музыкальными записями", Category.CLASS
        ),
        Classification(
            "47.63.0",
            "Розничная торговля в специализированных магазинах видео и музыкальными записями",
            Category.SUBCLASS,
        ),
        Classification(
            "47.64", "Розничная торговля в специализированных магазинах спортивными товарами", Category.CLASS
        ),
        Classification(
            "47.64.0", "Розничная торговля в специализированных магазинах спортивными товарами", Category.SUBCLASS
        ),
        Classification("47.65", "Розничная торговля в специализированных магазинах играми и игрушками", Category.CLASS),
        Classification(
            "47.65.0", "Розничная торговля в специализированных магазинах играми и игрушками", Category.SUBCLASS
        ),
        Classification("47.7", "Розничная торговля в специализированных магазинах прочими товарами", Category.GROUP),
        Classification("47.71", "Розничная торговля в специализированных магазинах одеждой", Category.CLASS),
        Classification(
            "47.71.1",
            "Розничная торговля в специализированных магазинах трикотажными и чулочно-носочными изделиями",
            Category.SUBCLASS,
        ),
        Classification(
            "47.71.9",
            "Розничная торговля в специализированных магазинах одеждой (кроме трикотажных и чулочно-носочных изделий)",
            Category.SUBCLASS,
        ),
        Classification(
            "47.72", "Розничная торговля в специализированных магазинах обувью и кожаными изделиями", Category.CLASS
        ),
        Classification("47.72.1", "Розничная торговля в специализированных магазинах обувью", Category.SUBCLASS),
        Classification(
            "47.72.9", "Розничная торговля в специализированных магазинах кожаными изделиями", Category.SUBCLASS
        ),
        Classification(
            "47.73", "Розничная торговля в специализированных магазинах фармацевтическими товарами", Category.CLASS
        ),
        Classification(
            "47.73.0", "Розничная торговля в специализированных магазинах фармацевтическими товарами", Category.SUBCLASS
        ),
        Classification(
            "47.74",
            "Розничная торговля в специализированных магазинах медицинскими и ортопедическими товарами",
            Category.CLASS,
        ),
        Classification(
            "47.74.0",
            "Розничная торговля в специализированных магазинах медицинскими и ортопедическими товарами",
            Category.SUBCLASS,
        ),
        Classification(
            "47.75",
            "Розничная торговля в специализированных магазинах косметическими и парфюмерными товарами",
            Category.CLASS,
        ),
        Classification(
            "47.75.0",
            "Розничная торговля в специализированных магазинах косметическими и парфюмерными товарами",
            Category.SUBCLASS,
        ),
        Classification(
            "47.76",
            "Розничная торговля в специализированных магазинах цветами и другими растениями, семенами, удобрениями, домашними животными (питомцами), кормом, средствами ухода и ветеринарными препаратами для них",
            Category.CLASS,
        ),
        Classification(
            "47.76.0",
            "Розничная торговля в специализированных магазинах цветами и другими растениями, семенами, удобрениями, домашними животными (питомцами), кормом, средствами ухода и ветеринарными препаратами для них",
            Category.SUBCLASS,
        ),
        Classification(
            "47.77", "Розничная торговля в специализированных магазинах часами и ювелирными изделиями", Category.CLASS
        ),
        Classification(
            "47.77.0",
            "Розничная торговля в специализированных магазинах часами и ювелирными изделиями",
            Category.SUBCLASS,
        ),
        Classification(
            "47.78", "Розничная торговля в специализированных магазинах прочими новыми товарами", Category.CLASS
        ),
        Classification(
            "47.78.0", "Розничная торговля в специализированных магазинах прочими новыми товарами", Category.SUBCLASS
        ),
        Classification("47.79", "Розничная торговля в магазинах товарами, бывшими в употреблении", Category.CLASS),
        Classification("47.79.0", "Розничная торговля в магазинах товарами, бывшими в употреблении", Category.SUBCLASS),
        Classification("47.8", "Розничная торговля вне магазинов", Category.GROUP),
        Classification("47.81", "Розничная торговля в палатках и на рынках пищевыми продуктами", Category.CLASS),
        Classification("47.81.0", "Розничная торговля в палатках и на рынках пищевыми продуктами", Category.SUBCLASS),
        Classification("47.82", "Розничная торговля в палатках и на рынках текстилем, одеждой, обувью", Category.CLASS),
        Classification(
            "47.82.0", "Розничная торговля в палатках и на рынках текстилем, одеждой, обувью", Category.SUBCLASS
        ),
        Classification("47.89", "Розничная торговля в палатках и на рынках прочими товарами", Category.CLASS),
        Classification("47.89.0", "Розничная торговля в палатках и на рынках прочими товарами", Category.SUBCLASS),
        Classification("47.9", "Розничная торговля вне магазинов, палаток и рынков", Category.GROUP),
        Classification("47.91", "Розничная дистанционная торговля (по почте и через Интернет)", Category.CLASS),
        Classification("47.91.0", "Розничная дистанционная торговля (по почте и через Интернет)", Category.SUBCLASS),
        Classification("47.99", "Прочая розничная торговля вне магазинов, палаток и рынков", Category.CLASS),
        Classification("47.99.0", "Прочая розничная торговля вне магазинов, палаток и рынков", Category.SUBCLASS),
        Classification("H", "ТРАНСПОРТНАЯ ДЕЯТЕЛЬНОСТЬ И ХРАНЕНИЯ ГРУЗОВ", Category.SECTION),
        Classification("49", "Деятельность наземного и трубопроводного транспорта", Category.DIVISION),
        Classification("49.1", "Деятельность пассажирского железнодорожного транспорта", Category.GROUP),
        Classification("49.10", "Деятельность пассажирского железнодорожного транспорта", Category.CLASS),
        Classification("49.10.0", "Деятельность пассажирского железнодорожного транспорта", Category.SUBCLASS),
        Classification("49.2", "Деятельность грузового железнодорожного транспорта", Category.GROUP),
        Classification("49.20", "Деятельность грузового железнодорожного транспорта", Category.CLASS),
        Classification("49.20.0", "Деятельность грузового железнодорожного транспорта", Category.SUBCLASS),
        Classification("49.3", "Деятельность прочего наземного транспорта", Category.GROUP),
        Classification(
            "49.31",
            "Деятельность наземного транспорта по городским и пригородным пассажирским перевозкам",
            Category.CLASS,
        ),
        Classification(
            "49.31.0",
            "Деятельность наземного транспорта по городским и пригородным пассажирским перевозкам",
            Category.SUBCLASS,
        ),
        Classification("49.32", "Деятельность такси по перевозке пассажиров", Category.CLASS),
        Classification("49.32.0", "Деятельность такси по перевозке пассажиров", Category.SUBCLASS),
        Classification(
            "49.39",
            "Деятельность прочего пассажирского наземного транспорта, не включенного в другие группировки",
            Category.CLASS,
        ),
        Classification(
            "49.39.0",
            "Деятельность прочего пассажирского наземного транспорта, не включенного в другие группировки",
            Category.SUBCLASS,
        ),
        Classification(
            "49.4",
            "Деятельность грузового автомобильного транспорта и предоставление услуг по переезду",
            Category.GROUP,
        ),
        Classification("49.41", "Деятельность грузового автомобильного транспорта", Category.CLASS),
        Classification("49.41.0", "Деятельность грузового автомобильного транспорта", Category.SUBCLASS),
        Classification("49.42", "Предоставление услуг по переезду (перемещению)", Category.CLASS),
        Classification("49.42.0", "Предоставление услуг по переезду (перемещению)", Category.SUBCLASS),
        Classification("49.5", "Деятельность трубопроводного транспорта", Category.GROUP),
        Classification("49.50", "Деятельность трубопроводного транспорта", Category.CLASS),
        Classification("49.50.0", "Деятельность трубопроводного транспорта", Category.SUBCLASS),
        Classification("50", "Деятельность водного транспорта", Category.DIVISION),
        Classification("50.1", "Деятельность пассажирского морского транспорта", Category.GROUP),
        Classification("50.10", "Деятельность пассажирского морского транспорта", Category.CLASS),
        Classification("50.10.0", "Деятельность пассажирского морского транспорта", Category.SUBCLASS),
        Classification("50.2", "Деятельность грузового морского транспорта", Category.GROUP),
        Classification("50.20", "Деятельность грузового морского транспорта", Category.CLASS),
        Classification("50.20.0", "Деятельность грузового морского транспорта", Category.SUBCLASS),
        Classification("50.3", "Деятельность пассажирского речного транспорта", Category.GROUP),
        Classification("50.30", "Деятельность пассажирского речного транспорта", Category.CLASS),
        Classification("50.30.0", "Деятельность пассажирского речного транспорта", Category.SUBCLASS),
        Classification("50.4", "Деятельность грузового речного транспорта", Category.GROUP),
        Classification("50.40", "Деятельность грузового речного транспорта", Category.CLASS),
        Classification("50.40.0", "Деятельность грузового речного транспорта", Category.SUBCLASS),
        Classification("51", "Деятельность воздушного транспорта", Category.DIVISION),
        Classification("51.1", "Деятельность пассажирского воздушного транспорта", Category.GROUP),
        Classification("51.10", "Деятельность пассажирского воздушного транспорта", Category.CLASS),
        Classification("51.10.0", "Деятельность пассажирского воздушного транспорта", Category.SUBCLASS),
        Classification("51.2", "Деятельность грузового воздушного транспорта", Category.GROUP),
        Classification("51.21", "Деятельность грузового воздушного транспорта", Category.CLASS),
        Classification("51.21.0", "Деятельность грузового воздушного транспорта", Category.SUBCLASS),
        Classification("51.22", "Деятельность космического транспорта", Category.CLASS),
        Classification("51.22.0", "Деятельность космического транспорта", Category.SUBCLASS),
        Classification("52", "Складирование грузов и вспомогательная транспортная деятельность", Category.DIVISION),
        Classification("52.1", "Складирование и хранение грузов", Category.GROUP),
        Classification("52.10", "Складирование и хранение грузов", Category.CLASS),
        Classification("52.10.0", "Складирование и хранение грузов", Category.SUBCLASS),
        Classification("52.2", "Прочая вспомогательная транспортная деятельность", Category.GROUP),
        Classification("52.21", "Прочая вспомогательная деятельность наземного транспорта", Category.CLASS),
        Classification(
            "52.21.1", "Продажа билетов, предварительный заказ билетов, камеры хранения багажа", Category.SUBCLASS
        ),
        Classification("52.21.9", "Прочая вспомогательная деятельность наземного транспорта", Category.SUBCLASS),
        Classification("52.22", "Прочая вспомогательная деятельность водного транспорта", Category.CLASS),
        Classification("52.22.0", "Прочая вспомогательная деятельность водного транспорта", Category.SUBCLASS),
        Classification("52.23", "Прочая вспомогательная деятельность воздушного транспорта", Category.CLASS),
        Classification("52.23.0", "Прочая вспомогательная деятельность воздушного транспорта", Category.SUBCLASS),
        Classification("52.24", "Транспортная обработка грузов", Category.CLASS),
        Classification("52.24.0", "Транспортная обработка грузов", Category.SUBCLASS),
        Classification("52.29", "Прочая вспомогательная транспортная деятельность", Category.CLASS),
        Classification("52.29.0", "Прочая вспомогательная транспортная деятельность", Category.SUBCLASS),
        Classification("53", "Почтовая и курьерская деятельность", Category.DIVISION),
        Classification(
            "53.1", "Почтовая деятельность, осуществляемая под руководством национальных операторов", Category.GROUP
        ),
        Classification(
            "53.10", "Почтовая деятельность, осуществляемая под руководством национальных операторов", Category.CLASS
        ),
        Classification("53.10.1", "Предоставление универсальных почтовых услуг", Category.SUBCLASS),
        Classification("53.10.2", "Предоставление прочих почтовых услуг", Category.SUBCLASS),
        Classification("53.2", "Прочая почтовая и курьерская деятельность", Category.GROUP),
        Classification("53.20", "Прочая почтовая и курьерская деятельность", Category.CLASS),
        Classification("53.20.0", "Прочая почтовая и курьерская деятельность", Category.SUBCLASS),
        Classification("I", "ДЕЯТЕЛЬНОСТЬ ГОСТИНИЦ И РЕСТОРАНОВ", Category.SECTION),
        Classification("55", "Деятельность гостиниц", Category.DIVISION),
        Classification("55.1", "Предоставление услуг гостиницами", Category.GROUP),
        Classification("55.10", "Предоставление услуг гостиницами", Category.CLASS),
        Classification("55.10.0", "Предоставление услуг гостиницами", Category.SUBCLASS),
        Classification("55.2", "Предоставление услуг для туристического проживания", Category.GROUP),
        Classification("55.20", "Предоставление услуг для туристического проживания", Category.CLASS),
        Classification("55.20.0", "Предоставление услуг для туристического проживания", Category.SUBCLASS),
        Classification(
            "55.3",
            "Предоставление услуг кемпингами, в том числе стоянками для автофургонов и автоприцепов",
            Category.GROUP,
        ),
        Classification(
            "55.30",
            "Предоставление услуг кемпингами, в том числе стоянками для автофургонов и автоприцепов",
            Category.CLASS,
        ),
        Classification(
            "55.30.0",
            "Предоставление услуг кемпингами, в том числе стоянками для автофургонов и автоприцепов",
            Category.SUBCLASS,
        ),
        Classification("55.9", "Предоставление услуг прочими местами для проживания", Category.GROUP),
        Classification("55.90", "Предоставление услуг прочими местами для проживания", Category.CLASS),
        Classification("55.90.0", "Предоставление услуг прочими местами для проживания", Category.SUBCLASS),
        Classification("56", "Деятельность ресторанов", Category.DIVISION),
        Classification(
            "56.1", "Деятельность ресторанов и предоставление мобильных услуг по обеспечению пищей", Category.GROUP
        ),
        Classification(
            "56.10", "Деятельность ресторанов и предоставление мобильных услуг по обеспечению пищей", Category.CLASS
        ),
        Classification(
            "56.10.0",
            "Деятельность ресторанов и предоставление мобильных услуг по обеспечению пищей",
            Category.SUBCLASS,
        ),
        Classification("56.2", "Предоставление разовых и прочих услуг по обеспечению пищей", Category.GROUP),
        Classification("56.21", "Предоставление разовых и прочих услуг по обеспечению пищей", Category.CLASS),
        Classification("56.21.0", "Предоставление разовых и прочих услуг по обеспечению пищей", Category.SUBCLASS),
        Classification("56.29", "Предоставление прочих услуг ресторанами", Category.CLASS),
        Classification("56.29.0", "Предоставление прочих услуг ресторанами", Category.SUBCLASS),
        Classification("56.3", "Предоставление услуг барами", Category.GROUP),
        Classification("56.30", "Предоставление услуг барами", Category.CLASS),
        Classification("56.30.0", "Предоставление услуг барами", Category.SUBCLASS),
        Classification("J", "ИНФОРМАЦИЯ И СВЯЗЬ", Category.SECTION),
        Classification("JA", "ИЗДАТЕЛЬСКАЯ ДЕЯТЕЛЬНОСТЬ; ВИДЕО- И ЗВУКОЗАПИСЬ; ТЕЛЕ- И РАДИОВЕЩАНИЕ", Category.SECTION),
        Classification("58", "Издательская деятельность", Category.DIVISION),
        Classification(
            "58.1", "Издание книг, периодических публикаций и прочая издательская деятельность", Category.GROUP
        ),
        Classification("58.11", "Издание книг", Category.CLASS),
        Classification("58.11.0", "Издание книг", Category.SUBCLASS),
        Classification("58.12", "Издание справочников и списков адресов", Category.CLASS),
        Classification("58.12.0", "Издание справочников и списков адресов", Category.SUBCLASS),
        Classification("58.13", "Издание газет", Category.CLASS),
        Classification("58.13.0", "Издание газет", Category.SUBCLASS),
        Classification("58.14", "Издание журналов и периодических публикаций", Category.CLASS),
        Classification("58.14.0", "Издание журналов и периодических публикаций", Category.SUBCLASS),
        Classification("58.19", "Прочая издательская деятельность", Category.CLASS),
        Classification("58.19.0", "Прочая издательская деятельность", Category.SUBCLASS),
        Classification("58.2", "Издание программного обеспечения (софта)", Category.GROUP),
        Classification("58.21", "Издание компьютерных игр", Category.CLASS),
        Classification("58.21.0", "Издание компьютерных игр", Category.SUBCLASS),
        Classification("58.29", "Издание прочего программного обеспечения", Category.CLASS),
        Classification("58.29.0", "Издание прочего программного обеспечения", Category.SUBCLASS),
        Classification(
            "59",
            "Производство кинофильмов, видео и телевизионных программ, звукозапись и издание музыки",
            Category.DIVISION,
        ),
        Classification("59.1", "Производство кинофильмов, видео и телевизионных программ", Category.GROUP),
        Classification("59.11", "Производство кинофильмов, видео и телевизионных программ", Category.CLASS),
        Classification("59.11.0", "Производство кинофильмов, видео и телевизионных программ", Category.SUBCLASS),
        Classification("59.12", "Компоновка кинофильмов, видео и телевизионных программ", Category.CLASS),
        Classification("59.12.0", "Компоновка кинофильмов, видео и телевизионных программ", Category.SUBCLASS),
        Classification("59.13", "Распространение кинофильмов, видео и телевизионных программ", Category.CLASS),
        Classification("59.13.0", "Распространение кинофильмов, видео и телевизионных программ", Category.SUBCLASS),
        Classification("59.14", "Показ кинофильмов", Category.CLASS),
        Classification("59.14.0", "Показ кинофильмов", Category.SUBCLASS),
        Classification("59.2", "Звукозапись и издание музыки", Category.GROUP),
        Classification("59.20", "Звукозапись и издание музыки", Category.CLASS),
        Classification("59.20.0", "Звукозапись и издание музыки", Category.SUBCLASS),
        Classification("60", "Радиовещание и телевидение", Category.DIVISION),
        Classification("60.1", "Радиовещание", Category.GROUP),
        Classification("60.10", "Радиовещание", Category.CLASS),
        Classification("60.10.0", "Радиовещание", Category.SUBCLASS),
        Classification("60.2", "Телевидение", Category.GROUP),
        Classification("60.20", "Телевидение", Category.CLASS),
        Classification("60.20.0", "Телевидение", Category.SUBCLASS),
        Classification("JB", "СВЯЗЬ", Category.SECTION),
        Classification("61", "Связь", Category.DIVISION),
        Classification("61.1", "Предоставление услуг проводной связи", Category.GROUP),
        Classification("61.10", "Предоставление услуг проводной связи", Category.CLASS),
        Classification("61.10.0", "Предоставление услуг проводной связи", Category.SUBCLASS),
        Classification("61.2", "Предоставление услуг беспроводной связи", Category.GROUP),
        Classification("61.20", "Предоставление услуг беспроводной связи", Category.CLASS),
        Classification("61.20.0", "Предоставление услуг беспроводной связи", Category.SUBCLASS),
        Classification("61.3", "Предоставление услуг спутниковой связи", Category.GROUP),
        Classification("61.30", "Предоставление услуг спутниковой связи", Category.CLASS),
        Classification("61.30.0", "Предоставление услуг спутниковой связи", Category.SUBCLASS),
        Classification("61.9", "Предоставление прочих телекоммуникационных услуг", Category.GROUP),
        Classification("61.90", "Предоставление прочих телекоммуникационных услуг", Category.CLASS),
        Classification("61.90.0", "Предоставление прочих телекоммуникационных услуг", Category.SUBCLASS),
        Classification(
            "JC", "ДЕЯТЕЛЬНОСТЬ В ОБЛАСТИ ВЫЧИСЛИТЕЛЬНОЙ ТЕХНИКИ И ИНФОРМАЦИОННОГО ОБСЛУЖИВАНИЯ", Category.SECTION
        ),
        Classification(
            "62",
            "Разработка программного обеспечения, консультирование и прочая деятельность в области вычислительной техники",
            Category.DIVISION,
        ),
        Classification(
            "62.0",
            "Разработка программного обеспечения, консультирование и прочая деятельность в области вычислительной техники",
            Category.GROUP,
        ),
        Classification("62.01", "Разработка программного обеспечения", Category.CLASS),
        Classification("62.01.0", "Разработка программного обеспечения", Category.SUBCLASS),
        Classification("62.02", "Консультирование в области вычислительной техники", Category.CLASS),
        Classification("62.02.0", "Консультирование в области вычислительной техники", Category.SUBCLASS),
        Classification("62.03", "Управление вычислительными системами", Category.CLASS),
        Classification("62.03.0", "Управление вычислительными системами", Category.SUBCLASS),
        Classification(
            "62.09", "Прочая деятельность в области информационных технологий и вычислительной техники", Category.CLASS
        ),
        Classification(
            "62.09.0",
            "Прочая деятельность в области информационных технологий и вычислительной техники",
            Category.SUBCLASS,
        ),
        Classification("63", "Деятельность в области информационного обслуживания", Category.DIVISION),
        Classification(
            "63.1",
            "Обработка данных, размещение прикладных программ и связанная с этим деятельность, использование Web-порталов",
            Category.GROUP,
        ),
        Classification(
            "63.11", "Обработка данных, размещение прикладных программ и связанная с этим деятельность", Category.CLASS
        ),
        Classification(
            "63.11.0",
            "Обработка данных, размещение прикладных программ и связанная с этим деятельность",
            Category.SUBCLASS,
        ),
        Classification("63.12", "Использование Web-порталов (Интернета)", Category.CLASS),
        Classification("63.12.0", "Использование Web-порталов (Интернета)", Category.SUBCLASS),
        Classification("63.9", "Прочая деятельность по информационному обслуживанию", Category.GROUP),
        Classification("63.91", "Деятельность информационных агентств", Category.CLASS),
        Classification("63.91.0", "Деятельность информационных агентств", Category.SUBCLASS),
        Classification(
            "63.99",
            "Прочая деятельность по информационному обслуживанию, не включенная в другие группировки",
            Category.CLASS,
        ),
        Classification(
            "63.99.0",
            "Прочая деятельность по информационному обслуживанию, не включенная в другие группировки",
            Category.SUBCLASS,
        ),
        Classification("K", "ФИНАНСОВОЕ ПОСРЕДНИЧЕСТВО И СТРАХОВАНИЕ", Category.SECTION),
        Classification(
            "64", "Финансовое посредничество, кроме услуг по страхованию и пенсионному обеспечению", Category.DIVISION
        ),
        Classification("64.1", "Денежное посредничество", Category.GROUP),
        Classification("64.11", "Деятельность центральных банков", Category.CLASS),
        Classification("64.11.0", "Деятельность центральных банков", Category.SUBCLASS),
        Classification("64.19", "Прочее денежное посредничество", Category.CLASS),
        Classification("64.19.1", "Деятельность банков", Category.SUBCLASS),
        Classification("64.19.2", "Денежное посредничество прочих финансовых учреждений", Category.SUBCLASS),
        Classification("64.19.9", "Прочее денежное посредничество", Category.SUBCLASS),
        Classification("64.2", "Деятельность холдинг-компаний", Category.GROUP),
        Classification("64.20", "Деятельность холдинг-компаний", Category.CLASS),
        Classification("64.20.0", "Деятельность холдинг-компаний", Category.SUBCLASS),
        Classification(
            "64.3",
            "Деятельность траст-компаний, инвестиционных фондов и аналогичных финансовых организаций",
            Category.GROUP,
        ),
        Classification(
            "64.30",
            "Деятельность траст-компаний, инвестиционных фондов и аналогичных финансовых организаций",
            Category.CLASS,
        ),
        Classification(
            "64.30.0",
            "Деятельность траст-компаний, инвестиционных фондов и аналогичных финансовых организаций",
            Category.SUBCLASS,
        ),
        Classification(
            "64.9", "Прочее финансовое посредничество, кроме страхования и пенсионного обеспечения", Category.GROUP
        ),
        Classification("64.91", "Финансовый лизинг", Category.CLASS),
        Classification("64.91.0", "Финансовый лизинг", Category.SUBCLASS),
        Classification("64.92", "Предоставление кредита", Category.CLASS),
        Classification("64.92.0", "Предоставление кредита", Category.SUBCLASS),
        Classification("64.99", "Прочее финансовое посредничество, не включенное в другие группировки", Category.CLASS),
        Classification(
            "64.99.0", "Прочее финансовое посредничество, не включенное в другие группировки", Category.SUBCLASS
        ),
        Classification(
            "65",
            "Страхование, перестрахование и пенсионное обеспечение, кроме обязательного социального обеспечения",
            Category.DIVISION,
        ),
        Classification("65.1", "Страхование", Category.GROUP),
        Classification("65.11", "Страхование жизни", Category.CLASS),
        Classification("65.11.0", "Страхование жизни", Category.SUBCLASS),
        Classification("65.12", "Прочие виды страхования (кроме страхования жизни)", Category.CLASS),
        Classification("65.12.0", "Прочие виды страхования (кроме страхования жизни)", Category.SUBCLASS),
        Classification("65.2", "Перестрахование", Category.GROUP),
        Classification("65.20", "Перестрахование", Category.CLASS),
        Classification("65.20.0", "Перестрахование", Category.SUBCLASS),
        Classification("65.3", "Пенсионное обеспечение", Category.GROUP),
        Classification("65.30", "Пенсионное обеспечение", Category.CLASS),
        Classification("65.30.0", "Пенсионное обеспечение", Category.SUBCLASS),
        Classification(
            "66", "Вспомогательная деятельность в сфере финансового посредничества и страхования", Category.DIVISION
        ),
        Classification(
            "66.1", "Вспомогательная деятельность в сфере финансового посредничества и страхования", Category.GROUP
        ),
        Classification("66.11", "Управление финансовыми рынками", Category.CLASS),
        Classification("66.11.0", "Управление финансовыми рынками", Category.SUBCLASS),
        Classification("66.12", "Биржевые операции с фондовыми ценностями", Category.CLASS),
        Classification("66.12.1", "Операции на финансовых рынках по поручению других лиц", Category.SUBCLASS),
        Classification("66.12.2", "Деятельность по управлению ценными бумагами", Category.SUBCLASS),
        Classification("66.12.9", "Деятельность меняльных контор, пунктов обмена валюты", Category.SUBCLASS),
        Classification(
            "66.19", "Прочая вспомогательная деятельность в сфере финансового посредничества", Category.CLASS
        ),
        Classification(
            "66.19.0", "Прочая вспомогательная деятельность в сфере финансового посредничества", Category.SUBCLASS
        ),
        Classification(
            "66.2", "Вспомогательная деятельность в сфере страхования и пенсионного обеспечения", Category.GROUP
        ),
        Classification("66.21", "Деятельность по оценке страхового риска и ущерба", Category.CLASS),
        Classification("66.21.0", "Деятельность по оценке страхового риска и ущерба", Category.SUBCLASS),
        Classification("66.22", "Деятельность страховых агентов и брокеров", Category.CLASS),
        Classification("66.22.0", "Деятельность страховых агентов и брокеров", Category.SUBCLASS),
        Classification(
            "66.29",
            "Прочие услуги, вспомогательные по отношению к страхованию и пенсионному обеспечению",
            Category.CLASS,
        ),
        Classification(
            "66.29.0",
            "Прочие услуги, вспомогательные по отношению к страхованию и пенсионному обеспечению",
            Category.SUBCLASS,
        ),
        Classification("66.3", "Управление фондами", Category.GROUP),
        Classification("66.30", "Управление фондами", Category.CLASS),
        Classification("66.30.0", "Управление фондами", Category.SUBCLASS),
        Classification("L", "ОПЕРАЦИИ С НЕДВИЖИМЫМ ИМУЩЕСТВОМ", Category.SECTION),
        Classification("68", "Операции с недвижимым имуществом", Category.DIVISION),
        Classification("68.1", "Покупка и продажа собственного недвижимого имущества", Category.GROUP),
        Classification("68.10", "Покупка и продажа собственного недвижимого имущества", Category.CLASS),
        Classification("68.10.0", "Покупка и продажа собственного недвижимого имущества", Category.SUBCLASS),
        Classification("68.2", "Сдача внаем собственного недвижимого имущества", Category.GROUP),
        Classification("68.20", "Сдача внаем собственного недвижимого имущества", Category.CLASS),
        Classification("68.20.0", "Сдача внаем собственного недвижимого имущества", Category.SUBCLASS),
        Classification(
            "68.3", "Операции с недвижимым имуществом за вознаграждение или на договорной основе", Category.GROUP
        ),
        Classification("68.31", "Деятельность агентств по операциям с недвижимым имуществом", Category.CLASS),
        Classification("68.31.0", "Деятельность агентств по операциям с недвижимым имуществом", Category.SUBCLASS),
        Classification("68.32", "Управление недвижимым имуществом", Category.CLASS),
        Classification("68.32.0", "Управление недвижимым имуществом", Category.SUBCLASS),
        Classification("M", "ПРОФЕССИОНАЛЬНАЯ, НАУЧНАЯ И ТЕХНИЧЕСКАЯ ДЕЯТЕЛЬНОСТЬ", Category.SECTION),
        Classification(
            "MA",
            "ДЕЯТЕЛЬНОСТЬ В ОБЛАСТИ ПРАВА, БУХГАЛТЕРСКОГО УЧЕТА, УПРАВЛЕНИЯ, АРХИТЕКТУРЫ, ИНЖЕНЕРНЫХ ИЗЫСКАНИЙ, ТЕХНИЧЕСКИХ ИСПЫТАНИЙ И КОНТРОЛЯ",
            Category.SECTION,
        ),
        Classification("69", "Деятельность в области права и бухгалтерского учета", Category.DIVISION),
        Classification("69.1", "Деятельность в области права", Category.GROUP),
        Classification("69.10", "Деятельность в области права", Category.CLASS),
        Classification("69.10.0", "Деятельность в области права", Category.SUBCLASS),
        Classification("69.2", "Деятельность в области бухгалтерского учета и аудита", Category.GROUP),
        Classification("69.20", "Деятельность в области бухгалтерского учета и аудита", Category.CLASS),
        Classification("69.20.0", "Деятельность в области бухгалтерского учета и аудита", Category.SUBCLASS),
        Classification(
            "70", "Деятельность центральных (головных) офисов, деятельность в области управления", Category.DIVISION
        ),
        Classification("70.1", "Деятельность центральных (головных) офисов", Category.GROUP),
        Classification("70.10", "Деятельность центральных (головных) офисов", Category.CLASS),
        Classification("70.10.0", "Деятельность центральных (головных) офисов", Category.SUBCLASS),
        Classification("70.2", "Консультирование по вопросам управления", Category.GROUP),
        Classification("70.21", "Консультирование по вопросам связи с общественностью", Category.CLASS),
        Classification("70.21.0", "Консультирование по вопросам связи с общественностью", Category.SUBCLASS),
        Classification("70.22", "Консультирование по вопросам коммерческой деятельности и управления", Category.CLASS),
        Classification(
            "70.22.0", "Консультирование по вопросам коммерческой деятельности и управления", Category.SUBCLASS
        ),
        Classification(
            "71",
            "Деятельность в области архитектуры и инженерных изысканий; технические испытания и контроль",
            Category.DIVISION,
        ),
        Classification(
            "71.1",
            "Деятельность в области архитектуры, инженерных изысканий и предоставление технических консультаций в этих областях",
            Category.GROUP,
        ),
        Classification("71.11", "Деятельность в области архитектуры", Category.CLASS),
        Classification("71.11.0", "Деятельность в области архитектуры", Category.SUBCLASS),
        Classification(
            "71.12",
            "Деятельность в области инженерных изысканий и предоставление технических консультаций в этих областях",
            Category.CLASS,
        ),
        Classification(
            "71.12.0",
            "Деятельность в области инженерных изысканий и предоставление технических консультаций в этих областях",
            Category.SUBCLASS,
        ),
        Classification("71.2", "Технические испытания и контроль", Category.GROUP),
        Classification("71.20", "Технические испытания и контроль", Category.CLASS),
        Classification("71.20.0", "Технические испытания и контроль", Category.SUBCLASS),
        Classification("MB", "НАУЧНЫЕ ИССЛЕДОВАНИЯ И РАЗРАБОТКИ", Category.SECTION),
        Classification("72", "Научные исследования и разработки", Category.DIVISION),
        Classification("72.1", "Исследования и разработки в области естественных и технических наук", Category.GROUP),
        Classification("72.11", "Исследования и разработки в области биотехнологии", Category.CLASS),
        Classification("72.11.0", "Исследования и разработки в области биотехнологии", Category.SUBCLASS),
        Classification(
            "72.19",
            "Исследования и разработки в области естественных и технических наук, кроме биотехнологии",
            Category.CLASS,
        ),
        Classification(
            "72.19.0",
            "Исследования и разработки в области естественных и технических наук, кроме биотехнологии",
            Category.SUBCLASS,
        ),
        Classification("72.2", "Исследования и разработки в области общественных и гуманитарных наук", Category.GROUP),
        Classification("72.20", "Исследования и разработки в области общественных и гуманитарных наук", Category.CLASS),
        Classification(
            "72.20.0", "Исследования и разработки в области общественных и гуманитарных наук", Category.SUBCLASS
        ),
        Classification("MC", "ПРОЧАЯ ПРОФЕССИОНАЛЬНАЯ, НАУЧНАЯ И ТЕХНИЧЕСКАЯ ДЕЯТЕЛЬНОСТЬ", Category.SECTION),
        Classification("73", "Рекламная деятельность и изучение рынка", Category.DIVISION),
        Classification("73.1", "Рекламная", Category.GROUP),
        Classification("73.11", "Деятельность рекламных агентств", Category.CLASS),
        Classification("73.11.0", "Деятельность рекламных агентств", Category.SUBCLASS),
        Classification("73.12", "Деятельность СМИ по предоставлению рекламных услуг", Category.CLASS),
        Classification("73.12.0", "Деятельность СМИ по предоставлению рекламных услуг", Category.SUBCLASS),
        Classification("73.2", "Исследование конъюнктуры рынка и изучение общественного мнения", Category.GROUP),
        Classification("73.20", "Исследование конъюнктуры рынка и изучение общественного мнения", Category.CLASS),
        Classification("73.20.0", "Исследование конъюнктуры рынка и изучение общественного мнения", Category.SUBCLASS),
        Classification("74", "Прочая профессиональная, научная и техническая деятельность", Category.DIVISION),
        Classification("74.1", "Специализированная дизайнерская деятельность", Category.GROUP),
        Classification("74.10", "Специализированная дизайнерская деятельность", Category.CLASS),
        Classification("74.10.0", "Специализированная дизайнерская деятельность", Category.SUBCLASS),
        Classification("74.2", "Деятельность в области фотографии", Category.GROUP),
        Classification("74.20", "Деятельность в области фотографии", Category.CLASS),
        Classification("74.20.0", "Деятельность в области фотографии", Category.SUBCLASS),
        Classification("74.3", "Письменный и устный перевод", Category.GROUP),
        Classification("74.30", "Письменный и устный перевод", Category.CLASS),
        Classification("74.30.0", "Письменный и устный перевод", Category.SUBCLASS),
        Classification(
            "74.9",
            "Прочая профессиональная, научная и техническая деятельность, не включенная в другие группировки",
            Category.GROUP,
        ),
        Classification(
            "74.90",
            "Прочая профессиональная, научная и техническая деятельность, не включенная в другие группировки",
            Category.CLASS,
        ),
        Classification(
            "74.90.0",
            "Прочая профессиональная, научная и техническая деятельность, не включенная в другие группировки",
            Category.SUBCLASS,
        ),
        Classification("75", "Ветеринарная деятельность", Category.DIVISION),
        Classification("75.0", "Ветеринарная деятельность", Category.GROUP),
        Classification("75.00", "Ветеринарная деятельность", Category.CLASS),
        Classification("75.00.0", "Ветеринарная деятельность", Category.SUBCLASS),
        Classification("N", "АДМИНИСТРАТИВНАЯ И ВСПОМОГАТЕЛЬНАЯ ДЕЯТЕЛЬНОСТЬ", Category.SECTION),
        Classification("77", "Аренда и лизинг", Category.DIVISION),
        Classification("77.1", "Аренда и лизинг автомобилей", Category.GROUP),
        Classification("77.11", "Аренда и лизинг пассажирских автомобилей и легких автофургонов", Category.CLASS),
        Classification("77.11.0", "Аренда и лизинг пассажирских автомобилей и легких автофургонов", Category.SUBCLASS),
        Classification("77.12", "Аренда и лизинг прочих автомобилей", Category.CLASS),
        Classification("77.12.0", "Аренда и лизинг прочих автомобилей", Category.SUBCLASS),
        Classification("77.2", "Прокат бытовых изделий и предметов личного пользования", Category.GROUP),
        Classification("77.21", "Прокат товаров для отдыха и спорта", Category.CLASS),
        Classification("77.21.0", "Прокат товаров для отдыха и спорта", Category.SUBCLASS),
        Classification("77.22", "Прокат видеокассет и дисков", Category.CLASS),
        Classification("77.22.0", "Прокат видеокассет и дисков", Category.SUBCLASS),
        Classification("77.29", "Прокат прочих бытовых изделий и предметов личного пользования", Category.CLASS),
        Classification("77.29.0", "Прокат прочих бытовых изделий и предметов личного пользования", Category.SUBCLASS),
        Classification("77.3", "Аренда прочих машин и оборудования и прочих предметов", Category.GROUP),
        Classification("77.31", "Аренда сельскохозяйственных машин и оборудования", Category.CLASS),
        Classification("77.31.0", "Аренда сельскохозяйственных машин и оборудования", Category.SUBCLASS),
        Classification("77.32", "Аренда строительных машин и оборудования", Category.CLASS),
        Classification("77.32.0", "Аренда строительных машин и оборудования", Category.SUBCLASS),
        Classification("77.33", "Аренда офисных машин и оборудования, включая вычислительную технику", Category.CLASS),
        Classification(
            "77.33.0", "Аренда офисных машин и оборудования, включая вычислительную технику", Category.SUBCLASS
        ),
        Classification("77.34", "Аренда водных транспортных средств и оборудования", Category.CLASS),
        Classification("77.34.0", "Аренда водных транспортных средств и оборудования", Category.SUBCLASS),
        Classification("77.35", "Аренда воздушных транспортных средств и оборудования", Category.CLASS),
        Classification("77.35.0", "Аренда воздушных транспортных средств и оборудования", Category.SUBCLASS),
        Classification(
            "77.39",
            "Аренда прочих машин и оборудования и прочих предметов, не включенных в другие группировки",
            Category.CLASS,
        ),
        Classification(
            "77.39.0",
            "Аренда прочих машин и оборудования и прочих предметов, не включенных в другие группировки",
            Category.SUBCLASS,
        ),
        Classification(
            "77.4",
            "Лизинг интеллектуальной собственности и аналогичных продуктов, кроме работ (произведений), защищенных авторским правом",
            Category.GROUP,
        ),
        Classification(
            "77.40",
            "Лизинг интеллектуальной собственности и аналогичных продуктов, кроме работ (произведений), защищенных авторским правом",
            Category.CLASS,
        ),
        Classification(
            "77.40.0",
            "Лизинг интеллектуальной собственности и аналогичных продуктов, кроме работ (произведений), защищенных авторским правом",
            Category.SUBCLASS,
        ),
        Classification("78", "Деятельность в области занятости", Category.DIVISION),
        Classification("78.1", "Деятельность агентств по трудоустройству", Category.GROUP),
        Classification("78.10", "Деятельность агентств по трудоустройству", Category.CLASS),
        Classification("78.10.0", "Деятельность агентств по трудоустройству", Category.SUBCLASS),
        Classification("78.2", "Деятельность по обеспечению временной рабочей силой", Category.GROUP),
        Classification("78.20", "Деятельность по обеспечению временной рабочей силой", Category.CLASS),
        Classification("78.20.0", "Деятельность по обеспечению временной рабочей силой", Category.SUBCLASS),
        Classification("78.3", "Деятельность по обеспечению прочими трудовыми ресурсами (персоналом)", Category.GROUP),
        Classification("78.30", "Деятельность по обеспечению прочими трудовыми ресурсами (персоналом)", Category.CLASS),
        Classification("78.30.0", "Деятельность по обеспечению прочими трудовыми ресурсами", Category.SUBCLASS),
        Classification(
            "79",
            "Деятельность туристических агентств и туроператоров, бронирование и прочая деятельность в области туризма",
            Category.DIVISION,
        ),
        Classification("79.1", "Деятельность туристических агентств и туроператоров", Category.GROUP),
        Classification("79.11", "Деятельность туристических агентств", Category.CLASS),
        Classification(
            "79.11.1",
            "Деятельность туристических агентств по оптовой розничной продаже экскурсий, путешествий, организованных туров",
            Category.SUBCLASS,
        ),
        Classification(
            "79.11.2",
            "Деятельность туристических агентств по бронированию мест на транспортных средствах",
            Category.SUBCLASS,
        ),
        Classification("79.11.9", "Прочая деятельность туристических агентств", Category.SUBCLASS),
        Classification("79.12", "Деятельность туроператоров", Category.CLASS),
        Classification("79.12.0", "Деятельность туроператоров", Category.SUBCLASS),
        Classification("79.9", "Бронирование и прочая деятельность в области туризма", Category.GROUP),
        Classification("79.90", "Бронирование и прочая деятельность в области туризма", Category.CLASS),
        Classification("79.90.0", "Бронирование и прочая деятельность в области туризма", Category.SUBCLASS),
        Classification("80", "Проведение расследований и обеспечение безопасности", Category.DIVISION),
        Classification("80.1", "Деятельность частных охранников и частных охранных бюро", Category.GROUP),
        Classification("80.10", "Деятельность частных охранников и частных охранных бюро", Category.CLASS),
        Classification("80.10.0", "Деятельность частных охранников и частных охранных бюро", Category.SUBCLASS),
        Classification("80.2", "Обеспечение функционирования систем безопасности", Category.GROUP),
        Classification("80.20", "Обеспечение функционирования систем безопасности", Category.CLASS),
        Classification("80.20.0", "Обеспечение функционирования систем безопасности", Category.SUBCLASS),
        Classification("80.3", "Проведение расследований", Category.GROUP),
        Classification("80.30", "Проведение расследований", Category.CLASS),
        Classification("80.30.0", "Проведение расследований", Category.SUBCLASS),
        Classification("81", "Деятельность по обслуживанию зданий и изменению ландшафта", Category.DIVISION),
        Classification("81.1", "Комплексная деятельность вспомогательно-технических служб", Category.GROUP),
        Classification("81.10", "Комплексная деятельность вспомогательно-технических служб", Category.CLASS),
        Classification("81.10.0", "Комплексная деятельность вспомогательно-технических служб", Category.SUBCLASS),
        Classification("81.2", "Деятельность по уборке", Category.GROUP),
        Classification("81.21", "Общая уборка помещений в зданиях всех типов", Category.CLASS),
        Classification("81.21.0", "Общая уборка помещений в зданиях всех типов", Category.SUBCLASS),
        Classification(
            "81.22", "Прочая (специализированная) уборка зданий и чистка промышленного оборудования", Category.CLASS
        ),
        Classification(
            "81.22.0",
            "Прочая (специализированная) уборка зданий и чистка промышленного оборудования",
            Category.SUBCLASS,
        ),
        Classification("81.29", "Прочая деятельность по уборке", Category.CLASS),
        Classification("81.29.0", "Прочая деятельность по уборке", Category.SUBCLASS),
        Classification("81.3", "Изменение ландшафта", Category.GROUP),
        Classification("81.30", "Изменение ландшафта", Category.CLASS),
        Classification("81.30.0", "Изменение ландшафта", Category.SUBCLASS),
        Classification(
            "82",
            "Административная и прочая дополнительная деятельность, направленная на поддержание бизнеса",
            Category.DIVISION,
        ),
        Classification(
            "82.1",
            "Административная и прочая дополнительная деятельность, направленная на поддержание бизнеса",
            Category.GROUP,
        ),
        Classification(
            "82.11", "Комплексная деятельность административных служб предприятий, организаций", Category.CLASS
        ),
        Classification(
            "82.11.0", "Комплексная деятельность административных служб предприятий, организаций", Category.SUBCLASS
        ),
        Classification(
            "82.19",
            "Фотокопирование, подготовка документов и прочая специальная дополнительная деятельность",
            Category.CLASS,
        ),
        Classification(
            "82.19.0",
            "Фотокопирование, подготовка документов и прочая специальная дополнительная деятельность",
            Category.SUBCLASS,
        ),
        Classification("82.2", "Деятельность телефонных справочных центров", Category.GROUP),
        Classification("82.20", "Деятельность телефонных справочных центров", Category.CLASS),
        Classification("82.20.0", "Деятельность телефонных справочных центров", Category.SUBCLASS),
        Classification("82.3", "Организация профессиональных салонов и конгрессов", Category.GROUP),
        Classification("82.30", "Организация профессиональных салонов и конгрессов", Category.CLASS),
        Classification("82.30.0", "Организация профессиональных салонов и конгрессов", Category.SUBCLASS),
        Classification(
            "82.9",
            "Дополнительная деятельность, направленная на поддержание бизнеса, не включенная в другие группировки",
            Category.GROUP,
        ),
        Classification(
            "82.91", "Деятельность агентств по сбору платежей и бюро по отчету о кредитных операциях", Category.CLASS
        ),
        Classification(
            "82.91.0",
            "Деятельность агентств по сбору платежей и бюро по отчету о кредитных операциях",
            Category.SUBCLASS,
        ),
        Classification("82.92", "Упаковывание", Category.CLASS),
        Classification("82.92.0", "Упаковывание", Category.SUBCLASS),
        Classification(
            "82.99",
            "Прочая дополнительная деятельность, направленная на поддержание бизнеса, не включенная в другие группировки",
            Category.CLASS,
        ),
        Classification(
            "82.99.0",
            "Прочая дополнительная деятельность, направленная на поддержание бизнеса, не включенная в другие группировки",
            Category.SUBCLASS,
        ),
        Classification(
            "O", "ГОСУДАРСТВЕННОЕ УПРАВЛЕНИЕ И ОБОРОНА; ОБЯЗАТЕЛЬНОЕ СОЦИАЛЬНОЕ ОБЕСПЕЧЕНИЕ", Category.SECTION
        ),
        Classification(
            "84", "Государственное управление и оборона; обязательное социальное обеспечение", Category.DIVISION
        ),
        Classification(
            "84.1", "Государственное управление общего характера; социально-экономическое управление", Category.GROUP
        ),
        Classification("84.11", "Государственное управление общего характера", Category.CLASS),
        Classification(
            "84.11.1", "Исполнительная и законодательная деятельность центральных органов управления", Category.SUBCLASS
        ),
        Classification("84.11.2", "Исполнительная деятельность региональных органов управления", Category.SUBCLASS),
        Classification(
            "84.11.3",
            "Деятельность представительных органов местного самоуправления - местные кенеши",
            Category.SUBCLASS,
        ),
        Classification(
            "84.11.4",
            "Деятельность исполнительных органов местного самоуправления - айыл окмоту, мэрии городов",
            Category.SUBCLASS,
        ),
        Classification("84.11.9", "Государственное управление общего характера", Category.SUBCLASS),
        Classification("84.12", "Управление социальными программами", Category.CLASS),
        Classification("84.12.0", "Управление социальными программами", Category.SUBCLASS),
        Classification(
            "84.13", "Регулирование и содействие эффективному ведению экономической деятельности", Category.CLASS
        ),
        Classification(
            "84.13.0", "Регулирование и содействие эффективному ведению экономической деятельности", Category.SUBCLASS
        ),
        Classification("84.2", "Предоставление государством услуг обществу в целом", Category.GROUP),
        Classification("84.21", "Международная деятельность", Category.CLASS),
        Classification("84.21.0", "Международная деятельность", Category.SUBCLASS),
        Classification("84.22", "Оборонная деятельность", Category.CLASS),
        Classification("84.22.0", "Оборонная деятельность", Category.SUBCLASS),
        Classification("84.23", "Деятельность в области юстиции и правосудия", Category.CLASS),
        Classification("84.23.0", "Деятельность в области юстиции и правосудия", Category.SUBCLASS),
        Classification("84.24", "Обеспечение общественного порядка и безопасности", Category.CLASS),
        Classification("84.24.0", "Обеспечение общественного порядка и безопасности", Category.SUBCLASS),
        Classification("84.25", "Обеспечение безопасности в чрезвычайных ситуациях", Category.CLASS),
        Classification("84.25.0", "Обеспечение безопасности в чрезвычайных ситуациях", Category.SUBCLASS),
        Classification("84.3", "Обязательное социальное страхование", Category.GROUP),
        Classification("84.30", "Обязательное социальное страхование", Category.CLASS),
        Classification("84.30.0", "Обязательное социальное страхование", Category.SUBCLASS),
        Classification("P", "ОБРАЗОВАНИЕ", Category.SECTION),
        Classification("85", "Образование", Category.DIVISION),
        Classification("85.1", "Дошкольное образование", Category.GROUP),
        Classification("85.10", "Дошкольное образование", Category.CLASS),
        Classification("85.10.0", "Дошкольное образование", Category.SUBCLASS),
        Classification("85.2", "Начальное образование", Category.GROUP),
        Classification("85.20", "Начальное образование", Category.CLASS),
        Classification("85.20.0", "Начальное образование", Category.SUBCLASS),
        Classification("85.3", "Среднее образование", Category.GROUP),
        Classification("85.31", "Общее среднее образование (вторая ступень)", Category.CLASS),
        Classification("85.31.0", "Общее среднее образование (вторая ступень)", Category.SUBCLASS),
        Classification("85.32", "Техническое и профессиональное среднее образование", Category.CLASS),
        Classification("85.32.1", "Начальное профессиональное (техническое) образование", Category.SUBCLASS),
        Classification("85.32.9", "Среднее профессиональное образование", Category.SUBCLASS),
        Classification("85.4", "Высшее образование", Category.GROUP),
        Classification("85.41", "Высшее образование (неполное)", Category.CLASS),
        Classification("85.41.0", "Высшее образование (неполное)", Category.SUBCLASS),
        Classification("85.42", "Высшее образование", Category.CLASS),
        Classification("85.42.0", "Высшее образование", Category.SUBCLASS),
        Classification("85.5", "Прочая образовательная деятельность", Category.GROUP),
        Classification("85.51", "Образовательная деятельность в области физической культуры и спорта", Category.CLASS),
        Classification(
            "85.51.0", "Образовательная деятельность в области физической культуры и спорта", Category.SUBCLASS
        ),
        Classification("85.52", "Образовательная деятельность в области культуры", Category.CLASS),
        Classification("85.52.0", "Образовательная деятельность в области культуры", Category.SUBCLASS),
        Classification("85.53", "Деятельность школ подготовки водителей", Category.CLASS),
        Classification("85.53.0", "Деятельность школ подготовки водителей", Category.SUBCLASS),
        Classification(
            "85.59", "Прочая деятельность в области образования, не включенная в другие группировки", Category.CLASS
        ),
        Classification(
            "85.59.0",
            "Прочая деятельность в области образования, не включенная в другие группировки",
            Category.SUBCLASS,
        ),
        Classification("85.6", "Вспомогательная деятельность в области образования", Category.GROUP),
        Classification("85.60", "Вспомогательная деятельность в области образования", Category.CLASS),
        Classification("85.60.0", "Вспомогательная деятельность в области образования", Category.SUBCLASS),
        Classification("Q", "ЗДРАВООХРАНЕНИЕ И СОЦИАЛЬНОЕ ОБСЛУЖИВАНИЕ НАСЕЛЕНИЯ", Category.SECTION),
        Classification("QA", "ЗДРАВООХРАНЕНИЕ", Category.SECTION),
        Classification("86", "Здравоохранение", Category.DIVISION),
        Classification("86.1", "Деятельность больниц", Category.GROUP),
        Classification("86.10", "Деятельность больниц", Category.CLASS),
        Classification("86.10.1", "Деятельность больниц", Category.SUBCLASS),
        Classification("86.10.9", "Деятельность санаторно-курортных учреждений", Category.SUBCLASS),
        Classification("86.2", "Деятельность в области врачебной практики и стоматологии", Category.GROUP),
        Classification("86.21", "Деятельность в области общей врачебной практики", Category.CLASS),
        Classification("86.21.0", "Деятельность в области общей врачебной практики", Category.SUBCLASS),
        Classification("86.22", "Деятельность в области специальной врачебной практики", Category.CLASS),
        Classification("86.22.0", "Деятельность в области специальной врачебной практики", Category.SUBCLASS),
        Classification("86.23", "Деятельность в области стоматологии", Category.CLASS),
        Classification("86.23.0", "Деятельность в области стоматологии", Category.SUBCLASS),
        Classification("86.9", "Прочая деятельность в области здравоохранения", Category.GROUP),
        Classification("86.90", "Прочая деятельность в области здравоохранения", Category.CLASS),
        Classification("86.90.0", "Прочая деятельность в области здравоохранения", Category.SUBCLASS),
        Classification("QB", "СОЦИАЛЬНОЕ ОБСЛУЖИВАНИЕ НАСЕЛЕНИЯ", Category.SECTION),
        Classification("87", "Социальное обслуживание населения с обеспечением проживания", Category.DIVISION),
        Classification(
            "87.1",
            "Социальное обслуживание с обеспечением проживания и ухода за пациентами средним медицинским персоналом",
            Category.GROUP,
        ),
        Classification(
            "87.10",
            "Социальное обслуживание с обеспечением проживания и ухода за пациентами средним медицинским персоналом",
            Category.CLASS,
        ),
        Classification(
            "87.10.0",
            "Социальное обслуживание с обеспечением проживания и ухода за пациентами средним медицинским персоналом",
            Category.SUBCLASS,
        ),
        Classification(
            "87.2",
            "Социальное обслуживание с обеспечением проживания лиц с задержкой умственного развития, лиц злоупотребляющих алкоголем или наркотиками, с психическими отклонениями или ограниченными возможностями здоровья (физическими недостатками)",
            Category.GROUP,
        ),
        Classification(
            "87.20",
            "Социальное обслуживание с обеспечением проживания лиц с задержкой умственного развития, лиц злоупотребляющих алкоголем или наркотиками, с психическими отклонениями или ограниченными возможностями здоровья (физическими недостатками)",
            Category.CLASS,
        ),
        Classification(
            "87.3", "Социальное обслуживание с обеспечением проживания пожилых и недееспособных", Category.GROUP
        ),
        Classification(
            "87.30", "Социальное обслуживание с обеспечением проживания пожилых и недееспособных", Category.CLASS
        ),
        Classification(
            "87.30.0", "Социальное обслуживание с обеспечением проживания пожилых и недееспособных", Category.SUBCLASS
        ),
        Classification("87.9", "Прочее социальное обслуживание с обеспечением проживания", Category.GROUP),
        Classification("87.90", "Прочее социальное обслуживание с обеспечением проживания", Category.CLASS),
        Classification("87.90.0", "Прочее социальное обслуживание с обеспечением проживания", Category.SUBCLASS),
        Classification("88", "Социальное обслуживание без обеспечения проживания", Category.DIVISION),
        Classification(
            "88.1", "Социальное обслуживание без обеспечением проживания пожилых и недееспособных", Category.GROUP
        ),
        Classification(
            "88.10", "Социальное обслуживание без обеспечения проживания пожилых и недееспособных", Category.CLASS
        ),
        Classification(
            "88.10.0", "Социальное обслуживание без обеспечения проживания пожилых и недееспособных", Category.SUBCLASS
        ),
        Classification("88.9", "Прочее социальное обслуживание без обеспечения проживания", Category.GROUP),
        Classification("88.91", "Дневной уход за детьми", Category.CLASS),
        Classification("88.91.0", "Дневной уход за детьми", Category.SUBCLASS),
        Classification(
            "88.99",
            "Прочее социальное обслуживание без обеспечения проживания, не включенное в другие группировки",
            Category.CLASS,
        ),
        Classification(
            "88.99.0",
            "Прочее социальное обслуживание без обеспечения проживания, не включенное в другие группировки",
            Category.SUBCLASS,
        ),
        Classification("R", "ИСКУССТВО, РАЗВЛЕЧЕНИЯ И ОТДЫХ", Category.SECTION),
        Classification(
            "90",
            "Артистическая и прочая деятельность в области искусства и проведения культурно-массовых развлекательных мероприятий",
            Category.DIVISION,
        ),
        Classification(
            "90.0",
            "Артистическая и прочая деятельность в области искусства и проведения культурно-массовых развлекательных мероприятий",
            Category.GROUP,
        ),
        Classification("90.01", "Артистическая деятельность", Category.CLASS),
        Classification("90.01.0", "Артистическая деятельность", Category.SUBCLASS),
        Classification("90.02", "Вспомогательная деятельность в области артистического искусства", Category.CLASS),
        Classification("90.02.0", "Вспомогательная деятельность в области артистического искусства", Category.SUBCLASS),
        Classification("90.03", "Деятельность в области прочих видов искусства", Category.CLASS),
        Classification("90.03.0", "Деятельность в области прочих видов искусства", Category.SUBCLASS),
        Classification("90.04", "Деятельность театральных и концертных залов", Category.CLASS),
        Classification("90.04.0", "Деятельность театральных и концертных залов", Category.SUBCLASS),
        Classification("91", "Деятельность библиотек, архивов, музеев и прочих учреждений культуры", Category.DIVISION),
        Classification("91.0", "Деятельность библиотек, архивов, музеев и прочих учреждений культуры", Category.GROUP),
        Classification("91.01", "Деятельность библиотек и архивов", Category.CLASS),
        Classification("91.01.1", "Деятельность библиотек и архивов", Category.SUBCLASS),
        Classification("91.01.9", "Деятельность учреждений культуры клубного типа", Category.SUBCLASS),
        Classification("91.02", "Деятельность музеев", Category.CLASS),
        Classification("91.02.0", "Деятельность музеев", Category.SUBCLASS),
        Classification("91.03", "Деятельность по сохранению и посещению исторических мест и зданий", Category.CLASS),
        Classification(
            "91.03.0", "Деятельность по сохранению и посещению исторических мест и зданий", Category.SUBCLASS
        ),
        Classification("91.04", "Деятельность ботанических садов, зоопарков и заповедников", Category.CLASS),
        Classification("91.04.0", "Деятельность ботанических садов, зоопарков и заповедников", Category.SUBCLASS),
        Classification("92", "Организация и проведение лотереи, продажа лотерейных билетов", Category.DIVISION),
        Classification("92.0", "Организация и проведение лотереи, продажа лотерейных билетов", Category.GROUP),
        Classification("92.00", "Организация и проведение лотереи, продажа лотерейных билетов", Category.CLASS),
        Classification("92.00.0", "Организация и проведение лотереи, продажа лотерейных билетов", Category.SUBCLASS),
        Classification("93", "Спортивная и прочая деятельность по организации отдыха и развлечений", Category.DIVISION),
        Classification("93.1", "Спортивная деятельность", Category.GROUP),
        Classification("93.11", "Эксплуатация и управление спортивными сооружениями", Category.CLASS),
        Classification("93.11.0", "Эксплуатация и управление спортивными сооружениями", Category.SUBCLASS),
        Classification("93.12", "Деятельность спортивных клубов", Category.CLASS),
        Classification("93.12.0", "Деятельность спортивных клубов", Category.SUBCLASS),
        Classification("93.13", "Деятельность фитнесс-клубов", Category.CLASS),
        Classification("93.13.0", "Деятельность фитнесс-клубов", Category.SUBCLASS),
        Classification("93.19", "Прочая спортивная деятельность", Category.CLASS),
        Classification("93.19.0", "Прочая спортивная деятельность", Category.SUBCLASS),
        Classification("93.2", "Деятельность по организации отдыха и развлечений", Category.GROUP),
        Classification("93.21", "Деятельность парков отдыха и развлечений", Category.CLASS),
        Classification("93.21.0", "Деятельность парков отдыха и развлечений", Category.SUBCLASS),
        Classification("93.29", "Прочая деятельность по организации отдыха и развлечений", Category.CLASS),
        Classification("93.29.0", "Прочая деятельность по организации отдыха и развлечений", Category.SUBCLASS),
        Classification("S", "ПРОЧАЯ ОБСЛУЖИВАЮЩАЯ ДЕЯТЕЛЬНОСТЬ", Category.SECTION),
        Classification("94", "Деятельность общественных объединений (организаций)", Category.DIVISION),
        Classification(
            "94.1",
            "Деятельность коммерческих, предпринимательских и профессиональных общественных организаций (ассоциаций)",
            Category.GROUP,
        ),
        Classification(
            "94.11",
            "Деятельность коммерческих, предпринимательских общественных организаций (ассоциаций)",
            Category.CLASS,
        ),
        Classification(
            "94.11.0",
            "Деятельность коммерческих, предпринимательских общественных организаций (ассоциаций)",
            Category.SUBCLASS,
        ),
        Classification("94.12", "Деятельность профессиональных общественных организаций (ассоциаций)", Category.CLASS),
        Classification(
            "94.12.0", "Деятельность профессиональных общественных организаций (ассоциаций)", Category.SUBCLASS
        ),
        Classification("94.2", "Деятельность профессиональных союзов", Category.GROUP),
        Classification("94.20", "Деятельность профессиональных союзов", Category.CLASS),
        Classification("94.20.0", "Деятельность профессиональных союзов", Category.SUBCLASS),
        Classification("94.9", "Деятельность прочих общественных объединений", Category.GROUP),
        Classification("94.91", "Деятельность религиозных организаций", Category.CLASS),
        Classification("94.91.0", "Деятельность религиозных организаций", Category.SUBCLASS),
        Classification("94.92", "Деятельность политических организаций", Category.CLASS),
        Classification("94.92.0", "Деятельность политических организаций", Category.SUBCLASS),
        Classification(
            "94.99", "Деятельность прочих общественных организаций, не включенных в другие группировки", Category.CLASS
        ),
        Classification(
            "94.99.1",
            "Деятельность общественных организаций (объединений) в области культуры и рекреации",
            Category.SUBCLASS,
        ),
        Classification(
            "94.99.2", "Деятельность правозащитных общественных организаций (объединений)", Category.SUBCLASS
        ),
        Classification(
            "94.99.3",
            "Деятельность общественных организаций (объединений) в области охраны окружающей среды",
            Category.SUBCLASS,
        ),
        Classification(
            "94.99.4",
            "Деятельность общественных организаций (объединений) в области филантропии и поощрения добровольной деятельности",
            Category.SUBCLASS,
        ),
        Classification(
            "94.99.5",
            "Деятельность общественных организаций (объединений), имеющих патриотические цели",
            Category.SUBCLASS,
        ),
        Classification(
            "94.99.6",
            "Деятельность общественных организаций (объединений) в области экономического, социального и общинного развития",
            Category.SUBCLASS,
        ),
        Classification(
            "94.99.9",
            "Деятельность прочих общественных организаций, не включенных в другие группировки",
            Category.SUBCLASS,
        ),
        Classification("95", "Ремонт компьютеров, предметов личного пользования и бытовых товаров", Category.DIVISION),
        Classification("95.1", "Ремонт компьютеров и оборудования связи", Category.GROUP),
        Classification("95.11", "Ремонт компьютеров и периферийного оборудования", Category.CLASS),
        Classification("95.11.0", "Ремонт компьютеров и периферийного оборудования", Category.SUBCLASS),
        Classification("95.12", "Ремонт оборудования связи", Category.CLASS),
        Classification("95.12.0", "Ремонт оборудования связи", Category.SUBCLASS),
        Classification("95.2", "Ремонт предметов личного пользования и бытовых товаров", Category.GROUP),
        Classification("95.21", "Ремонт электробытовых товаров", Category.CLASS),
        Classification("95.21.0", "Ремонт электробытовых товаров", Category.SUBCLASS),
        Classification("95.22", "Ремонт бытовой техники и садового оборудования", Category.CLASS),
        Classification("95.22.0", "Ремонт бытовой техники и садового оборудования", Category.SUBCLASS),
        Classification("95.23", "Ремонт обуви и прочих изделий из кожи", Category.CLASS),
        Classification("95.23.0", "Ремонт обуви и прочих изделий из кожи", Category.SUBCLASS),
        Classification("95.24", "Ремонт мебели и аналогичных домашних изделий", Category.CLASS),
        Classification("95.24.0", "Ремонт мебели и аналогичных домашних изделий", Category.SUBCLASS),
        Classification("95.25", "Ремонт часов и ювелирных изделий", Category.CLASS),
        Classification("95.25.0", "Ремонт часов и ювелирных изделий", Category.SUBCLASS),
        Classification("95.29", "Ремонт прочих предметов личного пользования и бытовых товаров", Category.CLASS),
        Classification("95.29.0", "Ремонт прочих предметов личного пользования и бытовых товаров", Category.SUBCLASS),
        Classification("96", "Прочее индивидуальное обслуживание", Category.DIVISION),
        Classification("96.0", "Прочее индивидуальное обслуживание", Category.GROUP),
        Classification(
            "96.01", "Стирка, химическая чистка и окрашивание текстильных и меховых изделий", Category.CLASS
        ),
        Classification(
            "96.01.0", "Стирка, химическая чистка и окрашивание текстильных и меховых изделий", Category.SUBCLASS
        ),
        Classification("96.02", "Деятельность парикмахерских и салонов красоты", Category.CLASS),
        Classification("96.02.0", "Деятельность парикмахерских и салонов красоты", Category.SUBCLASS),
        Classification("96.03", "Организация похорон и связанная с этим деятельность", Category.CLASS),
        Classification("96.03.0", "Организация похорон и связанная с этим деятельность", Category.SUBCLASS),
        Classification("96.04", "Деятельность по обеспечению физического комфорта", Category.CLASS),
        Classification("96.04.0", "Деятельность по обеспечению физического комфорта", Category.SUBCLASS),
        Classification(
            "96.09", "Прочее индивидуальное обслуживание, не включенное в другие группировки", Category.CLASS
        ),
        Classification(
            "96.09.0", "Прочее индивидуальное обслуживание, не включенное в другие группировки", Category.SUBCLASS
        ),
        Classification(
            "T",
            "ДЕЯТЕЛЬНОСТЬ ЧАСТНЫХ ДОМАШНИХ ХОЗЯЙСТВ С НАЕМНЫМИ РАБОТНИКАМИ; ПРОИЗВОДСТВО ЧАСТНЫМИ ДОМАШНИМИ ХОЗЯЙСТВАМИ РАЗНООБРАЗНЫХ ТОВАРОВ И УСЛУГ ДЛЯ СОБСТВЕННОГО ПОТРЕБЛЕНИЯ",
            Category.SECTION,
        ),
        Classification("97", "Деятельность частных домашних хозяйств с наемными работниками", Category.DIVISION),
        Classification("97.0", "Деятельность частных домашних хозяйств с наемными работниками", Category.GROUP),
        Classification("97.00", "Деятельность частных домашних хозяйств с наемными работниками", Category.CLASS),
        Classification("97.00.0", "Деятельность частных домашних хозяйств с наемными работниками", Category.SUBCLASS),
        Classification(
            "98",
            "Производство частными домашними хозяйствами разнообразных товаров и услуг для собственного потребления",
            Category.DIVISION,
        ),
        Classification(
            "98.1",
            "Производство частными домашними хозяйствами разнообразных товаров и услуг для собственного потребления",
            Category.GROUP,
        ),
        Classification(
            "98.10",
            "Производство частными домашними хозяйствами разнообразных товаров для собственного потребления",
            Category.CLASS,
        ),
        Classification(
            "98.10.0",
            "Производство частными домашними хозяйствами разнообразных товаров для собственного потребления",
            Category.SUBCLASS,
        ),
        Classification(
            "98.2",
            "Предоставление частными домашними хозяйствами разнообразных услуг для собственного потребления",
            Category.GROUP,
        ),
        Classification(
            "98.20",
            "Предоставление частными домашними хозяйствами разнообразных услуг для собственного потребления",
            Category.CLASS,
        ),
        Classification(
            "98.20.0",
            "Предоставление частными домашними хозяйствами разнообразных услуг для собственного потребления",
            Category.SUBCLASS,
        ),
        Classification("U", "ДЕЯТЕЛЬНОСТЬ ЭКСТЕРРИТОРИАЛЬНЫХ ОРГАНИЗАЦИЙ", Category.SECTION),
        Classification("99", "Деятельность экстерриториальных организаций", Category.DIVISION),
        Classification("99.0", "Деятельность экстерриториальных организаций", Category.GROUP),
        Classification("99.00", "Деятельность экстерриториальных организаций", Category.CLASS),
        Classification("99.00.0", "Деятельность экстерриториальных организаций", Category.SUBCLASS),
    ],
)
