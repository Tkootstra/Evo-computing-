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

class Solution():
    
    def __init__(self, values:np.array):
        
        self.value_vector = np.array(values, dtype=bool)
        self.length = len(self.value_vector)
# =============================================================================
#     fitness functions
# =============================================================================
def counting_ones_fitness_func(solution):
    return np.sum(solution.value_vector)

def create_new_children(parent_solution1, parent_solution2, n_crossover):
        pa1 = parent_solution1.value_vector
        pa2 = parent_solution2.value_vector
         # do uniform crossover
        if n_crossover == 0:
        # make one child first, then inverse to make second one
            child_a = np.zeros(len(pa1))
    
            for i, (a,b) in enumerate(zip(pa1, pa2)):
                first = np.random.choice(list((a,b)),1, replace=False)[0]
                child_a[i] += first
            
            # do n-point crossover

        elif n_crossover == 2:
            child_a = np.zeros(len(pa1),dtype=bool)
            # define edges for crossover points
            borders = np.random.randint(0, high=100, size=2)
            first_border, second_border = borders[0], borders[1]
            if int(np.random.randint(0,high=100,size=1)) > 50:
                child_a[0:first_border] += pa1[0:first_border]
                child_a[first_border:second_border] += pa2[first_border:second_border]
                child_a[second_border:len(pa1)] += pa1[second_border:len(pa1)]
            else:
                child_a[0:first_border] += pa2[0:first_border]
                child_a[first_border:second_border] += pa1[first_border:second_border]
                child_a[second_border:len(pa1)] += pa2[second_border:len(pa1)]
            
              
                
        else:
            raise ValueError('{}-point crossover is currently not supported'.format(n_crossover))
                
        
        child_b = np.array(1-child_a)
        if len(child_b) > 100 or len(child_a) > 100:
            print('AHAAAAAAAAAHHH')
        return Solution(child_a), Solution(child_b)
    
class Population():
    
    def __init__(self, solutions_list:list, previous_iter:int):
        self.solutions = solutions_list
        self.current_iter = previous_iter+1
        self.new_pairs = []
        self.offspring = []
        self.population_size = len(solutions_list)
    
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
        
        
    def shuffle_population(self):
        sols = self.solutions
        random.shuffle(sols)
        self.solutions = sols
        
    def pair_solutions(self):
        for i in range(0,len(self.solutions), 2):
            parent_one = self.solutions[i]
            parent_two = self.solutions[i+1]
            self.new_pairs.append((parent_one, parent_two))

    def create_offspring(self, crossover_operator):
        for pa1, pa2 in self.new_pairs:
            first_child, second_child = create_new_children(pa1,pa2, crossover_operator)
            self.offspring.append(first_child)
            self.offspring.append(second_child)
    
    def family_competition(self, valuefunc):
        
        best_children = []
        # sample families (2 parents and those children)
    
        for i in range(0,len(self.solutions),2):
            candidates = []
            candidates.append(self.solutions[i])
            candidates.append(self.solutions[i+1])
            candidates.append(self.offspring[i])
            candidates.append(self.offspring[i+1])
            # check the fittest solutions for this family
            function_values = np.array([valuefunc(sol) for sol in candidates])
            best_idx = function_values.argsort()[-2:]
            # append 2 best solution to list
            best_children.append(candidates[best_idx[0]])
            best_children.append(candidates[best_idx[1]])
        return best_children



        
        
            
            
            
            
        
        
        
        
    
    
        
        
        
    