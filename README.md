# Java Class Component Endpoint Extractor

## Overview

The Java Class Component Endpoint Extractor is a Python script designed to analyze Java source files, especially those used in Spring Framework applications. It extracts detailed information about API endpoints, such as the HTTP verbs, paths, return types, and method parameters. This script is ideal for developers looking to automatically generate documentation for their Java (Spring) API endpoints.

## Features

- **Endpoint Extraction**: Automatically extracts endpoint information from Java source files.
- **Support for Spring Annotations**: Parses `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`, and `@RequestMapping` annotations.
- **Markdown Output**: Generates a well-structured Markdown file, summarizing all extracted endpoint information.

## Code Explained

You can get the [detailed explanation of the code here ](./explained.md)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- Basic understanding of Python and regular expressions.
- Access to the Java source files of a Spring Framework application.

## Installation

To install the Java Class Component Endpoint Extractor, follow these steps:

1. Clone the repository:
 
```sh
 git clone https://github.com/charlpcronje/Java-Class-Component-Endpoint-Extractor.git
```
 
2. Navigate to the repository directory:
 
```sh
git clone https://github.com/charlpcronje/-Java-Class-Component-Endpoint-Extractor.git
```
 
3. No additional installation of packages is required if Python 3.x is already installed.
 
## Usage

To use the Java Class Component Endpoint Extractor, follow these steps:

1. Place your Java source files in a known directory.
2. Modify the script to specify the paths to your Java source directories and the desired output Markdown file name.
3. Run the script:
 
```
python endpointExtractor.py
```
 
4. Check the generated Markdown file for the extracted endpoint information.
 
## Contributing

Contributions to the Java Class Component Endpoint Extractor are welcome. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5. Push to the branch (`git push origin feature/AmazingFeature`).
6. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact
- Author: Charl Cronje
- Email: charl.cronje@mail.com
- LinkedIn: [https://www.linkedin.com/in/charlpcronje](https://www.linkedin.com/in/charlpcronje/)
- GitHub Link: [https://github.com/charlpcronje/-Java-Class-Component-Endpoint-Extractor.git](https://github.com/charlpcronje/-Java-Class-Component-Endpoint-Extractor.git)
