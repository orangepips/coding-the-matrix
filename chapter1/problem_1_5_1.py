import string

letter2number = {k:v for k,v in zip([c for c in string.ascii_uppercase + ' '], range(27))}
number2letter = {k:v for k,v in zip(range(27), [c for c in string.ascii_uppercase + ' '])}

'''
A -> 0 -> 00000
B -> 1 -> 00001
Z -> 25 -> 11001
space -> 26 -> 11010
'''

cyphertext = '10101 00100 10101 01011 11001 00011 01011 10101 00100 11001 11010'
cyphertext_decimals = [int(sequence, 2) for sequence in cyphertext.split()]

if __name__ == "__main__":
    for key in range(27):
        try:
            print(''.join([number2letter[c ^ key] for c in cyphertext_decimals]))
        except KeyError:
            continue
# EVE IS EVIL