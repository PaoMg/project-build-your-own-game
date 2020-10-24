import random
import json

nombre = input("Bienvenido a Adivina quién de Harry Potter! Cómo te llamas?")

def game():
    with open('./data.json') as f:
        diccionario_personajes = json.load(f)

    # Filtrando keys
    personajes = [name for name in diccionario_personajes]
    all_casas = list(dict.fromkeys([diccionario_personajes[i]['casa'] for i in personajes]))
    all_patronus = list(dict.fromkeys([diccionario_personajes[i]['patronus'] for i in personajes]))
    all_generos = list(dict.fromkeys([diccionario_personajes[i]['genero'] for i in personajes]))

    # Selección de personaje aleatorio
    secreto = random.choice(list(diccionario_personajes.keys()))

    # Funciones a evaluar
    def adivinar_per(personajes, secreto):
        print('\nOpciones:', menos_errados)
        ans = False
        while ans == False:
            guess = input()
            if guess.lower() in [menos_errados.lower() for menos_errados in menos_errados]:
                if guess.lower() == secreto.lower():
                    print("Felcidades! Ganaste el juego :)")
                    while True:
                        juego = input("Quieres jugar de nuevo y/n?")
                        try:
                            if juego.lower() == 'y':
                                game()
                            elif juego.lower() == 'n':
                                print("Gracias por jugar")
                                exit()
                            else:
                                raise ValueError
                        except ValueError:
                            print("Por favor ingresa y/n")
                else:
                    print('\nPersonaje incorrecto')
                    [pers_err.append(guess.capitalize())]
                    return posibles
                    ans = True
            else:
                print("Por favor selecciona un personaje correcto")

    def adivinar_casa(personajes, casa):
        print('\nOpciones:', casas_erradas)
        ans = False
        while ans == False:
            guess = input()
            if guess.lower() in [casas_erradas.lower() for casas_erradas in casas_erradas]:
                if guess.lower() == casa.lower():
                    print('\nCasa correcta')
                    personajes = [pers for pers in personajes if diccionario_personajes[pers]['casa'] == casa]
                    [correctas.append(3)]
                    return personajes
                    ans = True
                else:
                    print('\nCasa erronea')
                    [cas_err.append(guess.lower())]
                    return posibles
                    ans = True
            else:
                print("Por favor selecciona una casa correcta")

    def adivinar_patronus(personajes, patronus):
        print('\nOpciones:', patronus_errados)
        ans = False
        while ans == False:
            guess = input()
            if guess.lower() in [patronus_errados.lower() for patronus_errados in patronus_errados]:
                if guess.lower() == patronus.lower():
                    print('\nPatronus correcto')
                    personajes = ([pers for pers in personajes if diccionario_personajes[pers]['patronus'] == patronus])
                    [correctas.append(4)]
                    return personajes
                    ans = True
                else:
                    print('\nPatronus incorrecto')
                    [patr_err.append(guess.lower())]
                    return posibles
                    ans = True
            else:
                print("Por favor selecciona un patronus correcto")


    def adivinar_genero(personajes, genero):
        print('\nOpciones:', generos_errados)
        ans = False
        while ans == False:
            guess = input()
            if guess.lower() in [generos_errados.lower() for generos_errados in generos_errados]:
                if guess.lower() == genero.lower():
                    print('\nGénero correcto')
                    personajes = [pers for pers in personajes if diccionario_personajes[pers]['genero'] == genero]
                    [correctas.append(2)]
                    return personajes
                    ans = True
                else:
                    print('\nGénero incorrecto')
                    [gen_err.append(guess.lower())]
                    return posibles
                    ans = True
            else:
                print("Por favor selecciona un género correcto")


    def unir_listas(lista_a, lista_b):
        descartados = [i for i in lista_a if i not in lista_b]
        [blacklist.append(i) for i in descartados]
        return posibles


    # Iniciar el juego
    tries = 0
    posibles = personajes[:]
    blacklist = []
    preguntas = 4
    correctas = []
    pers_err = []
    cas_err = []
    patr_err = []
    gen_err = []

    while True:
       rondas = input(f"{nombre.capitalize()}, cuántas rondas quieres jugar?")
       try:
           rondas = int(rondas)
           if rondas > 20:
               print("Son demasiadas rondas... jueguemos solo 20")
               rondas = 20
       except ValueError:
           print ("Por favor ingresa un número correcto")
       else:
           break


    print('\nInicia el juego.')

    while tries < rondas:
        print(f"\nIntento: {tries+1}/{rondas}")
        set(blacklist)
        opciones = [i for i in [i + 1 for i in range(preguntas)] if i not in correctas]
        lista_posibles = [x for x in posibles if x not in blacklist]
        menos_errados = [i for i in lista_posibles if i not in pers_err]
        casas_erradas = [i for i in all_casas if i not in cas_err]
        patronus_errados = [i for i in all_patronus if i not in patr_err]
        generos_errados = [i for i in all_generos if i not in gen_err]

        print("\nPersonajes posibles: ", menos_errados)
        try:
            if tries == rondas - 1:
                print("\nÚltimo intento! Adivina el personaje")
                eleccion = 1
            else:
                print(f"Elige un número: ({', '.join(str(e) for e in opciones)})")
                print('1. Adivinar el personaje')
                if 2 not in correctas:
                    print('2. Adivinar su género')
                if 3 not in correctas:
                    print('3. Adivinar su casa')
                if 4 not in correctas:
                    print('4. Adivinar su patronus')
                eleccion = int(input())

            if eleccion == 1:
                adivinar_per(personajes, secreto)
            elif eleccion == 2 and 2 not in correctas:
                personajes_nuevos = adivinar_genero(posibles, diccionario_personajes[secreto]['genero'])
                personajes_nuevos = unir_listas(posibles, personajes_nuevos)
            elif eleccion == 3 and 3 not in correctas:
                personajes_nuevos = adivinar_casa(posibles, diccionario_personajes[secreto]['casa'])
                personajes_nuevos = unir_listas(posibles, personajes_nuevos)
            elif eleccion == 4 and 4 not in correctas:
                personajes_nuevos = adivinar_patronus(posibles, diccionario_personajes[secreto]['patronus'])
                personajes_nuevos = unir_listas(posibles, personajes_nuevos)
            elif eleccion in correctas:
                print("Ese valor ya lo elegiste antes")
                tries -= 1
            else:
                raise ValueError
            tries += 1
        except ValueError:
            print('Oops! Esa no fue una opción correcta. Intentémoslo de nuevo...')

    # Pierde el juego
    print(f"Lo siento, perdiste. El personaje secreto era {secreto}")

    while True:
        juego = input("Quieres jugar de nuevo y/n?")
        try:
            if juego.lower() == 'y':
                game()
            elif juego.lower() == 'n':
                print("Gracias por jugar")
                exit()
            else:
                raise ValueError
        except ValueError:
            print("Por favor ingresa y/n")


game()