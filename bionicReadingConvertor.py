
import requests

url = "https://bionic-reading1.p.rapidapi.com/convert"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\nLorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"response_type\"\r\n\r\nhtml\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"request_type\"\r\n\r\nhtml\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fixation\"\r\n\r\n1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"saccade\"\r\n\r\n10\r\n-----011000010111000001101001--\r\n\r\n"
headers = {
	"x-rapidapi-key": "1a5a7bc8cemshd00b7071346980cp1d4334jsn2b7195570453",
	"x-rapidapi-host": "bionic-reading1.p.rapidapi.com",
	"Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
}

response = requests.post(url, data=payload, headers=headers)

print(response.status_code)

print(response.content)