import urllib2, time
from bs4 import BeautifulSoup




def scrape_profile(name):

    html = urllib2.urlopen('https://twitter.com/' + name).read()
    soup = BeautifulSoup(html, "html.parser")

    for tweet in soup.findAll(class_="ProfileTweet"):
        time.sleep(0.3)
        try:
            print tweet.get_text()#.replace("\n","")
        except:
            print "something went wrong reading the html"
            #break

def remove_nonascii(text):
    ret = ""
    for letter in text:
        print letter
        #if ord(letter) <= 126:
            #ret += letter


def main():
    people = []
    for line in open("people.txt").readlines():
        if not line.startswith("#"): people.append(line)

    for p in people:
        print p
        time.sleep(1)
        scrape_profile(p)





if __name__ == '__main__':
    main()