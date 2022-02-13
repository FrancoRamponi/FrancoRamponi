'''
Juego - Sudoku
TPO - Programacion 1
Grupo 9
'''
import random


copiarTabla = lambda tabla :  [[tabla[f][c] for c in range(9)]for f in range(9)]

def inicio():
    while True:
        try:
            print("\033[3;35m"+"BIENVENIDO A SUDOKU\n"+'\033[0;m')
            print('\033[0;m'+"\033[2;36m"+"1. Para iniciar el juego.\n"+'\033[0;m'+ "\033[6;31m"+"2. Para ver la tabla de puntuaciones.\n"+'\033[0;m'+"\033[6;33m"+"3. Para salir."+'\033[0;m')
            opcion_menu = int(input("\033[1;36m"+"SELECCIONE UNA OPCIÓN: "+ '\033[0,m'))
            assert 1 <= opcion_menu <= 3
            if opcion_menu == 1:
                comenzarJuego(tabla_sudoku)
            if opcion_menu == 2:
                tabla_puntuaciones()
            if opcion_menu == 3:
                print("\nMUCHAS GRACIAS POR PARTICIPAR!")
            break
        except ValueError:
            print("Solo se permiten un números enteros.\n")
        except AssertionError:
            print("Debe ingresar una de las opciones válidas.\n")

def tablaFull(tabla_):
    '''Verificamos si la tabla para el Sudoku esta completa'''
    for fila in range(0,9):
        for columna in range(0,9):
            if tabla_[fila][columna] == 0:
                return False
    return True

def sudokuCompletado(tabla_,copia):
    '''
    Funcion para verificar si el sudoku esta solucionado.
    '''
    for fila in range(0,9):
        for columna in range(0,9):
            if not (copia[fila][columna] == tabla_[fila][columna]):
                return False
    return True

def imprimirSudoku(tabla_,fijas):
    '''Funcion para mostrar por pantalla la tabla'''
    l1 = ['','1','2','3','','4','5','6','','7','8','9']
    l2 = ['A  ','B  ','C  ','D  ','E  ','F  ','G  ','H  ','I  ']
    print ('\n\033[1m''\033[95m' ,*l1,'\033[0m''\033[0m\n',sep='  ')
    filas = len(tabla_)
    columnas = len(tabla_[0])
    for x in range (filas):
        print('\033[95m''\033[1m'+ l2[x] +'\033[0m''\033[0m',end='')
        for y in range (columnas):
            if (y == 3 or y== 6):
                print("|", end=" ")
            if fijas[x][y]==0:
                print('\033[94m'"%2d" %tabla_[x][y],'\033[0m',end='')
            else: 
                print ("%2d" %tabla_[x][y], end=" ")
            if ((x == 2) and y == 8):
                print()
                for a in range(filas):
                    print("- -", end=" ")
            if ((x == 5) and y == 8):
                print()
                for a in range(filas):
                    print("- -", end=" ")
        print()
    print()
                 
def generarSudoku(tabla_):
    numeros = [1,2,3,4,5,6,7,8,9]
    for i in range(0,81):
        fila = i//9
        columna = i%9
        if tabla_[fila][columna] == 0:
            random.shuffle(numeros)
            for numero in numeros:
                if not(numero in tabla_[fila]): 
                    if not numero in  (tabla_[0][columna],tabla_[1][columna],tabla_[2][columna],tabla_[3][columna],tabla_[4][columna],tabla_[5][columna],tabla_[6][columna],tabla_[7][columna],tabla_[8][columna]):
                        recuadro = []
                        if fila < 3:
                            if columna < 3:
                                recuadro = [tabla_[i][0:3] for i in range(0,3)]
                            elif columna < 6:
                                recuadro = [tabla_[i][3:6] for i in range(0,3)]
                            else:
                                recuadro = [tabla_[i][6:9] for i in range(0,3)]
                        elif fila < 6:
                            if columna < 3:
                                recuadro = [tabla_[i][0:3] for i in range(3,6)]
                            elif columna < 6:
                                recuadro = [tabla_[i][3:6] for i in range(3,6)]
                            else:
                                recuadro = [tabla_[i][6:9] for i in range(3,6)]
                        else:
                            if columna < 3:
                                recuadro = [tabla_[i][0:3] for i in range(6,9)]
                            elif columna < 6:
                                recuadro = [tabla_[i][3:6] for i in range(6,9)]
                            else:
                                recuadro = [tabla_[i][6:9] for i in range(6,9)]
                        if not numero in (recuadro[0] + recuadro[1] + recuadro[2]):
                            tabla_[fila][columna] = numero
                            if tablaFull(tabla_):
                                return True
                            else:
                                if generarSudoku(tabla_):
                                    return True
            break
    tabla_[fila][columna] = 0

