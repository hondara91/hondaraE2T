from datetime import date
from dateutil.relativedelta import relativedelta

año = int(input("INSERTA EL AÑO: "))
mes = int(input("INSERTA MES: "))
dia = int(input("INSERTA DIA: "))

fecha_nac = date(año, mes, dia)
hoy = date.today()

diferencia = relativedelta(hoy, fecha_nac)

print("Tu edad exacta es", diferencia.years, "años", diferencia.months, "meses y", diferencia.days, ("días."))



