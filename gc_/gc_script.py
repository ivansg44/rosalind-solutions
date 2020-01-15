#!/usr/bin/env python3

import argparse


def main(input_file, output_file):
    input_fp = open(input_file)

    curr_id, max_id = "", ""
    max_percent = 0
    curr_cg, curr_total = 0, 0
    while True:
        line = input_fp.readline()
        # Ignore ``\n``
        line = line.strip()

        # New string or EOF
        if line == "" or line[0] == ">":
            if curr_total:
                curr_percent = curr_cg/curr_total * 100
                if curr_percent > max_percent:
                    max_id = curr_id
                    max_percent = curr_percent

            # EOF
            if line == "":
                break
            # New string
            else:
                curr_id = line[1:]
                curr_cg, curr_total = 0, 0
        else:
            curr_total += len(line)
            for base in line:
                if base == "C" or base == "G":
                    curr_cg += 1

    input_fp.close()

    output_fp = open(output_file, "w")
    output_fp.write(max_id + "\n" + str(max_percent))
    output_fp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to .txt file containing at "
                                           "most 10 DNA strings in FASTA "
                                           "format (of length at most 1000 bp "
                                           "each).")
    parser.add_argument("output_file", help="Path of file to write the ID of "
                                            "the input string having the "
                                            "highest GC-content, followed by "
                                            "the GC-content of that string.")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
