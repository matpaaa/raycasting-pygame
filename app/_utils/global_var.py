from app.store.save_store import *
from app.store.user_store import *

last_page = 'home'
current_page = 'home'
running = True

save_store = SaveStore()
user_store = UserStore()

def navigatePage(page):
    global last_page,current_page
    last_page = current_page
    current_page = page