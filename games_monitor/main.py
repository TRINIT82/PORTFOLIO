#NEXT
import games_data.first_next_game_data as first_next_game
import games_data.sec_next_game_data as sec_next_game
#CURRENT
import games_data.first_current_game_data as first_current_game
import games_data.sec_current_game_data as sec_current_game
#UPDATES
import updates.next_game_update as next_game_updates
import updates.current_game_update as current_game_updates
#LOG
import logs
#GENRAL
import json

data = {
    "Next_Free_games" : [
        {
            "First_Game" : {
                
                "Name" : first_next_game.get_name(),
                "About": first_next_game.get_about(),
                "Original_Price": first_next_game.get_price(),
                "Release_date" : first_next_game.get_reldate(),
                "Expire_date" : first_next_game.get_expdate(),
            },
            
            "Second_Game" : {
                
                "Name" : sec_next_game.get_name(),
                "About": sec_next_game.get_about(),
                "Original_Price": sec_next_game.get_price(),
                "Release_date" : sec_next_game.get_reldate(),
                "Expire_date" : sec_next_game.get_expdate(),
            }
        }
    ],
    
    "Current_Free_games" : [
        
      {
        "First_Game" : {
            
            "Name" : first_current_game.get_name(),
            "About" : first_current_game.get_about(),
            "Original_Price" : first_current_game.get_price(),
            "Relsease_date" : first_current_game.get_reldate(),
            "Expire_date" : first_current_game.get_expdate()
        },
          
        "Second_Game" : {
            
            "Name" : None, #sec_current_game.get_name(),
            "About" : None, #sec_current_game.get_about(),
            "Original_Price" : None, #sec_current_game.get_price(),
            "Relsease_date" : None, #sec_current_game.get_reldate(),
            "Expire_date" : None #sec_current_game.get_expdate()
        } 
      }  
    ]
}

def update() -> None:
    with open("game_monitor/data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        print('Update Save - Succesed')
        
        
#Raise Log
logs.next_first_game()
logs.next_sec_game()
logs.current_first_game()
# logs.current_sec_game()

if next_game_updates.get_first_game_update() or next_game_updates.get_second_game_update() or current_game_updates.get_first_game_update() or current_game_updates.get_second_game_update():
    update()

'''
    З'єднуємо все до купи та записуємо в .json для зручності.
'''