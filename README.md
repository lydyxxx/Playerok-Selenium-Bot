# Playerok API(Playwright browser)
___In the process of development, I accept your ideas for implementation at this time! You can make a suggestion in Pull Requests___ 

## profile_info() - Returns -  Balance, Active Sales, How Many Sold, Username

```python
from tests import Playerok
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

## messages() - Gets information whether there are new messages - in case there are no messages. The script sends - None
```python
from tests import Playerok
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


