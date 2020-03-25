#!/usr/bin/env python3

import argparse


def _find_longest_common_sub_str(strs):
    """Finds the longest common substring of multiple strings.

    :param list[str] strs: Strings to find the longest common
        substring of
    :return: Longest common substring of ``strs``
    :rtype: str
    """
    # Sort strs from shortest to longest
    strs.sort(key=len)

    shortest_str = strs[0]
    longer_strs = strs[1:]
    str_len_to_try = 1
    longest_sub_str_so_far = ""

    while True:
        for i in range(0, len(shortest_str)-str_len_to_try):
            str_to_try = shortest_str[i:i+str_len_to_try]

            is_sub_str = True
            for longer_str in longer_strs:
                if str_to_try not in longer_str:
                    is_sub_str = False
                    break

            # Found a sub-str
            if is_sub_str:
                longest_sub_str_so_far = str_to_try
                break

        # Found a new, longer sub-str
        if len(longest_sub_str_so_far) == str_len_to_try:
            str_len_to_try += 1
        # Did not find a new, longer sub-str
        else:
            break

    return longest_sub_str_so_far


def main(input_file, output_file):
    input_fp = open(input_file)

    dna_strs = []
    line = input_fp.readline().strip()
    while line != "":
        if line[0] == ">":
            dna_strs += [""]
        else:
            dna_strs[-1] += line

        line = input_fp.readline().strip()

    longest_common_sub_str = _find_longest_common_sub_str(dna_strs)

    input_fp.close()

    output_fp = open(output_file, "w")
    output_fp.write(longest_common_sub_str)
    output_fp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="A collection of k (k≤100) DNA "
                                           "strings of length at most 1 kbp "
                                           "each in FASTA format.")
    parser.add_argument("output_file", help="A longest common substring of "
                                            "the collection.")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
