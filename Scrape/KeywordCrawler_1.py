import csv
from bs4 import BeautifulSoup
import requests
import re
import time

def get_requests(url): # request the url and apply html parse using bs4
    responses = requests.get(url, headers=headers).content
    soup = BeautifulSoup(responses, "html.parser")
    return soup

def get_sub (soup): # get the subpage keywords definition content function
    content =[] #store text in subpage
    for a_ in soup.find_all('div', attrs={'class': 'content'}): # locate the text by layers of element 
        keyword = a_.find('nav', attrs={'id': 'center-doc-outline'})
        keywords = keyword.find_next_siblings('p')
        for i_ in keywords:
            key = i_.get_text()#.replace("\n",",").split(",")
            content.append(key)
    words = list(filter(None, content))
    return words

def get_date(soup): # get the subpage date function
    date = []
    for _a in soup.find_all('ul', attrs={'class': 'metadata page-metadata'}):
        for d in _a.find_all('time', attrs={'aria-label': 'Article review date'}):
            time_ = d.get_text()[-17:]
            date.append(time_) 
    date = list(filter(None, date))
    return date
def get_li(soup): # get the subpage other content function
    li = []
    for _a_ in soup.find_all('div', attrs={'class': 'content'}):
        for d_ in _a_.find_all('ul'):
            for sub_li in d_.find_all('li'):
                sub_li_ = sub_li.get_text().strip()
                li.append(sub_li_) 
    li = list(filter(None, li))[2:]
    return li
def get_code(soup):
    try:
        code = soup.select('div pre code')
    except:
         code = ["no example codes"]
    #codes = list(filter(None, codes))[1:]
    return code
def get_result(soup): # get results, including keywords and href
    keywords = []
    hrefs = []
    defin=[]
    date = []
    li=[]
    codes= []
    for a in soup.find_all('section', attrs={'class': 'row'}):
        Keyword = a.find_all('div', attrs={'class': 'column'})
        for i in Keyword:
            key = i.get_text().replace("\n",",")[1:].split(",")
            keywords.extend(key)
    keywords = list(filter(None, keywords))

    for x in soup.find_all('a', attrs={'data-linktype': 'relative-path'}):
        url = x.get('href')
        ###different keywords adapt different subpage url. Specify three types of keywords.
        add_keyword = "https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/"+url
        add_refer = "https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/"+url[3:]
        add_sharp = "https://docs.microsoft.com/en-us/dotnet/csharp/"+url[6:]
        if url == "../": #ignore the link of "C#" at the bottom, which direct the page back to main page.
            continue
        if len(url)>6:
            if (url[1] == ".") & (url[4] != "."):
                href = add_refer
                hrefs.append(href)
                defin.append(get_sub(get_requests(href)))
                date.append(get_date(get_requests(href)))
                li.append(get_li(get_requests(href)))
                codes.append(get_code(get_requests(href)))
            elif (url[1] == ".") & (url[4] == "."):
                href = add_sharp
                hrefs.append(href)
                defin.append(get_sub(get_requests(href)))
                date.append(get_date(get_requests(href)))
                li.append(get_li(get_requests(href)))
                codes.append(get_code(get_requests(href)))
            elif (url[1] != "."):
                href = add_keyword
                hrefs.append(href)
                defin.append(get_sub(get_requests(href)))
                date.append(get_date(get_requests(href)))
                li.append(get_li(get_requests(href)))
                codes.append(get_code(get_requests(href)))
        elif len(url)>1 & len(url)<=6:
            if url[1] == ".":
                href = add_refer
                hrefs.append(href)
                defin.append(get_sub(get_requests(href)))
                date.append(get_date(get_requests(href)))
                li.append(get_li(get_requests(href)))
                codes.append(get_code(get_requests(href)))
            else:
                href = add_keyword
                hrefs.append(href)
                defin.append(get_sub(get_requests(href)))
                date.append(get_date(get_requests(href)))
                li.append(get_li(get_requests(href)))
                codes.append(get_code(get_requests(href)))
        else:    
            href = add_keyword
            hrefs.append(href)
            defin.append(get_sub(get_requests(href)))
            date.append(get_date(get_requests(href)))
            li.append(get_li(get_requests(href)))
            codes.append(get_code(get_requests(href)))
        
    print("The number of rows is",len(date))

    #create csv and write rows
    with open('Keywords1.csv', 'w',newline='') as csvfile:
        fieldnames = ['key', 'href','content','subcontent','date','codes'] #headers
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for num in range(len(keywords)):
            writer.writerow({'key': keywords[num], 'href': hrefs[num],'content':defin[num],'subcontent':li[num],'codes':codes[num],'date':date[num]})

