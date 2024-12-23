/* pomdp_err.c

  *****
  Copyright 1994-1997, Brown University
  Copyright 1998, 1999, Anthony R. Cassandra

                           All Rights Reserved
                           
  Permission to use, copy, modify, and distribute this software and its
  documentation for any purpose other than its incorporation into a
  commercial product is hereby granted without fee, provided that the
  above copyright notice appear in all copies and that both that
  copyright notice and this permission notice appear in supporting
  documentation.
  
  ANTHONY CASSANDRA DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
  INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR ANY
  PARTICULAR PURPOSE.  IN NO EVENT SHALL ANTHONY CASSANDRA BE LIABLE FOR
  ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
  WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
  ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
  OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
  *****

	This module contains the functions necessary for the creation,
maintainence and output of the data structure that holds the error
information generated by the scanner/parser.  

*/

#include	<stdio.h>
#include	<stdlib.h>
#include        <string.h>
#include	"parse_err.h"	/* constant and type defs. */

/***********************  GLOBAL VARIABLES ***************************/
/* GLOBAL Array of error messages */
static char *Err_Strings[NBR_ERRORS] = {
	ERROR_MSSG_0,
	ERROR_MSSG_1,
	ERROR_MSSG_2,
	ERROR_MSSG_3,
	ERROR_MSSG_4,
	ERROR_MSSG_5,
	ERROR_MSSG_6,
        ERROR_MSSG_7, 
        ERROR_MSSG_8, 
        ERROR_MSSG_9, 
        ERROR_MSSG_10, 
        ERROR_MSSG_11, 
        ERROR_MSSG_12, 
        ERROR_MSSG_13, 
        ERROR_MSSG_14, 
        ERROR_MSSG_15, 
        ERROR_MSSG_16, 
        ERROR_MSSG_17, 
	ERROR_MSSG_18,
	ERROR_MSSG_19,
	ERROR_MSSG_20,
	ERROR_MSSG_21,
	ERROR_MSSG_22,
	ERROR_MSSG_23,
	ERROR_MSSG_24,
	ERROR_MSSG_25,
	ERROR_MSSG_26,
	ERROR_MSSG_27,
	ERROR_MSSG_28
	};

/* pointer to the linked list of errors */
Err_node	*Err_list;		/* GLOBAL error list */


