import json
from pathlib import Path

DATA_FILE = Path("students_db.json")

class Student:
    def __init__(self, student_id, name, age, course):
        self.id = student_id
        self.name = name.strip().title()
        self.age = int(age)
        self.course = course.strip().upper()

    def to_dict(self):
        return {"name": self.name, "age": self.age, "course": self.course}


class ManagementSystem:
    def __init__(self):
        self.students = {}
        self.load_data()

    def load_data(self):
        if DATA_FILE.exists():
            try:
                with open(DATA_FILE, "r") as file:
                    raw_data = json.load(file)
                    for s_id, info in raw_data.items():
                        self.students[s_id] = Student(s_id, info["name"], info["age"], info["course"])
            except json.JSONDecodeError:
                print("Database file corrupted. Starting fresh.")

    def save_data(self):
        with open(DATA_FILE, "w") as file:
            json_compatible = {s_id: obj.to_dict() for s_id, obj in self.students.items()}
            json.dump(json_compatible, file, indent=4)

    def add_student(self, student_id, name, age, course):
        if student_id in self.students:
            print("❌ Error: A student with this Roll No/ID already exists!")
            return
        try:
            new_student = Student(student_id, name, age, course)
            self.students[student_id] = new_student
            self.save_data()
            print(f"✓ Student '{new_student.name}' added and database updated!")
        except ValueError:
            print("❌ Error: Age must be a valid integer number.")

    def display_all(self):
        if not self.students:
            print("\nNo student records found.")
            return
        
        print("\n" + "="*55)
        print(f"{'ID / Roll No':<15}{'Name':<20}{'Age':<10}{'Course':<10}")
        print("="*55)
        for s_id, s_obj in self.students.items():
            print(f"{s_id:<15}{s_obj.name:<20}{s_obj.age:<10}{s_obj.course:<10}")
        print("="*55 + "\n")

    def search_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(f"\n✨ Record Found:")
            print(f"🔹 ID: {student.id}\n🔹 Name: {student.name}\n🔹 Age: {student.age}\n🔹 Course: {student.course}\n")
        else:
            print("❌ Student record not found.")


def main():
    system = ManagementSystem()
    
    while True:
        print("=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == "1":
            s_id = input("Enter Student ID / Roll No: ").strip()
            name = input("Enter Student Name: ")
            age = input("Enter Student Age: ")
            course = input("Enter Course / Branch: ")
            system.add_student(s_id, name, age, course)
        elif choice == "2":
            system.display_all()
        elif choice == "3":
            s_id = input("Enter Student ID to search: ").strip()
            system.search_student(s_id)
        elif choice == "4":
            print("Exiting system. Data saved safely.")
            break
        else:
            print("❌ Invalid input! Choose between 1 and 4.\n")

if __name__ == "__main__":
    main()