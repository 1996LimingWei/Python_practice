import csv
from bs4 import BeautifulSoup
import requests
import re
import time

def get_requests(url): # request the url and apply html parse using bs4
    responses = requests.get(url, headers=headers).content
    soup = BeautifulSoup(responses, "html.parser")
    return soup

def get_def (soup):
    content =[] #store text in subpage
    for a in soup.find_all('div', attrs={'class': 'content'}):
        #print(a)
        keyword = a.find('nav', attrs={'id': 'center-doc-outline'})
        keywords = keyword.find_next_siblings('p')
        #print(Keyword)
        for i in keywords:
            key = i.get_text()#.replace("\n",",").split(",")
            content.append(key)
        words = list(filter(None, content))
    #print(words)
    return words
    
def get_result(soup):
    k = 0
    keywords = []
    href = []
    defin = [[]]
    for a in soup.find_all('section', attrs={'class': 'row'}):
        #print(a)
        Keyword = a.find_all('div', attrs={'class': 'column'})
        #print(Keyword)
        for i in Keyword:
            key = i.get_text().replace("\n",",")[1:].split(",")
            keywords.extend(key)
    keywords = list(filter(None, keywords))
    #print(keywords)
    for x in soup.find_all('a', attrs={'data-linktype': 'relative-path'}):
        href.append(x['href'])
        #print(x['href'])
        add_keyword = get_requests("https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/"+x['href'])
        add_refer = get_requests("https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/"+x['href'][3:])
        add_sharp = get_requests("https://docs.microsoft.com/en-us/dotnet/csharp/"+x['href'][6:])
        if len(x['href'])>5:
            if (x['href'][2] == "/") & (x['href'][5] != "/"):
                href = add_refer
                defin.append(get_def(href))
            elif x['href'][5] == "/":
                href = add_sharp
                defin.append(get_def(href))
            else:
                href = add_keyword
                defin.append(get_def(href))
        elif len(x['href'])>2 & len(x['href'])<=5:
            if x['href'][2] == "/":
                href = add_refer
                defin.append(get_def(href))
            else:
                href = add_keyword
                defin.append(get_def(href))
        else:
            href = add_keyword
            defin.append(get_def(href))
        #print(defin)
        print("k is",k)
        k += 1
        
    for y in range(len(keywords)):
        csv_writer.writerow([keywords[y],href[y],defin[y+1]])
        print("successfully wrote row")
if __name__ == '__main__':
    #create csv
    f = open('Keywords.csv', 'w', encoding='utf-8', newline='')
    #write csv
    csv_writer = csv.writer(f)
    #write headers
    csv_writer.writerow(["Keywords","href","definition"])

    headers = {
        'cookie': 'OT-SessionId=45272116-52de-48c9-8fdd-cf98fe223dbc; spredCKE=redcount=0; lsCKE=cbref=1; lvCKE=lvmreg=%2C0&histmreg=%2C0; otuvid=64E5EE37-2DC5-428A-A8F4-1841D6DEF392; ak_bmsc=6E8990D1BC16825EADD709219F0897074056CEE4E90300005A5B1B60FC62134A~pl11X3yNRzn0DTklsf27PM1SJ9W+BbWALJlzzx4fpHJkofS8E+kx0t155Qb9ZkEZCCL+eLoyl99HO5H4lvjXA96hVUM7u/GG+a0/LYph6LXydN5Lg8ONm8WEmz+HFtjy7qlt/JzuieyHoC8nMCIPZCzL9B35+n3gIdq0MBzIQDw312tK6i7oHiik/DOtnhJAJQptP3icxb4zkAfHJGP72aDorLaja/PhCHZTvDEv+ZLwc=; OptanonConsent=isIABGlobal=false&datestamp=Thu+Feb+04+2021+10%3A30%3A36+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.5.0&hosts=&consentId=1c065c11-e6a5-4e20-9b44-40ac8b5817fb&interactionCount=1&landingPath=https%3A%2F%2Fwww.opentable.com%2Fr%2Fleticias-cocina-and-cantina-santa-fe-hotel-las-vegas%3Fcorrid%3D78e4b95a-826a-4267-8e63-ec40359b90df&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; OT-Session-Update-Date=1612407626; ftc=x=2021-02-04T04%3A00%3A26&c=1&pt1=1&pt2=1&er=1040929&p1ca=r%2Fleticias-cocina-and-cantina-santa-fe-hotel-las-vegas&p1q=corrid%3D78e4b95a-826a-4267-8e63-ec40359b90df; bm_mi=55D667B5F6710BAF8AB2E4C40D8E58A4~pGBSoaz9qIG7MaNm2OlgiDRFQUJPZhtrJYvvesurfX/Im84D/RY801t06A45qWj6UG04fMCo6t7eaCNOq3FjsgylJFt9R63D2/ihKFbWXL7ILu+hmCNL1/JA61nlFPugBt499IuliqzBhGSMnwp6tJqqlP4faz5IbQQZBkk17MCAGXPWyJ7h63/t9cWHzdmCQgncxYY/XoYTPH1G+uLRjv6Klz0Hr2lSb8aKGwNoglYgjR+ICC2rkkbGZ5rnbILMmDCma78vR1VcktPMppA18g==; bm_sv=BBB024E3D2EE22A07E18B6961F38552F~hpLNgQNHlPfPzGn6uiirPmyTTdl8XdVYFXonQnJtKCmBatuln6M9qI1rgQJP/pqy4iq2rhgwdZxzUuPAm4I33t1so0cpPEB/vOCmvnzMrDU6aH6Gy/aK7mUDWeWaPfyWTNr+9d6GXeQSh/SgfH39157Vm8aHT4+N1ve2FAawffk=',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    #url
    res_url = f'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/'
    start_time = time.time()
    soup = get_requests(res_url)  
    get_result(soup) 
    print("My program took", time.time() - start_time, "to run")
    f.close()
