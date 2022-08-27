from petriDish import bug

tyler = bug('tyler').generateBug()
print('MOMMA BUG\n__________________________')
tyler.printBug()

mitchell = bug('mitchell').generateBug()
print('DADA BUG\n__________________________')
mitchell.printBug()


genOne = []
for i in range(10):
    genOne.append(tyler.mateBug(mitchell))

for kid in genOne:
    kid.printBug()
    print('\n')