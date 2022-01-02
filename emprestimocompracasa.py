#Escreva um programa para aprovar o empréstimo bancário para a compra de uma
#casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele
# vai pagar. A prestação mensal não pode exceder 30% do salário ou então o
# empréstimo será negado.

def prestação(valor_casa, parcelas,porcentagem, salario):
    p = valor_casa / parcelas
    if p > porcentagem:
        print('Empréstimo APROVADO')
    else:
        print('Empréstimo NEGADO')

def main():
    valor_casa = float(input('Digite o valor da casa: R$'))
    salario = float(input('Quanto é seu salário? R$ '))
    parcelas = int(input('Quantidade de parcelas: '))
    porcentagem = salario * 30 / 100
    resultado = prestação(valor_casa, parcelas, salario, porcentagem)
   
   
if __name__ == '__main__':
    main()