def establecerNivel(tabla_, dificultad):
    '''
    1 = Facil 25 (Se retiran 25 valores, dejando 56 pistas.)
    2 = Intermedio 35 (Se retiran 35 valores, dejando 45 pistas.) 
    3 = Dificil 55 (Se retiran 55 valores, dejando 26 pistas.)
    '''
    valoresEscondidos = 0
    if dificultad == 1:
        valoresEscondidos = 2
    elif dificultad == 2:
        valoresEscondidos = 40
    else: valoresEscondidos = 55
    while valoresEscondidos > 0:
        fila = random.randint(0,8)
        columna = random.randint(0,8)
        while tabla_[fila][columna] == 0:
            fila = random.randint(0,8)
            columna = random.randint(0,8)
        tabla_[fila][columna] = 0
        valoresEscondidos -= 1

def comenzarJuego(tabla_):
    puntaje = 0
    l1 = ['1','2','3','4','5','6','7','8','9']
    l2 = ['A','B','C','D','E','F','G','H','I','RENDIRSE']
    generarSudoku(tabla_)
    jugador = input("\033[1;34m" + '\nNombre: ' +'\033[0;m')
    print('\nNiveles de Dificultad: ')
    print("\033[1;32m" + " 1. Facilito\n" +'\033[0;m' + "\033[1;33m" + " 2. Semiprofesional\n" +'\033[0;m' + "\033[1;31m" + " 3. Frustrante\n" +'\033[0;m') 
    while True:
        try:
            nivel = int(input("Seleccione el nivel de dificultad para jugar: "))
            assert 1 <= nivel <= 3
            break
        except (ValueError, AssertionError):
            print("Debe ingresar un nivel válido, eliga entre 1, 2 y 3.")
    copiaSudoku = copiarTabla(tabla_)
    establecerNivel(copiaSudoku,nivel)
    fijas = copiarTabla(copiaSudoku)
    while sudokuCompletado(tabla_,copiaSudoku) == False:
        print(f'JUGADOR: {jugador}   NIVEL: {nivel}   INTENTOS: {puntaje}')
        imprimirSudoku(copiaSudoku,fijas)
        while True:
            try:
                print("Para desistir escriba en la fila: \033[1;31m" + 'rendirse' +'\033[0;m')
                coordJugador_fila = input("\033[1;30m" + "Ingrese la fila (Ej: A): " +'\033[0;m').upper()
                assert coordJugador_fila.isalpha(), "Solo se permiten letras."
                assert coordJugador_fila in l2, "Debe ingresar una fila válida, entre A e I."
                break
            except AssertionError as mensaje:
                print(mensaje)
        if coordJugador_fila == "RENDIRSE":
            print(f"TE RENDISTE {jugador.upper()}, HAS SIDO VENCIDO POR EL SUDOKU.")
            exit()
        while True:
            try:
                coordJugador_columna = int(input("\033[1;30m" + "Ingrese la columna (Ej: 1): " +'\033[0;m'))
                assert 1 <= coordJugador_columna <= 9 
                break
            except ValueError:
                print("Solo se permiten un números enteros.")
            except AssertionError:
                print("Debe ingresar una columna válida, entre 1 y 9.")
        while True:
            try:
                coordJugador_valor = int(input("\033[1;30m" + "Ingrese el valor (Ej: 7): " +'\033[0;m'))                
                assert 1 <= coordJugador_valor <= 9
                break
            except ValueError:
                print("Solo se permiten un números enteros.")
            except AssertionError:
                print("Debe ingresar un valor válido, entre 1 y 9.")
        x = l2.index(coordJugador_fila)
        y = l1.index(str(coordJugador_columna))
        if fijas[x][y] == 0:
            copiaSudoku[x][y] = coordJugador_valor
            puntaje += 1
            sudokuCompletado(tabla_,copiaSudoku)
        else:
            print("Esa es una casilla fija, no puede modificarla.")
    print(f'¡FELICIDADES! Lo lograste {jugador} en {puntaje} intentos.')
    registroJugador(jugador,nivel,puntaje)
    tabla_puntuaciones()

