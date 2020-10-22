import random

#Definir persoanjes
diccionario_personajes = {
  'Harry': {'casa':'gryffindor', 'patronus':'ciervo', 'genero':'male'},
  'Hermione': {'casa': 'gryffindor', 'patronus': 'nutria', 'genero':'female'},
  'Ron': {'casa': 'gryffindor', 'patronus': 'perro', 'genero':'male'},
  'Dumbledore': {'casa': 'gryffindor', 'patronus': 'fenix', 'genero':'male'},
  'Luna': {'casa': 'ravenclaw', 'patronus': 'liebre', 'genero': 'female'},
  'Snape': {'casa': 'slytherin', 'patronus': 'cierva', 'genero': 'male'},
  'Tonks': {'casa': 'hufflepuff', 'patronus': 'lobo', 'genero': 'female'},
  'Lupin': {'casa': 'gryffindor', 'patronus': 'lobo', 'genero': 'male'},
  'Ginny': {'casa': 'gryffindor', 'patronus': 'caballo', 'genero':'female'},
  'Fred': {'casa': 'gryffindor', 'patronus': 'lobo', 'genero':'male'},
  'George': {'casa': 'gryffindor', 'patronus': 'raton', 'genero':'male'},
  'Neville': {'casa': 'gryffindor', 'patronus': 'perro', 'genero':'male'},
  'Minerva': {'casa': 'gryffindor', 'patronus': 'gato', 'genero':'female'},
  'Lavender': {'casa': 'gryffindor', 'patronus': 'delfin', 'genero':'female'},
  'Seamus': {'casa': 'gryffindor', 'patronus': 'dragon', 'genero':'male'},
  'Mandy': {'casa': 'ravenclaw', 'patronus': 'conejo', 'genero': 'female'},
  'Cho': {'casa': 'ravenclaw', 'patronus': 'tigre', 'genero': 'female'},
  'Penelope': {'casa': 'ravenclaw', 'patronus': 'buho', 'genero': 'female'},
  'Marcus': {'casa': 'ravenclaw', 'patronus': 'perro', 'genero': 'male'},
  'Terry': {'casa': 'ravenclaw', 'patronus': 'hipogrifo', 'genero': 'male'},
  'Eddie': {'casa': 'ravenclaw', 'patronus': 'pantera', 'genero': 'male'},
  'Bradley': {'casa': 'ravenclaw', 'patronus': 'oso', 'genero': 'male'},
  'Michael': {'casa': 'ravenclaw', 'patronus': 'aguila', 'genero': 'male'},
  'Eleanor': {'casa': 'hufflepuff', 'patronus': 'perro', 'genero': 'female'},
  'Cedri': {'casa': 'hufflepuff', 'patronus': 'huron', 'genero': 'male'},
  'Owen': {'casa': 'hufflepuff', 'patronus': 'dragon', 'genero': 'male'},
  'Susan': {'casa': 'hufflepuff', 'patronus': 'huron', 'genero': 'female'},
  'Kevin': {'casa': 'hufflepuff', 'patronus': 'tortuga', 'genero': 'male'},
  'Justin': {'casa': 'hufflepuff', 'patronus': 'perro', 'genero': 'male'},
  'Rose': {'casa': 'hufflepuff', 'patronus': 'ciervo', 'genero': 'female'},
  'Summerby': {'casa': 'hufflepuff', 'patronus': 'cierva', 'genero': 'female'},
  'Malfoy': {'casa': 'slytherin', 'patronus': 'buho', 'genero': 'male'},
  'Pansy': {'casa': 'slytherin', 'patronus': 'gato', 'genero': 'female'},
  'Adriana': {'casa': 'slytherin', 'patronus': 'caballo', 'genero': 'female'},
  'Blaise': {'casa': 'slytherin', 'patronus': 'ballena', 'genero': 'female'},
  'Astoria': {'casa': 'slytherin', 'patronus': 'tigre', 'genero': 'female'},
  'Voldemort': {'casa': 'slytherin', 'patronus': 'serpiente', 'genero': 'male'},
  'Umbdrige': {'casa': 'slytherin', 'patronus': 'gato', 'genero': 'female'},
  'Aurora': {'casa': 'slytherin', 'patronus': 'gato', 'genero': 'female'},
  'Peeves': {'casa': 'slytherin', 'patronus': 'conejo', 'genero': 'male'},
  'Fletcher': {'casa': 'slytherin', 'patronus': 'huron', 'genero': 'male'},
  }

