#Em um banho de 5 minutos, fechando o registro ao se ensaboar, são gastos 45 litros de água. Sabendo que em 1 m3 de água há 1.000 litros, calcule quantos banhos de 5 minutos são necessários para consumir 1 metro cúbico de água?
#DaniloNCSouza
#05/03/2020

tempo_banho = int(input("Quantos minutos você utilizou para tomar banho: "))
litro_min = 9
consumo = tempo_banho * litro_min
banho = 1000 / consumo
print (" o número de banho com o tempo de %d minutos, permite 1m3 %.f banhos" % (tempo_banho, banho))

