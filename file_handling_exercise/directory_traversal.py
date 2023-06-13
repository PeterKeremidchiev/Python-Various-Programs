import os


def save_extensions(directory_name, first_level_dir=False):
    for file_name in os.listdir(directory_name):
        file = os.path.join(directory_name, file_name)

        if os.path.isfile(file):
            extension = file_name.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(file_name)

        elif os.path.isdir(file) and not first_level_dir:
            save_extensions(file, first_level_dir=True)


start_directory = input()
extensions = {}

result = []

try:
    save_extensions(start_directory)
except FileNotFoundError:
    print(f"Not a valid directory")

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}")
    [result.append(f"- - - {file}") for file in sorted(files)]

report_abs_path = os.path.dirname(os.path.abspath(__file__))
report_file_path = os.path.join(report_abs_path, "report.txt")

with open(report_file_path, "w") as report_file:
    report_file.write("\n".join(result))