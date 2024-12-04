stuff_dict = {'r':(3,25),
              'p':(2,15),
              'a':(2,15),
              'm':(2,20),
              'i':(1,5),
              'k':(1,15),
              'x':(3,20),
              't':(1,25),
              'f':(1,15),
              'd':(1,10),
              's':(2,20),
              'c':(2,20)
              }

item_dict = { 'r':(3,25),
              'p':(2,15),
              'a':(2,15),
              'm':(2,20),
              'i':(1,5),
              'k':(1,15),
              'x':(3,20),
              't':(1,25),
              'f':(1,15),
              'd':(1,10),
              's':(2,20),
              'c':(2,20)
              }


def get_space_and_value(stuff_dict):
    space = [stuff_dict[item][0] for item in stuff_dict]
    value = [stuff_dict[item][1] for item in stuff_dict]
    return space, value

def get_memtable(stuff_dict, S):
      space, value = get_space_and_value(stuff_dict)
      n = len(value) 
      
      V = [[0 for _ in range(S+1)] for _ in range(n+1)]

      for i in range(n+1):
            for s in range(S+1):
                  if i == 0 or s == 0:
                        V[i][s] = 0

                  elif space[i-1] <= s:
                        V[i][s] = max(value[i-1] + V[i-1][s-space[i-1]], V[i-1][s])

                  else:
                        V[i][s] = V[i-1][s]   
      return V, space, value


def get_selected_items_list(stuff_dict, S):
      V, space, value = get_memtable(stuff_dict, S)    
      n = len(value)
      res = V[n][S]      
      s = S             
      items_list = []    
    
      for i in range(n, 0, -1):  
            if res <= 0:  
                  break
            if res == V[i-1][s]:  
                  continue
            else:
                  items_list.append((space[i-1], value[i-1]))
                  res -= value[i-1]   
                  s -= space[i-1]  
            
      selected_stuff = []

      for search in items_list:
            for key, value in stuff_dict.items():
                  if value == search:
                        selected_stuff.append(key)
                        stuff_dict.pop(key)
                        break

      return selected_stuff


if __name__ == '__main__':
      result = get_selected_items_list(stuff_dict, 9)
      result_1 = result

      sum = 15
      for item in item_dict:
            if item in result_1:
                  sum += item_dict[item][1]
            else:
                  sum -= item_dict[item][1]

      backpack_size = 3
      for i in range(1, backpack_size + 1):
            j = 0
            while j < backpack_size:
                  for item in result:
                        if j + item_dict[item][0] <= backpack_size:
                              for i in range(item_dict[item][0]):
                                    print(f'[{item}],', end=' ')
                              result.remove(item)
                              j += item_dict[item][0]
            print('')

      print(sum)