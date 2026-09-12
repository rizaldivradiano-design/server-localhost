#Github By Rizal
#YT @MrRall_2JT

import time 
import os  

print("=== PILIH PORT SERVER ===")
print("1. 8080")
print("2. 8000") 
print("3. 8059")
port = input("Pilih apa? ")

if port == "1":
   port_angka = "8080"
elif port == "2":
    port_angka = "8000"
elif port == "3":
    port_angka = "8059"
else:
    print("Salah pilih opsi 1,2,3")
    exit() 
print(f"\nMenjalankan server di http://localhost:{port_angka}")
print("Tekan CTRL + C untuk berhenti")
time.sleep(2)
os.system(f"python -m http.server {port_angka} --bind 0.0.0.0")
