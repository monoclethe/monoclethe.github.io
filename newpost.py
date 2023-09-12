from datetime import datetime
htmlfile = []
with open("index.html") as f:
    htmlfile = f.readlines()

start = 21
end = 0
for line in htmlfile:
    end += 1
    if line == "        </div id=\"endposts\">\n":
        break

time = str(datetime.now())[:-7]
title = input("Title: ")
content = input("Content: ")
print("<p><strong>" + time + " - " + title + "</strong><br>" + content + "</p>")
if bool(input("Is this correct? true/false ")):
    htmlfile.insert(end-1, "            <p><strong>" + time + " - " + title + "</strong><br>" + content + "</p>\n")

with open("index.html", "r+") as f:
    f.truncate(0)
    f.writelines(htmlfile)
    f.close()