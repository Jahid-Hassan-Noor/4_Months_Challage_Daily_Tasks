# Day 10: Deep Dive Exercises

## Theory: Functional Programming (Lambda Map)

---

## DEEP DIVE - 1: The Anonymous Function
Lambdas are like guest accounts on a website where we don't bother making a real profile name. They are basically tiny, one-line functions that we use once and then throw away without giving them a permanent spot in our code's memory. It is just a faster way to write a simple math rule without all the extra typing usually required for a standard function.

---

## DEEP DIVE - 2: The Mapper
The map tool works like a factory assembly line for our data. Instead of we manually picking up every item in a list to change it, map sends the whole list through a "machine" that does the work at high speed. The only catch is that it is "lazy," so it does not actually start working until we force it to by putting the results into a list.

---

## DEEP DIVE - 3: The Filter
Filter is exactly what it sounds like. It acts like a strainer for our data. we give it a rule, and it checks every item in our list; if the item passes the test and is "truthy," it stays, but if it is not, it gets tossed out. It is a really clean way to get rid of junk data, like zeros or empty spaces, without writing a long, complicated loop.

---

## DEEP DIVE - 4: The Reducer
Reduce is like making a giant snowball out of tiny pieces of snow. It takes the first two things in our list, combines them into one value, then takes that new value and combines it with the next item. It keeps doing this over and over until our entire list has been squashed down into one single final answer.

---

## DEEP DIVE - 5: The Custom Sort Key
Sometimes we want to sort things in a weird way, like looking at the numbers inside a text string instead of just the letters. A custom sort key lets we tell the computer to pretend an item looks like something else just for a second so it can sort it properly. It does not actually change our original data; it only changes how the computer "sees" it during the sorting process.

---

## DEEP DIVE - 6: The Zip Lock
The zip tool is like the zipper on our jacket—it takes two separate tracks and locks them together side-by-side. If we have a list of names and a list of ages, zip pairs them up into little couples called tuples. we can then turn those pairs into a dictionary so we can easily look up someone's age just by using their name.

---

## DEEP DIVE - 7: List Comprehension Speed
List comprehensions are usually the "cool" way to write code because they are actually faster than using map with a lambda. The computer has an easier time reading them because it does not have to keep jumping back and forth between different workspaces for every single item in the list. It is basically like taking a direct flight to our destination instead of having a bunch of annoying layovers.

---


## DEEP DIVE - 8: Any & All
These tools are like lazy judges who want to go home as early as possible. If we use "any," the judge stops looking as soon as they find even one thing that is true. If we use "all," they stop the very moment they find one thing that is false. This "short-circuiting" saves a lot of time because the computer does not waste energy checking things it already knows the answer to.

---

## DEEP DIVE - 9: Partial Functions
Partial functions are like "freezing" a part of a recipe so we do not have to do it every single time. If we have a function that needs two numbers but we know one of them is always going to be the same, we can lock that one in place. This creates a new, simpler function that only asks we for the one piece of information that actually changes.

---

## DEEP DIVE - 10: The Immutability Test
In this style of coding, we are not allowed to touch or change our original data—this is a concept called "immutability". If we want to change something, we have to make a brand-new copy with the changes included instead of messing with the original version. It keeps our code safe and predictable because we never have to worry about a function accidentally breaking something else in the background.

---