#!/usr/bin/env python3

import argparse


def fibd(n, m):
    """See http://rosalind.info/problems/fibd/.

    :type n: int
    :type m: int
    :rtype: int
    """
    return _fibd_helper([1, 1], 3, n, m)


def _fibd_helper(f_arr, n, max_n, m):
    if n > max_n:
        return f_arr[-1]

    f_arr.append(f_arr[-1] + f_arr[-2])

    # Rabbits have started dying
    if n > m:
        # Remove the oldest fn from f_arr, and subtract its value from
        # all other fn values in f_arr.
        fn_m = f_arr.pop(0)
        f_arr = list(map(lambda x: max(0, x-fn_m), f_arr))

    return _fibd_helper(f_arr, n+1, max_n, m)


def main(input_file, output_file):
    input_fp = open(input_file)
    [n, m] = input_fp.read().strip().split()
    input_fp.close()

    f_n = str(fibd(int(n), int(m)))

    output_fp = open(output_file, "w")
    output_fp.write(f_n)
    output_fp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to .txt file containing two "
                                           "positive integers separated by a "
                                           "space. e.g., '6 3'")
    parser.add_argument("output_file", help="Path of file to write fibonacci "
                                            "output of input, as per sequence "
                                            "described at "
                                            "http://rosalind.info/problems/"
                                            "fibd/.")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
