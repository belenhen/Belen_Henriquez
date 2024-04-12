aclnum= int(input("Ingrese nuemero de acl: "))

if aclnum >= 1 and aclnum <= 99:
    print("este es un ACL estandar")

elif aclnum >= 100 and aclnum <= 199:
    print("este es un ACL extendida")

else:
    print("el numero no corresponde a una lista de acceso")