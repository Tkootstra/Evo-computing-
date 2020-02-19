#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:24:20 2020

@author: timo
"""

import exp_helperfunctions
import Builder as Builder

POP_START = 10
POP_MAX = 1280
N_ITERS = 5
STRING_LENGTH = 100
GLOBAL_OPTIMUM = STRING_LENGTH
MAX_GENS = 20
N_CORES = -2 # All but 1

# =============================================================================
# #1 - counting ones valuefunc with 2X crossover
# =============================================================================
print('\nEXPERIMENT 1a: 2X')
results_1a = exp_helperfunctions.run_exp(pop_start_size=POP_START, pop_max_size=POP_MAX,\
            n_iters=N_ITERS, string_length=STRING_LENGTH,value_func=Builder.counting_ones_fitness_func,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=2, max_gens=MAX_GENS)   


# =============================================================================
# #1 - counting ones valuefunc with UX crossover
# =============================================================================
print('\nEXPERIMENT 1b: UX')
results_1b = exp_helperfunctions.run_exp(pop_start_size=POP_START, pop_max_size=POP_MAX,\
            n_iters=N_ITERS, string_length=STRING_LENGTH,value_func=Builder.counting_ones_fitness_func,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=0, max_gens=MAX_GENS)      


# =============================================================================
# #2 - linked deceptive trap with 2X crossover
# =============================================================================
print('\nEXPERIMENT 2a: 2X')
results_2a = exp_helperfunctions.run_exp(pop_start_size=POP_START, pop_max_size=POP_MAX,\
            n_iters=N_ITERS, string_length=STRING_LENGTH,value_func=Builder.dec_linked_trap_fitness,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=2, max_gens=MAX_GENS) 


# =============================================================================
# #2 - linked deceptive trap with UX crossover
# =============================================================================
print('\nEXPERIMENT 2b: UX')
results_2b = exp_helperfunctions.run_exp(pop_start_size=POP_START, pop_max_size=POP_MAX,\
            n_iters=N_ITERS, string_length=STRING_LENGTH,value_func=Builder.dec_linked_trap_fitness,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=0, max_gens=MAX_GENS) 
    

# =============================================================================
# #3 - linked non-deceptive trap with 2X crossover
# =============================================================================
print('\nEXPERIMENT 3a: 2X')
results_3a = exp_helperfunctions.run_exp(pop_start_size=POP_START, pop_max_size=POP_MAX,\
            n_iters=N_ITERS, string_length=STRING_LENGTH,value_func=Builder.non_dec_linked_trap_fitness,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=2, max_gens=MAX_GENS, n_cores=N_CORES) 


# =============================================================================
# #3 - linked non-deceptive trap with UX crossover
# =============================================================================
print('\nEXPERIMENT 3b: UX')
results_3b = exp_helperfunctions.run_exp(pop_start_size=POP_START, pop_max_size=POP_MAX,\
            n_iters=N_ITERS, string_length=STRING_LENGTH,value_func=Builder.non_dec_linked_trap_fitness,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=0, max_gens=MAX_GENS, n_cores=N_CORES) 

    
# =============================================================================
# #4 - non-linked deceptive trap with 2X crossover
# =============================================================================
print('\nEXPERIMENT 4a: 2X')
results_4a = exp_helperfunctions.run_exp(pop_start_size=POP_START, pop_max_size=POP_MAX,\
            n_iters=N_ITERS, string_length=STRING_LENGTH,value_func=Builder.dec_non_linked_trap_fitness,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=2, max_gens=MAX_GENS, n_cores=N_CORES) 


# =============================================================================
# #4 - non-linked deceptive trap with UX crossover
# =============================================================================
print('\nEXPERIMENT 4b: UX')
results_4b = exp_helperfunctions.run_exp(pop_start_size=POP_START, pop_max_size=POP_MAX,\
            n_iters=N_ITERS, string_length=STRING_LENGTH,value_func=Builder.dec_non_linked_trap_fitness,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=0, max_gens=MAX_GENS, n_cores=N_CORES)     
    
    
    
    
    