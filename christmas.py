import os

def create_card(name):
    template_path = "template.txt"
    output_dir = "christmasCards"
    output_file = os.path.join(output_dir, name + ".txt")

    with open(template_path, "r") as template_file:
        template = template_file.read()

    personalized_message = template.replace("NAME", name)

    with open(output_file, "w") as output:
        output.write(personalized_message)

def main():
    employees_file = "employees.txt"

    with open(employees_file, "r") as employees:
        names = employees.read().splitlines()

    for name in names:
        create_card(name)

    print("Christmas cards created successfully!")

if __name__ == "__main__":
    main()
