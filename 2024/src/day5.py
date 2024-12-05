import os


def main(path_=None, verbose=1):
    if path_ is None:
        data = [
            "47|53",
            "97|13",
            "97|61",
            "97|47",
            "75|29",
            "61|13",
            "75|53",
            "29|13",
            "97|29",
            "53|29",
            "61|53",
            "97|53",
            "61|29",
            "47|13",
            "75|47",
            "97|75",
            "47|61",
            "75|61",
            "47|29",
            "75|13",
            "53|13",
            "",
            "75,47,61,53,29",
            "97,61,53,29,13",
            "75,29,13",
            "75,97,47,61,53",
            "61,13,29",
            "97,13,75,29,47",
        ]
        # Solution = 143
    else:
        with open(path_, "r") as file:
            data = file.readlines()
            data = [_.strip() for _ in data]
    if verbose > 0:
        print(data)
        print("\n".join(data))

    # Read and clean data
    conditions = data[:data.index("")]
    rules = parse_conditions(conditions)

    pages = data[data.index("") + 1:]
    pages = clean_pages(pages)

    sol_1, sol_2 = assert_order_and_sort_if_wrong(rules, pages)
    print(f"Solution Day 5 - Part 1: {sol_1}")
    print(f"Solution Day 5 - Part 2: {sol_2}")


def assert_order_and_sort_if_wrong(rules_, pages_):
    accum1 = 0
    accum2 = 0
    for page_ in pages_:
        is_valid = verify_order(page_, rules_)
        if is_valid:
            accum1 += page_[len(page_) // 2]
        else:
            fixed_order = fix_order(page_, rules_)
            accum2 += fixed_order[len(fixed_order) // 2]
    return accum1, accum2


def fix_order(page, rules):
    reordered_page = page.copy()
    while not verify_order(reordered_page, rules):
        for r in rules:
            if r[0] in reordered_page and r[1] in reordered_page:
                if reordered_page.index(r[0]) > reordered_page.index(r[1]):
                    t1 = reordered_page.index(r[0])
                    t2 = reordered_page.index(r[1])
                    reordered_page[t2] = r[0]
                    reordered_page[t1] = r[1]
                    break
    return reordered_page


def verify_order(page, rules):
    for r in rules:
        if r[0] in page and r[1] in page:
            if page.index(r[0]) > page.index(r[1]):
                return False
    return True


def parse_conditions(cond):
    rules_ = []
    for condition in cond:
        numbers = condition.split("|")
        rules_.append([int(x) for x in numbers])
    return rules_


def clean_pages(pag):
    cleaned_pages = []
    for p in pag:
        pa = p.split(",")
        cleaned_pages.append([int(x) for x in pa])
    return cleaned_pages


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day5.txt"

    path = os.path.join(datapath, filename)
    main(path)
