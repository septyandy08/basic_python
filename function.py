def my_function(first_name, last_name = ""):
    print("Hello {} {}".format(first_name, last_name))

my_function("Andy")

def my_function2(child3, child2, child1):
    print("The youngest child is " + child3)

my_function2(child3 = "Linus", child2 = "Tobias", child1 = "Emil")
my_function2("Linus", "Tobias", "Emil")