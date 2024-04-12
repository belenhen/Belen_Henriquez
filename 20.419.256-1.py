vlansw1=[10,20,30]
vlansw2=[40,50,60]
vlanENR=[10,100,30]

if native1 == 99:
    print ("la vilan nativa de sw1 es correcta y cumple con el requerimiento")
else:
    print("la vlan nativa de sw1 no es correcta y no cumple con los requerimientos")

if vlansw1== vlanENR:
    print("las vlans de sw1 son igulaes y cumplen con el requerimiento")
else:
    print("las vlans de sw1 no son iguales y no cumplen con el requerimiento")

 if native1 == 200:
    print("las vlans de sw2 no es correcta y no cumplen con el requerimiento")

if vlansw2== (40,50,60):
    print("las vlans de sw1 son igulaes y cumplen con el requerimiento")
else:
    print("las vlans de sw2 no son iguales y no cumplen con el requerimiento")