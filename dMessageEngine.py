alphabet_eng = [ chr (letter) for letter in range(ord('a'), ord('z') + 1)]
alphabet_rus = [ chr (letter) for letter in range(ord('а'), ord('я') + 1)]
alphabet_deu = ['a']+['ä']+[chr (l) for l in range(ord('b'), ord('o') + 1)]+['ö']+[chr(l) for l in range(ord('p'), ord('s') + 1)]+['ß','t','u','ü','v','w','x','y','z']

class DMessageEngine():
    #КОНСТРУКТОР КЛАССА
    def __init__(self, key, language, algoritm ):
        self.key = key
        
        self.languages =   {'alphabet_eng': alphabet_eng,
                            'alphabet_rus': alphabet_rus,
                            'alphabet_deu': alphabet_deu}   
        self.language = language
        
        self.algoritms ={
            'ceasarus': self.transform_ceasarus,
            'vigenere': self.transform_vigenere
        }
        self.selected_algoritm = algoritm
        if self.selected_algoritm == 'vigenere':
            self.current_index = None
            self.actual_key = key 
            selected_alphabet = self.languages [self.language]
            self.key = selected_alphabet.index (self.actual_key[0])
            
    def transform_ceasarus (self, letter, key):
        
        selected_alphabet = self.languages [self.language]
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

    def transform_vigenere (self, letter, key):
        selected_alphabet = self.languages [self.language]
        if self.current_index == None:
            self.current_index = 0
        else:
            if self.current_index == len(self.actual_key) - 1:
                self.current_index = 0
            else:
                self.current_index
                
        index_key = selected_alphabet.index (self.actual_key[self.current_index])
        if key < 0:
            index_key = -index_key
        return self.transform_ceasarus (letter, index_key)

        
    def report(self,begining_message):
        ciphered = ((self.cipher(begining_message,)))

        deciphered = (self.decipher(ciphered, ))
        print (('Используем ключ: {}').format(self.key))
        print( 'Исходный текст: {}'.format(begining_message))



        print(('После шифрования: {}').format(ciphered))

        print(('После дешифрования: {}').format(deciphered))



    def cipher(self,message):
        res = "".join([self.algoritms[self.selected_algoritm](letter,self.key) for letter in message ])
        if self.selected_algoritm == 'vigenere':
            self.current_index = None
        return res
    def decipher(self, ciphered):
        res =  "".join([self.algoritms[self.selected_algoritm](letter,-self.key) for letter in ciphered ])
        if self.selected_algoritm == 'vigenere':
            self.current_index = None
        return res
# Сделать понятней (с If, разными фкункициями)

       
        

   