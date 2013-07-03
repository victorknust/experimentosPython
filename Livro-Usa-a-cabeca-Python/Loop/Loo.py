movies = ['The Holy Grail', 'The Live of Brain']
count = 0

while count < len(movies):
    print(movies[count])
    count += 1

print('========================================')

for movie in movies:
    print(movie)

print('========================================')

print('Length range(5): ' + str(len(range(5))))
for item in range(5):
    print('#' + str(item))
