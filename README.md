# ComfyDiscordBot
A discord bot utilizing ComfyUI's API capability

In order to set up the Discord bot, install [ComfyUI](https://github.com/comfyanonymous/ComfyUI). After setting ComfyUI up following their instructions, add the checkpoints that you'd like to use into the /ComfyUI/models/checkpoints file. Inside of the models.py file, make a new entry or change one of the defaults to match the model and settings you'd like to use for the specific model. If you'd like to use the already set up models, download [Dreamshaper XL v2.1](https://civitai.com/models/112902?modelVersionId=351306) and [Yiffymix XL v52](https://civitai.com/models/3671?modelVersionId=732770), and put those into your checkpoints file

Make a new file and call it key.py, and enter `key = "1234"` replacing 1234 with your bot token

## Windows specific instructions
In order to run the code properly without errors, you must be running Python 3.11 or newer. I recommend checking "Add to PATH" so you don't have to reference to the file location. Once you have Python installed, run `python.exe -m venv env`, then run `.\env\Scripts\activate`. This will put you into an environment where you can install packages locally. Next, run `python.exe -m pip install -r requirements.txt` to install the required packages for the bot.

Once you have your venv set up properly, you should be able to run `python.exe main.py` to run the bot! If your commands do not show up, try restarting Discord, then you can run `/generate`, entering a prompt and one of the models configured to generate an image!

## Linux specific instructions
In order to run the code properly without errors, you must be running Python 3.11 or newer. Once you have Python installed, run `python3 -m venv env`, then run `source ./env/bin/activate`. This will put you into an environment where you can install packages locally. Next, run `python -m pip install -r requirements.txt` to install the required packages for the bot.

Once you have your venv set up properly, you should be able to run `python main.py` to run the bot! If your commands do not show up, try restarting Discord, then you can run `/generate`, entering a prompt and one of the models configured to generate an image!