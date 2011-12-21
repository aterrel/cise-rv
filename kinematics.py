from sympy import *
from sympy.statistics import *

x0, y0, yf, m, theta, t, g = symbols('x0 y0 y_f m theta t g', real=True)

x = x0 + m*cos(theta)*t
y = y0 + m*sin(theta)*t + g/2*t**2

t_impact = solve(y-yf, t)[1]

x_f = x.subs(t, t_impact)

d = {x0:0, y0:10, yf:0, m:10, theta:pi/4, g:S(-98)/10}
dr = {x0:0, y0:Normal(10,1), yf:0, m:10, theta:pi/4, g:S(-98)/10}

dr_big = {x0:0, y0:Normal(10,1, symbol=y0), yf:0, m:Normal(10,2, symbol=m),
        theta:Normal(pi/4, pi/20, symbol=th), g:S(-98)/10}

# Try
# x_f.subs(d).evalf()
# E(x_f.subs(dr))
# P(x_f.subs(dr_big), samples=1000)

def sampling_example():
    y0 = Normal(10,1)
    g = -9.8; x0=0; yf = 0
    m = Uniform(9,11.5)
    theta = Normal(pi/4, pi/20)

    x = x0 + m*cos(theta)*t
    y = y0 + m*sin(theta)*t + g/2*t**2
    t_impact = solve(y-yf, t)[1]
    x_f = x.subs(t, t_impact)

    return P(theta>pi/4  ,  x_f>16, samples=1000)


