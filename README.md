# PowerBuilder-decompile
Python module that parse power builder file (PBD) and analyze code (Incomplete)
this tool is composed of:
  * `pbd_dump.py <pbd file>` this tool extract files from pbd file and save it to folder named `<filename-pbd>`
  * `analyse_folder.py <folder name>` after extract pbd into folder you can use this tool to decompile supported files ("win", "fun", "udo")
  * `analyse.py <file-name>` this tool is used to decompile one file with extension ("win", "fun", "udo") by create a folder with name of the file and put inside it the code in hierarchical
  * all the above steps is done in one step using python file `pbd_analyse.py <file_name.pbd>`

please note:
* the work still incomplete
* I test against PB version 6
* the code result from decompilation is not related to any known programming language. I just make it as simple and descriptive as possible 
* I will be happy if someone want to share or modify the code
