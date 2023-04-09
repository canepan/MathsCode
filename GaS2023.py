import sys


def main(argv: list = None):
    if argv is None:
        argv = sys.argv[1:] or ["12"]
    result = 0
    for param in argv:
        if param == "12":
            result += main12() or 0
        elif param == "13":
            result += main13() or 0
        elif param == "13p":
            result += main13_precalc() or 0
        elif param == "15":
            result += main15() or 0
        else:
            print("Please specify either 12, 13 or 15 (or a list of those)")
            result += 100
    return result


def main15():
    print("15. Tre numeri misteriosi (non funziona)")
    limit = 1000
    # a + b + c == 0 ; a * b * c == 78
    # c = -a - b ; b = 78/(a*c)
    # c = -a - 78/(a*c) -> a*c^2 = - c*a^2 - 78 -> a*c(a+c) = -78
    # or: b = 78/(a*(-a - b)) -> b*(-a^2 - a*b) = 78 -> b*a^2 + a*b^2 = -78
    # result: (a+b)*(b+c)*(c+a) = (ab + ac + b^2 + bc)*(c+a) = abc + ba^2 + ac^2 + ca^2 + cb^2 + ab^2 + bc^2 + abc
    #   -> 2abc + ac^2 + ca^2 + cb^2 + bc^2 - 78 = ac^2 + ca^2  + cb^2 + bc^2 + 78
    for a in range(-limit, limit):
        for b in range(-limit, limit):
            c = -a - b
            if a + b + c == 0 and a * b * c == 78:
                print(f"{a=}, {b=}, {c=}: {(a+b)*(b+c)*(c+a)}")
                return
    return 15


def main13():
    print("13. Per un ladro che ha studiato matematica")
    for a in range(1, 10):
        n = 1
        while (n * (n + 1) / 2 != 111 * a) and (n * (n + 1) / 2 <= 999):
            n = n + 1
        if n * (n + 1) / 2 == 111 * a:
            print(n)
            return 0
    return 13


def main13_precalc():
    print("13. Per un ladro che ha studiato matematica (precalculated limit)")
    for n in range(1, 45):
        for a in range(1, 10):
            if n * (n + 1) / 2 == 111 * a:
                print(n)
                return 0
    return 13


def main12():
    print("12. Non si puo', ma e' giusto")
    for a in range(1, 10):
        for b in range(1, 10):
            for n in range(1, 10):
                if a != b and (10 * a + n) / (10 * n + b) == a / b:
                    print(f"{10 * a + n}/{10 * n + b}: {a=}, {b=}, {n=}")
                    return 0
    return 12


if __name__ == "__main__":
    sys.exit(main())
