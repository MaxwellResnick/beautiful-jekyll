---
layout: post
title: Postfix Calculator Lab
gh-repo: daattali/beautiful-jekyll
gh-badge: [star, fork, follow]
tags: [Art of Data]
---

## Results

For the Postfix Calculator Lab, my final results look as follows.

6.0
40.0
-162.0
-692.0
2.0
-19.0
93.0
95.0
-11.0
49000.0
38.0
84.0
-100.0
115.0
3.0
142.0
791.0
82.0
-192.0
-4.0
143.0
3060.0
137.0
384.0
11.0
48.0
805.0
11.0
-2700.0
190.0
-96.0
1715.0
60.0
48.0
-25.0
-4.0
-135.0
-77.0
663.0
40.0
10.0
-81.0
-15.0
-311.0
1095.0
1076.0
1260.0
-204.0
91.0
416.0
-26.0
34.0
-19.0
-343.0
11.0
-110.0
192.0
-63.0
-2.0
9.0
13.0
-33.0
-223.0
152.0
75.0
54.0
517.0
2110.0
412.0
10.0
-571.0
3432.0
23.0
-48.0
1764.0
7.0
240.0
-2.0
-936.0
9.0
1.0
5.0
414.0
386.0
128.0
-115.0
1.0
-18.0
0.0
-16186.0
1391.0
29.0
233.0
38.0
63.0
1560.0
591.0
-36.0
917.0
-25.0

Average: 529.91

## Process

In this lab, my objective was to create a postfix notation calculator, and use that to print out the values of a CSV file that contains numbers and operands. To do that, I first had to import the CSV file. Then, I had to create the stack class and define the __init__ method. Afterwards, I had to define the peek, push, pop methods, which look at, add, and remove the element from the top of the stack, respectively. After I defined the __repr__ method, I created a method that finds the average of the values that appear in a given list. Next, I defined an evaluate function to evaluate the CSV file and set up a stack that is used by the function. I ran a for loop through each element and returned the stack values. Finally, I applied the functions on each row of the CSV and printed the final values. To top it off, I found the average of the printed values. 

Here is the final block of code that printed my values and the final average:

   > average = []

   > with open("calculate_me.csv", "r") as f:
   >     data = csv.reader(f)
   >     for row in data: #evaluates the final average
   >         evaluate(row)
   >         average.append(float(row[0]))
   >         print(row)
   > print(average(average)) #prints the final average

The part of this lab that I found the most challenging was applying my theoretical knowledge of peek, push, and pop to the data. I understood what each method did, but I had to put the syntax into action to get my final results. Furthermore, it took me awhile to create the final for loop that ran through the elements of a list. To get a better sense of postfix notation, I used the following source.

[RunestoneAcademy](https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html)

For the most part, I worked by myself for this lab, but I discussed certain strategies with Aidan Resnick and Jake Federman. They helped me understand the initial steps of the process to create the postfix calculator. This lab taught me how to create a postfix calculator and apply the peek, push, pop, and __repr__ methods. 