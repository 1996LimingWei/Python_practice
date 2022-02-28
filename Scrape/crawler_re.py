import re  
import urllib.request
import csv
import time

def get_requests(url): # request the url and apply html parse using bs4
    content = urllib.request.urlopen(url).read().decode('utf=8)')
    return content
def get_keywords(content):
    pat1 = r'\">(.+?)\<\/a><br\/>'
    pat2 = r'(((?!>).)+?)<\/a><\/p>\n' #get the closest match
    key_1 = re.findall(pat1, content)
    key = re.findall(pat2, content)
    key_2 = [item[0] for item in key]
    keywords = key_1 and key_2 and key_1 + key_2
    return keywords
def get_sub (string): # get the subpage keywords definition content function
    pat_defin = r'\<p>(.+?)\<\/p>'
    word = re.findall(pat_defin,string)
    words =[re.sub(r'<.+?>', '', i) for i in word]
    return words

def get_date(content): # get the subpage date function
    pat_date = r'\"git">(.+?)\<\/time>'
    dates = re.findall(pat_date,content)
    #data = [item[0] for item in dates]
    return dates
def get_result(content,keywords):
    pat_url = r'(((?!").)+?)" data-linktype'
    href_ = re.findall(pat_url, content)
    href = [h[0] for h in href_ if '../' != h[0]] # exclude the C# main page
    #print(href)
    hrefs = []
    date = []
    defin = []
    for s in href:
        add_keyword = "https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/"+s
        add_refer = "https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/"+s[3:]
        add_sharp = "https://docs.microsoft.com/en-us/dotnet/csharp/"+s[6:]
        if len(s)>6:
            if (s[1] == ".") & (s[4] != "."):
                link = add_refer
                hrefs.append(link)
                date.append(get_date(get_requests(link)))
                defin.append(get_sub(get_requests(link)))
            elif (s[1] == ".") & (s[4] == "."):
                link = add_sharp
                hrefs.append(link)
                date.append(get_date(get_requests(link)))
                defin.append(get_sub(get_requests(link)))
            elif (s[1] != "."):
                link = add_keyword
                hrefs.append(link)
                date.append(get_date(get_requests(link)))
                defin.append(get_sub(get_requests(link)))
        elif len(s)>1 & len(s)<=6:
            if s[1] == ".":
                link = add_refer
                hrefs.append(link)
                date.append(get_date(get_requests(link)))
                defin.append(get_sub(get_requests(link)))
            else:
                link = add_keyword
                hrefs.append(link)
                date.append(get_date(get_requests(link)))
                defin.append(get_sub(get_requests(link)))
        else:    
            link = add_keyword
            hrefs.append(link)
            date.append(get_date(get_requests(link)))
            defin.append(get_sub(get_requests(link)))
    with open('Keywords_re.csv', 'w',newline='') as csvfile:
        fieldnames = ['key', 'href','date','definition'] #headers
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for num in range(len(keywords)):
            writer.writerow({'key': keywords[num], 'href': hrefs[num],'date':date[num],'definition':defin[num]})
if __name__ == '__main__':
    #url
    base_url = 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/'
    start_time = time.time()
    content = get_requests(base_url)  
    keywords = get_keywords(content)  
    get_result(content,keywords) 
    
    print("My program took", time.time() - start_time, "to run get the run time")