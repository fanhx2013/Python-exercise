#将输入的字符串设置为密码，规律是a->f，b->g；A->F, B->G，以此类推；同样可以反向解密。
str_original = ''
str_original_to_cipher = ''

str_cipher = ''
str_cipher_to_original = ''

def cipher(str_original):
    str_original = input("Please input the original: ")
    global str_original_to_cipher
    for r in str_original:
        num1 = ord(r)
        if (num1 > 64 and num1 < 86) or (num1 > 96 and num1 < 118):
            str_original_to_cipher += chr(num1 + 5)
        elif (num1 > 85 and num1 < 91) or (num1 > 117 and num1 < 123):
            str_original_to_cipher += chr(num1 + 5 - 26)
        else:
            str_original_to_cipher += chr(num1)
    print(str_original_to_cipher)

def decipher(str_cipher):
    str_cipher = input("Please input the cipher: ")
    global str_cipher_to_original
    for i in str_cipher:
        num2 = ord(i)
        if (num2 > 64 and num2 < 70) or (num2 > 96 and num2 < 102):
            str_cipher_to_original += chr(num2 + 26 - 5)
        elif (num2 > 69 and num2 < 91) or (num2 > 101 and num2 < 123):
            str_cipher_to_original += chr(num2 - 5)
        else:
            str_cipher_to_original += chr(num2)
    print(str_cipher_to_original)



choose_service = input("Please choose the service 1 or 2 below:\n"
                       "1.Input the original, and translate to cipher.\n"
                       "2.Input the cipher, and decipher it to original.\n")
if choose_service == '1':
    cipher(str_original)
elif choose_service == '2':
    decipher(str_cipher)
