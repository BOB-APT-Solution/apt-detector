import sys
import subprocess
import os
from optparse import OptionParser


MODULE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "modules/")
HWP_PARSER_PATH = os.path.join(MODULE_PATH, "hwp-parser/")
PDF_PARSER_PATH = os.path.join(MODULE_PATH, "pdf-analysis-module/")

def _command_pipeline(command:str) -> int:
    try:
        _ = subprocess.check_output(f'{command}',
            shell=True,
            stderr=subprocess.STDOUT,
        )
    except Exception as e:
        print(e)
        return -2

    return 1


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


    # if filename == *.hwp:
        # script_name = extract javascript from hwp and save it as filename.js
    # elif filename == *.xlsm:
        # script_name = do something that extracting vba script and save it as filename.vba
        

    # if script_name == '*.js':
        #command = _command_pipeline(f"python2 JS-Deobfuscator/deobfuscate.py {options.filename} {options.filename}")
        #print(f"[OBFUSCATE] python2 JS-Deobfuscator/deobfuscate.py {options.filename} {options.filename} ==> return code {command}")

        #raw_code = str
        #if command == 1: # success
        #    with open(options.filename, 'r') as f:
        #        raw_code = f.read().upper()

        #     print(f"{options.filename} malware result => {search_signature(raw_code)}")
    
