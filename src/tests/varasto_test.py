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

    def test_negatiiviset_alkuarvot_asetetaan_nollaksi(self):
        self.varasto = Varasto(-1, -2)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_tilavuutta_suurempi_alkusaldo_tasataan_tilavuuteen(self):
        self.varasto = Varasto(5, 10)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_negatiivinen_lisays_ei_muuta_tilannetta(self):
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liian_iso_lisays_asetttaa_varaston_taydeksi(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_otto_ei_poista_varastosta(self):
        self.varasto.lisaa_varastoon(2)
        otettu = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(otettu, 0)
        self.assertAlmostEqual(self.varasto.saldo, 2)

    def test_saldon_ylittava_otto_tyhjentaa_varaston(self):
        self.varasto.lisaa_varastoon(5)
        otettu = self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(otettu, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_merkkijonoesitys_oikein(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
