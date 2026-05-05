def fun(z):
    return z*2

print(fun(23))

# 

# list is just an array

# tuples are immutable ,(), space with ,
# dictionaries way of eliminating errors 
    # joel.get("joel",0) -->if joel is not present in teh dic then the output will be 0
    # .keys() .values() .items()


sentence={"python","math","python","english"}

word={}
for w in sentence:
    if w in word:
        word[w]+=1
    else:
        word[w]=1

print(word)