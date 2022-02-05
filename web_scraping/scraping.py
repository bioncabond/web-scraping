import requests
from bs4 import BeautifulSoup 

URL = 'https://en.wikipedia.org/wiki/Mansa_Musa'

def get_citations_needed_count(URL): 
    
    page =requests.get(URL) 
    # print(page.content)
   
    soup = BeautifulSoup(page.content, 'html.parser') 
    # print(soup) 

    results = soup.find(class_="mw-parser-output")
    # print(results.prettify) 

    a_tags = soup.find_all('a') 
    # print(a_tags)
    
    citations = [a for a in a_tags if 'citation needed' in a.text]
    print(citations) 

    citation_count = 0 
    for i in citations: 
        citation_count += 1 
    # print(f"this is citation count: {citation_count}")
    return citation_count 


def get_citations_needed_report(URL): 
    page =requests.get(URL) 
    soup = BeautifulSoup(page.content, 'html.parser') 
    results = soup.find(class_="mw-parser-output")

    #find all the paragraphs that have "citation needed" 
    search = results.find_all("p") 
    # print(search) 

    output_string = ''
    all_a_tags = soup.find_all('a')
    citations = [a for a in all_a_tags if 'citation needed' in a.text]
    for c in citations:
        output_string += (c.find_parent('p').text)
    return output_string

    
if __name__ == '__main__': 
    
    URL = 'https://en.wikipedia.org/wiki/Mansa_Musa' 
    print(get_citations_needed_count(URL)) 
    print(get_citations_needed_report(URL)) 


