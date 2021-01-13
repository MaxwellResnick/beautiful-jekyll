#this command imports the CSV file that we are using
import csv

#creates the stack class
class Stack:
    def __init__(self, stack=[]):
        self.stack = stack

    #defines the peek method
    def peek(self):
        return self.stack[-1]

    #defines the push method
    def push(self, i):
        self.stack.append(i)

    #defines the pop method
    def pop(self):
        p = self.stack[-1]
        del self.stack[-1]
        return pop

    #defines the __repr__ method
    def __repr__(self):
        return str(self.stack)
    
    #takes the average of the values that appear in a given list
    def average(list):
        sum = 0
        for i in range (0, len(list)):
            sum += list[i]
        average = sum/len(list)
        return average
    
    def evaluate(list): #define the evaluate function
        #Set up the stack for the evaluate function
        s = Stack([])
        l = len(list)
    for i in range(0, (len(list))): #for loop runs through the list
        if (list[i] not in ["+", "-", "*"]):
            s.push(float(list[i]))
        else:
            a = s.pop()
            b = s.pop()
            if list[i] == "+":
                c = a + b
                s.push(c)
            elif list[i] == "-":
                c = b - a
                s.push(c)
            elif list[i] == "*":
                c = a * b
                s.push(c)
    print(s.peek())
    return s

        #creates the average variable
    average = []

    with open("calculate_me.csv", "r") as f:
        data = csv.reader(f)
        for row in data: #evaluates the final average
            evaluate(row)
            average.append(float(row[0]))
            print(row)
    print(average(average)) #prints the final average