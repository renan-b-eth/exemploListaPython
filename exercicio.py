import tkinter as tk

#tupla é apenas python (, , , ,) - imutavel (dado não se altera)
#lista em python [, , , ,] - mutavel (dado se altera)
#set e dict

nome = []
i=0
while i < 10:
    nome.append(i)
    i+=1

nome[2]="teste"
nome.append("final") #adc um item no final da lista
nome.insert(2, "posicao3") #parametro posicao + o item, adc especificio.

nome2 = ['lista2','lista4','lista2']

nome.extend(nome2) #adiciona uma lista em outra
print(nome)
print(nome.index('lista2')) #pega o index da lista em numero
print(nome.count('lista2')) #pega a quantidade de repetições que aparece na lista
teste = ['oi', 'a']
#print(nome.sort()) #retorna o primeiro valor da lista // só funciona com numeros inteiros
print(teste.sort())
listateste = [0,1,2,3,4,5,6,7,8,9]
print(nome[0::2]) #retorna todos os numeros pares da lista essa tipo de lista se chama SLICE
print("AQUI",listateste[0::2])

root = tk.Tk()
root.geometry('700x500')
root.resizable(False, True)
root.title("Titulo teste")

label = tk.Label(root, text=nome, background="#021548", width=100, height=50, font=("Heveltica", 20))
label.pack()

#tamanhoLista = len(nome) #pega o tamanho da lista
#listaOrdenada = nome.sort() #ordenada uma lista

#label2 = tk.Label(root, text=tamanhoLista, width=100, height=50, font=("Heveltica", 20))
#label2.pack()

#label2 = tk.Label(root, text=listaOrdenada)
#label2.pack()

button = tk.Button(root, text="Button")
button.pack()

root.mainloop()




