def flatten_and_sort(array):
    # Flatten the array using a list comprehension and sort the result
    return sorted([item for sublist in array for item in sublist])


print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))

# Functional Prompt Answers (as comments):
# 1. This solution ensures data immutability by not modifying the original 'array' input. Instead, it creates a new list.
# 2. This is a pure function because it always produces the same output given the same input and has no side effects (it doesn't modify any external state).
# 3. This is not a higher-order function as it neither takes a function as an argument nor returns a function as its result.
# 4. This problem is well-suited to a functional style due to its simplicity and the absence of a need for maintaining or altering state.
# 5. Functional programming is helpful here because it provides a clear and concise way to express the operation of flattening and sorting a list without side effects or changing mutable state.


#################################################################

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self, other):
        print(f"Sebulbas fires a jet of flame at Anakin.")
        other.condition = "trashed"

anakin = AnakinsPod(1000, "perfect", 1000)
sebulbas = SebulbasPod(2000, "repaired", 500)

print (f"Anakin's max speed is {anakin.max_speed} and condition is {anakin.condition}.") # anakin.max_speed)
anakin.boost()
print (f"Anakin's max speed after boost is {anakin.max_speed}")

print (sebulbas.condition)
sebulbas.flame_jet(anakin)
print ("Anakin's condition after flame jet:", anakin.condition)
# Object Oriented Prompt Answers (as comments):
# 1. This solution demonstrates:
#    - Encapsulation by bundling the properties (max_speed, condition, price) and methods (repair, boost, flame_jet) within classes.
#    - Inheritance through the AnakinsPod and SebulbasPod classes extending the Podracer class, inheriting its properties and repair method.
#    - Polymorphism is not explicitly demonstrated in this example.
#    - Abstraction is shown by the use of methods like repair(), boost(), and flame_jet() that hide the details of the operations they perform.
# 2. An OOP approach is suitable for this problem as it involves creating entities with specific attributes and behaviors, which classes model well.
# 3. OOP is beneficial here as it allows us to model real-world entities (like Podracers) in a way that encapsulates their properties and behaviors, making the code more organized and reusable.
