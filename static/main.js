
let data = {
  "id": "8",
  "title": "Post Eight",
  "body": "Is this getting boring?"
}

function addNewPost(){
  fetch('http://localhost:5000/posts', {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
    cache: "no-cache",
    mode: "cors", 
  })
  .then(res => res.json())
  .then(() => console.log('done'))
  .catch(err => console.log(err))
}

function deletePost(){
  console.log('delete');
  
}

function updatePost(){
  console.log('update');
  
}

