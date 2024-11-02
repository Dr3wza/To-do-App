contents = ["All carrots must be sliced longitudinally",
            "The carrots were sliced",
            "The slicing was well presented"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../ExperimentalFolder/{filename}", "w")
    file.write(content)

a = ("I am a string"
     " on my own")