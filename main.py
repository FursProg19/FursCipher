from dMessageEngine import DMessageEngine as dme
# Вызов конструктора класса DMessageEngine с параметром 10 (key)
engine = dme(10)
engine1 = dme(15)
# ciphered присвоили результат шифрования методом cipher "hello world" (message) 
ciphered = engine.cipher("hello world")
# Дописать
deciphered = engine.decipher(ciphered)

engine.report("hello world!")
engine1.report("hello world!")

engine.report("very good???")
engine.key = 15
engine.report("i am cool!")