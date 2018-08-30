# filelist
데이터의 접근 주소의 목록이 필요할 때 이 코드를 사용하면 손쉽게 파일 목록을 작성할 수 있습니다.
기본적으로 csv 파일 포맷 out을 지원합니다.

# Dependencies
```
python3.5.x 
numpy
glob
```
# Usage
```
python3 fileNameList.py \
--source $YOUR_DATA_SOURCE \
--format $YOUR_DATA_FORMAT \
--depth $HOW_MANY_FOLDERS_TO_FIND_DATA \
--save $WHERE_TO_SAVE \
```
# Miscellaneous
1. numpy append 및 insert 활용
1. video data를 처리하기 위해 opencv를 활용하여 해당 비디오의 최대 프레임 count 가능

# To do
1. 4개 파일 간 데이터 연동 (클래스로 코드 작업하기)

# Contacts
seru_s@me.com

# License
MIT

