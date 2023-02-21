from view import View

# Импорт списка героев
from heroes_list import HeroesList

# Импорт интерфейса героя для подсказок типов
from hero_interface import AHero

# Импорт класса для подсчёта урона/лечения от разных источников
from damage_manager import DamageMmanager

# Импорт собственных классов исключений
from custom_exceptions import ZeroDamageError, OverDamageError, TwoFarmersError


# Главный класс, осуществляющий взаимодействие между героями
class Tournament:
    # Счётчики дуэлей и раундов в дуэлях необходимы для логирования
    __duels_counter = 0
    __rounds_counter = 0

    # Декоратор, для обновления нужных счётчиков, после завершения очереной дуэли
    @staticmethod
    def counters_wrapper(current_duel):
        def wrapper(*args, **kwargs):
            current_duel(args[0], args[1])

            # Счётчик дуэлей инкрементируется. Счётчик раундов обновляется
            Tournament.__increment_duels_counter()
            Tournament.__update_rounds_counter()

        return wrapper

    # Метод, запускающий турнир
    @staticmethod
    def tournament_init():
        # Сражения происходят до тех пор, пока в списке не останется один герой
        while heroes_list.heroes_remaining() >= 2:
            # В очередную дуэль поступают два героя. Метод возвращает победителя (с полным здоровьем)
            Tournament.__duel(heroes_list.get_hero(), heroes_list.get_hero())

        # Логирование победителя турнира
        View.heroes_log(heroes_list.get_hero())

    # Метод, запускающий очередную дуэль
    @staticmethod
    @counters_wrapper
    def __duel(hero1: AHero, hero2: AHero) -> None:
        assert isinstance(hero1, AHero) and isinstance(hero2, AHero), "В дуэль попали неправильные инстансы"

        # Производится начальное логирование дуэли: общая информация о соперниках, номере дуэли.
        # Подробную информацию смотрите в файле view.py
        View.initial_duel_log(hero1, hero2, Tournament.get_duels_counter())
        while True:
            # Состояние героев проверяется после каждого удара
            # Если здоровье героя, после очередного удара <= 0, он считается проигравшим
            # На этом моменте, дуэль считается оконченной. Победитель восполняет здоровье и возвращается
            # в общий список. Проигравший участник логируется

            if Tournament.__next_hit(hero1, hero2):
                return None
            if Tournament.__next_hit(hero2, hero1):
                return None

            # После каждых двух ударов, счётчик раунда инкрементируется
            Tournament.__increment_rounds_counter()

    # Метод осуществляет удары героев
    @staticmethod
    def __next_hit(defender: AHero, attacker: AHero):
        try:
            Tournament.__hit_event(defender, attacker)
        except OverDamageError:
            heroes_list.add_hero(Tournament.__update_stats(attacker, defender))
            return 1
        except ZeroDamageError:
            View.error_log(f"В дуэль №{Tournament.get_duels_counter()} попал крестьянин {attacker.get_name()}")
            heroes_list.add_hero(Tournament.__update_stats(defender, attacker))
            return 1
        except TwoFarmersError:
            View.error_log(f"В дуэль №{Tournament.get_duels_counter()} попало два крестьянина")
            View.heroes_log(defender)
            View.heroes_log(attacker)
            return 1

    @staticmethod
    def __hit_event(defender: AHero, attacker: AHero) -> None:

        try:
            # При попадании в дуэль двух крестьян, вызывается исключение
            assert not (not defender.get_damage() and not attacker.get_damage())
        except AssertionError:
            raise TwoFarmersError

        # Добавление баффа/дебаффа с определённым шансом
        defender.set_effects(attacker)

        # Получение информации об автоатаке для логирования
        hit_name, hit_damage = dmg_manager.auto_attack_damage(attacker)

        # Получение информации о дебаффе для логирования
        de_buff_name, de_buff_damage = dmg_manager.de_buff_damage(defender)

        # Получение информации о баффе для логирования
        buff_name, heal = dmg_manager.heal_value(defender)

        # Подсчёт общего урона и здоровья (до изменения), для простоты логирования
        total_damage = hit_damage + de_buff_damage - heal
        previous_hp = defender.get_hp()

        # Изменение здоровья, с учётом суммарного урона
        defender.set_hp(total_damage)

        # Производится логирование удара:
        # Подробную информацию смотрите в файле view.py
        View.hit_log(
            f"{attacker.get_class_name()}: {hit_name} ({hit_damage} dmg) -> {defender.get_class_name()}",
            f"Debuff: {de_buff_name} (-{de_buff_damage} hp)\n"
            f"Buff: {buff_name} (+{heal} hp)\n"
            f"Total damage: {hit_damage + de_buff_damage}, "
            f"with a heal: {total_damage if hit_damage + de_buff_damage >= heal else -total_damage}",
            f"{defender.get_class_name()} hp: {previous_hp} -> {defender.get_hp()}",
            Tournament.get_duels_counter(),
            Tournament.get_rounds_counter()
        )

    @staticmethod
    def __update_stats(winner: AHero, loser: AHero) -> AHero:
        # Проигравший логируется, прдварительно восстановиви здоровье
        loser.update_hp()
        assert loser.get_hp() == loser.get_default_hp(), f"Здоровье не было восстановлено у {loser.get_class_name()}"

        View.heroes_log(loser)

        # Победитель восстанавливает все параметры и возвращается в список героев
        winner.update_hp()
        assert winner.get_hp() == winner.get_default_hp(), f"Здоровье не было восстановлено у {winner.get_class_name()}"

        winner.update_buff()
        assert not winner.get_effects().buffs, f"Список баффов не был обновлен у {winner.get_class_name()}"

        winner.update_de_buff()
        assert not winner.get_effects().de_buffs, f"Список дебаффов не был обновлену {winner.get_class_name()}"

        return winner


    # Метод возвращает счётчик дуэлей
    @staticmethod
    def get_duels_counter() -> int:
        return Tournament.__duels_counter

    # Метод инкрементирует счётчик дуэлей
    @staticmethod
    def __increment_duels_counter() -> None:
        Tournament.__duels_counter += 1

    # Метод возвращает счётчик раундов
    @staticmethod
    def get_rounds_counter() -> int:
        return Tournament.__rounds_counter

    # Метод инкрементирует счётчик раундов
    @staticmethod
    def __increment_rounds_counter() -> None:
        Tournament.__rounds_counter += 1

    # Метод обновляет счётчик раундов
    @staticmethod
    def __update_rounds_counter() -> None:
        Tournament.__rounds_counter = 0


if __name__ == "__main__":
    # Инициализация списка героев
    heroes_list = HeroesList()
    heroes_list.create_hero_list(10)

    assert heroes_list.heroes_remaining() == 10, "Что-то пошло не так. Список заполнен не полностью!"

    # Инициализация менеджера урона
    dmg_manager = DamageMmanager()

    # Инициализация турнира
    tournament = Tournament()
    tournament.tournament_init()

    # Вывод логов в консоль
    View.get_duels_logs()
    View.get_heroes_rating()
    View.get_errors_logs()

