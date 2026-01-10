import json
import games_data.first_next_game_data as first_next_game
import games_data.sec_next_game_data as sec_next_game

with open("game_monitor/data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

'''
    Робимо порівняння по назві гри, бо якщо змінилась назва то очевидно що гра теж змінилась і немає сенсу перевіряти ціну і таке інше.
    Бо API підганяє все сама.
'''
        
def get_first_game_update():
    if data['Next_Free_games'][0]['First_Game']['Name'] != first_next_game.get_name():
        return True
        
    else:     
        return False 

def get_second_game_update():
    if data['Next_Free_games'][0]['Second_Game']['Name'] != sec_next_game.get_name():
        return True
    
    else:
        return False     
    
'''
    Для оновлень:
    
    Можемо в модулі оновлення створити функцію нових данних, вона отримує нові данні і повертає в main оновлення, а в main ми перезаписуємо.
    
    Update:
    - Навіщо перезаписувати окремо, коли можна перезаписувати повністью, в повному перезаписі є сенс, БО якщо хоч 1 елемент оновиться то логічно що оновиться все!
    Epic Games - оновлюють ВЕСЬ каталог разом, тому потреби в окремому записі просто немає !
'''

