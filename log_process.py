import time
import re
import argparse
import os
import yaml


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', help='Full path of log file', required=True)
    return parser


if __name__ == "__main__":
    parser = get_arg_parser()
    args = parser.parse_args()
    log = args.log

    output = []
    with open(log, 'r') as f:
        for line in f:
            matchObj = re.search(r'global_step/sec: \d+(\.\d+)?', line)
            if matchObj:
                output.append(matchObj.group()[17:])

    gstep = [float(i) for i in output[20:30]]
    avg = sum(gstep) / len(gstep)

    print("Training throughput is %0.2f" % (avg * 512))
