#posiciones
# 1 2 3
# 4 5 6
# 7 8 9



def print_tablero(tablero):
    print(' | '+ tablero[0] + ' | ' + tablero[1]+' | ' + tablero[2] +' | ')
    print(' | '+ tablero[3] + ' | ' + tablero[4]+' | ' + tablero[5] +' | ')
    print(' | '+ tablero[6] + ' | ' + tablero[7]+' | ' + tablero[8] +' | ')

tablero = [' ']*9
fin_juego = False 
turno_y = True
while not fin_juego:
    try:
     posicion = int(input('ingresa celda 1-9: '))
     if turno_y == True:
        tablero[posicion-1]= 'X'
        #posicion = int(input('ingresa celda 1-9 jugador x: '))
     else:
        tablero[posicion-1]= 'O'
        #posicion = int(input('ingresa celda 1-9 jugador y: '))
    except:
        print('solo puedes escribir numeros, intentalo de nuevo')
    print_tablero(tablero)
    if (tablero[0]== tablero[1]== tablero[2] and tablero[0] != ' ' or
        tablero[3]== tablero[4]== tablero[5] and tablero[3] != ' ' or
        tablero[6]== tablero[7]== tablero[8] and tablero[6] != ' ' or
        tablero[0]== tablero[3]== tablero[6] and tablero[0] != ' ' or
        tablero[1]== tablero[4]== tablero[7] and tablero[1] != ' ' or
        tablero[2]== tablero[5]== tablero[8] and tablero[2] != ' ' or
        tablero[0]== tablero[4]== tablero[8] and tablero[0] != ' ' or
        tablero[2]== tablero[4]== tablero[6] and tablero[2] != ' '):
          print('el ganador es: '+ 'x'if turno_y else 'el ganador es: '+'o')
          fin_juego= True
    if ' ' not in tablero:
        print("empate")
        fin_juego = True
    turno_y= not turno_y
    
    



