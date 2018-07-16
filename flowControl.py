secret = "swardnet"

pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count == 2: break
    pw = input("what is the secret word: ")
else: # only traverse when while look finishes normally, not break out
    auth = True

print('Authorized' if auth else 'calling the FBI')