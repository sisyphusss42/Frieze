# Frieze Generator
I'm a high school student doing research about Conway-Coxeter frieze, and here's the code I wrote for my research. Feel free to try it out and maybe even do some research yourself!

**Introduction**
---


Conway-Coxeter frieze is first created by mathematician H. S. M. Coxeter in the 1970's. It's a net of positive integers where any four numbers in a rhombus shape satisfies **the product of the left and right number is one greater than the product of the up and down number**. Not only that, the first and last row of the frieze must all be 1's. It would be reasonable to think that if we randomly filled in the second row with positive integers then calculate the rest of the frieze with the rule mentioned above, the numbers would blow up, or even end up negative or fractional. Surprisingly, Conway and Coxeter discovered that certain array of numbers can let the frieze return to a row of 1's if filled in the second row. It has something to do with "triangulation of polygons". I'll leave you here and provide links below for any enthusiasts who'd love to learn more about friezes.

[List of papers](https://www.maths.dur.ac.uk/users/anna.felikson/Projects/frieze/frieze-res.html)\
\
[Wonderful presentation by Dr.Sophie Morier-Genoud](https://www.youtube.com/watch?v=VxcWGg6QhyI&pp=ygURZnJpZXplIGxtcyBzb3BoaWU%3D&themeRefresh=1)


**How to Use this Code**
---

1. Run the python file
2. Enter the **quiddity sequence** you desire
    + format should be something like `1212` or `41321421`
    + for quiddity containing numbers with more than one digit, alter the code to change the input format
3. Voila! A frieze should appear in your terminal. It should print out four fundamental regions of your frieze. It will also tell you the quantity of each digit in two fundamental regions of the frieze. (The quantity of 1 doesn't incldue the first and last row of the frieze.) Note that the code can only output frieze containing numbers with one or two digits.
4. Enter 0 to terminate the code.



**Example Output**
---
This is the output of the quiddity sequence `31221`.\
\
Input:
```
Please enter the quiddity sequence of your frieze (e.g. 31221): 
31221
```
Output:

```
１    １    １    １    １    １    １    １    １    １     
   ３    １    ２    ２    １    ３    １    ２    ２    １     
      ２    １    ３    １    ２    ２    １    ３    １    ２     
         １    １    １    １    １    １    １    １    １    １     

1: 4  
2: 4  
3: 2  
```




