import requests,re
from bs4 import BeautifulSoup


headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'}

search = input("Enter name: ")
url = "http://spankbang.com/s/" + search + "/?length=short"
r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.content,"html.parser")
urls = []
for elements in soup.find_all('a',{'class':'thumb'}):
    href = "https://spankbang.com" + (elements.get('href'))
    urls.append(href)

for url in urls:
    r = requests.get(url, headers=headers)
    html = str(r.content)
    soup = BeautifulSoup(r.content, "html.parser")
    title = soup.select('#video > h1')[0].text
    continue_func = input("Do you want to download this video: " + str(title) + " (1/0) : ")
    if continue_func == "1":
        pass
    else:
        continue
    for element in soup.find_all('script', {'type':'text/javascript'}):
        if "stream_key" in element.text:
            data = (element.text)
            stream_key = re.findall("var stream_key  = '(.*?)';",data)[0]
            stream_id = re.findall("var stream_id  = '(.*?)';",data)[0]
    height = "720p"
    url = "http://spankbang.com/_" + stream_id + "/" + stream_key + "/title/" + height + "__mp4"
    print("Getting video... " + url)
    r = requests.get(url,headers=headers)
    if "404 Not Found" in str(r.content):
        print("Error... file not found. Retrying")
        height = str("hi")
        url = "http://spankbang.com/_" + stream_id + "/" + stream_key + "/title/" + height + "__mp4"
        print("Getting video... " + url)
        r = requests.get(url, headers=headers)
    with open(title+".mp4" , 'wb') as f:
        f.write(r.content)
