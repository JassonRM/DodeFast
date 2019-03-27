class Instructor:
    def __init__(self):
        self.parseado = []
    def parsear_intruccion(self,tupla):
        if(tupla[2] == "AF"):
            print("ENTRE AQUI")
            self.parseado.append("AF")
            return False
        if (tupla[2] == "F"):
            self.parseado.append("F")
            return False
        if (tupla[2] == "DFA"):
            self.parseado.append("DFA")
            return False
        if (tupla[2] == "IFA"):
            self.parseado.append("IFA")
            return False
        if (tupla[2] == "DFB"):
            self.parseado.append("DFB")
            return False
        if (tupla[2] == "IFB"):
            self.parseado.append("IFB")
            return False
        if (tupla[2] == "A"):
            self.parseado.append("A")
            return False
        if (tupla[2] == "DAA"):
            self.parseado.append("DAA")
            return False
        if (tupla[2] == "IAA"):
            self.parseado.append("IAA")
            return False
        if (tupla[2] == "DAB"):
            self.parseado.append("DAB")
            return False
        if (tupla[2] == "IAB"):
            self.parseado.append("IAB")
            return False
        if (tupla[2] == "AA"):
            self.parseado.append("AA")
            return False
        if (tupla[2] == ")"):
            self.parseado.append("AL")
            return False
    def obtener_string(self):
        return self.parseado
