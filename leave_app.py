import sys

def leave_status(total, used):
    remaining = total - used
    if remaining >= 10:
        return "Sufficient Leave"
    elif remaining > 0:
        return "Low Leave Balance"
    else:
        return "No Leave Available"


def main(emp_id, name, department, total_leaves, used_leaves):
    status = leave_status(total_leaves, used_leaves)

    print("----- Employee Leave Report -----")
    print(f"ID          : {emp_id}")
    print(f"Name        : {name}")
    print(f"Department  : {department}")
    print(f"Remaining   : {total_leaves - used_leaves}")
    print(f"Status      : {status}")


if __name__ == "__main__":
    emp_id = "E001"
    name = "Employee"
    department = "IT"
    total_leaves = 20
    used_leaves = 5

    if len(sys.argv) == 6:
        emp_id = sys.argv[1]
        name = sys.argv[2]
        department = sys.argv[3]
        total_leaves = int(sys.argv[4])
        used_leaves = int(sys.argv[5])

    main(emp_id, name, department, total_leaves, used_leaves)