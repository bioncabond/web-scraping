from web_scraping.scraping import *



def test_get_citation_count(): 
    URL = 'https://en.wikipedia.org/wiki/Mansa_Musa' 
    assert get_citations_needed_count(URL) == 3 

def test_get_citation_needed_report(): 
        text = get_citations_needed_report('https://en.wikipedia.org/wiki/Mansa_Musa') 
        expected =  'Musa Keita I (c. 1280[citation needed] – c. 1337), or Mansa Musa, was the ninth[2] Mansa of the Mali Empire, one of the most powerful West African states. He has sometimes been called the wealthiest person in history, though his wealth is impossible to accurately quantify and it is difficult to meaningfully compare the wealth of historical figures.' in text
        assert expected == True

 