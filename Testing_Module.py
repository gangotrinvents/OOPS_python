## Here are going to import our class "brk"
## we are importing class "brk" from file "Social_Media"

from Social_Media import brk

brk1 = brk()

## As we are able to create module "Social_Media" and able to import class from that module
## This is called "Modularity"

#print("1",brk._brk__name)
#print("2",brk.get_age())
#print("3",brk.set_age("John"))
#print("4",brk.get_age())


# print(brk1._brk__obj_cnt,brk1.cnt)
# brk2 = brk()
# print(brk2._brk__obj_cnt,brk2.cnt)
# brk3 = brk()
# print(brk3._brk__obj_cnt,brk3.cnt)
# brk4 = brk()
# print(brk4._brk__obj_cnt,brk4.cnt)/

print(brk1.get_id())

brk2 = brk()

print(brk2.get_id())
