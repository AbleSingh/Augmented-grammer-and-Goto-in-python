prod={}
nonterminals = []
inot = []
templist = []
goto = []

print("enter the number of productions :: ")
n = int(input())

p=[]
print("Enter productions :: ")
for i in range(n):
    x = input()
    p.append(x)

for i in range(n):
    prodlist=p[i].split('->')
    tempdict = {prodlist[0]:prodlist[1].split('|')}
    prod.update(tempdict)
    tempdict.clear()
    nonterminals.append(prodlist[0])
    
allprodlist = []

for i in prod:
    for j in prod[i]:
        allprodlist.append(i+"->"+j)

for i in range(len(allprodlist)):
    allprodlist[i] = allprodlist[i].split('->')[0] + "->" + "." + allprodlist[i].split('->')[1]

augGrammar = allprodlist[0].split('->')[0]+"'" + "->" + "." + allprodlist[0].split('->')[0]
allprodlist.insert(0,augGrammar)

for i in range(len(allprodlist)):
    if allprodlist[i].split(".")[1][0] in nonterminals:
        for j in range(len(allprodlist)):
            if allprodlist[j].split("->")[0] == allprodlist[i].split(".")[1][0]:
                templist.append(allprodlist[j])
                
        for i in range(len(templist)):
            inot.append(templist[i])
        
inot = list(set(inot))
inot.insert(0, augGrammar)
print(inot)


print("\n\nEnter the goto action to be performed :: ")
gotoGiven = input()

if gotoGiven.split(".")[1][0] in nonterminals:
    goto.append(gotoGiven.split(".")[0] + gotoGiven.split(".")[1] + ".")
    for i in range(len(allprodlist)):
        if allprodlist[i].split("->")[0] == gotoGiven.split(".")[1][0]:
            goto.append(allprodlist[i])
else:
    goto.append(gotoGiven.split(".")[0] + gotoGiven.split(".")[1] + ".")
    
print(goto)

# E->E+T|T
# T->i|(E)

