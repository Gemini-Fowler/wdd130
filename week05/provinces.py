def main():
    with open('provinces.txt', 'r') as file:
        provinces = [line.strip() for line in file]

    print("Original list of provinces:")
    print(provinces)

    if provinces:
        provinces.pop(0)

    if provinces:
        provinces.pop(-1)

    provinces = ["Alberta" if province == "AB" else province for province in provinces]

    alberta_count = provinces.count("Alberta")

    print("\nModified list of provinces:")
    print(provinces)
    print(f"\nNumber of occurrences of 'Alberta': {alberta_count}")

if __name__ == "__main__":
    main()
