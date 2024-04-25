import time

from groundlight import Groundlight
import framegrab
from framegrab import FrameGrabber

DETECTOR_NAME = "SDK Person Detector"
DETECTOR_QUERY = "Is there a person in the frame?"
WAIT_TIME = 60

# Find a connected camera that we can use to capture images and send to Groundlight
grabbers = FrameGrabber.autodiscover()
if len(grabbers) == 0:
    raise OSError("No attached cameras were found. Make sure your camera is connected, powered on, and is accessible to the current user.")
elif len(grabbers) > 1:
    print("Multiple cameras were found! Using the first one.")
grabber = list(grabbers.values())[0]

# Initialize the Groundlight client which we use to send images to the Groundlight service
# NOTE: You must have a valid API key saved to an environment variable named GROUNDLIGHT_API_TOKEN. You can get one by signing up at https://groundlight.ai
gl = Groundlight()
det = gl.get_or_create_detector(DETECTOR_NAME, DETECTOR_QUERY)

# Continuously grab frames from the camera and send them to Groundlight. By default, we wait 60 seconds between each frame.
while True:
    frame = grabber.grab()
    print("Sending image to Groundlight...")
    result = gl.submit_image_query(det, frame)
    print(f"Asked {DETECTOR_QUERY} and got answer: {str(result.result.label)}")
    time.sleep(WAIT_TIME)