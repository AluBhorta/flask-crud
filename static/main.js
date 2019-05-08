const inputTitle = document.getElementById("input-title");
const inputBody = document.getElementById("input-body");

function addNewPost() {
  title = inputTitle.value;
  body = inputBody.value;

  fetch("http://localhost:5000/posts", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ title, body })
    // cache: "no-cache",
    // mode: "cors"
  })
    .then(res => {
      inputTitle.value = "";
      inputBody.value = "";
      res.json();
    })
    .catch(err => console.log(err));
}

function deletePost() {
  const sPath = document.location.pathname.split("/");
  const id = sPath[sPath.length - 1];

  fetch(`http://localhost:5000/post/${id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json"
    }
  })
    .then(res => {
      window.location.replace("http://localhost:5000/posts");
      // window.location.href = "http://stackoverflow.com";
      console.log(res);
    })
    .catch(err => console.log(err));
}

function updatePost() {
  console.log("update");
}
