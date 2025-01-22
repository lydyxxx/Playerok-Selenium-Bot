# Playerok API(Playwright browser)
___В процессе разработки, я принимаю ваши идеи для реализации в данный момент! Вы можете внести предложение в Pull Requests___ 

## Что-бы получить куки с сайта используйте расширение для Google Chrome EditThisCookies - https://chromewebstore.google.com/detail/editthiscookie-v3/ojfebgpkimhlhcblbalbfjblapadhbol

## profile_info() - Возвращает - баланс, активные продажи, сколько продано, имя пользователя

```python
from playerok_api import Playerok
import asyncio

async def main():
    playerok = Playerok()
    page = await playerok.loading_cookies('cookies.json')
    balance, it_count, sells, username = await playerok.profile_info(page)
    await playerok.close()
    print(f"Username: {username}")
    print(f"Balance: {balance}")
    print(f"Items count: {it_count}")
    print(f"Sell: {sells}")
    

if __name__ == "__main__":
    result = asyncio.run(main())


```

## messages() - Получает информацию о наличии новых сообщений - в случае отсутствия сообщений. Скрипт отправляет - None
```python
from playerok_api import Playerok
import asyncio

async def main():
    playerok = Playerok()
    page = await playerok.loading_cookies('cookies.json')
    username, chatlink = await playerok.messages(page)
    print(username, chatlink)
    await playerok.close()

    

if __name__ == "__main__":
    result = asyncio.run(main())


```


## sell() - Выставляет товар по заданым критериям
if Platno == True - выставляет платно(премиум лот)
if Platno == False - бесплатно выставляет товар
```python
from playerok_api import Playerok
import asyncio

async def main():
    playerok = Playerok()
    page = await playerok.loading_cookies('cookies.json')
    await playerok.sell(page, 'Категория', 'подкатегория', 'Название товара', 'Описание товара', 'Цена товара', 'Путь к изображению', 'Товарное описание при продаже', Platno=False)
    await playerok.close()

    

if __name__ == "__main__":
    result = asyncio.run(main())



```
# DON`T READ TAGS !!!!!!!
playerok, заработок, как заработать в интернете, заработок в интернете, как заработать, плеерок, как, как заработать школьнику, на, без вложений, как заработать в интернете без вложений, заработать, заработок в интернете без вложений, как заработать на playerok, как заработать на плеерок, funpay, заработок в интернете 2024, плеерке, заработок в интернете в 2024, фанпей, playerok проверка, заработок школьнику, деньги, заработок денег, brawl stars, как заработать денег, на плеерок, бравл старс, товары, заработок на фанпей, денег, без вложений плеерок, как заработать деньги в интернете, товары без вложений, без подъемов, товары для заработка без вложений, товары плеерок, товары для playerok, выдачи, авто, для, memes, как набрать отзывы, стим, кс го, купить акк кс го, автовыдача, топ 200 товаров, за месяц, на фанпей, товары для отзывов, товары фанпей, на funpay, товары для автовыдачи, в месяц, отзывов, 200 товаров для фанпей, кс го стим акк, большое количество отзывов в месяц!, получить, количество, большое, автовыдача фанпей, дешевый акк бравл старс, заработок на играх, заработок в интернете2024, заработок фанпей, мемы, товары для funpay 2023, мемы майнкрафт, консоль, console, beee minecraft, steveee minecraft, beee майнкрафт, steveee channel, канал beee, beee канал, майнкрафт мем, мем, купить аккаунт бравл старс, магазин на проверку, купить аккаунт war thunder, war thunder, игровой аккаунт, warthunder,


