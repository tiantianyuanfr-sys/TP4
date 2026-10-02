from noeud import Noeud


# 创建节点
exp = Noeud("exp")
plus = Noeud("+")
deux = Noeud(2)
y = Noeud("y")


# 构造 2 + y
plus.ajouter_enfant(deux)
plus.ajouter_enfant(y)


# 构造 exp(2 + y)
exp.ajouter_enfant(plus)


# 显示波兰表示法
print("Expression en notation polonaise :")
exp.afficher()

print()


# 计算 y = 1 时的结果
resultat = exp.evaluer({"y": 1})

print("Pour y = 1 :")
print(resultat)


# 绘制函数
valeurs_y = [-2, -1, 0, 1, 2]

exp.tracer("y", valeurs_y)