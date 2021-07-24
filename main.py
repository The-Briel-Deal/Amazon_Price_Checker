import bs4
import requests
import threading
from time import sleep


def pull_price(url, threshold):
    gpu_link = requests.get(url=url,
                            headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, "
                                                   "like Gecko) Chrome/91.0.4472.77 Safari/537.36",
                                     "Accept-Language": "en-US,en;q=0.9",
                                     "ACCEPT": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
                                               "image/webp,image/apng,*/*;q=0.8,"
                                               "application/signed-exchange;v=b3;q=0.9",
                                     'cookie': "session-id=140-6872833-3827750; skin=noskin; "
                                               "ubid-main=134-9204787-6969449; "
                                               "x-main=\"R4gnw?ZU0dc6BG@qk?O5Jgs6fUfG@oeKcUwWaSPxAm7m7O0qljL"
                                               "@1DA8ESs0FM8W\"; "
                                               "at-main=Atza"
                                               "|IwEBIJO9wv6_JmIruaW1_jFurWCQakFO7rbbm9JWspG8XhVGwqfqFmZdPS"
                                               "-u1NfkE4gMUI1CVBs8arzkYP1ukZb7T_DpU8Y8IbUovgFI2nP9xHtSx2DL78mkkm"
                                               "Wht5wLhSVj0evEg2BU8py2-RabhNXgXtUmFRx3gUguY1L1b9yx9otLNOGwGoVM5qI1Whu"
                                               "UAb2oAY7NPqxpJimPG32iMLCoN24Y; sess-at-main=\"/LNLUb315VkTxg9zqyaXO8"
                                               "if8o+lXRlZKtWyxJUqn9Y=\"; sst-main=Sst1|PQEWp4L-VNAd-BRuRPgTK-3jCTlPB"
                                               "Qggq_GzdNw4OIvm5dfUL6hxcXL4A00mHrGEvzCX1c_tb73qo0pVCH4JNAK481c0LRIdis"
                                               "cTtNr3KcLq4C91fiOJWj2_nh7FwmjW2Rs31rEOt8qVEH-BIerZbbqcCcH1x_WJlb7F0Xq"
                                               "142hV0FnIVDwJfwKlwFC4B_krkzKbM0Vkdcba6TUt_oawVvLqrz2pKW_mFzDfLDZo8_kR"
                                               "IlMj0pqHE27EpdzpPRKaOqvUYUVrvclqJy_eQuPBQBh4O6o9JJVGe8Zu7lh-A0DAH_Q;"
                                               "lc-main=en_US; session-id-time=2082787201l; i18n-prefs=USD; "
                                               "session-token=\"+ABdt2ZZIwt9TgWjzQTyvIX1AJ5rRLY2z7fwMm0"
                                               "/Px1Wn5s0hP0nkAVpINFctKh8N4UQ4IxYYVOeyN5fpfyu6MJy"
                                               "/Rqkitgw1jaTuzm4qakeYc8TVOV62svrtpANF8NptwieUwNdD/FLlcsC2AZw"
                                               "/YLgW6fRBwf7dRNyQKwGvhi8GttYZZpkE3i0hrW60v4gcmVUyzQcB8h7+sUXFMyNjg"
                                               "==\"; "
                                               "csm-hit=tb:C3SP7ZMKDEXZJP7396QV+s-23EGG1EPPR0YDYW5Y861|1627145047227"
                                               "&t:1627145047227&adb:adblk_yes"})
    soupy_graphics = bs4.BeautifulSoup(markup=gpu_link.text, features='html.parser')
    sg_price = soupy_graphics.select_one(selector='span#priceblock_ourprice').string
    sg_name = soupy_graphics.select_one(selector='span#productTitle').string
    floaty_string = sg_price.removeprefix('$').replace(',', '')
    price = float(floaty_string)
    sg_name = sg_name.replace('\n', '')
    name = sg_name[:30]
    tf_below_thresh = threshold > price
    return price, name, tf_below_thresh


tf = True


def query_info(url):
    global tf
    while tf:
        print(pull_price(url, 1250))
        sleep(10)
    print('Im done looping!!!')

link = (str(input('What amazon link would you like notifications on?\n')))
thread1 = threading.Thread(target=query_info, args=(link,))


def test_func():
    global tf
    while True:
        if input('Enter EXIT to exit\n').upper() == 'EXIT':
            tf = False



thread2 = threading.Thread(target=test_func)

thread1.start()
thread2.start()
