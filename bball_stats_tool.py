from os import sep
import constants
import random
import sys

cleaned_player_list = []

players_guardians_names = []

panthers_players = []

bandits_players = []

warriors_players = []

num_players_team_balanced = int((len(constants.PLAYERS) / len(constants.TEAMS))/2)


def clean_data():
    for player in constants.PLAYERS:
        fixed = {}
        fixed["name"] = player["name"]
        fixed["guardians"] = player["guardians"].split()
        fixed["experience"] = player["experience"]
        fixed["height"] = player["height"]
        fixed["height"] = int(player["height"][0:2])
        if player["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        cleaned_player_list.append(fixed)
    players_guardians_names = []

    for player in cleaned_player_list:
        players_guardians_names.append(player["guardians"])


def balance_teams():
    global cleaned_player_list
    players_with_experience = []
    for player in cleaned_player_list:
        if player["experience"] == True:
            players_with_experience.append(player)
    players_without_experience = []
    for player in cleaned_player_list:
        if player["experience"] == False:
            players_without_experience.append(player)
    available_experienced_players = range(len(players_with_experience))
    available_inexperienced_players = range(len(players_without_experience))
    panthers_experienced_players_ids = random.sample(available_experienced_players, num_players_team_balanced)
    panthers_inexperienced_players_ids = random.sample(available_inexperienced_players, num_players_team_balanced)
    available_experienced_players = [id for id in available_experienced_players if id not in panthers_experienced_players_ids]
    available_inexperienced_players = [id for id in available_inexperienced_players if id not in panthers_inexperienced_players_ids]
    bandits_experienced_players_ids = random.sample(available_experienced_players, num_players_team_balanced) 
    bandits_inexperienced_players_ids = random.sample(available_inexperienced_players, num_players_team_balanced)
    available_experienced_players = [id for id in available_experienced_players if id not in bandits_experienced_players_ids]
    available_inexperienced_players = [id for id in available_inexperienced_players if id not in bandits_inexperienced_players_ids]
    warriors_experienced_players_ids = available_experienced_players
    warriors_inexperienced_players_ids = available_inexperienced_players
    global panthers_players, warriors_players, bandits_players
    panthers_players_experienced = [players_with_experience[id] for id in panthers_experienced_players_ids]
    panthers_players_inexperienced = [players_without_experience[id] for id in panthers_inexperienced_players_ids]
    panthers_players = panthers_players_experienced
    panthers_players.extend(panthers_players_inexperienced)
    bandits_players_experienced = [players_with_experience[id] for id in bandits_experienced_players_ids]
    bandits_players_inexperienced = [players_without_experience[id] for id in bandits_inexperienced_players_ids]
    bandits_players = bandits_players_experienced
    bandits_players.extend(bandits_players_inexperienced)
    warriors_players_experienced = [players_with_experience[id] for id in warriors_experienced_players_ids]
    warriors_players_inexperienced = [players_without_experience[id] for id in warriors_inexperienced_players_ids]
    warriors_players = warriors_players_experienced
    warriors_players.extend(warriors_players_inexperienced)
    #Note to Treehouse grader: This thread on the Treehouse forums helped me conceptualize how I to create this function:
    #https://teamtreehouse.com/community/appending-random-items-from-one-list-to-another-while-excluding-items-that-were-already-appended-to-a-previous-list

def display_welcome_message_to_console():
    print("\nBASKETBALL TEAM STATS TOOL")
    print("\n--- MENU ---")
    print("\nHere are your choices:")
    print("\nA) Display Team Stats")
    print("B) Quit")
    print("\nType either the letter A or the letter B, and press enter.")
    while True:
        try:
            select_option = (input("\nEnter an option: "))
            if not any(entry in select_option.lower() for entry in("a", "b")):
                raise ValueError("Please enter only the letter A, or the letter B.")
            if len(select_option) > 1:
                raise ValueError("Please enter only a single letter: A or B.")
        except ValueError as err:
            print("Oh no! We ran into an issue. {}".format(err))
        else:
            if select_option.lower() == "a":
                break
            if select_option.lower() == "b":
                print("OK! The program will be closing down now.")
                sys.exit()


def display_a_teams_stats():
    while True:
        print("\nTEAMS")
        print("A) Panthers")
        print("B) Bandits")
        print("C) Warriors")
        try:
            select_option = (input("\nEnter a letter (A for Panthers, B for Bandits, or C for Warriors) "))
            if not any(entry in select_option.lower() for entry in ("a", "b", "c")):
                raise ValueError("Please enter only the letter A, B, or C.")
            if len(select_option) > 1:
                raise ValueError("Please enter only a single letter: A, B, or C.")
        except ValueError as err:
            print("Oh no! We ran into an issue. {}".format(err))
        else:
            global panthers_players, warriors_players, bandits_players
            def display_a_specific_teams_stats():
                if select_option.lower() == "a":
                    display_teamname = "PANTHERS"
                    original_list = panthers_players
                if select_option.lower() == "b":
                    display_teamname = "BANDITS"
                    original_list = bandits_players
                if select_option.lower() == "c":
                    display_teamname = "WARRIORS"
                    original_list = warriors_players
                print("\n{} STATS: ".format(display_teamname))
                print("-----------")
                print("Total players: {}".format(len(original_list)))
                list_players_with_experience = []
                for player in original_list:
                    if player["experience"] == True:
                        list_players_with_experience.append(player)
                print("Total experienced: {}".format(len(list_players_with_experience)))
                list_players_without_experience = []
                for player in original_list:
                    if player["experience"] == False:
                        list_players_without_experience.append(player)
                print("Total experienced: {}".format(len(list_players_without_experience)))
                list_of_players_heights = []
                for player in original_list:
                    list_of_players_heights.append(player["height"])
                average_player_height = sum(list_of_players_heights)/len(list_of_players_heights)
                print("Average height: {} inches".format(round(average_player_height, 1)))
                print("\nPlayers on team: ")
                players_names = []
                for player in original_list:
                    players_names.append(player["name"])
                print(*players_names, sep= ", ")
                print("\nGuardians:")
                players_guardians = []
                for player in original_list:
                    players_guardians.append(player["guardians"])
                players_guardians_list = [" ".join(entry) for entry in players_guardians]
                print(*players_guardians_list, sep = ", ")
            display_a_specific_teams_stats()
            while True:
                try:
                    option_to_display_menu_again = input(
                        "\nWould you like to get back to the main menu? Enter yes or no: ")
                    if not any(entry in option_to_display_menu_again.lower() for entry in ("yes", "no")):
                        raise ValueError("Please enter only yes or no.")
                    if len(option_to_display_menu_again) > 3:
                        raise ValueError("Please enter only yes or no.")
                except ValueError as err:
                    print("Oh no! We ran into an issue. {}".format(err))
                    continue
                else:
                    if option_to_display_menu_again.lower() == "yes":
                        display_welcome_message_to_console()
                        display_a_teams_stats()
                    if option_to_display_menu_again.lower() == "no":
                        print("OK! The program will be closing down now.")
                        sys.exit()
                    #Note to Treehouse grader: This thread on the Treehouse forums helped me conceptualize a solution for printing the guardians list:
                    #https://teamtreehouse.com/community/in-a-print-statement-with-a-sep-parameter-the-values-are-not-being-separated-why-is-this-happening
            

def main():
    clean_data()
    balance_teams()
    display_welcome_message_to_console()
    display_a_teams_stats()


if __name__ == "__main__":
    main()

