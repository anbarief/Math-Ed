# 13 January 2018,
# Author : Arief Anbiya
# e-mail : anbarief@live.com

# Description :
#   A (currently) small module meant for education purposes,
#   to visualize integrals of a line and a quadratic curve.
#   *Feedbacks are appreciated.

import matplotlib.pyplot as matplot


class example_linear:
    
    def __init__(self, m, c, bound_interval):
        assert (type(bound_interval) == list) and (len(bound_interval)==2), \
               'bound_interval must be a numeric list of length 2.'
        self.gradient = m; self.intersect_y = c;
        self.bound = bound_interval;
        if m==0 and c==0:
            self.fun_str = 'f(x) = 0';
        elif m!=0 and c==0:
            self.fun_str = 'f(x) = '+str(round(m,4))+r'x';
        elif m!=0 and c!=0:
            self.fun_str = 'f(x) = '+str(round(m, 4))+r'x +'+str(round(c,4));
        else:
            self.fun_str = 'f(x) = '+str(round(c, 4));
        N_real = 2;
        dx_real = (self.bound[1]-self.bound[0])/N_real;
        self.x_real = [self.bound[0] + i*dx_real for i in range(0, N_real+1)];
        self.y_real = [self.fun(i) for i in self.x_real];

    def fun(self, x):
        return self.gradient*x + self.intersect_y

    def numeric_result(self, N, method='left-rectangle'):
        assert N>0, 'Input N must be a positive integer, '+ \
               'if float, it will be rounded to integer.'
        N = min(int(N), 5000);
        dx = (self.bound[1]-self.bound[0])/N;
        x = [self.bound[0] + i*dx for i in range(0, N)];
        y = [self.fun(i) for i in x];
        if method=='left-rectangle':
            sum_integral = sum([i*dx for i in y]);
            print('The numeric integral (by left-rectangle-method) is : '\
                  +str(sum_integral)\
                  +' (dx ='+str(round(dx, 4))+')');
        elif method=='trapezoid':
            sum_integral = 0.5*dx*sum([y[i] + y[i+1] for i in range(0, len(y)-1)]);
            print('The numeric integral (by trapezoid-method) is : '\
                  +str(sum_integral)\
                  +' (dx ='+str(round(dx, 4))+')');
        else:
            raise AssertionError('Input correct method, for example : method=''trapezoid''.');
        return sum_integral
    
    def visual_interpret(self, N, method='left-rectangle', ax=None, fig=None):
        assert N>0, 'Input N must be a positive integer, '+ \
               'if float, it will be rounded to integer.'
        N = min(int(N), 400);
        dx = (self.bound[1]-self.bound[0])/(N);
        x = [self.bound[0] + i*dx for i in range(0, N+1)];
        y = [self.fun(i) for i in x];
        line = '-k';
        if ax is None:
            ax=matplot; fig=matplot;
        ax.plot(x, [0 for i in x], 'r--');
        for i in _area_gen(x, y, line, ax, int_method=method):
                i;
        if method=='left-rectangle':
            ax.plot([x[-1],x[-1]], [y[-2],y[-2]], line);
        elif method=='trapezoid':
            ax.plot([x[-1],x[-1]], [y[-1],y[-1]], line);
        else:
            raise AssertionError('Input correct method, for example : method=''trapezoid''.');
        ax.plot(self.x_real, self.y_real, '-b', linewidth = 4, label = self.fun_str);
        if ax == matplot:
            ax.title(method+', dx='\
                     +str(round(dx, 4))+', N='\
                     +str(N));
            ax.xlabel(r'$x$'); ax.ylabel(r'$y$');
        else:
            ax.title.set_text(method+', dx='\
                              +str(round(dx, 4))+', N='\
                              +str(N));
            ax.xaxis.label.set_text(r'$x$'); ax.yaxis.label.set_text(r'$y$');
        ax.legend();
        if fig!=matplot:
            fig.tight_layout();
        else:
            fig.show();
   
