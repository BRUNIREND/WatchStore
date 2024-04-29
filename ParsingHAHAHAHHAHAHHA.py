import json

from bs4 import BeautifulSoup
import requests

url = "https://sibtime.ru/catalog/naruchnye_chasy/?PAGEN_1="
url_add = 1

user_agent = "Mozilla/5.0 (Windows NT 10)"

result = []
 
def parse_page(url_add):
    req = requests.get(url + str(url_add), headers={'User-Agent': user_agent}).content

    soup = BeautifulSoup(req, "html.parser")

    a = soup.find("div", class_="catalog")

    a = a.find_all("div")

    for i in a:
        try:

            price = i.findNext("div", class_="card-product__prices-default").text
            name = i.findNext("a", class_="card-product__title")
            img = i.findNext("div", class_="card-product__imgs").findNext("a", class_="card-product__img-link").findNext("img").get("src")
            img_link = "https://sibtime.ru" + img
            # print(img)
            href = "https://sibtime.ru" + name.get("href")
            name = name.text

            result.append((name, price, href, img_link), )

            # print(name)
            # print(price)
            # print(href)
            # print("-"*20)
        except Exception as e:
            # print(e)
            break
# def parse_characterisitc_page(url):
#     req =
def write_json(data, file_name):
    with open(file_name, "w", encoding='utf-8') as f:

        json.dump(data, f, indent=4, ensure_ascii=False)

def second_pars(datas):
    for url in datas['url_path']:
        req = requests.get(url, headers={'User-Agent': user_agent}).content

        soup = BeautifulSoup(req, "html.parser")

        a = soup.find("div", class_="bg-white py-32 mt-md-32 mb-xl-80 mb-md-32 my-24")

        a = a.find('div', class_='container')
        a = a.find('div', class_='row row-cols-xl-4 row-cols-md-2')

        article = (a.find_all('div', class_='product-info-row'))
        for i in article:
            value = i.text.strip().split('\n')
            if value[0] in datas['characteristics'].keys():
                datas['characteristics'][value[0]].append(value[1])
            # print(value)

        # print(datas['characteristics'].values())
        # gender = (a.findNext('div', class_='product-info-row').text).strip().split('\n')
        # brend = (a.findNext('div', class_='product-info-row').text).strip().split('\n')
        # country = (a.findNext('div', class_='product-info-row').text).strip().split('\n')
        # waterproof = (a.findNext('div', class_='product-info-row').text).strip().split('\n')
        # collection = (a.findNext('div', class_='product-info-row').text).strip().split('\n')
        # style = (a.findNext('div', class_='product-info-row').text).strip().split('\n')
        # print(article, gender)
        # break
    return datas
def load_json():
    with open("data.json", 'r') as f:
        data = json.load(f)
        return data
if __name__ == "__main__":
    data = load_json()
    file_name = "full_data.json"
    datas = {
        "name": [],
        "cost": [],
        "url_path": [],
        "url_img": [],
        "characteristics": {
            "Артикул": [],
            "Пол": [],
            "Бренд": [],
            # "Страна": [],
            # "Водостойкость": [],
            # "Тип механизма": [],
            # "Модель механизма": [],
            # "Камней в механизме": [],
            # "Материал корпуса": [],
            # "Цвет корпуса": [],
            # "Форма корпуса": [],
            # 'Диаметр корпуса': [],
            # 'Толщина/глубина корпуса':[],
            # 'Материал ремня/браслета':[],
            # 'Цвет ремня/браслета':[],
            # 'Ширина ушек':[],
            # 'Цвет циферблата':[],
            # 'Индексы на циферблате':[],
            # 'EOL':[],
            # 'Отображение даты':[],
            # 'Стекло':[],
            # "Коллекция": [],
            # "Стиль": []
        }
    }
    for el in data:
        datas["name"].append(el[0].strip())
        datas["cost"].append(el[1].strip())
        datas["url_path"].append(el[2].strip())
        datas["url_img"].append(el[3].strip())

    write_json(second_pars(datas), file_name)

    # for i in range(3):
    #     print(url_add)
    #     parse_page(url_add)
    #     url_add += 1
    #
    # result = list(set(result))
    # print(len(result))
    # write_json(result)
# import requests
# from bs4 import BeautifulSoup
#
# st_accept = "text/html" # говорим веб-серверу,
#                         # что хотим получить html
# # имитируем подключение через браузер Mozilla на macOS
# st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
# # формируем хеш заголовков
# headers = {
#    "Accept": st_accept,
#    "User-Agent": st_useragent
# }
#
# req = requests.get("https://sibtime.ru/catalog/naruchnye_chasy/", headers)
# # инициализируем html-код страницы
# src = req.text
# soup = BeautifulSoup(src, 'html.parser')
# # считываем заголовок страницы
# title = soup.title.string
# some = soup.find("div", class_="catalog")
# print(title)