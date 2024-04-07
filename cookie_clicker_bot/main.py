from cookie import Cookie
import time

URL = "https://orteil.dashnet.org/experiments/cookie"

timeout = time.time_ns() + 5*60
break_out = time.time_ns() + 50


cookie_bot = Cookie(URL)
while True:
    cookie_bot.click_cookie()

    if time.time_ns() > break_out:
        cookie_bot.buy_addons()
        break_out = time.time_ns() + 50

    # if time.time_ns() > timeout:
    #     break











