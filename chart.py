import matplotlib.pyplot as plt
import tkinter.messagebox as messagebox
import database


db = database.firebase.database()


def draw_chart():
    try:
        fig, ax = plt.subplots()
        get_employees = db.child("employees").get()
        employees = []
        for employee in get_employees.each():
            emp_data = employee.val()
            emp_tuple = {
                "id": emp_data.get("id"),
                "name": emp_data.get("name"),
                "phone": emp_data.get("phone"),
                "salary": emp_data.get("salary"),
                "department": emp_data.get("department"),
            }
            employees.append(emp_tuple)

        department_counts = {}
        for employee in employees:
            department = employee["department"]
            if department in department_counts:
                department_counts[department] += 1
            else:
                department_counts[department] = 1

        department_list = list(department_counts.keys())
        count_list = list(department_counts.values())

        department = department_list
        counts = count_list

        ax.bar(department, counts)

        ax.set_ylabel("Số lượng nhân viên")
        ax.set_title("Tổng số lượng nhân viên trong phòng ban")

        plt.show()
    except:
        messagebox.showerror(title="Error", message="No data")
        return
