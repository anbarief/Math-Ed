* Math-Ed

14 January 2018,

Arief

This is a small module with an objective of using Python in math education. This module is intended to be user-frendly for educators with minimum programming knowledge. The current focus is to use appropriate, modified, graphics to visualize math concept such as : 
integral calculation, descriptive statistics, and many other cases. In this version, the application is limited only for :
1. Visualize and working on simple integral calculations (linear and quadratic functions)
2. Visualize and working on basic statistics measurement (arithmetic-mean)

Modules : `integral_1D` and `basic_statistics`

**How to Start:**

`import math_ed.integral_1D as integral`

`import math_ed.basic_statistics as bstat`

(Note: The name `integral` and `bstat` are optional, you can set `as x` or `as y` or `as anyname`)

**Creating an `example_linear` object:**
The command `example1 = integral.example_linear(1, 0, [0, 1]);`  will create an object that represents the definite integral of : **f(x) = x** in the interval **[0, 1]**.
