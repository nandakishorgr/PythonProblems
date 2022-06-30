grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
    print(item)

for count, item in enumerate(grocery):
    print(count, item)

# changing default start value
for count, item in enumerate(grocery, 100):
    print(count, item)

"""""""""
output:
(0, 'bread')
(1, 'milk')
(2, 'butter')

0 bread
1 milk
2 butter

100 bread
101 milk
102 butter
"""""""""