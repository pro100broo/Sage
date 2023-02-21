# Общий класс ошибок
class Error(Exception):
    pass

# Вызывается при нанесении 0 урона
class ZeroDamageError(Error):
    pass

# Вызывается при смертельного (в том числе и отрицательного) урона
class OverDamageError(Error):
    pass

# Вызывается при попадании двух фермеров в дуэль
class TwoFarmersError(Error):
    pass