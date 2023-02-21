from pydantic import BaseModel


# Представление баффов/дебаффов
class Effect(BaseModel):
    name: str
    effect_power: int
    duration: int


# Представление супер-атаки
class SuperAttack(BaseModel):
    name: str
    damage: int


# Представление активных баффов/дебаффов
class ActiveEffects(BaseModel):
    buffs: list[Effect]
    de_buffs: list[Effect]


# Представление набора характеристик героя
class HeroInfo(BaseModel):
    name: str
    hp: int
    damage: int
    super_attacks: SuperAttack
    buff: Effect
    de_buff: Effect
    active_effects = ActiveEffects(buffs=[], de_buffs=[])








