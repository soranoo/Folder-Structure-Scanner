import os
import pyperclip

def generate_tree_structure(path:str, indent:str="|   ") -> str:
    tree = ""
    items = os.listdir(path)
    items.sort()
    for i, item in enumerate(items):
        full_path = os.path.join(path, item)
        is_last = i == len(items) - 1
        if os.path.isdir(full_path):
            tree += f"{indent}└── {item}\n"
            if not is_last:
                subtree = generate_tree_structure(full_path, f"{indent}|   ")
                tree += subtree
        else:
            tree += f"{indent}└── {item}\n" if is_last else f"{indent}├── {item}\n"
    return f"{tree}"

folder_path = input("Enter the path to the folder you want to scan: ")
folder_name = os.path.basename(folder_path)
tree_structure = f"{folder_name}\n{generate_tree_structure(folder_path, '')}"

print("\nTree structure:\n")
print(tree_structure)

copy_to_clipboard = input("\nDo you want to copy the structure to the clipboard? (y/n): ")
if copy_to_clipboard.lower() == "y":
    pyperclip.copy(tree_structure)
    print("Structure copied to clipboard!")
else:
    print("Exiting program.")
