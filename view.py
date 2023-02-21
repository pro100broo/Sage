from heroes_factory import AHero

from logs import Logs, DuelLog, RoundLog, Opponent


# Класс логирования
class View:
    __session_logs = Logs(
        logs=[],
        errors=[],
        heroes=[]
    )

    # Логирование ошибок
    @staticmethod
    def error_log(text: str) -> None:
        View.__session_logs.errors.append(text)

    # Сохранение всех участников дуэли
    @staticmethod
    def heroes_log(hero: AHero) -> None:
        View.__session_logs.heroes.append(hero)

    # Начальное логирование дуэли
    # Записывается номер дуэли, информация о соперниках, добавляется пустой список раундов
    @staticmethod
    def initial_duel_log(hero1: AHero, hero2: AHero, duel_id: int) -> None:
        View.__session_logs.logs.append(
            DuelLog(
                duel_id=duel_id,
                opponents=[
                    Opponent(
                        class_name=hero1.get_class_name(),
                        damage=hero1.get_damage(),
                        health=hero1.get_hp()
                    ),
                    Opponent(
                        class_name=hero2.get_class_name(),
                        damage=hero2.get_damage(),
                        health=hero2.get_hp()
                    )
                ],
                rounds=[]
            )
        )

    # Логирование ударов
    # Записывается номер раунда, информация здоровье и нанесённом уроне
    @staticmethod
    def hit_log(hit_info: str, effects_info: str, health_info: str, duel_id: int,  round_id: int) -> None:
        View.__session_logs.logs[duel_id].rounds.append(
            RoundLog(
                round_id=round_id,
                hit_info=hit_info,
                effects_info=effects_info,
                health_info=health_info

            )
        )

    # Вывод лога сражения в консоль
    @staticmethod
    def get_duels_logs():
        print("\nЛог дуэлей:")
        # Последовательный вывод информации о каждой дуэли
        for _, duel in enumerate(View.__session_logs.logs):
            print(f"\nНомер дуэли: {duel.duel_id + 1}\n"
                  f"Противники:\n"
                  f"{duel.opponents[0].class_name}, {duel.opponents[0].health} hp, {duel.opponents[0].damage} dmg\n"
                  f"{duel.opponents[1].class_name}, {duel.opponents[1].health} hp, {duel.opponents[1].damage} dmg\n")

            # Последовательный вывод информации о каждом раунде
            for _, current_round in enumerate(duel.rounds):
                print(f"Раунд: {current_round.round_id + 1}\n"
                      f"{current_round.hit_info}\n"
                      f"{current_round.effects_info}\n"
                      f"{current_round.health_info}\n"
                      )

    # Вывод лога ошибок в консоль
    @staticmethod
    def get_errors_logs():
        # Последовательный вывод лога ошибок
        if View.__session_logs.errors:
            print("\nСписок ошибок:\n")
            print("\n".join(error for error in View.__session_logs.errors))
        # Если ошибок не было, выводится соответствующее сообщение
        else:
            print("\nОшибок не было")

    # Все герои сохраняются в логи. Это позволяет получить доступ ко всем героям и вывести рейтинг
    @staticmethod
    def get_heroes_rating():
        # Вывод рейтинга по результам турнира
        print("\nРейтинг участников турнира:")
        for index, hero in enumerate(View.__session_logs.heroes):
            print(f"\n{len(View.__session_logs.heroes) - index} место:\n"
                  f"{hero.get_name()}\n"
                  f"Класс: {hero.get_class_name()}. Урон: {hero.get_damage()}. Здоровье: {hero.get_hp()}")
