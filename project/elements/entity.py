from enum import Enum
import project.elements.item as item


class EntityType(Enum):
    EGG = 0
    CHICKEN = 1
    PLAYER = 2


class Entity:
    def __init__(self, entityType: EntityType, hitBlock: float):
        """
        :param entityType: 实体类型
        :param hitBlock: 碰撞体积大小
        """
        self._x: float = 0
        self._y: float = 0
        self._type = entityType
        self._speed: float = 0
        self._hitBlock = float
        
    def passTick(self) -> None:
        """
        内置函数，不应当额外调用，不应当随意重写。
        重写时必须注意调用父类的同名函数，防止遗漏逻辑。
        """
        pass
    
    def tick(self) -> None:
        """
        交由具体类重写
        """
        pass
    
    def getX(self) -> float:
        """
        :return: x坐标
        """
        return self._x
    
    def getY(self):
        """
        :return: y坐标
        """
        return self._y
    
    def getType(self):
        """
        :return: 实体类型
        """
        return self._type


entities: list[Entity] = []


def tick() -> None:
    """
    不应调用。应当有且仅有一个调用点，位于main.py，gameThread()
    """
    for entity in entities:
        entity.tick()


class Player(Entity):
    def __init__(self):
        """
        创建玩家
        """
        super().__init__(EntityType.PLAYER, 0.5)
        self.health = 100
        self.maxHealth = 100
        self.name = 'Player'
        self.inventory = item.BackPack()

