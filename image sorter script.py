import numpy as np
import glob
import shutil
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter.filedialog import askopenfilename, askdirectory
import os.path
import tensorflow as tf
from PIL import UnidentifiedImageError

try:
    TF_MODEL_FILE_PATH = askopenfilename(filetypes= [("tflite files","*.tflite")])
    interpreter = tf.lite.Interpreter(TF_MODEL_FILE_PATH)

    #getting input and output layers
    print(interpreter.get_signature_list())
    
    # making a classifier for inference using the trained model  
    classifier = interpreter.get_signature_runner()

except (ValueError, NameError):
    print("Only .tflite files are supported. Please pick the correct file type.")


# file path function
def file_path():
    while(True):
        try:
            class_num = int(input("Please enter the number of classes: "))
        except ValueError:
            print("please enter an integer")
        else:
            break

    class_names = list(input(f"Please enter the name of all {class_num} classes separated by space: ").split(" "))
    print("Please select the directory where the folder for each class would be made")

    path_list = []
    # if no directory is selected the folders are made in the user directory
    path = askdirectory()
    
    for directories in range(class_num):
        # joining path returned from askdirectory() and joining the class names at the end
        folder_path = os.path.join(path, class_names[directories])
        os.makedirs(folder_path, exist_ok= True)
        path_list.append(folder_path)
        print(folder_path)
    return class_names, class_num, path_list


# sorter function
def sorter(class_names, class_num, path_list):
    for index in range(class_num):
        # when the class from inference matches the class name then a copy of the image is made in the folder associated with that class
        if class_names[np.argmax(score)] == class_names[index]:
            shutil.copy(image_path[img_index], path_list[np.argmax(score)])


# counter function
def counter(class_names, class_num, path_list):
    counter_dict = {}
    for count in range(class_num):
        # keys are class names and values are the number of files in the respective class folder
        print(f"{class_names[count]}: {len(os.listdir(path_list[count]))}")
        counter_dict.update({class_names[count] : len(os.listdir(path_list[count]))})
    return counter_dict
    

class_names, class_num, path_list = file_path()

print("Please select the directory where the images for inference are stored")
path = askdirectory()

# glob over all the files in the directory
image_path = glob.glob(os.path.join(path, "*"))



for img_index in range(len(image_path)):
    try:
        #loading the image that's being predicted
        pred_image = tf.keras.utils.load_img(image_path[img_index], target_size= (150, 150))

    except UnidentifiedImageError:
        print("Unidentified image file detected. Please run the script again after verifying the contents of the selected path")

    # converting image to float32 so the model can accept the image
    pred_image = np.float32(pred_image)

    # creating a batch
    image_array = tf.expand_dims(pred_image, 0)

    # change the input and output layers from signature list before running this cell
    predictions = classifier(rescaling_input= image_array)["dense_1"]

    # scaling the logits returned by prediction into probabilities
    score = tf.nn.softmax(predictions)

    print(f"the image belongs to {class_names[np.argmax(score)]} with the confidence of {np.max(score)}")

    sorter(class_names, class_num, path_list)


x = counter(class_names, class_num , path_list)

# converting the values of counter_dict into a list for visualization
x = list(x.values())

color_pallete = sns.color_palette("crest")

# autopct is used to display percent values in a string format in the piechart
plt.pie(x, labels= class_names, autopct= '%.2f%%', colors= color_pallete)
plt.show()