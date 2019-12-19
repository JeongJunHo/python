import requests

url = "http://google.com"
data = {
    "a": "10",
    "b": "20"
}
session = requests.session()
response = session.get(url, data=data)
response.raise_for_status()
print(response.text)

# session.post(url)
# session.put(url)
# session.delete(url)