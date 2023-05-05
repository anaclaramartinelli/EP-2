def define_posicoes(linha, coluna, orientacao, tamanho):
    saida = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            term = [linha+i, coluna]
            saida.append(term)
        else:
            term = [linha, coluna+i]
            saida.append(term)
    return saida

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    lista_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio in frota:
        frota[nome_navio].append(lista_posicoes)
    else:
        frota[nome_navio] = [lista_posicoes]

    return frota

  
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    saida_lista = define_posicoes(linha, coluna, orientacao, tamanho)
    
    for tipo_navio in frota.values():
        for navio in tipo_navio:
            for posicao in navio: 
                if posicao in saida_lista:
                    return False
                if posicao ==1 and posicao in saida_lista or posicao==0 and posicao in saida_lista:
                    return False
                for i in saida_lista:
                    if i[0] == posicao[0] and i[1] == posicao[1]:
                        return False
    for posicao in saida_lista:
        if  posicao[0] > 9 or posicao[0] < 0 or posicao[1] > 9 or posicao[1] < 0:
            return False 
                     
    return True


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):    
    tabuleiro = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    for posicao in frota.values():
        for i in posicao:
            for coord in i:
                linha = coord[0]
                coluna = coord[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro

def afundados(frota, tabuleiro):
    navios_afundados = 0
    for nome_navio, posicao in frota.items():
        for navio in posicao:
            tamanho_navio = len(navio)
            cont = 0
            for coord in navio:
                linha = coord[0]
                coluna = coord[1]
                if tabuleiro[linha][coluna] == 'X':
                    cont += 1
            if cont == tamanho_navio:
                navios_afundados += 1
    return navios_afundados

frota = {    
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

dici_navios = {
    'porta-aviões': 4, 'navio-tanque':3, 'contratorpedeiro':2, 'submarino':1
}

qtd = 0
i = 1


for nome_navio in dici_navios.keys():
    n = nome_navio
    tamanho = dici_navios[nome_navio]
    if nome_navio == 'porta-aviões':
        qtd = 1
    elif nome_navio == 'navio-tanque':
        qtd = 2
    elif nome_navio == 'contratorpedeiro':
        qtd = 3
    else:
        qtd = 4

    i = 1
    while i <= qtd:
        info = print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(n, tamanho))
    
        linha = input('Linha: ')
        coluna = input('Coluna: ')

        if linha.strip() == '' or coluna.strip()=='':    
            while linha == '' and coluna =='':
                print("A entrada do usuário está vazia. Digite um número")
                linha =  input('Linha: ')
                coluna = input('Coluna: ')
            

        linha = int(linha)
        coluna = int(coluna)

        if nome_navio != 'submarino':
            o = input("[1] Vertical [2] Horizontal > ")
            
            if o.strip() == '':    
                while o == '':
                    print("A entrada do usuário está vazia. Digite um número")
                    o =  input("[1] Vertical [2] Horizontal > ")                    
 
            o = int(o)

            if o == 1:
                orientacao = 'vertical'
                if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                    frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
                    i+=1
                else:
                    print('Esta posição não está válida!')
            else:
                orientacao = 'horizontal'
                if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                    frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
                    i+=1
                else:
                    print('Esta posição não está válida!')  
        else:
            orientacao = 'vertical'
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
                i+=1
            else:
                print('Esta posição não está válida!')

print (frota)