import matplotlib.pyplot as plt
from Bracketing.Function import Function as Func


def draw_from_lists(xs, ys):
    """
    :param xs: the list of x's
    :param ys: the list of y's such that for all xi  --> yi = f(xi)
    :return: plotting the function in a new window
    """
    plt.plot(xs, ys)
    plt.show()


def draw(function_string, number_of_points, left, right):
    seg = (right - left) / number_of_points
    fun = Func(function_string)
    xs = list()
    ys = list()

    while left < right:
        xs.append(left)
        ys.append(fun.get_value_at(left))
        left += seg
    draw_from_lists(xs , ys)


f = "x * x "
n = 50000
left = -200
right = 200
draw(f , n , left , right )
print("shit")