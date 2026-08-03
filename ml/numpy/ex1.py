import numpy as np

gold_close = np.array([
3352,
3361,
3358,
3371,
3378
])

print(np.max(gold_close))
print(np.min(gold_close))
print(np.mean(gold_close))
print(np.sum(gold_close))

for price in gold_close:
    print(price*1.01)
    print(price*0.98)
