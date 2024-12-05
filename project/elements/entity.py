from enum import Enum
import project.elements.item as item


class EntityType(Enum):
    EGG = 0
    CHICKEN = 1
    PLAYER = 2


class Entity:
    def __init__(this, entityType: EntityType):
        this.x = 0
        this.y = 0
        this.type = entityType
        this.pack: item.BackPack = item.BackPack()
    
    def tick(self): ...


entities: list[Entity] = []


def tick():
    for entity in entities:
        entity.tick()

