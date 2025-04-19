===================
Technické pozadí
===================

Tabulka obsahů
===================================
#. :ref:`Technologies`
#. :ref:`Project`
#. :ref:`Schematic`
#. :ref:`Neural networks`
#. :ref:`Calculations`

.. _Technologies:
Použité technologie
============

Samotná aplikace používá mnoho technologií k implementaci mnoha jejích částí. Například používá lokální komunikaci souborů pro komunikaci mezi hlavním aplikací a modulem AI. Tato stránka se pokusí vysvětlit všechny technické přístupy, které byly použity v rozvoji.

.. list-table:: List of used technologies
    :widths: 40 60

    * - **Used tech**
        - **Explanation**
    * - **App**
        - 
    * - ``ElectronJS``
        - Main backend for app behavior
    * - ``NodeJS``
        - Main code runtime
    * - ``Typescript``
        - Language used for backend
    * - ``node-addon-api/C++``
        - Used for resource intensive computations
    * - **AI module**
        - 
    * - ``Whisper``
        - ASR \*
    * - ``Rule-based NLP (regex, if-else)``
        - NLP \*
    * - ``VITS``
        - TTS \*
    * - ``Whisper.cpp``
        - Inference for Whisper model
    * - ``PiperTTS``
        - Inference for VITS model

\* **ASR** - Automatic Speech Recognition

\* **NLP** - Natural Language Processing

\* **TTS** - Text To Speech synthesis

.. _Project:
Schéma projektu
============

Samotný projekt je rozdělen do několika odvětví a struktur, takže by to bylo modulární a snadné rozšířit.
V současné době používá mnoho technologií / poskytovatelů pro dokumentaci a verze, například: **Huggingface** (Repository pro SEDAS-whisper model váhy, `link <https://huggingface.co/HelloWorld7894/SEDAS-whisper>`_), **Github** (Repository a organizační stránka pro celý SEDAS ekosystém `link <https://github.com/SEDAS-DevTeam>`_), **ReadTheDocs** (Hostování dokumentace pro celý projekt).
Celý kód je 100% open-source a každá jeho část je k dispozici na organizační stránce GitHub.

.. figure:: imgs/schema/project_structure.png

    Hlavní projekty SEDAS a jejich verze

.. _Schematic:
Schéma aplikace
============

.. image:: imgs/schema/backend_structure.png

Samotná aplikace je rozdělena do několika modulů, které jsou propojeny pomocí několika komunikačních mechanismů (viz níže):

* **IPC** (**I**\ nter **P**\ rocess **C**\ ommunication) - A protocol for the communication between frontend and backend. This is a very important communication mechanism, because it allows app to send signals to backend when they are triggered in user GUI and vice versa.

* **Worker threads** - This allows app to utilize its nonblocking architecture. These are primarily implemented in simulation time management, backup saving. Primarily this is used in methods, that could potentialy take a lot of time and block the app from responding properly.

* **MSC** (**M**\ odule **S**\ ocket **C**\ ommunication) - A protocol that is implemented in the communication between app modules and main backend. Most of the modules are written in C++ and are programmed to be running independently. The motivation to make modules behave like this, was to make module testing easier (``CMake`` configurations + ``invoke`` library) and also allowing app to run smoothly without the module blocking.

.. _Neural networks:
Neuronové sítě
=============

.. image:: imgs/schema/ai_module_structure.png

Modul AI je podle toho strukturován. Musíme **PTT** (**P**\ ush **T**\ o **T**\ alk) signál, který je vyzván na ATCo GUI. Tento signál začíná ATCo hlasové nahrávání. Pomocí dalšího **PTT** signálu, zastavíme hlas z nahrávání, který je pak převeden na ``Wavefile`` formát, který je pak zaslán do modelu ASR (Whisper).
Tento mechanismus odděluje ``callsign``, ``command`` a ``value`` od transkripce. Poté zkontrolujeme ``callsign`` pomocí databáze pseudopilotů (tj. pokud konkrétní pseudopilot existuje). Pokud ano, potom posílejte změnu signálu do databáze letadla, abyste nastavili nový název podle ``command`` a ``value``. Poté pseudopilot generuje odpověď, která je následně odeslána do modelu TTS, který generuje vlnové soubory.

    .. note::
        **Systém v současné době podporuje pouze zvukový systém Pipewire**.
        Audio systém, který by mohl být křížovou platformou, je stále v rozvoji.
        `GitHub issue <https://github.com/SEDAS-DevTeam/SEDAS-AI-backend/problémy/5>`_.

.. _Calculations:
Výpočety letadla/prostředí
=============

.. note::
    **Přidejte nějaké vysvětlení**
