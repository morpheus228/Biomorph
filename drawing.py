from matplotlib import pyplot as plt
import matplotlib
import numpy as np
import math
matplotlib.rcParams['backend'] = 'Qt5Agg'

class Biomorph():
    # initialization of the parameters of drawing creature
    def __init__(self, deep, degree, RDS, LDS, deg_k, add_deg, DA, length, RLS, LLS, add_len, LA):

        # parameters of drawing creature
        self.deep = deep

        self.degree = degree
        self.RDS = RDS
        self.LDS = LDS
        self.deg_k = deg_k
        self.add_deg = add_deg
        self.DA = DA

        self.length = length
        self.RLS = RLS
        self.LLS = LLS
        self.add_len = add_len
        self.LA = LA

        self.RDegrees = self.prepare_degrees(self.RDS)
        self.LDegrees = self.prepare_degrees(self.LDS)
        self.RLengths = self.prepare_length(self.RLS)
        self.LLengths = self.prepare_length(self.LLS)

    # parameters of degrees in relation to Degree Status(RDS, LDS)
    def prepare_degrees(self, DS):
        degree = self.degree * self.deg_k
        add_deg = self.add_deg * self.deg_k

        if DS == 1:
            return [degree for i in range(self.deep)]
        if DS == 2:
            return list(range(degree, degree + add_deg * self.deep, add_deg))
        if DS == 3:
            return list(range(degree, degree - add_deg * self.deep, -add_deg))
        if DS == 4:
            return (([degree] * self.DA + [degree + add_deg] * self.DA) * (self.deep // 2 + 1))[:self.deep]

    # parameters of degrees in relation to Length Status(RLS, LLS)
    def prepare_length(self, LS):
        if LS == 1:
            return [self.length for i in range(self.deep)]
        if LS == 2:
            return list(map(abs, range(self.length, self.length + self.add_len * self.deep, self.add_len)))
        if LS == 3:
            return list(map(abs, range(self.length, self.length - self.add_len * self.deep, -self.add_len)))
        if LS == 4:
            return (([self.length] * self.LA + [self.length + self.add_len] * self.LA) * (self.deep // 2 + 1))[
                   :self.deep]

    # the processing of drawing creatures
    def draw(self, ind):
        x0 = 0
        y0 = 0

        list_of_x = [[0, 0]]
        list_of_y = [[0, 0]]

        for i in range(self.deep):

            new_list_of_x = []
            new_list_of_y = []

            L_length = self.LLengths[i]
            R_length = self.RLengths[i]
            L_degree = self.LDegrees[i]
            R_degree = self.RDegrees[i]

            for id_branch in range(len(list_of_y)):

                x_branch = list_of_x[id_branch]
                y_branch = list_of_y[id_branch]
                diff_y = y_branch[-1] - y_branch[-2]
                diff_x = x_branch[-1] - x_branch[-2]

                if diff_y == 0 and diff_x > 0:
                    pr_degree = -90

                elif diff_y < 0 and diff_x > 0:
                    pr_degree = -180 + math.degrees(-math.atan(diff_x / diff_y))

                elif diff_y < 0 and diff_x == 0:
                    pr_degree = 180

                elif diff_y < 0 and diff_x < 0:
                    pr_degree = 180 + math.degrees(-math.atan(diff_x / diff_y))

                elif diff_y == 0 and diff_x < 0:
                    pr_degree = 90

                elif diff_y == 0 and diff_x == 0:
                    pr_degree = 0

                else:
                    pr_degree = math.degrees(-math.atan(diff_x / diff_y))

                rads = math.radians(pr_degree)

                x_L = L_length * math.cos(math.radians(L_degree))
                x_R = -R_length * math.cos(math.radians(R_degree))
                y_L = L_length * math.sin(math.radians(L_degree))
                y_R = R_length * math.sin(math.radians(R_degree))

                new_list_of_x.append(x_branch + [x_L * math.cos(rads) - y_L * math.sin(rads) + x_branch[-1]])
                new_list_of_y.append(y_branch + [x_L * math.sin(rads) + y_L * math.cos(rads) + y_branch[-1]])
                new_list_of_x.append(x_branch + [x_R * math.cos(rads) - y_R * math.sin(rads) + x_branch[-1]])
                new_list_of_y.append(y_branch + [x_R * math.sin(rads) + y_R * math.cos(rads) + y_branch[-1]])

            list_of_x = new_list_of_x.copy()
            list_of_y = new_list_of_y.copy()

        plt.rcParams.update({'figure.figsize': (5, 5)})
        for i in range(len(list_of_x)):
            plt.plot(list_of_x[i], list_of_y[i], c='black')
        min_ = np.c_[list_of_x, list_of_y].min()
        max_ = np.c_[list_of_x, list_of_y].max()
        plt.xticks([])
        plt.yticks([])
        plt.xlim(min_ - 1, max_ + 1)
        plt.ylim(min_ - 1, max_ + 1)
        plt.savefig('biomorth' + str(ind) + '.png', bbox_inches='tight', pad_inches=-0.05)
        
