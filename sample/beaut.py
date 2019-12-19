from bs4 import BeautifulSoup
# 태그 선택자
"ul"
"div"
"li"
# 아이디 선택자
"#<아이디>"
# 클래스 선택자
".<클래스>"
# 여러개의 클래스
".<클래스>.<클래스>.<클래스>"
# 후손 선택자
"#meigen li"
# 자식 선택자
"ul.items > li"

html = """
    <html>
        <body>
            <div id="meigen">
                <h1>위키북스 도서</h1>
                <ul class="items art it book">
                    <li>a</li>
                    <li>b</li>
                    <li>c</li>
                </ul>
            </div>
        </body>
    </html>
"""

soup = BeautifulSoup(html, 'html.parser')
header = soup.select_one("div#meigen > h1") # 요소
list_items = soup.select("ul.items > li") # 요소의 배열

print(header.string)
print(soup.select_one("ul").attrs)

for li in list_items:
    print(li.string)