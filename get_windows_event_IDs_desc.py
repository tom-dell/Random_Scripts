import bs4
import requests

EID = input('Enter the EventID ')


def WindowsEventCode(URL):
    res = requests.get(URL)

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # select the CSS selector section of the object I want to display
    elems = soup.select('#contentMargin > p.hey')
    print(elems[0].text.strip())


WindowsEventCode(
    "http://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=%s" % (EID,))
