from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'

SOURCES_LIST = [IMAGE]

# ML Model config
MODEL_DIR =  'weights/'
DETECTION_MODEL1 = MODEL_DIR+'model1/yolov8.pkl'
DETECTION_MODEL2 = MODEL_DIR+'model2/classifyWaste.h5'