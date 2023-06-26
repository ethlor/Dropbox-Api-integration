import dropbox
import os
import sys
from dropbox.exceptions import ApiError, AuthError
from dropbox.files import WriteMode,FileCategory,WriteError, GetMetadataArg
from dropbox.file_properties import LookupError



TOKEN = ''
#"C:\Users\Admin\OneDrive\Documents\practicdob"
#"C:\Users\Admin\OneDrive\Documents\tesetes"
def add_local_files(project,custom={},default=True):
    local_path = input("enter file path: ").strip()
    common_tag = input("Would you like to add a common tag to all the files?(y/n)")
    common_tag_lst=[]
    if common_tag =='y':
        while True:
            common_tag_lst.append(input("Enter tag:"))
            s = input("Enter another tag?(y/n)")
            if s =='n':
                break
            elif len(common_tag_lst)==19:
                break
    if os.path.exists(local_path):
        print("file exists beggining upload")
        
        if os.path.isfile(local_path):
            with open(local_path,"rb") as f:
                data = f.read()
                if default:
                    sort_files(data,f,project,common_tag_lst)
                else:
                    sort_file_custom(data,f,project,common_tag_lst,custom)
        else:
            for root,dname,fname in os.walk(local_path):
                for name in fname:
                    fullname = os.path.join(root,name)
                    # check file size and if enough space
                    # upload file but first check type
                    with open(fullname,"rb") as f:
                        data = f.read()
                        if default:
                            sort_files(data,name,project,common_tag_lst)   
                        else:
                            sort_file_custom(data,name,project,common_tag_lst,custom)                
    else:
        print("File not found.")
        # or raise an error and catch it 

#sort directory into default style
def sort_files(data,file,project,common_tag=[]):
    # sorts a file and uploadzs it to its field  
    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        #upload to image folder
        new = project + "/images/" +file
        specific_tag="Image"
    elif file.lower().endswith(('.mp3', '.wav', '.mid')):
        # upload to audio folder
        # add audio tag
        new = project + "/audio/" +file
        specific_tag="Audio"
    elif file.lower().endswith(('.doc', '.docx', '.txt')):
        # upload to txt folder
        new = project + "/document/" +file
        specific_tag="document"
    else:
        # add to miscelanios
        new = project + "/misselanious/" +file
        specific_tag="misselanious"

    new.replace("//","/")
    dbx.files_upload(data,new,mode=WriteMode('overwrite'))
    dbx.files_tags_add(new,specific_tag)
    for tags in common_tag:
        dbx.files_tags_add(new,tags)

# sort directory into custom folder style
def sort_file_custom(data,file,project,common_tag,custom_folder):
    new = project+"/miscilaneous/"+file
    for k,v in custom_folder.items():
        if file.lower().endswith(v):
            new = project+"/"+k+"/"+file
            break
    
    dbx.files_upload(data,new,mode=WriteMode('overwrite'))
    for tags in common_tag:
        dbx.files_tags_add(new,tags)


# create a main project folder
def folder_create(first=False,custom=False):
    project = input("Enter name of project: ")
    project_path = "/"+project
    
    # asks user for custom file info
    custom_type = {}
    if custom: 
        while True:
            num_custom=input("Enter amount of custom folders:")
            if not num_custom.isnumeric():
                print("sorry incorrect input.")
                break
            elif int(num_custom)==0:
                print("cannot enter 0")
                break
            else:
                num_custom = int(num_custom)
                break
        for i in range(num_custom):
            n = input(f"name of folder {i+1}: ")
            tagnum = int(input("How much types for folder?: "))
            for j in range(tagnum):
                type_folder = input("enter folder type,ie .py, .jpg etc: ")
                if n in custom_type:
                    # joins tuples
                    custom_type[n]= custom_type[n]+(type_folder,) 
                else:
                    # creates a tuple in the dictionary 
                    custom_type[n]=(type_folder,) 
        print(custom_type)
            
    #GetMetadataArg(path=project_path) 
    try:
        dbx.files_get_metadata(project_path) # checks if project folder exists
        
    except:
        if first:
            dbx.files_create_folder_v2(project_path,autorename=True)
            if custom:
                add_local_files(project_path,custom_type,default=False)
            else:
                add_local_files(project_path)
            return True
        else:
            print("file doesnt exist.")
            return False
    if first:
        print("File name alrady exists auto creating new.")
        dbx.files_create_folder_v2(project_path,autorename=True)

        if custom:
            add_local_files(project_path,custom_type,default=False)
        else:
            add_local_files(project_path)
        return True
        
    else:
        add_local_files(project_path)
        return True
        

if __name__ == '__main__' :
    # must enter Token
    with dropbox.Dropbox(TOKEN) as dbx:

        # Check that the access token is valid
        try:
            account = dbx.users_get_current_account()
        except AuthError:
            sys.exit("ERROR: Invalid access token; try re-generating an "
                "access token from the app console on the web.")
        
        while True:
            menu = input("\nWelcome "+account.name.given_name+". Please select an option\n a - Add a project \n b - Add to existing project\n c - Create custom folder type\n e -exit\n:")
            if menu == 'a':
                # add new project
                if folder_create(first=True):
                    print("New project added and files sorted.")
  
            elif menu == "b":
                # have them  enter a project file name and check if it exists then add and sort to it
                if folder_create():
                    print("files sorted")
            
            elif menu == 'c':
                folder_create(first=True,custom=True)
  
            elif menu =="e":
                sys.exit("Good Bye.")
            else:
                print("incorrect input please try again")
         
