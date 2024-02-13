# fdstruct

Command line tool that prettly prints your folder structure.

_Similar to [tree](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tree) but with much more options specially for Windows_

Usage after installation (see steps bellow):

    Usage: fdstruct <path> [-m <depth>] [-i <ignore_patterns>] [-a] [-o <output_file>]

- \<path> is the path of the folder to be mapped, or ". " for current folder.
- \<depth> specifies the maximum depth of folders the tool with go to.
- \<ignore_patterns> are folders, files or file extensions to ignore to ignore:
  - put "/" in front of folder names
  - to ignore file extensions use "_.\<file extension>", for example "_.md"
- Default behaviour is to ignore hidden folders (that starts with an "."), if you dont want that to happen, use the flag "-a".
- You can output the resulting structure to a text file by providing the flag "-o" followed by the name of the file.

## Installation

_You can run this script without properly installing it on your machine, although this will make it much more convenient. If you wish to not install it, see the last section._

#### **First, you will need to copy the fdstruct.py file in this repo and save it to your computer, and then follow this instructions depending on your operating system:**

### Windows

1.  #### Create a Batch Wrapper:

    - Create a new text file named fdstruct.bat and edit it to include the following line:

          @pythonw.exe C:\path\to\fdstruct.py %*

    - Replace "C:\path\to\fdstruct.py" with the full path to your fdstruct.py script.
    - Place fdstruct.bat in a directory that's included in your system's PATH environment variable.

2.  #### Add Python to PATH:

    - Ensure Python's installation directory is added to your system's PATH if it's not already. This step is typically done during Python installation by checking the option "Add Python to PATH."

### Linux and macOS

1.  #### Make the Script Executable:

    - Open a terminal.
    - Navigate to the directory containing fdstruct.py.
    - Make the script executable by running:
      chmod +x fdstruct.py

2.  #### Add a Shebang Line:

    - Edit the first line of fdstruct.py to include a shebang that specifies the path to the Python interpreter:

          #!/usr/bin/env python3

      This line should be the very first line in the file.

3.  #### Create a Symbolic Link (Optional):

    To run the script from any location without specifying its full path, create a symbolic link to fdstruct.py in a directory that's in your PATH, such as /usr/local/bin.

    Run the following command (you may need sudo for permissions):

        sudo ln -s /path/to/fdstruct.py /usr/local/bin/fdstruct

    Replace /path/to/fdstruct.py with the actual path to your script.

## Verifying Installation

After following these steps, open a new terminal or command prompt window and type fdstruct followed by your desired parameters to run the script. There's no need to prefix the command with "python".

For example, you can now simply type:

    fdstruct . -m 5

This command should execute your script with the specified parameters, displaying the folder structure.

If you are on Windows and for some reason it doesn't work, try changing the bat file to use "python.exe" instead of "pythonw.exe".

### Some clarifications:

For Windows, the batch file acts as a wrapper that calls Python to execute your script. Adjust the path to pythonw.exe if necessary, depending on where Python is installed on your system.

For Linux and macOS, making the script executable and adding the shebang line allows the system to recognize it as a standalone command. The optional symbolic link step makes the script globally accessible without having to specify its full path.

## Using it without installing

If you wish to not install it as guided above, you can still use this tool by explicitly running the python script.
However, anytime you wish to use it, you will have to provide python with the full path to the fdstruct.py file before actually providing the path that you wish to print and the optionall parameters, like this:

    python C:\path\to\fdstruct.py <path> [-m <depth>] [-i <ignore_patterns>] [-a] [-o <output_file>]

To make this easier, you can first navigate to the folder that the fdsctruct.py file is and you can provide only the path that you want to print, like this:

    python fdstruct.py C:\path\that\you\want\to\print [-m <depth>] [-i <ignore_patterns>] [-a] [-o <output_file>]

### Example

If you saved the fdstruct.py file into your Windows Desktop and your username is "Ritchie" than the path to the file is `C:\Users\Ritchie\Desktop\fdstruct`. Suppose you want to map and print out a folder called "TopSecret" present in your Documents folder, you want it to go only 3 levels deep "for security reasons" and also want to ignore the folder "/SuperTopSecret" and all the files ended with ".rmvb", then you use it like this:

    python C:\Users\Ritchie\Desktop\fdstruct C:\Users\Ritchie\Documents\TopSecret -m 3 -i /SuperTopSecret *.rmvb
