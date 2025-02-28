import re


def main():
    good_rows = []
    with open("./Day 5/input.txt", "r") as file:
        rules, updates = file.read().strip().split("\n\n")
    updates = updates.split("\n")

    for pages in updates:
        if check_page(pages, rules):
            good_rows.append(pages)

    print(answer(good_rows))


def answer(good_rows):
    answer = 0
    for pages in good_rows:
        pages = pages.split(",")
        middle = pages[int((len(pages)-1)/2)]
        answer += int(middle)
    return answer



def check_page(pages, rules):
    pages = pages.split(",")
    for index, page in enumerate(pages[1:]):
        matches = re.findall(rf"{page}\|(\d*)\n", rules)
        for match in matches:
            if match in pages[:index+1]:
                return False
    return True


if __name__ == "__main__":
    main()