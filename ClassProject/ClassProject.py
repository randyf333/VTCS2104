import hashlib
import time
import binascii
import itertools

import matplotlib.pyplot as plt


def hash(password, hashType):
    hashed_pwd = hashlib.pbkdf2_hmac(hashType, #later you will changes this to sha512
                         password.encode('utf-8'),# passowrd is encoded into binary  
                         'saltPhrase'.encode('utf-8'),# 'salt' is an extra bit of info added to the password. When using randomized 'salt' dictionary attacks becomes nealry impossible. For this project keep 'salt' static. In the real world 'salt' is randomized and later exctracted from the hashed password during the verififcation process. Essentially, the 'salt' portion of the hash can be separated from the password portion.
                         1000) # number of iterations ('resolution') of the hashing computation)
    hashed_pwd = binascii.hexlify(hashed_pwd)
    #print(hashed_pwd)
    return hashed_pwd# converting binary to hex

# def password_combo(words, length):
#     for r in range(1, min(length,3)+1):
#         for combo in itertools.product(words,repeat=r):
#             yield ''.join(combo)

def password_combo(words, userInput): 
    for i in range(1,4):
        for combo in itertools.product(words,repeat=i):
            word = ''.join(combo)
            if(len(word) == len(userInput)):
                yield word

# def crackWord(wordList, hashString, hashType):
#     start_time = time.time()
#     guesses = 0
#     for word in wordList:
#         guesses+=1
#         if(hash(word, hashType) == hashString):
#             print("Hash ", hashType, "cracked ",userInput," in ", time.time()-start_time)
#             return time.time()-start_time,guesses,True
#     return time.time()-start_time,guesses,False

def tryWord(word, hashString, hashType):
    if hash(word,hashType) == hashString:
        return True


def plot_results(results,wordlist):
    plt.figure(figsize=(10, 6))
    for result in results:
        plt.scatter(result['guesses'], result['time'], label=f"{result['hash_type']} ({result['password']})")
    plt.xlabel('Guesses')
    plt.ylabel('Time (seconds)')
    plt.title("Time vs Number of Guesses\nDictionary Size:"+len(wordList))
    plt.legend()
    plt.grid(True)
    plt.show()

userInput = input("Password: ")
#f = open(".txt","r")
f = open("best110.txt","r")
wordList = []
for x in f:
    wordList.append(x.rstrip("\n"))
f.close()

graphData = []
algorithms = ['sha256','sha512']
while(userInput != "q"):
    for algorithm in algorithms:
        #found = False
        guesses = 0
        start_time = time.time()
        for guess in password_combo(wordList, userInput):
            guesses += 1
            if tryWord(guess,hash(userInput,algorithm),algorithm):
                    time_taken = time.time()-start_time
                    print("Hash", algorithm, "cracked",userInput,"in", time_taken)
                    graphData.append({'hash_type':algorithm,'dict_size':len(wordList),'time':time_taken,'guesses':guesses,'password':userInput})
                    break
    userInput = input("Password: ")

#Create graph   
plot_results(graphData,wordList)



