#!/usr/bin/env python3

import argparse
from math import factorial


def main(input_file, output_file):
    input_fp = open(input_file)
    k, N = [int(x) for x in input_fp.readline().split()]
    input_fp.close()

    sum_probability = 0
    for i in range(N, 2**k + 1):
        probability_of_i_AaBb = 0.25**i * 0.75**(2**k-i)
        binomial_dist_i_count = \
            factorial(2**k) / (factorial(i) * factorial(2**k - i))
        sum_probability += probability_of_i_AaBb * binomial_dist_i_count

    output_fp = open(output_file, "w")
    output_fp.write(str(round(sum_probability, 3)))
    output_fp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Two positive integers k and N "
                                           "described at "
                                           "http://rosalind.info/problems/"
                                           "lia/.")
    parser.add_argument("output_file", help="Probability described at "
                                            "http://rosalind.info/problems/"
                                            "lia/.")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
