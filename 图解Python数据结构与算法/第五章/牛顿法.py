def f(x):
    return x**2 - 4

def f_prime(x):
    return 2*x

def newton_method(initial_guess, tol=1e-6, max_iter=100):
    x = initial_guess
    iterations = 0
    
    while abs(f(x)) > tol and iterations < max_iter:
        x = x - f(x) / f_prime(x)
        iterations += 1
    
    if iterations == max_iter:
        print("Maximum iterations reached without convergence.")
    else:
        print(f"Root found: {x} after {iterations} iterations.")
    
    return x

# 初始近似值
initial_guess = 2
# 调用牛顿法函数
root = newton_method(initial_guess)
