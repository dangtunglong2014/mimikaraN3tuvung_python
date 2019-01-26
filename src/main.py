import random

print("By Long Dang")

key = "0"
while(int(key) < 1 or int(key) > 12):
	key = raw_input("Unit 1/2/3/4/5/6/7/8/9/10/11/12: ")

dirVie = "./dat/Unit" + key + "/vie.dat"
arrayVie = []
with open(dirVie, "r") as file:
    for line in file:
    	line = line.strip()
        arrayVie.append(line)
#print(len(arrayVie))

dirHira = "./dat/Unit" + key + "/hiragana.dat"
arrayHira = []
with open(dirHira, "r") as file:
    for line in file:
    	line = line.strip()
        arrayHira.append(line)
#print(arrayHira[1])

dirKanji = "./dat/Unit" + key + "/kanji.dat"
arrayKanji = []
with open(dirKanji, "r") as file:
    for line in file:
    	line = line.strip()
        arrayKanji.append(line)
#print(arrayKanji[1])

dirSen = "./dat/sentence.dat"
arraySen = []
with open(dirSen,"r") as file:
	for line in file:
		line = line.strip()
		arraySen.append(line)

arrayQuestion = arrayVie
print("a. " + arraySen[4])
print("b. " + arraySen[5])
print("c. " + arraySen[6])
key = raw_input("a/b/c: ")
if(key == "a"): 
	arrayAnswer = arrayKanji
else: 
	if (key == "b"):
		arrayAnswer = arrayHira
	else:
		if (key == "c"):
			for i in range(len(arrayVie)):
				print('{:<30}'.format(arrayVie[i]) + '{:<20}'.format(arrayKanji[i]) + '{:<20}'.format(arrayHira[i]))
				print("") 
			quit();
		else:
			quit();

arrayID = range(0,len(arrayQuestion))
random.shuffle(arrayID)
#print(arrayID)
for i in range(len(arrayID)):
	arrayChoice = []
	arrayIndex = []

	question = arrayQuestion[arrayID[i]]
	#print(question)
	trueAnswer = arrayAnswer[arrayID[i]]
	arrayAnswer.pop(arrayID[i])

	for j in range(3):
		wrongAnswer = random.choice(arrayAnswer)
		arrayChoice.append(wrongAnswer)
		idx = arrayAnswer.index(wrongAnswer)
		arrayIndex.append(idx)
		arrayAnswer.pop(idx) 

	for j in range(3):
		arrayAnswer.insert(arrayIndex[2-j], arrayChoice[2-j])

	arrayAnswer.insert(arrayID[i], trueAnswer)
	arrayChoice.append(trueAnswer)
	random.shuffle(arrayChoice)

	print(str(i+1) + ". " + question)
	for m in range(len(arrayChoice)):
		print(chr(m+65) + ". " + arrayChoice[m])

	key = raw_input("A/B/C/D/Q: ")
	if(key == "q"):
		break 
	A = key == "a" and arrayChoice[0] == trueAnswer
	B = key == "b" and arrayChoice[1] == trueAnswer
	C = key == "c" and arrayChoice[2] == trueAnswer
	D = key == "d" and arrayChoice[3] == trueAnswer
	if( A or B or C or D):
		print(arraySen[0])
	else:
		print(arraySen[1] + trueAnswer + arraySen[2])

print(arraySen[3])







	

