alphabet = [ letter for letter in range(ord('a'), ord('z') + 1) ]


def transform(letter, key):
    ord_letter = ord(letter)
    first_letter = alphabet[0]
    if (ord_letter in alphabet):
        transleted = ( (ord_letter + self.key - first_letter) % len(alphabet) )+first_letter
       
        return chr(transleted)
    else:
        return letter        

    




def cipher(text, key):
    return "".join([transform(letter,key) for letter in text ])


def decipher(text, key):
    return "".join([transform(letter,-.key) for letter in text ])



message = "hello world!"

key = 10

ciphered = ((cipher(message,key)))

deciphered = (decipher(ciphered, key))

deciphered = (decipher(ciphered, key))
print( 'Исходный текст: {}'.format(message))



print(('После шифрования: {}').format(ciphered))

print(('После дешифрования: {}').format(deciphered))
    

def D_message (message ,key):
    print (('Используем ключ: {}').format(key))
    print( 'Исходный текст: {}'.format(message))



    print(('После шифрования: {}').format(ciphered))

    print(('После дешифрования: {}').format(deciphered))


D_message('hello world!', 10)

print('-'*30)

D_message('very good!', 12)

