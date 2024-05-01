file = input("Masukkan nama file : ")
handle = open(file)
ini_dict = dict()

for baris in handle:
    if baris.startswith("From "):
        kata = baris.split()
        email = kata[1]
        
        ini_dict[email] = ini_dict.get(email, 0) + 1

print(ini_dict)
handle.close()

