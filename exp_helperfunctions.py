#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:22:08 2020

@author: timo
"""
import Builder as Builder
import numpy as np

def run_exp(pop_start_size=10, pop_max_size=1280, n_iters=25, string_length=100,\
            value_func=Builder.counting_ones_fitness_func, global_optimum = 100,\
                crossover_operator=2):
    global_res = {key: [] for key in ['res_dict', 'iter', 'max_fitness']}
    for x in range(n_iters):
        N = pop_start_size
        res = {key: [] for key in ['Pop_size', 'best_fitness', 'generation_iter']}
        optimum_found = False
        sols = []
        for i in range(pop_start_size):
            values = np.random.randint(2, size=string_length)
            sol = Builder.Solution(values)
            sols.append(sol)
        first_gen = Builder.Population(solutions_list=sols, previous_iter=0)
        
        first_gen.shuffle_population()
        first_gen.pair_solutions()
        first_gen.create_offspring(crossover_operator=0)
        best_offspring = first_gen.family_competition(valuefunc = value_func)
        new_gen = Builder.Population(solutions_list=best_offspring, previous_iter=0)
        gen_x = new_gen
    
        while not optimum_found and N <= 1280:
            # log information for each iteration
            opt_reached = gen_x.global_optimum_reached(optimum = global_optimum, valuefunc = value_func)
            optimum_found = opt_reached
            current_optimum = gen_x.best_solution_fitness(valuefunc = value_func)
            res['Pop_size'].append(N)
            res['best_fitness'].append(current_optimum)
            res['generation_iter'].append(gen_x.current_iter)
            # do single iteration
            gen_x.shuffle_population()
            gen_x.pair_solutions()
            gen_x.create_offspring(crossover_operator=2)
            best_offspring = gen_x.family_competition(valuefunc = value_func)
            new_gen = Builder.Population(solutions_list=best_offspring, previous_iter = gen_x.current_iter)
            # check if next gen has a higher fitness function than current. if this is false, increase pop size (N)
            next_optimum = new_gen.best_solution_fitness(valuefunc = value_func)
            if current_optimum == next_optimum:
                # print('stuck in local optimum for fitness value of {}.\
                #       Upscaling N from {} to {}'.format(next_optimum, N, N+10))
                N+=10
                
            gen_x = new_gen
        global_res['res_dict'].append(res)
        global_res['iter'].append(x)
        global_res['max_fitness'].append(max(res['best_fitness']))
        print('found global fitness max of {}'.format(max(res['best_fitness'])))
        
    return global_res
    
        