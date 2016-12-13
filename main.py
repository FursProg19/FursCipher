from dMessageEngine import DMessageEngine as dme
# Вызов конструктора класса DMessageEngine с параметром 10 (key)
engine = dme('dad', 'alphabet_eng', 'vigenere')
engine1 = dme('dad','alphabet_eng', 'vigenere')
# ciphered присвоили результат шифрования методом cipher "hello world" (message) 
#ciphered = engine.cipher("hello world")
# Дописать
#deciphered = engine.decipher(ciphered)

engine1.report("uber")
engine.report("Ich heisse Leonid!!")

engine.report("very good???")
engine.key = 15
engine.report("i am cool!")