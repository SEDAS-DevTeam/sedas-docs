===================================
Uživatelská příručka
===================================

Tato příručka popisuje veškerou interakci uživatele s
aplikací SEDAS. Aplikace primárně určena pro stolní počítače. Příručka se skládá z **Instalace aplikace**, **Typů oken** a všech jejich funkcionalit
a **Nastavení aplikace** (typy nastavení a jejich efekt na běh aplikace).

Obsah
===================================
#. :ref:`Instalace aplikace`
    #. :ref:`Lokalni sestaveni`
    #. :ref:`Predpripravena verze`
#. :ref:`Okna`
    #. :ref:`Hlavni menu`
    #. :ref:`Nastaveni`
    #. :ref:`Ridici panel`
    #. :ref:`Pracovní okno`
#. :ref:`Konfigurace`

.. _Instalace aplikace:

Instalace aplikace
===================================

.. note::

   **Projekt zatím nemá žádné sestavení**, hlavní desktopová aplikace je nyní ve fázi ramého vývoje a mnoho funkcí není dosud dokončeno.
   Brzy ale budete moci najít vydané verze aplikace na `SEDAS GitHub Releases <https://github.com/SEDAS-DevTeam/SEDAS-manager/releases>`_.

.. _Lokalni sestaveni:

Lokální sestavení
-----------------------

.. note::
    **Všechny kroky sestavení byly testovány na Linuxových distribucích**, proto se pokyny pro Windows budou s největší pravděpodobností značně lišit.

.. tabs::

    .. tab:: Linux
        **Nastavení repozitáře**

        .. code-block:: shell

            git clone --recursive https://github.com/SEDAS-DevTeam/SEDAS-manager.git
            cd SEDAS-manager

        **Nastavení virtuálního prostředí**

        Doporučujeme používat `virtualenv` pro nastavení projektového prostředí (správa sestavení, kompilace atd.), pokud jste ale zvyklí na `conda`, není problém ji použít.
        Všechny závislosti projektového prostředí jsou v souboru `requirements.txt`

        .. code-block:: shell

            virtualenv sedas_manager_env
            source sedas_manager_env/bin/activate # Pro aktivaci venv, deaktivace příkazem "deactivate"
            pip install -r requirements.txt
            cd src # Přechod do pracovního adresáře

        **Instalace npm závislostí**

        .. code-block:: shell

            npm install

        **Kompilace C++, TS a node-addon-api souborů**

        .. code-block:: shell

            invoke compile

        **Spuštění aplikace v režimu vývoje**

        .. code-block:: shell

            invoke devel

        **Sestavení a publikace**

        .. note::
            **Tyto metody nejsou zatím implementovány**, ale budou doplněny v budoucnu, protože jsou klíčové pro vývoj aplikace.
            Níže uvedené příkazy jsou zatím pouze zástupné, **NEPOUŽÍVEJTE JE TEDY!**

        .. code-block:: shell

            invoke build # Provede sestavení aplikace
            invoke publish # Provede publikaci aplikace na GitHub

    .. tab:: Windows

        .. note::
            **Doplnit pokyny pro sestavení na Windows**

    .. tab:: MacOS

        .. note::
            **Doplnit pokyny pro sestavení na MacOS**

To by mělo být vše k instalaci :).

.. _Predpripravena verze:

Installace/Použití předpřipravených sestavení
-----------------------

.. tabs::
    .. tab:: Linux
        
        .. note::
            Projekt není prozatím sestaven
    
    .. tab:: Windows

        .. note::
            Projekt není prozatím sestaven
    
    .. tab:: MacOS

        .. note::
            Projekt není prozatím sestaven

.. _Okna:

Typy oken
-----------------------

Dosavadně jsou tyhle typy oken implementovány a využívány v aplikaci:

.. _Hlavni menu:

Hlavní menu
""""""""""""""""""

Při startu desktopové aplikace uživatel uvidí okno hlavního menu. Toto okno má pouze 3 tlačítka, které přesměrovávají uživatele
do různých částí aplikace.

* **Start** - Tohle tlačítko aktivuje SEDAS backend a ostatní moduly, a mimo jiné taky inicializuje všechny okna která budou používána (`Controller okno`, `Worker okno` (1 .. N - 1), N - definuje počet připojených monitorů k PC sestavě)

* **Settings** - Přesměrovává uživatele do okna nastavení

* **Reload last session** - Protože aplikace má funkcionalitu periodického ukládání stavu, uživatel má tu možnost obnovit poslední relaci simulace z poslední uložené zálohy. 

.. note::
    **Tlačítko obnovení je prozatím zakázáno**, implementace obnovení z poslední zálohy totiž není ještě hotova.

.. _Nastaveni:

Nastavení
""""""""""""""""""

.. image:: imgs/pic/settings.png

V okně nastavení může uživatel nastavit základní chování simulátoru. Samotné okno je rozděleno do několika kategorií. Máme zde obecná nastavení, která usnadňují
obecné chování simulátoru ATC. Dále zde máme Controller nastavení (tj. chování oken ATCo) a Nastavení simulace, které uživateli umožňují změnit některé
aspekty prostředí a také chování AI pseudopilota.

.. _Ridici panel:

Řidící panel
""""""""""""""""""

Jedná se o nejdůležitější okno v celé aplikaci. Rozděluje uživatelské akce do několika záložek (Nastavení, Simulace, Wiki, Monitory, Moduly), které jsou vysvětleny níže.
Dokumentace je formátována do různých kategorií, které vysvětlují konkrétní okno. Pořadí kategorií je podobné pořadí v Controller okně.

.. tabs::
    .. tab:: Setup karta

        .. figure:: imgs/pic/controller_setup.png
            :align: center

    .. tab:: Monitors karta

        .. figure:: imgs/pic/monitors.png
            :align: center

    .. tab:: Simulation karta

        .. figure:: imgs/pic/controller_sim.png
            :align: center

    .. tab:: Wiki karta

        .. figure:: imgs/pic/wiki.png
            :align: center

.. _Pracovni okno:

Pracovní (ATCo) okno
""""""""""""""""""

.. image:: imgs/pic/worker.png

Toto je grafické uživatelské rozhraní, které je viditelné pro ATCo (řídícího letového provozu). GUI je částečně inspirováno i jinými simulátory.
V horní části je topnav, která obsahuje akce ATCo (přepínání výstupu mikrofonu, datum a čas simulace a přepínání stavu simulace).
Simulátor také umožňuje ATCo ukončit simulaci (takže ATCo nemusí přetahovat myš do jiného okna, aby mohl ukončit aplikaci).
V pravém dolním rohu máme měřítko, takže ATCo může učinit nějaký jako předpoklad o velikosti ATM zóny. Letadla mají také za sebou tečky, které tak označují jejich předchozí polohu.

.. _Konfigurace:
Uživatelsky měnitelné JSON konfigurace
===================================