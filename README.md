# Math-Ed

14 January 2018,

Arief Anbiya, e-mail : anbarief@live.com

This is a small module with an objective of using Python in math education. This module is intended to be user-frendly for educators with minimum programming knowledge. The current focus is to use appropriate, modified, graphics to visualize math concept such as : 
integral calculation, descriptive statistics, and many other cases. In this version, the application is limited only for :
1. Visualize and working on simple integral calculations (linear and quadratic functions)
2. Visualize and working on basic statistics measurement (arithmetic-mean)

Modules : `integral_1D` and `basic_statistics`

**How to Start:**

`import math_ed.integral_1D as integral`

`import math_ed.basic_statistics as bstat`

(Note: The name `integral` and `bstat` are optional, you can set `as x` or `as y` or `as anyname`)

**Example of using the `integral_1D` module**

`import math_ed.integral_1D as integral`

`example_1 = integral.example_linear(1, 1, [-3, 3]);`

`example_2 = integral.example_cubic([1, 2, 1, 5], [-3, 3]);`

`example_1.numeric_result(N = 20);`

`example_2.numeric_result(N = 20, method = 'trapezoid');`

`example_1.visual_interpret(N = 20);`

`example_2.visual_interpret(N = 20, method = 'trapezoid');`

`integral.compare_visual_interpret(example = [example_1,example_2], \`
`                         N = [20, 20], \`
`                         compare_method = ['left-rectangle', 'trapezoid']);`

The command `example_1 = integral.example_linear(1, 1, [-3, 3]);`  will create an object that represents the definite integral of : **f(x) = x** in the interval **[0, 1]**. The `example_2` will create an object of integral of **f(x) = x^3 + 2x^2 + x + 5** in the interval **[-3, 3]**. Method `numeric_result` will calculate each integral numerically. Available numerical integration method : `'trapezoid'` and `'left-rectangle'`. The default input for `method` is `'left-rectangle'`. `visual_interpret` will give a visualization of the integral. Result :

`The numeric integral (by left-rectangle-method) is : 5.1000000000000005 (dx =0.3)`

`The numeric integral (by trapezoid-method) is : 51.93554999999999 (dx =0.3)`

[alt text](https://raw.githubusercontent.com/anbarief/Math-Ed/master/example_1.png)



