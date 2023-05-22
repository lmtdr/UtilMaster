# UtilMaster
Essential tool that creates config which provides better utility control in CS:GO

With the output config provided from my program, you will be able to have multiple actions on a single key for your utility.
All you need to do is to input your keybinds for each grenade and also three inputs for keys that will work as a "combinators".

By holding each of the combinator, you can do the following actions:
1) drop specific utility
2) buy specific utility
3) drop specific utility from market menu
And ofcourse, select specific utility by just pressing the key bind of your utility.

My binds are:
molotov: X
smoke: Y
flash: C
nade: V
combinator1: mouse4
combinator2: mouse5
combinator3: mouse3

For example, if i want to drop a flash around the corner i am about to peek without the need to select it manually, i hold mouse4 and press C.
It will execute the action for me automatically and i am able to get a good peek on timing when enemy is most likely turned around or in shock.

If you want for some reason to compile my python script yourself, do it trough pyinstaller along with these parameters:
pyinstaller --onefile --window --icon=favicon.ico --add-data "template.txt;." --add-data "favicon.ico;." --add-data "background.png;." hello.py
