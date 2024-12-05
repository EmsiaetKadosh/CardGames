class Breakable:
    def __init__(this, durability: int, maxDurability: int):
        this.durability = durability
        this.maxDurability = maxDurability
        
    def fix(this, amount: int) -> None:
        this.durability += amount
        if this.maxDurability > 0:
            this.durability = min(this.durability, this.maxDurability)
    
            
class WeaponLike(Breakable):
    def __init__(this, damage: int, durability: int, maxDurability: int):
        super().__init__(durability, maxDurability)
        this.damage = damage
        
    def onDamage(this) -> None:
        pass

    def onBreak(this) -> None:
        pass


class Item:
    def __init__(this, name: str, description: str):
        this.name = name
        this.description = description


class Weapon(Item, WeaponLike):
    def __init__(this, name: str, description: str):
        super().__init__(name, description)


class ItemStack:
    def __init__(this, item: Item, count: int = 1):
        this.item = item
        this.count = 1
        
        
class Inventory:
    def __init__(this, count: int):
        this.__items = [None for i in range(count)]
        this.__count = count
    
    def get(this, offset: int):
        if this.__count <= offset:
            raise IndexError()
        
        
class BackPack(Inventory):
    def __init__(this):
        super().__init__(32)

