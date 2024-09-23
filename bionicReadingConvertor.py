import os
import requests
from dotenv import load_dotenv
load_dotenv()

# Bionic Reader API accessed through Rapid API
# default params
url = "https://bionic-reading1.p.rapidapi.com/convert"

headers = {
	"x-rapidapi-key": os.getenv("BionicReadingToken"),
	"x-rapidapi-host": "bionic-reading1.p.rapidapi.com",
	"Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
}

text = "Hello! My name is Zhi!"

payload = f"-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\n{text}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"response_type\"\r\n\r\nhtml\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"request_type\"\r\n\r\nhtml\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fixation\"\r\n\r\n1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"saccade\"\r\n\r\n10\r\n-----011000010111000001101001--\r\n\r\n"

response = requests.post(url, data=payload, headers=headers)

# status codes:
# 200 = good, else = bad
print(response.status_code)

# convert from byte type to str to write into html
HTMLcode = str(response.content)

# removing unnecessary \n and b''
chars_to_remove = ["\\", "n"]

for char in chars_to_remove:
	HTMLcode = HTMLcode.replace(char, "")

HTMLcode = HTMLcode.lstrip("b'")
HTMLcode = HTMLcode.rstrip("'")

# write into HTML file
f = open("testPage.html", "w")
f.write(HTMLcode)
f.close()

#open and read the file after the appending:
# f = open("testPage.html", "r")
# print(f.read())