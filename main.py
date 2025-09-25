def dar_vuelta_texto(texto):
        if texto == "":
                return ""
        else:
            salida = texto[-1]
            for i in range(1, len(texto)):
                    salida = salida + (texto[-i-1])
            return salida

if __name__ == "__main__":
        dar_vuelta_texto(input("Introduce texto para darle la vuelta: "))