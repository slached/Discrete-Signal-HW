import matplotlib.pyplot as plt
import numpy as np

n = np.arange(-20, 20)

x = 0.8**n
y = (0.9**n) * np.sin(2 * np.pi * n / 10)

fig, axes = plt.subplots(
    ncols=2,
    nrows=1,
    figsize=(14, 6),
    layout="constrained",
)
axs = axes.ravel()

axs[0].set_xlabel("Sample index")
axs[0].set_ylabel("Amplitude")
axs[0].stem(
    n,
    x,
    linefmt="grey",
    markerfmt="bo",
    basefmt="k-",
)
axs[0].set_title("Discrete Signal a: $x[n] = 0.8^n$")

axs[1].set_xlabel("Sample index")
axs[1].set_ylabel("Amplitude")
axs[1].stem(
    n,
    y,
    linefmt="grey",
    markerfmt="ro",
    basefmt="k-",
)
axs[1].set_title("Discrete Signal b: $x[n] = (0.9^n) \\sin(2\\pi n/10)$")

axs[0].grid(True, linestyle="--", alpha=0.7)
axs[1].grid(True, linestyle="--", alpha=0.7)

plt.show()
