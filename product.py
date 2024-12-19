# WAP to create dictionaries for below task and perform all the above operations on it.

# Each product in a supermarket is associated with its price.

# Each student in a school is associated with their grade.

# Each customer ID in a company is ass
product_dict={"suger":240,"salt":100,"bornvita":150,"turmeric powder":120}
print(product_dict)
#adding new product in dectionary
product_dict['egg']=150
product_dict['maggi']=120
print(product_dict)
#deleting product in dictionary
del product_dict['turmeric powder']
print(product_dict)
all_product=product_dict.items
print("all item in supermarket",product_dict)
