import os
try:
    import sympy as sp
    from sympy import I
    from sympy.abc import x, y, z
except:
    os.system("pip install sympy")
    


def factorise(expr):
    try:
        print(sp.factor(expr, extension=[I]))

    except:
        print("Could not factorise expression \"{}\"".format(str(expr)))


def plot_function(function_plt):
    print("Plotting function {}".format(str(function_plt)))

    try:
        sp.plot(function_plt)

    except:
        print("Could not plot function {}".format(str(function_plt)))


def solve_eqn(eqn_expr):

    try:
        eqn = sp.sympify(eqn_expr)
        print("x = {}".format(str(sp.solveset(eqn))))

    except Exception as e:
        print(e)
        print("Could not solve equation \'{}\'".format(eqn_expr))


def calc_lim(lim_func):

    try:
        lim_to = sp.parse_expr(
            input(
                "Take the limit until? oo and -oo to represent infinity and neg infinity: "
            ))

        return "The limit of the function {} as x goes to {} is {}".format(
            str(lim_func), str(lim_to),
            str(sp.limit(sp.parse_expr(lim_func), x, lim_to)))

    except Exception as e:
        print("Could not take the limit.")
        print(e)


def deriv(deriv_func):

    try:
        return "dy/dx({}) = {}".format(str(deriv_func),
                                       sp.diff(sp.parse_expr(deriv_func), x))

    except Exception as e:
        print("Couldn't differentiate the function {}".format(deriv_func))
        print(e)


def integ(integ_func):
    lower_b = sp.parse_expr(
        input(
            "Integrate from? (input n if you want to calculate antiderivative, 2 lowercase o's to represent infinity): "
        ))
    upper_b = sp.parse_expr(
        input(
            "Integrate until? (input n if you want to calculate antiderivative, 2 lowercase o's to represent infinity): "
        ))

    try:

        if (lower_b == "n" and upper_b == "n"):
            return "integral: {}".format(
                sp.integrate(sp.parse_expr(integ_func), x))

        else:
            return "area under curve: {}".format(
                sp.integrate(sp.parse_expr(integ_func), (x, lower_b, upper_b)))

    except Exception as e:

        print(type(e))

        print("Couldn't integrate the function {}".format(integ_func))
        print(e)


def main():
    while True:
        cmd = input("What would you like to do?:").lower()

        if (cmd == 'help'):
            print(
                "solve equation, plot function, factorise polynomial/poly, integrate, differentiate, calculate limit, clearscreen/cls/clear,\nquit"
            )

        if (cmd == "clearscreen" or cmd == "cls" or cmd == "clear"):
            os.system("clear")
            print("Screen cleared")

        if (cmd == "solve eqn" or cmd == "solve" or cmd == "solve equation"):
            eq_inp = input(
                "Enter an equation (something = something): ").replace(
                    " ", "")

            parsed = "Eq({}, {})".format(
                eq_inp.split("=")[0],
                eq_inp.split("=")[1])
            solve_eqn(parsed)

        if (cmd == "plot func" or cmd == "plot function" or cmd == "plot"
                or cmd == "plt"):
            plot_function(sp.parse_expr(input("Enter a function to plot: ")))

        if (cmd == "factorise polynomial" or cmd == "factorise poly"
                or cmd == "factorise"):
            factorise(sp.parse_expr(input("Enter a polynomial: ")))

        if (cmd == "quit" or cmd == "exit"):
            quit(0)

        if (cmd == "diff" or cmd == "differentiate" or cmd == "derivative"):
            print(deriv(input("Enter a function to differentiate: ")))

        if (cmd == "integ" or cmd == "integrate" or cmd == "integral"):
            print(integ(input("Enter a function to integrate: ")))

        if (cmd == "lim" or cmd == "limit" or cmd == "calculate limit"):
            print(calc_lim(input("Input a function to take the limit: ")))


main()
