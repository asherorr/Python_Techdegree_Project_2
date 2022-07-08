from os import sep
import constants
import random
import sys

cleaned_player_list = []

panthers_players = []

bandits_players = []

warriors_players = []

num_players_team_balanced = int(
    (len(constants.PLAYERS) / len(constants.TEAMS))/2)


def clean_data():
    for player in constants.PLAYERS:
        fixed = {}
        fixed["name"] = player["name"]
        fixed["guardians"] = player["guardians"].split(" and ")
        fixed["experience"] = player["experience"]
        fixed["height"] = player["height"]
        fixed["height"] = int(player["height"][0:2])
        if player["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        cleaned_player_list.append(fixed)


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
    global panthers_players, warriors_players, bandits_players
    teams = constants.TEAMS
    for team in teams:
        if team == "Panthers":
            list_players = panthers_players
        if team == "Bandits":
            list_players = bandits_players
        if team == "Warriors":
            list_players = warriors_players
        random.shuffle(players_with_experience)
        random.shuffle(players_without_experience)
        for player in players_with_experience[0:int(num_players_team_balanced)]:
            list_players.append(player)
            players_with_experience.pop(0)
        for player in players_without_experience[0:int(num_players_team_balanced)]:
            list_players.append(player)
            players_without_experience.pop(0)


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
            if not any(entry in select_option.lower() for entry in ("a", "b")):
                raise ValueError(
                    "Please enter only the letter A, or the letter B.")
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
            select_option = (
                input("\nEnter a letter (A for Panthers, B for Bandits, or C for Warriors) "))
            if not any(entry in select_option.lower() for entry in ("a", "b", "c")):
                raise ValueError("Please enter only the letter A, B, or C.")
            if len(select_option) > 1:
                raise ValueError(
                    "Please enter only a single letter: A, B, or C.")
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
                print("Total experienced: {}".format(
                    len(list_players_with_experience)))
                list_players_without_experience = []
                for player in original_list:
                    if player["experience"] == False:
                        list_players_without_experience.append(player)
                print("Total inexperienced: {}".format(
                    len(list_players_without_experience)))
                list_of_players_heights = []
                for player in original_list:
                    list_of_players_heights.append(player["height"])
                average_player_height = sum(
                    list_of_players_heights)/len(list_of_players_heights)
                print("Average height: {} inches".format(
                    round(average_player_height, 1)))
                print("\nPlayers on team: ")
                players_names = []
                for player in original_list:
                    players_names.append(player["name"])
                print(*players_names, sep=", ")
                print("\nGuardians:")
                players_guardians = []
                for player in original_list:
                    players_guardians.append(player["guardians"])
                players_guardians_list = [
                    ", ".join(entry) for entry in players_guardians]
                print(*players_guardians_list, sep=", ")
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
