#!/usr/bin/env python3

import argparse


codon_table = {
    "UUU": "F",    "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F",    "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L",    "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L",    "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S",    "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S",    "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S",    "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S",    "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y",    "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y",    "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C",    "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C",    "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W",    "CGG": "R", "AGG": "R", "GGG": "G"
}


def main(input_file, output_file):
    input_fp = open(input_file)
    mrna = input_fp.read().strip()
    input_fp.close()

    start_codon_index = None
    for i in range(len(mrna)):
        if "".join(mrna[i:i+3]) == "AUG":
            start_codon_index = i
            break

    prot_str = ""
    if start_codon_index is not None:
        for i in range(start_codon_index, len(mrna), 3):
            codon = "".join(mrna[i:i+3])
            if codon_table[codon] == "Stop":
                break
            else:
                prot_str += codon_table[codon]

    output_fp = open(output_file, "w")
    output_fp.write(prot_str)
    output_fp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to .txt file containing an "
                                           "RNA string corresponding to a "
                                           "strand of mRNA (of length at most "
                                           "10 kbp).")
    parser.add_argument("output_file", help="Path of file to write the "
                                            "protein string encoded by the "
                                            "input RNA string.")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
