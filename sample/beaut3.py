import urllib.request
from bs4 import BeautifulSoup
import time

url = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
results = soup.select("#main_content .cluster_list .cluster_text a")
# print(results)
for result in results:
    # 기사를 가져옵니다.
    print("제목:", result.string)
    url_article = result.attrs["href"]
    # print(url_article)
    response = urllib.request.urlopen(url_article)
    soup_article = BeautifulSoup(response, "html.parser")
    content = soup_article.select_one("#articleBodyContents")
    # print(content.contents)
    output = ""
    for item in content.contents:
        stripped = str(item).strip()
        if stripped == "":
            continue
        if stripped[0] not in ["<", "/"]:
            output += str(item)
    print(output.replace("본문 내용  TV플레이어", ""))
    # 1초 휴식
    time.sleep(0.1)
