#include<iostream.h>
#include <stdio.h>
 
using namespace std;

int main(void)
{
  int nilai,nilai2;
  char nama[20],nama2[20];
  
  printf("/tData Mahasiswa Ke - 1\n");
  
  printf("Masukkan Nama Mahasiswa : ");
  scanf("%d",&nama);
  
  printf("Masukkan Nilai Mahasiswa : ");
  scanf("%d",&nilai);
  
  printf("/tData Mahasiswa Ke - 2\n");
  
  printf("Masukkan Nama Mahasiswa : ");
  scanf("%d",&nama2);
  
  printf("Masukkan Nilai Mahasiswa : ");
  scanf("%d",&nilai2);
  jumlah=nilai+nilai2;
  printf("\n");
  printf("\t\t Mahasiswa Telkom University\n");
  printf("Nama Mahasiswa Ke - 1 adalah: %d", nama);
  printf("Nama Mahasiswa Ke - 2 adalah: %d", nama2);
  printf("Jumlah Nilai 2 Mahasiswa adalah: %d", jumlah);
  printf("\n");
  
  return 0;
}