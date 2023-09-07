# Rocky is a software engineer and he is creating his own operating system called “myFirst os”. myFirst os is a GUI (
# Graphical user interface) based operating system where everything is stored in files and folders. He is facing
# issues on  creating unique folder names for the operating system . Help rocky to create the unique folder name for
# it’s os.If folder name already exists in the system and integer number is added at the name to make it unique. The
# integer added starts with 1 and is incremented by 1 for each new request of an existing folder name. Given a list
# of folder names , process all requests and return an array of corresponding folder names.

items = input()
items_list = items.split(" ")
new_items = []
visited = {}
for i in range(len(items_list)):
    if items_list[i] not in visited:
        visited[items_list[i]] = 1
        new_items.append(items_list[i])
    else:
        new_items.append(items_list[i] + str(visited[items_list[i]]))
        visited[items_list[i]] += 1

print(new_items)