if __name__ == '__main__':
    headers = {
        'cookie': 'OT-SessionId=45272116-52de-48c9-8fdd-cf98fe223dbc; spredCKE=redcount=0; lsCKE=cbref=1; lvCKE=lvmreg=%2C0&histmreg=%2C0; otuvid=64E5EE37-2DC5-428A-A8F4-1841D6DEF392; ak_bmsc=6E8990D1BC16825EADD709219F0897074056CEE4E90300005A5B1B60FC62134A~pl11X3yNRzn0DTklsf27PM1SJ9W+BbWALJlzzx4fpHJkofS8E+kx0t155Qb9ZkEZCCL+eLoyl99HO5H4lvjXA96hVUM7u/GG+a0/LYph6LXydN5Lg8ONm8WEmz+HFtjy7qlt/JzuieyHoC8nMCIPZCzL9B35+n3gIdq0MBzIQDw312tK6i7oHiik/DOtnhJAJQptP3icxb4zkAfHJGP72aDorLaja/PhCHZTvDEv+ZLwc=; OptanonConsent=isIABGlobal=false&datestamp=Thu+Feb+04+2021+10%3A30%3A36+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.5.0&hosts=&consentId=1c065c11-e6a5-4e20-9b44-40ac8b5817fb&interactionCount=1&landingPath=https%3A%2F%2Fwww.opentable.com%2Fr%2Fleticias-cocina-and-cantina-santa-fe-hotel-las-vegas%3Fcorrid%3D78e4b95a-826a-4267-8e63-ec40359b90df&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; OT-Session-Update-Date=1612407626; ftc=x=2021-02-04T04%3A00%3A26&c=1&pt1=1&pt2=1&er=1040929&p1ca=r%2Fleticias-cocina-and-cantina-santa-fe-hotel-las-vegas&p1q=corrid%3D78e4b95a-826a-4267-8e63-ec40359b90df; bm_mi=55D667B5F6710BAF8AB2E4C40D8E58A4~pGBSoaz9qIG7MaNm2OlgiDRFQUJPZhtrJYvvesurfX/Im84D/RY801t06A45qWj6UG04fMCo6t7eaCNOq3FjsgylJFt9R63D2/ihKFbWXL7ILu+hmCNL1/JA61nlFPugBt499IuliqzBhGSMnwp6tJqqlP4faz5IbQQZBkk17MCAGXPWyJ7h63/t9cWHzdmCQgncxYY/XoYTPH1G+uLRjv6Klz0Hr2lSb8aKGwNoglYgjR+ICC2rkkbGZ5rnbILMmDCma78vR1VcktPMppA18g==; bm_sv=BBB024E3D2EE22A07E18B6961F38552F~hpLNgQNHlPfPzGn6uiirPmyTTdl8XdVYFXonQnJtKCmBatuln6M9qI1rgQJP/pqy4iq2rhgwdZxzUuPAm4I33t1so0cpPEB/vOCmvnzMrDU6aH6Gy/aK7mUDWeWaPfyWTNr+9d6GXeQSh/SgfH39157Vm8aHT4+N1ve2FAawffk=',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    #url
    base_url = 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/'
    start_time = time.time()
    soup = get_requests(base_url)  
    get_result(soup) 
    print("My program took", time.time() - start_time, "to run get the run time")
    
    
  
    
