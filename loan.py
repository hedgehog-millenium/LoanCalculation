import math
import numpy as np


class loan:
    @classmethod
    def calc_annuity(cls, pv, duration, rate):
        # Formula  P= r(PV)/1-(1+r)-n
        # P = Payment
        # PV = Present Value
        # r = rate per period
        # n = number of periods
        n = duration * 12
        r = rate / 100 / 12
        form_up = r * pv
        form_down = 1 - math.pow(1 + r, -n)
        pmt = form_up / form_down
        return pmt

    @classmethod
    def calc_annuity_graph(cls, pv, duration, rate, additional_payment=0):
        n = duration * 12
        r = rate / 100 / 12
        pmt = loan.calc_annuity(pv, duration, rate)
        principal_left = pv
        graph = np.zeros((n, 5))

        for p in range(n):
            principal_left = pv if p == 0 else principal_left - graph[p - 1][2]-additional_payment
            if principal_left <= 0:
                break
            graph[p][0] = round(pmt, 2)
            graph[p][1] = round(principal_left * r, 2)
            graph[p][2] = round(pmt - graph[p][1], 2)
            graph[p][3] = additional_payment
            graph[p][4] = round(principal_left, 2)
        return graph
