import lxml, requests, json
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.0.1044 Yowser/2.5 Safari/537.36"
}

festivals_urls_list = []

for i in range(0, 96, 24):
    url = f"https://www.skiddle.com/festivals/search/?ajaxing=1&sort=2&fest_name=&from_date=17%20Oct%202021&to_date=&maxprice=500&o={i}&bannertitle="
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    html_response = json_data["html"]
    with open(f"data/index_{i}.html", "w", encoding="utf-8") as file:
        file.write(html_response)
    with open(f"data/index_{i}.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    x = soup.find_all("a", class_="card-details-link")
    for item in x:
        fest_url = "https://www.skiddle.com" + item.get("href")
        festivals_urls_list.append(fest_url)

festivals_list_result = []
count = 0
for festival_url in festivals_urls_list:
    count += 1
    print('Iteration #', count)
    req = requests.get(url=festival_url, headers=headers)
    try:
        soup = BeautifulSoup(req.text, "lxml")
        festival_info_div = soup.find("div", class_="top-info-cont")
        festival_name = festival_info_div.find("h1").text.strip()
        festival_date = festival_info_div.find("h3").text.strip()
        festival_location_url = "https://www.skiddle.com" + festival_info_div.find("a", class_="tc-white").get("href")

        req = requests.get(url=festival_location_url, headers=headers)
        soup = BeautifulSoup(req.text, "lxml")
        contact_details = soup.find("h2", string="Venue contact details and info").find_next()
        items = [item.text for item in contact_details.find_all("p")]
        contact_details_dict = {}
        for contact_detail in items:
            contact_detail_list = contact_detail.split(":")
            if len(contact_detail_list) == 3:
                contact_details_dict[contact_detail_list[0].strip()] = contact_detail_list[1].strip() + ":" \
                                                                       + contact_detail_list[2].strip()
            else:
                contact_details_dict[contact_detail_list[0].strip()] = contact_detail_list[1].strip()
        festivals_list_result.append(
            {
                "Festival name": festival_name,
                "Festival date": festival_date,
                "Contacts data": contact_details_dict
            }
        )
    except Exception:
        print(Exception)

with open("festival_list_result.json", "a", encoding="utf-8") as file:
    json.dump(festivals_list_result, file, indent=4, ensure_ascii=False)
