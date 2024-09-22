Homework description
Task 1:
Write a Python program that recursively copies files in the original directory, moves them to a new directory, and sorts them into subdirectories based on file extensions.
Also, note the following conditions:
Parsing arguments. The script must accept two command line arguments: the path to the source directory and the path to the destination directory (by default, if the destination folder is not passed, it should be named dist).
Recursive reading of directories:A function must be written that takes the path to the directory as an argument. The function must iterate over all the items in the directory. If the item is a directory, the function must call itself recursively for that directory. If the item is a file, it must be available for copying.
Copying files:For each type of file, a new path must be created in the source directory using the file extension to name the subdirectory. The file of the corresponding type should be copied to the corresponding subdirectory.
Exception handling. The code must correctly handle exceptions, such as file or directory access errors.

Task 2:
Write a Python program that uses recursion to create a Koch snowflake fractal, provided that the user must be able to specify the level of recursion.
