# -*- coding: utf-8 -*-
# Author: Yiping Liu
# Description: This script calculates the average of a list of numbers.
# Version: 1.0
# Last Modified: May 7, 2023

import pandas as pd

pd.set_option('display.precision', 11)

species = {
    ('psi', 'Na+', 'K+', 'Cl-'): {
        'a1': 6.48108127e00,
        'a2': 1.46803468e-03,
        'a3': 0,
        'a4': 0,
        'a5': -2.04354019e02,
        'a6': -1.09448043e00,
    },
    ('psi', 'Na+', 'K+', 'SO4-2'): {
        'a1': -0.563e-1,
        'a2': 0.14146e-2,
        'a3': 0.23e-7,
        'a4': -0.21088e-7,
        'a5': -0.25661e3,
        'a6': 0.18538e0,
    },
    ('psi', 'Na+', 'Ca+2', 'Cl-'): {
        'a1': -7.63980e00,
        'a2': -1.2990e-02,
        'a3': 1.1060e-05,
        'a4': 0,
        'a5': 0,
        'a6': 1.8475e00,
    },
    ('psi', 'Na+', 'Ca+2', 'SO4-2'): {
        'a1': -0.808e-1,
        'a2': 0.46565e-2,
        'a3': 0.5546e-5,
        'a4': -0.14107e-6,
        'a5': -0.10915e4,
        'a6': 0.96985e0,
    },
    ('psi', 'Na+', 'Mg+2', 'Cl-'): {
        'a1': -3.109870e-2,
        'a2': 5.4464780e-5,
        'a3': 0,
        'a4': 0,
        'a5': 1.99404210e0,
        'a6': 0,
    },
    ('psi', 'Na+', 'Mg+2', 'SO4-2'): {
        'a1': -0.1207e0,
        'a2': 0.5235e-3,
        'a3': -0.539e-6,
        'a4': -0.439e-9,
        'a5': -0.1723e2,
        'a6': 0.12645e-1,
    },
    ('psi', 'K+', 'Ca+2', 'Cl-'): {
        'a1': -5.930e-02,
        'a2': 2.54280e-04,
        'a3': 0,
        'a4': 0,
        'a5': -1.34390e01,
        'a6': 0,
    },
    ('psi', 'K+', 'Mg+2', 'Cl-'): {
        'a1': 5.0362230e-02,
        'a2': -8.750820e-06,
        'a3': 0,
        'a4': 0,
        'a5': -2.899090e01,
        'a6': 0,
    },
    ('psi', 'K+', 'Mg+2', 'SO4-2'): {
        'a1': -0.118e0,
        'a2': -0.478e-4,
        'a3': -0.327e-6,
        'a4': -0.937e-9,
        'a5': 0.3344e2,
        'a6': -0.884e-2,
    },
    ('psi', 'Ca+2', 'Mg+2', 'Cl-'): {
        'a1': 4.15790220e01,
        'a2': 1.30377312e-02,
        'a3': 0,
        'a4': 0,
        'a5': -9.81658526e02,
        'a6': -7.4061986e00,
    },
    ('psi', 'Ca+2', 'Mg+2', 'SO4-2'): {
        'a1': 0.24e-1,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('psi', 'Cl-', 'SO4-2', 'Na+'): {
        'a1': 0.2554e-1,
        'a2': -0.6138e-4,
        'a3': -0.90e-8,
        'a4': 0.304e-9,
        'a5': -0.890e0,
        'a6': -0.2275e-2,
    },
    ('psi', 'Cl-', 'SO4-2', 'K+'): {
        'a1': 0.608e-1,
        'a2': -0.1824e-3,
        'a3': -0.215e-7,
        'a4': -0.328e-9,
        'a5': 0.522e1,
        'a6': -0.301e-2,
    },
    ('psi', 'Cl-', 'SO4-2', 'Ca+2'): {
        'a1': -0.263e-1,
        'a2': -0.946e-4,
        'a3': -0.3125e-6,
        'a4': -0.128e-8,
        'a5': 0.2944e2,
        'a6': -0.649e-2,
    },
    ('psi', 'Cl-', 'SO4-2', 'Mg+2'): {
        'a1': 0.5869e-1,
        'a2': -0.897e-4,
        'a3': 0.47e-7,
        'a4': 0.65e-10,
        'a5': -0.2413e2,
        'a6': 0.4345e-2,
    },
    ('psi', 'Cl-', 'Na+', 'Li+'): {
        'a1': -0.003,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('psi', 'Cl-', 'Na+', 'Mn+2'): {
        'a1': -0.0136,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('psi', 'Cl-', 'Na+', 'Ba+2'): {
        'a1': -0.003,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
    ('zeta', 'Cl-', 'Na+', 'K+'): {
        'a1': 0,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
    },
}

index = pd.MultiIndex.from_tuples([('pr1', 'pr2', 'pr3', 'pr4')],
                                  names=["parameter", "species1", "species2", "species3"])
df = pd.DataFrame(columns=['a1', 'a2', 'a3', 'a4', 'a5', 'a6'], index=index)
for key, value in species.items():
    df.loc[key, :] = pd.Series(value)
df.sort_index()

spencer_ternary = df