def registroJugador(jugador,nivel,puntaje):
    try:
        archivoJugadores = open("archivoJugadores.txt","at")
        archivoJugadores.write(jugador+';'+str(nivel)+';'+str(puntaje)+'\n')
    except FileNotFoundError:
        print('No se encontro el archivo')
    except OSError as mensaje:
        print('Error al grabar')
        print(mensaje)
    finally:
        try:
            archivoJugadores.close()
        except NameError:
            pass

def tabla_puntuaciones():
    t_facil = []
    t_medio = []
    t_dificil = []
    try:
        archivoJugadores = open("archivoJugadores.txt","r")
        linea = archivoJugadores.readline()
        while linea:
            nombreJ,nivelJ,puntajeJ = linea.split(';')
            puntajeJ = puntajeJ.rstrip('\n')
            nivelJ = int(nivelJ)
            puntajeJ = int(puntajeJ)
            if nivelJ == 1 :
                t_facil.append((nombreJ,puntajeJ,))
            if nivelJ == 2:
                t_medio.append((nombreJ,puntajeJ,))
            if nivelJ == 3:
                t_dificil.append((nombreJ,puntajeJ))
            linea = archivoJugadores.readline()
    except FileNotFoundError:
        print('No se encontro el archivo')
    except OSError as mensaje:
        print(mensaje)
    finally:
        try:
            archivoJugadores.close()
        except NameError:
            pass
    imprimirTablaPuntuaciones(t_facil,t_medio,t_dificil)

def imprimirTablaPuntuaciones(t_facil,t_medio,t_dificil):
    print(f'\n{"CUADRO DEL HONOR":^32}\n')
    print("\033[1;32m" + f'{"NIVEL FACILITO":^32}' +'\033[0;m')
    print("\033[1;30m" + f'{"JUGADOR":<24} {"PUNTOS":>3}' +'\033[0;m') 
    print('-'*31)
    t_facil.sort(key = lambda x: x[1])
    if len(t_facil) > 5:
        for x in range(0,5):
            print(f'{t_facil[x][0]:<25} {t_facil[x][1]:>3}')
    if len(t_facil) == 0:
        print(f'{"SIN RETADORES...POR AHORA.":^31}')
    else:
        if len(t_facil) <= 5:
            for nombre, puntaje in t_facil:
                print(f'{nombre:<25} {puntaje:>3}')
    print('-'*31)
    print("\033[1;33m" + f'\n{"NIVEL SEMIPROFESIONAL":^32}' +'\033[0;m')
    print("\033[1;30m" + f'{"JUGADOR":<24} {"PUNTOS":>3}' +'\033[0;m')
    print('-'*31)
    t_medio.sort(key = lambda x: x[1])
    if len(t_medio) > 5:
        for x in range(0,5):
            print(f'{t_medio[x][0]:<25} {t_medio[x][1]:>3}')
    if len(t_medio) == 0:
        print(f'{"SIN RETADORES...POR AHORA.":^31}')
    else:
        if len(t_medio) <= 5:
            for nombre, puntaje in t_medio:
                print(f'{nombre:<25} {puntaje:>3}')
    print('-'*31)
    print("\033[1;31m" + f'\n{"NIVEL FRUSTRANTE":^32}' +'\033[0;m')   
    print("\033[1;30m" + f'{"JUGADOR":<24} {"PUNTOS":>3}' +'\033[0;m')
    print('-'*31)
    t_dificil.sort(key = lambda x: x[1])
    if len(t_dificil) > 5:
        for x in range(0,5):
            print(f'{t_dificil[x][0]:<25} {t_dificil[x][1]:>3}')
    if len(t_dificil) == 0:
        print(f'{"SIN RETADORES...POR AHORA.":^31}')
    else:
        if len(t_dificil) <= 5:
            for nombre, puntaje in t_dificil:
                print(f'{nombre:<25} {puntaje:>3}')
    print('-'*31)
    while True:
        try:
            opcion = input("\033[1;35m" + '\n¿Regresar al Menu Principal? S/N: ' +'\033[0;m')
            opcion = opcion.upper()
            assert opcion.isalpha(), "Solo se permiten letras."
            assert opcion == "S" or opcion == "N", "Debe ingresar una respuesta válida."
            break
        except AssertionError as mensaje:
            print(mensaje)
    if opcion == "S":
        inicio()
    else:
        print("\033[1;34m" + "Vuelva pronto!!" +'\033[0;m')
        
#Programa_Principal
tabla_sudoku = [[0 for f in range(9)]for c in range(9)]  
inicio()