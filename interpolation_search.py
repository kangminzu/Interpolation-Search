interpolation = [i for i in range (0,100,3)]
n = (int(input("finding data : ")))

low = int(0)
high = int(len(interpolation) - 1)

def interpolation_search (first, last, key) :
  if (interpolation[first] > key or interpolation[last] < key) :
    return -1
  
  pos = int(low +((high - low) *((key - interpolation[low]) / (interpolation[high] - interpolation[low]))))

  if interpolation[pos] == key :
    return pos
  elif interpolation[pos] > key :
    return interpolation_search(first, pos - 1, key)
  else : 
    return interpolation_search(pos + 1, last, key)

print(interpolation_search(low, high, n))