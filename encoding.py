def encoding(message):
    count = 0
    result = ""
    char = message[0]
    for i in range (0, len(message)):
        if (message[i] == char):
            count +=1
        else:
            char = message[i]
            result += str(count)+message[i -1]
            count = 1
    result += str(count)+message[-1]
    return result
encoded_message = encoding("ABBBBCCCCCCCCAB")
print(encoded_message)

