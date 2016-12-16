from vigenere_engine import VigenereEngine
from ceasarus_engine import CeasarusEngine
# Вызов конструктора класса DMessageEngine с параметром 10 (key)
engine = VigenereEngine('bbc', 'en')
engine1 = CeasarusEngine(9, 'de')
# ciphered присвоили результат шифрования методом cipher "hello world" (message) 
#ciphered = engine.cipher("hello world")
# Дописать
#deciphered = engine.decipher(ciphered)

engine1.report("öuber")
engine.report("Ich heisse Leonid!!")

engine.report("very good???")

engine.report("i am cool!")