#!/usr/bin/env python3

import argparse


def main(input_file, output_file):
    input_fp = open(input_file)

    # [[sample_id, prefix, suffix], ...]
    samples = []

    next_line = input_fp.readline().strip()
    while next_line:
        # Remove ``\n``
        sample_id = next_line[1:]

        # Read sample DNA str. Possibly multiple lines.
        sample = input_fp.readline().strip()
        while True:
            next_line = input_fp.readline().strip()
            if next_line != "" and next_line[0] != ">":
                sample += next_line
            else:
                break

        samples += [[sample_id, sample[0:3], sample[-3:]]]

    input_fp.close()

    # ["sample_id_1 sample_id_3", ...]
    edges = []

    for [s_id, _, s_suffix] in samples:
        for [t_id, t_prefix, _] in samples:
            if s_id != t_id and s_suffix == t_prefix:
                edges += ["%s %s" % (s_id, t_id)]

    output_fp = open(output_file, "w")
    output_fp.write("\n".join(edges))
    output_fp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to .txt file containing DNA "
                                           "strings in FASTA format having "
                                           "total length at most 10 kbp.")
    parser.add_argument("output_file", help="Path of file to write the "
                                            "unordered adjacency list "
                                            "corresponding to the overlap "
                                            "graph described at "
                                            "http://rosalind.info/problems/"
                                            "grph/.")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
