import pickle

with open('binario.pickle', 'wb') as pickleFile:
    pickle.dump([1, 2, 'Jefferson'], pickleFile)

with open('binario.pickle', 'rb') as pickleFile:
    var = pickle.load(pickleFile)

print(str(var))
