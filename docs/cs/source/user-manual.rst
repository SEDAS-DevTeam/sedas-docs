===================================
Uživatelský manuál
===================================

Tento manuál popisuje veškerou interakci uživatele s aplikací samotnou.
Manuál se skládá z **Installace aplikace**, **Typy oken** a všech jejich funkcionalit
a **Nastavení aplikace** (typy nastavení a jejich účinky na provozní dobu aplikace)

Tabulka obsahů
===================================
#. :ref:`App installation`
#. :ref:`Windows`
#. :ref:`Main menu`
#. :ref:`Settings`
#. :ref:`Controller`
#. :ref:`Worker`
#. :ref:`Modes`
#. :ref:`Configurations`

.. _App installation:

Instalace App
===================================

.. note::

**V současné době projekt nemá žádné vydání**, hlavní desktopová aplikace je nyní v raném vývoji a mnoho funkcí ještě není dokončeno.
Nicméně, brzy budete moci vidět vydání na `SEDAS github Releases <https://github.com/SEDAS-DevTeam/SEDAS-manager/releases>`_.

..
    Podporované značky:
    HTTPS://img.shields.io/badge/OK-green?style=flat-square = OK - stavět úspěšný
    HTTPS://img.shields.io/badge/WARN-žlutý?style=flat-square = WARN - některé problémy mohou být na cestě
    HTTPS://img.shields.io/badge/X-red?style=flat-square = X - stavět neúspěšný

.. list-table:: List of supported OSes/distros
    :header-rows: 1

    * - **Name**
      - **Status**
      - **Note**
    * - Ubuntu 24.04
      - .. image:: https://img.shields.io/badge/X-red?style=flat-square
      - Release not available
    * - Ubuntu 22.04
      - .. image:: https://img.shields.io/badge/X-red?style=flat-square
      - Release not available
    * - Arch Linux
      - .. image:: https://img.shields.io/badge/X-red?style=flat-square
      - Release not available
    * - Windows 11
      - .. image:: https://img.shields.io/badge/X-red?style=flat-square
      - Release not available
    * - Windows 10
      - .. image:: https://img.shields.io/badge/X-red?style=flat-square
      - Release not available
    * - MacOS
      - .. image:: https://img.shields.io/badge/X-red?style=flat-square
      - Release not available

.. |ok| image:: https://img.shields.io/badge/OK-green?style=flat-square
.. |warn| image:: https://img.shields.io/badge/WARN-yellow?style=flat-square
.. |fail| image:: https://img.shields.io/badge/X-red?style=flat-square

* |ok| - Working on distro  
* |warn| - Some issues are present  
* |fail| - Failing on distro/Not released yet


