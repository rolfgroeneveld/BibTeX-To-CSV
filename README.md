BibTeX-To-CSV
=============

When you read a scientific article I watch out for the following elements: (1) Innovation: what does the study do what others haven't done before? (2) Method: what method did they use? (3) Data: where did they get their data from? (4) Results: what are the main results? and (5) Relevance: who benefits from this research, and how?.

Once you have done that for many articles you might want to make an overview table so that you get a better grasp of what is happening in the literature. If you keep your notes in a bibtex file then this script can make the table for you. It will read the bibtex file, select the references that meet particular criteria (author name, in this script), and within those references, select the fields you are interested in. It then exports the fields to a CSV file.

bibTex2CSV.py is the python script.
Example.bib is an example of a bibtex file that can be read with this script.
