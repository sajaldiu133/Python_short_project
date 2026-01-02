#grade system 

marks = int(input("Enter marks = "))

if marks >= 80 and marks <= 100 :
    grade = 'A+'                                   #Also we can use SGPA Or CGPA ---- grade = "A+  SGPA = 4"

elif marks >= 75 and marks <80:
    grade = 'A'
    
elif marks >= 70 and marks <75:
    grade = 'A-'

elif marks >= 65 and marks <70:
    grade = 'B+'
    
elif marks >= 60 and marks <65:
    grade = 'B'
    
elif marks >= 55 and marks <60:
    grade = 'B-'   

elif marks >= 50 and marks <55:
    grade = 'C+'

elif marks >= 45 and marks <50:
    grade = 'C'

elif marks >= 40 and marks <45:
    grade = 'D'

elif marks  < 40 and marks > 0:
    grade = "F"

else:
    print("Invalaid Mark")
    
print(f"Your Grade is = {grade}")