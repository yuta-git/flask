"""
セッション管理に利用するSECRET_KEYと、パスワード
の暗号化の際に利用するSALTを保持するためのkey.pyファイルを作成します。
なぜ別ファイルに記述するのかと言うと、app.py等に直接記述してしまうと
GitHub等のコード共有サービスに上げた際に暗号化キーが漏洩してしまうためです。
"""

#どちらも任意の文字列で大丈夫です
SECRET_KEY = "g8wkf0pvje6m2unhgt3j"
SALT = "762ifuw9fj5wxjkeu0dk"