# ============================================
#   IL MIO PRIMO SCRIPT PYTHON
#   Autore: [scrivi il tuo nome qui]
#   Data: maggio 2026
# ============================================

# --------------------------
# 1. VARIABILI
# (scatole in cui conserviamo informazioni)
# --------------------------

nome = "Mario"
eta = 25
altezza = 1.75
appassionato_di_coding = True

print("=== INFORMAZIONI PERSONALI ===")
print("Nome:", nome)
print("Età:", eta)
print("Altezza:", altezza, "metri")
print("Appassionato di coding:", appassionato_di_coding)


# --------------------------
# 2. OPERAZIONI MATEMATICHE
# (Python come calcolatrice)
# --------------------------

print("\n=== OPERAZIONI MATEMATICHE ===")

a = 10
b = 3

print("Somma:      ", a + b)
print("Sottrazione:", a - b)
print("Moltiplica: ", a * b)
print("Divisione:  ", a / b)
print("Resto:      ", a % b)   # il "%" restituisce il resto della divisione
print("Potenza:    ", a ** b)  # 10 elevato alla 3


# --------------------------
# 3. CONDIZIONI (if / else)
# (il programma prende decisioni)
# --------------------------

print("\n=== CONDIZIONI ===")

temperatura = 30

if temperatura > 25:
    print("Fa caldo! Mettiti la maglietta.")
elif temperatura > 15:
    print("Temperatura gradevole.")
else:
    print("Fa freddo! Mettiti il cappotto.")


# --------------------------
# 4. CICLO (for loop)
# (ripetiamo un'azione più volte)
# --------------------------

print("\n=== CICLO FOR ===")

frutta = ["mela", "banana", "arancia", "kiwi"]

print("Frutta nel cesto:")
for frutto in frutta:
    print(" -", frutto)


# --------------------------
# 5. FUNZIONE
# (un blocco di codice riutilizzabile)
# --------------------------

print("\n=== FUNZIONE ===")

def saluta(nome, ora_del_giorno):
    if ora_del_giorno == "mattina":
        messaggio = "Buongiorno"
    elif ora_del_giorno == "sera":
        messaggio = "Buonasera"
    else:
        messaggio = "Ciao"
    return f"{messaggio}, {nome}!"

# Chiamiamo la funzione con valori diversi
print(saluta("Mario", "mattina"))
print(saluta("Lucia", "sera"))
print(saluta("Gianni", "pomeriggio"))


# --------------------------
# 6. DIZIONARIO
# (coppie chiave → valore, come un vocabolario)
# --------------------------

print("\n=== DIZIONARIO ===")

persona = {
    "nome": "Mario",
    "eta": 25,
    "città": "Verona",
    "hobby": "programmazione"
}

print("Dati della persona:")
for chiave, valore in persona.items():
    print(f"  {chiave}: {valore}")


# --------------------------
# FINE SCRIPT
# --------------------------
print("\n✅ Script completato con successo!")
