# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 15:51:11 2021

nama:sarahsakinah
nim:065002100033
prodi:sistem informasi
"""
print("@@@@  @@@  @@@@  @@@  @   @")
print("@     @ @  @  @  @ @  @   @")
print("@@@@  @@@  @@@@  @@@  @@@@@")
print("   @  @ @  @@    @ @  @   @")
print("   @  @ @  @ @   @ @  @   @")
print("@@@@  @ @  @  @  @ @  @   @")

string = list(map(str, input("masukan kalimat: ").lower()))

def vokal_kon(sarah):
  consonan=0
  vokal=0
  for i in range(0, len(string)):
    if string[i]=='s' or string[i]=='a' or string[i]=='r' or string[i]=='a' or string[i]=='h':
      vokal+=i
    else:
      consonan+=1
  print("Jumlah huruf Vokal adalah: ",vokal)
  print("Jumlah huruf konsonan adalah:",consonan)
  vokal_kon(string)