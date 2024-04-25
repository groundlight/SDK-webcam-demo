# SDK-webcam-demo
If you've tried the Groundlight explore page demo and are ready for more, this demo will help you set up your next full fledged detector

## Overview
All Groundlight users get one basic explore page detector that you can use to easily test Groundlight out from your own webcam. However, in order to customize your detectors or support a fleet of detectors answering different questions, you'll need to set up detectors through the Groundlight SDK. This demo will help you set up a new detector with the SDK that can be used to detect objects in your webcam feed.

After setting up a detector with the SDK, you can try use this demo as a starting point to build your own custom application. Try connecting to remote cameras over RTSP or using multiple detectors to ask more complex questions.

## How to use
To get started:
1. Clone this repository

        git clone https://github.com/groundlight/SDK-webcam-demo.git
        cd SDK-webcam-demo

2. Install dependencies. This installs the Groundlight SDK and Framegrab, a convenient library for capturing frames from cameras on your device or network.

        poetry install

or if you prefer pip

        pip install -r requirements.txt

3. Run the demo

        python demo.py

And as easy as that, you've created a new detector. Log into https://app.groundlight.ai to see your new detector in the dashboard. Then you can try changing the query and customizing your detector!