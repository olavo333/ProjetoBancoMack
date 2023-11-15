# PROJETO N2 FEITO POR OLAVO GOMES GUIMARÃES
# TIA: 42335728
#header
import string
from random import choice
import time
import re

#variaveis universais
#1+1=2
line = ('------------------------------------------------')
tamSenha = 6                                                # Tamanho minimo senha
limiteErroSenha = 3                                         # Quantas tentativas até bloquear a conta
acessoLimitado = 0                                          # Limitador de acesso (0 = falso 1 = verdadeiro)
cadastrado = 0                                              # 
historicoTipo = []                                          
historicoValor = []                                         
red = "\033[1;31m"
green = '\033[32m'
white = '\033[37m'


#def functions
def main(cadastrado, acessoLimitado):
    while True:
        while True:
            if acessoLimitado == 1 and cadastrado == 1:
                print(line)
                print('\t       ACESSO LIMITADO')
                print('\t\t- MACK BANK –\n')
                print('\t(1) DEPOSITAR')
                print('\t(2) FINALIZAR')
                enter = int(input('\nESCOLHA UMA OPÇÃO: '))
                if enter > 2 or enter < 1:
                    print(line)
                    print('FAVOR DIGITAR UMA ALTERNATIVA VALIDA')
                else:
                    if enter == 1:
                        saldo, historicoTipo, historicoValor = deposito(nConta, user, saldo, senha)
                    if enter == 2:
                        sair()
            else:
                break


        while True:
            if acessoLimitado == 0 and cadastrado == 1:
                print(line)
                print('\t\t- MACK BANK –\n')
                print('\t(1) DEPOSITAR')
                print('\t(2) SACAR')
                print('\t(3) CONSULTAR SALDO')
                print('\t(4) CONSULTAR EXTRATO')
                print('\t(5) FINALIZAR')
                enter = int(input('\nESCOLHA UMA OPÇÃO: '))
                if enter > 5 or enter < 1:
                    print(line)
                    print('FAVOR DIGITAR UMA ALTERNATIVA VALIDA')
                else:
                    if enter == 1:
                        saldo, historicoTipo, historicoValor = deposito(nConta, user, saldo, senha)
                    if enter == 2:
                        saldo, historicoTipo, historicoValor, limiteCred, acessoLimitado = saque(nConta, user, saldo, senha, limiteCred, acessoLimitado)
                        break
                    if enter == 3:
                        acessoLimitado = consultaSaldo(nConta, user, saldo, senha, limiteCred, acessoLimitado)
                    if enter == 4:
                        acessoLimitado = consultaExtrato(nConta, user, saldo, senha, limiteCred, acessoLimitado, historicoTipo, historicoValor)
                    if enter == 5:
                        sair()
            else:
                break


        while True:
            if cadastrado == 0 and acessoLimitado == 0:
                print(line)
                print('\t\t- MACK BANK –\n')
                print('\t(1) CADASTRAR CONTA CORRENTE')
                print('\t(2) FINALIZAR')
                enter = int(input('\nESCOLHA UMA OPÇÃO: '))
                if enter > 2 or enter < 1:
                    print(line)
                    print('FAVOR DIGITAR UMA ALTERNATIVA VALIDA')
                else:
                    if enter == 1:
                        nConta, user, tele, email, saldo, limiteCred, senha = cadastro()
                        cadastrado = 1
                        break
                    if enter == 2:
                        sair()
            else:
                break

                

