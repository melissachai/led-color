import requests
import time
import colorsys
import random
url = 'http://192.168.1.230:3000'

colour = [(255, 0, 0), (255, 192, 0), (255, 252, 0)] 

while True:
    for u in colour:
        red, green, blue = u
        requests.post(url + '/rgb', json={'red': red, 'green': green, 'blue': blue})
        time.sleep(.01)
    