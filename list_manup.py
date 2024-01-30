import argparse

CLI=argparse.ArgumentParser()

CLI.add_argument(
  "--list",
  nargs="*",
  type=int,
)

args = CLI.parse_args() #parsing


def manipulate_list(input_list):
    # Check if the length of the list is a multiple of 10
    if len(input_list) % 10 != 0:
        raise ValueError("List length must be a multiple of 10")

    # Remove items at positions that are a multiple of 2 or 3
    result_list = [item for index, item in enumerate(input_list) if (index + 1) % 2 != 0 and (index + 1) % 3 != 0]

    print(result_list)
    return result_list

manipulate_list(args.list)
