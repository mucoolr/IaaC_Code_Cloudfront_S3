import re

n = int(input())

for card in range(n):
    
    card_number= input().strip()
    card_number_removed_hiphen = credit.replace('-','')
    
    valid = True
    
    card_length_16 = bool(re.match(r'^[4-6]\d{15}$',card_number))
    card_length_19 = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$',card_number))    
    consecutive_digit = bool(re.findall(r'(?=(\d)\1\1\1)',card_number_removed_hiphen))
    
    if card_length_16 == True or card_length_19 == True:
        if consecutive_digit == True:
            valid=False
    else:
        valid = False       
    if valid == True:
        print('Valid')
    else:
        print('Invalid')
