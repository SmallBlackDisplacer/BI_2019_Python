import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("-m", "--min_length", type=int)
parser.add_argument("-k", "--keep_filtered", action='store_true')
parser.add_argument("-b", "--gc_bounds", nargs="+", type=int)
parser.add_argument("-o", "--output_base_name", type=str)

args_d = parser.parse_args()
# print(args_d)

def fastq_f(args):
    output_name = None
    if args.output_base_name is not None:
        output_name = args.output_base_name
    else:
        output_name = ''.join(args.filename.split('.')[:-1])

    inp = open(args.filename, 'r')
    passed = open(output_name + "__passed.fastq", 'w')
    failed = open(output_name + "__failed.fastq", 'w') if args.keep_filtered else None
    min_length = args.min_length or -1
    gc_bottom_bound = args.gc_bounds[0] if args.gc_bounds is not None else 0
    gc_top_bound = args.gc_bounds[1] if (args.gc_bounds is not None and len(args.gc_bounds) > 1) else 100

    # print (output_name)
    # print(min_length, gc_bottom_bound, gc_top_bound)

    def iterator():
        while True:
            yield 0
            yield 1
            yield 2
            yield 3

    read = [None, None, None, None]

    for (line, chunking) in zip(inp, iterator()):
        read[chunking] = line.strip()
        if chunking == 3:
            sequence = read[1]
            passes_min = len(sequence) >= min_length
            GC = 100.0 * len([x for x in sequence if x in "GC"]) / len(sequence)
            # print(GC)
            passes_gc_bottom = GC >= gc_bottom_bound
            passes_gc_top = GC <= gc_top_bound
            # print(passes_min, passes_gc_bottom, passes_gc_top)
            if all([passes_min, passes_gc_bottom, passes_gc_top]):
                # print("WRITINGpassed", read[1])
                passed.write("%s\n%s\n%s\n%s\n" % tuple(read))
            elif failed:
                # print("WRITINGfailed", read[1])
                failed.write("%s\n%s\n%s\n%s\n" % tuple(read))

    inp.close()
    passed.close()
    failed.close if failed else ""


if __name__ == '__main__':
    fastq_f(args_d)
