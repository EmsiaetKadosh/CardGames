import pygame
import project.utils as utils


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
    
    def set(self, x_or_pos: tuple[int, int] | int, y_or_None: int = None) -> None:
        if x_or_pos is tuple:
            self.x = x_or_pos[0]
            self.y = x_or_pos[1]
        else:
            self.x = x_or_pos
            self.y = y_or_None


class Status:
    def __init__(self, name: str):
        self.name = name
        self._presentStatus = False
        self._shouldDeal = False
    
    '''
    该函数应当仅在main.py的mainThread中调用。用于激活事件。
    '''
    
    def set(self, status: bool):
        self._presentStatus = status
        if status:
            self._shouldDeal = True
    
    '''
    需要处理时调用。
    :returns 如果需要处理，则返回True，随后将状态置为False。
    '''
    
    def deal(self):
        if self._shouldDeal:
            self._shouldDeal = False
            return True
        else:
            return False
    
    '''
    需要处理时调用。
    :returns 如果需要处理，则返回True。不改变状态。
    '''
    
    def peek(self):
        return self._shouldDeal
    
    def __str__(self):
        return f'{self.name}:{self._presentStatus}'


mouse: Point = Point(0, 0)
left: Status = Status('left')
right: Status = Status('right')
keys: list[Status | None] = [None] * 256
specialKeys: list[Status | None] = [None] * 256
for i in pygame.__dict__:
    if i.startswith('K_'):
        j = getattr(pygame, i)
        if j <= 256:
            keys[j] = Status(i[2:])
        else:
            specialKeys[j & 0xff] = Status(i[2:])
for i in keys:
    print(i)
print('\n')
for i in specialKeys:
    print(i)
utils.debug(f'keys长度{len(keys)}')
