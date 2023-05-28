from app import db, app, User 
with app.app_context():

# データベースと全てのテーブルを削除
  db.drop_all()

# データベースと全てのテーブルを作成
  db.create_all()

  #モデルに初期値を設定。これを実行すると、クラス内で定義した__init__メソッドが呼び出されてインスタンスに初期値が設定される。カラムの順番も合わせる。
  user1 = User("test_user1@test.com", "Test User1", "111")
  user2 = User("test_user2@test.com", "Test User2", "222")

  #テーブルにデータを追加
  db.session.add_all([user1, user2])

  # db.session.add(user1)
  # db.session.add(user2)

  db.session.commit()

  print(user1.id)
  print(user2.id)