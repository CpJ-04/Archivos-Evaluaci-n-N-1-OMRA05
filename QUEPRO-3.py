ACL = int(input("Ingrese el numero de ACL: "))

if ACL >= 1 and ACL <= 99:
    print(F"El numero ({ACL}) corresponde a una ACL Estandar")
elif ACL >= 100 and ACL <= 199:
    print(F"El numero ({ACL}) corresponde a una ACL Extendida")
else:
    print(F"El numero ({ACL}) no corresponde a una ACL")