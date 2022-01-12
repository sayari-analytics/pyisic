# -*- coding: utf-8 -*-
"""`SKIS2010 – Standard Classification of Institutional Sectors, ESR 2010 <https://www.stat.si/statweb/en/methods/classifications>`_.
"""
from ...types import Category, Classification, Standard, Standards

SKIS2010 = Standard(
    standard=Standards.SKIS2010,
    classes=[
        Classification("S.1", "Total economy", Category.SECTION),
        Classification("S.11", "Non-financial corporations", Category.GROUP),
        Classification("S.11001", "Public non-financial corporations", Category.CLASS),
        Classification("S.11002", "National private non-financial corporations", Category.CLASS),
        Classification("S.11003", "Foreign controlled non-financial corporations", Category.CLASS),
        Classification("S.12", "Financial corporations", Category.GROUP),
        Classification("S.121", "Central bank", Category.CLASS),
        Classification("S.122", "Deposit-taking corporations except the central bank", Category.CLASS),
        Classification("S.12201", "Public deposit-taking corporations except the central bank", Category.CLASS),
        Classification(
            "S.12202", "National private deposit-taking corporations except the central bank", Category.CLASS
        ),
        Classification(
            "S.12203", "Foreign controlled deposit-taking corporations except the central bank", Category.CLASS
        ),
        Classification("S.123", "Money market funds (MMFs)", Category.CLASS),
        Classification("S.12301", "Public money market funds (MMFs)", Category.CLASS),
        Classification("S.12302", "National private money market funds (MMFs)", Category.CLASS),
        Classification("S.12303", "Foreign controlled money market funds (MMFs)", Category.CLASS),
        Classification("S.124", "Non-MMF investment funds", Category.CLASS),
        Classification("S.12401", "Public non-MMF investment funds", Category.CLASS),
        Classification("S.12402", "National private non-MMF investment funds", Category.CLASS),
        Classification("S.12403", "Foreign controlled non-MMF investment funds", Category.CLASS),
        Classification(
            "S.125", "Other financial intermediaries, except insurance corporations and pension funds", Category.CLASS
        ),
        Classification(
            "S.12501",
            "Public other financial intermediaries, except insurance corporations and pension funds",
            Category.CLASS,
        ),
        Classification(
            "S.12502",
            "National private other financial intermediaries, except insurance corporations and pension funds",
            Category.CLASS,
        ),
        Classification(
            "S.12503",
            "Foreign controlled other financial intermediaries, except insurance corporations and pension funds",
            Category.CLASS,
        ),
        Classification("S.126", "Financial auxiliaries", Category.CLASS),
        Classification("S.1260", "Financial auxiliaries", Category.CLASS),
        Classification("S.12601", "Public financial auxiliaries", Category.CLASS),
        Classification("S.12602", "National private financial auxiliaries", Category.CLASS),
        Classification("S.12603", "Foreign controlled financial auxiliaries", Category.CLASS),
        Classification("S.127", "Captive financial institutions and money lenders", Category.CLASS),
        Classification("S.1270", "Captive financial institutions and money lenders", Category.CLASS),
        Classification("S.12701", "Public captive financial institutions and money lenders", Category.CLASS),
        Classification("S.12702", "National private captive financial institutions and money lenders", Category.CLASS),
        Classification(
            "S.12703", "Foreign controlled captive financial institutions and money lenders", Category.CLASS
        ),
        Classification("S.128", "Insurance corporations (IC)", Category.CLASS),
        Classification("S.1280", "Insurance corporations (IC)", Category.CLASS),
        Classification("S.12801", "Public insurance corporations (IC)", Category.CLASS),
        Classification("S.12802", "National private insurance corporations (IC)", Category.CLASS),
        Classification("S.12803", "Foreign controlled insurance corporations (IC)", Category.CLASS),
        Classification("S.129", "Pension funds (PF)", Category.CLASS),
        Classification("S.12901", "Public pension funds (PF)", Category.CLASS),
        Classification("S.12902", "National private pension funds (PF)", Category.CLASS),
        Classification("S.12903", "Foreign controlled pension funds (PF)", Category.CLASS),
        Classification("S.13", "General government", Category.GROUP),
        Classification("S.1311", "Central government (excluding social security funds)", Category.CLASS),
        Classification("S.13111", "Direct users of the state budget", Category.CLASS),
        Classification("S.13112", "State funds", Category.CLASS),
        Classification("S.13113", "Other units on the state level", Category.CLASS),
        Classification("S.1312", "State government", Category.CLASS),
        Classification("S.1313", "Local government (excluding social security funds)", Category.CLASS),
        Classification("S.13131", "Direct users of the municipal budget", Category.CLASS),
        Classification("S.13132", "Local funds", Category.CLASS),
        Classification("S.13133", "Other units on the local level", Category.CLASS),
        Classification("S.1314", "Social security funds", Category.CLASS),
        Classification("S.14", "Households", Category.GROUP),
        Classification("S.141", "Employers, self-employed", Category.CLASS),
        Classification("S.142", "Own account-workers", Category.CLASS),
        Classification("S.143", "Employees", Category.CLASS),
        Classification("S.144", "Recipients of property and transfer income", Category.CLASS),
        Classification("S.1441", "Recipients of property income", Category.CLASS),
        Classification("S.1442", "Recipients of pensions", Category.CLASS),
        Classification("S.1443", "Recipients of other transfers", Category.CLASS),
        Classification("S.15", "Non-profit institutions serving households", Category.GROUP),
        Classification("S.2", "Rest of the world", Category.SECTION),
        Classification("S.21", "Member States and institutions and bodies of the European Union", Category.GROUP),
        Classification("S.211", "Member States of the European Union", Category.CLASS),
        Classification("S.212", "Institutions and bodies of the European Union", Category.CLASS),
        Classification(
            "S.22",
            "Non-member countries and international organisations non- resident in the European Union",
            Category.GROUP,
        ),
    ],
)