.. tabs::

    .. tab:: Building locally

        .. note::
        **Všechny stavební kroky byly testovány pro Linux distribuce**, takže skutečné stavební pokyny pro Windows by se pravděpodobně významně lišily.


        Nastavení pracovního prostředí
        """"""""""""""""""

        .. tabs::

            .. tab:: Linux
                **Nastavení repozitáře**

                .. code-block:: shell

                    git clone --recursive https://github.com/SEDAS-DevTeam/SEDAS-manager.git
                    cd SEDAS-manager

                **Vytvoření Python virtuálního prostředí**

                Doporučuji používat ``pyenv`` pro nastavení projektového pomocníka (pro správu kompilace atd.), ale pokud jste více obeznámeni s ``conda``, není problém ji používat.
                Všechny závislosti na projektovém pomocníkovi se nacházejí v ``requirements.txt``

                .. code-block:: shell

                    pyenv install 3.11 # install python3.11
                    pyenv virtualenv 3.11 sedas_manager_env
                    pyenv local sedas_manager_env # Switches to environment
                    pip install -r requirements.txt # install depedendencies

                .. note::
                    Toto místní nastavení vytvořilo soubor ``.python-version`` ve vašem pracovišti. To pomáhá ``pyenv`` určit, které virtuální prostředí aktivovat.
                    Takže v podstatě nemusíte provádět aktivace/deaktivace.

                **Nastavení prostředí Node.js**

                Projekt používá ``nvm`` (Node Version Manager, `odkaz instalace <https://github.com/nvm-sh/nvm>`_) pro správu verze Node.js, takže projekt může zůstat většinou aktuální.
                V současné době projekt používá nejnovější verzi LTS (*v22.14.0*), abyste správně nastavili prostředí, musíte provést následující kroky:

                .. code-block:: shell

                    nvm install # to install LTS version from .nvmrc file
                    npm install -g npm@latext # ensure the latest version of npm

                Node.js prostředí je nyní nastaveno. invoke příkazy automaticky přechází na verzi uvedenou v ``.nvmrc ''.

                **Instalace závislostí npm**

                .. code-block:: shell

                    npm install
                    npm install -g node-gyp # to enable addon compilation

                .. note::

                    **V současné době Ubuntu 24.04 implementoval nové omezení AppImage,** takže uživatelé nemohou spustit aplikace Electron sandboxed (`github issue <https://github.com/electron/electron/issues/42510>`_).
                    Dočasný workaround je níže:

                    .. code-block:: shell

                        sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0 # deactivates the restriction
                        sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=1 # activates the restriction

                **Zkontrolujte jakékoli aktualizace submodules**

                .. code-block:: shell

                    invoke update # this will also check requirements.txt if any dependency is missing


                **Kompilace souborů C++, TS a node-addon-api**

                .. code-block:: shell

                    invoke compile

                **Běh aplikace v development režimu**

                .. code-block:: shell

                    invoke devel

                Všechno by mělo být na tuto chvíli připraveno :).


            .. tab:: Windows

                .. note::
                    **Přidat pokyny pro Windows**

            .. tab:: MacOS

                .. note::
                    **Přidat pokyny pro MacOS**

        Build a publikování na GitHub releases
        """"""""""""""""""

        Toolkit umožňuje vývojářům vytvářet a publikovat binární soubory. Tato funkce je pouze pro uživatele, kteří chtějí přispět a být součástí aktivního rozvoje.
        Prozatím je tato část v raném vývoji

        .. code-block:: shell

            invoke build # executes app build
            invoke publish # executes app publish to github

        .. note::
            Rozdíl mezi příkazem ``publish`` a ``build`` je v tom, že ``publish`` také publikuje binární soubor na GitHub. Takže nemusíte spouštět ``build`` před publikováním.

        .. note::
            **Vydávání není prozatím funkční.** Musíte být oprávněni a mít přístup k organizaci, což není v současné době možné, protože mnoho aspektů bude v budoucnu nutné přehodnotit.

        Nastavení dalších projektů
        """"""""""""""""""

        Tato část je zcela volitelná. Je zde právě pro lidi, kteří se chtějí podílet se na vývoji.

        .. tabs::

            .. tab:: SEDAS-AI-backend

                Tento modul je již postaven uvnitř SEDAS-manager jako podmodul, takže prakticky není nutné si ho sestavit.
                Ale pokud se chcete podílet na vývoji podpory SEDAS-AI-backend, můžete následovat tyto kroky:

                **Nastavení repozitáře**

                .. code-block:: shell

                    git clone --recursive https://github.com/SEDAS-DevTeam/SEDAS-AI-backend.git
                    cd SEDAS-AI-backend

                **Vytvoření Python virtuálního prostředí**

                .. code-block:: shell

                    pyenv install 3.11 # install python3.11
                    pyenv virtualenv 3.11 sedas_backend_env
                    pyenv local sedas_backend_env # Switches to environment
                    pip install -r requirements.txt # install depedendencies

                    cd src # přepínat na pracovat dir (kde se nachází tasks.py)

                **Získání všech zdrojů ASR/TTS**

                .. code-block:: shell

                    invoke fetch-resources

                .. note::
                    **Buďte si vědomi**, že toto pravděpodobně bude nějakou dobu trvat. Pomocník potřebuje získat ATC-whisper binární soubory z `huggingface repozitáře <https://huggingface.co/HelloWorld7894/SEDAS-whisper>`_ a také některé TTS soubory z webového zdroje Piper.

                **Sestavení whisper.cpp závislosti**

                .. code-block:: shell

                    invoke build-deps

                .. note::
                    Tento krok by také trval nějaký čas, `whisper.cpp <https://github.com/ggml-org/whisper.cpp>`_ potřebuje vytvořit wrapper, který bude zapínat model ATC-whisper na začátku simulace.
                    Takže pokud sestavujete verzi CUDA (to je nastaveno dle výchozího nastavení), tento proces pravděpodobně nějakou dobu potrvá.

                **Build celého projektu**

                **Pro testování**

                .. code-block:: shell

                    # for running a test
                    invoke build --DTESTING=ON
                    invoke run test

                Pro ``test`` executable můžete ovládat ASR a TTS jednoduše pomocí klávesnice (tj. klávesa ``a`` pro začátek / zastavení nahrávání a klávesa ``q`` pro zastavení celého programu).

                **Pro integraci**

                .. code-block:: shell

                    # to test the actual executable that is going to be integrated in SEDAS
                    invoke build --DTESTING=OFF
                    invoke run main

                Pro ``main`` executable k testování komunikace musíte spustit další skript na jiném okně terminálu (to je proto, že integrační skript komunikuje pomocí socketové komunikace na konkrétním portu ``65 432``).

                .. code-block:: shell

                    invoke test-main # runs the "commander" script that controls the "main" one

                .. note::
                    **Bohužel**, ``main`` executable v současné době komunikuje na konkrétním portu, který není možno změnit.
                    To se však určitě v budoucnu změní

                Použití skriptu ``test-main``:

                .. code-block:: shell

                    register  [callsign (string)] [noise-intensity (float)] # registers a pseudopilot to communicate with user (write without brackets)

                    start-mic # začíná nahrávání mikrofonů
                    stop-mic # stops mikro nahrávání

                    #
                    # Udělejte zde nějakou komunikaci pomocí start-mic nebo stop-mic
                    #

                    unregister [callsign (string)] # unregister/terminate pseudopilot
                    ukončit # ukončit hlavní program

            .. tab:: ATC-whisper

                Tento repozitář je v současné době používán pouze pro výzkumné účely, takže je zcela vyloučen z celého potrubí SEDAS-manager.
                Normální uživatel ho nepotřebuje postavit, protože sedas automaticky získává odpovídající binary z `huggingface repozitáře <https://huggingface.co/HelloWorld7894/SEDAS-whisper>`_.
                Tak následujte tento repo, pokud se chcete podílet na výzkumu a provádění pro lepší ASR model.

                .. note::
                    **V současné době**, ATC-whisper nepodporuje výcvik vlastní přizpůsobený model whisper, jen realizuje konverzi `whisper-ATC-czech-full <https://huggingface.co/BUT-FIT/whisper-ATC-czech-full>`_ (přizpůsobené váhy) do
                    model v ``GGML`` formátu. Ale v budoucnu bude projekt umožňovat trénování přizpůsobených modelů na ATCOSIM a dalších datasetech.

                **Nastavení repozitáře**

                .. code-block:: shell

                    git clone --recursive https://github.com/SEDAS-DevTeam/ATC-whisper.git
                    cd ATC-whisper

                **Vytvoření Python virtuálního prostředí**

                .. code-block:: shell

                    conda env create -f environment.yaml
                    conda activate atc_whisper # use conda deactivate for env deactivation

                    cd src # dostat do adresáře dir

                **Download zdrojů**

                .. code-block:: shell

                    invoke download
                    # use: invoke download -t="repo" to download SEDAS-whisper huggingface repo
                    # use: invoke download -t="model" to download whisper-ATC-czech-full resources

                **Build whisper.cpp binary** (pouze pro testování inference modelu whisper)

                .. code-block:: shell

                    invoke build

                .. note::
                    **Buďte si vědomi**, že to bude trvat nějakou dobu, protože whisper.cpp potřebuje vybudovat celý Whisper wrapper. Proces může být mnohem delší, pokud je stavěn s podporou CUDA (která je nyní dle navolena by default).

                **Konverze Pytorch modelu na GGML**

                .. code-block:: shell

                    invoke convert bin-to-ggml

                **Testování inference**

                .. code-block:: shell

                    invoke run-infer

                **Ukládání modifikovaného obsahu do Huggingface** (pouze pro ověřené uživatele s vlastním tokenem)

                Token je uložen na ``token.yaml`` v rootu projektu (musíte ho vytvořit sami), formátování je odpovídající:

                .. code-block:: yaml

                    token: <your huggingface token>

                Chcete-li nahrát modifikovaný obsah, spustit tento příkaz:

                .. code-block:: shell

                    invoke upload

            .. tab:: sedas-docs

                Také není nutné pro stavbu uživatele SEDAS-Manager, ale pokud chcete přispět k projektu **SEDAS**, pokračujte.

                **Připravení repozitáře**

                .. code-block:: shell

                    git clone https://github.com/SEDAS-DevTeam/sedas-docs.git
                    cd sedas-docs

                **Vytvoření Python virtuálního prostředí**

                .. code-block:: shell

                    pyenv install 3.10 #install python3.10
                    pyenv virtualenv 3.10 sedas_docs
                    pyenv local sedas_docs # Switches to environment
                    pip install -r requirements.txt
                    pip install -r ./docs/en/requirements.txt # Install the sphinx requirements

                **Sestavení dokumentace lokálně**

                .. code-block:: shell

                    invoke build en # for the english version (for others, supply other abbreviations: cz)

    .. tab:: Downloading/using prebuilt binaries

        .. tabs::
            .. tab:: Linux

                .. note::
                    Projekt ještě nebyl sestaven

            .. tab:: Windows

                .. note::
                    Projekt ještě nebyl sestaven

            .. tab:: MacOS

                .. note::
                    Projekt ještě nebyl sestaven

