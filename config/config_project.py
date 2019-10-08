import os
import multiprocessing
from keras import backend as k

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["CUDA_VISIBLE_DEVICES"] = '0'

EXT_AUDIO = '*.wav'
EXT_IMG = '.png'
SEED = 1337

# Spectrogram Parameters
N_MELS = 128
SR = 22050
HOP_LENGTH = 512
N_FFT = 2048
OFFSET = 0.0
DURATION = 29.0
AUDIO_THRESHOLD = 29.0

# Keras Parameters
FIG_SIZE = 7.68, 5.12
IMG_SIZE = (512, 768, 3)
TARGET_SIZE = (512, 768)

FIG_SIZE_AUTOENCODERS = 3.92, 2.56
IMG_SIZE_AUTOENCODERS = (256, 392, 3)
TARGET_SIZE_AUTOENCODERS = (256, 392)

BATCH_SIZE = 4

EARLY_STOPPING = 20
REDUCE_LR = 13
LR = 1e-3
LR_DECAY = 1e-6
MOMENTUM = 0.9
NUM_WORKERS = multiprocessing.cpu_count()
# NUM_EPOCHS = 128
NUM_EPOCHS = 1
 