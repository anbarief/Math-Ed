, # Math-Ed

14 January 2018,

Arief.A, e-mail : anbarief@live.com

This is a small module with an objective of using Python in math education. This module is intended to be user-frendly for educators with minimum programming knowledge. The current focus is to use appropriate, modified, graphics to visualize math concept such as : 
integral calculation, descriptive statistics, and many other cases. In this version, the application is limited only for :
1. Visualize and working on simple integral calculations (linear and quadratic functions)
2. Visualize and working on basic statistics measurement (arithmetic-mean)

Modules : `integral_1D` and `basic_statistics`

**How to Start:**

`import math_ed.integral_1D as integral`

`import math_ed.basic_statistics as bstat`

(Note: The name `integral` and `bstat` are optional, you can set `as x` or `as y` or `as anyname`)

**Creating and working on an `example_linear` object:**

The command `example1 = integral.example_linear(1, 0, [0, 1]);`  will create an object that represents the definite integral of : **f(x) = x** in the interval **[0, 1]**.

**Calculate integral numerically using `numeric_result` method:**

Available numerical integration method : `'trapezoid'` and `'left-rectangle'`. The default input for `method` is `'left-rectangle'`. 
Command `example1.numeric_result(N=100, method='trapezoid')` will print and return :

`The numeric integral (by trapezoid-method) is : 0.49005000000000004 (dx =0.01)`

`0.49005000000000004`

Higher `N` will give more accurate result, for example  `example1.numeric_result(N=1000, method='trapezoid')` will print and return : 

`The numeric integral (by trapezoid-method) is : 0.49900050000000007 (dx =0.001)`

`0.49900050000000007`

which is really close to the exact integral result **0.5**.


**Visualize using `visual_interpret` method**

To visualize how the integral was approximated : `example1.visual_interpret(N=10, method='trapezoid')`

![alt text](https://raw.githubusercontent.com/anbarief/Math-Ed/master/example_1.png)

Another example : `example1.visual_interpret(N=10, method='')`

![alt text](https://raw.githubusercontent.com/anbarief/Math-Ed/master/example_2.png)

**Creating and working on an `example_quadratic` object:**

The command `example2 = integral.example_quadratic([1, 2, 3], [-1, 1]);`  will create an object that represents the definite integral of : **f(x) = x^2 + 2x + 3** in the interval **[-1, 1]**.

**Calculate integral numerically using `numeric_result` method:**

Available numerical integration method : `'trapezoid'` and `'left-rectangle'`. The default input for `method` is `'left-rectangle'`. 
Command `example2.numeric_result(N=100)` will print and return :

`The numeric integral (by left-rectangle-method) is : 6.6267999999999985 (dx =0.02)`

`6.6267999999999985`

which is quite close to the actual integral result **20/3** or **6.66666...**.

**Visualize using `visual_interpret` method**

To visualize how the integral was approximated : `example2.visual_interpret(N=10)`

![alt text](https://raw.githubusercontent.com/anbarief/Math-Ed/master/example_3.png)

**Using `integral.compare_visual_interpret` to compare `visual_interpret` results**

`integral.compare_visual_interpret(example1, example2, N = [10, 10], compare_method = ['trapezoid', 'trapezoid'])` will result in :

![alt text](https://raw.githubusercontent.com/anbarief/Math-Ed/master/example_4.png)







































