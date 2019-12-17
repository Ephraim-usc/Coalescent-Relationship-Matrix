### importing packages
#import sys
#import time
#import datetime
import msprime
#import tskit
#import itertools
import math
import numpy as np
#import pandas as pd
#import os

### parameters
out = "tmp"
log_file = "tmp.log"

l = 32000000
N = 1000
mutation_rate = 1e-8
recomb_rate = 1e-8

cas_ratio = 0.1
obs_ratio = 0.2
Alpha = -0.5
Beta = 1
h2g = 1.0

### out-of-Africa parameters
N_B = 2100
N_EU0 = 1000
N_AF = 12300
N_A = 7300
r_EU = 0.004
generation_time = 25
T_EU_AS = 21.2e3 / generation_time
T_B = 140e3 / generation_time
T_AF = 220e3 / generation_time
N_EU = N_EU0 / math.exp(-r_EU * T_EU_AS)

### parameters
def simulate_hapdata(l = l, N = N, mutation_rate = mutation_rate, recomb_rate = recomb_rate):
    population_configurations = [msprime.PopulationConfiguration(sample_size = N, initial_size = N_EU, growth_rate = r_EU)]
    
    demo_events = [msprime.PopulationParametersChange(time=T_EU_AS, initial_size = N_B, growth_rate=0),
                   msprime.PopulationParametersChange(time=T_B, initial_size = N_AF, growth_rate=0),
                   msprime.PopulationParametersChange(time=T_AF, initial_size = N_A, growth_rate=0)]
    
    tree_sequence = msprime.simulate(length = l, population_configurations = population_configurations, 
                                     recombination_rate = recomb_rate, mutation_rate = mutation_rate, 
                                     demographic_events = demo_events)
    
    genotype_matrix = tree_sequence.genotype_matrix().astype("uint16")
    MAFs = genotype_matrix.mean(axis = 1); MACs = np.array(list(map(min, MAFs, 1-MAFs)))
    variants = np.array([v.position for v in tree_sequence.variants()])
    M = len(variants)
    
    return {"tree_sequence":tree_sequence, "genotype_matrix":genotype_matrix, 
            "MAFs":MAFs, "MACs":MACs, "variants":variants, "M":M}

def simulate_phenotypes(hapdata, h2g = h2g, cas_ratio = cas_ratio, Alpha = Alpha):
    



    



    

    
