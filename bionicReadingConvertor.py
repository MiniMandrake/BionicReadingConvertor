import os
import requests
from dotenv import load_dotenv
load_dotenv()

# Bionic Reader API accessed through Rapid API
# default params
url = "https://bionic-reading1.p.rapidapi.com/convert"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\nLorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"response_type\"\r\n\r\nhtml\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"request_type\"\r\n\r\nhtml\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fixation\"\r\n\r\n1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"saccade\"\r\n\r\n10\r\n-----011000010111000001101001--\r\n\r\n"
headers = {
	"x-rapidapi-key": os.getenv("BionicReadingToken"),
	"x-rapidapi-host": "bionic-reading1.p.rapidapi.com",
	"Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
}

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
f = open("testPage.html", "r")
print(f.read())