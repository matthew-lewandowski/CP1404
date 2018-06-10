def main():
    print("Hello")
    print(get_longest_line("file_name.txt"))


def get_longest_line(file_name):
    file_object = open(file_name, mode="r")
    # longest_line = 0
    # max_length = 0
    # for i, line in enumerate(file_object):
    #     if len(line) > max_length:
    #         max_length = len(line)
    #         longest_line = i
    results = max([(len(line), i) for i, line in enumerate(file_object)])
    file_object.close()
    # return (longest_line + 1), max_length
    return results[1] + 1, results[0]


main()
