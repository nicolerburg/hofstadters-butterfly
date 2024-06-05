import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation

def HMatrix(q, alpha, k_x, k_y):
    i = np.arange(0, q)
    a = 2 * np.cos(k_y - 2 * np.pi * alpha * i)
    ones = np.ones(q - 1)

    M = np.diag(a, k=0).astype(complex) + np.diag(ones, k=1) + \
        np.diag(ones, k=-1)

    b = q * 1.j * k_x
    c = 1 if q == 2 else 0
    M[q-1,   0] = np.exp(b) + c
    M[  0, q-1] = np.exp(-b) + c
    return M

def get_eigenvalues(p, q):
    alpha = p / q

    M_1 = HMatrix(q, alpha, 0, 0)
    M_2 = HMatrix(q, alpha, np.pi / q, np.pi / q)

    x_1 = np.linalg.eigvalsh(M_1)
    x_2 = np.linalg.eigvalsh(M_2)

    y = np.full(q, alpha)
    return x_1, x_2, y

def plot_eigenvalues(x_1, x_2, y):
    for x in zip(x_1, x_2):
        plt.plot(x, y[:2], '-', c='gray', linewidth=0.2)

    plt.plot(x_1, y, 'o', c='black', markersize=0.2)
    plt.plot(x_2, y, 'o', c='black', markersize=0.2)

def plot_butterfly(q_max):
    plt.title(r'Hofstadter Butterfly (q = ' + str(q_max) + ')')
    for q in range(1, q_max + 1):
      for p in range(1, q_max + 1):
          if q > p and np.gcd(p, q) == 1:# check that p and q are coprime
              x_1, x_2, y = get_eigenvalues(p, q)
              print("q",q)
              plot_eigenvalues(x_1, x_2, y)

def animate(i):
    q_max = i + 1
    print("q:", q_max)
    plot_butterfly(q_max)

def init_anim():
  print("Starting animation")

def init_plot():
  plt.rcParams["animation.html"] = "jshtml"
  plt.rcParams['figure.dpi'] = 150
  plt.ioff()
  fig, ax = plt.subplots()
  plt.xlabel(r'$\epsilon$', fontsize=15)
  plt.ylabel(r'$\alpha$', fontsize=15)
  plt.title(r'Hofstadter Butterfly')
  return fig

fig = init_plot()

q_max = 50

anim = matplotlib.animation.FuncAnimation(fig, animate, frames=q_max, init_func=init_anim, repeat=False)
#plot_butterfly(q_max)
#plt.show()
location = "C:/Users/Nicole/Desktop/butterfly/"
name = "butterfly_test.gif"
anim.save(location + name, writer='pillow', fps=10) 
plt.close() 