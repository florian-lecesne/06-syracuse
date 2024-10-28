# filename : main.my
"""
Ce programme calcule la suite de Syracuse pour un entier donné,
créer et affiche un graphique de cette suite,
et calcule en parallèle le temps de vol, l'altituude maximale,
et le temps de vol en altitude pour cette suite. 
"""
# imports
from plotly.graph_objects import Scatter, Figure

#### Fonctions secondaires


### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    Affiche un graphique des valeurs de la suite de Syracuse.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()

#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    l = []
    l.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """

    n = 0
    for elt in l:
        if elt == 1:
            n = l.index(elt)
            break
    return n

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    n = 0
    ini = l[0]
    for elt in l:
        if elt < ini:
            n = l.index(elt)-1
            break
    return n


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    n = 0
    for elt in l:
        n = max(n, elt)
    return n


#### Fonction principale


def main():
    """
    Quelques tests de bon fonctionnement.
    """

    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
