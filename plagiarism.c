//plagiarism checker
//Ashley Roberson

#include<stdbool.h>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include "CUnit.h"

int f1next, f2next;
int similar, size;
int hashIndex;
char key;


#define SIZE 20
#define ORIGINAL 1
#define FILETOCHECK 2

void hash(char *word){
	int i;
	int sum = 0;
	int length = strlen(word);
	for(; *word != '\0'; word++){
		sum = sum * 31 + *word;}	
    	hashIndex = sum % SIZE;}

void testHash(){
	hash("0");
	CU_ASSERT(48 == hashIndex);
	hash("10");
	CU_ASSERT(7 == hashIndex );
	hash("word");
	CU_ASSERT(19 == hashIndex);
	hash("hello world");
	CU_ASSERT(14 == hashIndex);}


char table1[SIZE][256];
int numTable1[SIZE];
char table2[SIZE][256];
int numTable2[SIZE];

/* lookup: look for word in hashtable */
int lookup(char *word, int place){
	hash(word);
	if(place  == ORIGINAL){
        	if(table1[hashIndex] == word){
        		return 1;}
		else{
			return 0;}}
	else{
		if(table2[hashIndex] == word){
			return 1;}
		else{
			return 0;}}}

void testLookup(){
	insert("0", 1);
	insert("10", 1);
	insert("hello", 1);
	insert("hello world", 1);
	CU_ASSERT(1 == lookup("hello", 1);
	CU_ASSERT(0 == lookup("hello", 2);
	CU_ASSERT(0 == lookup("igloo", 2);
	CU_ASSERT(1 == lookup("10", 1);}
	
/* install: put (key, value) in hashtab */
void insert(char *word, int place){
	if(place == ORIGINAL){
		if(lookup(word, ORIGINAL) == 0){
			strcpy(table1[hashIndex], word);
			numTable1[hashIndex] = numTable1[hashIndex] + 1;}
		else{
    			while(table1[hashIndex] != 0){
				hashIndex++;
				if(hashIndex > SIZE){
					hashIndex = 0;}}
			strcpy(table1[hashIndex], word);
			numTable1[hashIndex] = numTable1[hashIndex] + 1;}}
	else{
		if(lookup(word, FILETOCHECK) == 0){
			strcpy(table2[hashIndex], word);
			numTable2[hashIndex] = numTable2[hashIndex] + 1;}
		else{
    			while(table2[hashIndex] != 0){
				hashIndex++;
				if(hashIndex > SIZE){
					hashIndex = 0;}}
			strcpy(table2[hashIndex], word);
			numTable2[hashIndex] = numTable2[hashIndex] + 1;}}}

void testInsert(){
	insert("hello", 1);
	CU_ASSERT(strcmp("hello", numTable1[hashIndex]) == 0);
	CU_ASSERT(strcmp("hello", numTable2[hashIndex]) != 0);
	insert("0", 1);
	CU_ASSERT(strcmp("0", numTable1[hashIndex]) == 0);
	insert("hello world", 2);
	CU_ASSERT(strcmp("hello world", numTable1[hashIndex]) != 0);
	CU_ASSERT(strcmp("hello world", numTable2[hashIndex]) == 0);}}


void display(){
	int i;
	printf("Original File				File to Check\n");
	for(i = 0; i < SIZE; i++){
		printf("Index %d: %s %d				Index %d: %s %d\n", i, table1[i], numTable1[i], i, table2[i], numTable2[i]);}}

/*void getChar(FILE *file1, FILE *file2){
	f1next = getc(file1);
	f2next = getc(file2);}*/

void similarity(){
	int i;
	int similar = 0;
	for(i = 0; i < SIZE; i++){
		if(strcmp(table1[i], table2[i]) == 0 && table1[i] != 0){
			similar++;}}
	similar = similar * 100 / SIZE;
	printf("File 2 is %d %% similar to File 1\n", similar);}

void testSimilarity(){
	insert("hello", 1);
	CU_ASSERT(0 == similarity();
	insert("hello", 2);
	insert("world", 1);
	insert("igloo", 2);
	CU_ASSERT(50 == similarity();
	insert("igloo", 1);
	insert("world", 2);
	CU_ASSERT(100 == similarity();}
	
/*int check(FILE *fl1, FILE *fl2){
	similar = 0;
	size = 0;
	getChar(fl1, fl2);
	if(f1next == 0 || f2next == 0){
		exit(1);}
	else{ 
		similarity();
		do{
			getChar(fl1, fl2);
			similarity();}while(f1next != EOF && f2next != EOF);}
	int percent = similar * 100 / size;
	return percent;}*/

//in command line first argument needs to be the solutions and second argument needs to be the student's assignment
void main(int argc, char *argv[]){
	FILE *f1, *f2;
	//Assuming everything is entered correctly in the command line
	f1 = fopen(argv[1], "r");
	f2 = fopen(argv[2], "r");
	if(f1 == NULL || f2 == NULL){
		printf("Invalid file. Try uploading again.\n");
		exit(1);}
	//else{
		//printf("Similarity: %d %%\n", check(f1, f2));}
	int i;
	for(i=0; i < SIZE; i++){
		numTable1[i] = 0;
		numTable2[i] = 0;}
	char array1[40][256];
	char array2[40][256];
	for(i = 0; i < 40; i++){
		fscanf(f1, " %s ", array1[i]);
		fscanf(f2, " %s ", array2[i]);}

	testHash();
	testLookup();
	testInsert();
	testSimilarity();
	
	/*insert(array1[0], ORIGINAL);
	insert(array1[1], ORIGINAL);
	insert(array1[2], ORIGINAL);
	insert(array1[3], ORIGINAL);
	insert(array1[4], ORIGINAL);
	insert(array1[5], ORIGINAL);*/
	/*insert(array1[7]);
	insert(array1[8]);
	insert(array1[9]);*/
	/*insert(array1[10]);
	insert(array1[11]);
	insert(array1[12]);
	insert(array1[13]);
	insert(array1[14]);
	insert(array1[15]);
	insert(array1[16]);
	insert(array1[17]);
	insert(array1[18]);
	insert(array1[19]);*/
	/*insert(array1[20]);
	insert(array1[21]);
	insert(array1[22]);
	insert(array1[23]);
	insert(array1[24]);
	insert(array1[25]);
	insert(array1[26]);
	insert(array1[27]);
	insert(array1[28]);
	insert(array1[29]);
	insert(array1[30]);
	insert(array1[31]);
	insert(array1[32]);
	insert(array1[33]);
	insert(array1[34]);
	insert(array1[35]);
	insert(array1[36]);
	insert(array1[37]);
	insert(array1[38]);	
	insert(array1[39]);*/
	/*insert(array2[0], FILETOCHECK);
	insert(array2[1], FILETOCHECK);
	insert(array2[2], FILETOCHECK);
	insert(array2[3], FILETOCHECK);*/
	fclose(f1);
	fclose(f2);
	display();
	similarity(*argv[1], *argv[2]);}