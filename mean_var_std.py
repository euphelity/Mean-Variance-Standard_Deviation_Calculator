import numpy as np

def calculate(list):
  try:

    arr = np.array(list).reshape((3,3))
    d = {}
    d['mean'] = []
    d['mean'].append(np.mean(arr, axis = 0).tolist())
    d['mean'].append(np.mean(arr, axis = 1).tolist())
    d['mean'].append(np.mean(arr))
    d['variance'] = []
    d['variance'].append(np.var(arr, axis = 0).tolist())
    d['variance'].append(np.var(arr, axis = 1).tolist())
    d['variance'].append(np.var(arr))
    d['standard deviation'] = []
    d['standard deviation'].append(np.std(arr, axis = 0).tolist())
    d['standard deviation'].append(np.std(arr, axis = 1).tolist())
    d['standard deviation'].append(np.std(arr))
    d['max'] = []
    d['max'].append(np.max(arr, axis = 0).tolist())
    d['max'].append(np.max(arr, axis = 1).tolist())
    d['max'].append(np.max(arr))
    d['min'] = []
    d['min'].append(np.min(arr, axis = 0).tolist())
    d['min'].append(np.min(arr, axis = 1).tolist())
    d['min'].append(np.min(arr))
    d['sum'] = []
    d['sum'].append(np.sum(arr, axis = 0).tolist())
    d['sum'].append(np.sum(arr, axis = 1).tolist())
    d['sum'].append(np.sum(arr))
    return d

  except ValueError:
    raise ValueError("List must contain nine numbers.")

  