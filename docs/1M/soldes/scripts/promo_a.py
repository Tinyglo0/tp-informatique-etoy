# --- PYODIDE:code --- #

def promo_A (prix_1, prix_2):
    ...


# --- PYODIDE:corr --- #

def promo_A (prix_1, prix_2):
    if prix_1 < prix_2:
        prix_final = prix_1 / 2 + prix_2
    else:
        prix_final = prix_2 / 2 + prix_1
    return prix_final


# --- PYODIDE:tests --- #

assert promo_A(10, 20) == 25
assert promo_A(20, 10) == 25


# --- PYODIDE:secrets --- #

assert promo_A(10, 10) == 15
assert promo_A(30, 40) == 55