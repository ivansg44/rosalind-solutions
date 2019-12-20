#!/usr/bin/env python3

import argparse


def main(input_file, output_file):
    input_fp = open(input_file)
    dna_str = input_fp.read().strip()
    input_fp.close()

    rna_str = dna_str.replace("T", "U")

    output_fp = open(output_file, "w")
    output_fp.write(rna_str)
    output_fp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to .txt file containing a "
                                           "coding DNA string of length at "
                                           "most 1000 nt.")
    parser.add_argument("output_file", help="Path of file to write "
                                            "transcribed RNA string of input.")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
