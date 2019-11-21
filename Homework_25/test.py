class Temperatures:
    def fahr_to_celc(self, fahr):
        celcium = (fahr - 32) * 5/9
        return "{} °C".format(round(celcium, 4))
    def celc_to_fahr(self, celc):
        fahrenheit = (celc * 9/5) +32
        return "{} °F".format(round(fahrenheit, 4))

calculator = Temperatures()

print(calculator.fahr_to_celc(88))

print(calculator.celc_to_fahr(88))