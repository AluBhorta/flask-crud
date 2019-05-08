from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
# sample data

# init app
app = Flask(__name__)
app.debug = True
base_dir = os.path.abspath(os.path.dirname(__file__))

# db config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(base_dir, 'db/db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# db.drop_all()
# db.create_all()


# Post Class/Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.String(500))

    def __init__(self, title, body):
        self.title = title
        self.body = body


# Post Schema
class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body')


# Init schema
post_schema = PostSchema(strict=True)
posts_schema = PostSchema(many=True, strict=True)

# routes
@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/posts", methods=["GET", "POST"])
def posts():
    if request.method == "POST":
        title = request.json['title']
        body = request.json['body']

        new_post = Post(title, body)

        db.session.add(new_post)
        db.session.commit()
        app.logger.info(new_post.id)

    all_posts = Post.query.all()
    result = posts_schema.dump(all_posts)
    # print('result.data: ', result.data)

    return render_template('posts.html', posts=result.data)


@app.route("/post/<post_id>", methods=["GET", "PUT", "DELETE"])
def post(post_id):
    if request.method == "GET":
        post = Post.query.get(post_id)
        if post:
            ser_post = post_schema.dump(post)
            return render_template('post.html', post=ser_post.data)
        return render_template("error404.html", message="Invalid Post ID")
    elif request.method == "DELETE":
        post = Post.query.get(post_id)
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('posts'))
    elif request.method == "PUT":
        pass
        # ###
        #
        # implement put


# run app
if __name__ == "__main__":
    app.run()
