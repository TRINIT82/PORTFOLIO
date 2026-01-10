#NEXT
import games_data.first_next_game_data as first_next_game
import games_data.sec_next_game_data as sec_next_game

#CURRENT
import games_data.first_current_game_data as first_current_game
import games_data.sec_current_game_data as sec_current_game

#UPDATES
import updates.next_game_update as next_game_updates
import updates.current_game_update as current_game_updates

#Check Logic
def next_first_game():
    if next_game_updates.get_first_game_update() == True:
    
        print("We got [Next_First_Game] update !")
        print(f"New Game : ({first_next_game.get_name()})\n")

    else:
        print("[Next_First_Game] Nothing Changed\n")

def next_sec_game():
    if next_game_updates.get_second_game_update() == True:
    
        print("We got [Next_Second_Game] update !")
        print(f"New Game : ({sec_next_game.get_name()})\n")
    
    else:
        print("[Next_Second_Game] Nothing Changed\n")
        
def current_first_game():
    if current_game_updates.get_first_game_update() == True:
    
        print("We got [Current_First_Game] update !")
        print(f"New Game : ({first_current_game.get_name()})\n")
    
    else:
        print("[Current_First_Game] Nothing Changed\n")
        
def current_sec_game():
    if current_game_updates.get_second_game_update() == True:
    
        print("We got [Current_sec_Game] update !")
        print(f"New Game : ({sec_current_game.get_name()})\n")
    
    else:
        print("[Current_Second_Game] Nothing Changed\n")