.. _Windows:

Okna a jejich funkce
===================================

Typy oken
-----------------------

V současné době se používají tyto typy oken:

.. _Main menu:

Hlavní menu
""""""""""""""""""

Na začátku desktopové aplikace je uživatel vítán hlavním menu okna. Tento okno má pouze 3 tlačítka, které přesměrují uživatele
v různých částech aplikace.

* **Start** - Toto tlačítko aktivuje backend SEDAS a další moduly, a také spolu s tím iniciuje všechny okna, které se budou používat (`Controller window`, `Worker windows` (1 .. N - 1), N - definuje počet připojených monitorů)

* **Settings** - Odkazuje uživatele na okno nastavení

* **Reload last session** - Vzhledem k tomu, že aplikace má funkci pravidelného zálohování, uživatel má možnost obnovit poslední session z posledního zálohování, které je k dispozici.


.. note::
    **Reload tlačítko je prozatím zašedlé**, recovery poslední zálohy prozatím není implementováno.

.. _Settings:

nastavení
""""""""""""""""""

.. image:: imgs/pic/settings.png

V okně nastavení může uživatel nastavit základní chování simulátoru. samotné okno je rozděleno do několika kategorií. Máme obecné nastavení, které usnadňují
Pak máme nastavení ovládače (tj. chování oken ATCo) a nastavení simulace, které umožňují uživateli změnit některé
Z hlediska životního prostředí a také pseudopilotního chování AI.

