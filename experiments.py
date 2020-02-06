#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:24:20 2020

@author: timo
"""

import Builder as Builder
import numpy as np
# =============================================================================
# experiment 1: 2 experiments with crossover 2X and UX with sum fitnessfunc
# =============================================================================

# =============================================================================
# crossover 2x
# =============================================================================


res = {key: [] for key in ['Pop_size', 'best_fitness', 'generation_iter','offspring']}
optimum = 100
N = 10
string_length = 100
optimum_found = False
valuefunc = Builder.counting_ones_fitness_func
# generate first random generation
# geen idee hoe dit moet, maar nu gewoon random?
sols = []
for i in range(N):
    values = np.random.randint(2, size=string_length)
    sol = Builder.Solution(values)
    sols.append(sol)
first_gen = Builder.Population(solutions_list=sols, previous_iter=0)

first_gen.shuffle_population()
first_gen.pair_solutions()
first_gen.create_offspring(crossover_operator=2)
best_offspring = first_gen.family_competition(valuefunc = valuefunc)
new_gen = Builder.Population(solutions_list=best_offspring, previous_iter=0)
gen_x = new_gen


while not optimum_found and N <= 1280:
    # log information for each iteration
    opt_reached = gen_x.global_optimum_reached(optimum = optimum, valuefunc = valuefunc)
    optimum_found = opt_reached
    current_optimum = gen_x.best_solution_fitness(valuefunc = valuefunc)
    
    res['Pop_size'].append(N)
    res['best_fitness'].append(current_optimum)
    res['generation_iter'].append(gen_x.current_iter)
    # do single iteration
    gen_x.shuffle_population()
    gen_x.pair_solutions()
    gen_x.create_offspring(crossover_operator=2)
    best_offspring = gen_x.family_competition(valuefunc = valuefunc)
    new_gen = Builder.Population(solutions_list=best_offspring, previous_iter = gen_x.current_iter)
    # check if next gen has a higher fitness function than current. if this is false, increase pop size (N)
    next_optimum = new_gen.best_solution_fitness(valuefunc = valuefunc)
    if current_optimum == next_optimum:
        print('stuck in local optimum for fitness value of {}.\
              Upscaling N from {} to {}'.format(next_optimum, N, N+10))
        N+=10
        
    gen_x = new_gen
    


# =============================================================================
# crossover UX
# =============================================================================
import Builder as Builder
import numpy as np

res = {key: [] for key in ['Pop_size', 'best_fitness', 'generation_iter','offspring']}
optimum = 100
N = 10
string_length = 100
optimum_found = False
valuefunc = Builder.counting_ones_fitness_func
# generate first random generation
# geen idee hoe dit moet, maar nu gewoon random?
sols = []
for i in range(N):
    values = np.random.randint(2, size=string_length)
    sol = Builder.Solution(values)
    sols.append(sol)
first_gen = Builder.Population(solutions_list=sols, previous_iter=0)

first_gen.shuffle_population()
first_gen.pair_solutions()
first_gen.create_offspring(crossover_operator=0)
best_offspring = first_gen.family_competition(valuefunc = valuefunc)
new_gen = Builder.Population(solutions_list=best_offspring, previous_iter=0)
gen_x = new_gen


while not optimum_found and N <= 1280:
    # log information for each iteration
    opt_reached = gen_x.global_optimum_reached(optimum = optimum, valuefunc = valuefunc)
    optimum_found = opt_reached
    current_optimum = gen_x.best_solution_fitness(valuefunc = valuefunc)
    
    res['Pop_size'].append(N)
    res['best_fitness'].append(current_optimum)
    res['generation_iter'].append(gen_x.current_iter)
    # do single iteration
    gen_x.shuffle_population()
    gen_x.pair_solutions()
    gen_x.create_offspring(crossover_operator=2)
    best_offspring = gen_x.family_competition(valuefunc = valuefunc)
    new_gen = Builder.Population(solutions_list=best_offspring, previous_iter = gen_x.current_iter)
    # check if next gen has a higher fitness function than current. if this is false, increase pop size (N)
    next_optimum = new_gen.best_solution_fitness(valuefunc = valuefunc)
    if current_optimum == next_optimum:
        print('stuck in local optimum for fitness value of {}.\
              Upscaling N from {} to {}'.format(next_optimum, N, N+10))
        N+=10
        
    gen_x = new_gen
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    