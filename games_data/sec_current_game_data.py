from epicstore_api import EpicGamesStoreAPI

def get_name():
    try:
        api = EpicGamesStoreAPI()
        api_data = api.get_free_games()
        sec_current_game_name = api_data['data']['Catalog']['searchStore']['elements'][9]['title']
    
        return sec_current_game_name
    except(IndexError):
        return None

def get_about():
    try:
        api = EpicGamesStoreAPI()
        api_data = api.get_free_games()
        sec_current_game_expdate = api_data['data']['Catalog']['searchStore']['elements'][9]['description']
    
        return sec_current_game_expdate
    
    except(IndexError):
        return None

def get_price():
    try:
        api = EpicGamesStoreAPI()
        api_data = api.get_free_games()
        sec_current_game_price = api_data['data']['Catalog']['searchStore']['elements'][9]['price']['totalPrice']['fmtPrice']['originalPrice']
    
        return sec_current_game_price
    
    except(IndexError):
        return None

def get_reldate():
    try:
        api = EpicGamesStoreAPI()
        api_data = api.get_free_games()
        sec_current_game_reldate = api_data['data']['Catalog']['searchStore']['elements'][9]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate']
    
        return sec_current_game_reldate
    
    except(IndexError):
        return None

def get_expdate():
    try:
        api = EpicGamesStoreAPI()
        api_data = api.get_free_games()
        sec_current_game_expdate = api_data['data']['Catalog']['searchStore']['elements'][9]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate']
    
        return sec_current_game_expdate
    
    except(IndexError):
        return None

# def dev():
#     api = EpicGamesStoreAPI()
#     api_data = api.get_free_games()
#     return api_data['data']['Catalog']['searchStore']['elements'][1]['title']

# print(dev())

'''
    Переміщення по категорії '.get_free_games()' за шляхом :
    
    ['data']['Catalog']['searchStore']['elements'][index]
    index : 0 - 10
    
    Приклад в dev()
    
    Уточнення!
    На 9-10 індексах знаходяться нові ігри які скоро вийдуть у безкоштовний доступ.
    На 0 Індексі знаходиться поточна гра.
    
    В новорічний розпродаж трохи по іншому:
    0 - Гра яка скоро поступить.
    9-10 - Поточні.
'''