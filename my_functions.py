def division(a, b):
    """Ésta función regresa una tupla con el cociente
    y el residuo de la división de dos números enteros dados
    Los valores de entrada (a,b) son el dividendo y divisor respectivamente,
    las salidas q y r son el cociente y el residuo respectivamente
    Ejemplo: division(7,7) = (1,0) q=1, r=0"""   
    # Se inicializa el residuo en cero
    r = 0
    # Se inicializa el cociente en cero
    q = 0
    # Evalúa si el cociente q es menor o igual al dividendo "a". El algoritmo de la 
    # división se detiene cuando es mayor el cociente que el dividendo.
    while q <= a:
        # En este caso el residuo será cero
        r = 0
        # Evalúa mientras el residuo sea menor que el divisor, en este caso la división es válida
        while r < b:
            # Evalua si el divisor es igual al dividendo multiplicado por el cociente más residuo
            if a == b*q + r: 
              # Regresa el cociente y residuo acumulados
                return(q, r)
            # Acumula en uno el residuo si no no es menor al divisor            
            r = r + 1
        # Acumula en 1 el cociente si no es menor que el dividendo    
        q = q + 1
def is_prime(p):
    """Ésta función devuelve un valor lógico True o False
    al evaluar si un número es primo o no"""
    # Por default selecciona el valor de True, ya que 2 es primo
    prime = True 
    # Inicializa en 2, ya que desde aquí debe comenzarse la búsqueda
    i = 2
    """ ciclo que ejecuta las instrucciones mientras el valor a iterar "i" sea menor
        que el valor del número p, para que evalúe 2,3,4,5,...p """
    while i < p: 
        # Regresa el residuo de la división entre p e i (primer elemento)
        residuo = division(p, i)[1]
        if residuo == 0: 
          # Rompe el ciclo cuando se da un residuo exacto, ya que el número 
          # será divisible por otro número que no sea 1
            prime = False
            break
        else: 
            i = i + 1 # Incrementa el valor de "i" si p no es divisible entre i
    return prime
def primes(n): 
    """Ésta función devuelve una lista con los números 
    primos en el intervalo [2,n]
    Ejemplo: primes(9) = [2,3,5,7]"""    
    primos = [] #Inicializa la lista
    # Ejecuta un ciclo que va desde 2,3,4,5,... n+1
    for i in range(2, n + 1):
        # Evalua con la función anterior si el valor "i" es primo
        if is_prime(i) == True:
          # En caso que sí sea primo el valor de "i" lo guarda en la lista "primos"
            primos.append(i)
     # devuelve la lista de primos encontrados       
    return primos 