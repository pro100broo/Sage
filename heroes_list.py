from view import View

# Импорт фабрики, а так же интерфейса героя для подсказки типов
from heroes_factory import activate_factory

# Импорт интерфейса и абстрактного класса героя
from hero_interface import IHero, AHero

# Класс организует изменение списка героев
class HeroesList:
    __queue = []

    # Заполнение списка героями
    @staticmethod
    def create_hero_list(participants: int):
        # Проверка введённых данных
        if isinstance(participants, int) and participants > 0:
            for _ in range(participants):
                HeroesList.add_hero(activate_factory())
        else:
            View.error_log(f"Not enough participants or TypeError: {participants}")

    # Метод вытаскивает героя из списка героев
    @staticmethod
    def get_hero() -> AHero:
        try:
            return HeroesList.__queue.pop()
        # Обработка IndexError:
        except IndexError:
            View.error_log("Pop from empty list") if not HeroesList.__queue else View.error_log("Pop unexciting index")

    # Метод добавляет героя в список героев
    @staticmethod
    def add_hero(hero: IHero) -> None:

        assert isinstance(hero, IHero), "В список пытается попасть другой объект"
        HeroesList.__queue.append(hero)

    # Метод возвращает кол-во героев, оставшихся в списке
    @staticmethod
    def heroes_remaining() -> int:
        return len(HeroesList.__queue)


