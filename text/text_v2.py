# 格式：
# 人名：商品，数量：商品2，数量 
# 不填数量默认为 1

import sys

def ProcessSingleFile(docname):
    try:
        with open(docname, 'r', encoding="utf-8") as f, open("RES_" + docname, "w", encoding="utf-8") as new:
            for line in f:
                customer = [x.strip() for x in line.split(" ")]
                for item in customer[1:]:
                    suffix = ",1" if ',' not in item else ""
                    new.write(f"{customer[0]}.{item}{suffix}\n")
        return "RES_" + docname
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def CountProducts(docname):
    try:
        with open(docname, 'r', encoding="utf-8") as doc:
            products = {}
            for line in doc:
                try:
                    parts = line.split(".")
                    product, quantity = parts[2], int(parts[3])
                    products[product] = products.get(product, 0) + quantity
                except IndexError:
                    print(f"Error in line format: {line.strip()} in file {docname}")

            # Print the products and their counts
            for product, count in products.items():
                print(f"{product} : {count}")
            print("---------------")
            for product in products:
                print(product)
            print("================")
    except Exception as e:
        print(f"An error occurred: {e}")


def AggregateFiles(number):
    try:
        with open("sum.txt", "w", encoding="utf-8") as new_file:
            for i in range(1, number + 1):
                try:
                    with open(f"RES_{i}.txt", "r", encoding="utf-8") as currDoc:
                        for line in currDoc:
                            new_file.write(line.replace(",", "."))
                except FileNotFoundError:
                    print(f"File RES_{i}.txt not found, skipping.")
    except Exception as e:
        print(f"An error occurred: {e}")


def multiRun(number):
    for i in range(1,number + 1):
        ProcessSingleFile(str(i) + ".txt")

    AggregateFiles(number)
    CountProducts("sum.txt")

def main(arg):
    multiRun(arg)

if __name__ == "__main__":
    main(int(sys.argv[1]))