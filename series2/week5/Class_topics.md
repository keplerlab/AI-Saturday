
### Topics to be discussed : 
1. Last session recap.
2. Build a trainer for following kaggle competitions 
    ### Build a invasive-species-monitoring using the steps mentioned above.
    https://www.kaggle.com/c/invasive-species-monitoring/
    
    ### Learn computer vision fundamentals with the famous MNIST data 
    https://www.kaggle.com/c/digit-recognizer
3. Building a recommender system.


How to download the kaggle data
1. Download the kaggle cli project on the paperspace machine ''' git clone https://github.com/Kaggle/kaggle-api '''
2. Follow the installations steps mentioned on the github project page.
3. Download the data using the following commands ''' kaggle competitions download -c -f '''

Steps for Making Image classifier 
- [ ] Convert data downloaded using Kaggle api in Image format compatible with FastAI
- [ ] Divide training data in training and validation split ( 70:30 ) or ( 80:20) 
- [ ] Load Data 
- [ ] Enable data augmentation, and precompute = True
- [ ] Use lr_find() to find the highest learning rate where loss is cleary improving
- [ ] Train last layer from precomputed activations for 1-2 epochs
- [ ] Train last layer with data augmentation for 2-3 epochs with cycle len = 1
- [ ] Unfreeze all layers
- [ ] Set earlier to 3x-10x lower learning rate than next higher learning rate
- [ ] use lr_find() again
- [ ] Train full network with cycle mult=2 until over fitting
- [ ] Run on test data using log_preds_test2 = learn.predict(is_test=True)
- [ ] Convert results in sample submission csv 
- [ ] Submit results in Kaggle 
