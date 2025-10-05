print('Imported my_modules... ')

test = 'Test String'

def search_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return i
  #  return -1