alphabet_eng = [ letter for letter in range(ord('a'), ord('z') + 1)]
alphabet_rus = [ letter for letter in range(ord('а'), ord('я') + 1)]
alphabet_deu = ['a']+['ä']+[chr (l) for l in range(ord('b'), ord('o') + 1)]+['ö']+[chr(l) for l in range(ord('p'), ord('s') + 1)]+['ß','t','u','ü','v','w','x','y','z']
alphabet_deu = [ord(letter) for letter in alphabet_deu]

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
        
        selected_alphabet = []
        low = letter.lower()
        ord_letter = ord(low)
                    
        for alphabet in self.alphabets:
            if ord_letter in alphabet:
                selected_alphabet = alphabet
                break
        if selected_alphabet == []:
            return letter
        else:
            first_letter = selected_alphabet[0]
            if (ord_letter in selected_alphabet):
                transleted = ((ord_letter + key - first_letter) % len(selected_alphabet))+first_letter
                if isupper:
                    return (chr(transleted)).upper()
                return chr(transleted)                    
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

       
        

   