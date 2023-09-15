#!/usr/bin/env python

# NOTE: This program takes for granted that "ranking.txt" should already exist

# read ranking data

with open("ranking.txt", 'r') as file:
	ranking: list[str] = file.read().split('\n')

	# above line adds an empty item to end of list which needs removing

	ranking.pop()

# menu loop

while True:
	print()

	print("*** MAIN MENU ***")
	print("* 1: Print List")
	print("* 2: Add Item to End")
	print("* 3: Remove Last Item")
	print("* 4: Insert at Position")
	print("* 5: Remove at Position")
	print("* 6: Move to Position")
	print("* 7: Edit Item")
	print("* 8: Exit")

	option: str = input("* Enter Option #: ")

	print()

	match option:
		case '1':
			pass # results printed at the end
		case '2':
			print("ADD ITEM TO END")
			item: str = input("Enter item: ")
			ranking.append(item)

			print()
		case '3':
			print("REMOVE LAST ITEM")
			print(f"{ranking[-1]} removed from end of list.")
			ranking.pop()

			print()
		case '4':
			print("INSERT ITEM")
			position: int = int(input("Insert Position: "))
			item: str = input("Item to Insert: ")

			ranking.insert(position - 1, item)

			print()
		case '5':
			print("REMOVE AT POSITION")
			index: int = int(input("Position to remove: ")) - 1

			print(f"{ranking[index]} removed from position {index + 1}.")
			ranking.pop(index)

			print()
		case '6':
			print("MOVE TO POSITION")
			index_from: int = int(input("Move Item from: ")) - 1
			index_to: int = int(input("Move Item to: ")) - 1

			item: str = ranking[index_from]
			ranking.pop(index_from)
			ranking.insert(index_to, item)

			print()
		case '7':
			print("EDIT ITEM")
			position: int = int(input("Enter position: "))
			replacement: str = input("Replace with: ")

			ranking[position - 1] = replacement

			print()
		case '8':
			break
		case _:
			print("Invalid option. Try again...")

	# print results

	print("RANK LIST")

	if len(ranking) > 0:
		for i in range(len(ranking)):
			print(f"{i + 1}: {ranking[i]}")
	else:
		print("No Items in the Rank List")

	# save results

	with open("ranking.txt", 'w') as file:
		content: str = ''

		for item in ranking:
			content += item + '\n'

		file.write(content)
