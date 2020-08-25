 #-*- coding: utf-8 -*-
import os
import argparse

def MalFunc(Funcname):
  # 1. 파일 접근 관련 (R/W)
  if Funcname.find("For Output As")!=-1: return "파일 접근 관련 (Open문 Output)"
  if Funcname.find("For Input As")!=-1: return "파일 접근 관련 (Open문 Input)"
  if Funcname.find("For Append As")!=-1: return "파일 접근 관련 (Open문 Appen)"
  if Funcname.find("URLDownloadToFile")!=-1: return "파일 접근 관련 (URLDownloadToFile API)"
  if Funcname.find("WriteFile")!=-1: return "파일 접근 관련 (WriteFile API)"
  if Funcname.find("ReadFile")!=-1: return "파일 접근 관련 (ReadFile API)"
  if Funcname.find("FindFirstFile")!=-1: return "파일 검색 관련 (FindFirstFile API)"
  if Funcname.find("FileCopy(")!=-1: return "파일 복사 관련 (FileCopy 함수)"
  if Funcname.find("FileCopy ")!=-1: return "파일 복사 관련 (FileCopy 함수)"
  if Funcname.find("CopyFile")!=-1: return "파일 복사 관련 (CopyFile API)"
  if Funcname.find("Kill ")!=-1: return "파일 삭제 관련 (Kill 함수)"
  if Funcname.find("Kill(")!=-1: return "파일 삭제 관련 (Kill 함수)"
  if Funcname.find("DeleteFile")!=-1: return "파일 삭제 관련 (DeleteFile API)"
  if Funcname.find("CreateFile")!=-1: return "파일 삭제 관련 (CreateFile API)"
  # 2. 파일 실행 관련
  if Funcname.find("ShellExecute")!=-1: return "파일 실행 관련 (ShellExecut API)"
  if Funcname.find("Shell ")!=-1: return "파일 실행 관련 (Shell 함수)"
  if Funcname.find("Shell(")!=-1: return "파일 실행 관련 (Shell 함수)"
  if Funcname.find("Auto_Open(")!=-1: return "파일 실행 관련 (AutoOpen 함수)"
  # 3. 오브젝트 관련
  if Funcname.find("GetObject")!=-1: return "오브젝트 관련 (GetObject API)"
  if Funcname.find("CreateObject")!=-1: return "오브젝트 관련 (CreateObject API)"
  if Funcname.find("As Object")!=-1: return "오브젝트 변수"
  # 4. 메모리 관련
  if Funcname.find("ReadProcessMemory")!=-1: return "메모리 접근 관련 (ReadProcessMemory API)"
  if Funcname.find("WriteProcessMemory")!=-1: return "메모리 접근 관련 (WriteProcessMemory API)"
  # 5. 프로세스 관련
  if Funcname.find("CreateProcess")!=-1: return "프로세스 관련 (CreateProcess API)"
  if Funcname.find("OpenProcess")!=-1: return "프로세스 관련 (OpenProcess API)"
  if Funcname.find("WinExec")!=-1: return "프로세스 관련 (WinExec API)"
  if Funcname.find("SendMessage")!=-1: return "프로세스 관련 (SendMessage API)"
  if Funcname.find("PostMessage")!=-1: return "프로세스 관련 (PostMessage API)"
  # 6. 레지스트리 관련
  if Funcname.find("RegSetValue")!=-1: return "레지스트리 관련 (RegSetValue API)"
  if Funcname.find("RegEnumValue")!=-1: return "레지스트리 관련 (RegEnumValue API)"
  if Funcname.find("RegDeleteKey")!=-1: return "레지스트리 관련 (RegDeleteKey API)"
  if Funcname.find("RegCreateKey")!=-1: return "레지스트리 관련 (RegCreateKey API)"
  if Funcname.find("OpenProcessToken")!=-1: return "레지스트리 관련 (OpenProcessToken API)"
  # 7. 마우스, 키보드 제어 관련
  if Funcname.find("mouse_event")!=-1: return "마우스 제어 관련 (mouse_event API)"
  if Funcname.find("keybd_event")!=-1: return "키보드 제어 관련 (keybd_event API)"
  if Funcname.find("SetCursorPos")!=-1: return "마우스 제어 관련 (SetCursorPos API)"
  # 8. 스레드 관련
  if Funcname.find("CreateThread")!=-1: return "스레드 관련 (CreateThread API)"
  if Funcname.find("ResumeThread")!=-1: return "스레드 관련 (ResumeThread API)"
  if Funcname.find("CreateRemoteThread")!=-1: return "스레드 관련 (CreateRemoteThread API)"
  # 9. 정상 파일
  return ""


def find_malicious_code_from_vba(vba_code):
  MalCount = 0
  vba_code = vba_code.split('\r\n')
  for number, line in enumerate(vba_code): 
    if MalFunc(line):
      print("악성 명령 감지 [line :{0}, {1}]".format(number, MalFunc(line)))
      MalCount += 1
  if MalCount:
    print("※ 악성 매크로 파일\n 탐지한 악성 명령 수 : {}".format(MalCount))
  else:
    print("※ 정상 매크로 파일") 

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('-path', dest="path",help="What is the first number?")
  args = parser.parse_args()
  path1=str(args.path)
  MalCou = 0
  if os.path.isfile(path1) :
    with open(path1, "rt", encoding='UTF8') as fILE :
      Cou = 0
      while True :
        line = fILE.readline()
        if not line :
          if (MalCou == 1):
            print("※ 악성 매크로 파일")
          else:
            print("※ 정상 매크로 파일") 
          break
        Cou = Cou + 1
        if MalFunc(line) != 1 :
          print("악성 명령 감지 [line :", Cou, ", ", MalFunc(line), "]")
          MalCou = 1






