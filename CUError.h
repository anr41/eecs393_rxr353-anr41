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
00022  *  Contains CUnit error codes which can be used externally.
00023  *
00024  *  Created By     : Anil Kumar on ...(in month of Aug 2001)
00025  *  Last Modified  : 09/Aug/2001
00026  *  Comment        : -------
00027  *  EMail          : aksaharan@yahoo.com
00028  *
00029  *  Modified       : 02/Oct/2001
00030  *  Comment        : Added proper Eror Codes
00031  *  EMail          : aksaharan@yahoo.com
00032  *
00033  *  Modified       : 13-Oct-2001
00034  *  Comment        : Added Error Codes for Duplicate TestGroup and Test
00035  *  EMail          : aksaharan@yahoo.com
00036  *
00037  *  Modified       : 3-Aug-2004 (JDS)
00038  *  Comment        : Converted error code macros to an enum, doxygen comments
00039  *                   moved error handing code here, changed file name from Errno.h,
00040  *                   added error codes for file open errors, added error action selection
00041  *  EMail          : jds2@users.sourceforge.net
00042  *
00043  *  Modified       : 5-Sep-2004 (JDS)
00044  *  Comment        : Added internal test interface.
00045  *  EMail          : jds2@users.sourceforge.net
00046  */

 #ifndef _CUNIT_CUERROR_H
 #define _CUNIT_CUERROR_H
 #include <errno.h>

 /*------------------------------------------------------------------------*/
 typedef enum {
  /* basic errors */
   CUE_SUCCESS           = 0,  
   CUE_NOMEMORY          = 1,  
   /* Test Registry Level Errors */
  CUE_NOREGISTRY        = 10,  
  CUE_REGISTRY_EXISTS   = 11,  
   /* Test Suite Level Errors */
   CUE_NOSUITE           = 20,  
  CUE_NO_SUITENAME      = 21,  
  CUE_SINIT_FAILED      = 22,  
   CUE_SCLEAN_FAILED     = 23,  
  CUE_DUP_SUITE         = 24,  
   /* Test Case Level Errors */
  CUE_NOTEST            = 30,  
  CUE_NO_TESTNAME       = 31,  
  CUE_DUP_TEST          = 32,  
   CUE_TEST_NOT_IN_SUITE = 33,  
   /* File handling errors */
   CUE_FOPEN_FAILED      = 40,  
  CUE_FCLOSE_FAILED     = 41,  
  CUE_BAD_FILENAME      = 42,  
  CUE_WRITE_ERROR       = 43   
 } CU_ErrorCode;

 /*------------------------------------------------------------------------*/
typedef enum CU_ErrorAction {
  CUEA_IGNORE,    
   CUEA_FAIL,      
   CUEA_ABORT      
 } CU_ErrorAction;
/* Error handling & reporting functions. */
 #ifdef __cplusplus
extern "C" {
 #endif

 CU_ErrorCode   CU_get_error(void);
 const char*    CU_get_error_msg(void);
 void           CU_set_error_action(CU_ErrorAction action);
 CU_ErrorAction CU_get_error_action(void);
 #ifdef CUNIT_BUILD_TESTS
 void test_cunit_CUError(void);
 #endif
/* Internal function - users should not generally call this function */
 void  CU_set_error(CU_ErrorCode error);
 #ifdef __cplusplus
 }
 #endif
 #ifdef USE_DEPRECATED_CUNIT_NAMES
 #define get_error() CU_get_error_msg()
 #endif  /* USE_DEPRECATED_CUNIT_NAMES */
 #endif  /*  _CUNIT_CUERROR_H  */