def cadastro():
    print(line)
    print('MACK BANK – CADASTRO DE CONTA\n')
    chars = string.digits
    nConta =  ''.join(choice(chars) for _ in range(4))    
    user=input('CADASTRAR NOME DO CLIENTE:\t')
    while True:
        if user == "":
            print('NOME NÃO PODE ESTAR EM BRANCO')
            user=input('CADASTRAR NOME DO CLIENTE:\t')
        else:
            
            break
        
    tele=input('CADASTRAR NUMERO DE TELEFONE:\t')
    while True:
        if tele == "":
            print('TELEFONE NÃO PODE ESTAR EM BRANCO')
            tele=input('CADASTRAR NUMERO DE TELEFONE:\t')
        else:
            
            break
        
    email=input('CADASTRAR EMAIL:\t\t')
    while True:
        if email == "":
            print('EMAIL NÃO PODE ESTAR EM BRANCO')
            email=input('CADASTRAR EMAIL:\t\t')
        elif check(email)==False:
            print('FORMATO INVALIDO, USE SOMENTE NOME@EXEMPLO.COM')
            email=input('CADASTRAR EMAIL:\t\t')
        else:
            
            break
        
    saldo=int(input('CADASTRAR SALDO INICIAL:\t'))
    while True:
        if saldo < 1000:
            print('SALDO DEVE SER MAIOR OU IGUAL A R$1000')
            saldo=int(input('CADASTRAR SALDO INICIAL:\t'))
        else:
            
            break
        
    limiteCred=int(input('CADASTRAR LIMITE DE CRÉDITO:\t'))
    while True:
        
        if limiteCred < 0:
            print('LIMITE DE CREDITO DEVE SER MAIOR OU IGUAL A 0')
            limiteCred=int(input('CADASTRAR LIMITE DE CRÉDITO:\t'))
        else:
            
            break
        
    senha=input('CADASTRAR SENHA:\t\t')
    while True:
        if len(senha) != tamSenha:
            print('SENHA DEVE SER COMPOSTA POR ',tamSenha,' CARACTERES')
            senha=input('CADASTRAR SENHA:\t\t')
        else:
            while True:
                senha2=input('REPITA A SENHA:\t\t\t')
                if senha2!=senha:
                    print('SENHA DIGITADA INCORRETAMENTE')
                else:
                    print('\nCONTA REGISTRADA COM SUCESSO')
                    break
            break
        
    print(line)
    print('\t\t- DADOS CLIENTE -\n')
    print('NUMERO DA CONTA:\t', nConta)
    print('NOME DO CLIENTE:\t', user)
    print('TELEFONE:\t\t', tele)
    print('EMAIL:\t\t\t', email)
    print('SALDO INICIAL:\t\t', saldo)
    print('LIMITE DE CRÉDITO:\t', limiteCred)
    
    
    return nConta, user, tele, email, saldo, limiteCred, senha





def deposito(nConta, user, saldo, senha):
    print(line)
    print('MACK BANK – DEPÓSITO EM CONTA\n')
    nConta2=input('INFORME O NÚMERO DA CONTA: ')
    while True:
        if nConta2!=nConta:
            print('NÚMERO DA CONTA INCORRETO')
            nConta2=input('INFORME O NÚMERO DA CONTA: ')
        else:
            break
    print('NOME DO CLIENTE: ', user)
    deposito=int(input('VALOR DO DEPÓSITO: '))
    while True:
        if deposito <= 0:
            print('DEPOSITO DEVE SER MAIOR QUE 0')
            deposito=int(input('VALOR DO DEPÓSITO: '))
        else:
            saldoNovo = deposito + saldo
            historicoTipo.append('DEPÓSITO: ')
            historicoValor.append(deposito) 
            print('\nDEPÓSITO REALIZADO COM SUCESSO!')
            break
        
    return saldoNovo, historicoTipo, historicoValor




