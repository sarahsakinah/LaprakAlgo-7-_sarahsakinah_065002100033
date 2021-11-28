# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 16:16:32 2021

nama :sarah sakinah
nim:065002100033
prodi :sistem informasi
"""

def main(ss):
    if ss %5==0:
        ss**5 
        print ("hasilnya adalah",ss**5)
    else:
        cek(nomor)
def cek(ss):
    if ss %5!=0:
        print ("false")
        exit(0)
nomor=int(input("masukan bilangan: "))
main(nomor)