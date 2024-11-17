Getting Started with YukkiMusic
===============================

Requirements
------------

.. list-table::
   :header-rows: 0
   :widths: 10 90

   * - :fa:`check`
     - **Python 3.9 or higher**  
       Latest version recommended.
   * - :fa:`check`
     - **Telegram API Key**  
       API_ID and API_HASH from my.telegram.org  
       `Learn how to get API_ID and API_HASH <deployment/api-id-hash.html>`_
   * - :fa:`check`
     - **Telegram Bot Token**  
       Get from @BotFather on Telegram.
   * - :fa:`check`
     - **MongoDB Database URL**  
       Get from mongodb.com  
       `Learn how to set up MongoDB <deployment/mongo.html>`_

Installation Steps
------------------

1. Clone the Repository

   .. code-block:: bash

      git clone https://github.com/TeamYukki/YukkiMusicBot

2. Install Dependencies

   .. code-block:: bash

      pip3 install -r requirements.txt

3. Configure Environment Variables  
   Copy ``sample.env`` to ``.env`` and fill in your values.

4. Run the Bot

   .. code-block:: bash

      python3 -m YukkiMusicBot

Notes
-----

.. attention::  
   **Important**  
   Make sure to replace the placeholders in the ``.env`` file with your actual values.
