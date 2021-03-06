"""`Concordance between NACEBEL2008 and NACE2 <https://economie.fgov.be/sites/default/files/Files/Entreprises/KBO/conversiontable-Nacebel-2003-2008.xls>`_.

All the NACEBEL2008 codes that end in 0 and are 5 characters long directly map to a NACE2 code by removing the last 0
and adding a dot (.) in the second position.
"""
from ...types import Concordance, Standards
from ..nace2 import NACE2
from . import NACEBEL2008

NACEBEL2008_to_NACE2 = Concordance(
    src=NACEBEL2008,
    dst=NACE2,
    concordances=[
        ((Standards.NACEBEL2008, "01110"), (Standards.NACE2, "01.11")),
        ((Standards.NACEBEL2008, "01120"), (Standards.NACE2, "01.12")),
        ((Standards.NACEBEL2008, "01130"), (Standards.NACE2, "01.13")),
        ((Standards.NACEBEL2008, "01140"), (Standards.NACE2, "01.14")),
        ((Standards.NACEBEL2008, "01150"), (Standards.NACE2, "01.15")),
        ((Standards.NACEBEL2008, "01160"), (Standards.NACE2, "01.16")),
        ((Standards.NACEBEL2008, "01260"), (Standards.NACE2, "01.26")),
        ((Standards.NACEBEL2008, "01280"), (Standards.NACE2, "01.28")),
        ((Standards.NACEBEL2008, "01290"), (Standards.NACE2, "01.29")),
        ((Standards.NACEBEL2008, "01630"), (Standards.NACE2, "01.63")),
        ((Standards.NACEBEL2008, "01640"), (Standards.NACE2, "01.64")),
        ((Standards.NACEBEL2008, "02300"), (Standards.NACE2, "02.30")),
        ((Standards.NACEBEL2008, "01250"), (Standards.NACE2, "01.25")),
        ((Standards.NACEBEL2008, "02100"), (Standards.NACE2, "02.10")),
        ((Standards.NACEBEL2008, "01240"), (Standards.NACE2, "01.24")),
        ((Standards.NACEBEL2008, "01210"), (Standards.NACE2, "01.21")),
        ((Standards.NACEBEL2008, "01220"), (Standards.NACE2, "01.22")),
        ((Standards.NACEBEL2008, "01230"), (Standards.NACE2, "01.23")),
        ((Standards.NACEBEL2008, "01270"), (Standards.NACE2, "01.27")),
        ((Standards.NACEBEL2008, "10410"), (Standards.NACE2, "10.41")),
        ((Standards.NACEBEL2008, "11020"), (Standards.NACE2, "11.02")),
        ((Standards.NACEBEL2008, "01410"), (Standards.NACE2, "01.41")),
        ((Standards.NACEBEL2008, "01420"), (Standards.NACE2, "01.42")),
        ((Standards.NACEBEL2008, "01450"), (Standards.NACE2, "01.45")),
        ((Standards.NACEBEL2008, "01430"), (Standards.NACE2, "01.43")),
        ((Standards.NACEBEL2008, "01490"), (Standards.NACE2, "01.49")),
        ((Standards.NACEBEL2008, "01440"), (Standards.NACE2, "01.44")),
        ((Standards.NACEBEL2008, "03220"), (Standards.NACE2, "03.22")),
        ((Standards.NACEBEL2008, "01500"), (Standards.NACE2, "01.50")),
        ((Standards.NACEBEL2008, "81300"), (Standards.NACE2, "81.30")),
        ((Standards.NACEBEL2008, "01610"), (Standards.NACE2, "01.61")),
        ((Standards.NACEBEL2008, "01620"), (Standards.NACE2, "01.62")),
        ((Standards.NACEBEL2008, "01700"), (Standards.NACE2, "01.70")),
        ((Standards.NACEBEL2008, "02200"), (Standards.NACE2, "02.20")),
        ((Standards.NACEBEL2008, "16100"), (Standards.NACE2, "16.10")),
        ((Standards.NACEBEL2008, "02400"), (Standards.NACE2, "02.40")),
        ((Standards.NACEBEL2008, "03110"), (Standards.NACE2, "03.11")),
        ((Standards.NACEBEL2008, "03120"), (Standards.NACE2, "03.12")),
        ((Standards.NACEBEL2008, "03210"), (Standards.NACE2, "03.21")),
        ((Standards.NACEBEL2008, "09900"), (Standards.NACE2, "09.90")),
        ((Standards.NACEBEL2008, "05100"), (Standards.NACE2, "05.10")),
        ((Standards.NACEBEL2008, "19200"), (Standards.NACE2, "19.20")),
        ((Standards.NACEBEL2008, "05200"), (Standards.NACE2, "05.20")),
        ((Standards.NACEBEL2008, "08920"), (Standards.NACE2, "08.92")),
        ((Standards.NACEBEL2008, "09100"), (Standards.NACE2, "09.10")),
        ((Standards.NACEBEL2008, "06100"), (Standards.NACE2, "06.10")),
        ((Standards.NACEBEL2008, "06200"), (Standards.NACE2, "06.20")),
        ((Standards.NACEBEL2008, "52210"), (Standards.NACE2, "52.21")),
        ((Standards.NACEBEL2008, "52220"), (Standards.NACE2, "52.22")),
        ((Standards.NACEBEL2008, "07210"), (Standards.NACE2, "07.21")),
        ((Standards.NACEBEL2008, "07100"), (Standards.NACE2, "07.10")),
        ((Standards.NACEBEL2008, "07290"), (Standards.NACE2, "07.29")),
        ((Standards.NACEBEL2008, "08910"), (Standards.NACE2, "08.91")),
        ((Standards.NACEBEL2008, "10840"), (Standards.NACE2, "10.84")),
        ((Standards.NACEBEL2008, "08930"), (Standards.NACE2, "08.93")),
        ((Standards.NACEBEL2008, "08990"), (Standards.NACE2, "08.99")),
        ((Standards.NACEBEL2008, "10110"), (Standards.NACE2, "10.11")),
        ((Standards.NACEBEL2008, "10120"), (Standards.NACE2, "10.12")),
        ((Standards.NACEBEL2008, "10130"), (Standards.NACE2, "10.13")),
        ((Standards.NACEBEL2008, "10850"), (Standards.NACE2, "10.85")),
        ((Standards.NACEBEL2008, "10890"), (Standards.NACE2, "10.89")),
        ((Standards.NACEBEL2008, "10200"), (Standards.NACE2, "10.20")),
        ((Standards.NACEBEL2008, "10320"), (Standards.NACE2, "10.32")),
        ((Standards.NACEBEL2008, "10420"), (Standards.NACE2, "10.42")),
        ((Standards.NACEBEL2008, "10510"), (Standards.NACE2, "10.51")),
        ((Standards.NACEBEL2008, "10520"), (Standards.NACE2, "10.52")),
        ((Standards.NACEBEL2008, "10610"), (Standards.NACE2, "10.61")),
        ((Standards.NACEBEL2008, "10620"), (Standards.NACE2, "10.62")),
        ((Standards.NACEBEL2008, "10910"), (Standards.NACE2, "10.91")),
        ((Standards.NACEBEL2008, "10920"), (Standards.NACE2, "10.92")),
        ((Standards.NACEBEL2008, "10720"), (Standards.NACE2, "10.72")),
        ((Standards.NACEBEL2008, "10810"), (Standards.NACE2, "10.81")),
        ((Standards.NACEBEL2008, "10820"), (Standards.NACE2, "10.82")),
        ((Standards.NACEBEL2008, "10730"), (Standards.NACE2, "10.73")),
        ((Standards.NACEBEL2008, "10830"), (Standards.NACE2, "10.83")),
        ((Standards.NACEBEL2008, "82920"), (Standards.NACE2, "82.92")),
        ((Standards.NACEBEL2008, "10860"), (Standards.NACE2, "10.86")),
        ((Standards.NACEBEL2008, "11010"), (Standards.NACE2, "11.01")),
        ((Standards.NACEBEL2008, "20140"), (Standards.NACE2, "20.14")),
        ((Standards.NACEBEL2008, "11030"), (Standards.NACE2, "11.03")),
        ((Standards.NACEBEL2008, "11040"), (Standards.NACE2, "11.04")),
        ((Standards.NACEBEL2008, "11050"), (Standards.NACE2, "11.05")),
        ((Standards.NACEBEL2008, "11060"), (Standards.NACE2, "11.06")),
        ((Standards.NACEBEL2008, "11070"), (Standards.NACE2, "11.07")),
        ((Standards.NACEBEL2008, "12000"), (Standards.NACE2, "12.00")),
        ((Standards.NACEBEL2008, "13100"), (Standards.NACE2, "13.10")),
        ((Standards.NACEBEL2008, "13200"), (Standards.NACE2, "13.20")),
        ((Standards.NACEBEL2008, "13300"), (Standards.NACE2, "13.30")),
        ((Standards.NACEBEL2008, "18120"), (Standards.NACE2, "18.12")),
        ((Standards.NACEBEL2008, "32500"), (Standards.NACE2, "32.50")),
        ((Standards.NACEBEL2008, "33190"), (Standards.NACE2, "33.19")),
        ((Standards.NACEBEL2008, "95290"), (Standards.NACE2, "95.29")),
        ((Standards.NACEBEL2008, "13930"), (Standards.NACE2, "13.93")),
        ((Standards.NACEBEL2008, "13940"), (Standards.NACE2, "13.94")),
        ((Standards.NACEBEL2008, "13950"), (Standards.NACE2, "13.95")),
        ((Standards.NACEBEL2008, "13960"), (Standards.NACE2, "13.96")),
        ((Standards.NACEBEL2008, "13990"), (Standards.NACE2, "13.99")),
        ((Standards.NACEBEL2008, "17220"), (Standards.NACE2, "17.22")),
        ((Standards.NACEBEL2008, "13910"), (Standards.NACE2, "13.91")),
        ((Standards.NACEBEL2008, "14310"), (Standards.NACE2, "14.31")),
        ((Standards.NACEBEL2008, "14390"), (Standards.NACE2, "14.39")),
        ((Standards.NACEBEL2008, "14110"), (Standards.NACE2, "14.11")),
        ((Standards.NACEBEL2008, "32990"), (Standards.NACE2, "32.99")),
        ((Standards.NACEBEL2008, "14120"), (Standards.NACE2, "14.12")),
        ((Standards.NACEBEL2008, "14130"), (Standards.NACE2, "14.13")),
        ((Standards.NACEBEL2008, "14140"), (Standards.NACE2, "14.14")),
        ((Standards.NACEBEL2008, "14200"), (Standards.NACE2, "14.20")),
        ((Standards.NACEBEL2008, "15110"), (Standards.NACE2, "15.11")),
        ((Standards.NACEBEL2008, "15120"), (Standards.NACE2, "15.12")),
        ((Standards.NACEBEL2008, "15200"), (Standards.NACE2, "15.20")),
        ((Standards.NACEBEL2008, "22190"), (Standards.NACE2, "22.19")),
        ((Standards.NACEBEL2008, "22290"), (Standards.NACE2, "22.29")),
        ((Standards.NACEBEL2008, "16210"), (Standards.NACE2, "16.21")),
        ((Standards.NACEBEL2008, "16230"), (Standards.NACE2, "16.23")),
        ((Standards.NACEBEL2008, "16220"), (Standards.NACE2, "16.22")),
        ((Standards.NACEBEL2008, "43320"), (Standards.NACE2, "43.32")),
        ((Standards.NACEBEL2008, "16240"), (Standards.NACE2, "16.24")),
        ((Standards.NACEBEL2008, "17110"), (Standards.NACE2, "17.11")),
        ((Standards.NACEBEL2008, "17120"), (Standards.NACE2, "17.12")),
        ((Standards.NACEBEL2008, "17210"), (Standards.NACE2, "17.21")),
        ((Standards.NACEBEL2008, "17230"), (Standards.NACE2, "17.23")),
        ((Standards.NACEBEL2008, "17240"), (Standards.NACE2, "17.24")),
        ((Standards.NACEBEL2008, "17290"), (Standards.NACE2, "17.29")),
        ((Standards.NACEBEL2008, "58110"), (Standards.NACE2, "58.11")),
        ((Standards.NACEBEL2008, "58120"), (Standards.NACE2, "58.12")),
        ((Standards.NACEBEL2008, "58130"), (Standards.NACE2, "58.13")),
        ((Standards.NACEBEL2008, "58140"), (Standards.NACE2, "58.14")),
        ((Standards.NACEBEL2008, "58190"), (Standards.NACE2, "58.19")),
        ((Standards.NACEBEL2008, "18110"), (Standards.NACE2, "18.11")),
        ((Standards.NACEBEL2008, "18140"), (Standards.NACE2, "18.14")),
        ((Standards.NACEBEL2008, "18130"), (Standards.NACE2, "18.13")),
        ((Standards.NACEBEL2008, "18200"), (Standards.NACE2, "18.20")),
        ((Standards.NACEBEL2008, "19100"), (Standards.NACE2, "19.10")),
        ((Standards.NACEBEL2008, "20130"), (Standards.NACE2, "20.13")),
        ((Standards.NACEBEL2008, "24460"), (Standards.NACE2, "24.46")),
        ((Standards.NACEBEL2008, "20110"), (Standards.NACE2, "20.11")),
        ((Standards.NACEBEL2008, "20120"), (Standards.NACE2, "20.12")),
        ((Standards.NACEBEL2008, "20150"), (Standards.NACE2, "20.15")),
        ((Standards.NACEBEL2008, "20160"), (Standards.NACE2, "20.16")),
        ((Standards.NACEBEL2008, "20170"), (Standards.NACE2, "20.17")),
        ((Standards.NACEBEL2008, "20200"), (Standards.NACE2, "20.20")),
        ((Standards.NACEBEL2008, "20300"), (Standards.NACE2, "20.30")),
        ((Standards.NACEBEL2008, "21100"), (Standards.NACE2, "21.10")),
        ((Standards.NACEBEL2008, "20420"), (Standards.NACE2, "20.42")),
        ((Standards.NACEBEL2008, "20510"), (Standards.NACE2, "20.51")),
        ((Standards.NACEBEL2008, "20520"), (Standards.NACE2, "20.52")),
        ((Standards.NACEBEL2008, "20590"), (Standards.NACE2, "20.59")),
        ((Standards.NACEBEL2008, "20530"), (Standards.NACE2, "20.53")),
        ((Standards.NACEBEL2008, "26800"), (Standards.NACE2, "26.80")),
        ((Standards.NACEBEL2008, "26110"), (Standards.NACE2, "26.11")),
        ((Standards.NACEBEL2008, "20600"), (Standards.NACE2, "20.60")),
        ((Standards.NACEBEL2008, "22110"), (Standards.NACE2, "22.11")),
        ((Standards.NACEBEL2008, "22210"), (Standards.NACE2, "22.21")),
        ((Standards.NACEBEL2008, "33200"), (Standards.NACE2, "33.20")),
        ((Standards.NACEBEL2008, "22220"), (Standards.NACE2, "22.22")),
        ((Standards.NACEBEL2008, "22230"), (Standards.NACE2, "22.23")),
        ((Standards.NACEBEL2008, "27330"), (Standards.NACE2, "27.33")),
        ((Standards.NACEBEL2008, "23110"), (Standards.NACE2, "23.11")),
        ((Standards.NACEBEL2008, "23120"), (Standards.NACE2, "23.12")),
        ((Standards.NACEBEL2008, "23130"), (Standards.NACE2, "23.13")),
        ((Standards.NACEBEL2008, "23140"), (Standards.NACE2, "23.14")),
        ((Standards.NACEBEL2008, "23190"), (Standards.NACE2, "23.19")),
        ((Standards.NACEBEL2008, "23410"), (Standards.NACE2, "23.41")),
        ((Standards.NACEBEL2008, "23420"), (Standards.NACE2, "23.42")),
        ((Standards.NACEBEL2008, "23430"), (Standards.NACE2, "23.43")),
        ((Standards.NACEBEL2008, "23440"), (Standards.NACE2, "23.44")),
        ((Standards.NACEBEL2008, "23490"), (Standards.NACE2, "23.49")),
        ((Standards.NACEBEL2008, "23200"), (Standards.NACE2, "23.20")),
        ((Standards.NACEBEL2008, "23310"), (Standards.NACE2, "23.31")),
        ((Standards.NACEBEL2008, "23510"), (Standards.NACE2, "23.51")),
        ((Standards.NACEBEL2008, "23520"), (Standards.NACE2, "23.52")),
        ((Standards.NACEBEL2008, "23610"), (Standards.NACE2, "23.61")),
        ((Standards.NACEBEL2008, "23620"), (Standards.NACE2, "23.62")),
        ((Standards.NACEBEL2008, "23630"), (Standards.NACE2, "23.63")),
        ((Standards.NACEBEL2008, "23640"), (Standards.NACE2, "23.64")),
        ((Standards.NACEBEL2008, "23650"), (Standards.NACE2, "23.65")),
        ((Standards.NACEBEL2008, "23690"), (Standards.NACE2, "23.69")),
        ((Standards.NACEBEL2008, "23700"), (Standards.NACE2, "23.70")),
        ((Standards.NACEBEL2008, "23910"), (Standards.NACE2, "23.91")),
        ((Standards.NACEBEL2008, "23990"), (Standards.NACE2, "23.99")),
        ((Standards.NACEBEL2008, "24100"), (Standards.NACE2, "24.10")),
        ((Standards.NACEBEL2008, "24510"), (Standards.NACE2, "24.51")),
        ((Standards.NACEBEL2008, "24520"), (Standards.NACE2, "24.52")),
        ((Standards.NACEBEL2008, "24410"), (Standards.NACE2, "24.41")),
        ((Standards.NACEBEL2008, "24200"), (Standards.NACE2, "24.20")),
        ((Standards.NACEBEL2008, "24310"), (Standards.NACE2, "24.31")),
        ((Standards.NACEBEL2008, "24320"), (Standards.NACE2, "24.32")),
        ((Standards.NACEBEL2008, "24330"), (Standards.NACE2, "24.33")),
        ((Standards.NACEBEL2008, "24340"), (Standards.NACE2, "24.34")),
        ((Standards.NACEBEL2008, "24420"), (Standards.NACE2, "24.42")),
        ((Standards.NACEBEL2008, "24430"), (Standards.NACE2, "24.43")),
        ((Standards.NACEBEL2008, "24440"), (Standards.NACE2, "24.44")),
        ((Standards.NACEBEL2008, "24450"), (Standards.NACE2, "24.45")),
        ((Standards.NACEBEL2008, "24530"), (Standards.NACE2, "24.53")),
        ((Standards.NACEBEL2008, "24540"), (Standards.NACE2, "24.54")),
        ((Standards.NACEBEL2008, "25110"), (Standards.NACE2, "25.11")),
        ((Standards.NACEBEL2008, "33110"), (Standards.NACE2, "33.11")),
        ((Standards.NACEBEL2008, "25120"), (Standards.NACE2, "25.12")),
        ((Standards.NACEBEL2008, "25290"), (Standards.NACE2, "25.29")),
        ((Standards.NACEBEL2008, "25210"), (Standards.NACE2, "25.21")),
        ((Standards.NACEBEL2008, "25300"), (Standards.NACE2, "25.30")),
        ((Standards.NACEBEL2008, "25610"), (Standards.NACE2, "25.61")),
        ((Standards.NACEBEL2008, "25620"), (Standards.NACE2, "25.62")),
        ((Standards.NACEBEL2008, "25710"), (Standards.NACE2, "25.71")),
        ((Standards.NACEBEL2008, "28410"), (Standards.NACE2, "28.41")),
        ((Standards.NACEBEL2008, "28490"), (Standards.NACE2, "28.49")),
        ((Standards.NACEBEL2008, "28920"), (Standards.NACE2, "28.92")),
        ((Standards.NACEBEL2008, "25720"), (Standards.NACE2, "25.72")),
        ((Standards.NACEBEL2008, "25910"), (Standards.NACE2, "25.91")),
        ((Standards.NACEBEL2008, "25920"), (Standards.NACE2, "25.92")),
        ((Standards.NACEBEL2008, "25930"), (Standards.NACE2, "25.93")),
        ((Standards.NACEBEL2008, "25940"), (Standards.NACE2, "25.94")),
        ((Standards.NACEBEL2008, "28110"), (Standards.NACE2, "28.11")),
        ((Standards.NACEBEL2008, "27110"), (Standards.NACE2, "27.11")),
        ((Standards.NACEBEL2008, "33120"), (Standards.NACE2, "33.12")),
        ((Standards.NACEBEL2008, "28120"), (Standards.NACE2, "28.12")),
        ((Standards.NACEBEL2008, "28130"), (Standards.NACE2, "28.13")),
        ((Standards.NACEBEL2008, "28140"), (Standards.NACE2, "28.14")),
        ((Standards.NACEBEL2008, "28150"), (Standards.NACE2, "28.15")),
        ((Standards.NACEBEL2008, "28210"), (Standards.NACE2, "28.21")),
        ((Standards.NACEBEL2008, "28220"), (Standards.NACE2, "28.22")),
        ((Standards.NACEBEL2008, "28250"), (Standards.NACE2, "28.25")),
        ((Standards.NACEBEL2008, "33130"), (Standards.NACE2, "33.13")),
        ((Standards.NACEBEL2008, "28300"), (Standards.NACE2, "28.30")),
        ((Standards.NACEBEL2008, "95220"), (Standards.NACE2, "95.22")),
        ((Standards.NACEBEL2008, "28240"), (Standards.NACE2, "28.24")),
        ((Standards.NACEBEL2008, "27900"), (Standards.NACE2, "27.90")),
        ((Standards.NACEBEL2008, "33140"), (Standards.NACE2, "33.14")),
        ((Standards.NACEBEL2008, "28910"), (Standards.NACE2, "28.91")),
        ((Standards.NACEBEL2008, "28930"), (Standards.NACE2, "28.93")),
        ((Standards.NACEBEL2008, "28940"), (Standards.NACE2, "28.94")),
        ((Standards.NACEBEL2008, "28950"), (Standards.NACE2, "28.95")),
        ((Standards.NACEBEL2008, "28990"), (Standards.NACE2, "28.99")),
        ((Standards.NACEBEL2008, "28960"), (Standards.NACE2, "28.96")),
        ((Standards.NACEBEL2008, "25400"), (Standards.NACE2, "25.40")),
        ((Standards.NACEBEL2008, "30300"), (Standards.NACE2, "30.30")),
        ((Standards.NACEBEL2008, "30400"), (Standards.NACE2, "30.40")),
        ((Standards.NACEBEL2008, "33160"), (Standards.NACE2, "33.16")),
        ((Standards.NACEBEL2008, "27510"), (Standards.NACE2, "27.51")),
        ((Standards.NACEBEL2008, "27520"), (Standards.NACE2, "27.52")),
        ((Standards.NACEBEL2008, "28230"), (Standards.NACE2, "28.23")),
        ((Standards.NACEBEL2008, "26200"), (Standards.NACE2, "26.20")),
        ((Standards.NACEBEL2008, "62090"), (Standards.NACE2, "62.09")),
        ((Standards.NACEBEL2008, "27120"), (Standards.NACE2, "27.12")),
        ((Standards.NACEBEL2008, "27320"), (Standards.NACE2, "27.32")),
        ((Standards.NACEBEL2008, "27310"), (Standards.NACE2, "27.31")),
        ((Standards.NACEBEL2008, "27200"), (Standards.NACE2, "27.20")),
        ((Standards.NACEBEL2008, "29310"), (Standards.NACE2, "29.31")),
        ((Standards.NACEBEL2008, "26300"), (Standards.NACE2, "26.30")),
        ((Standards.NACEBEL2008, "30200"), (Standards.NACE2, "30.20")),
        ((Standards.NACEBEL2008, "26510"), (Standards.NACE2, "26.51")),
        ((Standards.NACEBEL2008, "26120"), (Standards.NACE2, "26.12")),
        ((Standards.NACEBEL2008, "95120"), (Standards.NACE2, "95.12")),
        ((Standards.NACEBEL2008, "26400"), (Standards.NACE2, "26.40")),
        ((Standards.NACEBEL2008, "26600"), (Standards.NACE2, "26.60")),
        ((Standards.NACEBEL2008, "26700"), (Standards.NACE2, "26.70")),
        ((Standards.NACEBEL2008, "26520"), (Standards.NACE2, "26.52")),
        ((Standards.NACEBEL2008, "32130"), (Standards.NACE2, "32.13")),
        ((Standards.NACEBEL2008, "29100"), (Standards.NACE2, "29.10")),
        ((Standards.NACEBEL2008, "30910"), (Standards.NACE2, "30.91")),
        ((Standards.NACEBEL2008, "29320"), (Standards.NACE2, "29.32")),
        ((Standards.NACEBEL2008, "33150"), (Standards.NACE2, "33.15")),
        ((Standards.NACEBEL2008, "30110"), (Standards.NACE2, "30.11")),
        ((Standards.NACEBEL2008, "30120"), (Standards.NACE2, "30.12")),
        ((Standards.NACEBEL2008, "33170"), (Standards.NACE2, "33.17")),
        ((Standards.NACEBEL2008, "30920"), (Standards.NACE2, "30.92")),
        ((Standards.NACEBEL2008, "30990"), (Standards.NACE2, "30.99")),
        ((Standards.NACEBEL2008, "31010"), (Standards.NACE2, "31.01")),
        ((Standards.NACEBEL2008, "31020"), (Standards.NACE2, "31.02")),
        ((Standards.NACEBEL2008, "95240"), (Standards.NACE2, "95.24")),
        ((Standards.NACEBEL2008, "31030"), (Standards.NACE2, "31.03")),
        ((Standards.NACEBEL2008, "32110"), (Standards.NACE2, "32.11")),
        ((Standards.NACEBEL2008, "32200"), (Standards.NACE2, "32.20")),
        ((Standards.NACEBEL2008, "32300"), (Standards.NACE2, "32.30")),
        ((Standards.NACEBEL2008, "32400"), (Standards.NACE2, "32.40")),
        ((Standards.NACEBEL2008, "32910"), (Standards.NACE2, "32.91")),
        ((Standards.NACEBEL2008, "38310"), (Standards.NACE2, "38.31")),
        ((Standards.NACEBEL2008, "35140"), (Standards.NACE2, "35.14")),
        ((Standards.NACEBEL2008, "35110"), (Standards.NACE2, "35.11")),
        ((Standards.NACEBEL2008, "35120"), (Standards.NACE2, "35.12")),
        ((Standards.NACEBEL2008, "38120"), (Standards.NACE2, "38.12")),
        ((Standards.NACEBEL2008, "35130"), (Standards.NACE2, "35.13")),
        ((Standards.NACEBEL2008, "35220"), (Standards.NACE2, "35.22")),
        ((Standards.NACEBEL2008, "35210"), (Standards.NACE2, "35.21")),
        ((Standards.NACEBEL2008, "35230"), (Standards.NACE2, "35.23")),
        ((Standards.NACEBEL2008, "35300"), (Standards.NACE2, "35.30")),
        ((Standards.NACEBEL2008, "36000"), (Standards.NACE2, "36.00")),
        ((Standards.NACEBEL2008, "43110"), (Standards.NACE2, "43.11")),
        ((Standards.NACEBEL2008, "43120"), (Standards.NACE2, "43.12")),
        ((Standards.NACEBEL2008, "43130"), (Standards.NACE2, "43.13")),
        ((Standards.NACEBEL2008, "42990"), (Standards.NACE2, "42.99")),
        ((Standards.NACEBEL2008, "42130"), (Standards.NACE2, "42.13")),
        ((Standards.NACEBEL2008, "42220"), (Standards.NACE2, "42.22")),
        ((Standards.NACEBEL2008, "43910"), (Standards.NACE2, "43.91")),
        ((Standards.NACEBEL2008, "42110"), (Standards.NACE2, "42.11")),
        ((Standards.NACEBEL2008, "42120"), (Standards.NACE2, "42.12")),
        ((Standards.NACEBEL2008, "80200"), (Standards.NACE2, "80.20")),
        ((Standards.NACEBEL2008, "43310"), (Standards.NACE2, "43.31")),
        ((Standards.NACEBEL2008, "43390"), (Standards.NACE2, "43.39")),
        ((Standards.NACEBEL2008, "45310"), (Standards.NACE2, "45.31")),
        ((Standards.NACEBEL2008, "45320"), (Standards.NACE2, "45.32")),
        ((Standards.NACEBEL2008, "47300"), (Standards.NACE2, "47.30")),
        ((Standards.NACEBEL2008, "46110"), (Standards.NACE2, "46.11")),
        ((Standards.NACEBEL2008, "46120"), (Standards.NACE2, "46.12")),
        ((Standards.NACEBEL2008, "46130"), (Standards.NACE2, "46.13")),
        ((Standards.NACEBEL2008, "46140"), (Standards.NACE2, "46.14")),
        ((Standards.NACEBEL2008, "46150"), (Standards.NACE2, "46.15")),
        ((Standards.NACEBEL2008, "46160"), (Standards.NACE2, "46.16")),
        ((Standards.NACEBEL2008, "46170"), (Standards.NACE2, "46.17")),
        ((Standards.NACEBEL2008, "46180"), (Standards.NACE2, "46.18")),
        ((Standards.NACEBEL2008, "46190"), (Standards.NACE2, "46.19")),
        ((Standards.NACEBEL2008, "46220"), (Standards.NACE2, "46.22")),
        ((Standards.NACEBEL2008, "46240"), (Standards.NACE2, "46.24")),
        ((Standards.NACEBEL2008, "46350"), (Standards.NACE2, "46.35")),
        ((Standards.NACEBEL2008, "46360"), (Standards.NACE2, "46.36")),
        ((Standards.NACEBEL2008, "46370"), (Standards.NACE2, "46.37")),
        ((Standards.NACEBEL2008, "46520"), (Standards.NACE2, "46.52")),
        ((Standards.NACEBEL2008, "46450"), (Standards.NACE2, "46.45")),
        ((Standards.NACEBEL2008, "46460"), (Standards.NACE2, "46.46")),
        ((Standards.NACEBEL2008, "46480"), (Standards.NACE2, "46.48")),
        ((Standards.NACEBEL2008, "46710"), (Standards.NACE2, "46.71")),
        ((Standards.NACEBEL2008, "46720"), (Standards.NACE2, "46.72")),
        ((Standards.NACEBEL2008, "46620"), (Standards.NACE2, "46.62")),
        ((Standards.NACEBEL2008, "46630"), (Standards.NACE2, "46.63")),
        ((Standards.NACEBEL2008, "46640"), (Standards.NACE2, "46.64")),
        ((Standards.NACEBEL2008, "46510"), (Standards.NACE2, "46.51")),
        ((Standards.NACEBEL2008, "46660"), (Standards.NACE2, "46.66")),
        ((Standards.NACEBEL2008, "46650"), (Standards.NACE2, "46.65")),
        ((Standards.NACEBEL2008, "46610"), (Standards.NACE2, "46.61")),
        ((Standards.NACEBEL2008, "46900"), (Standards.NACE2, "46.90")),
        ((Standards.NACEBEL2008, "47210"), (Standards.NACE2, "47.21")),
        ((Standards.NACEBEL2008, "47230"), (Standards.NACE2, "47.23")),
        ((Standards.NACEBEL2008, "47260"), (Standards.NACE2, "47.26")),
        ((Standards.NACEBEL2008, "47730"), (Standards.NACE2, "47.73")),
        ((Standards.NACEBEL2008, "47740"), (Standards.NACE2, "47.74")),
        ((Standards.NACEBEL2008, "47750"), (Standards.NACE2, "47.75")),
        ((Standards.NACEBEL2008, "47530"), (Standards.NACE2, "47.53")),
        ((Standards.NACEBEL2008, "47540"), (Standards.NACE2, "47.54")),
        ((Standards.NACEBEL2008, "47430"), (Standards.NACE2, "47.43")),
        ((Standards.NACEBEL2008, "47630"), (Standards.NACE2, "47.63")),
        ((Standards.NACEBEL2008, "47620"), (Standards.NACE2, "47.62")),
        ((Standards.NACEBEL2008, "47610"), (Standards.NACE2, "47.61")),
        ((Standards.NACEBEL2008, "47640"), (Standards.NACE2, "47.64")),
        ((Standards.NACEBEL2008, "47770"), (Standards.NACE2, "47.77")),
        ((Standards.NACEBEL2008, "47410"), (Standards.NACE2, "47.41")),
        ((Standards.NACEBEL2008, "47420"), (Standards.NACE2, "47.42")),
        ((Standards.NACEBEL2008, "47650"), (Standards.NACE2, "47.65")),
        ((Standards.NACEBEL2008, "47910"), (Standards.NACE2, "47.91")),
        ((Standards.NACEBEL2008, "47810"), (Standards.NACE2, "47.81")),
        ((Standards.NACEBEL2008, "47820"), (Standards.NACE2, "47.82")),
        ((Standards.NACEBEL2008, "47890"), (Standards.NACE2, "47.89")),
        ((Standards.NACEBEL2008, "47990"), (Standards.NACE2, "47.99")),
        ((Standards.NACEBEL2008, "95230"), (Standards.NACE2, "95.23")),
        ((Standards.NACEBEL2008, "95210"), (Standards.NACE2, "95.21")),
        ((Standards.NACEBEL2008, "95250"), (Standards.NACE2, "95.25")),
        ((Standards.NACEBEL2008, "55100"), (Standards.NACE2, "55.10")),
        ((Standards.NACEBEL2008, "55300"), (Standards.NACE2, "55.30")),
        ((Standards.NACEBEL2008, "55900"), (Standards.NACE2, "55.90")),
        ((Standards.NACEBEL2008, "56290"), (Standards.NACE2, "56.29")),
        ((Standards.NACEBEL2008, "56210"), (Standards.NACE2, "56.21")),
        ((Standards.NACEBEL2008, "49200"), (Standards.NACE2, "49.20")),
        ((Standards.NACEBEL2008, "49100"), (Standards.NACE2, "49.10")),
        ((Standards.NACEBEL2008, "49310"), (Standards.NACE2, "49.31")),
        ((Standards.NACEBEL2008, "49390"), (Standards.NACE2, "49.39")),
        ((Standards.NACEBEL2008, "49320"), (Standards.NACE2, "49.32")),
        ((Standards.NACEBEL2008, "49420"), (Standards.NACE2, "49.42")),
        ((Standards.NACEBEL2008, "49410"), (Standards.NACE2, "49.41")),
        ((Standards.NACEBEL2008, "49500"), (Standards.NACE2, "49.50")),
        ((Standards.NACEBEL2008, "50200"), (Standards.NACE2, "50.20")),
        ((Standards.NACEBEL2008, "50100"), (Standards.NACE2, "50.10")),
        ((Standards.NACEBEL2008, "50400"), (Standards.NACE2, "50.40")),
        ((Standards.NACEBEL2008, "50300"), (Standards.NACE2, "50.30")),
        ((Standards.NACEBEL2008, "51100"), (Standards.NACE2, "51.10")),
        ((Standards.NACEBEL2008, "51210"), (Standards.NACE2, "51.21")),
        ((Standards.NACEBEL2008, "51220"), (Standards.NACE2, "51.22")),
        ((Standards.NACEBEL2008, "52100"), (Standards.NACE2, "52.10")),
        ((Standards.NACEBEL2008, "52230"), (Standards.NACE2, "52.23")),
        ((Standards.NACEBEL2008, "79110"), (Standards.NACE2, "79.11")),
        ((Standards.NACEBEL2008, "79120"), (Standards.NACE2, "79.12")),
        ((Standards.NACEBEL2008, "52290"), (Standards.NACE2, "52.29")),
        ((Standards.NACEBEL2008, "53100"), (Standards.NACE2, "53.10")),
        ((Standards.NACEBEL2008, "82190"), (Standards.NACE2, "82.19")),
        ((Standards.NACEBEL2008, "53200"), (Standards.NACE2, "53.20")),
        ((Standards.NACEBEL2008, "61200"), (Standards.NACE2, "61.20")),
        ((Standards.NACEBEL2008, "60200"), (Standards.NACE2, "60.20")),
        ((Standards.NACEBEL2008, "61100"), (Standards.NACE2, "61.10")),
        ((Standards.NACEBEL2008, "61300"), (Standards.NACE2, "61.30")),
        ((Standards.NACEBEL2008, "61900"), (Standards.NACE2, "61.90")),
        ((Standards.NACEBEL2008, "64110"), (Standards.NACE2, "64.11")),
        ((Standards.NACEBEL2008, "64190"), (Standards.NACE2, "64.19")),
        ((Standards.NACEBEL2008, "64910"), (Standards.NACE2, "64.91")),
        ((Standards.NACEBEL2008, "64200"), (Standards.NACE2, "64.20")),
        ((Standards.NACEBEL2008, "64300"), (Standards.NACE2, "64.30")),
        ((Standards.NACEBEL2008, "65200"), (Standards.NACE2, "65.20")),
        ((Standards.NACEBEL2008, "65300"), (Standards.NACE2, "65.30")),
        ((Standards.NACEBEL2008, "66110"), (Standards.NACE2, "66.11")),
        ((Standards.NACEBEL2008, "66120"), (Standards.NACE2, "66.12")),
        ((Standards.NACEBEL2008, "66300"), (Standards.NACE2, "66.30")),
        ((Standards.NACEBEL2008, "66220"), (Standards.NACE2, "66.22")),
        ((Standards.NACEBEL2008, "66210"), (Standards.NACE2, "66.21")),
        ((Standards.NACEBEL2008, "66290"), (Standards.NACE2, "66.29")),
        ((Standards.NACEBEL2008, "68100"), (Standards.NACE2, "68.10")),
        ((Standards.NACEBEL2008, "81100"), (Standards.NACE2, "81.10")),
        ((Standards.NACEBEL2008, "77110"), (Standards.NACE2, "77.11")),
        ((Standards.NACEBEL2008, "77120"), (Standards.NACE2, "77.12")),
        ((Standards.NACEBEL2008, "77340"), (Standards.NACE2, "77.34")),
        ((Standards.NACEBEL2008, "77350"), (Standards.NACE2, "77.35")),
        ((Standards.NACEBEL2008, "77310"), (Standards.NACE2, "77.31")),
        ((Standards.NACEBEL2008, "77320"), (Standards.NACE2, "77.32")),
        ((Standards.NACEBEL2008, "77330"), (Standards.NACE2, "77.33")),
        ((Standards.NACEBEL2008, "77220"), (Standards.NACE2, "77.22")),
        ((Standards.NACEBEL2008, "77210"), (Standards.NACE2, "77.21")),
        ((Standards.NACEBEL2008, "62020"), (Standards.NACE2, "62.02")),
        ((Standards.NACEBEL2008, "62010"), (Standards.NACE2, "62.01")),
        ((Standards.NACEBEL2008, "58290"), (Standards.NACE2, "58.29")),
        ((Standards.NACEBEL2008, "58210"), (Standards.NACE2, "58.21")),
        ((Standards.NACEBEL2008, "63110"), (Standards.NACE2, "63.11")),
        ((Standards.NACEBEL2008, "62030"), (Standards.NACE2, "62.03")),
        ((Standards.NACEBEL2008, "60100"), (Standards.NACE2, "60.10")),
        ((Standards.NACEBEL2008, "63120"), (Standards.NACE2, "63.12")),
        ((Standards.NACEBEL2008, "95110"), (Standards.NACE2, "95.11")),
        ((Standards.NACEBEL2008, "72190"), (Standards.NACE2, "72.19")),
        ((Standards.NACEBEL2008, "72110"), (Standards.NACE2, "72.11")),
        ((Standards.NACEBEL2008, "72200"), (Standards.NACE2, "72.20")),
        ((Standards.NACEBEL2008, "73200"), (Standards.NACE2, "73.20")),
        ((Standards.NACEBEL2008, "70210"), (Standards.NACE2, "70.21")),
        ((Standards.NACEBEL2008, "70220"), (Standards.NACE2, "70.22")),
        ((Standards.NACEBEL2008, "70100"), (Standards.NACE2, "70.10")),
        ((Standards.NACEBEL2008, "73110"), (Standards.NACE2, "73.11")),
        ((Standards.NACEBEL2008, "73120"), (Standards.NACE2, "73.12")),
        ((Standards.NACEBEL2008, "78100"), (Standards.NACE2, "78.10")),
        ((Standards.NACEBEL2008, "78200"), (Standards.NACE2, "78.20")),
        ((Standards.NACEBEL2008, "78300"), (Standards.NACE2, "78.30")),
        ((Standards.NACEBEL2008, "80100"), (Standards.NACE2, "80.10")),
        ((Standards.NACEBEL2008, "80300"), (Standards.NACE2, "80.30")),
        ((Standards.NACEBEL2008, "81220"), (Standards.NACE2, "81.22")),
        ((Standards.NACEBEL2008, "81210"), (Standards.NACE2, "81.21")),
        ((Standards.NACEBEL2008, "81290"), (Standards.NACE2, "81.29")),
        ((Standards.NACEBEL2008, "82200"), (Standards.NACE2, "82.20")),
        ((Standards.NACEBEL2008, "74300"), (Standards.NACE2, "74.30")),
        ((Standards.NACEBEL2008, "82110"), (Standards.NACE2, "82.11")),
        ((Standards.NACEBEL2008, "82300"), (Standards.NACE2, "82.30")),
        ((Standards.NACEBEL2008, "82910"), (Standards.NACE2, "82.91")),
        ((Standards.NACEBEL2008, "82990"), (Standards.NACE2, "82.99")),
        ((Standards.NACEBEL2008, "63990"), (Standards.NACE2, "63.99")),
        ((Standards.NACEBEL2008, "77400"), (Standards.NACE2, "77.40")),
        ((Standards.NACEBEL2008, "84120"), (Standards.NACE2, "84.12")),
        ((Standards.NACEBEL2008, "84130"), (Standards.NACE2, "84.13")),
        ((Standards.NACEBEL2008, "84210"), (Standards.NACE2, "84.21")),
        ((Standards.NACEBEL2008, "84220"), (Standards.NACE2, "84.22")),
        ((Standards.NACEBEL2008, "84250"), (Standards.NACE2, "84.25")),
        ((Standards.NACEBEL2008, "85410"), (Standards.NACE2, "85.41")),
        ((Standards.NACEBEL2008, "85520"), (Standards.NACE2, "85.52")),
        ((Standards.NACEBEL2008, "86220"), (Standards.NACE2, "86.22")),
        ((Standards.NACEBEL2008, "86210"), (Standards.NACE2, "86.21")),
        ((Standards.NACEBEL2008, "86230"), (Standards.NACE2, "86.23")),
        ((Standards.NACEBEL2008, "75000"), (Standards.NACE2, "75.00")),
        ((Standards.NACEBEL2008, "37000"), (Standards.NACE2, "37.00")),
        ((Standards.NACEBEL2008, "38110"), (Standards.NACE2, "38.11")),
        ((Standards.NACEBEL2008, "39000"), (Standards.NACE2, "39.00")),
        ((Standards.NACEBEL2008, "94110"), (Standards.NACE2, "94.11")),
        ((Standards.NACEBEL2008, "94120"), (Standards.NACE2, "94.12")),
        ((Standards.NACEBEL2008, "94200"), (Standards.NACE2, "94.20")),
        ((Standards.NACEBEL2008, "94910"), (Standards.NACE2, "94.91")),
        ((Standards.NACEBEL2008, "94920"), (Standards.NACE2, "94.92")),
        ((Standards.NACEBEL2008, "59120"), (Standards.NACE2, "59.12")),
        ((Standards.NACEBEL2008, "59130"), (Standards.NACE2, "59.13")),
        ((Standards.NACEBEL2008, "59140"), (Standards.NACE2, "59.14")),
        ((Standards.NACEBEL2008, "63910"), (Standards.NACE2, "63.91")),
        ((Standards.NACEBEL2008, "91030"), (Standards.NACE2, "91.03")),
        ((Standards.NACEBEL2008, "91020"), (Standards.NACE2, "91.02")),
        ((Standards.NACEBEL2008, "93110"), (Standards.NACE2, "93.11")),
        ((Standards.NACEBEL2008, "93130"), (Standards.NACE2, "93.13")),
        ((Standards.NACEBEL2008, "85510"), (Standards.NACE2, "85.51")),
        ((Standards.NACEBEL2008, "92000"), (Standards.NACE2, "92.00")),
        ((Standards.NACEBEL2008, "96040"), (Standards.NACE2, "96.04")),
        ((Standards.NACEBEL2008, "97000"), (Standards.NACE2, "97.00")),
        ((Standards.NACEBEL2008, "98100"), (Standards.NACE2, "98.10")),
        ((Standards.NACEBEL2008, "98200"), (Standards.NACE2, "98.20")),
        ((Standards.NACEBEL2008, "99000"), (Standards.NACE2, "99.00")),
    ],
)
