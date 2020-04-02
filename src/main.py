import os
import subprocess
import time
import sys
import psutil
from os.path import isfile
from Bio import SeqIO

import bwt_fm_simple as bfs
import bwt_fm_optimized as bfo


def read_sequence(file_path):
    with open(file_path) as file:
        for record in SeqIO.parse(file, "fasta"):
            return str(record.seq)

def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024

usage = "-o(ptimized)/-s(imple) fasta_file patterns... "


def main():
    if len(sys.argv) < 3:
        print("Not enough arguments")
        print(usage)
        return
    
    algorithm = sys.argv[1]
    if not algorithm == "-o" and not algorithm == "-s":
        print("First argument must be -o for opitmized or -s for simple algorithm")
        print(usage)
        return

    file = sys.argv[2]
    if not isfile(file):
        print(file, "is not file")
        print(usage)
        return

    patterns = sys.argv[3:]

    print("Start analizing file ", file)
    print("Reading sequence from FASTA file")
    start = time.time()
    text = read_sequence(file)
    end = time.time()
    print("Reading done in", end - start, "seconds")

    if algorithm == "-s":
        print("Start making BwtFmSimple object")
        start = time.time()
        bwt_fm = bfs.BwtFmSimple(text)
        end = time.time()
        print("BwtFmSimple object created in", end - start, "seconds")
    else:
        print("Start printing sequence in file for the SAIS")
        start = time.time()
        sa_file = open("sequence.txt", "w")
        sa_file.write(text + '$')
        sa_file.close()
        end = time.time()
        print("Done writing sequence in", end - start, "seconds")

        print("Start SAIS")
        subprocess.check_output(["./sais", "sequence.txt", "sa_file.txt"])
        print("SAIS done")

        print("Start making BwtFmOptimized object")
        start = time.time()
        bwt_fm = bfo.BwtFmOptimized(text, 128, 128, "sa_file.txt")
        end = time.time()
        print("BwtFmSimple object created in", end - start, "seconds")

    for pattern in patterns:
        print("Start searching for", pattern)
        start = time.time()
        positions = bwt_fm.find_pattern(pattern)
        end = time.time()
        print(pattern, "found on", len(positions) if positions != None else 0, "positions in", end - start, "seconds")

    print("Memory usage is", memory_usage(), "MB")
    
if __name__ == "__main__":
    main()
