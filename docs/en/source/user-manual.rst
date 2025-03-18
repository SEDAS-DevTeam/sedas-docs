===================================
User manual
===================================

This manual depicts all the user interaction with the
desktop app itself. Manual consists of **App installation**, **Types of windows** and all their functionalities
and **App settings** (types of settings and their effects on the application runtime)

Table of contents
===================================
#. :ref:`App installation`
    #. :ref:`Build locally`
    #. :ref:`Prebuilt`
#. :ref:`Windows`
    #. :ref:`Main menu`
    #. :ref:`Settings`
    #. :ref:`Controller`
    #. :ref:`Worker`

.. _App installation:

App installataion
===================================

.. note::

   **Currently, project does not have any builds**, the main desktop app is now in early development and many features are not done yet.
   However, you'll soon be able to see releases at `SEDAS github Releases <https://github.com/SEDAS-DevTeam/SEDAS-manager/releases>`_.

.. _Build locally:

Building locally
-----------------------

.. note::
    **All the build steps were tested for Linux distros**, so the actual build instructions for Windows would probably differ significantly.

.. tabs::

    .. tab:: Linux
        **Setting up repository**

        .. code-block:: shell

            git clone --recursive https://github.com/SEDAS-DevTeam/SEDAS-manager.git
            cd SEDAS-manager

        **Setting up virtual environment**

        I recommend using `virtualenv` for setting up project helper (for managing building, compiling, etc.), but if you are more familiar with `conda`, there is no problem of using that.
        All the project helper dependencies are in `requirements.txt`

        .. code-block:: shell

            virtualenv sedas_manager_env
            source sedas_manager_env/bin/activate # To activate venv, use "deactivate" for deactivation
            pip install -r requirements.txt
            cd src # get to working dir

        **Install npm dependencies**

        .. code-block:: shell

            npm install

        **Compile C++, TS and node-addon-api files**

        .. code-block:: shell

            invoke compile

        **Run app in development mode**

        .. code-block:: shell

            invoke devel

        **Building and publishing**

        .. note::
            **These methods arent set up yet**, but will be worked on in the future, because they are quite crucial for the app development.
            Commands down here are mostly placeholders, so please, do not **USE THEM YET**.

        .. code-block:: shell

            invoke build # executes app build
            invoke publish # executes app publish to github


    .. tab:: Windows

        .. note::
            **Add windows build instructions**

    .. tab:: MacOS

        .. note::
            **Add MacOS build instructions**

Everything should be set up for now :).

.. _Prebuilt:

Downloading/using prebuilt binaries
-----------------------

.. tabs::
    .. tab:: Linux
        
        .. note::
            Project is not built yet
    
    .. tab:: Windows

        .. note::
            Project is not built yet
    
    .. tab:: MacOS

        .. note::
            Project is not built yet

.. _Windows:

Windows and their functionalities
===================================

Types of windows
-----------------------

Currently, these types of windows are utilized:

.. _Main menu:

Main menu
""""""""""""""""""

In the start of the desktop app, user is greeted with the main menu window. This window just has 3 buttons, that redirect user
to different parts of the app.

* **Start** - This button activates SEDAS backend and other modules, and also alongside with that initializes all the windows that are going to be used (`Controller window`, `Worker windows` (1 .. N - 1), N - defines number monitors connected)

* **Settings** - Redirects user to the settings window

* **Reload last session** - Because app has the periodical backup save functionality, user has the ability to recover last session from the last backup that is available.


.. note::
    **Reload button is greyed out for now**, the last session recovery is not yet implemented.

.. _Settings:

Settings
""""""""""""""""""

.. image:: imgs/pic/settings.png

In the settings window, user can set up the basic simulator behavior. The window itself is separated into multiple categories. We have the general settings, which facilitate
the general ATC simulator behavior. Then we have the Controller settings (i. e. the behavior of the ATCo windows) and the Simulation settings, which allow user to change some
environmental aspects and also AI pseudopilot behavior.

.. _Controller:

Controller window
""""""""""""""""""

This is the most important window in the whole app. It categorizes user actions into multiple tabs (Setup, Simulation, Wiki, Monitors, Plugins) that are explained below.
The documentation is formatted into different categories that explain specific window. Category order is similar to the order in Controller window.

.. tabs::
    .. tab:: Setup tab
        
        .. figure:: imgs/pic/controller_setup.png
            :align: center

            Controller Setup tab

        .. note::
            **Add tab description**
    
    .. tab:: Monitors tab

        .. figure:: imgs/pic/monitors.png
            :align: center
            
            Controller Monitors tab

        .. note::
            **Add tab description**
    
    .. tab:: Simulation tab

        .. figure:: imgs/pic/controller_sim.png
            :align: center

            Controller Simulation tab

        .. note::
            **Add tab description**

    .. tab:: Plugins tab

        .. note::
            **The plugin GUI is not done yet**, project needs some reworking of the plugin implementations.

    .. tab:: Wiki tab

        .. figure:: imgs/pic/wiki.png
            :align: center

            Controller Wiki tab

        .. note::
            **Add tab description**

.. _Worker:

Worker (ATCo) window
""""""""""""""""""

.. image:: imgs/pic/worker.png

This is the GUI that is visible for the ATCo (Air traffic control officer). The overlay is partly inspired from other simulators as well.
On the top is the topnav that contains ATCo actions (microphone output toggle, Date and time of simulation and simulation state switching).
Simulator also allows ATCo to exit simulations (so that ATCo doesnt have to drag their mouse to separate window in order to exit app).
On the bottom right corner we have the scale, so that ATCo can make some as assumption about the area of the ATM zone. Planes also have dotted paths that indicate their previous location.