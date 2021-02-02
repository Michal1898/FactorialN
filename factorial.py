import timeit
from functools import lru_cache


class CustomException(Exception):
    def __init__(self, a=""):
        message = a
        super().__init__(message)


@lru_cache(maxsize=100)
def fact_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_rec(n - 1)


@lru_cache(maxsize=100)
def fact_iter(n):
    for my_counter in range(n + 1):
        if my_counter == 0 or my_counter == 1:
            n_factorial = 1
        else:
            n_factorial = n_factorial * my_counter
    return n_factorial


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    n = int(input("Zadej n pro výpočet faktoriálu: "))
    if n < 0:
        raise CustomException("N musí být nezáporné!")
    else:
        n_factorial1 = fact_iter(n)
        print("Faktoriál iterací: ", n_factorial1)

        n_factorial2 = int(fact_rec(n))
        print("Faktoriál rekurzí: ", n_factorial2)

        print("Faktoriál rekurzí: ", timeit.timeit("fact_rec(n)",
                                                   "from __main__ import fact_rec, n",
                                                   number=1000000),
              "sekund")
        print("Faktoriál iterací: ", timeit.timeit("fact_iter(n)",
                                                   "from __main__ import fact_iter, n",
                                                   number=1000000),
              "sekund")
