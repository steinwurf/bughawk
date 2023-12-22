import argparse
import glob
import os
import fnmatch
import gitignorefile

BOLD = "\033[1m"
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"

def get_all_sources(project_directory):
    headers = glob.glob(os.path.join(project_directory, "**/*.hpp"), recursive=True)
    sources = glob.glob(os.path.join(project_directory, "**/*.cpp"), recursive=True)

    # Make relative to project directory
    headers = [os.path.relpath(header, project_directory) for header in headers]
    sources = [os.path.relpath(source, project_directory) for source in sources]

    gitignore_path = os.path.join(project_directory, ".gitignore")
    matches = gitignorefile.parse(gitignore_path)

    filtered_headers = [header for header in headers if not matches(header)]
    filtered_sources = [source for source in sources if not matches(source)]

    return filtered_headers, filtered_sources

# Function to check headers for self-inclusion
def check_self_inclusion(project_directory):
    result = {}
    headers, _ = get_all_sources(project_directory)
    if not headers:
        print("No header files found")
        return return_code

    for header in headers:
        header = os.path.relpath(header, project_directory)
        with open(header, "r") as f:
            result[header] = False
            lines = f.readlines()
            for line in lines:
                if line.startswith("#include"):
                    # determine include type
                    if line.startswith("#include <"):
                        # system include
                        continue
                    elif line.startswith("#include \""):
                        # local include
                        include = line[10:-2]

                        # If the include is relative check if it ends up in the same file
                        old_cwd = os.getcwd()
                        os.chdir(os.path.dirname(header))
                        include = os.path.relpath(os.path.abspath(include))
                        os.chdir(old_cwd)

                        if include == os.path.basename(header):
                            result[header] = True
                            break
                    else:
                        raise Exception(f"Unknown include type in {header}")

    return result

# Function to check project for unused headers
def check_unused_headers(project_directory):
    results = {}
    headers, _ = get_all_sources(project_directory)

    return results


# Function to check if version.hpp is included in all source files
def check_version_hpp_inclusion(project_directory):
    print("📝 Checking if version.hpp is included in all source files...")

# Function to check that all headers have pragma once and that the pragma once is
# before any other includes
def check_pragma_once(project_directory):
    print("📝 Checking that all headers have pragma once and that the pragma once is before any other includes...")

# Function to check that all headers and sources have a license header
def check_license_header(project_directory):
    print("📝 Checking that all headers and sources have a license header...")


def main():
    parser = argparse.ArgumentParser(description="Bughawk - Code Quality Tool")
    parser.add_argument(
        "--project_directory", "-p",
        default=os.getcwd(),
        help="Path to the project directory to be analyzed (default: current directory)"
    )
    subparsers = parser.add_subparsers(title="Available Tools", dest="tool")

    # Tool to check headers for self include
    parser_self_include = subparsers.add_parser(
        "self_include",
        help="Check headers for self-inclusion"
    )

    # Tool to check project for unused headers
    parser_unused_headers = subparsers.add_parser(
        "unused_headers",
        help="Check project for unused headers"
    )

    # Tool to check if version.hpp is included in all source files
    parser_version_hpp = subparsers.add_parser(
        "version_hpp",
        help="Check if version.hpp is included in all source files"
    )

    parser_pragma_once = subparsers.add_parser(
        "pragma_once",
        help="Check that all headers have pragma once and that the pragma once is before any other includes"
    )

    parser_license_header = subparsers.add_parser(
        "license_header",
        help="Check that all headers and sources have a license header"
    )

    args = parser.parse_args()

    if args.tool == "self_include":
        print("Checking for self-inclusion in headers... 🔍")
        results = check_self_inclusion(args.project_directory)

        # Sort result so that errors are printed last
        results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1])}

        max_header_length = max(len(header) for header in results.keys())

        for header, self_included in results.items():
            status = "✅ No self-inclusion detected." if not self_included else "❌ Self-inclusion detected!"
            color = GREEN if not self_included else RED
            padding = " " * (max_header_length - len(header))
            print(f"{BOLD}{header}:{padding}{RESET} {color}{BOLD}{status}{RESET}")

        return any([self_included for self_included in results.values()])

    elif args.tool == "unused_headers":
        print("Checking for unused headers in the project... 🧹")
        check_unused_headers(args.project_directory)
    elif args.tool == "version_hpp":
        check_version_hpp_inclusion(args.project_directory)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
