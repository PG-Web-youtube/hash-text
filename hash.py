import hashlib

your_hash = input("Enter your MD5 hash : ")
wordlist = input(" password file : ")

flag = 0

try:
    passfile = open(wordlist, "r")
except:
    print("NO file Found")
    quit()

for word in passfile:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    print(word)
    print(digest)
    print(your_hash)

    if digest == your_hash:
        print("Password Found")
        print("Password is " + word)
        flag = 1
        break
if flag == 0:
    print("Password Not Found")