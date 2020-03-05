#!/usr/bin/env python3

import argparse


def fib(n, k):
    """See http://rosalind.info/problems/fib/.

    :type n: int
    :type k: int
    :rtype: int
    """
    return _fib_helper(1, 1, n-2, k)


def _fib_helper(fn_1, fn_2, n, k):
    if n <= 0:
        return fn_1

    return _fib_helper(k*fn_2+fn_1, fn_1, n-1, k)


def main(input_file, output_file):
    input_fp = open(input_file)
    [n, k] = input_fp.read().strip().split()
    input_fp.close()

    f_n = str(fib(int(n), int(k)))

    output_fp = open(output_file, "w")
    output_fp.write(f_n)
    output_fp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to .txt file containing two "
                                           "positive integers separated by a "
                                           "space. e.g., '5 3'")
    parser.add_argument("output_file", help="Path of file to write fibonacci "
                                            "output of input, as per sequence "
                                            "described at http://rosalind.info/"
                                            "problems/fib/.")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
