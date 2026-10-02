import math
import matplotlib.pyplot as plt


class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfants = []

    # 添加子节点
    def ajouter_enfant(self, enfant):
        self.enfants.append(enfant)

    # 用波兰表示法显示表达式
    def afficher(self):
        print(self.valeur, end=" ")

        for enfant in self.enfants:
            enfant.afficher()

    # 计算表达式
    def evaluer(self, variables):
        # 1. 如果是数字，直接返回
        if isinstance(self.valeur, (int, float)):
            return self.valeur

        # 2. 如果是变量，例如 x、y
        if self.valeur in variables:
            return variables[self.valeur]

        # 3. 二元运算符
        if self.valeur == "+":
            return (
                self.enfants[0].evaluer(variables)
                + self.enfants[1].evaluer(variables)
            )

        if self.valeur == "-":
            return (
                self.enfants[0].evaluer(variables)
                - self.enfants[1].evaluer(variables)
            )

        if self.valeur == "*":
            return (
                self.enfants[0].evaluer(variables)
                * self.enfants[1].evaluer(variables)
            )

        if self.valeur == "/":
            return (
                self.enfants[0].evaluer(variables)
                / self.enfants[1].evaluer(variables)
            )

        # 4. 一元运算符
        if self.valeur == "exp":
            return math.exp(
                self.enfants[0].evaluer(variables)
            )

        if self.valeur == "log":
            return math.log(
                self.enfants[0].evaluer(variables)
            )

        if self.valeur == "sin":
            return math.sin(
                self.enfants[0].evaluer(variables)
            )

        if self.valeur == "cos":
            return math.cos(
                self.enfants[0].evaluer(variables)
            )

        # 5. 如果走到这里，说明是一个没有给值的变量
        raise ValueError(
            "Variable inconnue : " + str(self.valeur)
        )

    # 绘制函数
    def tracer(self, variable, valeurs):
        resultats = []

        for valeur in valeurs:
            resultat = self.evaluer({variable: valeur})
            resultats.append(resultat)

        plt.plot(valeurs, resultats)
        plt.xlabel(variable)
        plt.ylabel("Valeur de l'expression")
        plt.grid()
        plt.show()