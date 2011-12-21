from sympy import *
from sympy.statistics import *

x0, y0, yf, m, th, t, g = symbols('x0 y0 yf m theta t g', real=True)

x = x0 + m*cos(th)*t
y = y0 + m*sin(th)*t + g/2*t**2

t_impact = solve(y-yf, t)[1]

x_f = x.subs(t, t_impact)

d = {x0:0, y0:10, yf:0, m:10, th:pi/4, g:S(-98)/10}
dr = {x0:0, y0:Normal(10,1), yf:0, m:10, th:pi/4, g:S(-98)/10}

dr_big = {x0:0, y0:Normal(10,1, symbol=y0), yf:0, m:Normal(10,2, symbol=m), th:Normal(pi/4, pi/20, symbol=th), g:S(-98)/10}

# Try
# x_f.subs(d).evalf()
# E(x_f.subs(dr))
# P(x_f.subs(dr_big), samples=1000)

