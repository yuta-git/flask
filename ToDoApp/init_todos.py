from app import db, app, Todo
with app.app_context():

  # db.drop_all()
  # db.create_all()

  todo1 = Todo(content="ContentTest1", status=1, user_id= 1)

  # db.session.add_all([blog_post1, blog_post2, blog_post3])
  db.session.add(todo1)
  db.session.commit()