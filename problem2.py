from collections import defaultdict,Counter

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# salay_ten=defaultdict(list)

# for sal,ten in salaries_and_tenures:
#     salay_ten[ten].append(sal)
    
# avg_sal={
#     ten:sum(sal)/len(sal)  #key : value here key is years: salary
#     for ten,sal in salay_ten.items()
# }
# print(avg_sal)

# here no we will seperate it by buckets

# here we can see that we are grouping according to the tenure 
def tenure_and_sal(tenure):
    if(tenure)<2:
        return "avg sal for less than 2"
    elif(tenure)<5:
        return "avg sal b/w 2 to 5"
    else:
        return "avg sal for >5"
    

dict_avg_tenure_sal=defaultdict(list)

for sal, ten in salaries_and_tenures:
    bucket=tenure_and_sal(ten)
    dict_avg_tenure_sal[bucket].append(sal)

buck_avg_sal={
    ten:sum(sal)/len(sal)
    for ten,sal in dict_avg_tenure_sal.items()
    
}

print(buck_avg_sal)

# findinf the words or the intrests that is highly used
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

count=Counter(word for user,intrest in interests
                   for word in intrest.lower().split() )

for user,intrest in count.most_common():
    if intrest>1:
        print(user,intrest)
        

    
    
