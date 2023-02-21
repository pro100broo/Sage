import random

from hero_interface import AHero

from custom_exceptions import ZeroDamageError


class DamageMmanager:
    # Расчитывает урон автоатаки
    @staticmethod
    def auto_attack_damage(attacker: AHero) -> tuple[str, int]:
        # При нанесении 0 урона, вызывается исключение
        try:
            assert attacker.get_damage()
        except AssertionError:
            raise ZeroDamageError

        # Вероятность выпадения супер-атаки, рачистывается с помощью весов
        return random.choices(
            [
                ("default_hit", attacker.get_damage()), # Стандартная атака
                (attacker.get_super_attack().name, attacker.get_super_attack().damage) # Супер атака
            ], weights=[0.8, 0.2]
        )[0]

    # Расчитывает урон от дебаффа
    @staticmethod
    def de_buff_damage(defender: AHero) -> tuple[str, int]:
        try:
            # Если на героя действует дебафф, счётчик длительности эффекта уменьшается на 1 раунд и
            # возвращается текущая информация об эффекте, для логирования
            if defender.get_effects().de_buffs[0].duration:
                defender.decrement_de_buff_duration()
                return defender.get_effects().de_buffs[0].name, defender.get_effects().de_buffs[0].effect_power
            else:
                # Если счётчик длительности равен 0, действие дебаффа считается законченным
                # Сам дебаф удаляется из списка активных эфектов, возвращается соответствующая информация
                defender.update_de_buff()
                return "No de_buff", 0
        except IndexError:
            # При отсутстввии дебаффа, возвращается соответствующая информация
            return "No de_buff", 0

    # Работает про принципу метода для дебаффа
    @staticmethod
    def heal_value(defender: AHero) -> tuple[str, int]:
        try:
            if defender.get_effects().buffs[0].duration:
                defender.decrement_buff_duration()
                return defender.get_effects().buffs[0].name, defender.get_effects().buffs[0].effect_power
            else:
                defender.update_buff()
                return "No buff", 0
        except IndexError:
            return "No buff", 0
