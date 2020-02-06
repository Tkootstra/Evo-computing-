#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:24:20 2020

@author: timo
"""

import exp_helperfunctions
import Builder as Builder


# =============================================================================
# #1 - counting ones valuefunc with 2X crossover
# =============================================================================

results_1a = exp_helperfunctions.run_exp(pop_start_size=10, pop_max_size=1280, n_iters=25, string_length=100,\
            value_func=Builder.counting_ones_fitness_func, global_optimum = 100,\
                crossover_operator=2)      



# =============================================================================
# #1 - counting ones valuefunc with UX crossover
# =============================================================================

results_1b = exp_helperfunctions.run_exp(pop_start_size=10, pop_max_size=1280,\
            n_iters=25, string_length=100,value_func=Builder.counting_ones_fitness_func,\
            global_optimum = 100, crossover_operator=0)      
