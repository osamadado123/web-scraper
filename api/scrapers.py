import requests
import json
from bs4 import BeautifulSoup
import re


url = 'https://en.wikipedia.org/wiki/2022_FIFA_World_Cup'



def get_citations_needed_count(url) -> int:
    """
    This functions recives url as string, and gets all the missing citations
    in a wikipedia page
    """

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    citation_needed = soup.find_all(title='Wikipedia:Citation needed')
    num =len(citation_needed)
    print(f'this article has {num} citations \n')
    
    return num


def get_citations_needed_report(url) -> str:

    """
    This functions Gets all the paragraphs that missing citations
    """

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    citations = soup.find_all(title='Wikipedia:Citation needed')
    for citation in citations:
        print(citation.parent.parent.parent.text)
        print()


get_citations_needed_count(url)
get_citations_needed_report(url)