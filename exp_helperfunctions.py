#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:22:08 2020

@author: timo
"""
import Builder as Builder
import numpy as np
import time

def run_exp(pop_start_size=10, pop_max_size=1280, n_iters=25, string_length=100,\
            value_func=Builder.counting_ones_fitness_func, global_optimum = 100,\
                crossover_operator=2):
    
    global_res = {key: [] for key in ['res_dict', 'iter', 'max_fitness']}
    
    for x in range(n_iters):
        start = time.time()
        
        res = {key: [] for key in ['Pop_size', 'best_fitness', 'generation_iter']}
        
        N = pop_start_size
        num_gens = 1
        optimum_found = False
        
        while N <= pop_max_size and not optimum_found:
            sols = []
            
            for i in range(N):
                values = np.random.randint(2, size=string_length)
                sol = Builder.Solution(values)
                sols.append(sol)
            
            # Build first gen and find its fitness
            first_gen = Builder.Population(solutions_list=sols, previous_iter=0)
            optimum_found = first_gen.global_optimum_reached(optimum = global_optimum, valuefunc = value_func)
            current_optimum = first_gen.best_solution_fitness(valuefunc = value_func)
            
            # Create and select offspring
            first_gen.shuffle_population()
            first_gen.pair_solutions()
            first_gen.create_offspring(crossover_operator=crossover_operator)
            best_offspring = first_gen.family_competition(valuefunc = value_func)
            
            # Build new generation and check fitness
            new_gen = Builder.Population(solutions_list=best_offspring, previous_iter=1)
            optimum_found = new_gen.global_optimum_reached(optimum = global_optimum, valuefunc = value_func)
            next_optimum = new_gen.best_solution_fitness(valuefunc = value_func)
            
            gen_x = new_gen
        
            while not optimum_found and current_optimum < next_optimum:
                current_optimum = next_optimum
                
                # do single iteration
                gen_x.shuffle_population()
                gen_x.pair_solutions()
                gen_x.create_offspring(crossover_operator=crossover_operator)
                best_offspring = gen_x.family_competition(valuefunc = value_func)
                new_gen = Builder.Population(solutions_list=best_offspring, previous_iter = gen_x.current_iter)
                
                # check if next gen has a higher fitness function than current. if this is false, increase pop size (N)
                next_optimum = new_gen.best_solution_fitness(valuefunc = value_func)

                    
                gen_x = new_gen
                num_gens += 1
                # print(num_gens)
            
            res['Pop_size'].append(N)
            res['best_fitness'].append(current_optimum)
            res['generation_iter'].append(gen_x.current_iter)
            
            last_N = N
            N *= 2
        
        global_res['res_dict'].append(res)
        global_res['iter'].append(x)
        global_res['max_fitness'].append(max(res['best_fitness']))
        
        fitness = (max(res['best_fitness']) / global_optimum) * 100
        mean_gens = np.mean(res['generation_iter'])
        
        end = time.time()
        print('{0}: Found global fitness max of {1:.0f}%, N={2}. ({3:.2f}s, {4:.2f} gens)'.format(x + 1, 
                                                                       fitness,
                                                                       last_N,
                                                                       end - start,
                                                                       mean_gens))
        
    return global_res
    
        