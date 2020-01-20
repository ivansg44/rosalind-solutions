#!/usr/bin/env python3

import argparse


def main(input_file, output_file):
    input_fp = open(input_file)
    dna_str_1 = input_fp.readline().strip()
    dna_str_2 = input_fp.readline().strip()
    input_fp.close()

    locations = []
    for i in range(len(dna_str_1)):
        if dna_str_1[i : i+len(dna_str_2)] == dna_str_2:
            locations.append(str(i+1))

    output_fp = open(output_file, "w")
    output_fp.write(" ".join(locations))
    output_fp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to .txt file containing two "
                                           "DNA strings of length at most 10 "
                                           "kbp.")
    parser.add_argument("output_file", help="Path of file to write all "
                                            "locations of the second input "
                                            "DNA string in the first.")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
