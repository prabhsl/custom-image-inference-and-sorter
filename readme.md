**Custom-image-inference-and-sorter**
This is an image sorter which uses a user supplied tflite model to sort images into their respective directories based on the inference by model.
It is completely based on user input with no modifications to the code required

![alt text](image-1.png)
![alt text](image-2.png)

**How it works**
1) File picker window is opened and a .tflite model is then picked by the user as per their need
2) Then the user enters the number of classes (classes are different kinds of pictures for eg. mountains, sea, etc.)
3) The user the names of all the classes which are then saved as a list
4) The user is then prompted to enter the names of the folders that will be created. The pictures are sorted in these respective folders and each folder corresponds to the class it was entered with it
5) The user then enters the file path to the directory with all the pictures

**Libraries used**
1) TensorFlow
2) Glob
3) Shutil
4) Pyplot and seaborn for visualization
5) Tkinter
6) Numpy
7) os