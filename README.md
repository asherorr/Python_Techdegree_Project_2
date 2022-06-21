PROJECT TITLE: BASKETBALL STATS TOOL

---TABLE OF CONTENTS---
SECTION 1: GENERAL INFO
SECTION 2: TECHNOLOGIES
SECTION 3: LICENSE

SECTION 1: GENERAL INFO

This is my second project in the Python TechDegree program at Treehouse. I'm so excited to share it with you!

The file app.py imports a file called bball_stats_tool.py. The latter file contains a script that imports data about 18 basketball players, cleans the data, and distributes the players across 3 teams. Each team is balanced- no team has more or less players than the other two. Furthermore, each team has the same number of experienced players and inexperienced players.

Once the teams are balanced, the user can view any team's stats. The console prints out:

- The team's name
- The total number of players
- The number of experienced players
- The number of inexperienced players
- The average height of the team (in inches)
- The name of each player on the team
- The name of each player's guardian

The file bball_stats_tool.py contains 5 functions. Below, I go into detail about each one:

Function 1: clean_data()

The file constants.py contains the original data for each player. It is a list of dictionaries, with each dictionary including key:value pairs for the player's name, their guardian's name, the player's experience (Yes or No), and the player's height.

The clean_data function loops through each dictionary in the file "constants.py." It creates a new dictionary for each player, called "fixed," and it adds a new key:value pair for each category of data (name, guardians, experience, and height.)

While creating key:value pairs for the "fixed" dictionary, the guardian's string is split into a list, height is converted into an integer, and the player's experience is converted into a Boolean value (True or False.) This is to help with data processing later.

Lastly, the updated dictionary for each player is added to a list titled cleaned_player_list.

-----------------------------------------------------------------------------

Function 2: balance_teams()

Now that each player's data is cleaned, it's time to "balance" the teams. By this, I mean distributing an equal number of players to each team (and ensuring that each team has the same number of experienced and inexperienced players.)

The balance_teams function creates 2 lists: players with experience, and players without experience.

The function loops through each player in cleaned_player_list. The players with experience are added to the players_with_experience list, whereas the players without experience are added to the players_without_experience list.

Then 2 variables appear:

 1. available_experienced_players
 - This is assigned a range of the length [players_with_experience]
 2. available_inexperienced_players
 - This is assigned a range of the length [players_without_experience]

In the constants.py file, there were 3 teams: Panthers, Bandits, and Warriors. To assign an equal number of experienced and inexperienced players to each team, I created 2 lists:

 List 1: {team_name}_experienced_players_ids
 List 2: {team_name}_inexperienced_players_ids
 
 For my first team, the Panthers, I took the variable panthers_experienced_players_ids and assigned it a random sample of index values from available_experienced_players, with the k value "num_players_team_balanced."

I then took the variable panthers_inexperienced_players_ids and assigned it a random sample of index values from available_inexperienced_players, with the k value num_players_team_balanced.

num_players_team_balanced is the length of "players" in constants.py, divided by the length of "teams" in constants.py. Then that number is divided by 2. 

In other words, it's the total number of players divided by the total number of teams. This returns "6", since there are 18 players and 3 numbers of team. 6 is then divided by 2, since each team needs an equal number of experienced (3) and inexperienced (3) players. 

Then I used list comprehension to update the range of values in available_experienced_players and available_inexperienced players:

available_experienced_players = [id for id in available_experienced_players if id not in panthers_experienced_players_ids]

available_inexperienced_players = [id for id in available_inexperienced_players if id not in panthers_inexperienced_players_ids]

I repeated the process for the Bandits and Warriors teams.

For my first team (Panthers), I made 2 lists: panthers_players_experienced, and panthers_players_inexperienced. I used list comprehension to populate these lists:

panthers_players_experienced = [players_with_experience[id] for id in panthers_experienced_players_ids]

panthers_players_inexperienced = [players_without_experience[id] for id in panthers_inexperienced_players_ids]

Then I added the lists "panthers_players_experienced" and "panthers_players_inexperienced" to a list called panthers_players. I repeated the process with the Bandits and Warriors teams.

-----------------------------------------------------------------------------

Function 3: display_welcome_message_to_console():

Users are now prompted by the display_welcome_message_to_console() to either:

- Display a Team's Stats
OR
- Quit

This function also contains a try block to catch any input errors. If the user chooses to display a team's stats, they are taken to the next function: display_a_teams_stats()

If they choose to quit, a sys.exit() command executes.

-----------------------------------------------------------------------------

Function 4: display_a_teams_stats()

If the user chose to display a team's stats, this function prints:

"TEAMS:
A) Panthers
B) Bandits
C) Warriors

Enter a letter (A for Panthers, B for Bandits, or C for Warriors)"

If they enter anything except the letter A, B, or C, a try block raises a ValueError.

When they enter the correct letter, the console prints out:

- The team's name
- The total number of experienced players
- The total number of inexperienced players
- The average height of the team in inches
- The name of each player on the team
- The name of each player's guardian

Then the user is asked "Would you like to get back to the main menu? Enter yes or no."

Entering "yes" will take the user back to function 3: display_welcome_message_to_console. 

Entering "no" will close the program. A try block also exists in this function to catch any input errors.

-----------------------------------------------------------------------------

Function 5: main()
This simply ensures the script doesn't automatically execute when imported. 

The file app.py contains this code:

~~~
import bball_stats_tool


bball_stats_tool.main()
~~~

The main() function in bball_stats_tool contains the clean_data, balance_teams, display_welcome_message_to_console, and display_a_teams_stats functions. 

Thus, all of bball_stats_tool will execute when the script app.py is run.


SECTION 2: TECHNOLOGIES

Project is created with:
- Python

SECTION 3: LICENSE

Copyright (c) [2022] [Stephen Asher Orr]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
