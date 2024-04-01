# print("Hello World")

import requests

url = "https://bionic-reading1.p.rapidapi.com/convert"

payload = {
	"content": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.",
	"response_type": "html",
	"request_type": "html",
	"fixation": "1",
	"saccade": "10"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "1a5a7bc8cemshd00b7071346980cp1d4334jsn2b7195570453",
	"X-RapidAPI-Host": "bionic-reading1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())

