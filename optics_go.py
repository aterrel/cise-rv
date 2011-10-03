
from sympy import *
from sympy.statistics import *
from sympy.physics import gaussopt as optics

# Describe a beam expander system
f1 = Symbol('f1')
f2 = Symbol('f2')
d = Symbol('d')

lens1 = optics.ThinLens(f1)
lens2 = optics.ThinLens(f2)
space = optics.FreeSpace(d)

beam_expander = space*lens2*space*lens1
# SIMPLIFY STATEMENT - NOT IN PAPER
beam_expander = Matrix(2,2, map(simplify, beam_expander.mat))

ray = optics.GeometricRay(5, 0) # inputs are height and angle
exit_ray = beam_expander * ray

exit_height, exit_angle = exit_ray

print exit_height


#if we substitute f1 = -1, f2 = 6, d = 5 we see that the ray exits at 30 cm

height = 5
angle = Normal(0, pi/100, symbol=Symbol('theta'))
ray = optics.GeometricRay(height, angle)

exit_ray = beam_expander * ray

exit_height, exit_angle = exit_ray

print E(exit_height)
print simplify(var(exit_height))
print Density(exit_height)

## Give numbers
exit_height = exit_height.subs({f1:-1, d:5, f2:6})
#print E(exit_height)
#print P(exit_height>31)
