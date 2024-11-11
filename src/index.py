from varasto import Varasto


def display_varasto_status(varasto, name):
    print(f"{name} varasto: {varasto}")


def test_varasto_creation():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def perform_mehu_operations(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    display_varasto_status(mehua, "Mehu")

    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    display_varasto_status(mehua, "Mehu")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    display_varasto_status(mehua, "Mehu")


def perform_olut_operations(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    display_varasto_status(olutta, "Olut")

    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    display_varasto_status(olutta, "Olut")


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    display_varasto_status(mehua, "Mehu")
    display_varasto_status(olutta, "Olut")

    perform_olut_operations(olutta)
    perform_mehu_operations(mehua)
    test_varasto_creation()

    print(f"Olutvarasto: {olutta}")
    print(f"Mehuvarasto: {mehua}")


if __name__ == "__main__":
    main()
