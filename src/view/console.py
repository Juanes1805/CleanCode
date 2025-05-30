import sys 
sys.path.append("src")

from model import app

amount = float( input( "Ingrese la couta mensual a ahorrar: ") )
interest = float( input( "Ingrese el interés: ") )
period= int( input( "Ingrese el número de cuotas que quiere ahorrar: ") ) 

try:
    payment = app.Saving(amount, interest, period)
    paymentt = payment.calculate_programmed_savings()
    print( f"El valor de la cuota es: {paymentt}" )
except Exception as err :
    print(f"No se puedo calcular el monto a ahorrar { err } ")
