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
import time

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


def dec_non_linked_trap_fitness(solution):
    if solution.length % 4 != 0:
        raise ValueError("Input must be multiple of 4")
    
    fitness = []
    stepsize = int(solution.length / 4)
    
    for i in range(stepsize):
        f = [solution.value_vector[i],
             solution.value_vector[i + stepsize],
             solution.value_vector[i + stepsize * 2],
             solution.value_vector[i + stepsize * 3]]
        
        fitness.append(dec_linked_trap_fitness(Solution(f)))
    
    return sum(fitness)


def non_dec_linked_trap_fitness(solution, k=4, d=2.5):
    co = counting_ones_fitness_func(solution)
    if co % k == 0 and co > 0:
        return co
    else:
        return k - d - ((k - d) / (k - 1)) * co


def non_dec_non_linked_trap_fitness(solution):
    if solution.length % 4 != 0:
        raise ValueError("Input must be multiple of 4")
    
    fitness = []
    stepsize = int(solution.length / 4)
    
    for i in range(stepsize):
        f = [solution.value_vector[i],
             solution.value_vector[i + stepsize],
             solution.value_vector[i + stepsize * 2],
             solution.value_vector[i + stepsize * 3]]
        
        fitness.append(non_dec_linked_trap_fitness(Solution(f)))
    
    return sum(fitness)

# =============================================================================
# Crossover functions
# =============================================================================
def n_point_xover(pa1, pa2):
    parent_length = len(pa1)
    
    child_a = np.zeros(parent_length,dtype=bool)
    child_b = np.zeros(parent_length,dtype=bool)
    
    # define edges for crossover points
    borders = np.random.randint(0, high=parent_length, size=2)
    first_border, second_border = borders[0], borders[1]
    
    # Create child a
    child_a[0:first_border] = pa1[0:first_border]
    child_a[first_border:second_border] = pa2[first_border:second_border]
    child_a[second_border:parent_length] = pa1[second_border:parent_length]

    # Create child b    
    child_b[0:first_border] = pa2[0:first_border]
    child_b[first_border:second_border] = pa1[first_border:second_border]
    child_b[second_border:parent_length] = pa2[second_border:parent_length]
    
    return Solution(child_a), Solution(child_b)

def uniform_xover(pa1, pa2):
    child_a = np.zeros(len(pa1), dtype=bool)
    child_b = np.zeros(len(pa1), dtype=bool)
    
    for i, (a, b) in enumerate(zip(pa1, pa2)):
        options = [a, b]
        
        first = np.random.choice(options, 1)[0]
        second = np.random.choice(options, 1)[0]
        child_a[i] = first
        child_b[i] = second
    
    if len(child_a) != len(pa1):
        raise ValueError('oeps')
    
    return Solution(child_a), Solution(child_b)    

def create_new_children(parents, n_crossover):
        pa1 = parents[0].value_vector
        pa2 = parents[1].value_vector
        
        # do uniform crossover
        if n_crossover == 0:
            return uniform_xover(pa1, pa2)
                    
        # do 2-point crossover
        elif n_crossover == 2:
            return n_point_xover(pa1, pa2)
                 
        else:
            raise ValueError('{}-point crossover is currently not supported'.format(n_crossover))
                
        
        
class Population():
    
    def __init__(self, solutions_list:list, previous_iter:int):
        self.solutions = solutions_list
        self.current_iter = previous_iter+1
        self.new_pairs = []
        self.offspring = []
        self.population_size = len(solutions_list)
        self.best_children = []
        
        self.fitness = None
        

    def get_fitness(self, optimum, valuefunc):
        if not self.fitness:
            self.fitness = self.best_solution_fitness(valuefunc)
            
            return (self.global_optimum_reached(optimum, valuefunc), 
                    self.fitness)
        else:
            return self.fitness
    
    def global_optimum_reached(self, optimum, valuefunc):
        if not self.fitness:
            self.fitness = self.best_solution_fitness(valuefunc)
        
        if np.max(self.fitness) == optimum:
            return True
        return False
    
    def best_solution_fitness(self, valuefunc):
        start = time.time()
        values = []
        for to_check in self.solutions:
            value = valuefunc(to_check)
            values.append(value)
        
        # print('Fitness: {:.2f}'.format(time.time() - start))
        return max(values)

    def step_gen(self, crossover_operator, valuefunc, cores):
        self.shuffle_population()
        self.pair_solutions()
        self.create_offspring(crossover_operator, cores=cores)
        
        self.family_competition(valuefunc)
        return self.best_children
    
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
        start = time.time()
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
        
        # print('Crossover: {:.2f}'.format(time.time() - start))
                
    
    def family_competition(self, valuefunc):
        start = time.time()
        best_children = []
        # sample families (2 parents and those children)        
        
        for i in range(0,len(self.solutions),2):
            candidates = []
            
            
            candidates.append(self.solutions[i])
            candidates.append(self.solutions[i+1])
            candidates.append(self.offspring[i])
            candidates.append(self.offspring[i+1])
          
            function_values = np.array([valuefunc(sol) for sol in candidates])
            # check if fitness of any children is equal to one of the parents, 
            # if this is true, delete from possible candidates
            par_1 = function_values[0]
            par_2 = function_values[1]
            to_del = []
            for ii in range(2,4):
                child = function_values[ii]
                if child == par_1:
                    to_del.append(0)
                elif child == par_2:
                    to_del.append(1)
                    
            function_values = [v for i,v in enumerate(function_values) if i not in to_del]
            candidates = [v for i,v in enumerate(candidates) if i not in to_del]
                
            best_idx = np.array(function_values).argsort()[::-1]
            
            # append 2 best solution to list
            best_children.append(candidates[best_idx[0]])
            best_children.append(candidates[best_idx[1]])
            # for n in range(2):
            #     # print(len(function_values))
            #     max_idx = function_values.index(max(function_values))
            #     best_sol = candidates.pop(max_idx)
            #     function_values.pop(max_idx)
            #     best_children.append(best_sol)
        
        # print('Competition: {:.2f}'.format(time.time() - start))        
        self.best_children = best_children
    
    def proportion_bits1_population(self):
        total_sum = 0
        length = self.solutions[0].length
        for sol in self.solutions:
            total_sum += counting_ones_fitness_func(sol)
        return total_sum / (length * self.population_size)
    
    def selection_errors_gen(self):
        # this method returns the selection errors/correct for this generation. 
        # errors are defined as when parents have 1 and 0 bit at index i, 
        # and the winners of the family competition (self.best_children) have a 0 bit at this index.
        # the other way around for correct: 1 bit at index i for the winners of family competition
        if self.best_children == []:
            raise ValueError("selection errors can't be calculated before family competition")
            
        selection_correct = 0
        selection_error = 0
        for i in range(0,len(self.solutions),2):
            pa1, pa2 = self.solutions[i].value_vector, self.solutions[i+1].value_vector
            child1, child2 = self.best_children[i].value_vector, self.best_children[i+1].value_vector
            diff_idx = list(np.argwhere((pa1-pa2) != 0))
            for ii in diff_idx:
                if child1[ii] and child2[ii] == 0:
                    selection_error+=1
                elif child1[ii] and child2[ii] == 1:
                    selection_error+=1
                    
        return selection_correct, selection_error

    def competing_schemata
                    
                
    
    
    
        


  
    