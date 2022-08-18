## Enemy Randomizer v3 by Echocolat

Shoutouts to __ArchLeaders__ for huge help with the code, and to __MintLightning__ as well.

### What is Enemy Randomizer

Enemy Randomizer is a mod that replaces every single non-problematic enemy with another random one. Their  
weapon is randomized as well. There are options you can change in `resources\config_randomizer.json` which  
are the following (with explanations) :  
* randomizeMainField : Decide whether or not the main map enemies should be randomized.
* randomizeShrines : Decide whether or not the non-dlc shrine enemies should be randomized.
* randomizeDLCShrines : Decide whether or not the dlc shrine enemies should be randomized.
* randomizeDivineBeasts : Decide whether or not the divine beast enemies (not final) should be randomized.
* randomizeTrials : Decide whether or not the ToS enemies should be randomized.
* bossProb : The ratio Normal enemies / Bosses in number. High numbers might crash the game / raise Panic Blood Moons.
* chaosMode : Makes every enemy have the same weight in the randomization. (bosses still spawn at 1/bossProb rate).
* autoinstall : Decide whether or not the script should auto install the mod with BCML.

There is another config file, `resources\config_enemy_weights.json` whose name is pretty self-explanatory.  
You can modify the weights of the enemies in the randomization. Warning : __Bosses and enemies have__  
__separate pools.__  

### How to use it

Install the modules `botw_flag_util`, `oead` and `bcml` (`pip install [module]`).  
There are two modes of utilisation; the "vanilla mode", which simply takes files in your game dump (using BCML),  
and the "modded mode", which takes files that YOU will take and put in a special folder, and will randomize using it.  
This allows to randomize enemies from another mod, but it will take more steps. More details below.  

##### Vanilla Mode

Modify `config_randomizer.json` and / or `config_enemy_weights` as you please, and launch `main_vanilla_mode.py`.  
Wait until it finishes; if you don't use autoinstall, drag the `rules.txt` into the newly created Enemizer folder,  
and install it later with BCML. If you do use autoinstall, you can just activate the mod and enjoy.

##### Modded Mode

Work In Progress

#### Conclusion

I hope you will enjoy the mod. If there is any problem with the installation, make sure the `oead`, `botw_flag_util`  
and `bcml` modules are installed on your computer. If there's still problems, contact me through Discord (@Echocolat#998)  
or commentate on the GameBanana page of the mod. You should favor Discord, since I'm not always on GameBanana.  

##### Enjoy !