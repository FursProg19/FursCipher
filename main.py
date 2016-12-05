from dMessageEngine import DMessageEngine as dme
# Вызов конструктора класса DMessageEngine с параметром 10 (key)
engine = dme(10,)
engine1 = dme(15,)
# ciphered присвоили результат шифрования методом cipher "hello world" (message) 
#ciphered = engine.cipher("hello world")
# Дописать
#deciphered = engine.decipher(ciphered)

engine1.report("über")
engine.report("Ich heiße Leonid!!")

engine.report("very good???")
engine.key = 15
engine.report("i am cool!")