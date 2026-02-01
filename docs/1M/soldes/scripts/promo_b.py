# --- PYODIDE:code --- #

def promo_B (prix_1, prix_2):
    ...


# --- PYODIDE:corr --- #

def promo_B (prix_1, prix_2):
    prix_final = (prix_1 + prix_2) * (80/100)
    return prix_final


# --- PYODIDE:tests --- #

assert promo_B(10, 20) == 24
assert promo_B(20, 10) == 24


# --- PYODIDE:secrets --- #

assert promo_B(10, 10) == 16
assert promo_B(30, 40) == 56
