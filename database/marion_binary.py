# -*- coding: utf-8 -*-
# Author: Yiping Liu
# Description: This script calculates the average of a list of numbers.
# Version: 1.0
# Last Modified: May 7, 2023

import pandas as pd

pd.set_option('display.precision', 11)

species = {
    ('b0', 'Fe+2', 'Cl-'): {
        'a1': 3.359E-1, # Marion et al. 2003
        # 'a1': 0.40942, # Christov, 2005
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('b1', 'Fe+2', 'Cl-'): {
        'a1': 3.83836e1,
        'a2': -1.236e-1,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    # ('b1', 'Fe+2', 'Cl-'): {
    #     'a1': 1.99612, # Christov, 2005
    #     'a2': 0,
    #     'a3': 0,
    #     'a4': 0,
    #     'a5': 0,
    #     'a6': 0,
    #     'a7': 0,
    # },
    # ('b2', 'Fe+2', 'Cl-'): {
    #     'a1': -0.34439, # Christov, 2005
    #     'a2': 0,
    #     'a3': 0,
    #     'a4': 0,
    #     'a5': 0,
    #     'a6': 0,
    #     'a7': 0,
    # },
    ('c_phi', 'Fe+2', 'Cl-'): {
        'a1': -8.61E-3,  # Marion et al. 2003
        # 'a1': -0.02643, # Christov, 2005
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('b0', 'Fe+2', 'HCO3-'): {
        'a1': 1.369710e4,
        'a2': 8.250840e0,
        'a3': -4.34e-3,
        'a4': 0,
        'a5': -2.7340617e5,
        'a6': -2.6071152e3,
        'a7': 0,
    },
    ('b1', 'Fe+2', 'HCO3-'): {
        'a1': -1.5783984e5,
        'a2': -9.2777935e1,
        'a3': 4.77642e-2,
        'a4': 0,
        'a5': 3.2032097e6,
        'a6': 2.9927152e4,
        'a7': 0,
    },
    ('c_phi', 'Fe+2', 'HCO3-'): {
        'a1': 0,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },

    ('b0', 'Fe+2', 'SO4-2'): {
        'a1': 1.29506e1,
        'a2': -3.86e-2,
        'a3': 3.91e-5,
        'a4': 0,
        'a5': -1.38964e3,
        'a6': 0,
        'a7': 0,
    },
    ('b1', 'Fe+2', 'SO4-2'): {
        'a1': 8.758343e1,
        'a2': -6.383194e-1,
        'a3': 1.190408e-3,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('b2', 'Fe+2', 'SO4-2'): {
        'a1': -4.20e1,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('c_phi', 'Fe+2', 'SO4-2'): {
        'a1': 2.09e-2,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('b0', 'Fe+2', 'HSO4-'): {
        'a1': 6.758464e1,
        'a2': -7.649696e-1,
        'a3': 2.894494e-3,
        'a4': -3.636364e-6,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('b1', 'Fe+2', 'HSO4-'): {
        'a1': 3.48e0,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('c_phi', 'Fe+2', 'HSO4-'): {
        'a1': 0,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('b0', 'Fe+2', 'NO3-'): {
        'a1': 5.207e-1,
        'a2': -5.1525e-4,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('b1', 'Fe+2', 'NO3-'): {
        'a1': 2.9242e0,
        'a2': -4.4925e-3,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('c_phi', 'Fe+2', 'NO3-'): {
        'a1': -2.062e-2,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('b0', 'FeOH+', 'OH-'): {
        'a1': -1.0e-1,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('b1', 'FeOH+', 'OH-'): {
        'a1': 1.658e0,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('c_phi', 'FeOH+', 'OH-'): {
        'a1': 0,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('theta', 'Fe+2', 'Na+'): {
        'a1': 8.0e-2, # Marion et al. 2003
        # 'a1': 0.10945,
        # 'a1': 0, # Christov 2004
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('theta', 'Fe+2', 'K+'): {
        # 'a1': -0.18,   # Christov, 2004
        # 'a1': 0.02737, # Woog,2004
        'a1': 1.167e-1,  # Marion 2003
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('theta', 'Fe+2', 'H+'): {
        'a1': 0,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('theta', 'Fe+2', 'Mg+2'): {
        'a1': 0,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },
    ('theta', 'Fe+2', 'Ca+2'): {
        'a1': 5.31274136e0,
        'a2': -6.3424248e-3,
        'a3': 0,
        'a4': 0,
        'a5': -9.83113847e2,
        'a6': 0,
        'a7': 0,
    },
    ('lambda', 'Fe+2', 'Ca+2'): {
        'a1': 0,
        'a2': 0,
        'a3': 0,
        'a4': 0,
        'a5': 0,
        'a6': 0,
        'a7': 0,
    },


}

index = pd.MultiIndex.from_tuples([('pr1', 'pr2', 'pr3')], names=["parameter", "species1", "species2"])
df = pd.DataFrame(columns=['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'], index=index)
for key, value in species.items():
    df.loc[key, :] = pd.Series(value)
df.sort_index()

marion_binary = df

