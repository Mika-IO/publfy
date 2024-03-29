from playwright.sync_api import sync_playwright
import urllib 
from random_files.numbers import all_contacts
from pitch_messages import start_message

def send_messages(text, contacts):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        text = urllib.parse.quote(text)
        for contact in contacts:
            link = f"https://web.whatsapp.com/send?phone={contact}&text={text}"
            print("Enviando: {}")
            print(link)
            page.goto(link)
            page.wait_for_selector('#side', state='attached', timeout=100000)

            if not page.is_visible('text="Phone number shared via url is invalid."'):

                page.wait_for_selector('span[data-icon="send"]', state='visible', timeout=100000)
                
                page.click('span[data-icon="send"]')

            page.wait_for_timeout(5000)
            
        browser.close()

send_messages(start_message, all_contacts)
