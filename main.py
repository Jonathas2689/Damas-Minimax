from rich import print
from rich.table import Table
from rich.console import Console
rodada = 1
jogador_vez = "M" if rodada%2==0 else "J"
tab = []
colunas = ('  ','A','B','C','D','E','F','G','H')
P_J = "[blue]●[/blue]"
P_M = "[red]●[/red]"
D_J = "[purple]●[/purple]"
D_M = "[brown]●[/brown]"

def gera_tabuleiro():

    for y in range(8):
        tab.insert(y,[])
        for x in range(8):
            if (x+y)%2!=0:
                c = "rgb(65,65,65)"
                if y <= 2:
                    p = P_M
                elif y >= 5:
                    p = P_J
                else:
                    p = " "

            else:
                c = "grey30"
                p = " "
            tab[y].append([c,p])
    
    return tab

def mostrar_tabuleiro(tabuleiro):

    global colunas
    tabela = Table(show_header=False, show_lines=True, box=None, padding=0)

    for i_linhaY,linhaY in enumerate(tabuleiro):
        v = [str(len(tabuleiro)-i_linhaY)]

        for i_linhaX,linhaX in enumerate(linhaY):
            v.append(f"[on {linhaX[0]} ]{linhaX[1]} [/]")

        tabela.add_row(*v)

    tabela.add_row(*colunas)
    console.print(tabela)

def validar_jogada(y1,x1,y2,x2):

    global colunas
    #p_atual = tab[y1-1][x1]
    jogada_valida = False
    #y1 = 8-y1
    #y2 = 8-y2

    if (y1 in range(8) and y1 in range(8) and x1 in colunas[1:8] and x2 in colunas[1:8]):
        x1 = colunas.index(x1)-1
        x2 = colunas.index(x2)-1
        print(1)
        if tab[y2][x2][1] in (" ",P_M,D_M):
            print(2)
            
            if tab[y1][x1][1] == P_J:
                jogada_valida = y1-y2 == 1 and x2-x1 in (-1,1)
                print(3)

            elif tab[y1][x1][1] == D_J:
                jogada_valida = (y1-y2)/x1-x2 == 1
                print(4)
                    
    return jogada_valida

def realizar_jogada(y1,x1,y2,x2):

    global tab
    global colunas
    y1 = 8-int(y1)
    y2 = 8-int(y2)

    if validar_jogada(y1,x1,y2,x2):
        x1 = colunas.index(x1)-1
        x2 = colunas.index(x2)-1
        tab[y2][x2][1] = tab[y1][x1][1]
        tab[y1][x1][1] = " "
        mostrar_tabuleiro(tab)
    else:
        print(False)
    
    # realizar se for válido
    



tab = gera_tabuleiro()
console = Console()
mostrar_tabuleiro(tab)
realizar_jogada(3,"A",4,"B")
#mostrar_tabuleiro(tab)

