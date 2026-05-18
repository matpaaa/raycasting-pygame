

last_page = 'home'
current_page = 'home'
running = True

def navigatePage(page):
    global last_page,current_page
    last_page = current_page
    current_page = page