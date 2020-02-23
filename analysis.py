#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 17:10:02 2020

@author: mba
"""
import os
import numpy as np
import pickle


filenames = ['1a.p', '1b.p', '2a.p', '2b.p', '3a.p', '3b.p', '4a.p', '4b.p', '5a.p', '5b.p']

files = []
for filename in filenames:
    file = open(filename,'rb')
    f = pickle.load(file)
    file.close()
    
    files.append(f)

    best_fitnesses = f['max_fitness']
    is_pass = True if sum(best_fitnesses) > 2400 else False
    
    cpu_times = f['cpu_time']
    
    result_dicts = f['res_dict']
    pop_sizes = [r['Pop_size'][-1] for r in result_dicts]
    generations = [r['generation_iter'][-1] for r in result_dicts]
    
    
    print(filename)
    print('PASS = {}'.format(is_pass))
    print('Mean fitness = {}'.format(np.mean(best_fitnesses)))
    print('Popsize = {}'.format(min(pop_sizes)))
    print('Generations = {} ({})'.format(np.mean(generations),
                                         np.std(generations)))
    print('Eval functions = {} ({})'.format('????', '?'))
    print('CPU time = {} ({})'.format(np.mean(cpu_times) / 60,
                                      np.std(cpu_times) / 60))
    print('\n')



