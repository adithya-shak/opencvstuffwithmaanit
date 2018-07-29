from html.parser import HTMLParser
import requests
import cv2

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get("https://google.com", headers=headers)
class htmlbozz (HTMLParser):
    isImage = False
    def handle_starttag(self, tag, attr):
        if (tag == "img"):
            print("Isimage")
            self.isImage = True
        else:
            self.isImage = False
    def handle_data(self, data):
        if (self.isImage):
            print(data)


parser = htmlbozz()
parser.feed(str( response.content))

parser.handle_starttag("div", [("id", "hplogo")])

print ("Kevin ya boi")