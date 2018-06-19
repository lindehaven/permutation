import cProfile
import pstats
import permutation_strings
cProfile.run('permutation_strings.calculate("DA")', 'restats')
p = pstats.Stats('restats')
p.sort_stats('cumulative').print_stats(20)
