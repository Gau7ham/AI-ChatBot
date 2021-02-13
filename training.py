import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer  #word net lemmatizer just means that when multiple words means the same ie work working worked it make them as a single word

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD