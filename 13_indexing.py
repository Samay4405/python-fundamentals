# string indexing = accessing elements of a sequence using [] (indexing operstor)
#                     [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])                     # TO GET THE CHARACTER OF THE POSITION.
print(credit_number[1])                    
print(credit_number[4])
print(credit_number[0:4])                   # TO GET FIRST 4 CHARACTER  
print(credit_number[:4])                    # SAME
print(credit_number[5:9])                   # TO GET CHARACTERS FROM PLACE 5 TO 9TH.
print(credit_number[5:])                    # TO GET CHARACTERS FROM PLACE 5.
print(credit_number[-1])                    # TO GET LAST CHARACTER
print(credit_number[-2])
print(credit_number[::2])                   # TO GET EVERY SECOND CHARACTER
print(credit_number[::3])                   # TO GET EVERY THIRD CHARACTER
print(credit_number[::-1])                  # TO GET THE REVERSE ORDER OF THE CHARACTERS.
print(credit_number[:-5:])                  # DOES NOT DISPLAY LAST 5 CHARACTERS
print(credit_number[:-5])                   # SAME SHIT
print(credit_number[:5:])                   # DISPLAYS FIRST 5 CHARACTERS


LAST_DIGITS = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{LAST_DIGITS}")