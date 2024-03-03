import datetime
doctext = ""
addIndex = 0

with open("index.html", "r+", encoding="utf8") as doc:
    doctext = str(doc.read())
    docparts = doctext.split("<!--newpost-->")
    title = input("Title: ")
    content = input("Content: ")

    tsuffix = " AM"

    t = datetime.datetime.now()
    if t.hour >= 12:
        tsuffix = " PM"
    formatted_t = str(t.month) + "/" + str(t.day) + "/" + str(t.year) + " - " + "{:02d}:{:02d}".format(t.hour % 12, t.minute) + tsuffix

    inject = "<!--newpost-->\n                <div class=\"post\">\n                 <h3>" + title + "</h3>\n                    <span class=\"date\">" + formatted_t + "</span><br>\n                   " + content + "\n                </div>"

    doc.truncate(0)
    doc.seek(0)
    doc.write(docparts[0] + inject + docparts[1])