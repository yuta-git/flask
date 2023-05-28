def divide_else_finally(a, b):
  try:
    print(a / b)
  except ZeroDivisionError as e: # False だったら
    print('catch ZeroDivisionError:', e)
  else: # False じゃなかったら
    print('finish (no error)')
  finally: # いつでも実行
    print('all finish')
    
if True:
  divide_else_finally(1, 2)
else:
  divide_else_finally(1, 0)
  
  
try:
	a = 100/10
	raise Exception('例外のテスト') # 意図的に例外を発生させる

except Exception as e:
	print(e) # 例外のテスト