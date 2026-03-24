import matplotlib.pyplot as plt
import numpy as np

# r g b
x = [[1, 2, 3, 4, 5], [0, 0, 5, 5, 5, 5, 0, 0], [2, -1, 3, -2, 1, -1]]
h = [[1, 1, 1], [1, 0, -1], [0.5, 0.25, 0.125]]

# start end
x_bounds = [[0, 4], [-2, 5], [-3, 2]]
h_bounds = [[0, 2], [-1, 1], [0, 2]]


def get_bound(x_bound, h_bound):
    y_start = x_bound[0] + h_bound[0]
    y_end = x_bound[1] + h_bound[1]
    n_y = np.arange(y_start, y_end + 1)
    return n_y


def my_conv(x_sig, h_sig, x_bound, h_bound):
    n_y = get_bound(x_bound, h_bound)

    y = np.zeros(len(n_y))


    k_start = x_bound[0]
    k_end = x_bound[1]

    h_start = h_bound[0]
    h_end = h_bound[1]

    for idx, n in enumerate(n_y):
        sum = 0

        for k_idx, k in enumerate(range(k_start, k_end + 1)):

            h_k_index = n - k
            if h_start <= h_k_index <= h_end:
                h_list_index = h_k_index - h_start
                sum += x_sig[k_idx] * h_sig[h_list_index]

        y[idx] = sum

    return n_y, y


fig, axes = plt.subplots(
    ncols=2,
    nrows=2,
    figsize=(12, 8),
    layout="constrained",
)
axs = axes.ravel()

# input signal 1
axs[0].stem(
    np.arange(x_bounds[0][0], x_bounds[0][1] + 1),
    x[0],
    linefmt="r-",
    markerfmt="rs",
    basefmt="k-",
)
# input signal 2
axs[0].stem(
    np.arange(x_bounds[1][0], x_bounds[1][1] + 1),
    x[1],
    linefmt="g-",
    markerfmt="g^",
    basefmt="k-",
)
# input signal 3
axs[0].stem(
    np.arange(x_bounds[2][0], x_bounds[2][1] + 1),
    x[2],
    linefmt="b-",
    markerfmt="bv",
    basefmt="k-",
)

axs[0].set_title("Input Signal: x[n]", fontweight="bold")
axs[0].grid(True, linestyle="--", alpha=0.6)


# kernel signal 1
axs[1].stem(
    np.arange(h_bounds[0][0], h_bounds[0][1] + 1),
    h[0],
    linefmt="r-",
    markerfmt="rs",
    basefmt="k-",
)
#  kernel signal 2
axs[1].stem(
    np.arange(h_bounds[1][0], h_bounds[1][1] + 1),
    h[1],
    linefmt="g-",
    markerfmt="g^",
    basefmt="k-",
)
# kernel signal 3
axs[1].stem(
    np.arange(h_bounds[2][0], h_bounds[2][1] + 1),
    h[2],
    linefmt="b-",
    markerfmt="bv",
    basefmt="k-",
)

axs[1].set_title("Kernel Signal: h[n]", fontweight="bold")
axs[1].grid(True, linestyle="--", alpha=0.6)

n_y_1, y1 = my_conv(x[0], h[0], x_bounds[0], h_bounds[0])
n_y_2, y2 = my_conv(x[1], h[1], x_bounds[1], h_bounds[1])
n_y_3, y3 = my_conv(x[2], h[2], x_bounds[2], h_bounds[2])

axs[2].stem(
    n_y_1,
    y1,
    linefmt="r-",
    markerfmt="rs",
    basefmt="k-",
)
axs[2].stem(
    n_y_2,
    y2,
    linefmt="g-",
    markerfmt="g^",
    basefmt="k-",
)
axs[2].stem(
    n_y_3,
    y3,
    linefmt="b-",
    markerfmt="bv",
    basefmt="k-",
)
axs[2].set_title("My Convolution: y[n]", fontweight="bold")
axs[2].grid(True, linestyle="--", alpha=0.6)

axs[3].stem(
    get_bound(x_bound=x_bounds[0], h_bound=h_bounds[0]),
    np.convolve(x[0], h[0]),
    linefmt="r-",
    markerfmt="rs",
    basefmt="k-",
)
axs[3].stem(
    get_bound(x_bound=x_bounds[1], h_bound=h_bounds[1]),
    np.convolve(x[1], h[1]),
    linefmt="g-",
    markerfmt="g^",
    basefmt="k-",
)
axs[3].stem(
    get_bound(x_bound=x_bounds[2], h_bound=h_bounds[2]),
    np.convolve(x[2], h[2]),
    linefmt="b-",
    markerfmt="bv",
    basefmt="k-",
)
axs[3].set_title("Built-in Convolution: y[n]", fontweight="bold")
axs[3].grid(True, linestyle="--", alpha=0.6)


plt.show()
