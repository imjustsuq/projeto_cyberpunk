import os
os.system('cls')
# listas
exames = ['Hemograma completo', 'Raio-x de Tórax', 'Ultrassonografia Abdominal', 'Eletrocardiograma', 'Tomografia Computadorizada', 'Ressonância Magnética', 'Teste de Glícemia']
codigo = []
preco = [50, 120, 200, 80, 350, 600, 30]
subtotal = 0
exames_escolhidos = []
# Loop
while True:
    print("""   
                    Lista de Exames Hospitalares    |
      
        Código          |       Exames                   |       Preços
            1           |   Hemograma completo           |      R$ 50.00
            2           |   Raio-X de Tórax              |      R$ 120.00
            3           |   Ultrassonografia Abdominal   |      R$ 200.00
            4           |   Eletrocardiograma            |      R$ 80.00
            5           |   Tomografia Computadorizada   |      R$ 350.00
            6           |   Ressonância Magnética        |      R$ 600.00
            7           |   Teste de Glícemia            |      R$ 30.00
            0           |   Finalizar atendimento
      """)
    codigo = int(input('Digite o código do exame desejado: '))
    # Validação das opções
    if codigo == 0:
        print('Programa encerrado!')
        break
    elif codigo == 1:
        print(exames[0])
        print(f'R$ {preco[0]}')
    elif codigo == 2:
        print(exames[1])
        print(f'R$ {preco[1]}')
    elif codigo == 3:
        print(exames[2])
        print(f'R$ {preco[2]}')
    elif codigo == 4:
        print(exames[3])
        print(f'R$ {preco[3]}')
    elif codigo == 5:
        print(exames[4])
        print(f'R$ {preco[4]}')
    elif codigo == 6:
        print(exames[5])
        print(f'R$ {preco[5]}')
    elif codigo == 7:
        print(exames[6])
        print(f'R$ {preco[6]}')
    else:
        print('Código inválido, tente novamente.')
    # Para validar preços
    subtotal += preco[codigo - 1]
    exames_escolhidos.append(exames[codigo - 1])
    novo_exame = input('Deseja selecionar um novo exame? (s/n): ')
    
# Formas de pagamento
print("\nFormas de pagamento:")
print("1 - Convênio (15% desconto)")
print("2 - Particular (sem desconto)")
print("3 - Cartão de crédito (8% acréscimo)")
# Input pagamento
pagamento = int(input("Escolha a forma de pagamento: "))

desconto = 0
acrescimo = 0
# Condição para verificar pagamento
if pagamento == 1:
    desconto = subtotal * 0.15
    total = subtotal - desconto
    forma = "Convênio"
elif pagamento == 2:
    total = subtotal
    forma = "Particular"
elif pagamento == 3:
    acrescimo = subtotal * 0.08
    total = subtotal + acrescimo
    forma = "Cartão de crédito"
else:
    print("Forma inválida! Considerando pagamento particular.")
    total = subtotal
    forma = "Particular"

# Resultado
print("\n===== RESUMO =====")
print("Exames escolhidos:")

for exame in exames_escolhidos:
    print("-", exame)

print(f"\nSubtotal: R$ {subtotal:.2f}")
print(f"Forma de pagamento: {forma}")
# Verificar se tem desconto ou acrescimo
if desconto > 0:
    print(f"Desconto: R$ {desconto:.2f}")

if acrescimo > 0:
    print(f"Acréscimo: R$ {acrescimo:.2f}")
# Valor total
print(f"Total a pagar: R$ {total:.2f}")

# Feito por Safira Nascimento Conceição Costa, Lucas Araújo do Nascimento.