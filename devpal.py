from db import init_db, add_snippet, list_snippets, delete_snippet_by_id, search_snippets

def add_new_snippet():
    name = input("Snippet name: ")
    language = input("Language (ex: Python, Java, JS): ")
    tags = input("Tags (separated w/ commas): ")
    description = input("Short description: ")
    file_path = input("Enter path to your code file (e.g., snippet.py): ")
    try:
        with open(file_path, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print("File not found. Please try again.\n")
        return
    add_snippet(name, language, tags, description, code)
    print("\nCode snippet saved successfully!\n")

def view_snippets():
    snippets = list_snippets()
    if not snippets:
        print("No snippets saved yet.\n")
        return
    print("\nSaved snippets:")
    for s in snippets:
        print(f"ID: {s[0]} | Name: {s[1]} | Language: {s[2]} | Tags: {s[3]}")
    print()

def delete_snippet():
    view_snippets()
    snippet_id = input("Enter the ID of the snippet you want to delete: ")
    if snippet_id.isdigit():
        delete_snippet_by_id(int(snippet_id))
        print(f"Snippet ID {snippet_id} deleted.\n")
    else:
        print("Invalid ID entered.\n")

def search_for_snippet():
    keyword = input("Enter keyword to search: ")
    results = search_snippets(keyword)
    if not results:
        print("No matching snippets found.\n")
    else:
        print(f"\nFound {len(results)} snippet(s):")
        for s in results:
            print(f"ID: {s[0]} | Name: {s[1]} | Language: {s[2]} | Tags: {s[3]}")
            print(f"   → {s[4]}\n")

def main():
    init_db()
    print("DevPal Code Snippet Manager\n")
    while True:
        print("Choose an option:")
        print("1. Add new snippet")
        print("2. View saved snippets")
        print("3. Delete a snippet")
        print("4. Search snippets")
        print("5. Exit")
        choice = input("Enter option number: ")
        if choice == "1":
            add_new_snippet()
        elif choice == "2":
            view_snippets()
        elif choice == "3":
            delete_snippet()
        elif choice == "4":
            search_for_snippet()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
