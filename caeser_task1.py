alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=char
    print(f"Here is the encrypted text:{cipher_text}")
        
def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position-shift_key)%26
            plain_text+=alphabet[new_position]
        else:
            plain_text+=char
    
    print(f"Here is the decrypted text:{plain_text}")
        
choice=input("Enter your choice:\n")
text=input("Type the message:\n").lower()
shift=int(input("Enter the shift key:\n"))
if choice=="encryption":
    encryption(plain_text=text,shift_key=shift)
elif choice=="decryption":
     decryption(cipher_text=text,shift_key=shift)
    
        
