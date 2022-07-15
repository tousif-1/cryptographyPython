alpha = 'abcdefghijklmnopqrstuvwxyz'

message = input("Enter the message: ") 

def decrypt(msg,key):
    caeserCode = ''
    for k in msg.lower():
        
        try:    
                temp = (alpha.index(k) + key) % 26
                caeserCode += alpha[temp]
         
        except ValueError:
            caeserCode += k
    return caeserCode.lower()

for key in range(1,26):
  
    encrypt_text = decrypt(message,key)

    print ("Encrypted Data for key " +str(key)+ " is: "  +encrypt_text)
