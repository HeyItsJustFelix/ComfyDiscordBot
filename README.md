# ComfyDiscordBot
A discord bot utilizing ComfyUI's API capability

In order to set up the Discord bot, install [ComfyUI](https://github.com/comfyanonymous/ComfyUI). After setting ComfyUI up following their instructions, add the checkpoints that you'd like to use into the /ComfyUI/models/checkpoints file. Inside of the models.py file, make a new entry or change one of the defaults to match the model and settings you'd like to use for the specific model.

Make a new file and call it key.py, and enter `key = "discord bot token"` entering your bot token

In order to run the code properly without errors, you must be running Python 3.11 or newer. Once you have Python installed, run `python.exe -m venv env` if on Windows or `python3 -m venv env` if on Linux, then run `.\env\Scripts\activate` if on Windows, or `source ./env/bin/activate` on Linux. This will put you into an environment where you can install packages locally. Next, run `python.exe -m pip install -r requirements.txt` if on Windows or `python -m pip install -r requirements.txt` on Linux.

Once you have your venv set up properly, you should be able to run `python.exe main.py` or `python main.py` to run the bot! If your commands do not show up, try restarting Discord, then you can run `/generate`, entering a prompt and one of the models configured to generate an image!