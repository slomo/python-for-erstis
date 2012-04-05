source = [1,35,43,1,23,5,123,23,2,3];
target = []



for s in source:
    for i in xrange(0, len(target)):
        if s <= target[i]:
            target.insert(i,s)
            break
    else:
            target.append(s)

print(target)
