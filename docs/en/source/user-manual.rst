===================================
User manual
===================================

This manual depicts all the user interaction with the
desktop app itself. Manual consists of **App installation**, **Types of windows** and all their functionalities
and **App settings** (types of settings and their effects on the application runtime)

Table of contents
===================================
#. :ref:`App installation`
#. :ref:`Windows`

.. _App installation:
App installataion
===================================

.. note::

   **Currently, project does not have any builds**, the main desktop app is now in early development and many features are not done yet.
   However, you'll soon be able to see releases at `SEDAS github Releases <https://github.com/SEDAS-DevTeam/SEDAS-manager/releases>`_.

Building locally
-----------------------

.. note::
    **This part is not done yet and requires reformulation**, however, build documentation currently resides at `SEDAS github Setup/Installaton <https://github.com/SEDAS-DevTeam/SEDAS-manager?tab=readme-ov-file#setup-for-development>`_.

Windows
-----------------------

.. note::
    Project is not built yet

Linux
-----------------------

.. note::
    Project is not built yet

MacOS
-----------------------

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
^^^^^^^^^^^^^^^^^^^^^^^

In the start of the desktop app, user is greeted with the main menu window. This window just has 3 buttons, that redirect user
to different parts of the app.

* **Start** - This button activates SEDAS backend and other modules, and also alongside with that initializes all the windows that are going to
be used (`Controller window`, `Worker windows` (1 .. N - 1), N - defines number monitors connected)
* **Settings** - Redirects user to the settings window
* **Reload last session** - Because app has the periodical backup save functionality, user has the ability to recover last session from the last backup that is available.

.. note::
    **Reload button is greyed out for now**, the last session recovery is not yet implemented.

.. _Settings:
Settings
^^^^^^^^^^^^^^^^^^^^^^^

.. image:: imgs/pic/settings.png

.. _Controller:
Controller window
^^^^^^^^^^^^^^^^^^^^^^^

This is the most important window in the whole app. It categorizes user actions into multiple tabs (Setup, Simulation, Wiki, Monitors, Plugins) that are explained below.

Controller Setup
""""""""""""""""""

.. image:: imgs/pic/controller_setup.png

Controller Simulation
""""""""""""""""""

.. image:: imgs/pic/controller_sim.png

Controller Wiki
""""""""""""""""""

.. image:: imgs/pic/wiki.png

Controller Monitors
""""""""""""""""""

.. image:: imgs/pic/monitors.png

Controller Plugins
""""""""""""""""""

.. note::
    **The plugin GUI is not done yet**, project needs some reworking of the plugin implementations.

.. _Controller:
Worker (ATCo) window
^^^^^^^^^^^^^^^^^^^^^^^

.. image:: imgs/pic/worker.png

.. _App settings:
App settings
===================================

