import random
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

print("Welcome to Twitch Chat Bot\n"
      "Press enter to continue\n")
print("Close prompt the end program")
username = input("Enter Your UserName: ")
password = input("Enter Your Password: ")
channel_name = input("What is the channel name: ")
mature = input("Is this channel mature: ").lower()

chat_message = input(
    "Enter Messages to randomly send to Twitch Chat separate with comma (hi , morning) are two separate messages: ").split(
    ", ")
time_interval = input("Enter Time Interval(5 input = 5 seconds) (DEFAULT = 30sec): ")
background = input("Do you want to run the bot in the background(yes or no)").lower()
token_number = input("Enter Your Token:\n ")

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

tw = webdriver.ChromeOptions()
if background == "yes":
    tw.headless = True
    tw.add_argument("--mute-audio")
else:
    tw.headless = False
tw.add_argument(f'user-agent={user_agent}')
tw.add_argument("--window-size=1920,1080")
tw.add_argument('--ignore-certificate-errors')
tw.add_argument('--allow-running-insecure-content')

tw.add_argument("--disable-extensions")
tw.add_argument("--proxy-server='direct://'")
tw.add_argument("--proxy-bypass-list=*")
tw.add_argument("--start-maximized")
tw.add_argument('--disable-gpu')
tw.add_argument('--disable-dev-shm-usage')
tw.add_argument('--no-sandbox')
tw.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=tw)

driver.implicitly_wait(15)
driver.maximize_window()

# first page {

driver.get("https://www.twitch.tv/")
print("Bot in progress....\n")

# }

time.sleep(1)

# login {

driver.implicitly_wait(10)

login = driver.find_element(By.XPATH,
                            """//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button/div/div""")
login.click()
time.sleep(1)
user_name = driver.find_element(By.XPATH, """//*[@id="login-username"]""")
time.sleep(1)
pass_word = driver.find_element(By.XPATH, """//*[@id="password-input"]""")

user_name.send_keys(username)
time.sleep(1)
pass_word.send_keys(password)

login_click = driver.find_element(By.XPATH,
                                  """/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button/div/div""")
time.sleep(1)
login_click.click()

token = driver.find_element(By.XPATH,
                            """/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/div/div[1]/div/div[2]/input""")
token.send_keys(token_number)

submit = driver.find_element(By.XPATH,
                             """/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/div/div[2]/button/div/div""")
submit.click()

# }
time.sleep(1)


# Interval Chat Class
def chatt():
    i = 0
    while (i < 1, 20000):
        i += 1
        time.sleep(int(time_interval))
        chat = driver.find_element(By.CSS_SELECTOR, '[maxlength="500"]')

        s = random.choice(chat_message)
        chat.send_keys(s)

        post = driver.find_element(By.CSS_SELECTOR, '[data-a-target="chat-send-button"]')
        try:
            post.click()
            print(s)
            print("message posted\n")
            print(f"New message in {time_interval} secs\n ")


        except:
            print("post blocked")


# search

driver.implicitly_wait(5)
time.sleep(2)
bar = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search Input"]')
ActionChains(driver).move_to_element(bar).click(bar).perform()
ActionChains(driver).move_to_element(bar).click(bar).perform()
ActionChains(driver).move_to_element(bar).send_keys(channel_name).perform()

time.sleep(2)
enter = driver.find_element(By.XPATH, """//*[@id="search-result-row__0"]/div/div/a/div/div[2]""")
ActionChains(driver).move_to_element(enter).click(enter).perform()
time.sleep(1)

time.sleep(1.5)
if mature == "yes":
    mature = driver.find_element(By.CSS_SELECTOR, '[data-a-target="player-overlay-mature-accept"]')
    mature.click()

# }
time.sleep(1)

# chat {

try:
    chat = driver.find_element(By.CSS_SELECTOR, '[maxlength="500"]')
    chat.click()
    print(f"New message in {time_interval} secs\n ")
except:
    print("try again")

start_watching = driver.find_elements(By.CSS_SELECTOR, '[data-test-selector="chat-rules-ok-button"]')
for start in start_watching:
    if start.is_displayed():
        start.click()

chat = driver.find_element(By.CSS_SELECTOR, '[maxlength="500"]')
# }

chatt()

input()
