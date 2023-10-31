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
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_asettuu_nollaksi(self):
        varasto = Varasto(-2)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo_asettuu_nollaksi(self):
        varasto = Varasto(10,-2)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_negatiivinen_lisays_ei_tee_mitaan(self):
        self.varasto.lisaa_varastoon(-3)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_liian_suuri_lisays_asettaa_saldon_tilavuuden_arvoksi(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivinen_otto_palauttaa_nollan(self):
        otto = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(otto, 0.0)

    def test_saldon_ylittava_otto_tyhjentaa_varaston(self):
        self.varasto.lisaa_varastoon(5)
        otto = self.varasto.ota_varastosta(500)
        self.assertAlmostEqual(otto, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varaston_merkkijono_esitys_tulostuu_oikein(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
