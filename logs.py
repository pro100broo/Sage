from pydantic import BaseModel


# Представление логов раунда
class RoundLog(BaseModel):
    round_id: int
    hit_info: str
    effects_info: str
    health_info: str



# Представление информации о герое
class Opponent(BaseModel):
    class_name: str
    damage: int
    health: int


# Представление логов дуэли
class DuelLog(BaseModel):
    duel_id: int
    opponents: list[Opponent, Opponent]
    rounds: list[RoundLog]


# Общее представление логов (дуэли + ошибки)
class Logs(BaseModel):
    logs: list[DuelLog]
    errors: list[str]
    heroes: list







