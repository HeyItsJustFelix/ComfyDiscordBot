# ComfyDiscordBot
A discord bot utilizing ComfyUI's API capability

# Instructions
## Installing ComfyUI
In order for the bot to work, you need to install [ComfyUI](https://github.com/comfyanonymous/ComfyUI) first. After setting ComfyUI up following their instructions, add the checkpoints that you'd like to use into the /ComfyUI/models/checkpoints file. If you'd like to use the already set up models, download [Dreamshaper XL v2.1](https://civitai.com/models/112902?modelVersionId=351306) and [Yiffymix XL v52](https://civitai.com/models/3671?modelVersionId=732770), and put those into your checkpoints folder.

## Setting up the bot
Go to the [Discord Developers Portal](https://discord.com/developers/applications) and make a new bot. Make sure to copy the token somewhere safe. Go to the oauth tab and select "Bot" as the Scope, and allow the permissions "Send Messages", and "Attach Files". Inside of the Bot tab, turn on the "Server Members Intent" to allow users to use the bot in DMs.

## Setting up the code
Download and unzip the [Code](https://github.com/HeyItsJustFelix/ComfyDiscordBot/archive/refs/heads/main.zip). Inside of the folder you just extracted, make a new file called `key.py`. Add inside of this file the text `key = "1234"` replacing 1234 with the bot token you saved earlier.

If you downloaded models different from Dreamshaper XL v2.1 or Yiffymix XL v52, open up the models.py file. Inside of the models.py file, make a new entry or change one of the defaults to match the model and settings you'd like to use for the specific model. If you have only one model, you can delete one of the entries.

## Running the bot code
### Windows specific instructions
In order to run the code properly without errors, you must be running Python 3.11 or newer. I highly recommend checking "Add to PATH" during installation so you don't have to reference to the file location. Once you have Python installed, make sure that you're inside of the folder with the code by typing `cmd` at the top of the file explorer window. Once the command prompt is open, run `python.exe -m venv env`, then run `.\env\Scripts\activate`. This will put you into an environment where you can install packages locally. Next, run `python.exe -m pip install -r requirements.txt` to install the required packages for the bot.

Once you have your venv set up properly, you should be able to run `python.exe main.py` to run the bot! If your commands do not show up, try restarting Discord, then you can run `/generate`, entering a prompt and one of the models configured to generate an image!

### Windows troubleshooting
If you receive `python.exe not found` or something similar, please rerun the installer, click modify, and click next, and make sure that `Add python to environment variables` is checked, then click Install.

If you get an error saying `Actively refused connection` when running /generate, make sure that you have comfyui open and running

### Linux specific instructions
In order to run the code properly without errors, you must be running Python 3.11 or newer. Once you have Python installed, run `python3 -m venv env`, then run `source ./env/bin/activate`. This will put you into an environment where you can install packages locally. Next, run `python -m pip install -r requirements.txt` to install the required packages for the bot.

Once you have your venv set up properly, you should be able to run `python main.py` to run the bot! If your commands do not show up, try restarting Discord, then you can run `/generate`, entering a prompt and one of the models configured to generate an image!

### Linux troubleshooting
If you get an error saying `Actively refused connection` when running /generate, make sure that you have comfyui open and running