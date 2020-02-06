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

class Solution():
    
    def __init__(self, string_length:int):
        
    self.value_vector = []
    self.
    
    
# =============================================================================
#     fitness functions
# =============================================================================
    def counting_ones_fitness_func(self):
        return np.sum(self.value_vector)
    
    
class Population():
    
    def __init__(self, solutions_list:list, previous_iter:int):
        self.solutions = solutions_list
        self.current_iter = previous_iter+1
        self.new_pairs = []
        self.offspring = []
        
        
    def shuffle_population(self):
        self.solutions = np.random.shuffle(self.solutions)
        
    def pair_solutions(self):
        for i in range(0,len(self.solutions, 2)):
            parent_one = self.solutions[i]
            parent_two = self.solutions[i+1]
            self.new_pairs.append(parent_one, parent_two)
            
    def create_new_child(parent_solution1, parent_solution2, n_crossover):
        if n_crossover == 0:
            # do uniform crossover
            child = np.zeros(len(parent_solution1))
            
        else:
            # do n-point crossover
        
        return child
            
        
    
    def create_offspring(self, crossover_operator):
        if crossover_operator =='2X':
        
        else:
            
        
        
        
        
    
    
        
        
        
    