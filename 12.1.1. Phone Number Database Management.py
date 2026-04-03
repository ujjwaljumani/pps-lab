def manage_phonebook():
	phonebook = {}
	line = input().strip()
	if not line:
		return
	n = int(line)
	for _ in range(n):
		operation = input().split()
		if not operation:
			continue
		command = operation[0]

        if command == "ADD":
            name = operation[1]
            phone = operation[2]
            phonebook[name] = phone
        elif command == "REMOVE":
            name = operation[1]
            phonebook.pop(name, None)
                    
        elif command == "DISPLAY":
            if not phonebook:
                print("No contacts")
            else:
                sorted_names = sorted(phonebook.keys())
                for name in sorted_names:
                    print(f"{name}: {phonebook[name]}")

if __name__ == "__main__":
    manage_phonebook()