def saque(nConta, user, saldo, senha, limiteCred, acessoLimitado):
    limiteNovo=limiteCred
    print(line)
    print('MACK BANK – SAQUE DA CONTA\n')
    nConta2=input('INFORME O NÚMERO DA CONTA: ')
    while True:
        if nConta2!=nConta:
            print('NÚMERO DA CONTA INCORRETO')
            nConta2=input('INFORME O NÚMERO DA CONTA: ')
        else:
            break
    print('NOME DO CLIENTE: ', user)
    contErroSenha=0
    while contErroSenha < limiteErroSenha:
        senha2 = input('INFORME A SENHA: ')
        if senha2==senha:
            saque=int(input('VALOR DO SAQUE: '))
            while True:
                disponivel=saldo+limiteCred
                if saque <= 0:
                    print('SAQUE DEVE SER MAIOR QUE 0')
                    saque=int(input('VALOR DO SAQUE: '))
                    
                elif saque > disponivel:
                    print('\nSALDO INDISPONIVEL')
                    saldoNovo=saldo
                    break
                
                elif saque > saldo and saque <= disponivel:
                    print('VOCE ESTÁ USANDO O SEU LIMITE DE CRÉDITO')
                    saldoNegativo=saldo-saque
                    limiteNovo=saldoNegativo+limiteCred
                    saldoNovo=0
                    saqueNegativo=saque*-1
                    historicoTipo.append('SAQUE: ')
                    historicoValor.append(saqueNegativo) 
                    print('\nSAQUE REALIZADO COM SUCESSO!')
                    break
                    
                else:
                    saldoNovo=saldo-saque
                    saqueNegativo=saque*-1
                    historicoTipo.append('SAQUE: ')
                    historicoValor.append(saqueNegativo) 
                    print('\nSAQUE REALIZADO COM SUCESSO!')
                    break
            break
        else:
            contErroSenha += 1
            restante=limiteErroSenha-contErroSenha
            print('SENHA INCORRETA. TENTATIVAS RESTANTES:',restante)
            if restante == 0:
                saldoNovo=saldo
                acessoLimitado = 1
                print('\nTENTATIVAS EXAUSTADAS, CONTA LIMITADA')
                
    return saldoNovo, historicoTipo, historicoValor, limiteNovo, acessoLimitado

      

def consultaSaldo(nConta, user, saldo, senha, limiteCred, acessoLimitado):
    print(line)
    print('MACK BANK – CONSULTA SALDO\n')
    nConta2=input('INFORME O NÚMERO DA CONTA: ')
    while True:
        if nConta2!=nConta:
            print('NÚMERO DA CONTA INCORRETO')
            nConta2=input('INFORME O NÚMERO DA CONTA: ')
        else:
            break
    print('NOME DO CLIENTE: ', user)
    contErroSenha=0
    while contErroSenha < limiteErroSenha:
        senha2 = input('INFORME A SENHA: ')
        if senha2==senha:
            print('\nSALDO EM CONTA: R$', saldo)
            print('LIMITE DE CRÉDITO: R$', limiteCred)
            input('\nPRESSIONE QUALQUER TECLA PARA VOLTAR AO MENU...')
            break
        else:
            contErroSenha += 1
            restante=limiteErroSenha-contErroSenha
            print('SENHA INCORRETA. TENTATIVAS RESTANTES:',restante)
            if restante == 0:
                saldoNovo=saldo
                acessoLimitado = 1
                print('\nTENTATIVAS EXAUSTADAS, CONTA LIMITADA')
                
    return acessoLimitado





def consultaExtrato(nConta, user, saldo, senha, limiteCred, acessoLimitado, historicoTipo, historicoValor):
    print(line)
    print('MACK BANK –  EXTRATO DA CONTA\n')
    nConta2=input('INFORME O NÚMERO DA CONTA: ')
    while True:
        if nConta2!=nConta:
            print('NÚMERO DA CONTA INCORRETO')
            nConta2=input('INFORME O NÚMERO DA CONTA: ')
        else:
            break
    print('NOME DO CLIENTE: ', user)
    contErroSenha=0
    while contErroSenha < limiteErroSenha:
        senha2 = input('INFORME A SENHA: ')
        if senha2==senha:
            print('\nSALDO EM CONTA: R$', saldo)
            print('LIMITE DE CRÉDITO: R$', limiteCred)
            print('\nULTIMAS OPERAÇÕES:')
            for op in range(len(historicoValor)):
                print(historicoTipo[op],'R$',historicoValor[op])
            input('\nPRESSIONE QUALQUER TECLA PARA VOLTAR AO MENU...')
            break
        else:
            contErroSenha += 1
            restante=limiteErroSenha-contErroSenha
            print('SENHA INCORRETA. TENTATIVAS RESTANTES:',restante)
            if restante == 0:
                saldoNovo=saldo
                acessoLimitado = 1
                print('\nTENTATIVAS EXAUSTADAS, CONTA LIMITADA')
                
    return acessoLimitado






def check(s):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat,s):
        return True
    else:
        return False




def sair():
    print(line,'''
MACK BANK – SOBRE

Este programa foi desenvolvido por
Olavo G Guimarães''')
    time.sleep (3)
    quit()




#main call
main(cadastrado, acessoLimitado)
