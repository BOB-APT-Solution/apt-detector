import sys
import subprocess
from optparse import OptionParser


def _command_pipeline(command:str) -> int:
    try:
        _ = subprocess.check_output(f'{command}',
            shell=True,
            stderr=subprocess.STDOUT,
        )
    except Exception as e:
        print(e)
        return -2


if __name__ == "__main__":
    usage = "usage: %prog --file=file.hwp"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file", dest="filename",
                      help="bob")
    
    (options, args) = parser.parse_args()

    print(options.filename)

    
    