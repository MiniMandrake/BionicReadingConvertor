async function getPayload(payload) {
  const url = "https://bionic-reading1.p.rapidapi.com/convert";
  const data = new FormData();

  data.append("content", payload);
  data.append("response_type", "html");
  data.append("request_type", "html");
  data.append("fixation", "1");
  data.append("saccade", "10");

  const options = {
    method: "POST",
    headers: {
      "x-rapidapi-key": "1a5a7bc8cemshd00b7071346980cp1d4334jsn2b7195570453",
      "x-rapidapi-host": "bionic-reading1.p.rapidapi.com",
    },
    body: data,
  };

  try {
    const response = await fetch(url, options);
    const result = await response.text();
    console.log(result);
    document.getElementById("output").innerHTML = result;
  } catch (error) {
    console.error(error);
  }
}

function readFile() {
  const fileInput = document.getElementById("input");
  const out = document.getElementById("output");

  fileInput.addEventListener("change", (event) => {
    const files = event.target.files;

    if (files.length > 0) {
      const file = files[0];

      // Do something with the file, e.g., read its contents:
      const reader = new FileReader();

      reader.onload = (e) => {
        const fileContent = e.target.result;
        console.log(fileContent);
        getPayload(fileContent);
      };
      console.log("bruh");
      reader.readAsText(file);
    }
  });
}

readFile();

// getPayload("gello");
// getPayload(text);
