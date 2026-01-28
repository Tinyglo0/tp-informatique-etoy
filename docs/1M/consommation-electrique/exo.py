def puissance_appareil(...):
    ...

def energie_consommee(...):
    ...

def cout_utilisation(...):
    ...

def cout_consommation(...):
    tension = 230
    prix = 0.1582

    puissance = ...(...,...)

    energie_en_Wh = ...(...,...)
    energie_en_kWh = energie_en_Wh / 1000
    
    cout = ...(...,...)

    return cout

assert puissance_appareil(230, 20) == 4600
assert energie_consommee(4600, 1.5) == 6900
assert cout_utilisation(6.9, 0.1582) == 1.09
assert cout_consommation(20, 1.5) == 1.09

