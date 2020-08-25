# -*- coding: utf-8 -*- 

import sys
import os
from oletools.olevba import VBA_Parser, TYPE_OLE, TYPE_OpenXML, TYPE_Word2003_XML, TYPE_MHTML, detect_autoexec, VBA_Scanner
#PYTHON 2,3버전 모두 호환 
if sys.version_info[0]<= 2:
      #python 2
      from oletools.olevba import VBA_Parser
else:
     #python 3
     from oletools.olevba3 import VBA_Parser


def Extract_VBA(file_name : str)->str:
  result = ""  
  # VBA 퍼져 온 
  vbaparser = VBA_Parser(file_name)
  # 매크로 검사
  if not vbaparser.detect_vba_macros():
   print ("{} hasn't any vba codes".format(file_name))
 #경고모듈 넣는 위치 
   vbaparser.close()
   return result

  if vbaparser.detect_vba_macros():
   print ("{} has vba codes".format(file_name))
   for (_,_,_, vba_code) in  vbaparser.extract_macros():
     result += vba_code
    # 퍼져 닫기 
   vbaparser.close()
   return result





if __name__ == "__main__":
    Extract_VBA(sys.argv[1])
