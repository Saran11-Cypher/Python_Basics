import os

def merge_html_files(input_folder, output_folder, num_files):
    os.makedirs(output_folder, exist_ok=True)  # Ensure output folder exists
    output_file = os.path.join(output_folder, "Merged.html")
    
    html_contents = []
    file_list = sorted(os.listdir(input_folder))[:num_files]  # Get the first N files

    for file_name in file_list:
        file_path = os.path.join(input_folder, file_name)
        if file_name.endswith(".html"):
            with open(file_path, "r", encoding="utf-8") as file:
                html_contents.append(file.read())

    merged_content = "\n".join(html_contents)  # Merge keeping structure intact

    with open(output_file, "w", encoding="utf-8") as output:
        output.write(merged_content)

    print(f"Files merged successfully! Merged file is saved at: {output_file}")

# User input for number of files
num_files = int(input("Enter the number of HTML files to merge: "))

# Define input and output folder paths
input_folder = "path/to/your/html/files"  # Change to your actual folder
output_folder = "Folder"  # This will be created if it doesn't exist

merge_html_files(input_folder, output_folder, num_files)
