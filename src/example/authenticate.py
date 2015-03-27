#!/usr/bin/env python

# Credentials shamelessly stolen from:
# https://github.com/Tsar/sony_qx_controller/blob/master/sony_qx_controller.py#L144

from pysony import SonyAPI, payload_header
import base64, hashlib

AUTH_CONST_STRING = "90adc8515a40558968fe8318b5b023fdd48d3828a2dda8905f3b93a3cd8e58dc"

# Enable everything we know about
METHODS_TO_ENABLE = "\
camera/stopMovieRec:\
camera/startMovieRec:\
camera/stopIntervalStillRec:\
camera/startIntervalStillRec:\
camera/stopAudioRec:\
camera/startAudioRec:\
camera/getSupportedShutterSpeed:\
camera/getAvailableShutterSpeed:\
camera/getShutterSpeed:\
camera/setShutterSpeed:\
camera/getSupportedWhiteBalance:\
camera/getAvailableWhiteBalance:\
camera/getWhiteBalance:\
camera/setWhiteBalance:\
camera/stopRecMode:\
camera/startRecMode:\
camera/getSupportedExposureMode:\
camera/getAvailableExposureMode:\
camera/getExposureMode:\
camera/setExposureMode:\
camera/getSupportedFlashMode:\
camera/getAvailableFlashMode:\
camera/getFlashMode:\
camera/setFlashMode:\
camera/getSupportedBeepMode:\
camera/getAvailableBeepMode:\
camera/getBeepMode:\
camera/setBeepMode:\
camera/getSupportedFocusMode:\
camera/getAvailableFocusMode:\
camera/getFocusMode:\
camera/setFocusMode:\
camera/getSupportedShootMode:\
camera/getAvailableShootMode:\
camera/getShootMode:\
camera/setShootMode:\
camera/getSupportedSteadyMode:\
camera/getAvailableSteadyMode:\
camera/getSteadyMode:\
camera/setSteadyMode:\
camera/actFormatStorage:\
camera/getSupportedViewAngle:\
camera/getAvailableViewAngle:\
camera/getViewAngle:\
camera/setViewAngle:\
system/setCurrentTime:\
camera/actTakePicture:\
camera/awaitTakePicture:\
camera/getSupportedIsoSpeedRate:\
camera/getAvailableIsoSpeedRate:\
camera/getIsoSpeedRate:\
camera/setIsoSpeedRate:\
camera/getSupportedPostviewImageSize:\
camera/getAvailablePostviewImageSize:\
camera/getPostviewImageSize:\
camera/setPostviewImageSize:\
camera/startLiveviewWithSize:\
camera/getSupportedStillSize:\
camera/getAvailableStillSize:\
camera/getStillSize:\
camera/setStillSize:\
camera/getSupportedLiveviewSize:\
camera/getAvailableLiveviewSize:\
camera/getLiveviewSize:\
camera/setLiveviewSize:\
camera/actZoom:\
camera/getStorageInformation:\
camera/getSupportedExposureCompensation:\
camera/getAvailableExposureCompensation:\
camera/getExposureCompensation:\
camera/setExposureCompensation:\
camera/getSupportedCameraFunction:\
camera/getAvailableCameraFunction:\
camera/getCameraFunction:\
camera/setCameraFunction:\
camera/cancelTouchAFPosition:\
camera/getTouchAFPosition:\
camera/setTouchAFPosition:\
camera/getApplicationInfo:\
camera/getSupportedFNumber:\
camera/getAvailableFNumber:\
camera/getFNumber:\
camera/setFNumber:\
camera/getSupportedSelfTimer:\
camera/getAvailableSelfTimer:\
camera/getSelfTimer:\
camera/setSelfTimer:\
camera/cancelHalfPressShutter:\
camera/actHalfPressShutter:\
camera/getSupportedProgramShift:\
camera/setProgramShift:\
camera/getEvent:\
camera/getAvailableApiList:\
camera/stopLiveview:\
camera/startLiveview:\
camera/getSupportedMovieQuality:\
camera/getAvailableMovieQuality:\
camera/getMovieQuality:\
camera/setMovieQuality:\
"

camera = SonyAPI()
print "API List:", camera.getAvailableApiList()

# This call fails with a '403 - Permission Error' on the HDR-AS15 (fw V3.0)
print "Get Movie Quality:", camera.getMovieQuality()

resp = camera.actEnableMethods([{"methods": "", "developerName": "", "developerID": "", "sg": ""}])
dg = resp["result"][0]["dg"]

h = hashlib.sha256()
h.update(bytes(AUTH_CONST_STRING + dg))
sg = base64.b64encode(h.digest()).decode("UTF-8")

resp = camera.actEnableMethods([{"methods": METHODS_TO_ENABLE, "developerName": "Sony Corporation", \
   "developerID": "7DED695E-75AC-4ea9-8A85-E5F8CA0AF2F3", "sg": sg}])
print "Authenicated:", resp

print "Get Movie Quality:", camera.getMovieQuality()

