# Getting Started
This lesson will help set you up for future lessons. 
___
## 1 Create a GitHub account
GitHub is used by all software developers as a place to store their code and collaborate on it with others. For now, you'll just use it to download the code for the lessons.  
https://github.com/signup
___
## 2 Install Chocolatey
Chocolatey is a popular package manager for Windows. It makes it easy to install lots of programs from the command line, instead of having to manually install them all from different websites, use their installers, etc.    
https://chocolatey.org/install  
Here you can search for packages and see how many installs they have:  
https://community.chocolatey.org/packages  
Package managers are one of the main appeals of using something like Linux. On Linux, you can install almost any program with a single command, and it will automatically install all of the dependencies for you. Chocolatey is one of the best options for that on Windows.  
___

## 3 Install VSCode, Python, and Git
Open a Windows terminal as administrator and run the following command:
```powershell
choco install vscode python git
```
VSCode is a popular code editor, Python is the programming language we'll be using, and Git are programs that we'll use to interact with GitHub. 
___

## 4 Clone the lesson repository
Right click your desktop and make a new folder called "code", then open a Windows terminal in that folder and run the following commands:
```powershell
# gh repo fork exformation/tutoring --clone --public
git clone https://github.com/exformation/tutoring.git
cd tutoring
code .
```
___

## 5 Install the Python extension for VSCode
In VSCode, press ctrl+shift+x, then search for "Python" and install the extension by Microsoft (1st result).  
Extensions like these will give you lots of useful features, like code completion, syntax highlighting, debugging, and more. We can go over other useful extensions later, like Copilot, which gives you AI autocomplete. 
___

## 6 Run lesson00/main.py
Open the file lesson00/main.py in VSCode and press F5. You should see the output "Hello, world!" in the terminal. If you see this, you're all set up and ready to go for the next lesson. 
___