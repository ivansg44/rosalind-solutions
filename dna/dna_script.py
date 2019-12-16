#!/usr/bin/env python3

import argparse


def main(args):
    output_fp = open(args.input_file)
    dna_str = output_fp.read().strip()
    output_fp.close()

    counts = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nt in dna_str:
        counts[nt] += 1

    output_fp = open("dna_output.txt", "w")
    output_fp.write("%s %s %s %s"
                    % (counts["A"], counts["C"], counts["G"], counts["T"]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to .txt file containing a "
                                           "DNA string of length at most 1000 "
                                           "nt.")
    main(parser.parse_args())
