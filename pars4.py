import requests
from bs4 import BeautifulSoup as bs

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.3.954 (beta) Yowser/2.5 Safari/537.36'
}

url='https://akipress.org/'
# req=requests.get(url=url,headers=headers)

# print(src)
# with open('work.html', 'w',encoding='utf-8') as file:
    # file.write(req.text)
with open('html.html',encoding='utf-8') as file:
    src = file.read()
soup = bs(src, 'lxml')
articles = soup.find_all(class_='newslink')
# print(articles)
for i in articles:
    a=i.text
    b='https:'+i.get('href')
    a=a.split()[0:4]
    a="_".join(a)+'_итд'
    a=a.replace(' ','_').replace('-','_').replace('.','_').replace(',','_').replace(':','_')
    # print(a)
    req=requests.get(url=b,headers=headers)
    # with open(f'html/{a}.html', 'w',encoding='utf-8') as file:
    #     file.write(req.text)
    with open(f'html/{a}.html',encoding='utf-8') as file:
        source = file.read()
    sp=bs(source,'lxml')
    news_text=sp.find_all('p')
    tx=' '
    for z in news_text:
        tx+=f'{z.text}\n'
    with open(f'txt/{a}.txt', 'w',encoding='utf-8') as file:
        # for v in news_text:
        #     n_text=v.text
            # print(f'{n_text}')
            file.write(f'{tx}')





    # rep=[',','.',' ',"'",'-']
    # for item in rep:
    #     if item in a:
    #         a=a.replace(item,'_')
    #         print(a)

