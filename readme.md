**Custom-image-inference-and-sorter**

This is an image sorter which uses a user supplied tflite model to sort images into their respective directories based on the inference by model.
It is completely based on user input with only one modification to the code required

A pretrained tflite model is already provided which can be used to detect if the picture is one of the following:
1) building
2) forest
3) glacier
4) mountain
5) sea
6) steeet

**dataset:** https://www.kaggle.com/datasets/puneet6060/intel-image-classification/data
the model provided is trained on the above dataset. It has a separate folder (seg_pred) with 7000+ pictures which can be used for inference

**How it works**
1) File picker window is opened and a .tflite model is then picked by the user as per their need
2) Then the user enters the number of classes (classes are different kinds of pictures for eg. mountains, sea, etc.)
3) The user then enters the names of all the classes which are then saved as a list
4) The user is then prompted to enter the names of the folders that will be created. The pictures are sorted in these respective folders and each folder corresponds to the class it was entered with it
5) The user then changes the names of input and output layers in the **code** by looking at the signature list output in the cells above. The names of input and output layers is different model to model.
5) The user then enters the file path to the directory with all the pictures

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
2) requirements.txt
3) Add images/videos to show it works

**Future ideas**
1) Giving an user interface
