#http module
import requests
r = requests.get("https://smartatentertainment.blogspot.com/")
#print(r.text)
with open("abc.html","w") as f:
    f.write(r.text)
    f.write("hii delete hua ki nai")
with open("abc.html","w") as f:
    f.write("hii delete hua ki nai")
