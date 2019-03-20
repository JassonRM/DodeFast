class Instructor:
    def __init__(self):
        self.parseado = ""
    def parsear_intruccion(self,tupla):
        if(tupla[2] == "AF"):
            self.parseado = self.parseado + "AF" + "\n"
        if (tupla[2] == "F"):
            self.parseado = self.parseado + "F" + "\n"
        if (tupla[2] == "DFA"):
            self.parseado = self.parseado + "DFA" + "\n"
        if (tupla[2] == "IFA"):
            self.parseado = self.parseado + "IFA" + "\n"
        if (tupla[2] == "DFB"):
            self.parseado = self.parseado + "DFB" + "\n"
        if (tupla[2] == "IFB"):
            self.parseado = self.parseado + "IFB" + "\n"
        if (tupla[2] == "A"):
            self.parseado = self.parseado + "A" + "\n"
        if (tupla[2] == "DAA"):
            self.parseado = self.parseado + "DAA" + "\n"
        if (tupla[2] == "IAA"):
            self.parseado = self.parseado + "IAA" + "\n"
        if (tupla[2] == "DAB"):
            self.parseado = self.parseado + "DAB" + "\n"
        if (tupla[2] == "IAB"):
            self.parseado = self.parseado + "IAB" + "\n"
        if (tupla[2] == "AA"):
            self.parseado = self.parseado + "AA" + "\n"
        if (tupla[2] == ")"):
            self.parseado = self.parseado + "AL" + "\n"
    def obtener_string(self):
        return self.parseado
