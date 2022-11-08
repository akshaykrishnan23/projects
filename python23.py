import random
digits=['0','1','2','3','4','5','6','7','8','9']
lowercase=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
uppercase=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
symbols=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
mix=digits+lowercase+uppercase+symbols
maxlen=8
rand_digit = random.choice(digits)
rand_upper = random.choice(uppercase)
rand_lower = random.choice(lowercase)
rand_symbol = random.choice(symbols)
password=rand_digit + rand_upper + rand_lower + rand_symbol
for x in range(maxlen -4):
    password=password+random.choice(mix)
print("YOUR PASSWORD IS :" ,password)

