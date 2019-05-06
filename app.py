from flask import Flask, jsonify, render_template
import os

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
    return render_template('posts.html')


# run app
if __name__ == "__main__":
    app.run()
