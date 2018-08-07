# Princeton Document Registry

This registry serves as a means to 

* Track existing Princeton documents 
* Determine document codes for new documents

The registry consists of two files:

1. `author.csv`: lists allocated author codes and author names.
2. `documents.csv`: lists registered documents: the document code, the title, a link to the document, the date of submission and additional comments.

## Notes

1. This may be a temporary solution - better solutions such as a web service to allow users to view/register new documents may be more appropriate.
2. The tables are not completely normalised for readability purposes. For example, the author appears in both `author.csv` and `documents.csv`. This may be changed should these files be used by a web service for example.
3. The first line of both CSV files contains a "#' to provide a convenient means of parsing out the first line
4. Quotes are used for all fields, to allow whitespaces in field values.


