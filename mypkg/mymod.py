#qn.str

def countlines(file_path):
    k = open(file_path,'r')
    m = k.readlines()
    k.close()

    lines = len(m)
    print(lines)
    


def countchar(file_path):
    c = open(file_path,'r')
    d = len(c.read())
    char = d
    c.close()
    count_char = print(char)


def count_both(file_path):
    count_lines = countlines(file_path)
    count_char = countchar(file_path)
    return count_lines, count_char






    









