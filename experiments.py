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
print('\nEXPERIMENT 1: 2X')
results_1a = exp_helperfunctions.run_exp(pop_start_size=10, pop_max_size=1280, n_iters=25, string_length=100,\
            value_func=Builder.counting_ones_fitness_func, global_optimum = 100,\
                crossover_operator=2)      



# =============================================================================
# #1 - counting ones valuefunc with UX crossover
# =============================================================================
print('\nEXPERIMENT 1: UX')
results_1b = exp_helperfunctions.run_exp(pop_start_size=10, pop_max_size=1280,\
            n_iters=25, string_length=100,value_func=Builder.counting_ones_fitness_func,\
            global_optimum = 100, crossover_operator=0)      


# # =============================================================================
# # #2 - linked deceptive trap with 2X crossover
# # =============================================================================
# print('\nEXPERIMENT 2: 2X')
# results_2a = exp_helperfunctions.run_exp(pop_start_size=10, pop_max_size=1280,\
#             n_iters=25, string_length=100,value_func=Builder.dec_linked_trap_fitness,\
#             global_optimum = 100, crossover_operator=2) 


# # =============================================================================
# # #2 - linked deceptive trap with UX crossover
# # =============================================================================
# print('\nEXPERIMENT 2: UX')
# results_2b = exp_helperfunctions.run_exp(pop_start_size=10, pop_max_size=1280,\
#             n_iters=25, string_length=100,value_func=Builder.dec_linked_trap_fitness,\
#             global_optimum = 100, crossover_operator=0) 
    

# # =============================================================================
# # #3 - linked non-deceptive trap with 2X crossover
# # =============================================================================
# print('\nEXPERIMENT 3: 2X')
# results_3a = exp_helperfunctions.run_exp(pop_start_size=10, pop_max_size=1280,\
#             n_iters=25, string_length=100,value_func=Builder.non_dec_linked_trap_fitness,\
#             global_optimum = 100, crossover_operator=2) 


# # =============================================================================
# # #3 - linked non-deceptive trap with UX crossover
# # =============================================================================
# print('\nEXPERIMENT 3: UX')
# results_3b = exp_helperfunctions.run_exp(pop_start_size=10, pop_max_size=1280,\
#             n_iters=25, string_length=100,value_func=Builder.non_dec_linked_trap_fitness,\
#             global_optimum = 100, crossover_operator=0) 