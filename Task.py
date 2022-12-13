

import random
import sympy

weights = [[3753139396, 166740188573], [724520588560, 766050680304],  [10457920653, 1051487855], [1722571966294, 2846977754550], [22496742244741, 4310194783973]]



## Изначально хотел найти градиентным спуском
def apply_transactions(weights: list[list[int]], token_amount: float, iteration:int = None)-> float:
    for idx, lp in enumerate(weights):
        token_amount = lp[1]*token_amount/(lp[0]+token_amount)
        if iteration == idx+1:
            return token_amount
    
    return token_amount

def calc_gradients(weights: list[list[int]], token_amount: float) -> float:
    grad:float = 1
    for idx, lp in enumerate(weights):
        grad = lp[1]*lp[0]/(lp[0]-token_amount)**2 * grad
        token_amount = lp[1]*token_amount/(lp[0]+token_amount)
    print(grad)
    return grad
        

def gradient_descent(weights: list[list[int]], lr:float = 1, e:float=0.01) -> float:
    w_new = random.randint(1, 1000000)
    w_old = 0
    while abs(w_new-w_old)>e:
        w_old = w_new
        w_new = w_old + lr*calc_gradients(weights, w_old)
    return w_new
## Не получалось, так как градиент очень маленький, нужно много шагов.
## В принципе функция легко дифференцируется. Только руками считать произодную  трудно.

x = func = sympy.Symbol('x')
for lp in weights:
    func = lp[1]*func/(lp[0]-func)
## Нам нужно максимизировать F(x) - x, то есть, найти наиболее выгодное решение. 
func = func - x
derivative = sympy.Derivative(func,x)
result = sympy.solve(func, x)
##Сама F(x) всегда возрастает, но производная убывает. F(x)-x сначала возрастает, потом убывает. Соответственно
##Нам нужно 2-е значение.
##Оценить сложность трудно, так как непонятна сложность функций, но работает достаточно быстро.
