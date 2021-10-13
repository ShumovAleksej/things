import re
from bs4 import BeautifulSoup

with open("index.html", encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

# title = soup.title
# print(title.text)

# page_h1 = soup.find('h1')
# print(page_h1)
# page_h1_all = soup.find_all('h1')
# print(page_h1_all)

# user_name = soup.find("div", class_="user__name")
# print(user_name.text.strip())

# user_name = soup.find("div", class_="user__name").find("span")
# print(user_name)

# user_name = soup.find("div", {'class': 'user__name', 'id': 'idone'}).find("span")
# print(user_name)

# spans = soup.find_all("div", {"class": "user__info"})
# for sp in spans:
#     print(sp.text.strip())
# -->
# spans = soup.find(class_='user__info').find_all("span")
# print(spans)
# for sp in spans:
#     print(sp.text)

# social_urls = soup.find(class_="social__networks").find("ul").find_all("a")
# for sp in social_urls:
#     print(sp)

# all_a = soup.find_all('a')
# print(all_a)
# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     item_url = item["href"]
#     print(f"{item_text}:{item_url}")

# post_div = soup.find(class_="post__text").find_parent("div", "user__post")
# print(post_div)

# next_el = soup.find(class_="post__title").find_next().text
# print(next_el)

# next_sib = soup.find(class_="post__title").find_next_sibling()
# print(next_sib)

# prev_sib = soup.find(class_="post__date").find_previous_sibling()
# print(prev_sib)

# find_all_clothes = soup.find_all(text=re.compile("нейросеть"))
# print(find_all_clothes)