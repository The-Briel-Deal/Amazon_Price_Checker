import bs4
import requests

gpu_link = requests.get(url='https://www.amazon.com/Giga-Graphics-Protection-WINDFORCE-DisplayPort/dp/B096YM573B/ref=sr_1_2?dchild=1&keywords=3070&qid=1627085235&sr=8-2',
                        headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
                                 "Accept-Language": "en-US,en;q=0.9"})

soupy_graphics = bs4.BeautifulSoup(markup=gpu_link.text, features='html.parser')
sg_price = soupy_graphics.select_one(selector='span#priceblock_ourprice').string
floaty_string = sg_price.removeprefix('$').replace(',', '')
floaty_float = float(floaty_string)
if floaty_float < 1300:
    print('less')