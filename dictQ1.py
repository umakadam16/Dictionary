# dict={'name':'reema',1:[1,2,3,4,5],'sub':'math'}
# print("dictionary",dict)
# print("Length of dictionary:", len(dict))
# dict={'name':'uma','name':'kadam','age':21,
#       'address':'Rahatani chowk near pimple saudagar'}
# print(dict)
# dict['sub']=dict['name']
# print(dict)
d1={'a':2,'b':3,'c':4,'d':5}
d2={'e':9,'f':10}
# d1.update(d2)
# d3={**d1,**d2}
d3=(d1 | d2)
print(d3)