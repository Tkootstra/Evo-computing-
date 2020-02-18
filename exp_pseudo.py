#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:42:33 2020

@author: timo
"""
LOOP VOOR 25 ITERS
1. Maak random populatie. N = 10. alleen multiples gebruiken
LOOP
2. Doe crossover, family selection maak nieuwe children.
3. nieuwe gen wordt gemaakt: heeft iemand in de nieuwe gen de max fitness? stop dan, je bent klaar
4. niet global optimum? verdubbel N
5. N > 1280? werkt niet!
END LOOP
6. global optimum gevonden: nu bisection search

END LOOP 25

24/25 global opt -> werkt! anders niet


