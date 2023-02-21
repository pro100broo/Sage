import random

# Импорт представления супер атаки героя
from heroes_info import SuperAttack, Effect

# Интерфейс для пресетов всех характеристик классов героев
class IPreset:
    __names: list[str]
    __hp: int
    __damage: int
    __super_attacks: list[SuperAttack]
    __buffs: list[Effect]
    __de_buffs: list[Effect]

# Абстрактный класс пресетов
class APreset(IPreset):
    # Список настраиваемых атрибутов
    def __init__(self, names: list[str], hp: int, damage: int, super_attacks: list[SuperAttack], buffs: list[Effect],
                 de_buffs: list[Effect]):
        self.__names = names
        self.__hp = hp
        self.damage = damage
        self.__super_attacks = super_attacks
        self.__buffs = buffs
        self.__de_buffs = de_buffs


    # Метод возвращает имя из списка имён
    def get_preset_name(self) -> str:
        return random.choice(self.__names)

    # Метод возвращает здоровье
    def get_preset_hp(self) -> int:
        return self.__hp

    # Метод возвращает урон
    def get_preset_damage(self) -> int:
        return self.damage

    # Метод возвращает супер атаку
    def get_preset_super_attack(self) -> SuperAttack:
        return random.choice(self.__super_attacks)

    # Метод возвращает бафф
    def get_preset_buff(self) -> Effect:
        return random.choice(self.__buffs)

    # Метод возвращает дебафф
    def get_preset_de_buff(self) -> Effect:
        return random.choice(self.__de_buffs)

# Имплементации настроек для каждого класса героев:
class ArcherPresets(APreset):
    def __init__(self):
        super().__init__(
            names=["Rogerin the Clumsy", "Ralphwolf the Shepherd", "Thoma of the North", "Fulbert the Heroic",
                   "Nob the Noble", "Sewell the Strong", "Willelmus the Black", "Charlot the Lion"],
            hp=150,
            damage=random.randint(5, 10),
            super_attacks=[
                SuperAttack(name="Power shot", damage=35),
                SuperAttack(name="Rain of arrows", damage=45)
            ],
            buffs=[
                Effect(name="holy_water",effect_power=5,duration=5),
                Effect(name="holy_power",effect_power=15,duration=3)
            ],
            de_buffs=[
            Effect(name="poisoned_arrow",effect_power=5,duration=5),
            Effect(name="fire_arrow",effect_power=15,duration=2)
            ]
        )


class KnightPresets(APreset):
    def __init__(self):
        super().__init__(
            names=["Nicolas the Harbinger", "Farmanus the Brown", "Neal the Cute", "Fulk the Rude", "Noe the Heroic",
                   "Pawelinus the Clever", "Imbart the Bold", "Charles the Red"],
            hp = 200,
            damage=random.randint(10, 15),
            super_attacks=[
                SuperAttack(name="Shield crash", damage=40),
                SuperAttack(name="Execute", damage=60)
            ],
            buffs=[
                Effect(name="holy_water", effect_power=5, duration=5),
                Effect(name="holy_power", effect_power=15, duration=3)
            ],
            de_buffs=[
                Effect(name="bleeding", effect_power=10, duration=3)
            ]
        )


class MagePresets(APreset):
    def __init__(self):
        super().__init__(
            names=["Evrouin the Handsome", "Raullin the Twisted", "Yvon the Jackal", "Niall the Friend",
                   "Huon the Huge", "Addie the Magnificent", "Wymark the Demon", "Elyes the Keeper"],
            hp = 100,
            damage=random.randint(15, 20),
            super_attacks=[
                SuperAttack(name="Pyro blast", damage=50),
                SuperAttack(name="Arcane blast", damage=70)
            ],
            buffs=[
                Effect(name="holy_water", effect_power=5, duration=5),
                Effect(name="holy_power", effect_power=15, duration=3)
            ],
            de_buffs=[
                Effect(name="magical_exhaustion",effect_power=7,duration=5)
            ]
        )



class FarmerPresets(APreset):
    def __init__(self):
        super().__init__(
            names=["Peter", "Cedric", "Mike", "Luke"],
            hp=50,
            damage=0,
            super_attacks=[
                SuperAttack(name="Shovel strike", damage=1),
                SuperAttack(name="Pitchfork strike", damage=2)
            ],
            buffs=[
                Effect(name="earth_force", effect_power=5, duration=10),
                Effect(name="crowd_support", effect_power=7, duration=5),
            ],
            de_buffs=[
                Effect(name="Look what's there!!!?", effect_power=1, duration=1)
            ]
        )
