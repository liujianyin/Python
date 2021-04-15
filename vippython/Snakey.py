#
# file:Snakey.py
#
import sys
import threading
import random
import time
import pygame


class Snakey:

    def __init__(self, Row=15, Column=20):
        pygame.init()  # pygame初始化
        self.score = 0
        self.Tx_font = pygame.font.SysFont('arial', 30)
        self.Row = Row
        self.Column = Column
        self.Side = 25
        self.screen = pygame.display.set_mode((Column * self.Side, Row * self.Side))  # 设置显示模式
        pygame.display.set_caption("Snakey")  # 设置窗口标题
        self.screen.fill((128, 128, 128), (0, 0, Column * self.Side, Row * self.Side))
        self.Tx_font = pygame.font.SysFont('arial', 20)
        self.body = [[random.randint(0, Column - 1), random.randint(0, Row - 1)]]
        food = [random.randint(0, Column - 1), random.randint(0, Row - 1)]
        while self.body.count(food) != 0:
            food = [random.randint(0, Column - 1), random.randint(0, Row - 1)]
        pygame.draw.rect(self.screen, (0, 255, 0), (food[0] * self.Side, food[1] * self.Side, self.Side, self.Side))
        self.direct = 0
        self.color = self.screen.get_at((self.Side // 2, self.Side // 2))
        """
        for i in range(self.Column+1):
            pygame.draw.line(self.screen, (0,0,0), (i*self.Side,0), (i*self.Side,Row*self.Side), 2)
        for i in range(self.Row+1):
            pygame.draw.line(self.screen, (0,0,0), (0,i*self.Side), (Column*self.Side,i*self.Side), 2)
        """
        pygame.draw.rect(self.screen, (0, 0, 0),
                         (self.body[0][0] * self.Side, self.body[0][1] * self.Side, self.Side, self.Side))
        pygame.display.flip()  # 刷新屏幕
        pygame.event.set_blocked([pygame.MOUSEMOTION, pygame.KEYUP])
        pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])
        self.clock = pygame.time.Clock()
        self.run()

    def run(self):
        while True:
            # timer=threading.Timer(1,self.run)
            self.clock.tick(4)  # 每秒循环5次
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # timer.cancel()
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:  # 键被按下
                    # pygame.draw.rect(self.screen,self.color,(self.body[0][0]*self.Side,self.body[0][1]*self.Side,self.Side,self.Side))

                    if event.key == pygame.K_LEFT:
                        if self.direct != 4:
                            self.direct = 3
                    elif event.key == pygame.K_RIGHT:
                        if self.direct != 3:
                            self.direct = 4
                    elif event.key == pygame.K_UP:
                        if self.direct != 2:
                            self.direct = 1
                    elif event.key == pygame.K_DOWN:
                        if self.direct != 1:
                            self.direct = 2
            self.move()
            # timer.start()

    def move(self):
        index = len(self.body) - 1
        pos_x = self.body[index][0]
        pos_y = self.body[index][1]
        if self.direct == 1:
            pos_y -= 1
        elif self.direct == 2:
            pos_y += 1
        elif self.direct == 3:
            pos_x -= 1
        elif self.direct == 4:
            pos_x += 1
        if pos_x < 0 or pos_x >= self.Column or pos_y < 0 or pos_y >= self.Row:
            self.screen.blit(self.Tx_font.render("SCORE:" + str(self.score), True, (255, 0, 0)), (10, 10))
            pygame.display.flip()  # 刷新屏幕
            time.sleep(5)
            pygame.quit()
            sys.exit()
        elif self.screen.get_at((pos_x * self.Side + self.Side // 2, pos_y * self.Side + self.Side // 2)) == (
        0, 255, 0):
            self.body.append([pos_x, pos_y])
            food = [random.randint(0, self.Column - 1), random.randint(0, self.Row - 1)]
            while self.body.count(food) != 0:
                food = [random.randint(0, self.Column - 1), random.randint(0, self.Row - 1)]
            pygame.draw.rect(self.screen, (0, 255, 0), (food[0] * self.Side, food[1] * self.Side, self.Side, self.Side))
            pygame.draw.rect(self.screen, (0, 0, 0), (pos_x * self.Side, pos_y * self.Side, self.Side, self.Side))
            pygame.display.flip()  # 刷新屏幕
            self.score += 1
        elif self.body.count([pos_x, pos_y]) != 0 and self.direct != 0:
            self.screen.blit(self.Tx_font.render("SCORE:" + str(self.score), True, (255, 0, 0)), (10, 10))
            pygame.display.flip()  # 刷新屏幕
            time.sleep(5)
            pygame.quit()
            sys.exit()
        else:
            pygame.draw.rect(self.screen, self.color,
                             (self.body[0][0] * self.Side, self.body[0][1] * self.Side, self.Side, self.Side))
            self.body.append([pos_x, pos_y])
            pygame.draw.rect(self.screen, (0, 0, 0), (pos_x * self.Side, pos_y * self.Side, self.Side, self.Side))
            self.body = self.body[1:len(self.body)]
            pygame.display.flip()  # 刷新屏幕


Snakey()
