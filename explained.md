# Java Class Component Endpoint Extractor Script Explained

This Python script is designed to analyze Java source files in specified directories, extract information about API endpoints defined within them, and output this information in a Markdown file. The script focuses on extracting details from Java methods annotated with specific mapping annotations (like `@GetMapping`, `@PostMapping`, etc.) typically used in Spring Framework for defining web request handlers. Below is a detailed explanation of each part of the script:

## Imports
```python
import os
import re
```
- `os`: This module provides a way of using operating system-dependent functionality like reading or writing to the file system.
- `re`: This module allows the use of regular expressions in Python, which is used here to parse text patterns in Java files.

## Function: `extract_info_from_file(file_path)`
This function takes a single argument, `file_path`, representing the path to a Java file. It extracts the base route and method information from the file.

### Reading the File
```python
with open(file_path, 'r') as file:
    content = file.read()
```
- Opens the file at `file_path` in read mode and reads its content into the `content` variable.

### Extracting Base Route
```python
base_route_match = re.search(r'@RequestMapping\("([^"]*)"\)', content)
base_route = base_route_match.group(1) if base_route_match else ""
```
- Uses a regular expression to find the `@RequestMapping` annotation and extract the base route.
- If the `@RequestMapping` annotation is found, `base_route` is set to the captured group; otherwise, it's an empty string.

### Extracting Method Information
```python
method_info = re.findall(
    r'@(GetMapping|PostMapping|PutMapping|DeleteMapping)\(.*?\)\s+public\s+([\w<?> ]+)\s+(\w+)\((.*?)\)', content)
```
- This regular expression finds methods annotated with `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`.
- It captures details like HTTP verb, return type, method name, and parameters.

### Formatting Method Information
```python
method_info = [(verb.replace('Mapping', ''), return_type, method_name, params) 
               for verb, return_type, method_name, params in method_info]
```
- Processes the extracted method information to remove the word 'Mapping' from the HTTP verbs.

### Return Values
```python
return base_route, method_info
```
- Returns the base route and the processed method information.

## Function: `process_java_files(directory, output_file)`
This function processes Java files in a given directory and writes the extracted information to an output Markdown file.

### Writing to the Markdown File
```python
with open(output_file, 'w') as file:
    file.write("# Application Endpoints, Classes and Components

")
```
- Opens (or creates) the Markdown file in write mode and writes the heading.

### Processing Each Java File
```python
for root, dirs, files in os.walk(directory):
    for file_name in files:
        if file_name.endswith('.java'):
            # ... [extraction and writing logic] ...
```
- Iterates over all files in the specified directory and its subdirectories.
- Processes each `.java` file to extract API endpoint information.

### Writing Extracted Information
```python
file.write(f"## File: {file_name}
")
if base_route:
    file.write(f"### Route: {base_route}
")
for verb, return_type, method_name, params in methods:
    file.write(f" - Verb: {verb}
   - Path: {base_route}
   - Return Type: {return_type}
   - Method: {method_name}({params})

")
```
- Writes the file name, base route, and details of each method (HTTP verb, path, return type, method name, and parameters) to the Markdown file.

## Execution Logic
```python
path1 = 'ignite-api/src/main/java/net/integrategroup/ignite/controller'
path2 = 'ignite/src/main/java/net/integrategroup/ignite/controller'
output_file = 'Endpoints, Classes and Components.md'

process_java_files(path1, output_file)
process_java_files(path2, output_file)
```
- Defines two paths (`path1` and `path2`) pointing to directories containing Java files and an output file name.
- Calls `process_java_files` for each of these paths to analyze the Java files and write the results to the Markdown file. 

The script is particularly useful for automatically generating documentation of API endpoints in a Java (Spring) application. The resulting Markdown file provides a clear overview of all the routes, their HTTP methods, return types, and other relevant information.
