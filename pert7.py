# operasi logika atau bolean 
# not, or, and, xor 

print ("=========NOT=========")
a = True
b = not a
print("nilai dari b = ", b)

print ("=========OR(ATAU)=========")
print("hasil akan true, selama ada satu saja true")
a = False
b = False
hasil = a or b 
print(a, "OR", b, "=", hasil)
a = False
b = True
hasil = a or b 
print(a, "OR", b, "=", hasil)
a = True
b = False
hasil = a or b 
print(a, "OR", b, "=", hasil)
a = True
b = True
hasil = a or b 
print(a, "OR", b, "=", hasil)

print ("=========(^xor)=========")
print("hasil akan true, jika salah satu true dan lainnya false")
a = False
b = False
hasil = a ^ b 
print(a, "^xor", b, "=", hasil)
a = False
b = True
hasil = a ^ b 
print(a, "^xor", b, "=", hasil)
a = True
b = False
hasil = a ^ b 
print(a, "^xor", b, "=", hasil)
a = True
b = True
hasil = a ^ b 
print(a, "^xor", b, "=", hasil)
