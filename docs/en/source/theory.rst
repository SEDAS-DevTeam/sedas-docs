===================================
ATC theory
===================================

Table of contents
===================================
#. :ref:`Sources`

.. _Sources:
Used sources for this project
============

In order to make this project functional according to ATC legislation. Following sources were used.
Be aware that some aspects had to be changed a little bit, to make the development more easier (callsigns, ultralight category acceptance, etc.).
In the future, the ideal state of the project would be that the software would be compliant to all ATC rules regarding most of the regions (ICAO and FAA sometimes differ in their regulations).
But be aware that this is going to take a time before we approach this goal.

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

.. note::
    \* Currently, simulation calculates all the movement based on the values from B737-800 plane. This plane was chosen because it had open technical data and also because it was one of the most used commercial planes.
    In future, this is definitely going to change and the simulator will be supporting more planes to make simulation more diverse