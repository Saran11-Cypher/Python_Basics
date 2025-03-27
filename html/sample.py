import os
import math

def merge_files_in_batches(input_folder, output_folder, num_files, batch_size=50):
    os.makedirs(output_folder, exist_ok=True)  # Ensure output folder exists
    file_list = sorted([f for f in os.listdir(input_folder) if f.endswith(".html")])[:num_files]  # Get the required files
    
    total_batches = math.ceil(num_files / batch_size)  # Calculate number of batches
    batch_files = []

    # Step 1: Merge in batches and store them
    for i in range(total_batches):
        batch_start = i * batch_size
        batch_end = min((i + 1) * batch_size, num_files)
        batch_file_list = file_list[batch_start:batch_end]

        batch_output_path = os.path.join(output_folder, f"batch_{i+1}.html")
        batch_files.append(batch_output_path)

        with open(batch_output_path, "w", encoding="utf-8") as batch_file:
            for file_name in batch_file_list:
                file_path = os.path.join(input_folder, file_name)
                with open(file_path, "r", encoding="utf-8") as f:
                    batch_file.write(f.read() + "\n")  # Maintain separation
            
        print(f"Batch {i+1} merged and saved as {batch_output_path}")

    # Step 2: Merge all batch files into the final merged file
    final_output_path = os.path.join(output_folder, "Final.html")
    
    with open(final_output_path, "w", encoding="utf-8") as final_file:
        for batch_file in batch_files:
            with open(batch_file, "r", encoding="utf-8") as bf:
                final_file.write(bf.read() + "\n")
    
    print(f"All batches merged into {final_output_path}")

# User input
num_files = int(input("Enter the number of HTML files to merge: "))
input_folder = "path/to/your/html/files"  # Change this to actual folder path
output_folder = "Merged_Files"  # Store batches & final file inside this folder

merge_files_in_batches(input_folder, output_folder, num_files)
