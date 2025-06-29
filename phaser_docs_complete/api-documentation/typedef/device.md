# Device

Phaser.Device

## Audio

### <static> Audio

Determines the audio playback capabilities of the device running this Phaser Game instance.

These values are read-only and populated during the boot sequence of the game.

They are then referenced by internal game systems and are available for you to access

via `this.sys.game.device.audio` from within any Scene.

| name | type | optional | description |
| --- | --- | --- | --- |
| audioData | boolean | No | Can this device play HTML Audio tags? |
| --- | --- | --- | --- |
| dolby | boolean | No | Can this device play EC-3 Dolby Digital Plus files? |
| m4a | boolean | No | Can this device can play m4a files. |
| aac | boolean | No | Can this device can play aac files. |
| flac | boolean | No | Can this device can play flac files. |
| mp3 | boolean | No | Can this device play mp3 files? |
| ogg | boolean | No | Can this device play ogg files? |
| opus | boolean | No | Can this device play opus files? |
| wav | boolean | No | Can this device play wav files? |
| webAudio | boolean | No | Does this device have the Web Audio API? |
| webm | boolean | No | Can this device play webm files? |

**Type**: object

**Member of**: Phaser.Device

> Source: [src/device/Audio.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/device/Audio.js#L9)  
> Since: 3.0.0

---

## Browser

### <static> Browser

Determines the browser type and version running this Phaser Game instance.

These values are read-only and populated during the boot sequence of the game.

They are then referenced by internal game systems and are available for you to access

via `this.sys.game.device.browser` from within any Scene.

| name | type | optional | description |
| --- | --- | --- | --- |
| chrome | boolean | No | Set to true if running in Chrome. |
| --- | --- | --- | --- |
| edge | boolean | No | Set to true if running in Microsoft Edge browser. |
| firefox | boolean | No | Set to true if running in Firefox. |
| ie | boolean | No | Set to true if running in Internet Explorer 11 or less (not Edge). |
| mobileSafari | boolean | No | Set to true if running in Mobile Safari. |
| opera | boolean | No | Set to true if running in Opera. |
| safari | boolean | No | Set to true if running in Safari. |
| silk | boolean | No | Set to true if running in the Silk browser (as used on the Amazon Kindle) |
| trident | boolean | No | Set to true if running a Trident version of Internet Explorer (IE11+) |
| chromeVersion | number | No | If running in Chrome this will contain the major version number. |
| firefoxVersion | number | No | If running in Firefox this will contain the major version number. |
| ieVersion | number | No | If running in Internet Explorer this will contain the major version number. Beyond IE10 you should use Browser.trident and Browser.tridentVersion. |
| safariVersion | number | No | If running in Safari this will contain the major version number. |
| tridentVersion | number | No | If running in Internet Explorer 11 this will contain the major version number. See {@link [http://msdn.microsoft.com/en-us/library/ie/ms537503(v=vs.85).aspx}](http://msdn.microsoft.com/en-us/library/ie/ms537503(v=vs.85).aspx%7D) |

**Type**: object

**Member of**: Phaser.Device

> Source: [src/device/Browser.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/device/Browser.js#L9)  
> Since: 3.0.0

---

## CanvasFeatures

### <static> CanvasFeatures

Determines the canvas features of the browser running this Phaser Game instance.

These values are read-only and populated during the boot sequence of the game.

They are then referenced by internal game systems and are available for you to access

via `this.sys.game.device.canvasFeatures` from within any Scene.

| name | type | optional | description |
| --- | --- | --- | --- |
| supportInverseAlpha | boolean | No | Set to true if the browser supports inversed alpha. |
| --- | --- | --- | --- |
| supportNewBlendModes | boolean | No | Set to true if the browser supports new canvas blend modes. |

**Type**: object

**Member of**: Phaser.Device

> Source: [src/device/CanvasFeatures.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/device/CanvasFeatures.js#L9)  
> Since: 3.0.0

---

## Features

### <static> Features

Determines the features of the browser running this Phaser Game instance.

These values are read-only and populated during the boot sequence of the game.

They are then referenced by internal game systems and are available for you to access

via `this.sys.game.device.features` from within any Scene.

| name | type | optional | description |
| --- | --- | --- | --- |
| canvas | boolean | No | Is canvas available? |
| --- | --- | --- | --- |
| canvasBitBltShift | boolean | No | True if canvas supports a 'copy' bitblt onto itself when the source and destination regions overlap. |
| file | boolean | No | Is file available? |
| fileSystem | boolean | No | Is fileSystem available? |
| getUserMedia | boolean | No | Does the device support the getUserMedia API? |
| littleEndian | boolean | No | Is the device big or little endian? (only detected if the browser supports TypedArrays) |
| localStorage | boolean | No | Is localStorage available? |
| pointerLock | boolean | No | Is Pointer Lock available? |
| stableSort | boolean | No | Is Array.sort stable? |
| support32bit | boolean | No | Does the device context support 32bit pixel manipulation using array buffer views? |
| vibration | boolean | No | Does the device support the Vibration API? |
| webGL | boolean | No | Is webGL available? |
| worker | boolean | No | Is worker available? |

**Type**: object

**Member of**: Phaser.Device

> Source: [src/device/Features.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/device/Features.js#L11)  
> Since: 3.0.0

---

## Fullscreen

### <static> Fullscreen

Determines the full screen support of the browser running this Phaser Game instance.

These values are read-only and populated during the boot sequence of the game.

They are then referenced by internal game systems and are available for you to access

via `this.sys.game.device.fullscreen` from within any Scene.

| name | type | optional | description |
| --- | --- | --- | --- |
| available | boolean | No | Does the browser support the Full Screen API? |
| --- | --- | --- | --- |
| keyboard | boolean | No | Does the browser support access to the Keyboard during Full Screen mode? |
| cancel | string | No | If the browser supports the Full Screen API this holds the call you need to use to cancel it. |
| request | string | No | If the browser supports the Full Screen API this holds the call you need to use to activate it. |

**Type**: object

**Member of**: Phaser.Device

> Source: [src/device/Fullscreen.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/device/Fullscreen.js#L7)  
> Since: 3.0.0

---

## Input

### <static> Input

Determines the input support of the browser running this Phaser Game instance.

These values are read-only and populated during the boot sequence of the game.

They are then referenced by internal game systems and are available for you to access

via `this.sys.game.device.input` from within any Scene.

| name | type | optional | description |
| --- | --- | --- | --- |
| wheelType | string | No | The newest type of Wheel/Scroll event supported: 'wheel', 'mousewheel', 'DOMMouseScroll' |
| --- | --- | --- | --- |
| gamepads | boolean | No | Is navigator.getGamepads available? |
| mspointer | boolean | No | Is mspointer available? |
| touch | boolean | No | Is touch available? |

**Type**: object

**Member of**: Phaser.Device

> Source: [src/device/Input.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/device/Input.js#L9)  
> Since: 3.0.0

---

## OS

### <static> OS

Determines the operating system of the device running this Phaser Game instance.

These values are read-only and populated during the boot sequence of the game.

They are then referenced by internal game systems and are available for you to access

via `this.sys.game.device.os` from within any Scene.

| name | type | optional | description |
| --- | --- | --- | --- |
| android | boolean | No | Is running on android? |
| --- | --- | --- | --- |
| chromeOS | boolean | No | Is running on chromeOS? |
| cordova | boolean | No | Is the game running under Apache Cordova? |
| crosswalk | boolean | No | Is the game running under the Intel Crosswalk XDK? |
| desktop | boolean | No | Is running on a desktop? |
| ejecta | boolean | No | Is the game running under Ejecta? |
| electron | boolean | No | Is the game running under GitHub Electron? |
| iOS | boolean | No | Is running on iOS? |
| iPad | boolean | No | Is running on iPad? |
| iPhone | boolean | No | Is running on iPhone? |
| kindle | boolean | No | Is running on an Amazon Kindle? |
| linux | boolean | No | Is running on linux? |
| macOS | boolean | No | Is running on macOS? |
| node | boolean | No | Is the game running under Node.js? |
| nodeWebkit | boolean | No | Is the game running under Node-Webkit? |
| webApp | boolean | No | Set to true if running as a WebApp, i.e. within a WebView |
| windows | boolean | No | Is running on windows? |
| windowsPhone | boolean | No | Is running on a Windows Phone? |
| iOSVersion | number | No | If running in iOS this will contain the major version number. |
| pixelRatio | number | No | PixelRatio of the host device? |

**Type**: object

**Member of**: Phaser.Device

> Source: [src/device/OS.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/device/OS.js#L7)  
> Since: 3.0.0

---

## Video

### <static> Video

Determines the video support of the browser running this Phaser Game instance.

These values are read-only and populated during the boot sequence of the game.

They are then referenced by internal game systems and are available for you to access

via `this.sys.game.device.video` from within any Scene.

In Phaser 3.20 the properties were renamed to drop the 'Video' suffix.

| name | type | optional | description |
| --- | --- | --- | --- |
| h264 | boolean | No | Can this device play h264 mp4 video files? |
| --- | --- | --- | --- |
| hls | boolean | No | Can this device play hls video files? |
| mp4 | boolean | No | Can this device play h264 mp4 video files? |
| m4v | boolean | No | Can this device play m4v (typically mp4) video files? |
| ogg | boolean | No | Can this device play ogg video files? |
| vp9 | boolean | No | Can this device play vp9 video files? |
| webm | boolean | No | Can this device play webm video files? |
| getVideoURL | function | No | Returns the first video URL that can be played by this browser. |

**Type**: object

**Member of**: Phaser.Device

> Source: [src/device/Video.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/device/Video.js#L9)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Device](#device)

  + [Audio](#audio)

    - [<static> Audio](#static-audio)
  + [Browser](#browser)

    - [<static> Browser](#static-browser)
  + [CanvasFeatures](#canvasfeatures)

    - [<static> CanvasFeatures](#static-canvasfeatures)
  + [Features](#features)

    - [<static> Features](#static-features)
  + [Fullscreen](#fullscreen)

    - [<static> Fullscreen](#static-fullscreen)
  + [Input](#input)

    - [<static> Input](#static-input)
  + [OS](#os)

    - [<static> OS](#static-os)
  + [Video](#video)

    - [<static> Video](#static-video)

Back to top

©2025[Phaser](https://docs.phaser.io)



Device