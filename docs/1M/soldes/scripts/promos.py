# --- PYODIDE:env --- #
def promo_A (prix_1, prix_2):
    if prix_1 < prix_2:
        prix_final = prix_1 / 2 + prix_2
    else:
        prix_final = prix_2 / 2 + prix_1
    return prix_final

def promo_B (prix_1, prix_2):
    prix_final = (prix_1 + prix_2) * (80/100)
    return prix_final

# --- PYODIDE:code --- #
...

