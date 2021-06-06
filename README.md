# LSRP Paycheck Farmer


This python automation was created for the game San Andreas Multiplayer and in particular the Los Santos Roleplay community.

Problem statement: 

* Characters are given a "paycheck" for playing for a total of 20 minutes / hour, at approximately :00-:02 of every hour. 
* After completing ~1000 of those, your character automatically becomes a millionaire.
* To prevent abuse, the server automatically kicks people if they don't move for 3-4 minutes. In addition, administrators spectate players to ensure that they're not AFK.
* If you are caught using macros or any form of cheating to avoid the anti-kick system, the administrators will ban you from the game.

How this script bypasses all security measures and has been tested to farm over ~4000 hours undetected:
1. Logs in at a random time to prevent pattern recognition software/spectators from detecting it as a bot.
2. Stays logged in for a random amount of time between 20-25 minutes.
3. While logged in, it moves completely randomly from a set of pre-defined moves.
4. If the bot detects that an administrator has contacted the player to ask whether they're here or afk, it will respond with a random response, and then forcefully terminate the process to appear as though they lost internet connection.
5. The game will automatically minimize itself after every random moveset in order to allow for the user to watch videos/movies and in general utilize their computer while the bot farms the paychecks.
