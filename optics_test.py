from sympy import *
from sympy.statistics import *
from sympy.physics import gaussopt as optics
# Describe a light ray with a vertical position and an angle
position = Symbol('y')
angle = Symbol('theta')
ray = optics.GeometricRay(position, angle)
horizontal_ray = optics.GeometricRay(position, 0)

# Describe a beam expander made up of two thin lenses separated by empty space
f1 = Symbol('f1')
f2 = Symbol('f2')
d = Symbol('d')

lens1 = optics.ThinLens(f1)
lens2 = optics.ThinLens(f2)
space = optics.FreeSpace(d)

beam_expander = lens2*space*lens1
beam_expander = Matrix(2,2, map(simplify, beam_expander.mat))

exit_ray = beam_expander*horizontal_ray
exit_position, exit_angle = exit_ray
# Solve for what f2 must be for the beam_expander to map horizontal beams to
# horizontal beams (this defines a beam expander)
f2_intended = solve(exit_angle, f2)[0]
# Given the correct focal length what is the magnification?
magnification = (exit_position / position).subs(f2, f2_intended)


s1, s2, sd = symbols('sigma_1 sigma_2 sigma_d', positive=True, bounded=True)
F1 = Normal(f1, s1, symbol=Symbol('F1'))
F2 = Normal(f2_intended, s2, symbol=Symbol('F2'))
D = Normal(d, sd, symbol=Symbol('D'))

lens1 = optics.ThinLens(f1)
lens2 = optics.ThinLens(f2)
space = optics.FreeSpace(D)

beam_expander = lens2*space*lens1
beam_expander = Matrix(2,2, map(simplify, beam_expander.mat))

mud, muy, mut = symbols('mu_d mu_y mu_t', bounded=True, real=True)
sd, sy, st = symbols('sigma_d sigma_y sigma_t', bounded=True, positive=True)

f1 = -1
#d = Normal(5,S(1)/10, symbol=Symbol('d'))
#d = Normal(mud, sd, symbol=Symbol('d'))
d = 5
#d = Uniform(S(4),S(6), symbol=Symbol('d'))
f2 = E(d) - f1

position = 5
# mupos, muang = symbols('mu_y mu_{\theta}', bounded=True, real=True)
#position = Normal(muy, sy , symbol=Symbol('y'))
#position = Normal(5, S(1)/100, symbol=Symbol('y'))
#angle = Normal(0, st, symbol=Symbol('Theta'))
angle = Normal(0, pi/100, symbol=Symbol('Theta'))
#angle = Uniform(-pi/100, +pi/100, symbol=Symbol('Theta'))
#angle = 0

ray = optics.GeometricRay(position, angle)

lens1 = optics.ThinLens(f1)
lens2 = optics.ThinLens(f2)
space = optics.FreeSpace(d)

beam_expander = lens2*space*lens1
beam_expander = Matrix(2,2, map(simplify, beam_expander.mat))

out_ray = beam_expander*ray
out_height, out_angle = out_ray

