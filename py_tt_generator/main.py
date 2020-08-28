import os
import fileinput

print("\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ENTER LINK WITHOUT HTTPS://!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n")
subject = []
links = []
day_list = ['a', 'b', 'c', 'e', 'f', 'g']

days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday"
}
for i in range(6):
    print(
        f"==============================================={days[i]}=============================================\n\n\n")
    for j in range(10):
        sub = str(input(f"Hour {j + 1} Sub Name: "))
        link = str(input(f"Hour {j + 1} Sub Link: "))
        subject.append(sub if sub else "-")
        if link:
            if link[0:4] == 'http':
                links.append(link)
            else:
                links.append(f'https://{link}')
        else:
            links.append(' ')

os.rename("index.html", "timetable.txt")
count = 0
for i in day_list:
    for j in range(10):
        # f1 = open('timetable.txt', 'r')
        # f2 = open('file2.txt', 'w')
        with fileinput.FileInput("timetable.txt", inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace(f'{i}{j}', f"<a href = \"{links[count]}\" target = \"_blank\">{subject[count]}</a>"),end='')
        count += 1
        # f1.close()
        # f2.close()
        # os.remove('timetable.txt')
        # os.rename("file2.txt", "timetable.txt")

os.rename("timetable.txt", "timetable.html")
os.remove("timetable.txt.bak")

print(subject)
print(links)
