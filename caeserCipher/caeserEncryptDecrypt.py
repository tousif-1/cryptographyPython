alpha = 'abcdefghijklmnopqrstuvwxyz'

def caeserCip(msg,key):
    caeserCode = ''
    for k in msg.lower():
        try:
            temp = (alpha.index(k) + key) % 26
            #print (alpha.index(k))
            caeserCode += alpha[temp]
        except ValueError:
            caeserCode += k
    return caeserCode.lower()



def caeserDCip(msg,key):
    caeserCode = ''
    for k in msg.lower():
        try:
            temp = (alpha.index(k) - key) % 26
            #print (alpha.index(k))
            caeserCode += alpha[temp]
        except ValueError:
            caeserCode += k
    return caeserCode.lower()



message = input("Enter the message: ") 

key = 4

encrypt_text = caeserCip(message,key)

print ("Encrypted Data: ", encrypt_text)

Decrypt_text = caeserDCip(encrypt_text,key)

print ("Decrypted Data: ", Decrypt_text)
