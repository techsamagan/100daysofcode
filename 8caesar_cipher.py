#day 8 - Caesar Ciper encrypt and decrypt


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode(text, shift):

    before = []
    after = []
    encpyption = []
    for i in text:
        if i==" ":
            before.append(-1)
        for k in alphabet:
            if i==k:
                num = alphabet.index(k)
                before.append(num)
    
#    print(before)  
    for j in before:
        if j >= 0:
            j += shift
            if j > 25:
                j = j%25
            after.append(j)
        elif j == -1:
            after.append(-1)
#    print(after)
    for l in after:
        if l == "*":
            encpyption.append(" ")
        else:
            encpyption.append(alphabet[l])
    encpyption_word = "".join(encpyption)
    print("Your encoded word is : ")
    print(encpyption_word)
    
def decode(text, shift):

    before = []
    after = []
    decpyption = []
    for i in text:
        if i==" ":
            before.append("*")
        for k in alphabet:
            if i==k:
                num = alphabet.index(k)
                before.append(num)
    
#    print(before)  
    for j in before:
        if j >= 0:
            j -= shift
            if j > 25:
                j = j%25
            after.append(j)
        elif j == "*":
            after.append(-1)
#    print(after)
    for l in after:
        if l == "*":
            decpyption.append(" ")
        else:
            decpyption.append(alphabet[l])
    decpyption_word = "".join(decpyption)
    print("Your decoded word is : ")
    print(decpyption_word)




while True:
    ques = int(input("Do you want encode or decode? if encode enter 1 if decode please enter 2: "))
    if ques == 1:
        text = str(input("Enter the text to encrypt: "))
        shift = int(input("Enter the shift for encrypt: "))
        encode(text, shift)
    elif ques == 2:
        text = str(input("Enter the text to decrypt: "))
        shift = int(input("Enter the shift for decrypt: "))
        encode(text, shift)
    else:
        print("Your choice is incorrest. Please choose again")






















