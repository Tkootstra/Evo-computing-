#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:42:33 2020

@author: timo
"""
import exp_helperfunctions as helper
import Builder as builder
# LOOP VOOR 25 ITERS
# 1. Maak random populatie. N = 10. alleen multiples gebruiken
# LOOP
# 2. Doe crossover, family selection maak nieuwe children.
# 3. nieuwe gen wordt gemaakt: heeft iemand in de nieuwe gen de max fitness? stop dan, je bent klaar
# 4. niet global optimum? verdubbel N
# 5. N > 1280? werkt niet!
  
# END LOOP
# 6. global optimum gevonden: nu bisection search

# END LOOP 25

# 24/25 global opt -> werkt! anders niet
def evaluate_generation(generation, optimum, fitness_func):
    optimum_reached, best_fitness = generation.get_fitness(optimum, fitness_func)
    return optimum_reached, best_fitness
    
def generate(generation, optimum, fitness_func, crossover_operator):
    best_offspring = generation.step_gen(crossover_operator, fitness_func, cores=n_cores)
    new_gen = builder.Population(solutions_list=best_offspring, previous_iter=generation.current_iter)
    return new_gen
    
    
N = 10
glob_opt = 100
max_gen_iters = 100
n_cores = 1
fitness_function = builder.counting_ones_fitness_func
optimum_found = False
cross_over_operator = 2

while True:
    random_start_pop = helper.create_solutions(n=N, string_length=100)
    random_start_pop = builder.Population(random_start_pop,0)
    
    gen_x = random_start_pop
    
    
    for n in range(max_gen_iters):
        optimum_reached, best_fitness = evaluate_generation(gen_x, glob_opt, fitness_func=builder.counting_ones_fitness_func)
        if optimum_reached:
            print('found optimum of {} for generation {} and N of {}'.format(glob_opt, gen_x.current_iter, N))
            break
        new_gen = generate(gen_x,glob_opt,fitness_function, cross_over_operator)
        gen_x = new_gen
    if not optimum_reached:
        N = N * 2
        if N > 1280:
            N = 1280
    # else:
        # do bisection search
        
        
    
    
    
    
    
    



    





# N = N*2

