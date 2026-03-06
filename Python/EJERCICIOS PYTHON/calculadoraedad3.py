from datetime import date
from dateutil.relativedelta import relativedelta

hoy = date.today()

año = int(input("INSERTA EL AÑO: "))
mes = int(input("INSERTA MES: "))
dia = int(input("INSERTA DIA: "))

fecha_nac = date(año, mes, dia)

diferencia_años = hoy.year - fecha_nac.year 
diferencia_mes = hoy.month - fecha_nac.month
diferencia_dia = hoy.day - fecha_nac.day

print("Tu edad exacta es", diferencia.years, "años", diferencia.months, "meses y", diferencia.days, ("días."))