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
    def calc_annuity_graph(cls, pv, duration, rate, additional_payment=0, add_pay_frequency=1):
        n = duration * 12
        r = rate / 100 / 12
        pmt = loan.calc_annuity(pv, duration, rate)
        principal_left = pv
        graph = np.zeros((n, 5))

        for p in range(n):
            if p == 0:
                principal_left = pv
            else:
                principal_left = principal_left - graph[p - 1][2]
                if p % add_pay_frequency == 0:
                    principal_left -= additional_payment

            # principal_left = pv if p == 0 else principal_left - graph[p - 1][2] - additional_payment
            if principal_left <= 0:
                break
            graph[p][0] = pmt
            graph[p][1] = principal_left * r
            graph[p][2] = pmt - graph[p][1]
            graph[p][3] = additional_payment if p % add_pay_frequency == 0 else 0
            graph[p][4] = principal_left
        return graph[~(graph == 0).all(1)]

    @classmethod
    def print_graph(cls, graph, PV, RATE, ADD_PAY):
        np.set_printoptions(precision=2, suppress=True)
        r_count, c_count = graph.shape

        print(graph)
        print('-----------------------------------')
        print('Loan Amount:', PV)
        print('Duration:', RATE)
        print('Rate:', RATE, '%')
        print('Additional Payment: ', ADD_PAY, '$')
        print('-----------------------------------')

        print('Months Count: ', r_count)
        print('Intrest Total: {} $'.format(round(graph[:, 1].sum(), 2)))
        print(
            'Monthly Payment:{0} + {1} = {2} $'.format(round(graph[0, 0], 2), ADD_PAY, round(graph[0, 0], 2) + ADD_PAY))

    @classmethod
    def save_graph_to_csv(cls, graph, path):
        import pandas as pd
        df = pd.DataFrame(graph)
        df.to_csv(path, header=['PMT', 'Interest', 'Principal', 'Additional_Payment', 'Principal Left'])
        return path
