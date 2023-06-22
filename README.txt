Solution written in python version 3.8.10

Project structure:
    ├── game
    │   ├── game.py
    │   ├── item.py
    │   ├── knight.py
    │   └── tile.py
    ├── main.py
    ├── moves.txt
    ├── README.txt
    ├── requirments.txt
    ├── results.json
    └── test.py


Assumptions Made: 
    - Attack and defence scores are not combined and not carried over
    - item modifiers are added to attack/defence only once during equipping
    - a tie would be a death to the defender 
    - There can only be one live knight per tile

How to run:
    - in this current directory run 'python main.py'
    - no special packages were used however to reduce any errors run 'pip install -r requirments.txt"
    - output will go to results.json and will be printed in the terminal
