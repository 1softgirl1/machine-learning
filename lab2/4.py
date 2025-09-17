import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Внутренние вычисления с обработкой особых случаев
    sin_sq = np.sin(x) ** 2
    denominator = 1 + sin_sq
    tan_arg = 1 / denominator

    # Избегаем деления на ноль и недопустимых значений
    mask = denominator != 0
    tan_val = np.zeros_like(x)
    tan_val[mask] = np.tan(tan_arg[mask])

    # Основание логарифма
    log_base = 1 + tan_val

    # Проверяем допустимость основания логарифма
    valid_log = (log_base > 0) & (log_base != 1) & (x ** 2 + 1 > 0)

    # Вычисляем логарифм только для допустимых значений
    log_part = np.zeros_like(x)
    log_part[valid_log] = np.log(x[valid_log] ** 2 + 1) / np.log(log_base[valid_log])

    # Экспоненциальная часть
    exp_part = np.exp(-np.abs(x) / 10)
    return log_part * exp_part


x = np.linspace(-10, 10, 10000)
y = f(x)
plt.figure(figsize=(12, 8))

plt.plot(x, y, 'b-', linewidth=1.5,
         label=r'$y(x) = \log_{1+\tan\left(\frac{1}{1+\sin^2(x)}\right)}(x^2+1) \cdot \exp\left(-\frac{|x|}{10}\right)$')


plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$y(x)$', fontsize=14)
plt.title(
    r'График функции $\log_{1+\tan\left(\frac{1}{1+\sin^2(x)}\right)}(x^2+1) \cdot \exp\left(-\frac{|x|}{10}\right)$',
    fontsize=16, pad=20)

plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)

plt.xlim(-10, 10)
plt.ylim(-5, 5)

plt.tight_layout()

plt.show()
