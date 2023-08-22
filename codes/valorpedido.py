valorPedido = int(input())

congrat = ["Parabens, ", "Que pena, ", "none",]
venceu = ["você ganhou ", "você nao ganhou ", "none",]
premio = ["uma sobremesa gratis!", "nenhum brinde especial.", "none",]


if valorPedido >= 50:
    msg1 = congrat[0]
    msg2 = venceu[0]
    msg3 = premio[0]
else:
    msg1 = congrat[1]
    msg2 = venceu[1]
    msg3 = premio[1]
    
print(f"{msg1}{msg2}{msg3}")
