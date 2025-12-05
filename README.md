Project Title: Snake Game <br>
Team Members: <br>
•	Jayuna Khatiwada<br>
•	Manoj Kumar Cherukuneedi <br><br>
Description:<br>
This is the classic snake game which is created using Pygame library in Python. The objective is to simply control the sanke on the screen,
eat the orange/red food blocks to grow longer and achieve score. The snake moves on a fixed screen size, and the game ends if snake collides
with itself or the end of the screen. Initially, the game is not started unless done as instructed and there is an instruction to restart the game
if the game over screen pops up.<br><br>
Control: <br>
To move snake in a particular direction use the particular arrow in the keyboard. Like up for upward direction, left for left direction and so on. 
Initially to start the game you can press any key on the keyboard. After game over is displayed you need to press r key and any key on the keyboard 
to restart the game. Help menu is also available in case of any confusion.<br><br>
Checklist<br>
•	Game loop : For running the game continuously until user wants to close it<br>
•	Snake mechanics: Drawing snake on the screen, moving it on the screen based on key press, growth upon eating foods<br>
•	Collision detection: Detecting self and end of screen snake collision<br>
•	Food spawning: Food randomly spamming on the screen and reset the location after being eaten.<br>
•	Score display: Displaying score after the food is eaten on the screen.<br>
•	Help screen: For knowing the control and objective of the game<br><br>
Division of work:<br>
•	Jayuna: <br>
o Created game loop,<br>
o	 snake movement, <br>
o	collision detection with wall<br>
o	Added background image and help box<br>
o	Power point presentation and README<br><br>
•	Manoj:<br>
o	Created  all the codes related to food<br>
o	Collision detection with snake<br>
o	Snake length increment<br>
o	Score display and Game over screen<br><br>
Enhancement:<br>
•	Adding audio after food being eaten and collision with the wall or snake<br>
•	Adding high score variable on the screen<br>
•	Improving the visual design of the snake as well as snake<br><br>
Bugs:<br>
•	The collision detection is not perfect<br>
•	The restart and initial screen both being shown after restarting the game<br>
•	Game not being paused when help is clicked while the game is already started<br>

