import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_volume_cannot_be_negative(self):
        varasto = Varasto(-10)

        self.assertAlmostEqual(varasto.tilavuus, 0)
    
    def test_initial_saldo_cannot_be_negative(self):
        varasto = Varasto(10,-10)

        self.assertAlmostEqual(varasto.saldo, 0)

    def test_cannot_add_negative_amount(self):
        self.varasto = Varasto(10)

        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_cannot_add_more_than_maximum_volume(self):
        self.varasto = Varasto(10)

        self.varasto.lisaa_varastoon(100)

        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_cannot_take_out_negative_amount_from_storage(self):
        self.varasto = Varasto(10,10)

        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)

    def test_cannot_take_out_more_than_is_in_the_storage(self):
        self.varasto = Varasto(10,10)

        self.assertAlmostEqual(self.varasto.ota_varastosta(100), 10)

    def test_str_function_works(self):
        self.varasto = Varasto(10,10)

        self.assertEqual(str(self.varasto), "saldo = 10, vielä tilaa 0")
