"""The entry point module"""

from salary import total_salary

def main():
    """Boots the application"""
    filename = 'salaries.txt'
    total, average = total_salary(filename)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()
