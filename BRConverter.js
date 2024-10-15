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

  fileInput.addEventListener("change", (event) => {
    const files = event.target.files;

    if (files.length > 0) {
      const file = files[0];

      // Do something with the file, e.g., read its contents:
      const reader = new FileReader();

      reader.onload = (e) => {
        const fileContent = e.target.result;
        console.log(fileContent);
        // Send payload to server
        // convert input into bionic text
        getPayload(fileContent);
      };
      console.log("bruh");
      reader.readAsText(file);
    }
  });
}

readFile();

// HERE ON IS THE DRAG AND DROP FUNCTION

function dropHandler(ev) {
  console.log("File(s) dropped");

  // Prevent default behavior (Prevent file from being opened)
  ev.preventDefault();

  if (ev.dataTransfer.items) {
    // Use DataTransferItemList interface to access the file(s)
    [...ev.dataTransfer.items].forEach((item, i) => {
      // If dropped items aren't files, reject them
      if (item.kind === "file") {
        const file = item.getAsFile();
        // console.log(`… file[${i}].name = ${file.name}`);
      }
    });
  } else {
    // Use DataTransfer interface to access the file(s)
    [...ev.dataTransfer.files].forEach((file, i) => {
      // console.log(`… file[${i}].name = ${file.name}`);
    });
  }
}

function dragOverHandler(ev) {
  console.log("File(s) in drop zone");

  // Prevent default behavior (Prevent file from being opened)
  ev.preventDefault();
}

function dropFileHandler() {
  const dropzone = document.getElementById("dropzone");
  const output = document
    .getElementById("output")

    [
      // Prevent default behaviors for dragover and drop to enable file drop
      ("dragover", "drop")
    ].forEach((eventType) => {
      dropzone.addEventListener(eventType, (event) => {
        event.preventDefault();
      });
    });

  dropzone.addEventListener("drop", (event) => {
    event.preventDefault();

    // Access the dropped files
    const files = event.dataTransfer.files;

    // Iterate through the files and display their names
    if (files.length > 0) {
      let fileDetails = "Files dropped:\n";
      for (let i = 0; i < files.length; i++) {
        const file = files[i];
        fileDetails += `File Name: ${file.name}\nSize: ${file.size} bytes\nType: ${file.type}\n\n`;
      }
      getPayload(fileDetails);
    } else {
      output.textContent = "No files dropped.";
    }
  });
}
