import urllib.parse
import argparse
import sys

def convert_url(input_url):
    # Encode the entire input URL
    encoded_url = urllib.parse.quote(input_url, safe='')
    
    # Construct the new URL
    new_url = f"cursor://ms-vsliveshare.vsliveshare/join?vslsLink={encoded_url}"
    
    return new_url

def main():
    parser = argparse.ArgumentParser(description="Convert VS Code Live Share URLs to Cursor format.")
    parser.add_argument("url", nargs="?", help="The URL to convert")
    args = parser.parse_args()

    if args.url:
        input_url = args.url
    else:
        # If no argument is provided, prompt the user for input
        input_url = input("Enter the URL to convert: ")

    try:
        converted_url = convert_url(input_url)
        print(f"Converted URL: {converted_url}")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
