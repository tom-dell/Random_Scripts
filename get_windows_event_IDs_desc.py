import bs4, requests

EID = input('Enter the EventID ')

def WindowsEventCode(URL):   
    res = requests.get(URL)

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    elems = soup.select('#contentMargin > p.hey')
    print(elems[0].text.strip())

WindowsEventCode("http://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=%s" %(EID,))
