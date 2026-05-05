student1=(123,"anmol")
student2=(156,"bhavani")
student3=(178,"kavya")

courses={"english","maths","physics","chemistry"}

stu1_course = ["english", "maths", "physics"]
stu2_course = ["maths", "physics", "chemistry"]
stu3_course = ["english", "chemistry", "physics","maths"]

students=[
    (student1,stu1_course),
    (student2,stu2_course),
    (student3,stu3_course)
]

stu1_set=set(stu1_course)
stu2_set=set(stu2_course)
stu3_set=set(stu3_course)

print(f" comm b/w 1 &2:{stu1_set & stu2_set}")
print(f"comm b/w 2 and 3 :{stu2_set & stu3_set}")
print(f"comm b/w 3 and 1:{stu3_set & stu1_set}")
print(f"comm b/w 1,2,3:{stu1_set & stu2_set & stu3_set}")
    
print("-" *20)

# finding the course that is registered by noone

registered=stu3_set | stu2_set | stu1_set
unregistered=courses-registered
print(f"courses that is unregistered:{unregistered}")

# with most courses
count=0
for cou in students:
    maxi=len[cou[1]]
    if(maxi>count):
        count=maxi
        
    
    