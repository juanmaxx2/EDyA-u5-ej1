from hash import Hash
if __name__ == "__main__":
    tam = 10
    Hashing = Hash(tam)
   
    Hashing.insertar(2000)
    Hashing.insertar(328)
    Hashing.insertar(4788)
    Hashing.insertar(12386)
    Hashing.insertar(478129)
    Hashing.insertar(29328)
    Hashing.insertar(230)
    Hashing.insertar(41821)
    Hashing.insertar(12345)
    Hashing.insertar(422)
   
    print(Hashing.buscar(41821))