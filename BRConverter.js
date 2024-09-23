require("dotenv").config();
dotenv.config();

const url = "https://bionic-reading1.p.rapidapi.com/convert";
const data = new FormData();

data.append(
  "content",
  "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
);
data.append("response_type", "html");
data.append("request_type", "html");
data.append("fixation", "1");
data.append("saccade", "10");

const options = {
  method: "POST",
  headers: {
    "x-rapidapi-key": BionicReadingToken,
    "x-rapidapi-host": "bionic-reading1.p.rapidapi.com",
  },
  body: data,
};

try {
  const response = await fetch(url, options);
  const result = await response.text();
  console.log(result);
} catch (error) {
  console.error(error);
}
return result;
