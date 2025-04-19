===================================
ATC teorie
===================================

Tabulka obsahů
===================================
#. :ref:`Sources`

.. _Sources:
Použité zdroje pro tento projekt
============

Aby tento projekt fungoval v souladu s právními předpisy ATC. následující zdroje byly použity.
Mějte na paměti, že některé aspekty musely být trochu změněny, aby se vývoj usnadnil (hlasování, ultrazvukové přijetí kategorie, atd.).
V budoucnu by ideální stav projektu byl, že software bude v souladu se všemi pravidly ATC týkající se většiny regionů (ICAO a FAA se někdy liší ve svých předpisech).
Ale vězte, že to bude trvat nějakou dobu, než se k tomuto cíli přiblížíme.

.. list-table:: List of used ATC sources

    * - **Name**
      - **Publisher**
      - **Link**
      - **Used for**
    * - **Glossary**
      -
      -
      -
    * - *All-Clear? ICAO Standard Phraseology*
      - ICAO
      - `Skybrary <https://skybrary.aero/sites/default/files/bookshelf/115.pdf>`_
      - Phraseology used in this ATC simulator
    * - *Say Again? Phraseology Database*
      - EUROCONTROL
      - `eurocontrol contentzone <https://contentzone.eurocontrol.int/phraseology/>`_
      - Phraseology used in this ATC simulator
    * - *Aeronautical phraseology and terminology*
      - AIM CZ
      - `Aeronautical information service of CZ <https://aim.rlp.cz/predpisy/predpisy/dokumenty/L/L-Frazeologie/data/print/Frazeologie_cely.pdf>`_
      - Phraseology used in this ATC simulator
    * - **ATC basics**
      -
      -
      -
    * - *Skybrary articles*
      - Skybrary
      - `Skybrary website <https://skybrary.aero/>`_
      - Used for implementation of basic ATC principles
    * - *Article 2*
      - UK Civil Aviation Authority
      - `caa.co.uk article 2 definitions <https://regulatorylibrary.caa.co.uk/965-2012/Content/Regs/00040_art._2_Definitions.htm>`_
      - For implementing aircraft classes
    * - **ATC environment**
      -
      -
      -
    * - *FAA PHAK*
      - FAA
      - `faa.gov <https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak>`_
      - Pilot's Handbook of Aeronautical Knowledge was used for implementing plane movement
    * - *Boeing 737 Characteristics for Airport Planning*
      - Boeing
      - `boeing.com <https://www.boeing.com/content/dam/boeing/boeingdotcom/commercial/airports/acaps/737_RevA.pdf>`_
      - Technical details and variables of Boeing 737 plane *
    * - **Others**
      -
      -
      -
    * - *ICAO APIRG*
      - ICAO
      - `icao.int <https://www.icao.int/wacaf/documents/apirg/sg/2010/afi_opmet_mtf2/docs/wp08.pdf>`_
      - AFI OPMET database catalogue was used for assigning ICAO codes to airports in simulator

\* Simulace v současné době vypočítá celý pohyb na základě hodnot z letadla B737-800. Tento letoun byl vybrán proto, že měl otevřené technické údaje a také proto, že byl jedním z nejvíce používaných komerčních letadel.
V budoucnu se to určitě změní a simulátor bude podporovat více letadel, aby simulace byla více rozmanitá.
