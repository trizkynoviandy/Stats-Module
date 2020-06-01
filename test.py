import stats_module

x = [84, 86, 89, 92, 82, 86, 89, 92, 80, 86, 80, 90, 87, 83]

print('Total number of data   : {} data'.format(len(x)))
print('Mean                   :', stats_module.mean(x))
print('Median                 :', stats_module.median(x))
print('Mode                   :', stats_module.mode(x))
print('Variance               :', stats_module.var(x))
print('Standar Deviation      :', stats_module.stdev(x))

stats_module.describe(x)