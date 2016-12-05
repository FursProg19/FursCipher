alphabet_eng = [ chr (letter) for letter in range(ord('a'), ord('z') + 1)]
alphabet_rus = [ chr (letter) for letter in range(ord('а'), ord('я') + 1)]
alphabet_deu = ['a']+['ä']+[chr (l) for l in range(ord('b'), ord('o') + 1)]+['ö']+[chr(l) for l in range(ord('p'), ord('s') + 1)]+['ß','t','u','ü','v','w','x','y','z']

class DMessageEngine():
    #КОНСТРУКТОР КЛАССА
    def __init__(self, key, lenguage ):
        self.key = key
        
        self.lenguages =   {'alphabet_eng': alphabet_eng,
                            'alphabet_rus': alphabet_rus,
                            'alphabet_deu': alphabet_deu}   
        self.lenguage = lenguage
                 
    
  #  print( alphabet_now (self, self.rus))
    
    def transform (self, letter, key):
        
        selected_alphabet = self.lenguages [self.lenguage]
        isupper = letter.isupper()
        low = letter.lower()           

        if low not in selected_alphabet:
            return letter
        else:
            ord_letter = selected_alphabet.index(low)
            transleted = ((ord_letter + key ) % len(selected_alphabet))
            if isupper:
                return selected_alphabet[transleted].upper()
            return selected_alphabet[transleted]              
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

       
        

   