   1. Watch the video on fast ai Lesson 1: https://www.youtube.com/watch?v=IPBSB1HLNLo&feature=youtu.be

   2. Execute the Week1_Exercise_Notebook.ipynb notebook steps for Dog-Cat classification so that you get insight of the code.

   3. Once through with Point-2, you can try with different dataset. 
   Example: Lion Vs Tiger, Indian rupee Vs U.S Dollar etc.
   Share your accuracy results on slack.
   You can refer to the Point(4) for the steps.

  4. Steps to Train a world-class image classifier
      1. Download the data from google api(https://github.com/hardikvasa/google-images-download).
      2. Download minimum 100 images for each class.
      3. Prepare the data in separate folders.[train and valid] 
      4. Choose your model.
      5. Train the model using architecture, dataset with precompute = True
      6. Use lr_find() to find the highest learning rate where loss is clearly improving
      7. Train last layer from precomputed activations for 1-2 epochs using learn.fit.
      8. Try improving the accuracy by tuning the hyper-parameters such as Learning Rate, No of Epochs etc.
  

