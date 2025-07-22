# Define the input file and the list of IPs to remove
import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

print(f"--- Starting IP Allow List Update ---")
print(f"Input file: {import_file}")
print(f"IPs to remove: {remove_list}")

# Read the file contents
try:
    with open(import_file, "r") as file:
        initial_ip_string = file.read()
        ip_addresses = initial_ip_string.split()
    print(f"\nInitial IP addresses (from file): {ip_addresses}")
except FileNotFoundError:
    print(f"Error: The file '{import_file}' was not found. Please create it.")
    exit()

# Remove IP addresses that are on the remove list
# Create a new list to avoid issues with removing elements during iteration
updated_ip_list = []
for element in ip_addresses:
    if element not in remove_list: # Only add elements that are NOT in the remove_list
        updated_ip_list.append(element)

# Convert the updated list back into a string
ip_addresses_string = " ".join(updated_ip_list)
print(f"Updated IP addresses (as list): {updated_ip_list}")
print(f"Updated IP addresses (as string): {ip_addresses_string}")


# Update the file with the revised list of IP addresses
with open(import_file, "w") as file:
    file.write(ip_addresses_string)

print(f"\n--- Update Complete! '{import_file}' has been updated. ---")

# Optional: Verify the update (you can run this part separately or manually check the file)
# with open(import_file, "r") as file:
#     verified_content = file.read()
#     print(f"\nVerified content in '{import_file}':\n{verified_content}")
