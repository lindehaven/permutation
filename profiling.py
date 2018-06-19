import cProfile
import pstats
import permutation_strings
arg = 'permutation_strings.calculate("'+input("Type symbols: ")+'")'
cProfile.run(arg, 'restats')
p = pstats.Stats('restats')
p.sort_stats('cumulative').print_stats(20)
