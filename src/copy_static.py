import os
import shutil

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)


# def copy_static():
#     working_directory = os.getcwd()
#     public_directory = os.path.join(working_directory, "public")
#     static_directory = os.path.join(working_directory, "static")

#     if not os.path.exists(static_directory):
#         sys.exit(1)


#     if os.path.exists(public_directory):
#         shutil.rmtree(public_directory)

#     os.mkdir(public_directory)

#     copy_static_recursive(static_directory, public_directory)
    

# def copy_static_recursive(static_directory, dst):
#     for tree_element in os.listdir(static_directory):
#         src = os.path.join(static_directory, tree_element)
#         if os.path.isdir(src):
#             new_directory = os.path.join(dst, tree_element)
#             os.mkdir(new_directory)
#             copy_static_recursive(src, new_directory)
#             continue
#         if os.path.isfile(src):
#             shutil.copy(src, dst)
