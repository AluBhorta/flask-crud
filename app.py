from flask import Flask, render_template, request, jsonify
from db.sampledata import posts as Posts

# init app
app = Flask(__name__)
app.debug = True


# routes
@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/posts" , methods=["GET", "POST"])
def posts():
    if request.method == "POST":
        post_id = request.json['id']
        title = request.json['title']
        body = request.json['body']
        Posts.append({
            "id": post_id,
            "title": title,
            "body": body
        })
    return render_template('posts.html', posts=Posts)


@app.route("/post/<post_id>")
def post(post_id):
    for post in Posts:
        if int(post['id']) == int(post_id):
            return render_template('post.html', post=post)
    return render_template("error404.html", message="Invalid Post ID")



# run app
if __name__ == "__main__":
    app.run()
