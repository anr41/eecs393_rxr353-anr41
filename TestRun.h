/*
00002  *  CUnit - A Unit testing framework library for C.
00003  *  Copyright (C) 2001  Anil Kumar
00004  *  Copyright (C) 2004  Anil Kumar, Jerry St.Clair
00005  *
00006  *  This library is free software; you can redistribute it and/or
00007  *  modify it under the terms of the GNU Library General Public
00008  *  License as published by the Free Software Foundation; either
00009  *  version 2 of the License, or (at your option) any later version.
00010  *
00011  *  This library is distributed in the hope that it will be useful,
00012  *  but WITHOUT ANY WARRANTY; without even the implied warranty of
00013  *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
00014  *  Library General Public License for more details.
00015  *
00016  *  You should have received a copy of the GNU Library General Public
00017  *  License along with this library; if not, write to the Free Software
00018  *  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
00019  */
 
 /*
00022  *  Contains Interface to Run tests.
00023  *
00024  *  Created By     : Anil Kumar on ...(in month of Aug 2001)
00025  *  Last Modified  : 09/Aug/2001
00026  *  Comment        : Contains generic run tests interface which can be used
00027  *                   be used for any type of frontend interface framework.
00028  *  EMail          : aksaharan@yahoo.com
00029  *
00030  *  Last Modified  : 24/Nov/2001
00031  *  Comment        : Added Handler for Group Initialization failure condition.
00032  *  EMail          : aksaharan@yahoo.com
00033  *
00034  *  Last Modified  : 5-Aug-2004 (JDS)
00035  *  Comment        : New interface.  Since these should be internal functions,
00036  *                   no support for deprecated version 1 names provided now,
00037  *                   eliminated global variables for current test & suite,
00038  *                   moved (renamed) _TestResult here from TestDB.h.
00039  *  EMail          : jds2@users.sourceforge.net
00040  *
00041  *  Modified       : 5-Sep-2004 (JDS)
00042  *  Comment        : Added internal test interface.
00043  *  EMail          : jds2@users.sourceforge.net
00044  */
 #ifndef _CUNIT_TESTRUN_H
 #define _CUNIT_TESTRUN_H
 #include "CUnit.h"
 #include "CUError.h"
 #include "TestDB.h"
 #ifdef __cplusplus
extern "C" {
 #endif
 /* CU_FailureRecord type definition. */
 typedef struct CU_FailureRecord
{
   unsigned int  uiLineNumber;     
   char*         strFileName;      
  char*         strCondition;     
   CU_pTest      pTest;            
   CU_pSuite     pSuite;           
  struct CU_FailureRecord* pNext; 
   struct CU_FailureRecord* pPrev; 
 } CU_FailureRecord;
 typedef CU_FailureRecord* CU_pFailureRecord;  
 /* CU_RunSummary type definition. */
typedef struct CU_RunSummary
 {
  unsigned int nSuitesRun;        
   unsigned int nSuitesFailed;     
   unsigned int nTestsRun;         
  unsigned int nTestsFailed;      
   unsigned int nAsserts;          
   unsigned int nAssertsFailed;    
   unsigned int nFailureRecords;   
 } CU_RunSummary;
 typedef CU_RunSummary* CU_pRunSummary;  
 /* Type Definitions for Message Handlers. */
 typedef void (*CU_TestStartMessageHandler)(const CU_pTest pTest, const CU_pSuite pSuite);
 typedef void (*CU_TestCompleteMessageHandler)(const CU_pTest pTest, const CU_pSuite pSuite,const CU_pFailureRecord pFailure);
 typedef void (*CU_AllTestsCompleteMessageHandler)(const CU_pFailureRecord pFailure);
 typedef void (*CU_SuiteInitFailureMessageHandler)(const CU_pSuite pSuite);
 /* Get/Set functions for Message Handlers. */
void CU_set_test_start_handler(CU_TestStartMessageHandler pTestStartMessage);
 void CU_set_test_complete_handler(CU_TestCompleteMessageHandler pTestCompleteMessage);
 void CU_set_all_test_complete_handler(CU_AllTestsCompleteMessageHandler pAllTestsCompleteMessage);
 void CU_set_suite_init_failure_handler(CU_SuiteInitFailureMessageHandler pSuiteInitFailureMessage);
 CU_TestStartMessageHandler        CU_get_test_start_handler(void);
 CU_TestCompleteMessageHandler     CU_get_test_complete_handler(void);
 CU_AllTestsCompleteMessageHandler CU_get_all_test_complete_handler(void);
 CU_SuiteInitFailureMessageHandler CU_get_suite_init_failure_handler(void);
 
 /* Functions for running registered tests and suites. */
CU_ErrorCode CU_run_all_tests(void);
 CU_ErrorCode CU_run_suite(CU_pSuite pSuite);
 CU_ErrorCode CU_run_test(CU_pSuite pSuite, CU_pTest pTest);
 /* Functions for getting information about the previous test run. */
 unsigned int CU_get_number_of_suites_run(void);
 unsigned int CU_get_number_of_suites_failed(void);
 unsigned int CU_get_number_of_tests_run(void);
unsigned int CU_get_number_of_tests_failed(void);
 unsigned int CU_get_number_of_asserts(void);
 unsigned int CU_get_number_of_successes(void);
 unsigned int CU_get_number_of_failures(void);
 unsigned int CU_get_number_of_failure_records(void);
 CU_pFailureRecord CU_get_failure_list(void);
 CU_pRunSummary CU_get_run_summary(void);
 /* Functions for internal & testing use. */
 CU_pSuite CU_get_current_suite(void);
 CU_pTest  CU_get_current_test(void);
 BOOL      CU_is_test_running(void);
 void      CU_clear_previous_results(void);
 /* Assertion implementation function. */
 BOOL CU_assertImplementation(BOOL bValue,
                              unsigned int uiLine,
                            char strCondition[],
                             char strFile[],
                             char strFunction[],
                              BOOL bFatal);
 #ifdef USE_DEPRECATED_CUNIT_NAMES
 typedef CU_FailureRecord  _TestResult;  
 typedef CU_pFailureRecord PTestResult;  
 #endif  /* USE_DEPRECATED_CUNIT_NAMES */
 #ifdef CUNIT_BUILD_TESTS
 void test_cunit_TestRun(void);
 #endif
#ifdef __cplusplus
 }
 #endif
 #endif  /*  _CUNIT_TESTRUN_H  */