/**********************  ERR_initialize  ******************************/
void ERR_initialize()
/*
	Initializes the linked list of errors by creating the first
node in that list as empty.  The list will actually start with the
second node of the list.  The 'unused first node' scheme is used so that
functions that might alter the front of the list need not return
a pointer to the list (as would be required, since the front of the
list might change).
*/
{
	/* Initialize the error list */
	Err_list = (Err_node *) malloc(sizeof(Err_node));
	checkAllocatedPointer((void *) Err_list );

	Err_list->nextError = NULL;
        Err_list->source = NULL;
        Err_list->modString = NULL;

}  /* ERR_initialize */
/**********************  ERR_enter  ***********************************/
void ERR_enter(source, lineno, errorid, modificationString)
/*
	The routine will create a new node for the linked list of errors and fill
it with the proper data.  It will then insert this node into the existing linked
list of errors in line number order.  If there already exists one or more errors
for that line number the new node will be placed at the end of all of those so 
that for a line, first generated is the first displayed.  Error messages with no
associated line number will always precede all the other messages with a line
number and, similiarly, on a first generated-first displayed basis.

	Parameter Descriptions:

 	   "source" is a pointer to a string that will indicate the
		part of the compiler generating the message as well
		as the function (routine) that is giving the message.
		This will onl be displayed to output during the
		debugging of the compiler.

	   "lineno" is the line number that the error occured on.  If a line
		number is inappropriate, pass the constant NO_LINE.

	   "errorid" is the type of error that occured.  If this number is
		larger than the maximum id, an error message will be output
		and no error will be recorded.

	   "modificationString" is a pointer to a string of characters that will
		be used to replace the character ERR_META when the error
		message is printed out. (if ERR_META is in error message)

*/
	char 	*source;
	int	lineno,errorid;
	char	*modificationString;
{
	Err_node	*newNode;	/* node for new error */

	Err_node	*tempPtr,      /* for insertion in sorted list */
			*trailPtr;

	/* Is the error number valid? */
	if (errorid >= NBR_ERRORS)
	    {
		printf(OUT_OF_RANGE_MSSG, errorid);
		return;
	    }

	/* Create a new error node */
	newNode = (Err_node *) malloc(sizeof(Err_node));
	checkAllocatedPointer((void *) newNode );

	/* Put the information in */
	newNode->lineNumber = lineno;
	newNode->errorNumber = errorid;
        if( modificationString != NULL ) {
           newNode->modString = (char *) calloc(strlen(modificationString)+1,
                                                sizeof(char));
           strcpy(newNode->modString, modificationString);
        }
        else
           newNode->modString = NULL;


        if( source != NULL ) {
           newNode->source = (char *) calloc(strlen(source)+1, sizeof(char));
           strcpy(newNode->source, source);
        }
        else
           newNode->source = NULL;

	newNode->nextError = NULL;

	/* Insert it in the linked list in sorted order (by line number) */
	trailPtr = Err_list;
	tempPtr = Err_list->nextError;

	while(tempPtr != NULL)
	{
	  if (tempPtr->lineNumber <= newNode->lineNumber)
	  {
	    trailPtr = tempPtr;
	    tempPtr = tempPtr->nextError;
	  }  /* end if */
	
	  else  /* list line number > new line number */
		break;  /* this is the place to insert */

	}  /* end of while loop */
	/* node will be inserted after "trailPtr" and before "tempPtr" */

	newNode->nextError = tempPtr;
	trailPtr->nextError = newNode;

}  /* ERR_enter */
/*****************************  ERR_dump  ***********************************/
int ERR_dump()
/*
	   This function prints out the error messages found in the list
	Err_list.  Each error
	is printed on a separate line.  If the error string has the
	character ERR_META in it, the string that was passed to ERR_enter
	when the node was created will be passed instead. ("modString")
	   If there were no errors in the list, the message "No Errors found."
	will be printed.
	  The "source" string of where the error occurred is only printed out
	when the Global constant DEBUG is not zero.
*/
{
	char		*currChar;	/* used for outputting string */
	Err_node	*currErr;	/* used for traversing node list */
	int numErrors = 0;
	int numWarnings = 0;

	if (Err_list->nextError == NULL)
	/* then there are no errors in the list */
	{
	   /*  printf(NO_ERRORS); */
	   return 0;
	}  /* end if no errors in list */


	/* Write out error list */
	currErr = Err_list->nextError;

	while (currErr != NULL) {
           if ((DEBUG) && (currErr->source != NULL))
              /* then printout where error was generated */
              printf("(%s) ", currErr->source);

           /* check whether it is a warning or an error */
           switch(currErr->errorNumber) {  
              /* WARINGS */
           case -1:  /* Currently no warnings are defined */
              numWarnings++;
              if (currErr->lineNumber == NO_LINE)
                 /* then the warning didn't have a line number associated
                    with it */
                 printf(NO_LINE_WARNING);

               else  /* there was a line number */
                 printf(LINE_WARNING, currErr->lineNumber);
              break;

		  /* ERRORS */
           default:
              numErrors++;

              if (currErr->lineNumber == NO_LINE)
                 /* then the error didn't have a line number associated
                    with it
                    */
                 printf(NO_LINE_ERROR);

              else  /* there was a line number */
                 printf(LINE_ERROR, currErr->lineNumber);
		         break;
           }  /* end of switch */

           /* Dump the string */
           currChar = Err_Strings[currErr->errorNumber];

           while (*currChar != '\0')  {
              /* Meta-symbol? */
              if ((*currChar == ERR_META) && (currErr->modString != NULL ))
                 printf("%s",currErr->modString);	/* dump str */
              else	/* just write character */
                 printf("%c",*currChar);

              /* Next character */
              currChar = currChar + 1;
           }

           printf("\n");	/* next line */

           /* Next error node */
           currErr = currErr->nextError;
        }

	printf("%d errors and %d warnings found.\n", numErrors, numWarnings);
	return 1;

}  /* ERR_dump */
/***************************************************************************/
void ERR_cleanUp() {
   Err_node *temp;

   while( Err_list != NULL ) {
      temp = Err_list;
      Err_list = Err_list->nextError;
      if( temp->source != NULL )
         free( temp->source );
      if( temp->modString != NULL )
         free( temp->modString );
      free( temp );
   }  /* while */

}
/***************************************************************************/
