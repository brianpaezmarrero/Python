# x = [ [5,2,3], [10,8,9] ] 
# x[1][0] = 15
# print(x)
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# students[0]['last_name'] = 'Brayant'
# print(students)
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)
# z = [ {'x': 10, 'y': 20} ]
# z[0]['y'] = 30
# print(z)
##############################################################################

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# def iterate_dictionary(a):
#     for i in range(0,len(a)):
#         output = ""
#         for key,val in a[i].items():
#             output += f" {key} - {val}"
#         print(output)

# iterate_dictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# def iterate_dictionary2(key_name, list):
#     for i in range(0,len(list)):
#         # print('yo')
#         for key,val in list[i].items():
#             # print('yo')
#             if key == key_name:
#                 print(val)

# iterate_dictionary2('first_name',students) 
# iterate_dictionary2('last_name',students) 


dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info(nin):
    for key,val in nin.items():
        print("--------------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])



print_info(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
