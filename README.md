1. SETUP VIRTUAL ENV
2. For api:
    cd api
    behave
3. For selenium tests: Ensure that Chrome drive binary is downloaded and placed into your system path. If virtualenv is activated then place the Chrome binary in bin folder ($VIRTUAL_ENV/<your_env>/bin)
    cd selenium
    py.test search_ui.py --driver Chrome

