import os
os.system('cls')

import time

listaUsers = []

def timer():
    funcionando = True
    segundos = 15
    fim = 0

    while(funcionando):
        print(segundos)
        time.sleep(1)
        if segundos == 10:
            print('Joseane está indo resolver seu problema. Em poucos minutos ela chegará')
        segundos-=1
        if(segundos <= fim):
            funcionando = False
            print(segundos)
    print('Obrigado por aguardar!')
    return 

def home_page():
    os.system('cls')
    print('QuickSolver')
    next = int(input('Acesso Chambres[0] ou Acesso Hóspede[1]: '))
    if next == 0:
        return tela_escolha_gerencia_or_funcionario()
    if next ==1:
        return tela_inicial_hosp()
    else:
        return home_page()

def tela_escolha_gerencia_or_funcionario():
    os.system('cls')
    print('QuickSolver')
    next = input('Acesso gerência[0], Acesso funcionários[1] ou voltar para a Home Page[2]: ')
    if next == '0':
        return tela_inicial_chambres_gerente()
    elif next == '1':
        return tela_inicial_chambres_func()
    elif next =='2':
        return home_page()
    else:
        return tela_escolha_gerencia_or_funcionario()

def tela_inicial_chambres_gerente():
    os.system('cls')
    print('QuickSolver')
    voltar = input('Deseja voltar? [S] ou [N]').upper()
    if voltar == 'S':
        return tela_escolha_gerencia_or_funcionario()
    elif voltar =='N':
        os.system('cls')
        print('QuickSolver')
        usuario = input('Login: ')
        senha = input('Senha: ')
        verificadorUser = users_gerencia.get(usuario)
        if verificadorUser == None:
            print('Login não cadastrado!')
            time.sleep(1.5)
            return tela_inicial_chambres_gerente()
        elif senha == users_gerencia[usuario]:
            return tela_chambres_gerente2()
        else:
            print('Senha incorreta!')
            time.sleep(1.5)
            return tela_inicial_chambres_gerente()
    else:
        return tela_inicial_chambres_gerente()

def tela_chambres_gerente2():
    os.system('cls')
    print('QuickSolver')
    next=input('Digite para: \n0.Ver as notificações dos hóspedes \n1. Resolver problema do hóspede \n2. Ver os feedbacks \n3. Cadastrar funcionário \n4. Encerrar sessão : ')
    if next =='0':
        return tela_notificoes()
    elif next =='1':
        return resolver_problemas()
    elif next=='2':
        return ver_notas()
    elif next=='3':
        return cadastro()
    elif next =='4':
        os.system('cls')
        print('Sessão Encerrada')
        time.sleep(1.5)
        return home_page()
    else:
        return tela_chambres_gerente2()
    

def tela_notificoes():
    os.system('cls')
    print('QuickSolver')
    print('NOTIFICAÇÕES')
    print('QUARTO   PROBLEMA                                COMENTÁRIO')
    print(quartos_problemas)
    time.sleep(5)
    return tela_chambres_gerente2()

def resolver_problemas():
    os.system('cls')
    print('QuickSolver')
    chave = input('Qual o quarto que você quer resolver o problema?: ')
    erro = quartos_problemas.pop(chave, 'Quarto sem problemas')
    if erro == 'Quarto sem problemas':
        print(erro)
        time.sleep(1.5)
    else:
        print(f'Problema do quarto {chave} resolvido')
        time.sleep(1.5)
    return tela_chambres_gerente2()

def ver_notas():
    os.system('cls')
    print('QuickSolver')
    print('FEEDBACKS')
    print('QUARTO|ATENDIMENTO HOTEL| NOTA HOTEL |NOTA FUNCIONÁRIOS')
    print(nota)
    time.sleep(5)
    return tela_chambres_gerente2()

