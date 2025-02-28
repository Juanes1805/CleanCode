import unittest
import app


class Ahorro_programado_test(unittest.TestCase):

    def test_normal_1(self):
        monto = 300000
        interes = 0.035
        periodo = 24

        result = app.calcular_ahorro_programado(monto, interes, periodo)
        expected = 7451971.429
        self.assertAlmostEqual(expected, result, 2)
    
    def test_normal_2(self):
        monto = 500000
        interes = 0.06
        periodo = 36

        result = app.calcular_ahorro_programado(monto, interes, periodo)
        expected = 19079983.33
        self.assertAlmostEqual(expected, result, 2)
    
    def test_normal_3(self):
        monto = 1000000
        interes = 0.1
        periodo = 60

        result = app.calcular_ahorro_programado(monto, interes, periodo)
        expected = 65999990
        self.assertAlmostEqual(expected, result, 2)
    
    def test_normal_4(self):
        monto = 250000
        interes = 0.05
        periodo = 1

        result = app.calcular_ahorro_programado(monto, interes, periodo)
        expected = 262480
        self.assertAlmostEqual(expected, result, 2)
    
    def test_normal_5(self):
        monto = 200000
        interes = 0.045
        periodo = 12

        result = app.calcular_ahorro_programado(monto, interes, periodo)
        expected = 2507977.778
        self.assertAlmostEqual(expected, result, 2)
    
    def test_extraordinary_1(self):
        monto = 1000000
        interes = 0.02
        periodo = 1

        result = app.calcular_ahorro_programado(monto, interes, periodo)
        expected = 1019950
        self.assertAlmostEqual(expected, result, 2)
    
    def test_extraordinary_2(self):
        monto = 200000
        interes = 0.05
        periodo = 600

        result = app.calcular_ahorro_programado(monto, interes, periodo)
        expected = 125999980
        self.assertAlmostEqual(expected, result, 2)
    
    def test_extraordinary_3(self):
        monto = 500000
        interes = 1
        periodo = 12

        result = app.calcular_ahorro_programado(monto, interes, periodo)
        expected = 11999999
        self.assertAlmostEqual(expected, result, 2)
    
    def test_error_1(self):
        monto = 300000
        interes = -0.05
        periodo = 12

        with self.assertRaises( app.Invalidinterest ):
            app.calcular_ahorro_programado( monto, interes, periodo )
    
    def test_error_2(self):
        monto = 500000
        interes = 0.06
        periodo = -12

        with self.assertRaises( app.Invalidmonths ):
            app.calcular_ahorro_programado( monto, interes, periodo )
    
    def test_error_3(self):
        monto = 600000
        interes = 0
        periodo = 24

        with self.assertRaises( app.Invalidinterest ):
            app.calcular_ahorro_programado( monto, interes, periodo )
    
    def test_error_4(self):
        monto = 400000
        interes = 1.5
        periodo = 12

        with self.assertRaises( app.Invalidinterest ):
            app.calcular_ahorro_programado( monto, interes, periodo )
    
if __name__ == '__main__':
    unittest.main()