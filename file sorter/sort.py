import os
import shutil

source = "C:/Users/lenovo/OneDrive/Desktop/New folder"


arrange = {
    "Images" : ".jpg",
    "Documents" : ".pdf"
}

if os.path.exists(source) is True:
    content = os.listdir(source)

    for files in content:
        file_ext = os.path.splitext(files)[1] 

        for folder_name, extension in arrange.items():
            if file_ext == extension:
                full_file_path = os.path.join(source, files)
                target_drt = os.path.join(source, folder_name)

                if not os.path.exists(target_drt):
                    os.makedirs(target_drt)

                shutil.move(full_file_path, target_drt)
                print(f"moved {files} to {folder_name}")

else:
    print("Directory path does not exist")