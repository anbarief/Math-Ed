# 13 January 2018,
# Author : Arief Anbiya
# e-mail : anbarief@live.com

# Description :
#   A (currently) small module meant for
#   (junior, general) math-education purposes,
#   to visualize basic statistics measurements such as the arithmetic-mean.
#   *Feedbacks are appreciated.

import matplotlib.pyplot as matplot

class example_numeric:

    def __init__(self, name, data_points):
        assert len(data_points)>1, 'Number of data points must be at least 2.'
        assert all([(type(i) == int or type(i) == float) for i in data_points]),\
               'The data must be numeric.'
        assert type(name)==str, 'Name must be string-type.'
        self.title = name;
        self.data = list(data_points);
        self.length = len(self.data);
        self.minmax = [min(self.data), max(self.data)];
        self.mean = ar_mean(self.data);
        print('*****'+self.title+'*****');
        if self.length > 4:
            print('Data : ['+str(self.data[0])+',' \
                  +str(self.data[1])+',' \
                  +str(self.data[2])+',' \
                  +str(self.data[3])+', ..... , '+str(self.data[-1])+']');
        else:
            print('Data : '+str(self.data));
        print('Number of data points : '+str(self.length));
        print('Minimum value : '+str(self.minmax[0]));
        print('Maximum value : '+str(self.minmax[1]));
        print('(Arithmetic) Mean : '+str(self.mean));

    def scatterplot_interpret(self, ax=matplot, fig=matplot):
        idxs = [i for i in range(0,self.length)];
        if ax!= matplot:
            ax.title.set_text('Scatter plot of : "'+self.title+'"');
        else:
            ax.title('Scatter plot of: "'+self.title+'"');
        ax.plot([0, self.length], [self.mean, self.mean], \
                     'r--', label = '(Arithmetic) Mean='+str(round(self.mean,4)));
        ax.scatter(idxs, self.data, \
                        c = 'b', linewidth = 3, label = 'Data points (index, data[index])');
        ax.legend();
        fig.show();
        
class example_categorical:

    IDN_resident_district = ['Jakarta', 'Jakarta', 'Medan', 'Medan', \
                         'Bandung', 'Surabaya', 'Jakarta', 'Jakarta', \
                         'Solo', 'Yogyakarta', 'Bandung', 'Bandung', \
                         'Banten', 'Jakarta', 'Jakarta', 'Banten', \
                         'Yogyakarta', 'Medan', 'Aceh', 'Aceh', 'Yogyakarta', \
                         'Medan', 'Medan', 'Jakarta', 'Bandung', 'Bandung', \
                         'Jakarta', 'Banten', 'Banten', 'Solo', 'Yogyakarta', \
                         'Bandung', 'Bandung', 'Yogyakarta', 'Medan', 'Aceh', \
                         'Aceh', 'Jakarta', 'Jakarta', 'Medan', 'Medan', 'Bekasi', \
                         'Bekasi', 'Jakarta', 'Bandung', 'Surabaya', 'Surabaya', \
                         'Bekasi', 'Bogor', 'Surabaya'];
    
    def __init__(self, name, data_points=IDN_resident_district):
        assert len(data_points)>1, 'Number of data points must be at least 2.'
        assert all([type(i) == str for i in data_points]),\
               'The data must be categorical(strings).'
        self.title = name;
        self.data = list(data_points);
        self.length = len(self.data);
        self.category = list(set(data_points));
        self.length_cat = len(self.category);
        print('*****'+self.title+'*****');
        if self.length > 4:
            print('Data : ['+str(self.data[0])+', ' \
                  +str(self.data[1])+', ' \
                  +str(self.data[2])+', ' \
                  +str(self.data[3])+', ..... , '+str(self.data[-1])+']');
        else:
            print('Data : '+str(self.data));
        print('Number of data points : '+str(self.length));
        print('Category :');
        for i in range(0, len(self.category)):
            print(str(i+1)+'. '+self.category[i]);
        print('Number of categories : '+str(self.length_cat));

    def piechart_interpret(self, ax=matplot, fig=matplot):
        pie_val = [self.data.count(i) for i in self.category];
        if ax!=matplot:
            ax.title.set_text('Pie chart of : "'+self.title+'"');
        else:
            ax.title('Pie chart of : "'+self.title+'"');
        ax.pie(pie_val, labels=[i for i in self.category]);
        ax.legend([self.category[i]+' : '+str(pie_val[i]) \
                        for i in range(0, len(pie_val))]);
        fig.show();

def ar_mean(data_points):
    res = sum(data_points)/len(data_points);
    return res
     
def compare_interpret(example1, example2):
    FIG, AX = matplot.subplots(2, 1);
    try:
        example1.scatterplot_interpret(ax=AX[0], fig=FIG);
    except AttributeError:
        example1.piechart_interpret(ax=AX[0], fig=FIG);
    try:
        example2.scatterplot_interpret(ax=AX[1], fig=FIG);
    except AttributeError:
        example2.piechart_interpret(ax=AX[1], fig=FIG);
    FIG.tight_layout();
    FIG.show();
