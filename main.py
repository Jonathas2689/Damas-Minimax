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

def ler_jogada():

    global colunas
    jogada = input("Digite a jogada: ").upper().strip()
    c1,c2 = jogada.split()
    coordenada_certa = len(c1)==2 and len(c2) == 2
    coordenada_certa = coordenada_certa and c1.isalnum() and c2.isalnum()
    print(c1,c2)
    
    if coordenada_certa:
        if c1[0] in colunas and int(c1[1]) in range(1,8):
            x1,y1=c1
            print(x1,y1,"T1")
        elif c1[1] in colunas and int(c1[0]) in range(1,8):
            y1,x1=c1
            print(x1,y1,"T1-1")
        else:
            print("T1-2")
            coordenada_certa = False


        if c2[0] in colunas and int(c2[1]) in range(1,8):
            x2,y2=c2
            print(x2,y2,"T2")
        elif c2[1] in colunas and int(c2[0]) in range(1,8):
            y2,x2=c2
            print(x2,y2,"T2-1")
        else:
            coordenada_certa = False
            print("T2-2")
            
    if coordenada_certa: 
        return int(y1),x1,int(y2),x2
    else:
        print("Coordenada inválida. Tente novamente")


def validar_jogada(y1,x1,y2,x2):

    global colunas
    #p_atual = tab[y1-1][x1]
    jogada_valida = False
    #y1 = 8-y1
    #y2 = 8-y2

    if (y1 in range(8) and y2 in range(8) and x1 in range(8) and x2 in range(8)):

        print(1)
        if tab[y2][x2][1] == " ":
            print(2)
            
            if tab[y1][x1][1] == P_J:
                jogada_valida = y1-y2 == 1 and x2-x1 in (-1,1)
                print(3)

            elif tab[y1][x1][1] == D_J:
                jogada_valida = (y1-y2)/(x1-x2) == 1
                print(4)
                    
    return jogada_valida

def realizar_jogada(Coordenadas):

    y1,x1,y2,x2 = Coordenadas
    print(y1,x1,y2,x2)
    global tab
    global colunas
    x1 = colunas.index(x1)-1
    x2 = colunas.index(x2)-1
    y1 = 8-y1
    y2 = 8-y2

    if validar_jogada(y1,x1,y2,x2):

        tab[y2][x2][1] = tab[y1][x1][1]
        tab[y1][x1][1] = " "
        mostrar_tabuleiro(tab)
    else:
        print(False)
    
    # realizar se for válido
    



tab = gera_tabuleiro()
console = Console()
mostrar_tabuleiro(tab)
realizar_jogada((3,"A",4,"B"))
realizar_jogada(ler_jogada())
#mostrar_tabuleiro(tab)

