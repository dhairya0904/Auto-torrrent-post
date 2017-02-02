import re
import requests
from bs4 import BeautifulSoup
# from lxml import html                    # no hidden inputs in form


def post_link(magnet):

    s = requests.session()             #creates a session

    login = s.get('https://www.zbigz.com')

    form = {}
    form['e-mail'] = #your mail
    form['password'] = #your password

    response = s.post('https://www.zbigz.com/login.php',data = form)    #login
    info = {'url':magnet}
    a = s.post('https://www.zbigz.com/myfiles',data = info)              #post the magnet link
    print "successful"


def get_link(search):
    count = int(0)
    links = []

    search.replace(' ','%20')
    site = "https://thepiratebay.org/search/" + search + '/0/99/0'
    url = requests.get(site)

    soup = BeautifulSoup(url.text,'html.parser')
    seeds = soup('td')
    tags = soup('a')

    peers = []                   # for getting seeders and leechers of the magnet link

    for seed in seeds:
        no = seed.getText()
        if re.search('^[0-9]',no):
            peers.append(no)

    for tag in tags:
        if(re.search('^/torrent',tag['href'])):
            links.append('https://thepiratebay.org'+tag['href'])
            print count,tag.getText(),peers[count],peers[count+1],"\n"
            count += 1
        if(count == 10):
            break



    num = int(raw_input("\nselect the link: "))
    url = requests.get(links[num])

    soup = BeautifulSoup(url.text,'html.parser')
    tags = soup('a')

    for tag in tags:
        try:
            if(tag['href'].startswith('magnet')):                            #get the required magnet link
                magnet_link =  tag['href']
                break
        except:
            pass
    return magnet_link


def main():

    name = raw_input("enter the name of the movie or tv series: ")
    m_link = get_link(name)
    post_link(m_link)

if __name__ == '__main__':
    main()
