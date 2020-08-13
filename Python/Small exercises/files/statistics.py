def statistics(input_file):
    with open(input_file) as file:
        file_whole = file.read()
    line_number = len(file_whole.split("\n"))
    word_number = len(file_whole.split())
    character_number = len(file_whole)
    results = {"lines": line_number, "words": word_number, "characters": character_number}
    return results
    
   



statistics("story.txt")


"""simplified as:
def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }"""