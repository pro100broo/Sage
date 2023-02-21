import random

from heroes_info import HeroInfo, ActiveEffects, SuperAttack, Effect

from heroes_presets import APreset

# Импорт собственных классов исключений
from custom_exceptions import OverDamageError

# Общий интерфейс для героя
class IHero:
    __info: HeroInfo
    __class_name: str
    __class_default_hp: int

# Абстрактный класс для героя
class AHero(IHero):
    def __init__(self, presets: APreset, class_name: str):
        self.__class_name = class_name
        self.__default_hp = presets.get_preset_hp()
        self.__info = HeroInfo(
            name=presets.get_preset_name(),
            hp=presets.get_preset_hp(),
            damage=presets.get_preset_damage(),
            super_attacks=presets.get_preset_super_attack(),
            buff=presets.get_preset_buff(),
            de_buff=presets.get_preset_de_buff(),
            active_effects=ActiveEffects(buffs=[], de_buffs=[])
        )

    # Метод возвращает имя героя
    def get_name(self) -> str:
        return self.__info.name

    # Метод возвращает здоровье героя
    def get_hp(self) -> int:
        return self.__info.hp

    # Метод возвращает здоровье из пресета
    def get_default_hp(self) -> int:
        return self.__default_hp

    # Метод возвращает урон героя
    def get_damage(self) -> int:
        return self.__info.damage

    # Метод возвращает название класса героя
    def get_class_name(self) -> str:
        return self.__class_name

    # Метод возвращает бафф из списка возможных баффов героя
    def get_buff(self) -> Effect:
        return self.__info.buff

    # Метод возвращает дебафф из списка возможных дебаффов героя
    def get_de_buff(self) -> Effect:
        return self.__info.de_buff

    # Метод возвращает данные суператаки
    def get_super_attack(self) -> SuperAttack:
        return self.__info.super_attacks

    # Метод возвращает список активных эффектов
    def get_effects(self) -> ActiveEffects:
        return self.__info.active_effects

    # Метод добавляет бафф/дебафф в список активных эффектов героя
    def set_effects(self, attacker) -> None:
        # Получение дебаффа, с определённым шансом
        if not self.get_effects().buffs and random.choices([0, 1], weights=[.6, .4])[0]:
            self.__info.active_effects.buffs.append(self.get_buff())

        # Получение баффа, с определённым шансом
        if not self.get_effects().de_buffs and random.choices([0, 1], weights=[.8, .2])[0]:
            self.__info.active_effects.de_buffs.append(attacker.get_de_buff())

    # Метод уменьшает длительность активного баффа на 1 раунд
    def decrement_buff_duration(self) -> None:
        self.__info.active_effects.buffs[0].duration -= 1

    # Метод уменьшает длительность активного дебаффа на 1 раунд
    def decrement_de_buff_duration(self) -> None:
        self.__info.active_effects.de_buffs[0].duration -= 1

    # Метод изменяет здоровье героя
    def set_hp(self, enemy_damage: int) -> None:
        try:
            # При нанесении смертельного урона, вызывается исключение
            assert self.__info.hp > enemy_damage
        except AssertionError:
            raise OverDamageError
        else:
            # Если исключение не было вызывано, здоровье изменяется
            self.__info.hp -= enemy_damage

    # Обновляет здоровье героя, при выходе из дуэли
    def update_hp(self) -> None:
        self.__info.hp = self.__default_hp

    # Очищает список баффов героя
    def update_buff(self) -> None:
        self.__info.active_effects.buffs = []

    # Очищает список дебаффов героя
    def update_de_buff(self) -> None:
        self.__info.active_effects.de_buffs = []