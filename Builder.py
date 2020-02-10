#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:23:03 2020

@author: timo
"""
# =============================================================================
# Builder classes solution and population. Use the functions of these classes to initiate the GA
# =============================================================================
import numpy as np
import random
from joblib import Parallel, delayed 

class Solution():
    
    def __init__(self, values:np.array):
        
        self.value_vector = np.array(values, dtype=bool)
        self.length = len(self.value_vector)

# =============================================================================
#     fitness functions
# =============================================================================
def counting_ones_fitness_func(solution):
    return np.sum(solution.value_vector)

def dec_linked_trap_fitness(solution, k=4, d=1):
    co = counting_ones_fitness_func(solution)
    if co % k == 0 and co > 0:
        return co
    else:
        return k - d - ((k - d) / (k - 1)) * co


def non_dec_linked_trap_fitness(solution, k=4, d=2.5):
    co = counting_ones_fitness_func(solution)
    if co % k == 0 and co > 0:
        return co
    else:
        return k - d - ((k - d) / (k - 1)) * co

# TODO: Non-linked functions

def mutate(solution):
        # mutate_location = np.random.randint(0, len(solution), 1)[0]
        # solution[mutate_location] = np.invert(solution[mutate_location])
        
        return solution

def create_new_children(parents, n_crossover):
        pa1 = parents[0].value_vector
        pa2 = parents[1].value_vector
        
        # do uniform crossover
        if n_crossover == 0:
            child_a = np.zeros(len(pa1), dtype=bool)
            child_b = np.zeros(len(pa1), dtype=bool)
    
            for i, (a, b) in enumerate(zip(pa1, pa2)):
                options = [a, b]
                
                first = np.random.choice(options, 1)[0]
                second = np.random.choice(options, 1)[0]
                child_a[i] += first
                child_b[i] += second
            
            # child_a = mutate(child_a)
            # child_b = mutate(child_b)
            
            return Solution(child_a), Solution(child_b)
        
        # do 2-point crossover
        elif n_crossover == 2:
            child_a = np.zeros(len(pa1),dtype=bool)
            # define edges for crossover points
            borders = np.random.randint(0, high=len(pa1), size=2)
            first_border, second_border = borders[0], borders[1]

            
            # if int(np.random.randint(0,high=100,size=1)) > 50:
            #     child_a[0:first_border] += pa1[0:first_border]
            #     child_a[first_border:second_border] += pa2[first_border:second_border]
            #     child_a[second_border:len(pa1)] += pa1[second_border:len(pa1)]
            # else:
            #     child_a[0:first_border] += pa2[0:first_border]
            #     child_a[first_border:second_border] += pa1[first_border:second_border]
            #     child_a[second_border:len(pa1)] += pa2[second_border:len(pa1)]
            
            child_a[0:first_border] = pa1[0:first_border]
            child_a[first_border:second_border] = pa2[first_border:second_border]
            child_a[second_border:len(pa1)] = pa1[second_border:len(pa1)]
            
            child_b = np.invert(child_a)
            
            # child_a = mutate(child_a)
            # child_b = mutate(child_b)
            
            if len(child_b) != len(pa1) or len(child_a) != len(pa1):
                print('AHAAAAAAAAAHHH') # haha
            
            return Solution(child_a), Solution(child_b)   
                
        else:
            raise ValueError('{}-point crossover is currently not supported'.format(n_crossover))
                
        
        
    
class Population():
    
    def __init__(self, solutions_list:list, previous_iter:int):
        self.solutions = solutions_list
        self.current_iter = previous_iter+1
        self.new_pairs = []
        self.offspring = []
        self.population_size = len(solutions_list)

    def get_fitness(self, optimum, valuefunc):
        return (self.global_optimum_reached(optimum, valuefunc), 
                self.best_solution_fitness(valuefunc))
    
    def global_optimum_reached(self, optimum, valuefunc):
        function_values = [valuefunc(sol) for sol in self.solutions]
        if max(function_values) == optimum:
            return True
        return False
    
    def best_solution_fitness(self, valuefunc):
        values = []
        for to_check in self.solutions:
            value = valuefunc(to_check)
            values.append(value)
        
        return max(values)

    def step_gen(self, crossover_operator, valuefunc, cores):
        self.shuffle_population()
        self.pair_solutions()
        self.create_offspring(crossover_operator, cores=cores)
        
        return self.family_competition(valuefunc)
        
    def shuffle_population(self):
        sols = self.solutions
        random.shuffle(sols)
        self.solutions = sols
        
    def pair_solutions(self):
        for i in range(0,len(self.solutions), 2):
            parent_one = self.solutions[i]
            parent_two = self.solutions[i+1]
            self.new_pairs.append((parent_one, parent_two))

    def create_offspring(self, crossover_operator, cores):
        if cores == 1:
            for parent in self.new_pairs:            
                first_child, second_child = create_new_children(parent, crossover_operator)
                self.offspring.append(first_child)
                self.offspring.append(second_child) 
       
        else:
            xovers = [crossover_operator] * len(self.new_pairs)
            
            children = Parallel(n_jobs=-2, backend='loky', verbose=False)(
                delayed(create_new_children)(pa, xover) for pa, xover in zip(self.new_pairs, xovers))
            
            for c1, c2 in children:
                self.offspring.append(c1)
                self.offspring.append(c2)
                
    
    def family_competition(self, valuefunc):
        
        best_children = []
        # sample families (2 parents and those children)
    
        for i in range(0,len(self.solutions),2):
            candidates = []
            candidates.append(self.solutions[i])
            candidates.append(self.solutions[i+1])
            candidates.append(self.offspring[i])
            candidates.append(self.offspring[i+1])
            
            # for cand in candidates:
            #     print(cand.value_vector)
            
            # check the fittest solutions for this family
            function_values = np.array([valuefunc(sol) for sol in candidates])
            best_idx = function_values.argsort()[::-1]
            
            # append 2 best solution to list
            best_children.append(candidates[best_idx[0]])
            best_children.append(candidates[best_idx[1]])
        
        return best_children



        
        
            
            
            
            
        
        
        
        
    
    
        
        
        
    