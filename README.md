# apt-detector

APT 공격 감지 프론트엔드


## Work flow

1. 파일을 매개변수로 apt-detector 
2. 입력으로 hwp, xls, docx 받아들임 ...
    1. 스크립트 추출 (javascript, vba)
  
3. 추출한 스크립트 타입별(.js, .vba)로 검출기에 입력
    1. 추출한 스크립트가 Javascript면 apt-detector에서 함수명 기반으로 검사
    2. 추출한 스크립트가 vba면 vba 검출기로 제어 넘김
    

## install

``` 
git submodule init
git submodule update
```
