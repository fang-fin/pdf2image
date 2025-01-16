import sys
import os
from pdf2image import convert_from_path



def make_dir_for_results(pdf_path):
    #make new directory for results
    result_dir_name = os.path.basename(pdf_path)+"_result"
    os.mkdir(result_dir_name)
    print(result_dir_name)
    
    #change current working directory
    current_working_dir = os.getcwd()
    new_working_dir = os.path.join(current_working_dir,result_dir_name)
    os.chdir(new_working_dir)
    print(new_working_dir)
    

def convert_to_images(pdf_path):
    #Load images from pdf
    images = convert_from_path(pdf_path,thread_count=8)
    
    #go through the file 
    for i in range(len(images)):
        image = images[i].save("page"+str(i+1)+".jpg","JPEG") 

def go_back_to_last_cwd():
    
    #get current working file
    current_working_dir = os.getcwd()
    new_working_dir = os.path.split(current_working_dir)[0]
    print(new_working_dir)
    #go back to last working directory
    os.chdir(new_working_dir)
     

    
 
 
if __name__ =="__main__":
    if len(sys.argv) <2 :
        print("Usage:python convert_pdf_to_img.py <file1.pdf> <file2.pdf> <file3.pdf>")
    
    for pdf_path in sys.argv[1:]:
        make_dir_for_results(pdf_path)
        convert_to_images(pdf_path)
        go_back_to_last_cwd()
        
       