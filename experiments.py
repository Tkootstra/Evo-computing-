#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:24:20 2020

@author: timo
"""

import exp_helperfunctions
import Builder as Builder
import pickle

POP_START = 10
POP_MAX = 1280
N_ITERS = 25
STRING_LENGTH = 100
GLOBAL_OPTIMUM = STRING_LENGTH
MAX_GENS = 500
N_CORES = -2 # All but 1

# =============================================================================
# #1 - counting ones valuefunc with 2X crossover
# =============================================================================
print('\nEXPERIMENT 1a: 2X')
results_1a = exp_helperfunctions.run_exp(POP_START, POP_MAX,\
            N_ITERS, STRING_LENGTH,value_func=Builder.counting_ones_fitness_func,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=2, max_gens=100)   
pickle.dump(results_1a, open("1a.p", "wb" ))

# =============================================================================
# #1 - counting ones valuefunc with UX crossover
# =============================================================================
print('\nEXPERIMENT 1b: UX')
results_1b = exp_helperfunctions.run_exp(POP_START, POP_MAX,\
            N_ITERS, STRING_LENGTH,value_func=Builder.counting_ones_fitness_func,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=0, max_gens=100)      
pickle.dump(results_1b, open("1b.p", "wb" ))

# =============================================================================
# #2 - linked deceptive trap with 2X crossover
# =============================================================================
print('\nEXPERIMENT 2a: 2X')
results_2a = exp_helperfunctions.run_exp(POP_START, POP_MAX,\
            N_ITERS, STRING_LENGTH,value_func=Builder.dec_linked_trap_fitness,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=2, max_gens=300) 
pickle.dump(results_2a, open("2a.p", "wb" ))

# =============================================================================
# #2 - linked deceptive trap with UX crossover
# =============================================================================
print('\nEXPERIMENT 2b: UX')
results_2b = exp_helperfunctions.run_exp(POP_START, POP_MAX,\
            N_ITERS, STRING_LENGTH,value_func=Builder.dec_linked_trap_fitness,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=0, max_gens=300, n_cores=N_CORES) 
pickle.dump(results_2b, open("2b.p", "wb" ))    

# =============================================================================
# #3 - linked non-deceptive trap with 2X crossover
# =============================================================================
print('\nEXPERIMENT 3a: 2X')
results_3a = exp_helperfunctions.run_exp(POP_START, POP_MAX,\
            N_ITERS, STRING_LENGTH,value_func=Builder.non_dec_linked_trap_fitness,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=2, max_gens=MAX_GENS, n_cores=N_CORES) 
pickle.dump(results_3a, open("3a.p", "wb" ))

# =============================================================================
# #3 - linked non-deceptive trap with UX crossover
# =============================================================================
print('\nEXPERIMENT 3b: UX')
results_3b = exp_helperfunctions.run_exp(POP_START, POP_MAX,\
            N_ITERS, STRING_LENGTH,value_func=Builder.non_dec_linked_trap_fitness,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=0, max_gens=MAX_GENS, n_cores=N_CORES) 
pickle.dump(results_3b, open("3b.p", "wb" )) 
    
# =============================================================================
# #4 - non-linked deceptive trap with 2X crossover
# =============================================================================
print('\nEXPERIMENT 4a: 2X')
results_4a = exp_helperfunctions.run_exp(POP_START, POP_MAX,\
            N_ITERS, STRING_LENGTH,value_func=Builder.dec_non_linked_trap_fitness,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=2, max_gens=MAX_GENS, n_cores=N_CORES) 
pickle.dump(results_4a, open("4a.p", "wb" ))

# =============================================================================
# #4 - non-linked deceptive trap with UX crossover
# =============================================================================
print('\nEXPERIMENT 4b: UX')
results_4b = exp_helperfunctions.run_exp(POP_START, POP_MAX,\
            N_ITERS, STRING_LENGTH,value_func=Builder.dec_non_linked_trap_fitness,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=0, max_gens=MAX_GENS, n_cores=N_CORES)     
pickle.dump(results_4b, open("4b.p", "wb" ))     

# =============================================================================
# #5 - non-linked non-deceptive trap with 2X crossover
# =============================================================================
print('\nEXPERIMENT 5a: 2X')
results_5a = exp_helperfunctions.run_exp(POP_START, POP_MAX,\
            N_ITERS, STRING_LENGTH,value_func=Builder.non_dec_non_linked_trap_fitness,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=2, max_gens=MAX_GENS, n_cores=N_CORES) 
pickle.dump(results_5a, open("5a.p", "wb" ))

# =============================================================================
# #5 - non-linked non-deceptive trap with UX crossover
# =============================================================================
print('\nEXPERIMENT 5b: UX')
results_5b = exp_helperfunctions.run_exp(POP_START, POP_MAX,\
            N_ITERS, STRING_LENGTH,value_func=Builder.non_dec_non_linked_trap_fitness,\
            global_optimum = GLOBAL_OPTIMUM, crossover_operator=0, max_gens=MAX_GENS, n_cores=N_CORES)     
pickle.dump(results_5b, open("5b.p", "wb" ))    
    
    