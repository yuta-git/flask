"""
a が空の場合は返却値に0を入れ、そうでなければ b の値を確認する。
その b が空の場合は...と思考のままにプログラムを行うとネストが深くなりがちに。。
"""
def badCheck(a, b, c):
  if not a:
    result = 0
  else:
    if not b:
      result = 0
    else:
      if not c:
        result = 0
      else:
        result = 1
  return result

"""
「ガード節」を使い書き換えた場合
関数の先頭に異常系となる条件を集め、即座にreturnしています。
正常系と異常系が明確になっていますね。
"""
def check (a, b, c):
  if not a:
    return 0
  if not b:
    return 0
  if not c:
    return 0
  return 1

    
check = check(1, 1, 1)
print(check)

badCheck = badCheck(1, 1, 0)
print(badCheck)

