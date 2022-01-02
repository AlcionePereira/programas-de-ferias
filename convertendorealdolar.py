#Crie um programa que leia quanto dinheiro uma pessoa tem na
#  carteira e mostre quantos dólares ela pode comprar.
#considere US$1,00 = R$3,27


def main():
     real = float(input('Digite quanto você tem na carteira: R$'))
     dolar = real / 3.27
     print(f'Com R${real:.2f} na carteira você pode comprar US${dolar:.2f}')
if __name__ == "__main__":
    main()
