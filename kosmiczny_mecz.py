#1.1
with open("mecz_przyklad.txt", "r") as plik:
    file = plik.read()
    change_AB = file.split("AB")
    change_BA = file.split("BA")

print(len(change_AB)+len(change_BA)-2)

#1.2
A_wins = 0
B_wins = 0

for i in range(len(file)):
    if file[i] == "A":
        A_wins += 1
    if file[i] == "B":
        B_wins += 1
    if A_wins >= 1000 or B_wins >= 1000:
        if A_wins+3 <= B_wins or B_wins+3 <= A_wins:
            print(f"pierwszy set: {A_wins}:{B_wins}")
            break
 #1.3
passaA = 0
passaB = 0
dobra_passaA = 0
dobra_passaB = 0

for i in range(len(file)-1):
    if file[i] == file[i+1] == "A":
        passaA += 1
    if file[i] == file[i+1] == "B":
        passaB += 1
    if passaB >= 10:
       dobra_passaB += 1
    if passaA >= 10:
        dobra_passaA += 1
print(f"dobre passy A: {dobra_passaA}")
print(f"dobre passy B: {dobra_passaB}")