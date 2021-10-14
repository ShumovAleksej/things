import json
import os
import re
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.0.1044 Yowser/2.5 Safari/537.36"
}


def get_url(url):
    # req = requests.get(url, headers)
    # src = req.text
    # # with open("index.html", "w", encoding="utf-8") as f:
    # #     f.write(src)
    # with open("index.html", encoding="utf-8") as f:
    #     src = f.read()
    # soup = BeautifulSoup(src, "lxml")
    # list_scp = soup.find("div", class_="side-block").find_all("div", class_="menu-item")
    # all_objs_dict = dict()
    # for item in list_scp:
    #     obj = item.find("a", text=re.compile("Объект"))
    #     if obj == None:
    #         continue
    #     all_objs_dict[obj.text] = "http://scpfoundation.net/" + obj.get("href")
    # with open("data/all_objects_cat_dict.json", "w", encoding="utf-8") as file:
    #     json.dump(all_objs_dict, file, indent=4, ensure_ascii=False)

    with open("data/all_objects_cat_dict.json", encoding="utf-8") as file:
        all_objs = json.load(file)
    count = 0
    for category_name, category_href in all_objs.items():
        if count == 0:
            folder_name = f"data/data_{category_name.split()[1]}"
            # if os.path.exists(folder_name):
            #     print("Папка уже существует!")
            # else:
            #     os.mkdir(folder_name)
            if " " in category_name:
                category_name = category_name.replace(" ", "_")
            # req = requests.get(url=category_href, headers=headers)
            # src = req.text
            # with open(f"{folder_name}/{category_name}.html", "w", encoding="utf-8") as file:
            #     file.write(req.text)
            # with open(f"{folder_name}/{category_name}.html", encoding="utf-8") as file:
            #     src = file.read()
            #
            # soup = BeautifulSoup(src, "lxml")
            # all_scp_dict = dict()
            # all_scp_list = soup.find("div", id="page-content").find_all("a", text=re.compile("SCP"))
            # for scp in all_scp_list:
            #     all_scp_dict[scp.text] = "http://scpfoundation.net/" + scp.get("href")
            # with open(f"{folder_name}/{category_name}.json", "w", encoding="utf-8") as file:
            #     json.dump(all_scp_dict, file, indent=4, ensure_ascii=False)
            iteration_count = 1
            with open(f"{folder_name}/{category_name}.json", encoding="utf-8") as file:
                all_scp = json.load(file)
            scp_data_list = []
            for scp_num, scp_href in all_scp.items():
                if iteration_count > 50:
                    break
                req = requests.get(url=scp_href, headers=headers)
                src = req.text
                with open(f"{folder_name}/{scp_num}.html", "w", encoding="utf-8") as file:
                    file.write(req.text)
                with open(f"{folder_name}/{scp_num}.html", encoding="utf-8") as file:
                    src = file.read()

                soup = BeautifulSoup(src, "lxml")
                scp_data = soup.find("div", id="main-content")
                try:
                    scp_name = scp_data.find("div", id="page-title").text
                except Exception:
                    scp_name = "No SCP name"
                try:
                    scp_img = scp_data.find("div", class_="rimg").find("img").get("src")
                except Exception:
                    scp_img = "No SCP image"
                try:
                    scp_class = scp_data.find("div", id="page-content").find("p").find_next_sibling().find("a").text
                except Exception:
                    scp_class = "No SCP class"

                scp_data_list.append(
                    {
                        "Num": scp_num,
                        "Name": scp_name.strip(),
                        "Class": scp_class,
                        "Image": scp_img
                    }
                )
                print(f"Итерация {iteration_count} завершена")
                iteration_count +=1
            with open(f"{folder_name}/scp_data.json", "w", encoding="utf-8") as file:
                json.dump(scp_data_list, file, indent=4, ensure_ascii=False)
            count += 1


def main():
    get_url("http://scpfoundation.net/")


if __name__ == "__main__":
    main()
