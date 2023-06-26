# Dropbox-Api-integration
**This program integrates the Dropbox API to sorts a complete folder into varying folders based on its file type directly into your Dropbox.**
## Brief
This mission of the project is to design an application to work with the Dropbox Api.
The main inspiration of the application was designed to help gaming developers
automate how they save files to their Dropbox. With a few authentication prompts,
file destination designation and naming prompt all the work of sorting files based on
types are handled easily. 
### Key Program Functionality guides
The menu allows for 3 options: adding a new project folder, adding to an existing
project folder or creating a custom file type system:
- When adding a new project file, the user gets prompt with the new name of a
file to create and the folder path on the local computer to access. This follows a
default sorting type of music, audio related files i.e., “.mp3”, images, picture or
image related files i.e., “.jpg”, documents, text related files i.e., “.txt” and
miscellaneous for everything else.

- Adding to an existing project, checks if the folder exists and then adds all the
files specified by the user into its respective filetype folders.

- Creating a custom sorting system takes in multiple inputs. The amount of sub
folders and their names, the types of files to be stored in each sub folder. The
application creates all these sub folders and checks the user's files and places
them in the corresponding folder type.
### Info guides
There is still a lot that can be done. Dropbox authentication is the biggest issue as the token
is the only way to start and successfully run the program. There are a lot of input errors that
need to be checked and debugged (space in Dropbox sufficient or email validation or
corrupted files). 
### Resources
Main resource for learning about the Dropbox Api: https://dropbox-sdk-python.readthedocs.io/en/latest/index.html

Website to get ideas on what the Dropbox Api can be used for and some help on its methods: https://python.hotexamples.com/examples/dropbox/Dropbox/-/python-dropbox-classexamples.html

Dropbox Api community help forum: https://www.dropboxforum.com/t5/API-Support-Feedback/ct-p/101000041A
