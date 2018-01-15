# Math-Ed

14 January 2018,

Arief Anbiya, e-mail : anbarief@live.com

This is a (*still in work*) small module with an objective of using Python in math education. This module is intended to be user-frendly for educators with minimum programming knowledge. The current focus is to use appropriate, modified, graphics to visualize math concept such as : 
integral calculation, descriptive statistics, and many other cases. In this version, the application is limited only for :
1. Visualize and working on simple integral calculations (linear and quadratic functions)
2. Visualize and working on basic statistics measurement (arithmetic-mean)

Modules : `integral_1D` and `basic_statistics`

**How to Start:**

`import math_ed.integral_1D as integral`

`import math_ed.basic_statistics as bstat`

(Note: The name `integral` and `bstat` are optional, you can set `as x` or `as y` or `as anyname`)

**Example of using the `integral_1D` module :**

<pre><code> 
import math_ed.integral_1D as integral

example_1 = integral.example_linear(1, 1, [-3, 3]);
example_2 = integral.example_cubic([1, 2, 1, 5], [-3, 3]);
example_1.numeric_result(N = 20);
example_2.numeric_result(N = 20, method = 'trapezoid');
example_1.visual_interpret(N = 20);
example_2.visual_interpret(N = 20, method = 'trapezoid');
integral.compare_visual_interpret(example = [example_1,example_2], \
                                  N = [20, 20], \
                                  compare_method = ['left-rectangle', 'trapezoid']);
</code></pre>

The command `example_1 = integral.example_linear(1, 1, [-3, 3]);`  will create an object that represents the definite integral of : **f(x) = x** in the interval **[0, 1]**. The `example_2` will create an object of integral of **f(x) = x^3 + 2x^2 + x + 5** in the interval **[-3, 3]**. Method `numeric_result` will calculate each integral numerically. Available numerical integration method : `'trapezoid'` and `'left-rectangle'`. The default input for `method` is `'left-rectangle'`. `visual_interpret` will give a visualization of the integral. Result :

<pre><code> 
The numeric integral (by left-rectangle-method) is : 5.1000000000000005 (dx =0.3)
The numeric integral (by trapezoid-method) is : 51.93554999999999 (dx =0.3) </code></pre>

![alt text](https://raw.githubusercontent.com/anbarief/Math-Ed/master/example_1.png)

**Example of using the `basic_statistics` module :**

<pre><code>
import math_ed.basic_statistics as bstat
import random

data = [random.uniform(0, 100) for i in range(100)];
example_1 = bstat.example_numeric(name = 'Example 1', \
                                  data_points = data);
example_2 = bstat.example_categorical(name = 'Example 2');
example_1.scatterplot_interpret();
example_2.piechart_interpret();
bstat.compare_interpret(example_1, example_2); </code></pre>

The `example_numeric` is anclass of simple numerical data, with a method `scatterplot_interpret` that shows its scatter plot. The `example_categorical` is a class of simple categorical data, with a method `piechart_interpret` that shows its pie chart. Result :
<pre><code>
*****Example 1*****
Data : [85.31496511990515,24.193040440009106,31.612178301634074,13.547575820140933, ..... , 94.3721786895224]
Number of data points : 100
Minimum value : 2.1122426323771815
Maximum value : 99.2147012377662
(Arithmetic) Mean : 50.741698145265275
*****Example 2*****
Data : [Jakarta, Jakarta, Medan, Medan, ..... , Surabaya]
Number of data points : 50
Category :
1. Yogyakarta
2. Banten
3. Jakarta
4. Solo
5. Aceh
6. Surabaya
7. Bandung
8. Medan
9. Bekasi
10. Bogor
Number of categories : 10 </code></pre>


![alt text](https://raw.githubusercontent.com/anbarief/Math-Ed/master/example_2.png)

![alt text](https://raw.githubusercontent.com/anbarief/Math-Ed/master/example_3.png)
