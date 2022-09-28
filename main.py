import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import random
from csvReader import gotWorld

# 1隨機 2 CSV
mode = int(input("Please input your mode : "))

if mode == 1:
    WIDTH = int(input("Please input your row and col : ")) ; LENGTH = WIDTH
    world = []
    for i in range(LENGTH):
        world.append( [random.randint(0,1) for j in range(WIDTH)] )

elif mode == 2 :
    world,WIDTH,LENGTH = gotWorld()

day = 0
generationText = "Generation"

def next_generation(): #下個世代
    for i in range(LENGTH):
        for j in range(WIDTH):
            
            #串列走訪
            life_nearby = 0 #此變數用來表示附近生物數量
            if i != 0:
                if world[i-1][j] in [1,-1]:
                    life_nearby += 1
            if i != LENGTH-1:
                if world[i+1][j] in [1,-1]:
                    life_nearby += 1
            if j != WIDTH-1:
                if world[i][j+1] in [1,-1]:
                    life_nearby += 1
            if j != 0:
                if world[i][j-1] in [1,-1]:
                    life_nearby += 1
            if i != 0 and j != 0:
                if world[i-1][j-1] in [1,-1]:
                    life_nearby += 1
            if i != 0 and j != WIDTH-1:
                if world[i-1][j+1] in [1,-1]:
                    life_nearby += 1
            if i != LENGTH-1 and j != 0:
                if world[i+1][j-1] in [1,-1]:
                    life_nearby += 1
            if i != LENGTH-1 and j != WIDTH-1:
                if world[i+1][j+1] in [1,-1]:
                    life_nearby += 1

            #即將死亡改成「-1」 即將出生改成「2」
            if life_nearby<2 and world[i][j]==1:
                world[i][j] = -1
            elif 2<=life_nearby<=3 and world[i][j]==1:
                pass
            elif life_nearby>3 and world[i][j]==1:
                world[i][j] = -1
            elif life_nearby==3 and world[i][j]==0:
                world[i][j] = 2
            
def finish():          #世代結束，將-1改成0 將2改成1
    for i in range(LENGTH):
        for j in range(WIDTH):
            if world[i][j] == 2:
                world[i][j] = 1
            elif world[i][j] == -1:
                world[i][j] = 0

def animate(self): #matplotlib animation用法
    global day,world

    generationText = "Generation " + str(day) #generationText字串，用於顯示
    next_generation()
    finish()
    plt.cla() #清除上次的圖像
    plt.title("Conway's Game of Life - NSYSU")
    plt.text(-2,2,generationText,ha="right",wrap=True) #顯示generationText
    world_np = np.array(world) #創建np.array以利matplotlib使用
    plt.imshow(world_np)

    print("Generation",day)
    day += 1


fig = plt.figure() #創建figure
world_np = np.array(world) #創建np.array以利matplotlib使用
animator = ani.FuncAnimation(fig, animate, interval = 500) #matplotlib animation用法
plt.imshow(world_np)  
plt.title("Conway's Game of Life - NSYSU") #標題名稱
generationText = "Generation " + str(day) #generationText字串，用於顯示
plt.text(-2,2,generationText,ha="right",wrap=True) #顯示generationText
plt.show() #顯示圖表
