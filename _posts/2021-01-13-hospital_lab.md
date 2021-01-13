---
layout: post
title: Postfix Calculator Lab
gh-repo: daattali/beautiful-jekyll
gh-badge: [star, fork, follow]
tags: [Art of Data]
---

## Process

In this lab, my objective was to turn a dataset into an answer regarding which New York county has the most hospital beds per person. I first needed to go through the API data in order to turn it into a CSV by piping it. Then, I standardized the data so it would show the number of hospital beds per 1,000 people. While I hope to learn how to do this through code, I manually standardized to find hospital beds per 1,000 people. I was now ready to run through the data. Since some keys contained multiple values, I needed to add the values of each county together to find hospital beds per 1,000. The code for that part looked as follows:

> #Add values contained in a list
> def sum(list):
    > sum = 0
    > for i in range (0, len(list)):
        > sum += list[i]
    > return sum

> #Adds the beds per county after standardizing
> for i in counties:
    > sum = sum(counties[i])
    > #Add the sum into counties
    > counties[i].append(total)

## Results

Answer: I found that New York County had the highest number of hospital beds per person among all New York counties.

## Reflection

While I believe I reached the final answer, parts of the lab were challenging for me. The most notable obstacle that I faced was standardization. I am fortunate that the CSV contained 135 rows, because otherwise manually standardizing would have been a colossal waste of time when there are easier ways to do it. I also struggled with the initial stages of cleaning and organizing the API. When I needed assgit istance, I mostly consulted with my brother Aidan who gave me some helpful ideas. The following source also helped me understand APIs:

[TechnologyAdvice](https://technologyadvice.com/blog/information-technology/how-to-use-an-api/)

Overall, I learned how to work with APIs, organize a CSV, and run through the data in a CSV. 