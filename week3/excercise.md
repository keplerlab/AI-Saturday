# Steps to Train a world-class image classifier
1. Enable data augmentation, and precompute = True
2. Use lr_find() to find the highest learning rate where loss is cleary improving
3. Train last layer from precomputed activations for 1-2 epochs
4. Train last layer with data augmentation for 2-3 epochs with cycle len = 1
5. Unfreeze all layers
6. Set earlier to 3x-10x lower learning rate than next higher learning rate
7. use lr_find() again
8. Train full network with cycle mult=2 until over fitting

# How to download the kaggle data
1. Download the kaggle cli project on the paperspace machine
'''
git clone https://github.com/Kaggle/kaggle-api
'''
2. Follow the installations steps mentioned on the github project page.
3. Download the data using the following commands 
   '''
   kaggle competitions download -c <REPLACE THE COMPETITION NAME> -f <REPLACE THE FILE NAME>
   ''' 

## Build a digit recognizer using the steps mentioned above
1. Create a new notebook.
2. Download the data  from here https://www.kaggle.com/c/digit-recognizer/data
   
   ## Build a plant seedlings classification using the steps mentioned above.
1. Create a new notebook.
2. Download data from here https://www.kaggle.com/c/plant-seedlings-classification/data
'''
function to create validation set when there are multiple classes

'''

## Build a invasive-species-monitoring using the steps mentioned above.
1. Create a new notebook
2. Download data from here https://www.kaggle.com/c/invasive-species-monitoring/data
'''
Function to create validation set when there is only one class
def create_val(path, r):
    """ Takes a path to a dataset and creates a validation set of specified size

    Parameters:
    -----------
    path: dataset path
    r (float): proportion of examples to use for validation, in the range from 0 to 1

    """
    val_path = os.path.join(os.path.split(path)[0], 'valid')
    print(val_path)
                  
    files = [p for p in glob(os.path.join(path, '*'))]
    copy_or_move_files(files, path, val_path, r, move=True)

def copy_or_move_files(file_lst, src, dst, r, move=False):
    do = shutil.move if move else shutil.copyfile
    os.makedirs(dst)
    np.random.shuffle(file_lst)
    for f in file_lst[:int(len(file_lst) * r)]:
        do(f, os.path.join(dst, os.path.split(f)[1]))

'''


