from app.store.save_store import *
from app.store.user_store import *

last_page = 'home'
current_page = 'home'
running = True
verify_code_email = None

save_store = SaveStore()
user_store = UserStore()

def navigate_page(page):
    global last_page,current_page
    if page == current_page: return
    
    last_page = current_page
    current_page = page
    
def back_page():
    global last_page,current_page
    if last_page:
        current_page = last_page
        last_page = None