#!/usr/bin/env python3

import argparse


def main(input_file, output_file):
    input_fp = open(input_file)
    dna_str = input_fp.read().strip()
    input_fp.close()

    complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
    dna_complement_str = ""
    for nt in reversed(dna_str):
        dna_complement_str += complements[nt]

    output_fp = open(output_file, "w")
    output_fp.write(dna_complement_str)
    output_fp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to .txt file containing a "
                                           "DNA string of length at most 1000 "
                                           "bp.")
    parser.add_argument("output_file", help="Path of file to write reverse "
                                            "complement of input.")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
