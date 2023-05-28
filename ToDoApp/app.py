from flask import Flask, render_template, url_for, redirect, flash, request
from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pytz import timezone

from flask_migrate import Migrate

#Flaskをインスタンス化
app = Flask(__name__)

#環境変数
app.config['SECRET_KEY'] = 'mysecretkey'

"""
データベースを定義
osモジュールを利用したコードは「変更に対応できる」「OSに依存しない」
"""
# __file__ Pythonのモジュールがロードされたファイルのディレクトリと名前が設定される
# os.path.dirname その中からディレクトリ名だけを取得する。
# os.path.abspath 上記まででは相対パスになっているので、絶対パスに変換する
basedir = os.path.abspath(os.path.dirname(__file__))
# SQLiteのDBを作成するディレクトリを指定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# データベースの変更履歴は不要
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemyからインスタンス化されたDBオブジェクト、データベースが作成される
db = SQLAlchemy(app)
# Migrate の設定
Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
# 以下のコードでリダイレクトするビュー関数を"login"に。
login_manager.login_view = 'login'

# 未ログインユーザーにエラーメッセージ表示
def localize_callback(*args, **kwarg):
    return 'このページにアクセスするには、ログインが必要です'
login_manager.localize_callback = localize_callback

#現在のログインユーザーの情報を保持し、必要なときに参照できるようになる。
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
  
"""
SQLAlchemy と SQLite 接続時の外部キー制約設定
"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
    
"""
フォーム User
"""
class RegistrationForm(FlaskForm):
  email = StringField('メールアドレス', validators=[DataRequired(), Email(message='正しいメールアドレスを入力してください')])
  username = StringField('ユーザー名', validators=[DataRequired()])
  password = PasswordField('パスワード', validators=[DataRequired(), EqualTo("pass_confirm", message='パスワードが一致していません')])
  pass_confirm = PasswordField('パスワード(確認)', validators=[DataRequired()])
  submit = SubmitField('登録')
  
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='正しいメールアドレスを入力してください')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('ログイン')


"""
モデル User
"""
#モデルがテーブルになる(db.Modelを継承)
class User(db.Model, UserMixin):
  #テーブル名を指定。この記述がなければクラス名がテーブル名となる。
  __tablename__ = 'user'
  #テーブル列を設定
  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String(64), unique=True, index=True)
  username = db.Column(db.String(64), unique=True, index=True)
  password_hash = db.Column(db.String(128))
  
  # Todoモデルとのリレーションシップの設定
  todo = db.relationship('Todo', backref='author', lazy='dynamic')
  
  #上記クラスをインスタンス化する初期化の処理
  #クラス内にめそっどを記述する際には"self"を入れるのが決まりごと
  def __init__(self, email, username, password):
    self.email = email
    self.username = username
    self.password = password
    
  def __repr__(self):
    return f"UserName: {self.username}"
  
  def check_password(self, password):
    return check_password_hash(self.password_hash, password)
  
  #クラスのインスタンスに保持するデータで、値の参照や変更方法を制限することが可能
  @property
  def password(self):
    raise AttributeError('password is not a readable attribute')
  
  @password.setter
  def password(self, password):
      self.password_hash = generate_password_hash(password)


"""
モデル Todo
"""
class Todo(db.Model):
  __tablename__ = 'todos'
  id = db.Column(db.Integer, primary_key=True)
  # date = db.Column(db.DateTime, default=datetime.now(timezone('Asia/Tokyo')))
  content = db.Column(db.String(140))
  status = db.Column(db.Integer)
  
  #外部キー制約
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __init__(self, content, status, user_id):
    self.content = content
    self.status = status
    self.user_id = user_id
  
  def __repr__(self):
    return f"PostID: {self.id}, Title: {self.title}, Author: {self.author} \n"


"""
ビュー関数 Todo
"""
@app.route('/')
# 未ログインユーザーはログインページに転送されるようになる。
@login_required
def index():
  # todos = Todo.query.all()
  todos = Todo.query.filter_by(user_id=current_user.id)
  return render_template("index.html", todos = todos)

@app.route('/new', methods=["POST"])
def new():
    content = request.form["new_text"]
    #フォームのinput hidden で current_user.id をもたせる
    user_id = request.form["user_id"]
    todo = Todo(content=content, status=0, user_id=user_id)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))
  
@app.route('/completion', methods=["POST"])
def completion():
    id = request.form["id"]
    todo = Todo.query.filter_by(id=id).first()
    todo.status = 1
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update', methods=["POST"])
def update():
  id = request.form["id"]
  content = request.form["text"]
  todo = Todo.query.filter_by(id=id).first()
  todo.content = content
  db.session.commit()
  return redirect(url_for('index'))

@app.route('/delete', methods=["POST"])
def delete():
    id = request.form["id"]
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


"""
ビュー関数 User
"""
@app.route("/user_maintenance")
def user_maintenance():
  #全レコードの取得
  users = User.query.all()
  return render_template("user_maintenance.html", users=users)

# 新規登録
@app.route("/register", methods=["GET", "POST"])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(email=form.email.data, username=form.username.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("index"))
  return render_template("register.html", form=form)

# ログイン
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            if user.check_password(form.password.data):
                #ログイン処理
                login_user(user)
                next = request.args.get('next')
                if next == None or not next[0] == '/':
                    next = url_for('index')
                return redirect(next)
            else:
                flash('パスワードが一致しません')
        else:
            flash('入力されたユーザーは存在しません')
    return render_template('login.html', form=form)

@app.route('/logout')
# 未ログインユーザーはログインページに転送されるようになる。
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

"""
起動処理
"""
if __name__ == "__main__":
    # app.run(debug=True)
    # app.run(host="0.0.0.0", port=80, debug=True)
    app.run(host="0.0.0.0", port=80, debug=False)