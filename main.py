formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]
special_commands = ["!help", "!done"]

def help():
    print("Available formatters: " + " ".join(formatters))
    print("Special commands: " + " ".join(special_commands))

def done(text):
    with open("output.md", "w") as file:
        file.write(text)
    exit()


def main():
    full_text = ""
    while True:
        formatter = input("Choose a formatter: ")
        if formatter in formatters:
            if formatter == "header":
                while True:
                    level = input("Level: ")
                    if level.isdigit() and 1 <= int(level) <= 6:
                        break
                    print("The level should be within the range of 1 to 6")
                text = input("Text: ")
                full_text += "#" * int(level) + " " + text + "\n"
                print(full_text)
            elif formatter == "plain":
                text = input("Text: ")
                full_text += text
                print(full_text)
            elif formatter == "bold":
                text = input("Text: ")
                full_text += "**" + text + "**"
                print(full_text)
            elif formatter == "italic":
                text = input("Text: ")
                full_text += "*" + text + "*"
                print(full_text)
            elif formatter == "inline-code":
                text = input("Text: ")
                full_text += "`" + text + "`"
                print(full_text)
            elif formatter == "link":
                label = input("Label :")
                url = input("URL: ")
                full_text += "[" + label + "]" + "(" + url + ")"
                print(full_text)
            elif formatter == "new-line":
                full_text += "\n"
                print(full_text)
            elif formatter == "ordered-list":
                while True:
                    rows = input("Number of rows: ")
                    if rows.isdigit() and int(rows) >= 1:
                        break
                    print("The number of rows should be greater than zero")
                full_text += "".join([f"{i + 1}. {input('Row #' + str(i + 1) + ': ')}\n" for i in range(int(rows))])
                print(full_text)
            elif formatter == "unordered-list":
                while True:
                    rows = input("Number of rows: ")
                    if rows.isdigit():
                        break
                    print("The number of rows should be greater than zero")
                full_text += "".join([f"* {input('Row #' + str(i + 1) + ': ')}\n" for i in range(int(rows))])
                print(full_text)
            continue
        elif formatter in special_commands:
            if formatter == "!help":
                help()
            elif formatter == "!done":
                done(full_text)
        else:
            print("Unknown formatting type or command.")

main()
