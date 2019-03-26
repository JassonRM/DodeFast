class Instructor:
    def __init__(self):
        self.parseado = []
    def parsear_intruccion(self,tupla):
        if(tupla[2] == "AF"):
            print("ENTRE AQUI")
            self.parseado.append("AF")
        if (tupla[2] == "F"):
            self.parseado.append("F")
        if (tupla[2] == "DFA"):
            self.parseado.append("DFA")
        if (tupla[2] == "IFA"):
            self.parseado.append("IFA")
        if (tupla[2] == "DFB"):
            self.parseado.append("DFB")
        if (tupla[2] == "IFB"):
            self.parseado.append("IFB")
        if (tupla[2] == "A"):
            self.parseado.append("A")
        if (tupla[2] == "DAA"):
            self.parseado.append("DAA")
        if (tupla[2] == "IAA"):
            self.parseado.append("IAA")
        if (tupla[2] == "DAB"):
            self.parseado.append("DAB")
        if (tupla[2] == "IAB"):
            self.parseado.append("IAB")
        if (tupla[2] == "AA"):
            self.parseado.append("AA")
        if (tupla[2] == ")"):
            self.parseado.append("AL")
    def obtener_string(self):
        return self.parseado
