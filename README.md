# Cobblemon-Karma-Farmer
This program will automatically type 'welcome' in the chat whenever prompted by the server in the Cobblemon GG Minecraft server. This allows for the user to go AFK and not worry about missing out on gaining more karma points.  

***
You will need to install PyTesseract to your machine. 
  - The download can be found here: https://github.com/UB-Mannheim/tesseract/wiki

Additionally if you do not have them installed, you should pip install pyautogui, pillow, and pytesseract (pytesseract needs to be pip installed after its initial download).
```
pip install pyautogui pillow pytesseract
```
***
## FIRST go into chat-space-checker.py
Use chat-space-checker.py to take screenshots of your computer screen in order to adjust the dimensions to properly fit the Minecraft chat window.
Consult the image in chat_region_example.png for reference. 
If you are using a singular monitor, I find this step works best when Minecraft is in windowed-fullscreen mode and your program is windowed in the top right corner of the screen so that the whole Minecraft chat window is still visible. You will also have to open the chat to go into cursor mode, this will allow you to click into your IDE running this code while the entire chat window is visible. 

### Next edit main.py
Use the dimensions from the previous step and replace the ones used in main.py

# EDIT YOUR KEYBINDS IN main.py
in main.py pyautogui uses the keys to open the chat and to send a message. You may have to change the string to your Minecraft keybind.  

***
Additionally, the server will also prompt the user to send 'gg' in the chat for karma points. I have attempted to implement that via an 'if-statement' but it broke the program, so for now I have left it out. In the future I will figure out a way for both to be included.

***
### About the Cobblemon GG server
The Cobblemon GG server can be accessed directly via the Modrinth client
  - the download for the client can be found here: https://modrinth.com/app

Once downloaded, in the search bar you can search for 'Cobblemon GG' and it should be a pokeball logo with an Onix on it.




