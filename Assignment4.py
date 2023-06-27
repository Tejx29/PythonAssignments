#Loop manipulation Statements

#break
for i in "tejas":
    if i=="c":
        break
    else:
        print(i)

i=1
while i<=10:
    if i==5:
        break
    else:
        print(i)


#pass
for i in "tejas":
    if i=="e":
        pass
    else:
        print(i)

i=1
while i<=10:
    if i==5:
        pass
    else:
        print(i)


#continue
for i in "tejas":
    if i=="j":
        continue
    else:
        print(i)

i=1
while i<=10:
    if i==5:
        continue
    else:
        print(i)

        
#for with else loop
for i in "tejas":
    if i=="a":
        break
    else:
        print(i)
else:
    print("This has break")

for i in "tejas":
    if i=="t":
        pass
    else:
        print(i)
else:
    print("This has pass")

for i in "tejas":
    if i=="t":
        continue
    else:
        print(i)
else:
    print("This has continue")


#while with else loop
i=1
while i<=10:
    if i==5:
        break
    else:
        print(i)
else:
    print("This has break")

i=1
while i<=10:
    if i==5:
        continue
    else:
        print(i)
else:
    print("This has continue")

i=1
while i<=10:
    if i==5:
        pass
    else:
        print(i)
else:
    print("This has pass")

