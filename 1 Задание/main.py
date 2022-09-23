import numpy as np
import matplotlib.pyplot as plt

firstRange = np.random.randint(26, 31, size = 30)
secondRange = np.random.randint(50, 71, size = 30)

abscissa = np.arange(1, 31)

np.random.shuffle(firstRange)
np.random.shuffle(secondRange)

fig1, ax1 = plt.subplots()
ax1.plot(abscissa, firstRange, label='Доллар')
ax1.set_xlabel('Дни месяца (д)')
ax1.set_ylabel('Курс ($)')
ax1.legend(loc='best')
ax1.set_title('Курс доллара в апреле 2020 года', fontsize=20)
plt.show()

fig2, ax2 = plt.subplots()
ax2.plot(abscissa, secondRange, label='Доллар')
ax2.set_xlabel('Дни месяца (д)')
ax2.set_ylabel('Курс ($)')
ax2.legend(loc='best')
ax2.set_title('Курс доллара в апреле 2018 года', fontsize=20)
plt.show()