file = input("Masukkan nama file : ")
handle = open(file)
ini_dict = dict()

for baris in handle:
    if baris.startswith("From "):
        kata = baris.split()
        email = kata[1]
        
        simbol_at = email.find('@')
        domain = email[simbol_at + 1:]
        
        ini_dict[domain] = ini_dict.get(domain, 0) + 1

print(ini_dict)
handle.close()


