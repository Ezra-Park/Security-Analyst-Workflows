# Python IP Allow List Updater

## Project Overview

This Python script automates the process of updating an IP address "allow list" by removing specified IP addresses. This is particularly useful where maintaining accurate access control lists is crucial (e.g., network security & administration). The script demonstrates basic file I/O, string manipulation, and list operations in Python.

## Problem Statement

Manually removing multiple IP addresses from an allow list in IT/security environments can be tedious and prone to human error. This project addresses the need for an automated solution to efficiently clean an `allow_list.txt` file by removing a predefined set of "unwanted" IP addresses.

## Technologies Used

* **Language:** Python 3 (developed in a Jupyter Notebook environment, but runnable as a standard Python script)
* **Editor:** Jupyter Notebook (for initial development and testing)
* **Input File:** `allow_list.txt` (simple text file with IP addresses separated by spaces or newlines)

## Algorithm & Script Breakdown

The automation is achieved through a simple, step-by-step Python algorithm:

1.  **Define Input and Removal List:**
    * `import_file`: Specifies the name of the text file containing the IP allow list.
    * `remove_list`: A Python list containing the IP addresses to be removed from the `allow_list.txt`.

2.  **Read File Contents:**
    * The `allow_list.txt` is opened in read mode (`"r"`).
    * The `with open(...) as file:` statement ensures the file is automatically closed, preventing resource leaks.
    * The entire content of the file (a string of IP addresses) is read into the `ip_addresses` variable.

3.  **Convert String to List:**
    * The `ip_addresses` string is split into a list of individual IP addresses using `.split()`. By default, `split()` separates the string by whitespace, making each IP address a separate list entry.

4.  **Remove Unwanted IP Addresses:**
    * The script iterates through each `element` (IP address) in the `ip_addresses` list.
    * If an `element` is found within the `remove_list`, it is removed from the `ip_addresses` list using `ip_addresses.remove(element)`.

5.  **Convert List Back to String:**
    * The `ip_addresses` list is joined back into a single string, with each IP address separated by a space, using `" ".join(ip_addresses)`. This prepares the data for writing back to the file.

6.  **Update the File:**
    * The `allow_list.txt` file is opened in write mode (`"w"`).
    * The modified `ip_addresses` string is written back to the file, effectively overwriting the original content with the updated list.

## How to Use (Simple Example)

1.  **Create `allow_list.txt`:**
    Create a file named `allow_list.txt` in the same directory as the Python script.
    *Example `allow_list.txt` content:*
    ```
    192.168.1.10 192.168.97.225 192.168.1.11 192.168.158.170 192.168.1.12
    192.168.201.40 192.168.1.13 192.168.58.57 192.168.1.14
    ```

2.  **Save the Python Script:**
    Save the following Python code as `update_allow_list.py` (or a similar name) in the same directory.

    ```python
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
    ```

3.  **Run the Script:**
    Open your terminal or command prompt, navigate to the directory where you saved the files, and run:
    ```bash
    python3 update_allow_list.py
    ```

## Future Improvements

* **Function with Parameters:** Encapsulate the logic within a function that accepts `import_file` and `remove_list` as parameters, making it reusable.
* **Error Handling:** Add more robust error handling (e.g., for empty files, invalid IP formats, parsing comments).
* **More Efficient Removal:** While this approach works for small lists, for very large lists, iterating and removing from the same list can be inefficient. A more optimized approach for large datasets might involve creating a *new* list that only includes elements not in the `remove_list`.
* **User Input:** Allow the user to input the file name and/or IP addresses to remove directly via the terminal.
* **Logging:** Implement basic logging to record when the script runs and what changes were made.
* **Backup:** Create a backup of the original `allow_list.txt` before modifying it.

## Contact

Feel free to connect with me on [LinkedIn](www.linkedin.com/in/ezra-park-779325330) if you have any questions or feedback.