def cadastro():
    os.system('cls')
    print('QuickSolver')
    next=input('Digite para: \n0.Ver funcionários cadastrados \n1. Recadastrar usuário e senha \n2. Cadastrar novo usuário\n3. Remover usuário \n4. Voltar ao menu inicial\n: ')
    if next == '0':
        os.system('cls')
        print('QuickSolver')
        print('esquema - USUÁRIO : SENHA')
        print(users_chambres)
        time.sleep(5)
        return cadastro()
    elif next =='1':
        login = input('Qual o usuário que você quer alterar? ')
        erro = users_chambres.get(login, 'Usuário inexistente')
        if erro == 'Usuário inexistente':
            print(erro)
            print('Para cadastrar novo usuário digite 2')
            time.sleep(1.5)
        else:
            senha = input(f'Qual nova senha do login: {login}? ')
            users_chambres[login] = senha
            print('Dados do usuário atualizados com sucesso')
            time.sleep(1.5)
        return cadastro()
    elif next =='2':
        login = input('Qual o login que você quer cadastrar? ')
        verificador = users_chambres.get(login)
        if verificador == None:
            senha = input(f'Qual a senha do usuário: {login}? ')
            users_chambres[login] = senha
            print('Usuário cadastrado com sucesso')
            time.sleep(1.5)
        else:
            print('Usuário já cadastrado, para modificar digite 1')
            time.sleep(1.5)
        return cadastro()
    elif next =='3':
        login = input('Qual login você quer apagar? ')
        erro = users_chambres.pop(login, 'Login inexistente')
        if erro == 'Login inexistente':
            print(erro)
            time.sleep(1.5)
        else:
            print('Usuário removido com sucesso')
            time.sleep(1.5)
        return cadastro()
    elif next =='4':
        return tela_chambres_gerente2()
    else:
        return cadastro()


def tela_inicial_chambres_func():
    os.system('cls')
    print('QuickSolver')
    voltar = input('Deseja voltar? [S] ou [N]').upper()
    if voltar == 'S':
        return tela_escolha_gerencia_or_funcionario()
    elif voltar =='N':
        os.system('cls')
        print('QuickSolver')
        usuario = input('Login: ')
        senha = input('Senha: ')
        verificadorUser = users_chambres.get(usuario)
        if verificadorUser == None:
            print('Login não cadastrado!')
            time.sleep(1.5)
            return tela_inicial_chambres_func()
        elif senha == users_chambres[usuario]:
            return tela_chambres_func2()
        else:
            print('Senha incorreta!')
            time.sleep(1.5)
            return tela_inicial_chambres_func()
    else:
        return tela_inicial_chambres_func()

def tela_chambres_func2():
    os.system('cls')
    print('QuickSolver')
    print('NOTIFICAÇÕES')
    print('QUARTO   PROBLEMA                                COMENTÁRIO')
    print(quartos_problemas)
    time.sleep(5)
    return tela_chambres_func3()

def tela_chambres_func3():
    os.system('cls')
    print('QuickSolver')
    next=input('Digite para: 0.Rever as notificações, 1. Resolver problema do hóspede ou 2. Encerrar sessão: ')
    if next =='0':
        return tela_chambres_func2()
    elif next =='1':
        return tela_chambres_func4()
    elif next =='2':
        os.system('cls')
        print('Sessão Encerrada')
        time.sleep(1.5)
        return home_page()
    else:
        return tela_chambres_func3()

def tela_chambres_func4():
    os.system('cls')
    print('QuickSolver')
    chave = input('Qual o quarto que você quer resolver o problema?: ')
    erro = quartos_problemas.pop(chave, 'Quarto sem problemas')
    if erro == 'Quarto sem problemas':
        print(erro)
        time.sleep(1.5)
    else:
        print(f'Problema do quarto {chave} resolvido')
        time.sleep(1.5)
    sequencia=input('Você deseja rever as notificações[0] ou voltar para a home_page[1]')
    if sequencia == '0':
        return tela_chambres_func2()
    else:
        return home_page()


