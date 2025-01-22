import asyncio, json, requests, re 
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
from colorama import Fore, Style

class Playerok:
    def __init__(self):
        self.nd = None
    
    
    async def load_cookies(self, cookies_file):
        with open(cookies_file, 'r') as f:
            cookies = json.load(f)
        
        for cookie in cookies:
            if cookie.get('sameSite') is None:
                cookie['sameSite'] = 'None'
            elif cookie['sameSite'] == 'no_restriction':
                cookie['sameSite'] = 'None'
            elif cookie['sameSite'] not in ['Strict', 'Lax', 'None']:
                cookie['sameSite'] = 'Lax'  
        return cookies
    
    def filter_text(self, text):
        return re.sub(r'[^\u0000-\uFFFF]', '', text)
    
    async def profile_info(self, page, max_retries=3):
        retries = 0
        while retries < max_retries:
            try:
                await page.goto('https://playerok.com/profile')
                await asyncio.sleep(2)

                username_element = await page.query_selector("span.MuiTypography-root.MuiTypography-20.mui-style-111p9a6")
                balance_element = await page.query_selector(".MuiBox-root.mui-style-s9g809 .MuiTypography-16.mui-style-13jxvcr")
                tovars_element = await page.query_selector(".MuiTypography-root.MuiTypography-14.mui-style-pwnbg9")
                prodazhi_element = await page.query_selector("#next-modal > div.MuiBox-root.mui-style-1i48s3q > div.MuiBox-root.mui-style-159csam > div > div > a:nth-child(3) > div > p > span.MuiTypography-root.MuiTypography-14.mui-style-s8sapl")

                if not (username_element and balance_element and tovars_element and prodazhi_element):
                    raise Exception("Не удалось найти один или несколько элементов профиля")

                username = await username_element.inner_text()
                balance = await balance_element.inner_text()
                tovars = await tovars_element.inner_text()
                prodazhi = await prodazhi_element.inner_text()

                return balance, tovars, prodazhi, username

            except Exception as e:
                #print(f"Ошибка при получении информации профиля: {e}")
                retries += 1
                if retries < max_retries:
                    #print(f"Повторная попытка {retries}/{max_retries}...")
                    await asyncio.sleep(2)  # Задержка перед повторной попыткой
                else:
                    #print("Превышено максимальное количество попыток")
                    return None, None, None, None
                
    async def sell(self, page, category, categoryosn, nazvanie, opisanie, tsena, img_path, s, Platno=None):
        await page.goto('https://playerok.com/sell')
        
        try:
            await page.wait_for_selector("div.MuiBox-root.mui-style-16442oc")
        except Exception:
            return
        
        await asyncio.sleep(2)

        elements = await page.query_selector_all("div.MuiBox-root.mui-style-16442oc")
        for element in elements:
            try:
                name_element = await element.query_selector("p.MuiTypography-root.MuiTypography-body1.mui-style-ji33ly")
                if await name_element.inner_text() == category:
                    await element.click()
                    break
            except Exception:
                continue
        await asyncio.sleep(2)
        
        
        ctg2 = await page.query_selector_all("label.MuiBox-root.mui-style-xcklu4")
        for element in ctg2:
            try:
                name_element = await element.query_selector("span.MuiTypography-root.MuiTypography-16.mui-style-mnmbnr")
                if await name_element.inner_text() == categoryosn:
                    await element.click()
                    break
            except Exception:
                continue
        
        await asyncio.sleep(3)
        
        try:
            cont = await page.query_selector("button.MuiBox-root.mui-style-16ty3xs")
            if cont:
                await cont.scroll_into_view_if_needed()
                await asyncio.sleep(4)
                await cont.click()
            else:
                print("Ошибка: Кнопка продолжения не найдена.")
                return
            
            
            await asyncio.sleep(4)

            file_input = await page.query_selector("input[type='file'][accept='image/*']")
            if file_input:
                await file_input.set_input_files(img_path)

            tsena_filtered = self.filter_text(tsena)
            nazvanie_filtered = self.filter_text(nazvanie)
            opisanie_filtered = self.filter_text(opisanie)
            s_filtered = self.filter_text(s)

            await page.fill("#item-price", tsena_filtered)
            await page.fill("input[name='title']", nazvanie_filtered)
            await page.fill("textarea[name='description']", opisanie_filtered)
            await page.fill("textarea[name='textData']", s_filtered)

            await page.click("button.MuiBox-root.mui-style-16ty3xs")
            print(Fore.GREEN + "Данные для продажи введены." + Style.RESET_ALL)

            if Platno:
                print(Fore.GREEN + "Оплачиваю лот..." + Style.RESET_ALL)
                await asyncio.sleep(1.5)
                await page.click("button.MuiBox-root.mui-style-16ty3xs")
                btn = await page.wait_for_selector("button.MuiBox-root.mui-style-p0ojd3", state='visible')
                await btn.click()
                print(Fore.GREEN + "Оплата прошла успешно." + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "Бесплатно выставляю лот..." + Style.RESET_ALL)
                freebtn = await page.query_selector("body > div.MuiModal-root.mui-style-1xkzkcs > div.MuiBox-root.mui-style-3uhxzk > div.MuiBox-root.mui-style-17kncur > div > div.MuiBox-root.mui-style-xvakb2 > label:nth-child(2) > div > div.MuiBox-root.mui-style-sct0cv > span > div")
                if freebtn:
                    await freebtn.click()

                freevist = await page.query_selector("body > div.MuiModal-root.mui-style-1xkzkcs > div.MuiBox-root.mui-style-3uhxzk > div.MuiBox-root.mui-style-n5f5kl > button")
                if freevist:
                    await freevist.click()

                print(Fore.GREEN + "Лот успешно выставлен." + Style.RESET_ALL)

            await asyncio.sleep(2)
            current_url = page.url
            print(Fore.CYAN + f"Ссылка на лот: {current_url}" + Style.RESET_ALL)
        
        except Exception as e:
            print(f"Ошибка в процессе: {e}")
            await page.screenshot(path="error.png")
            
    async def loading_cookies(self, cookies_file):
        if not hasattr(self, 'playwright'):
            self.playwright = await async_playwright().start()
        
        self.browser = await self.playwright.webkit.launch(headless=False)
        page = await self.browser.new_page()
        await stealth_async(page)
            
        cookies = await self.load_cookies(cookies_file)
        await page.context.add_cookies(cookies)
        
        return page
            
        
    async def close(self):
        if hasattr(self, 'browser'):
            await self.browser.close()
        if hasattr(self, 'playwright'):
            await self.playwright.stop()                       
