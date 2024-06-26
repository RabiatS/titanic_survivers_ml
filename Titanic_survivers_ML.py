!chmod 600 kaggle.json && (ls ~/.kaggle 2>/dev/null || mkdir ~/.kaggle) && cp kaggle.json ~/.kaggle/ && echo 'Done'
!kaggle competitions download -c titanic
!mv ../notebooks/titanic.zip ../data/
!ls

# Dependencies
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

trainset = pd.read_csv("../data/train.csv")
testset = pd.read_csv("../data/test.csv")
genderset = pd.read_csv("../data/gender_submission.csv")