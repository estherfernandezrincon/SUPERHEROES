from datetime import date
from datetime import datetime

   
dictNombre={"A":"Sobaco","B":"Asesino","C":"Capitan"," D":" Pezon", "E":"Trueno","F":"Lobo","G":"Conejo","H":"Halcon", "I":"Sargento","J":"Prepucio","K":"El Milagro","L":"El Rey", "M":"Maestro","N":"Robot","Ñ":"Capitan","O":"Vigilanate","P":"Avispa","Q":"Doctor", "R":"Orificio","S":"Pepino", "T":"Principe","U":"Tiburon","V":"Aguijon","W":"Fantasma","X":"Agente"," Y":"tornado"," Z":"Brujo"}
dictApellido={"A":"Elastico","B":"Carmesi","C":"Radioactivo", "D":" Volador", "E":"Espacial","F":"Letal","G":"Flacido","H":"Marciano", "I":"Venenoso","J":"Invisible","K":"Mutante","L":"Vengador", "M":"Amoroso","N":"Apestoso","Ñ":"Amoroso","O":"Magico","P":"Gigante","Q":"Nazi", "R":"Bionico","S":"Celestial", "T":"Sangriento","U":"Rocoso","V":"De Hierro","W":"Psiquico","X":"Maravilla", "Y":"Hipster", "Z":"Invencible"}
dictTraje={"1": "Dorado","2":"Amarillo","3":"Oscuro","4":"Verde","5":"Blanco","6":"Azul","7":"Gris","8":"Plateado","9":"Rojo","0":"Escarlata"}
dictMesNac={"1":"Convertir todo en algondon","2":"Velocidad de la luz","3":"Hablar con Animales","4":"Super fuerza","5":"Control mental","6":"Invisibilidad","7":"Control del Fuego","8":"Crear Tormentas","9":"Converitr agu en cerveza","10":"Destruir planetas","11":"Saltar 20 metros","12":"Volar"}
dictDia={"1":"Baston","2":"Espada","3":"Hacha","4":"Sombrilla","5":"Escudo","6":"Barita Magica","7":"Rifle","8":"cuchillo","9":"Bat de Baseball","10":"Cuerda","11":"Araco y flecha","12":"Guantes de Box","13":"Sarten","14":"Pistola","15":"Manopla","16":"Chacos de Ninja","17":"Martillo","18":"Motosierra","19":"Cadenas","20":"Destornillador","21":"Escoba","22":"Dagas","23":"Boomerangs","24":"Estrellas Ninja","25":"Extintor","26":"Tijeras","27":"Destapacaños","28":"Lanza misiles","29":"Bastos de Hokey","30":"Cepillo de dientes","31":"Espada Magica"}


simbolos = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz"
validaÑ_apellido= dictApellido.get("C")[0]
validaÑ_nombre= dictNombre.get("C")[0]


now=datetime.now()

def validarSimbolos(letra):  
    if letra not in simbolos:
        return False
    return True

def validaMayuscula(letra):
    if letra != letra.upper():
        return False
    return True

def validaFecha():
    if str(Fecha) > str(now):
        return False
    return True


    

nombre=input("introduce tu nombre:   ")
letraNombre = nombre[0]

while not validarSimbolos(letraNombre) or not validaMayuscula(letraNombre):
    print("no escribas numeros ni simbolos, escribe la 1º letra en mayuscula")
    nombre=input("introduce tu nombre:   ")
    letraNombre = nombre[0]

apellido=input("introduce tu apellido:   ")
letraApellido = apellido[0]

while not validarSimbolos(letraApellido) or not validaMayuscula(letraApellido):
    print("no escribas numeros ni simbolos, escribe la 1º letra en mayuscula")
    apellido=input("introduce tu apellido:   ")
    letraApellido = apellido[0]


Fecha=input("introduce tu fecha de nacimiento (dd/mm/aaaa):   ")
numeroAgnoNac=Fecha[3]
Mes=Fecha[6]
Dia=Fecha[9]

while not validaFecha():
    print("introduce fecha correcta, no has nacido aun")
    Fecha=input("introduce tu fecha de nacimiento (aaaa/mm/dd):   ")
    

if numeroAgnoNac in dictTraje:   
    numeroAgnoNac=Fecha[3]
    
if Mes in dictMesNac:
    Mes=Fecha[6]
    
if Dia in dictDia:
    Dia=Fecha[9]

print("Soy {}, el superheroe".format(nombre) ,dictNombre[letraNombre],
      dictApellido[letraApellido],dictTraje[numeroAgnoNac],"mi poder es ",
      dictMesNac[Mes],"y voy a luchar contra la injusticia con mi" ,dictDia[Dia])
