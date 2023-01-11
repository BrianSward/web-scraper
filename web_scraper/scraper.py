import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    a_links = soup.find_all('a', title="Wikipedia:Citation needed")
    return len(a_links)


def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    a_links = soup.find_all('a', title="Wikipedia:Citation needed")
    return_me = ""
    for i in a_links:
        return_me += i.parent.parent.parent.text + '\n'
    return return_me


if __name__ == '__main__':
    print(get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico"))
    print(get_citations_needed_report('https://en.wikipedia.org/wiki/Milford,_Connecticut'))