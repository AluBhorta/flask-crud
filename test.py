from app import db, Post, app, post_schema, posts_schema

with app.app_context():
    post = Post.query.all()

    print(post_schema.jsonify(post))
