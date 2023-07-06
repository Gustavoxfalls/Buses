def llenar(arreglo):
    x = 1
    for f in range(8):
        for c in range(4):
            if len(str(x)) == 1:
                arreglo[f][c]= '0'+str(x)
            else:
                arreglo[f][c] = str(x)
            x = x + 1
def mostrar(arreglo):
    for f in range(8):
        fila = ''
        for c in range(4):
            fila = fila + ' | ' + arreglo[f][c]
        print(fila)

def marcarAsiento(arreglo, num_asiento):
    x = 1
    for f in range(8):
        for c in range(4):
            if x == num_asiento:
                arreglo[f][c]='XX'
            x = x +1

def verificarAsiento(arreglo,num_asiento):
    x = 1
    for f in range(8):
        for c in range(4):
            if x == num_asiento:
                if arreglo[f][c] == 'XX':
                    return  False
            x = x + 1
    return True

def salir():
    print("juanito simio ltda.")
    return False