def tela_inicial_hosp():
    os.system('cls')
    print('QuickSolver')
    print('Resolvemos seu problema em 15min')
    a=input('Deseja iniciar?[s]ou[n]').upper()
    if a == 'SIM' or a == 'S':
        return menu_h_quarto()
    elif a == 'NAO' or a == 'NÃO' or a =='N':
        b=input('Deseja voltar à Home Page?[S]ou[N]: ').upper()
        if b == 'SIM' or b == 'S':
            return home_page()
        else:
            return tela_inicial_hosp()
    else:
        return tela_inicial_hosp()

def menu_h_quarto():
    os.system('cls')
    print('QuickSolver')
    chave = input('Qual quarto você está hóspedado? ')
    verificador = quartos_problemas.get(chave)
    if verificador == None:
        
        return menu_h1(chave)
    else:
        a=input('Problema ja cadastrado, deseja reportar um novo problema? [s]ou[n]').upper()
        if a=='S':
           
           return menu_h1(chave)
        else:
            return home_page()  
      

def menu_h1(chave):
    os.system('cls')
    resp1=input('0. Limpeza\n1. Manutenção\n2. Incômodos\n3. Solicitar itens\n4. Outros\n5. voltar\nResposta: ')
    print(chave)
    if resp1 == '0':
        quartos_problemas[chave]=['Limpeza']
        return menu_h2(chave)
    elif resp1 == '5':
        return tela_inicial_hosp()
    else:
        return menu_h1()

def menu_h2(chave):
    os.system('cls')
    resp2=input('0. Itens não foram trocados\n1. Enxoval não adequado\n2. Roupas de cama sujas\n3. Limpar quarto\n4. Outros\n5.voltar\nResposta: ')
    if resp2 == '0':
        quartos_problemas[chave].append('Itens não foram trocados ')
        return menu_h22(chave)
    elif resp2 == '5':
        return menu_h1()
    else:
        return menu_h2()

def menu_h22(chave):
    os.system('cls')
    a=input('Descrever seu problema(opcional)\nSim[S] OU Não[N]: ').upper()
    if a == 'S' or a == 'SIM':
        quartos_problemas[chave].append(input('Digite seu problema: '))
    
    os.system('cls')
    b=input('Enviar uma foto[s]ou[n](opcional): ').upper()

    if b == 'S':
        print('foto enviada')
        time.sleep(2.5)
    os.system('cls')
    timer()
    return menu_h3(chave)

def menu_h3(chave):
    os.system('cls')
    print('Avaliação')
    print('Como foi nosso atendimento?')
    chavenotas=input('0. Péssimo\n1. Ruim\n2. Bom\n3. Ótimo\n4. Excelente\n: ')
    nota[chave]=[tradução[chavenotas]]
    return menu_h32(chave)

def menu_h32(chave):
    os.system('cls')
    print('Avalie nosso hotel')
    chavenotas=input('0. Péssimo\n1. Ruim\n2. Bom\n3. Ótimo\n4. Excelente\n: ')
    nota[chave].append(tradução[chavenotas])
    return menu_h33(chave)

def menu_h33(chave):
    os.system('cls')
    print('Avalie Joseane')
    chavenotas=input('0. Péssimo\n1. Ruim\n2. Bom\n3. Ótimo\n4. Excelente\n: ')
    nota[chave].append(tradução[chavenotas])
    return tela_final()

def tela_final():
    os.system('cls') 
    print('Quick Solver')
    print('Obrigada pela avaliação')
    print('Tenha uma excelente estadia')
    resp_final = input('Voltar para o início[S]ou[N]: ').upper()
    if resp_final == 'S':
        return home_page()
    else:
        return tela_final()

users_gerencia={
    'philippe@chambres.com':'admin1234'
}

users_chambres={
    'joseane@chambres.com':'12345678'
}

quartos_problemas={}
nota={}
tradução={'0': 'Péssimo','1':'Ruim','2':'Bom','3':'Ótimo','4':'Excelente'}
chave=''

home_page()