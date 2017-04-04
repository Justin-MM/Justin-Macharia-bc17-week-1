def data_type(x):

  if isinstance(x, str):
    return len(x)
  elif isinstance(x, list):
    if len(x) >= 3:
      return x[2]
    else:
      return None
  if x is None:
    return 'no value'
  elif x is True:
    return True
  elif x is False:
    return False
  elif isinstance(x, int):
    if x < 100:
      return 'less than 100'
    elif x > 100:
      return 'more than 100'
    else:
      return 'equal to 100'


__author__ = 'Justin M'
