from flask import Flask, jsonify, render_template
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


@app.route("/posts")
def posts():
    # ###
    #
    # query db and fetch posts
    return render_template('posts.html', posts=Posts)


@app.route("/post/<post_id>")
# ###
#
# query db and fetch post with id=id
def post(post_id):
    for post in Posts:
        if int(post['id']) == int(post_id):
            return render_template('post.html', post=post)
    return render_template("error404.html", message="Invalid Post ID")



# run app
if __name__ == "__main__":
    app.run()
