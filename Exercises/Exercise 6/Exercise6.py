filenames = ['doc.txt', 'report.txt', 'presentation.txt']

contents = ["hello", "hello", "hello"]

for filename, content in zip(filenames, contents):
    file = open(filename, "w")
    file.write(content)
    file.close()
