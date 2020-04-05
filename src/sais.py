import argparse
import time
import subprocess
from os.path import isfile
from Bio import SeqIO


def read_sequence(file_path):
    with open(file_path) as file:
        for record in SeqIO.parse(file, "fasta"):
            return str(record.seq)

def main():
    parser = argparse.ArgumentParser(description="Run SAIS algorithm on the given genome file")
    parser.add_argument("-g", "--genome", dest="file", required=True, help="Genome file")
    parser.add_argument("-o", "--output", dest="output", required=True, help="Output file")

    args = parser.parse_args()

    if not isfile(args.file):
        print(args.file, " is not a file")
        parser.print_usage()
        return

    text = read_sequence(args.file)
    print("Start printing sequence in file for the SAIS")
    start = time.time()
    sa_file = open("seq.txt", "w")
    sa_file.write(text + '$')
    sa_file.close()
    end = time.time()
    print("Done writing sequence in", end - start, "seconds")

    print("Start SAIS")
    subprocess.check_output(["./sais", "seq.txt", args.output])
    print("SAIS done")

if __name__ == "__main__":
    main()