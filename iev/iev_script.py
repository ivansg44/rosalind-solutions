#!/usr/bin/env python3

import argparse


couple_probs = [1, 1, 1, 0.75, 0.5, 0]


def main(input_file, output_file):
    input_fp = open(input_file)
    input_text = input_fp.read().strip()
    couple_counts = [int(x) for x in input_text.split(" ")]
    input_fp.close()

    expected_number = 0
    for i in range(len(couple_counts)):
        couple_count = couple_counts[i]
        couple_prob = couple_probs[i]
        expected_number += couple_count * couple_prob
        expected_number += couple_count * couple_prob

    output_fp = open(output_file, "w")
    output_fp.write(str(expected_number))
    output_fp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to .txt file containing six "
                                           "nonnegative integers, each of "
                                           "which does not exceed 20,000. The "
                                           "integers correspond to the number "
                                           "of couples in a population "
                                           "possessing each genotype pairing "
                                           "for a given factor. In order, the "
                                           "six given integers represent the "
                                           "number of couples having the "
                                           "following genotypes:\n"
                                           "1. AA-AA 2. AA-Aa 3. AA-aa "
                                           "4. Aa-Aa 5. Aa-aa 6. aa-aa")
    parser.add_argument("output_file", help="Path of file to write the "
                                            "expected number of offspring "
                                            "displaying the dominant "
                                            "phenotype in the next "
                                            "generation, under the assumption "
                                            "that every couple has exactly "
                                            "two offspring.")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
