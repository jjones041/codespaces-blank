# A Look at the Original Six Olympians
#### Video Demo: <https://youtu.be/r9itfG0tilc>

#### I took a Greek Mythology course at the University of Ottawa recently, so I've decided to base my final project on the six original Olympians. The program translates the original six Olympians Greek names into their Roman names, displays the gods genders, and asks the user for the god's weapon of choice. 

#### The program begins by prompting the user for one of the original six Olympian gods' Greek name. The program either prints the respective Greek gods' translated Roman name. If the user inputs an incorrect or uncapitalized name, the program exits. 

#### If the prior step is done correctly, the user will see the Roman name, and will be prompted to answer whether they're satisfied with the translation, if not the program exits, if they are satisfied then the program responds with the gods gender. 

#### After the gender is revealed, the user is hit with a pop quiz, asking for their gods typical weapon of choice. If the user answers correctly, then they are rewarded with a nice message, otherwise they must retry the whole program.

#### The program uses four lists which work together using .index() as each list is setup in the same order. The four lists contained:
#### - The original six Olympians Greek names
#### - The original six Olympians Roman names
#### - The original six Olympians genders
#### - The original six Olympians weapons of choice

#### The test_project.py file checks each formula to ensure they work correctly and the project.py file runs the program that is thoroughly explained above.
