# Day 12: Deep Dive Exercises

## Theory: The Blueprint (Object-Oriented Programming)

---

## DEEP DIVE - 1: The Constructor
A constructor is like the setup wizard that runs the moment an object is created. In Python, this setup happens inside a special method called `__init__`. Its job is not to create the object, but to **initialize** it by giving it starting values. Every time we create a new user, the constructor makes sure the user begins life in a valid and predictable state, such as being active by default.

---

## DEEP DIVE - 2: The Self Reference
The `self` keyword is how an object recognizes itself. When we call a method using an object, Python secretly passes that object into the method as the first argument. `self` is simply a name for that object. Without `self`, the method would not know *which* user’s data it is supposed to work with. It is the bridge between the method and the object’s own variables.

---

## DEEP DIVE - 3: The String Representation
By default, printing an object gives us a confusing memory address that is not useful for humans. String representation fixes this problem. By defining `__str__`, we control what normal users see when the object is printed. By defining `__repr__`, we give developers a more detailed and precise description useful for debugging. This makes objects easier to understand and work with.

---

## DEEP DIVE - 4: Private Variables
Sometimes, we want to protect important data from being changed accidentally. Python allows us to do this using private variables. When we add double underscores before a variable name, Python secretly renames it using a process called **name mangling**. This does not make the variable completely inaccessible, but it strongly discourages direct access from outside the class, helping keep data safe.

---

## DEEP DIVE - 5: The Property Decorator
The property decorator allows us to create a variable that looks normal but actually runs code behind the scenes. This is useful when a value should be calculated instead of stored. For example, age does not need to be saved because it can be calculated from the birth year. This technique is called **encapsulation**, because it hides internal logic while keeping the interface simple.

---

## DEEP DIVE - 6: Class Variables vs Instance Variables
Class variables belong to the class itself and are shared by all objects created from it. Instance variables belong to individual objects and are unique to each one. If a class variable is changed, every object sees the change. This saves memory and is useful for information that should be common to all objects, such as species or category.

---

## DEEP DIVE - 7: Inheritance
Inheritance allows a new class to reuse the features of an existing class. The new class automatically gets all the variables and methods of the parent class. It can also add new abilities that only it has. Python looks for methods first in the child class and then in the parent class. This searching process follows the **Method Resolution Order (MRO)**.

---

## DEEP DIVE - 8: The Super Proxy
When a child class has its own constructor, the parent’s constructor does not run automatically. The `super()` function fixes this problem. It allows the child class to call the parent’s method so important setup code is not lost. This ensures that the object is fully initialized using both parent and child logic.

---

## DEEP DIVE - 9: Operator Overloading
Operator overloading lets objects behave like built-in data types. By defining special methods such as `__add__`, we can tell Python what should happen when operators like `+` are used on objects. This makes code more natural and readable. It is an example of **polymorphism**, where different types respond to the same operation in their own way.

---

## DEEP DIVE - 10: Equality
By default, Python checks whether two objects are stored in the same memory location when using `==`. This is often not what we want. By overriding the `__eq__` method, we can compare objects based on their actual content instead. This allows two different objects to be considered equal if their important data matches.

---