.. _Controller:

Kontrolní okno
""""""""""""""""""

To je nejdůležitější okno v celé aplikaci. kategorizuje uživatelské akce do několika tabulek (Nastavení, Simulace, Wiki, Monitory, Plugins), které jsou vysvětleny níže.
Dokumentace je formátována do různých kategorií, které vysvětlují konkrétní okno.

.. tabs::
    .. tab:: Setup tab

        .. figure:: imgs/pic/controller_setup.png
            :align: center

            Controller Setup tab

        Simulace SEDAS jsou rozděleny do dvou kategorií: **Planned** a **Unplanned**.

        **Plánované simulace**

        Uživatel může nastavit plánované simulace v tabulce nastavení, když vyberou mapu (a odpovídající scénář), předem nastavení letadla a předem nastavení příkazů s dodatečnými tweaks.
        Po tom simulátor určí a nastaví tak simulace.Varianty, které jsou uživatelem přepínavé, jsou vysvětleny níže:

        * **Map** - here, user can select a specific map/airport that will be used in the simulation. Every map has its type according to ATC zone classification (ACC, TWR and APP). They also have designated ICAO airport code (if the map is designated as an airport), Country and City (could be left empty if the simulation doesnt redirect to actual place) and the description (also optional).
        
        * **Scenario** - Every map has its own predefined sets of scenarios, that define what plane types are going to be used in the simulation and also other key aspects (time of plane spawning, special situations). Every map has different scenarios.
        
        * **Scenario adjustment** - User can adjust selected scenarios. Currently, scenario adjustments just allow to exclude WTC (Wake Turbulence - **UL**\ tralight, **L**\ ight, **M**\ edium, **H**\ eavy, **J** - Super) or CAT (aircraft category - **AI**\ rplane, **HE**\ licopter, **GL**\ ider, **AE**\ rostat) categories.
        
        * **Scenario time** - User can select the time of scenario (this setting is just aesthetic, so it could be left at random, which generates random time and date)
        
        * **Aircraft preset** - Allows user to select specific types of planes (planes from only one manufacturer, etc.). User can inspect the preset before selecting it.
        
        * **Commands preset** - Allows user to select specific commands that are going to be allowed in the simulation. Other commands are not going to be accepted by AI pseudopilots.

        .. note::
            **V současné době plánované simulace zatím nefungují.** To je proto, že implementace simulace nastavení motoru je docela těžké a vyžaduje zavedení mnoha pravidel a výjimek při jeho implementaci.
            Při jeho provádění je tedy doporučeno, aby uživatel používal **Neplánované simulace**.

        **Neplánované simulace**

        Každá mapa umožňuje uživateli nastavit každou předvolbu na prázdnou. To znamená, že simulátor bude nastaven na výchozí a nulové výjimky budou použity na simulace.
        Simulace by byla prázdná a zobrazí se pouze vybraná mapa.Po tom, uživatel může volně šroubovat letadla v tabulce **Simulace**, takže simulace je řízen uživatelem.

    .. tab:: Monitors tab

        .. figure:: imgs/pic/monitors.png
            :align: center

            Ovládání monitorů Tab

        Simulátor umožňuje uživateli přizpůsobit několik okenních příkladů. samotná aplikace je navržena tak, aby pracovala na nastavení více monitorů. Doporučený počet monitorů je v současné době 2 (jeden pro kartu Controller, druhý pro kartu Fro Worker (ATCo).
        Nicméně, aplikace také pracuje pouze na jednom nastavení monitoru ( okna by se přesto překrývala). Uživatel může vybrat, jaké chování by konkrétní okno / monitor měl.
        Možnosti jsou uvedeny níže:

        * **TWR** - Tower view for the simulation (Map has to support TWR)
        
        * **APP** - Approach view for the simulation (Map has to support APP)
        
        * **ACC** - Area control view for the simulation (Map has to support ACC)
        
        * **weather** - Embeds weather data into simulation (Map has to point into specific place on the earth - Country and City tags cannot be empty when selected)
        
        * **dep_arr** - Departure/Arrival view for the currently activated planes.
        
        * **embed** - Allows user to embed external web resource from the URL.

        .. note::
            Simulátor v současné době podporuje pouze **ACC**, **veather** a **dep_arr** zobrazení.

    .. tab:: Simulation tab

        .. figure:: imgs/pic/controller_sim.png
            :align: center

            Ovladač simulace tab

        V tabulce simulace může uživatel ovládat chování simulace. To není opravdu nutné v **Planovaných simulacích**, ale docela důležité v **Neplanovaných simulacích**.
        Na vrcholu, uživatel může ovládat stav simulace. Poté máme letadlo spouštěcí část. Tam můžeme nastavit název letadla (náhodně generované nebo vytisknuté) a
        počáteční hodnocení, úroveň a rychlost.Můžeme také určit konkrétní odletové a příjezdové body na letadlo.

        .. note::
            **Možnosti: Typ letadla a Monitor** ještě nejsou funkční. nejsou v nastavení simulace letadla relevantní, takže v budoucnu je buď odstraníme, nebo je provedeme tak, aby byly funkční.

        Po potvrzení letadla bude letadlo spouštět na okně ATCo a uvidíme nový panel otevřen v kategorii Ovládání letadla.
        Tento panel je určen pouze pro základní opravu, není nutný, protože jeho funkčnost je doplněna pseudopiloty AI (tj. uživatel ovládá všechny variabily letadla verbálně).

        Poslední část je terminál letadla. zde může uživatel vidět všechny záznamy o letadlech reagujících na příkazy ATCo a také změny názvu, úrovně a projevu provedené letadlem.

    .. tab:: Plugins tab

        .. note::
            **Plugin GUI ještě není dokončen**, projekt potřebuje nějaký přepracování implementací pluginu.

    .. tab:: Wiki tab

        .. figure:: imgs/pic/wiki.png
            :align: center

            Controller Wiki tab

        Simulátor je určen pro lidi, kteří jsou začátečníky v ATC. Z tohoto důvodu je okno ovládacího prvku určeno pouze pro dokumentaci.
        Uživatel může přepínat mezi **SEDAS** a **IVAO** dokumentací (která také obsahuje zajímavé údaje o ATC).
        je spolehlivým zdrojem ATC spravovaným společností EUROCONTROL.

.. _Worker:

Pracovní okno (ATCo)
""""""""""""""""""

.. image:: imgs/pic/worker.png

To je GUI, který je viditelný pro ATCo (Aer Traffic Control Officer).
Na vrcholu je topnav, který obsahuje akce ATCo (mikrofonový výstup, datum a čas simulace a simulace stavu přepínání).
Simulátor také umožňuje ATCo k výstupu simulace (tak, že ATCo nemusí vytiahnout myši do odděleného okna, aby se výstup aplikace).
V pravém dolním rohu máme skalu, takže ATCo může udělat některé jako předpoklad o oblasti ATM zóny.

.. _Modes:

Simulační režimy
===================================

V současné době aplikace podporuje dva režimy ATC simulací: **plánované** a **neplánované** simulace.

* **Planned simulations -** For the user, these ones are easier to set up. Only thing user needs to do is setting up the simulation in the :ref:`Controller` (more specificaly, the setup tab). Here, user specifies map, its corresponding scenario, some adjustments, aircraft presets, command presets and scenario time. After user clicks on the *Confirm and setup* button, the app starts its environment handler which then sets up all the monitors and also the whole ATC environment. After that, user can just click on the ``START`` button in the *Simulation tab*. After that, the simulation is set up and running. (User can then do some small tweaks in the terms of plane handling etc.)

* **Unplanned simulations -** Every map supports an empty scenario. When user selects this, while also setting up the rest of presets, and pressing the *Confirm and setup* button, the app will not start its environment handler, because it detected that there is no scenario available. The only thing it will set up is the map and the rest of presets (aircrafts, commands). So in order to spawn any planes in the user-specified map, user needs to spawn planes manually, which is done in the *Simulation tab*.

.. note::
    **V současné době aplikace podporuje pouze neplánované simulace**, plánovaný mechanismus nastavení simulace je stále v rozvoji.

.. _Configurations:
Uživatelská konfigurace JSON
===================================

Naštěstí uživatelé nepotřebují upravovat samotné konfigurace, pokud nechtějí větší kontrolu nad chováním programů.
Hlavní nastavení aplikace lze změnit prostřednictvím grafického rozhraní nastavení SEDAS, který je přístupný prostřednictvím hlavního menu. Nicméně, tato kapitola popisuje další konfigurace a také nastavení formátování, takže uživatel může ručně zasahovat do funkce aplikace.

.. tabs::
    .. tab:: Main settings

    .. tab:: Modules

    .. tab:: Plugins

    .. tab:: GUI layout

        .. tabs::
            .. tab:: Settings

            .. tab:: Plugin

    .. tab:: Environments

        .. tabs::
            .. tab:: Map config

            .. note::
                Ve výchozím nastavení SEDAS vloží některé mapy v nově nainstalovaném balíčku. Uživatel může přidat vlastní balíček, ale s cílem to udělat,
                Musí se manuálně dostat do zdrojů aplikací a přidat odpovídající „json“ soubor sám. V budoucnu bude SEDAS mít integrovaný modul pro tvorbu aplikací (**SEDAS-mapbuilder**).

            **Instalace mapy předem manuálně**

            **Instalace mapy předem pomocí SEDAS-mapbuilder**

            .. tab:: Airline config

                .. note::
                    **Nastavení leteckých společností** se zatím v pozadí neprovádí, zatím slouží k žádnému účelu.
                    Ale tato funkce bude implementována vedle plánovaného algoritmu simulace a nastavení.
                    V současné době nejsou ani volitelné v tabulce *Nastavení*, protože provozovatel prostředí ještě není dokončen, a proto by v podstatě sloužil jako žádný účel.

            .. tab:: Command config

                .. note::
                    **Nastavení pro příkazy** se zatím v pozadí neprovádí, zatím slouží k žádnému účelu.
                    Ale tato funkce bude implementována vedle plánovaného algoritmu simulace a nastavení.

            .. tab:: Planes config

                .. note::
                    **Nastavení pro letadla** nejsou v pozadí dodnes implementovány, zatím slouží k žádnému účelu.
                    Ale tato funkce bude implementována vedle plánovaného algoritmu simulace a nastavení.
                    K dnešnímu dni celá simulace vypočítá leteckou fyziku na základě letadla B737-800 (viz :doc:`teorie` pro více informací).

.. note::
    **Moduly a pluginy** mají také své vlastní konfigurace, ale jsou spravovány samotným modulem/pluginem.
    Celý panel konfigurace modulů/pluginů bude k dispozici v následující verzi SEDAS.
