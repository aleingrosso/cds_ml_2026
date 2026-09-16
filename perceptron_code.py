import numpy as np
import math
from cubature import cubature
from scipy.stats import multivariate_normal
from scipy.special import erf, erfc, comb

################## REPLICA THEORY OF PERCEPTRON GENERALIZATION ##################

math_prefix = np
# math_prefix = math

log = math_prefix.log
exp = math_prefix.exp
sqrt = math_prefix.sqrt
PI = math_prefix.pi
atan = math.atan
asin = math.asin
acos = math.acos
sign = np.sign

def G(x):
    return 1/sqrt(2*PI) * exp(-0.5 * x**2)

def erfsq2(x):
    return erf(x / sqrt(2))

def H(x):
    if x < 5:
        return 0.5 * (1 - erfsq2(x))
    else:
        return G(x) * (1./x - 1./x**3 + 3./x**5)
    
def IntR(t, R):
    return exp(-0.5 * R * t**2) / H(-sqrt(R) * t) * multivariate_normal.pdf(t, mean=0, cov=1)

def IR(R):
    xmin, xmax = -10., 10.
    return cubature(IntR, 1, 1, [xmin], [xmax], args=(R,))[0][0]

def eqR(R, α = 1):
    return R / sqrt(1-R) - α / PI * IR(R)

def compute_gen_error(R):
    return 1/PI * acos(R)


def generate_teacher_and_test_set(Ptest, N):
    T = np.random.randn(N)
    T *= np.sqrt(N / (T**2).sum())
    Xtest = np.random.randn(Ptest, N)
    ytest_sign = np.sign(Xtest @ T)
    return T, Xtest, ytest_sign
