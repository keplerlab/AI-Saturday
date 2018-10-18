1) Watch the video on fast ai Lesson 1: https://www.youtube.com/watch?v=IPBSB1HLNLo&feature=youtu.be

2) Read the notes.

3) Execute the lesson1.ipynb notebook steps for Dog-Cat classification so that you get insight of the code.

4) Once through with Point-2, you can try with different dataset. 
Example: Lion Vs Tiger, Indian rupee Vs U.S Dollar etc.
You can refer to Point(5).

5) Steps to Train a world-class image classifier
a) Download the data using google api(https://github.com/hardikvasa/google-images-download).
b) Prepare the data in separate folders.[train and valid] 
c) Choose your model.
d) Train the model using architecture, dataset with precompute = True
e) Use lr_find() to find the highest learning rate where loss is clearly improving
f) Train last layer from precomputed activations for 1-2 epochs using learn.fit.
g) Try improving the accuracy by tuning the hyper-parameters such as Learning Rate, No of Epochs etc.


