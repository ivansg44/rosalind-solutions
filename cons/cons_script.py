#!/usr/bin/env python3

import argparse
import typing


def _fasta_dna_strs(input_fp):
    """Iterate through DNA strings in FASTA file.

    Ignores ID values and newline characters.

    :param typing.TextIO input_fp: Fasta file pointer
    """
    # Skip first id
    next(input_fp)

    eof = False
    while not eof:
        dna_str = ""
        while True:
            next_line = input_fp.readline().strip()
            if not next_line:
                eof = True
                break
            if next_line[0] == ">":
                break
            dna_str += next_line

        yield dna_str


def main(input_file, output_file):
    input_fp = open(input_file)

    first_dna_str = True
    profile_matrix = []

    for dna_str in _fasta_dna_strs(input_fp):
        # Use first DNA str to populate profile_matrix with
        # appropriate amount of 0's.
        if first_dna_str:
            for i in range(4):
                profile_matrix.append([0] * len(dna_str))
            first_dna_str = False

        for i in range(len(dna_str)):
            if dna_str[i] == "A":
                profile_matrix[0][i] += 1
            elif dna_str[i] == "C":
                profile_matrix[1][i] += 1
            elif dna_str[i] == "G":
                profile_matrix[2][i] += 1
            elif dna_str[i] == "T":
                profile_matrix[3][i] += 1

    input_fp.close()

    cons_str = ""
    cons_str_len = len(profile_matrix[0])
    for i in range(cons_str_len):
        max_ = 0
        max_j = 0
        for j in range(4):
            if profile_matrix[j][i] > max_:
                max_ = profile_matrix[j][i]
                max_j = j

        if max_j == 0:
            cons_str += "A"
        elif max_j == 1:
            cons_str += "C"
        elif max_j == 2:
            cons_str += "G"
        elif max_j == 3:
            cons_str += "T"

    output_fp = open(output_file, "w")
    output_fp.write(cons_str + "\n")
    output_fp.write("A: " + " ".join(str(x) for x in profile_matrix[0]) + "\n")
    output_fp.write("C: " + " ".join(str(x) for x in profile_matrix[1]) + "\n")
    output_fp.write("G: " + " ".join(str(x) for x in profile_matrix[2]) + "\n")
    output_fp.write("T: " + " ".join(str(x) for x in profile_matrix[3]))
    output_fp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to .txt file containing a "
                                           "collection of at most 10 DNA "
                                           "strings of equal length (at most "
                                           "1 kbp) in FASTA format.")
    parser.add_argument("output_file", help="Path of file to write a "
                                            "consensus string and profile "
                                            "matrix for the input collection.")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
