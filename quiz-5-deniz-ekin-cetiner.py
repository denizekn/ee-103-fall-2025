name = input("Enter name: ")
department = input("Enter department: ")
gpa = float(input("Enter GPA: "))
student_id = int(input("Enter ID: "))
student_info = {"name": name, "department": department, "gpa": gpa, "id": student_id}
def describe_student(info_dict):
    return f"Student {info_dict['name']} from {info_dict['department']} has a GPA of {info_dict['gpa']:.2f} and ID: {info_dict['id']}."
result = describe_student(student_info)
print(describe_student(student_info))