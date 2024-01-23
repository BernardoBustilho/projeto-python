## Atividade Sistema Escolar

import random
dados_alunos = []

nome = str(input('Nome: '))

sobrenome = str(input('Sobrenome: '))

idade = int(input('Idade: '))
if(idade >= 16):
        resp = print('Pode entrar em uma universidade')
        enem=int(input('Qual a nota do enem?'))

else:
        resp = print('Você não tem idade para entrar na faculdade.')


if enem >500:
    print("Parabéns, você passou no Enem.")

elif enem == 500:
    print('Passou na média')   

else: 
    print("Nota insuficiente")

email = str(input('Email: '))
 
renda_familiar = float(input('Renda Familiar: '))
result = renda(renda_familiar)

def renda ():
    if(renda_familiar == 1.412):
        resp = print('Você tem direito a uma bolsa de até 35%')
        saida = ("Parabéns, bons estudos")

    elif(renda_familiar > 1.412):
        resp = print('Você tem direito a uma bolsa de até 15%')
        saida = ("Parabéns, bons estudos")

    elif(renda_familiar < 1.412):
        resp = print('Você tem direito a uma bolsa de até 50%')
        saida = ("Parabéns, bons estudos")
    
    elif(renda_familiar == 0):
        resp = print('Você tem direito a uma bolsa de até 100%')
        saida = ("Parabéns, bons estudos")
        return saida 



filiação = str(input('Filiação: '))


cpf = str(input('CPF: '))


escolaridade = str(input('Escolaridade: '))
if(escolaridade == "Ensino Médio Completo"):
       resp = print('Você pode se matricular na universidade')
else:
       resp = print('Você não pode se matricular na faculdade')

dados_alunos.append("Nome: "+nome+"\nSobrenome:"+sobrenome+"\nIdade: "+str(idade)+"\nENEM:"+enem+"\nEmail: "+email+"\nRenda Familiar"+str(renda_familiar)+"\nFiliação: "+filiação+"\nCPF :"+cpf+"\nEscolaridade: "+escolaridade)

     




