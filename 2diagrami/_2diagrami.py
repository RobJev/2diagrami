import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Формирование данных и построение диаграммы
x = np.arange(-9,0)
y = (-1/16)*(x+5)**2+2
x1 = np.arange(1,10)
y1 = (-1/16)*(x1-5)**2+2
x2 = np.arange(-9,0)
y2= 1/4*(x2+5)**2-3
x3 = np.arange(1,10)
y3 = 1/4*(x3-5)**2-3
x4 = np.arange(-9,-5)
y4 = -(x4+7)**2+5
x5 = np.arange(6,10)
y5 = -(x5-7)**2+5
x6 = np.arange(-1,2)
y6 = (-0.5)*(x6**2)+1.5

plt.title("Очки")
plt.xlabel("Ось абсцисс")
plt.ylabel("Ось ординат")
plt.grid(True)# Отображение сетки на координатной плоскости

plt.plot(x,y, '--r',linewidth=5,label="Очки")# График красного цвета
plt.plot(x1,y1, '--r',linewidth=5,label="Кит")
plt.plot(x2,y2, '--r',linewidth=5,label="Кит")
plt.plot(x3,y3, '--r',linewidth=5,label="Кит")
plt.plot(x4,y4, '--r',linewidth=5,label="Кит")
plt.plot(x5,y5, '--r',linewidth=5,label="Кит")
plt.plot(x6,y6, '--r',linewidth=5,label="Кит")

plt.savefig("my_image.png")  # Сохранение изображения или
plt.show()  # Вывод изображения на экран

title ="Население Эстонии"
fail=open("dannie.txt","r")
mas1=[]
mas2=[]
for line in fail:
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(int(line[n+1:len(line)].strip()))
fail.close()
plt.grid(True)
color_rectangle = np.random.rand(7, 3)
plt.barh(mas1, mas2, color=color_rectangle)
plt.show()
title = "Население Эстонии"
fig, (ax1, ax2) = plt.subplots(ncols=2)
fig.canvas.set_window_title(title)
fig.suptitle(title)
ax1.set_xlabel("Население Эстонии")
ax1.set_ylabel("")
ax2.set_xlabel("")
ax2.set_ylabel("Месяца")
data = [
    [1940, 1054000],
    [1960, 1209100],
    [1980, 1472190],
    [2000, 1401250],
    [2020, 1328976],
]
size = [x[1] for x in data]
nums = [x + 1 for x in range(len(size))]
tick_label = [x[0] for x in data]
ax1.bar(nums, size, tick_label=tick_label, width=0.5, color="#a500ff")
ax2.barh(nums, size, tick_label=tick_label, height=0.7, color="#ffa500")
plt.show()
title = "Население Эстонии"
fig, ax = plt.subplots()
fig.canvas.set_window_title(title)
# Настройки диаграммы и осей
ax.set_title(title)
ax.set_ylabel("Кол")
#
data = [1054000, 1209100, 1472190, 1401250, 1328976 ]
bins_to_be = 5# Количество интервалов разбиения
n, bins, patches = ax.hist(data, bins=bins_to_be,
                               color="blue", edgecolor="red")
# Вывод итоговых данных в легенду
res = ""
ax.legend([res.strip()])
plt.show()