class example_quadratic(example_linear):

    def __init__(self, coef_vec, bound_interval):
        assert coef_vec[0] != 0, 'The 1st coefficient of x^2 must be nonzero.'
        assert (type(bound_interval) == list) and (len(bound_interval)==2), \
               'bound_interval must be a numeric list of length 2.'
        self.coef = coef_vec; self.intersect_y = coef_vec[-1];
        self.bound = bound_interval;
        self.fun_str = [None, None, None];
        if self.coef[0] == 0:
            self.fun_str[0] = '';
        else:
            self.fun_str[0] = str(round(self.coef[0],4))+r'$x^{2}$';
        if self.coef[1] == 0:
            self.fun_str[1] = '';
        else:
            self.fun_str[1] = ' + '+str(round(self.coef[1],4))+r'$x$';
        if self.coef[2] == 0:
            self.fun_str[2] = '';
        else:
            self.fun_str[2] = ' + '+str(round(self.coef[2], 4));
        self.fun_str = r'$f(x) =$ '+self.fun_str[0]+self.fun_str[1]+self.fun_str[2];
        N_real = 1000;
        dx_real = (self.bound[1]-self.bound[0])/N_real;
        self.x_real = [self.bound[0] + i*dx_real for i in range(0, N_real+1)];
        self.y_real = [self.fun(i) for i in self.x_real];

    def fun(self, x):
        return self.coef[0]*x**2 + self.coef[1]*x + self.coef[2]

class example_cubic(example_linear):

    def __init__(self, coef_vec, bound_interval):
        assert coef_vec[0] != 0, 'The 1st coefficient of x^3 must be nonzero.'
        assert (type(bound_interval) == list) and (len(bound_interval)==2), \
               'bound_interval must be a numeric list of length 2.'
        self.coef = coef_vec; self.intersect_y = coef_vec[-1];
        self.bound = bound_interval;
        self.fun_str = [None, None, None, None];
        if self.coef[0] == 0:
            self.fun_str[0] = '';
        else:
            self.fun_str[0] = str(round(self.coef[0],4))+r'$x^{3}$';
        if self.coef[1] == 0:
            self.fun_str[1] = '';
        else:
            self.fun_str[1] = ' + '+str(round(self.coef[1],4))+r'$x^{2}$';
        if self.coef[2] == 0:
            self.fun_str[2] = '';
        else:
            self.fun_str[2] = ' + '+str(round(self.coef[2], 4))+r'$x$';
        if self.coef[3] == 0:
            self.fun_str[3] = '';
        else:
            self.fun_str[3] = ' + '+str(round(self.coef[3], 4));
        self.fun_str = r'$f(x) =$ '\
                       +self.fun_str[0]+self.fun_str[1]+self.fun_str[2]+self.fun_str[3];
        N_real = 1000;
        dx_real = (self.bound[1]-self.bound[0])/N_real;
        self.x_real = [self.bound[0] + i*dx_real for i in range(0, N_real+1)];
        self.y_real = [self.fun(i) for i in self.x_real];

    def fun(self, x):
        return self.coef[0]*(x**3) + self.coef[1]*(x**2) + self.coef[2]*x + self.coef[3]
        
def compare_visual_interpret(example = [example_cubic([1,1,1,1], [-2, 2])], N = [10], \
                             compare_method = ['left-rectangle']):
    assert len(set([len(N),len(example),len(compare_method)]))==1, \
           'len(example), len(N), and len(compare_method) must be the same.'
    FIG, AX = matplot.subplots(len(N), 1);
    for i in range(0, len(example)):
        example[i].visual_interpret(N[i], ax=AX[i], fig=FIG, method = compare_method[i]);
    FIG.show();

def _area_gen(x, y, line, ax, int_method='left-rectangle'):
        if int_method=='left-rectangle':
            for i in range(0, len(x)-1):
                area_list = [ax.plot([x[i],x[i]], [0,y[i]], line), \
                            ax.plot([x[i+1],x[i+1]], [0,y[i]], line), \
                            ax.plot([x[i], x[i+1]], [y[i], y[i]], line), \
                             ax.fill_between([x[i], x[i+1]], [y[i], y[i]], color = 'teal')];
                yield area_list
        if int_method=='trapezoid':
            for i in range(0, len(x)-1):
                area_list = [ax.plot([x[i],x[i]], [0,y[i]], line), \
                            ax.plot([x[i+1],x[i+1]], [0,y[i+1]], line), \
                            ax.plot([x[i], x[i+1]], [y[i], y[i+1]], line), \
                             ax.fill_between([x[i], x[i+1]], [y[i], y[i+1]], color = 'teal')];
                yield area_list











