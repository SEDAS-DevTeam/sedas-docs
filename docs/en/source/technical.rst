===================================
Technical background
===================================

Application itself uses a lot of technologies to implement many of its parts. For example it utilises localhost sockets communication for the
communication between main app and AI module. This page will try to explain all the technical approaches that were used in the development.

.. list-table:: List of used technologies
    :widths: 30 70

    * - Used tech
      - 
    * - **App**
      -
    * - `ElectronJS`
      - Main backend for app behavior
    * - `NodeJS`
      - Main code runtime
    * - `Typescript`
      - Language used for backend
    * - `node-addon-api/C++`
      - Used for resource intensive computations
    * - **AI module**
      -
    * - `Whisper`
      - **ASR**
    * - `Rule-based NLP`
      - **NLP**
    * - `VITS`
      - **TTS**
    * - `Whisper.cpp`
      - Inference for Whisper model
    * - `PiperTTS`
      - Inference for VITS model

.. note::
    **Rework all the image resources to english**

App schematic
===================================

.. image:: imgs/schema/backend_structure.png

Neural networks part
===================================

.. image:: imgs/schema/ai_module_structure.png