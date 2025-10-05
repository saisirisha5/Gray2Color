import numpy as np
import cv2
import os
from PIL import Image

DIR = os.path.dirname(os.path.abspath(__file__))
PROTOTXT = os.path.join(DIR, "models/colorization_deploy_v2.prototxt")
POINTS = os.path.join(DIR, "models/pts_in_hull.npy")
MODEL = os.path.join(DIR, "models/colorization_release_v2.caffemodel")

print("Loading colorization model...")
net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
pts = np.load(POINTS)

# Load cluster centers
class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")
pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full((1, 313), 2.606, dtype="float32")]

def colorize(pil_image: Image.Image) -> Image.Image:
    """Takes a PIL image (grayscale), returns colorized PIL image."""

    # Convert PIL → OpenCV
    image = np.array(pil_image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    scaled = image.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

    # Resize to 224x224 and extract L
    resized = cv2.resize(lab, (224, 224))
    L = cv2.split(resized)[0]
    L -= 50

    # Run model
    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))

    # Resize result to original
    ab = cv2.resize(ab, (image.shape[1], image.shape[0]))
    L = cv2.split(lab)[0]

    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized, 0, 1)
    colorized = (255 * colorized).astype("uint8")

    # Back to PIL
    return Image.fromarray(cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB))
