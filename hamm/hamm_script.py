#!/usr/bin/env python3

import argparse


def main(input_file, output_file):
    input_fp = open(input_file)
    dna_str_one = input_fp.readline().strip()
    dna_str_two = input_fp.readline().strip()
    input_fp.close()

    hamm_distance = 0
    for i in range(len(dna_str_one)):
        if dna_str_one[i] != dna_str_two[i]:
            hamm_distance += 1

    output_fp = open(output_file, "w")
    output_fp.write(str(hamm_distance))
    output_fp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to .txt file containing two "
                                           "DNA strings of equal length (not "
                                           "exceeding 1 kbp).")
    parser.add_argument("output_file", help="Path of file to write the "
                                            "Hamming distance of the input.")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
