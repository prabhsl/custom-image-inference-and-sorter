**Custom-image-inference-and-sorter**

This is an image sorter which uses a user supplied tflite model to sort images into their respective directories based on the inference by model.
It is completely based on user input with only one modification to the code required which is changing the names of input and output layers from the result returned by **interpreter.get_signature_list()**

A pretrained tflite model is already provided which can be used to detect if the picture is one of the following:
1) building
2) forest
3) glacier
4) mountain
5) sea
6) steeet

**dataset:** https://www.kaggle.com/datasets/puneet6060/intel-image-classification/data
the model provided is trained on the above dataset. It has a separate folder (seg_pred) with 7000+ pictures which can be used for inference

**How it works (using the script version)**
1) File picker window is opened and a .tflite model is then picked by the user as per their need
2) The user then changes the names of input and output layers in the code. The names of input and output layers is different model to model. The script then needs to be run again if the names of input and output layers are different after they are updated.
3) Then the user enters the number of classes
4) The user then enters the names of all the classes
5) The user then selects the directory where the folders would be made based on the class names. The pictures are sorted in these respective folders
6) The user then selects the directory where the images for prediction are stored
7) A visualization is then provided based on the results of sorting which tells us how many pictures each class had

**Libraries used**
1) TensorFlow
2) Glob
3) Shutil
4) Pyplot and seaborn for visualization
5) Tkinter
6) Numpy
7) os

**To do**
1) ~~Error handling~~ done
2) ~~requirements.txt~~ done
3) Add images/videos to show it works

**Future ideas**
1) Giving an user interface
