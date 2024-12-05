import sys

import pygame
import project.utils as utils


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        """
        屏幕上的点
        :param x: 横坐标，相对左上角
        :param y: 纵坐标，相对左上角
        """
        self.x = x
        self.y = y
    
    def set(self, x_or_pos: tuple[int, int] | int, y_or_None: int = None) -> None:
        """
        重设坐标。可以直接传入一个唯一参数set((x, y))元组，也可以传入两个参数set(x, y)
        """
        if x_or_pos is tuple:
            self.x = x_or_pos[0]
            self.y = x_or_pos[1]
        else:
            self.x = x_or_pos
            self.y = y_or_None


class Status:
    def __init__(self, name: str):
        """
        :param name: 监视状态的名称
        """
        self.name = name
        self._presentStatus = False
        self._shouldDeal = False
    
    def set(self, status: bool) -> None:
        """
        设置状态。应当仅在main.py的mainThread中调用。用于激活事件
        :param status: 设置为的值
        """
        self._presentStatus = status
        if status:
            self._shouldDeal = True
    
    def deal(self):
        """
        查看是否需要处理时调用
        :returns 如果需要处理，则返回True，随后将状态置为False
        """
        if self._shouldDeal:
            self._shouldDeal = False
            return True
        else:
            return False
    
    def peek(self):
        """
        需要处理时调用。
        :returns 如果需要处理，则返回True，但是不重置状态
        """
        return self._shouldDeal
    
    def __str__(self):
        return f'{self.name}: {self._presentStatus}'


_KeyCount = 256
mouse: Point = Point(0, 0)
left: Status = Status('left')
right: Status = Status('right')
keys: list[Status | None] = [Status('')] * _KeyCount
specialKeys: list[Status | None] = [Status('')] * _KeyCount
for i in pygame.__dict__:
    if not i.startswith('K_'):
        continue
    j = getattr(pygame, i)
    if j <= _KeyCount:
        keys[j].name = i[2:]
    else:
        specialKeys[j & (_KeyCount - 1)].name = i[2:]
utils.debug(f'keys长度{len(keys)}')

print(f'break {hex(pygame.K_BREAK)} pause {hex(pygame.K_PAUSE)}')
