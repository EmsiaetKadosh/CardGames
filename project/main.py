from sys import stderr

import pygame
import utils
import threading
import interact.interact as interact
import elements.entity as entity
import elements.item as item
import traceback


def gameThread():
    entity.tick()


def mainThread():
    threading.Thread(name="GameThread", target=gameThread())
    info = pygame.display.Info()
    pygame.display.set_mode((info.current_w / 2, info.current_h / 2))
    while True:
        try:
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        utils.info("退出游戏消息")
                        return
                    case pygame.KEYDOWN:
                        print(hex(event.key))
                        interact.keys[event.key] = True
                        break
                    case pygame.KEYUP:
                        interact.keys[event.key] = False
                        break
                    case pygame.MOUSEMOTION:
                        interact.mouse.set(event.pos)
                        break
                    case pygame.MOUSEBUTTONDOWN:
                        print(event.__dict__)
                        interact.left.set(True)
                        break
                    case pygame.MOUSEBUTTONUP:
                        interact.left.set(False)
                        break
        except Exception as e:
            utils.printException(e)


if __name__ == '__main__':
    ret = pygame.init()
    utils.info(f"pygame初始化。成功{ret[0]}模块，失败{ret[1]}模块")
    utils.info("主线程启动")
    mainThread()
    utils.info("终止游戏")
    pygame.quit()
