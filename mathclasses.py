from math import sqrt

specials = {
    "0": "⁰",
    "1": "¹",
    "2": "²",
    "3": "³",
    "4": "⁴",
    "5": "⁵",
    "6": "⁶",
    "7": "⁷",
    "8": "⁸",
    "9": "⁹",
    "root": "√"
}

class PythagoreanTheorem:
    def findc(a,b):
        step1 = f"{str(a) + specials['2']} + {str(b) + specials['2']} = c{specials['2']}"
        step2 = f"{str(a*a)} + {str(b*b)} = c{specials['2']}"
        step3 = f"{specials['root']}{str((a*a)+(b*b))} = {specials['root']}c{specials['2']}"
        step4 = f"{str(sqrt((a*a)+(b*b)))} = c"
        return f"{step1}\n{step2}\n{step3}\n{step4}"

    def findleg(a,c):
        step1 = f"{str(a) + specials['2']} + b{specials['2']} = {str(c) + specials['2']}"
        step2 = f"{str(a*a)} + b{specials['2']} = {str(c*c)}"
        step3 = f"-{str(a*a)}       -{str(a*a)}"
        step4 = f"{specials['root']}b{specials['2']} = {specials['root']+str((c*c)-(a*a))}"
        step5 = f"b = {str(sqrt((c*c)-(a*a)))}"
        return f"{step1}\n{step2}\n{step3}\n{step4}\n{step5}"