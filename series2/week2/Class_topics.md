## Topics to be discussed

1. Week 1 review
2. Week 1 exercise solution.
3. The 3 steps of training.
    1. Preparing the data for training.
        1. Why do we need to prepare the data for training?
        2. Why the data needs to split between Train and validation?
        3. How the process looks like for data stored in a CSV file.
        4. Important properties of the data object from the below code
        5. 'data = ImageClassifierData.from_paths(PATH, tfms=tfms_from_model(arch, sz))'
        6. What is data augmentation and why it is helpful.
    2. Setting up the architecture
        1. What are the pre-trained weights. 
        2. Where they came from?
        3. Why they are useful?  
    3. Training the network
        1. What is batch processing. Why it is helpful? what is the trade off.
        2. What is gradient descent.
        3. What is stochastic gradient descent.
        4. What is SGDR and why it helps. Understanding cycle len and cycle multiplier.
        5. Techniques to reduce the training time
            1. Precompute parameter.
            2. Freezing and Unfreezing layers.
    4. Analyzing results
        1. Confusion matrix.
        2. Creating the confusion matrix in the code.
    5. High level overview of CNN.
    6. Summary 





