import numpy as np
import argparse
import cv2
import os

DIR = os.path.dirname(os.path.abspath(__file__))
PROTOTXT = os.path.join(DIR, r"models\colorization_deploy_v2.prototxt")
POINTS = os.path.join(DIR, r"models\pts_in_hull.npy")
MODEL = os.path.join(DIR, r"models\colorization_release_v2.caffemodel")

# Argument parser for image path
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
                help="path to input black and white image")
args = vars(ap.parse_args())

print("Loading model...")
net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
pts = np.load(POINTS)

# Load cluster centers for colorization
class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")
pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full((1, 313), 2.606, dtype="float32")]

# Load and preprocess the input image
image = cv2.imread(args["image"])
scaled = image.astype("float32") / 255.0
lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

# Resize to 224x224 and extract L channel
resized = cv2.resize(lab, (224, 224))
L = cv2.split(resized)[0]
L -= 50

print("Colorizing the image...")
net.setInput(cv2.dnn.blobFromImage(L))
ab = net.forward()[0, :, :, :].transpose((1, 2, 0))

# Resize the `ab` result back to original dimensions
ab = cv2.resize(ab, (image.shape[1], image.shape[0]))

# Merge L with ab channels and convert back to BGR
L = cv2.split(lab)[0]
colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
colorized = np.clip(colorized, 0, 1)
colorized = (255 * colorized).astype("uint8")

# Display results
cv2.imshow("Original", image)
cv2.imshow("Colorized", colorized)
cv2.waitKey(0)
cv2.destroyAllWindows()
