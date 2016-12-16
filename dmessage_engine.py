alphabet_eng = [ chr (letter) for letter in range(ord('a'), ord('z') + 1)]
alphabet_rus = [ chr (letter) for letter in range(ord('а'), ord('я') + 1)]
alphabet_deu = ['a']+['ä']+[chr (l) for l in range(ord('b'), ord('o') + 1)]+['ö']+[chr(l) for l in range(ord('p'), ord('s') + 1)]+['ß','t','u','ü','v','w','x','y','z']
class DMessageEngine():
    def __init__ (self, key, language):
        self.key = key
        
        self.languages =   {'en': alphabet_eng,
                            'ru': alphabet_rus,
                            'de': alphabet_deu}   
        
        self.language = language

    def report(self,begining_message):
        ciphered_message = ((self.cipher(begining_message)))
        deciphered_message = (self.decipher(ciphered_message ))

        
        print (('Используем ключ: {}').format(self.key))
        print( 'Исходный текст: {}'.format(begining_message))
        print(('После шифрования: {}').format(ciphered_message))
        print(('После дешифрования: {}').format(deciphered_message))

    def cipher(self,message):
        return "".join([self.cipher_letter(letter) for letter in message ])

    def decipher(self, ciphered):
        return "".join([self.decipher_letter(letter) for letter in ciphered ])

    def cipher_letter (self, letter):
        return letter
    
    def decipher_letter (self, letter):
        return letter    


       
        

   