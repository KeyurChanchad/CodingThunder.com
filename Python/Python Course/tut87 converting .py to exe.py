"""
Steps to Create an Executable from Python Script using Pyinstaller
Step 1: Install the Pyinstaller Package
The first step is to install the module pyinstaller. For this, we will create or destinate a folder and open our power shell window there using shift + mouse right-click.

Now we will run the following command for our module installation.

pip install pyinstaller

Step 2: Save your Python Script
Right-click on the screen and then new and text document to create a .txt file and write the python script. We can save our python script in a text file, too, for the conversion, it does not necessarily have to be a .py file, but the code in it should be of Python. Now open the power shell window and write the following commands.
python .\main.txt   or .\main.py

Step 3: Create the Executable using Pyinstaller
As we want a .exe file. So we are going to run the following command.
pyinstaller main.txt  or .\main.py

Step 4: Run the Executable
After running pyinstaller main.txt command, it will create some folders. Click on the dist folder and then click on the main.

In that folder, we can find our .exe file. We can open it through the PowerShell window by running the command
.\main.exe

Now, as you saw that by converting the file to .exe, we got several files in the folder, but we can also run a command that will provide us with only one file as a resultant. It will take more time in creation and later on it will extract too, but for compatibility, we can use the following command:

pyinstaller --onefile file.py
"""

