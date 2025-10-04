# import math

if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        quary_name = input()
        marks = []

        for _ in range(3):
            data = float(input())
            marks.append(data)
        student_marks[quary_name] = marks
    
    for name, marks in student_marks.items():
        print(name, marks)
    for name, marks in student_marks.items():    
        query = input()
        if query in student_marks:
            avg = sum(student_marks[query]) / len(student_marks[query])
            print(avg)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        # key = int(input())
    # print(marks)   
    