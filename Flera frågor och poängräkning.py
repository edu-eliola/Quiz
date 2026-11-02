a = 0
gissning_1 = int(input("Vilken huvudstad har Norge? \n1. Oslo \n2. Bergen \n3. Trondheim \nDitt val: "))
if gissning_1 == 1:
    print("Rätt, Oslo är Norges huvustad")
    a += 1
else:
    print("Fel, Norges huvudstad är Oslo")

gissning_2 = int(input("\nVilket år började andra världskriget? \n1. 1914 \n2. 1939 \n3. 1945 \nDitt val: "))
if gissning_2 == 2:
    print("Rätt, andra världskriget började år 1939")
    a +=1
else:
    print("Fel, andra världskriget började år 1939")

print(f"\nDu fick {a} av 2 rätt")