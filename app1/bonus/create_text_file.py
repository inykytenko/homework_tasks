contents = ["All carrots are to be sliced ",
            "longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)


a = "I am a string" \
    "on my " \
    "own"
#open and read file
file = open("essay.txt", 'r')
content = file.read()
print(content.title())

#open, read and output chapters number
file = open("essay.txt", 'r')
content = file.read()

nr_chars = len(content)
print(nr_chars)
