# User pushover key: "uka4jemnzmmn3qdde82dvvmmgggbh5"
# Device name: "poddy"
# email: "ih62w7x8i8@pomail.net"
# API token: "a18k8gshofxz9gvu1sr4rteaxm8tum"




import sys
import os
import requests
import httplib, urllib
conn = httplib.HTTPSConnection("api.pushover.net:443")

#USER = os.environ["uka4jemnzmmn3qdde82dvvmmgggbh5"]
#API = os.environ["a18k8gshofxz9gvu1sr4rteaxm8tum"]

def send_message(text):
    """Send a message"""
    payload = {"message": text, "user": "uka4jemnzmmn3qdde82dvvmmgggbh5", "token": "a18k8gshofxz9gvu1sr4rteaxm8tum", "sound": "echo", }
    r = requests.post('https://api.pushover.net/1/messages.json', data=payload, headers={'User-Agent': 'Python'})
    return r
    
def main():
    """Main function."""
    r = send_message(" ".join(sys.argv[1:]))
    if not r.status_code == 200:
        print(r.text)
    
if __name__ == '__main__':
    main()