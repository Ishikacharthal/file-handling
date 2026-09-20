import os


def count_lines(input_path):
    with open(input_path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def extract_first_lines(input_path, n=2):
    first_lines = []
    with open(input_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            first_lines.append(line)
    return first_lines


def write_lines(output_path, lines):
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(lines)


if __name__ == "__main__":
    # Always use the folder this script is saved in
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "input.txt")
    output_path = os.path.join(base_dir, "output_first_two_lines.txt")

    # Create a sample input file if none exists
    if not os.path.exists(input_path):
        with open(input_path, "w", encoding="utf-8") as f:
            f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n")
        print("input.txt not found, so a sample file was created.")

    # Count total lines
    total_lines = count_lines(input_path)
    print("Total number of lines:", total_lines)

    # Extract first two lines
    first_two = extract_first_lines(input_path, 2)
    print("\nFirst two lines:")
    for line in first_two:
        print(line.strip())

    # Write them into a new file
    write_lines(output_path, first_two)
    print("\nFirst two lines written to:", output_path)