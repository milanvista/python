resultaat = None
Getal = None
operator = None
wacht_voor_getal = True

# als de operator = teken word gegeven geeft hij de expression. 
# de f in de print zorgt ervoor dat de expression in een string kan worden geformat

while True:
    if operator == '=':
        print(f"Resultaat: {resultaat}")
        break

# de Float functie zorgt ervoor dat de value wordt overgezet in een float getal
    elif wacht_voor_getal == True:
        while True:
            try:
                Getal = float(input("Typ een getal: "))

# Als er een fout type input word gegeven krijg je de volgende fout melding :

            except ValueError:
                print("Dit is geen getal, probeer opnieuw.")

# Als er geen foute input gevonden word gaat hij de operator input vergelijken met de mogelijke operators als hij een gelijke vind
# dan gebruikt hij de bijpassende operator bij het resultaat.
            else:
                if resultaat == None:
                    resultaat = Getal
                else:
                    if operator == '+':
                        resultaat = resultaat + Getal
                    elif operator == '-':
                        resultaat = resultaat - Getal
                    elif operator == '*':
                        resultaat = resultaat * Getal
                    elif operator == '/':
                        resultaat = resultaat / Getal

                break
        wacht_voor_getal = False

# Als de rekenmachine niet voor een getal aan het wachten is vraagt hij voor een operator wanneer de operator word ingevuld wordt 
# wacht_voor_getal weer true waardoor je een nieuwe input kan geven. dit loopt door totdat de operator = word gegeven.

    else:
        while True:
            operator = input("Vul een van de volgende in +, -, *, /, =: ")
            if operator in ('+', '-', '*', '/', '='):
                break
            else:
                print("Dit is niet geldig, probeer opnieuw.")
        wacht_voor_getal = True