# -*- coding: utf-8 -*-
# Author: Yiping Liu
# Description: This script calculates the average of a list of numbers.
# Version: 1.0
# Last Modified: May 7, 2023

import pandas as pd

pd.set_option('display.precision', 11)

species = {
    ('b0', 'Na+', 'Cl-'): {
        'a1': 7.87239712e00,
        'a2': -8.3864096e-3,
        'a3': 1.44137774e-5,
        'a4': -8.7820301e-9,
        'a5': -4.96920671e2,
        'a6': -8.20972560e-1
    },
    ('b1', 'Na+', 'Cl-'): {
        'a1': 8.66915291e2,
        'a2': 6.06166931e-1,
        'a3': -4.80489210e-4,
        'a4': 1.88503857e-7,
        'a5': -1.70460145e4,
        'a6': -1.67171296e2,
    },
    ('b2', 'Na+', 'Cl-'): {
        'a1': 0,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('c_phi', 'Na+', 'Cl-'): {
        'a1': 1.70761824e00,
        'a2': 2.32970177e-03,
        'a3': -2.46665619e-06,
        'a4': 1.21543380e-09,
        'a5': -1.35583596e00,
        'a6': -3.87767714e-01,
    },
    ('b0', 'Na+', 'SO4-2'): {
        'a1': -0.12709e1,
        'a2': 0.4425144e-2,
        'a3': -0.35e-8,
        'a4': -0.928e-9,
        'a5': 0.1425e2,
        'a6': -0.584e-2,
    },
    ('b1', 'Na+', 'SO4-2'): {
        'a1': -0.13915e1,
        'a2': 0.107532e-1,
        'a3': -0.183e-6,
        'a4': -0.4498e-8,
        'a5': 0.9328e2,
        'a6': -0.167885e0,
    },
    ('c_phi', 'Na+', 'SO4-2'): {
        'a1': 0.21225e0,
        'a2': -0.72306e-3,
        'a3': 0,
        'a4': -0.114e-9,
        'a5': 0.435e1,
        'a6': -0.1855e-2,
    },
    ('b0', 'K+', 'Cl-'): {
        'a1': 2.65718766e1,
        'a2': 9.92715099e-3,
        'a3': -3.62323330e-6,
        'a4': -6.28427180e-11,
        'a5': -7.55707220e2,
        'a6': -4.67300770e0,
    },
    # ('b0', 'K+', 'Cl-'): {
    #     'a1': 0.04835, # Christov
    #     'a2': 0,
    #     'a3': 0,
    #     'a4': 0,
    #     'a5': 0,
    #     'a6': 0,
    # },
    ('b1', 'K+', 'Cl-'): {
        'a1': 1.69742977e3,
        'a2': 1.22270943e0,
        'a3': -9.9904449e-4,
        'a4': 4.04786721e-7,
        'a5': -3.286844221e4,
        'a6': -3.288138481e2,
    },
    # ('b1', 'K+', 'Cl-'): {
    #     'a1': 0.2122, # Christov
    #     'a2': 0,
    #     'a3': 0,
    #     'a4': 0,
    #     'a5': 0,
    #     'a6': 0,
    # },

    ('c_phi', 'K+', 'Cl-'): {
        'a1': -3.27571680e0,
        'a2': -1.27222054e-3,
        'a3': 4.71374283e-7,
        'a4': 1.1162507e-11,
        'a5': 9.07747666e1,
        'a6': 5.80513562e-1,
    },

    # ('c_phi', 'K+', 'Cl-'): {
    #     'a1': -0.00084, # Christov
    #     'a2': 0,
    #     'a3': 0,
    #     'a4': 0,
    #     'a5': 0,
    #     'a6': 0,
    # },


    ('b0', 'K+', 'SO4-2'): {
        'a1': -0.7568e0,
        'a2': 0.2529e-2,
        'a3': 0.365e-7,
        'a4': 0.531e-9,
        'a5': -0.108e1,
        'a6': -0.125e-2,
    },
    ('b1', 'K+', 'SO4-2'): {
        'a1': 0.1953e1,
        'a2': -0.3996e-2,
        'a3': 0.355e-6,
        'a4': 0.1669e-7,
        'a5': 0.267e2,
        'a6': -0.4785e-1,
    },
    ('c_phi', 'K+', 'SO4-2'): {
        'a1': 0.70e-3,
        'a2': 0.48e-4,
        'a3': 0.90e-8,
        'a4': 0.326e-9,
        'a5': -0.768e1,
        'a6': 0.2835e-2,
    },
    ('b0', 'Ca+2', 'Cl-'): {
        'a1': -5.62764702e01,
        'a2': -3.00771997e-02,
        'a3': 1.05630400e-05,
        'a4': 3.3331626e-09,
        'a5': 1.11730349e03,
        'a6': 1.06664743e01,
    },
    ('b1', 'Ca+2', 'Cl-'): {
        'a1': 3.4787e00,
        'a2': -1.5417e-02,
        'a3': 3.1791e-05,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('c_phi', 'Ca+2', 'Cl-'): {
        'a1': 2.64231655e01,
        'a2': 2.46922993e-02,
        'a3': -2.48298510e-05,
        'a4': 1.22421864e-08,
        'a5': -4.18098427e02,
        'a6': -5.35350322e00,
    },

    ('b0', 'Ca+2', 'SO4-2'): {
        'a1': 0.795e-1,
        'a2': -0.122e-3,
        'a3': 0.5001e-5,
        'a4': 0.6704e-8,
        'a5': -0.15228e3,
        'a6': -0.6885e-2,
    },
    ('b1', 'Ca+2', 'SO4-2'): {
        'a1': 0.28945e1,
        'a2': 0.7434e-2,
        'a3': 0.5287e-5,
        'a4': -0.101513e-6,
        'a5': -0.208505e4,
        'a6': 0.1345e1,
    },
    ('b2', 'Ca+2', 'SO4-2'): {
        'a1': -0.5704e2,
        'a2': -0.1028e-1,
        'a3': -0.2235e-3,
        'a4': 0.3526e-6,
        'a5': 0.5788e4,
        'a6': -0.18378e1,
    },
    ('c_phi', 'Ca+2', 'SO4-2'): {
        'a1': 0.33e-1,
        'a2': -0.1529e-3,
        'a3': 0.897e-6,
        'a4': 0.1569e-8,
        'a5': 0.11e1,
        'a6': -0.12755e-1,
    },
    ('b0', 'Mg+2', 'Cl-'): {
        'a1': 3.13852913e02,
        'a2': 2.61769099e-01,
        'a3': -2.46268460e-04,
        'a4': 1.15764787e-07,
        'a5': -5.53133381e03,
        'a6': -6.21616862e01,
    },
    ('b1', 'Mg+2', 'Cl-'): {
        'a1': -3.18432525e04,
        'a2': -2.86710358e01,
        'a3': 2.78892838e-02,
        'a4': -1.3279705e-05,
        'a5': 5.24032958e05,
        'a6': 6.40770396e03,
    },
    ('c_phi', 'Mg+2', 'Cl-'): {
        'a1': 5.9532e-02,
        'a2': -2.49949e-04,
        'a3': 2.41831e-07,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },

    ('b0', 'Mg+2', 'SO4-2'): {
        'a1': 0.1678e1,
        'a2': -0.5514e-2,
        'a3': 0.597e-6,
        'a4': 0.15651e-7,
        'a5': -0.22392e3,
        'a6': 0.6594e-1,
    },

    ('b1', 'Mg+2', 'SO4-2'): {
        'a1': 0.1484e1,
        'a2': 0.6274e-2,
        'a3': 0.541e-5,
        'a4': 0.884e-7,
        'a5': -0.1321e4,
        'a6': 0.30605e0,
    },
    ('b2', 'Mg+2', 'SO4-2'): {
        'a1': 0.18829e3,
        'a2': -0.103999e1,
        'a3': 0.12242e-2,
        'a4': 0.34974e-5,
        'a5': 0.8975e5,
        'a6': -0.679235e2,
    },
    ('c_phi', 'Mg+2', 'SO4-2'): {
        'a1': 0.2230e0,
        'a2': -0.6101e-3,
        'a3': -0.10e-8,
        'a4': -0.1096e-8,
        'a5': 0.4265e2,
        'a6': -0.1792e-1,
    },
    ('theta', 'Na+', 'K+'): {
        'a1': -1.82266741e1,
        'a2': -3.69038470e-3,
        'a3': 0,
        'a4': 0,
        'a5': 6.12415011e2,
        'a6': 3.02994981e0,
    },
    ('theta', 'Na+', 'Ca+2'): {
        'a1': 0.30e-1,
        'a2': -0.19e-4,
        'a3': 0,
        'a4': 0.95e-9,
        'a5': -0.250e1,
        'a6': 0.13e-2,
    },
    # ('theta', 'Na+', 'Ca+2'): {
    #     'a1': 5.0e-2,
    #     'a2': 0,
    #     'a3': 0,
    #     'a4': 0,
    #     'a5': 0,
    #     'a6': 0,
    # },
    ('theta', 'Na+', 'Mg+2'): {
        'a1': 7.0e-02,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('theta', 'Na+', 'Li+'): {
        'a1': 0.012,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('theta', 'K+', 'Ca+2'): {
        'a1': 2.365710e00,
        'a2': -4.540e-03,
        'a3': 0,
        'a4': 0,
        'a5': -2.84940e02,
        'a6': 0,
    },
    ('theta', 'K+', 'Mg+2'): {
        'a1': 1.1670e-01,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('theta', 'Ca+2', 'Mg+2'): {
        'a1': 5.31274136e00,
        'a2': -6.3424248e-03,
        'a3': 0,
        'a4': 0,
        'a5': -9.83113847e02,
        'a6': 0,
    },
    ('theta', 'Cl-', 'SO4-2'): {
        'a1': 0.70e-1,
        'a2': 0,
        'a3': 0,
        'a4': -0.78e-9,
        'a5': -0.100e1,
        'a6': 0,
    },
    ('b0', 'Sr+2', 'Cl-'): {
        'a1': 0.28344,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('b1', 'Sr+2', 'Cl-'): {
        'a1': 1.625625,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('c_phi', 'Sr+2', 'Cl-'): {
        'a1': -0.00044547727,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('b0', 'Li+', 'Cl-'): {
        'a1': 0.14847,
        'a2': 0,
        'a3': 0,
        'a4': -1.546e-4,
        'a5': 0,
        'a6': 0,
    },
    ('b1', 'Li+', 'Cl-'): {
        'a1': 0.307,
        'a2': 0,
        'a3': 0,
        'a4': 6.36e-4,
        'a5': 0,
        'a6': 0,
    },
    ('c_phi', 'Li+', 'Cl-'): {
        'a1': 0.003710,
        'a2': 4.115,
        'a3': 0,
        'a4': 0,
        'a5': -3.71e-9,
        'a6': 0,
    },
    ('b0', 'Rb+', 'Cl-'): {
        'a1': 0.04319,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('b1', 'Rb+', 'Cl-'): {
        'a1': 0.15398,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('c_phi', 'Rb+', 'Cl-'): {
        'a1': -0.001098,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('b0', 'Cs+', 'Cl-'): {
        'a1': 0.03352,
        'a2': -1290.0,
        'a3': -8.4279,
        'a4': 0.018502,
        'a5': -6.7942e-6,
        'a6': 0,
    },
    ('b1', 'Cs+', 'Cl-'): {
        'a1': 0.0429,
        'a2': -38,
        'a3': 0,
        'a4': 0.001306,
        'a5': 0,
        'a6': 0,
    },
    ('c_phi', 'Cs+', 'Cl-'): {
        'a1': -2.62e-4,
        'a2': 157.13,
        'a3': 1.086,
        'a4': -0.0025242,
        'a5': 9.84e-7,
        'a6': 0,
    },
    ('b0', 'Ba+2', 'Cl-'): {
        'a1': 0.26280,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('b1', 'Ba+2', 'Cl-'): {
        'a1': 1.49625,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('c_phi', 'Ba+2', 'Cl-'): {
        'a1': -9.68913066e-03,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },

    ('b0', 'Mn+2', 'Cl-'): {
        'a1': 0.3322275,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('b1', 'Mn+2', 'Cl-'): {
        'a1': 1.514625,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('c_phi', 'Mn+2', 'Cl-'): {
        'a1': -0.011343760537185188,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('theta', 'Mn+2', 'Na+'): {
        'a1': 0.0432,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('b0', 'Zn+2', 'Cl-'): {
        'a1': 0.2282475,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('b1', 'Zn+2', 'Cl-'): {
        'a1': 1.731375,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('c_phi', 'Zn+2', 'Cl-'): {
        'a1': -0.03276379270627868,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('b0', 'Pb+2', 'Cl-'): {
        'a1': 0.26018,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('b1', 'Pb+2', 'Cl-'): {
        'a1': 1.64250,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('c_phi', 'Pb+2', 'Cl-'): {
        'a1': -0.08798,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('lambda', 'Na+', 'Cl-'): {
        'a1': 0,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
}

index = pd.MultiIndex.from_tuples([('pr1', 'pr2', 'pr3')], names=["parameter", "species1", "species2"])
df = pd.DataFrame(columns=['a1', 'a2', 'a3', 'a4', 'a5', 'a6'], index=index)
for key, value in species.items():
    df.loc[key, :] = pd.Series(value)
df.sort_index()

spencer_binary = df
