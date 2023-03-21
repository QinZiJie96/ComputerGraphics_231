import pygame
import random
import pgu
from pgu import gui,timer

class TestDialog(gui.Dialog):
    def __init__(this):
        title = gui.Label("Some Dialog Box")
        label = gui.Label("Close this window to resume.")
        gui.Dialog.__init__(this, title, label)

pygame.init()
screencaption = pygame.display.set_caption('chess')
screen = pygame.display.set_mode((500, 500))
global a
a = 0
app = gui.App()                       #初始化gui
c = gui.Container(align=-1,valign=-1) #生成gui的容器
abc = TestDialog()                    #生成弹窗abc
btn = gui.Button("a")                 #生成文字为a的按钮
def add(self):
    global a
    a = a + 1
btn.connect(gui.CLICK, add, None)#将按钮与弹窗的弹出绑定
c.add(btn,0,0)                       #将按钮安放在容器(0,0)位置
app.init(c)

while True:
    for e in pygame.event.get():
        if e.type is pygame.QUIT:
            pygame.quit()
        else:
            app.event(e)    #将pygame的事件传递给pgu，很重要
    screen.fill((0,0,0))    #生成一个屏幕
    app.paint()             #将pgu容器的内容画出
    if a > 5:
        abc.open()
        a = 0
    pygame.display.update()

