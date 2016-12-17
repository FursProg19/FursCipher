from vigenere_engine import VigenereEngine
from ceasarus_engine import CeasarusEngine
# Вызов конструктора класса DMessageEngine с параметром 10 (key)
# ciphered присвоили результат шифрования методом cipher "hello world" (message) 
#ciphered = engine.cipher("hello world")
# Дописать
#deciphered = engine.decipher(ciphered)

# engine1.report("О")
# engine.report("Привет")
# engine.report("Как дела")
# engine.report("Спокойной ночи!!")

import web
        
urls = (
    '/(.*)', 'hello'
)

app = web.application(urls, globals())

engine = VigenereEngine('вав', 'ru')
ceasarus_engine = CeasarusEngine(10, 'en')

class hello:        
    def GET(self, name):
        # if not name: 
        #     name = 'roro'
        # return 'Hello, ' + name + '!'
        return ceasarus_engine.cipher(name)

if __name__ == "__main__":
    web.config.debug = True
    app.run()