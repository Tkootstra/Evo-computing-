#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:22:08 2020

@author: timo
"""
import Builder as Builder
import random
import time
import matplotlib.pyplot as plt


def create_solutions(n, string_length):
    sols = []
    for i in range(n):
        values = []
        for s in range(string_length):
            values.append(random.randint(0, 1))
#        values = np.random.randint(2, size=string_length)
        sol = Builder.Solution(values)
        sols.append(sol)
    
    return sols


def run_exp(pop_start_size=10, pop_max_size=1280, n_iters=25, string_length=100,\
            value_func=Builder.counting_ones_fitness_func, global_optimum = 100,\
                crossover_operator=2, max_gens=100, n_cores=1):
    
    global_res = {key: [] for key in ['res_dict', 'iter', 'max_fitness', 'cpu_time']}
    
    for x in range(n_iters):
        start = time.time()
        
        res = {key: [] for key in ['Pop_size', 'best_fitness', 'generation_iter', 'proportions', 'eval_functions']}
        
        N = pop_start_size
        optimum_found = False
        
        while N <= pop_max_size and not optimum_found:
            props = []
            counter = []
            num_gens = 1
            
            sols = create_solutions(N, string_length)
            
            # Build first gen and find its fitness
            first_gen = Builder.Population(solutions_list=sols, previous_iter=0)
            optimum_found, current_optimum = first_gen.get_fitness(global_optimum, value_func)
            
            # Create and select offspring
            best_offspring = first_gen.step_gen(crossover_operator, value_func, cores=n_cores)
            
            # Build new generation and check fitness
            new_gen = Builder.Population(solutions_list=best_offspring, previous_iter=1)
            optimum_found, next_optimum = new_gen.get_fitness(global_optimum, value_func)
            
            props.append(next_optimum)
            counter.append(num_gens)
            gen_x = new_gen
            num_gens += 1
        
            while not optimum_found and current_optimum <= next_optimum and num_gens <= max_gens:
                current_optimum = next_optimum
                
                # Create and select offspring
                best_offspring = gen_x.step_gen(crossover_operator, value_func, cores=n_cores)
                
                # Build new generation and check fitness
                new_gen = Builder.Population(solutions_list=best_offspring, previous_iter = gen_x.current_iter)
                optimum_found, next_optimum = new_gen.get_fitness(global_optimum, value_func)
                
                props.append(next_optimum)
                counter.append(num_gens)
                gen_x = new_gen
                num_gens += 1
                
            
            res['Pop_size'].append(N)
            res['best_fitness'].append(next_optimum)
            res['generation_iter'].append(num_gens)
            res['eval_functions'].append(num_gens * N)
            
#            plt.plot(counter, props)
#            plt.title('N={}'.format(N))
#            plt.show()
            
            last_N = N
            N *= 2
        
        ##############################################
        ### Optimum was found. Do bisection search ###
        ##############################################            
        if optimum_found:            
            stepsize = (last_N - last_N / 2) / 2
            N = last_N - stepsize
            
            while stepsize >= pop_start_size:
                props = []
                counter = []
                num_gens = 1
                last_N = N
                
                # Do generations until optimum is found or not
                sols = create_solutions(int(N), string_length)
                first_gen = Builder.Population(solutions_list=sols, previous_iter=0)
                optimum_found, current_optimum = first_gen.get_fitness(global_optimum, value_func)
                
                best_offspring = first_gen.step_gen(crossover_operator, value_func, cores=n_cores)
                
                new_gen = Builder.Population(solutions_list=best_offspring, previous_iter=1)
                optimum_found, next_optimum = new_gen.get_fitness(global_optimum, value_func)
                
                props.append(next_optimum)
                counter.append(num_gens)
                gen_x = new_gen
                num_gens += 1
                
                while not optimum_found and current_optimum <= next_optimum and num_gens < max_gens:
                    current_optimum = next_optimum
                    best_offspring = gen_x.step_gen(crossover_operator, value_func, cores=n_cores)
                
                    new_gen = Builder.Population(solutions_list=best_offspring, previous_iter = gen_x.current_iter)
                    optimum_found, next_optimum = new_gen.get_fitness(global_optimum, value_func)

                    props.append(next_optimum)
                    counter.append(num_gens)
                    gen_x = new_gen
                    num_gens += 1
                    
                # Write to dict
                res['Pop_size'].append(N)
                res['best_fitness'].append(next_optimum)
                res['generation_iter'].append(num_gens)
                res['eval_functions'].append(num_gens * N)
                
                # plt.plot(counter, props)
                # plt.title('N={}'.format(N))
                # plt.show()
                
                if optimum_found:
                    N -= stepsize
                else:
                    N += stepsize
                
                # Change stepsize
                stepsize /= 2
            
        
        fitness = (max(res['best_fitness']) / global_optimum) * 100
        mean_gens = sum(res['generation_iter']) / len(res['generation_iter'])
        
        end = time.time()
        print('{0}: Found global fitness max of {1:.0f}%, N={2} ({3:.2f}s, {4:.2f} gens)'.format(x + 1, 
                                                                       fitness,
                                                                       int(last_N),
                                                                       end - start,
                                                                       mean_gens))
        
        
        global_res['res_dict'].append(res)
        global_res['iter'].append(x)
        global_res['max_fitness'].append(max(res['best_fitness']))
        global_res['cpu_time'].append(end - start)
        
    return global_res
    
        