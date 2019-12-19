import urllib.request
import urllib.parse

api = "https://search.naver.com/search.naver"
values = {
    "where": "nexearch",
    "sm": "top_hty",
    "fbm": "",
    "ie": "utf8",
    "query": "초콜릿"
}
params = urllib.parse.urlencode(values)
url = api + "?" + params

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8") # euc-kr 또는 utf-8로 테스트해볼 것
print(text) 