# Global scope
global_var = 100


def fun():
    # Local scope
    # This statement defines a new global_var variable inside fun() scope
    # It doesn't modify global_var value in global scope
    global_var = 200

    if True:
        # No block scope
        # This variable is available inside the fun() scope
        if_var = 400

    print(global_var)  # 200
    print(if_var)  # 400


fun()

# local variable can't be accessed outside the local scope
# print(if_var)
print(global_var)  # 100


# Modify variable value in global scope
def modify_global_var():
    global global_var

    global_var = 500


modify_global_var()

print(global_var)  # 500
