

class DMessageEngine():
    #КОНСТРУКТОР КЛАССА
    def __init__(self, key):
        self.key = key
        self.alphabet = [ letter for letter in range(ord('a'), ord('z') + 1)]
        self.alphabet2 = [ letter for letter in range(ord('A'), ord('Z') + 1)]
        
    def transform (self, letter, key):
        ord_letter = ord(letter)
        first_letter = self.alphabet[0]
        first_letter2 = self.alphabet2[0]
        
        if (ord_letter in self.alphabet):
            transleted = ((ord_letter + key - first_letter) % len(self.alphabet))+first_letter
            return chr(transleted)
        if (ord_letter in self.alphabet2):
            transleted = ((ord_letter + key - first_letter2) % len(self.alphabet2))+first_letter2
            return chr(transleted)
        else:
            return letter
                    
        
    def report(self,begining_message):
        ciphered = ((self.cipher(begining_message,)))

        deciphered = (self.decipher(ciphered, ))
        print (('Используем ключ: {}').format(self.key))
        print( 'Исходный текст: {}'.format(begining_message))



        print(('После шифрования: {}').format(ciphered))

        print(('После дешифрования: {}').format(deciphered))



    def cipher(self,message):
        return "".join([self.transform(letter,self.key) for letter in message ])
    def decipher(self, ciphered):
        return "".join([self.transform(letter,-self.key) for letter in ciphered ])

       
        

   