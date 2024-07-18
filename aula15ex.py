import pandas as pd
import statistics
import matplotlib.pyplot as plt
import tkinter as tk

dados = pd.read_csv('aula15.csv')

nome = dados['Nome']
compra = dados['Compra']
regiao = dados['Região']
qntd = len(nome)
print(qntd)

media = statistics.mean(compra)
mediana = statistics.median(compra)
desvio = statistics.stdev(compra)

metricas = [media,mediana,desvio]
Tmetricas = ['média','mediana','desvio']


def pizza01():
    plt.pie(compra, labels =regiao,autopct='%.2f')
    plt.show()

def pizza02():
    plt.pie(metricas, labels =Tmetricas,autopct='%.2f')
    plt.show()

janela = tk.Tk()
janela.geometry('200x200')
janela.title('GRÁFICOS')
texto = tk.Label(janela, text = 'Escolha um tipo de gráfico')
texto.pack()

btn = tk.Button(janela,text = 'Métrica',command=pizza02)
btn.pack()

btn = tk.Button(janela,text = 'Regiões',command=pizza01)
btn.pack()

janela.mainloop()

#sul e sudeste são as regiões que mais foram compradas sendo com o maior fatoramento o sudeste então deve investir mais em propaganda nas outras regiões
