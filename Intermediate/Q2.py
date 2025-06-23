def read_lines(filename):
    """
    Reads and returns lines from the specified file.
    
    Args:
        filename (str): The name of the file to read.

    Returns:
        list[str]: A list of lines from the file, or None if file not found.
    """
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found. Please check the file name and try again.")
        return None


def main():
    filename = input("Enter the filename to read: ").strip()
    lines = read_lines(filename)
    
    if lines is not None:
        print(f"✅ File '{filename}' loaded successfully.")
        print(f"📄 Line count: {len(lines)}")


if __name__ == "__main__":
    main()
