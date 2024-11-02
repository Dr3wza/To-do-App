head_count = 0
total_count = 0
open("CoinFlips.txt", "a")

while True:

    result = input("Throw the coin and enter 'head' or 'tail' here: ")

    match result:
        case "head":
            head_count = head_count + 1
            total_count = total_count + 1

            probability = (head_count / total_count) * 100
            print(f"Heads: {probability}%")

            with open("CoinFlips.txt", "r") as Prev_file:
                results = Prev_file.readlines()

            results.append(result + "\n")

            with open("CoinFlips.txt", "w") as New_file:
                New_file.writelines(results)

        case "tail":
            total_count = total_count + 1

            probability = (head_count / total_count) * 100
            print(f"Heads: {probability}%")

            with open("CoinFlips.txt", "r") as Prev_file:
                results = Prev_file.readlines()

            results.append(result + "\n")

            with open("CoinFlips.txt", "w") as New_file:
                New_file.writelines(results)

        case "exit":
            exit()
