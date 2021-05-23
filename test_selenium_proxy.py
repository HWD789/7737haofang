from selenium import webdriver
import os, sys, time, re, json
import logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s - %(filename)s] - %(levelname)s: %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
)

running_path = (os.path.dirname(os.path.realpath(sys.argv[0])))
os.chdir(running_path)
start = time.time()

chromeOptions = webdriver.ChromeOptions()

local_proxy = "http://127.0.0.1:1080"

ip_url = 'http://myip.ipip.net/'
artworks_url = 'https://www.pixiv.net/ajax/user/13534898/profile/all?lang=zh'
art_url = 'https://www.pixiv.net/artworks/89365024'
baidu_url = 'https://www.baidu.com'
pixiv_login_url = 'https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2Fartworks%2F89365024&lang=zh&source=pc&view_type=page'

chromeOptions.add_argument('--proxy-server={0}'.format(local_proxy))
chrome_driver = "I:\\File\\Code\\driver\\chromedriver.exe"
browser = webdriver.Chrome(
    executable_path=chrome_driver,
    # chrome_options=chromeOptions,
)

browser.set_page_load_timeout(10)

try:
    browser.get(pixiv_login_url)        # 首页为登录页面
    logging.info('finish load ....')

except Exception:
    js_stop = 'window.stop()'
    browser.execute_script( js_stop)
    logging.info ('停止页面加载')
    logging.info(browser.title)

# print(browser.page_source)
# print (browser.get_cookies)
# print (browser.get_cookies() )

# print ( dir (browser.get_cookies() ))
# print ( type (browser.get_cookies() ))
# for a in browser.get_cookies():
#     print ( f'{a["name"]} : {a["value"]}'  )
    # print (a['name'])

# time.sleep(3)
# browser.quit()
# end = time.time()
# print ('time',end-start)

# 2020292844@qq.com  hint
# WANGHAO1997


def Read_txt():
    with open ('./data/user_id.txt', 'r+', encoding='utf-8') as f:
        data = f.readlines()
    return data

def Click_login():
    js_name = 'document.querySelector("#LoginComponent > form > div.input-field-group > div:nth-child(1) > input[type=text]").value="2020292844@qq.com"'
    js_passwd = 'document.querySelector("#LoginComponent > form > div.input-field-group > div:nth-child(2) > input[type=password]").value="WANGHAO1997"'
    js_login = 'document.querySelector("#LoginComponent > form > button").click()'

    time.sleep(1)
    browser.execute_script(js_name)
    browser.execute_script(js_passwd)
    logging.info('文本填充')
    time.sleep(1)
    browser.execute_script(js_login)
    logging.info ('点击事件')
    time.sleep(5)
    Get_source()


def Get_source():
    url_list = Read_txt()
    for url in url_list:
        time.sleep(1)
        browser.get(url)
        logging.info(url)
        source = browser.page_source
        # url = 'https://www.pixiv.net/ajax/user/13534898/profile/all?lang=zh'
        userid_pattern = r'\d\d{0,12}'
        userid = re.findall(userid_pattern,url)
        logging.info (userid[0])
        time.sleep(1)
        with open('./pixiv/'+userid[0]+'.txt', 'w+', encoding='utf-8') as f:
            f.write(source)
    logging.info('即将关闭浏览器')
    time.sleep(3)
    browser.quit()

if __name__ == '__main__':
    Click_login()
    # Get_source()
    pass
    