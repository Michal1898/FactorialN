import timeit

class CustomException(Exception):
    def __init__(self,a=""):
        message = a
        super().__init__(message)


def fact_rec(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact_rec(n-1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=int(input("Zadej n pro výpočet faktoriálu: "))
    if n<0:
        raise CustomException("N musí být nezáporné!")
    else:
        start_time = timeit.timeit()
        n_factorial=1
        for my_counter in range(n+1):
            if my_counter==0 or my_counter==1:
                n_factorial=1
            else:
                n_factorial=n_factorial*my_counter

        end_time = timeit.timeit()
        print("Délka výpočtu faktoriálu iterací:",(end_time-start_time))

        print("Faktoriál iterací: ",n_factorial)

        print("Délka výpočtu faktoriálu iterací:",(end_time - start_time))
        start_time = timeit.timeit()
        n_factorial2=int(fact_rec(n))
        end_time = timeit.timeit()
        print("Délka výpočtu faktoriálu rekurzí:",(end_time - start_time))
        print("Faktoriál rekurzí: ",n_factorial2)


