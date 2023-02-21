import random

# Импорт пресетов героев
from heroes_presets import KnightPresets, ArcherPresets, MagePresets, FarmerPresets

# Импорт интерфейса и абстрактного класса героя
from hero_interface import IHero, AHero

# Имплементации героев
class Archer(AHero):
    def __init__(self, presets):
        super().__init__(presets, class_name="Archer")


class Knight(AHero):
    def __init__(self, presets):
        super().__init__(presets, class_name="Knight")


class Mage(AHero):
    def __init__(self, presets):
        super().__init__(presets, class_name="Mage")


class Farmer(AHero):
    def __init__(self, presets):
        super().__init__(presets, class_name="Farmer")


# Общий интерфейс фабрики героя
class AFactory:
    # Метод создаёт героя
    @staticmethod
    def create_hero() -> IHero:
        return random.choice(
            [
                Archer(ArcherPresets()),
                Knight(KnightPresets()),
                Mage(MagePresets()),
                Farmer(FarmerPresets())
             ]
        )

# Имплементация фабрики
class Factory(AFactory):
    def __init__(self):
        super().__init__()


# Функция, осуществляющая управление фабриками
def activate_factory() -> IHero:
    factory = Factory()
    return factory.create_hero()
