import requests
import os
from PIL import Image
#from IPython.display import IFrame

url = "http://adis.springer.com/"
result =requests.get(url)
print(f"status code for get request: {result.status_code}")
print(f"request headers  for get request: {result.request.headers}")
print(f"Encoding   for get request: {result.encoding}")
#print(f"Content-Type of request headers  for get request: {result.request.headers['content-type']}")
print(f"User-Agent of request headers  for get request: {result.request.headers['User-Agent']}")
print(f"response headers  for get request: {result.headers}")
print(f"Request body for get request: {result.request.body}")
print(f"first 100 chars of response for get request: {result.text[0:100]}")

path=os.path.join(os.getcwd(),'image.png')
path

with open(path,'wb') as f:
    f.write(result.content)
#Image.open(path)


#Get Request with URL Parameters
profilesLink ="https://adisinsight.springer.com/drugs/800027914"
payload = { "bpIds": "3000093925%2C3001592458", "checksum": "0797b62b299e320ff6a4540863dde990b9bb80f1-1605093671452-c17183323f9f28903db80698e601e448979854bdf911905893237a83e0d9ad4a05397e65a874c51567277828def432d0"}

result2 = requests.get(profilesLink, payload)
print(f"url of Request with URL Parameters: {result2.url}")
print("request body:", result2.request.body)
#print("json request body:", result2.json())

#Post Requests
url_post='http://httpbin.org/post'
payload2={"name":"Swati","ID":"123"}
r_post=requests.post(url_post,data=payload2)
print("POST request URL:",r_post.url )
print("POST request body:",r_post.request.body)