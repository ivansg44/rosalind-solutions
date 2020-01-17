#!/usr/bin/env python3

import argparse


def main(input_file, output_file):
    input_fp = open(input_file)
    input_text = input_fp.read().strip()
    input_fp.close()

    [homo_dom, hetero, homo_rec] = [int(x) for x in input_text.split()]
    total_pop = sum([homo_dom, hetero, homo_rec])

    probability = homo_dom/total_pop
    probability += hetero/total_pop * homo_dom/(total_pop - 1)
    probability += hetero/total_pop * (hetero - 1)/(total_pop - 1) * 0.75
    probability += hetero/total_pop * homo_rec/(total_pop - 1) * 0.5
    probability += homo_rec/total_pop * homo_dom/(total_pop - 1)
    probability += homo_rec/total_pop * hetero/(total_pop - 1) * 0.5

    output_fp = open(output_file, "w")
    output_fp.write(str(probability))
    output_fp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to .txt file containing "
                                           "three positive integers "
                                           "representing the number of "
                                           "individuals in a population that "
                                           "are homozygous dominant, "
                                           "heterozygous, and homozygous "
                                           "recessive for a factor "
                                           "respectively.")
    parser.add_argument("output_file", help="Path of file to write the "
                                            "probability that two randomly "
                                            "selected mating organisms from "
                                            "the input population will "
                                            "produce an individual possessing "
                                            "a dominant allele, assuming that "
                                            "any two organisms can mate.")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
