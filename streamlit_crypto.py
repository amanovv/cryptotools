from bs4 import BeautifulSoup
import requests
from summarizer import Summarizer
import streamlit as st


def main():
    st.set_page_config(layout="wide")
    st.title("Latest news summarizer based on given keywords")
    st.subheader("Just provide the keyword below and see the magic lol")
    keyword_input = st.text_input("Type the keyword here")
    if keyword_input.lower() == "dovran amanov":
        st.error("Don't do this, this is creepy")
    else:
        if keyword_input:
            s = KeywordScraper(keyword_input)
            output = s.scrape_start()
            st.write(output)

def add_keywords(keywords):
    keywords = keywords.split()
    keyword_concat= ""
    for i in keywords:
        keyword_concat += i + "+"
    keyword_concat = keyword_concat[:-1]
    return keyword_concat

class KeywordScraper:
    def __init__(self, keyword):
        self.keyword = keyword
        all_keywords = add_keywords(keyword)
        self.links_scraped = []
        self.search_string = "https://news.google.com/search/?q=" + all_keywords

    def scrape_start(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
        content = requests.get(self.search_string, headers=headers).text
        soup = BeautifulSoup(content, "html.parser")
        related_news_section = soup.find("div", {"class": "lBwEZb BL5WZb xP6mwf"})
        news_cols = related_news_section.find_all("div", {"class": "xrnccd"})

        for col in news_cols:
            list_of_keywords = col.find_all("a", {"class": "VDXfz"})
            #print(list_of_keywords)
            for i in list_of_keywords:
                self.links_scraped.append(i['href'])
        model = Summarizer()
        output = {}
        n = 0
        for link in self.links_scraped:
            search_link = link.split("./")
            full_link = "https://news.google.com/" + search_link[1]

            content = requests.get(full_link, headers=headers).text
            soup = BeautifulSoup(content, 'html.parser')

            news_body = soup.find("body")
            link_div = news_body.find("div", {"class": "m2L3rb eLNT1d"})
            link_final = link_div.find("a")['href']
            source_init = link_final.split("https://www.")
            if len(source_init) == 1:
                source = link_final.split("https://")[1].split(".")[0]
            else:
                source = source_init[1].split(".")[0]

            content = requests.get(link_final, headers=headers).text
            soup = BeautifulSoup(content, 'html.parser')
            news_body = soup.find("body")
            parapraphs = news_body.find_all('p')
            if news_body.find('h1'):
                header = news_body.find('h1').getText().strip()
            else:
                header = 'Could not retreive headline'

            text_news = ""
            i = 0

            for p in parapraphs:
                if i<1 or len(parapraphs) - i < 12:
                    i += 1
                    continue
                if p:
                    text_news = p.getText().strip() + text_news
                i += 1
            result = model(text_news, num_sentences=3)
            full = ''.join(result)
            final_key = source + ": " + header
            output[final_key] = full
            n += 1
            if n>10:
                break
        return output

if __name__ == "__main__":
    main()
