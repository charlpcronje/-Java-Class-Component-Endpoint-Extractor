import os
import re

def extract_info_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Extracting the base route
    base_route_match = re.search(r'@RequestMapping\("([^"]*)"\)', content)
    base_route = base_route_match.group(1) if base_route_match else ""

    # Extracting method information
    method_info = re.findall(
        r'@(GetMapping|PostMapping|PutMapping|DeleteMapping)\(.*?\)\s+public\s+([\w<?> ]+)\s+(\w+)\((.*?)\)', content)

    # Update here to remove 'Mapping' from the verb
    method_info = [(verb.replace('Mapping', ''), return_type, method_name, params) 
                   for verb, return_type, method_name, params in method_info]

    return base_route, method_info

def process_java_files(directory, output_file):
    with open(output_file, 'w') as file:
        # Write the Markdown heading
        file.write("# Application Endpoints, Classes and Components\n\n")

        for root, dirs, files in os.walk(directory):
            for file_name in files:
                if file_name.endswith('.java'):
                    file_path = os.path.join(root, file_name)
                    # Normalize file path to use forward slashes
                    normalized_file_path = file_path.replace('\\', '/')
                    base_route, methods = extract_info_from_file(file_path)
                    if base_route or methods:
                        # Write the normalized file path
                        file.write(f"## File: {normalized_file_path}\n")
                        if base_route:
                            file.write(f"### Route: {base_route}\n")
                        for verb, return_type, method_name, params in methods:
                            file.write(f" - Verb: {verb}\n   - Path: {base_route}\n   - Return Type: {return_type}\n   - Method: {method_name}({params})\n\n")

# Define the paths to the directories and the output file
path1 = 'ignite-api/src/main/java/net/integrategroup/ignite/controller'
path2 = 'ignite/src/main/java/net/integrategroup/ignite/controller'
output_file = 'Endpoints, Classes and Components.md'

# Call the function for both paths
process_java_files(path1, output_file)
process_java_files(path2, output_file)
