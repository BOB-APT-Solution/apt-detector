import sys
import subprocess
import os
from optparse import OptionParser
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TESTS = os.path.join(ROOT, 'testset')
MODULE_PATH = os.path.join(ROOT, "module/")
HWP_PARSER_PATH = os.path.join(MODULE_PATH, "hwp-parser")
PDF_PARSER_PATH = os.path.join(MODULE_PATH, "pdf-analysis-module")
PYTHON_PATH = os.path.join(ROOT, "venv/bin")

def _print_result(file:str, result :bool):
    print("++++++++++++++++++")
    print(f"{file} malware result => {result}")
    print("++++++++++++++++++")
def _command_pipeline(command:str) -> int:
    try:
        _ = subprocess.check_call(f'{command}',
            shell=True,
            stdout=sys.stdout,
        )
    except Exception as e:
        print(e)
        return -2

    return 0


def search_signature(js: str) -> bool:
    signature = [
        "setcookie",
        "getcookie",
        "createxmlhttprequest",
        "unescape",
        "document.write",
        "element.appendChild",
        "dateObject.toGmtString",
        "newactivexobject",
        "document.createelement"
    ]

    for sig in signature:
        if sig.upper() in js:
            return True # yes virus

    return False # no virus
    
if __name__ == "__main__":
    
    usage = "usage: %prog --file=file.hwp"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file", dest="filename",
                      help="bob")
    
    (options, args) = parser.parse_args()
    
    file_name = options.filename
    pure_file_name = file_name.split('.')[0]
    abs_file_name = os.path.abspath(file_name)


    # if filename == *.hwp:
        # _command_pipeline(f"python {HWP_PARSER_PATH}/hwp-parser.py {abs_file_name}")
    # elif filename == *.xlsm:
        # script_name = do something that extracting vba script and save it as filename.vba
    # elif filename == *.pdf:
        # command = _command_pipeline(f"python {PDF_PARSER_PATH}/main.py --file {abs_file_name}")
    # pdf extract javascript

    if True == True: # .js
        with open(f"{pure_file_name}.js", 'r') as f:
            raw_code = f.read().upper()
            _print_result(f"{pure_file_name}.js", search_signature(raw_code))

