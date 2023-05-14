# Intelligent terminal TicTacToe game

My version of tic-tac-toe has two main modes: one with two human opponents who take turns filling an empty square with their piece, and the other with a human (you) against an artificial intelligence.

### project description:
My project is my own implementation of a tic-tac-toe game in order to assimilate previously learned skills such as python and algorithm, and others.
I used Python to build this project because its purpose was to put into practice the skills I had learned so far. Also, it was built following the MVC design pattern to facilitate eventual integration of a better view and debugging/error handling.

### how to install and run it?
- Clone this repository
- run the file main.py, which is like the main file : python3 main.py (this may vary depending on your python version)

### how to use the project?
At the beginning of the game, we are asked to choose between {1, 2}, i.e. 1 for human versus AI and 2 for human versus human.
If we have chosen 1, we are prompted again to choose our avatar, either an "X" cross or an "O" cycle, and the avatar with an X sign ALWAYS places its piece first.
Note: The sleep time of 1 second was set on purpose and serves as a sort of bottleneck for further development of the other levels. The artificial intelligence is based on the minimax algorithm.
Otherwise, if we choose 2, we are directly asked for X's next move, or rather his first move. And so forth.
The format of a move is a string consisting of a single letter in {A, B, C} followed by a number from 1 to 3. For example, the top leftmost cell is labeled A1, and the bottom rightmost cell is C3, ...

### eventual update:
Further work on this project could include adding two additional levels: easy and hard.








This project is licensed under the Attribution-NonCommercial license.