#Filtrando atributos
personajes = [name for name in diccionario_personajes]
all_casas = list(dict.fromkeys([diccionario_personajes[i]['casa'] for i in personajes]))
all_patronus = list(dict.fromkeys([diccionario_personajes[i]['patronus'] for i in personajes]))
all_generos = list(dict.fromkeys([diccionario_personajes[i]['genero'] for i in personajes]))
personajes_1=[]

#Selección de personaje aleatorio
secreto = random.choice(list(diccionario_personajes.keys()))
print(f'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \nEl personaje secreto es: {secreto}\nSu casa es: {diccionario_personajes[secreto]["casa"]}\nSu genero es: {diccionario_personajes[secreto]["genero"]}\nSu patronus es: {diccionario_personajes[secreto]["patronus"]}\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \n')

#Funciones a evaluar
def adivinar_per(personajes,secreto):
  print('\nOpciones:',personajes)
  if input() == secreto:
    print('¡Felicidades, ganaste el juego!')
    exit()
  else:
    print('Personaje incorrecto')
    return posibles


def adivinar_casa(personajes,casa):
  print('\nOpciones:', all_casas)
  print('Elige la casa del personaje')
  if input() == casa:
    print('Casa correcta')
    personajes = [pers for pers in personajes if diccionario_personajes[pers]['casa'] == casa]
    return personajes
  else:
    print('Casa erronea')
    return posibles

def adivinar_patronus(personajes,patronus):
  print('\nOpciones:', all_patronus)
  print('Elige el patronus del personaje')
  if input() == patronus:
    print('Patronus correcto')
    personajes = ([pers for pers in personajes if diccionario_personajes[pers]['patronus'] == patronus])
    return personajes
  else:
    print('Patronus erroneo')
    return posibles

def adivinar_genero(personajes,genero):
  print('\nOpciones:', all_generos)
  print('Elige el género del personaje')
  if input() == genero:
    print('Genero correcto')
    personajes = [pers for pers in personajes if diccionario_personajes[pers]['genero'] == genero]
    return personajes
  else:
    print('Genero incorrecto')
    return posibles

def unir_listas(lista_a,lista_b):
    #print("lista a: ", lista_a)
    #print("lista b: ", lista_b)
    descartados = [i for i in lista_a if i not in lista_b]
    [blacklist.append(i) for i in descartados]
    return posibles

#Inicia el juego
win = False
tries = 0
posibles = personajes[:]
blacklist = []
print('Inicia el juego.')

while tries < 5 or win == False:
  print('\nIntentos:', tries)
  set(blacklist)
  print("Personajes posibles: ", [x for x in posibles if x not in blacklist])
  try:
    print('Elige un número (1,2,3 4)\n')
    print('1. Adivinar el personaje')
    print('2. Adivinar su género')
    print('3. Adivinar su casa')
    print('4. Adivinar su patronus')
    eleccion = int(input())
    if eleccion == 1:
        adivinar_per(personajes,secreto)
    elif eleccion == 2:
        personajes_nuevos = adivinar_genero(posibles,diccionario_personajes[secreto]['genero'])
        personajes_nuevos = unir_listas(posibles, personajes_nuevos)
    elif eleccion == 3:
        personajes_nuevos = adivinar_casa(posibles,diccionario_personajes[secreto]['casa'])
        personajes_nuevos = unir_listas(posibles, personajes_nuevos)
    elif eleccion == 4:
        personajes_nuevos = adivinar_patronus(posibles,diccionario_personajes[secreto]['patronus'])
        personajes_nuevos = unir_listas(posibles, personajes_nuevos)
    else:
        raise ValueError
    tries += 1
  except ValueError:
    print ('Oops!  Eso no fue una opción correcta.  Intentémoslo de nuevo...')

#Pierde el juego
print('Lo siento, perdiste :(')
print('Finaliza el juego')