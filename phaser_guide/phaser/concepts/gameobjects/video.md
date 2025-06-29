# Video

A Guide to the Phaser Video Game Object

This Game Object is capable of handling playback of a video file, video stream or media stream.

You can optionally 'preload' the video into the Phaser Video Cache:

```
Copypreload () {
  this.load.video('ripley', 'assets/aliens.mp4');
}

create () {
  this.add.video(400, 300, 'ripley');
}

```

You don't have to 'preload' the video. You can also play it directly from a URL:

```
Copycreate () {
  this.add.video(400, 300).loadURL('assets/aliens.mp4');
}

```

To all intents and purposes, a video is a standard Game Object, just like a Sprite. And as such, you can do all the usual things to it, such as scaling, rotating, cropping, tinting, making interactive, giving a physics body, etc.

Transparent videos are also possible via the WebM file format. Providing the video file has was encoded with an alpha channel, and providing the browser supports WebM playback (not all of them do), then it will render in-game with full transparency.

Playback is handled entirely via the Request Video Frame API, which is supported by most modern browsers. A polyfill is provided for older browsers.

**Autoplaying Videos**

Videos can only autoplay if the browser has been unlocked with an interaction, or satisfies the MEI settings. The policies that control autoplaying are vast and vary between browser. You can, and should, read more about it here: <https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide>

If your video doesn't contain any audio, then set the noAudio parameter to true when the video is loaded, and it will often allow the video to play immediately:

```
Copypreload () {
  this.load.video('pixar', 'nemo.mp4', true);
}

```

The 3rd parameter in the load call tells Phaser that the video doesn't contain any audio tracks. Video without audio can autoplay without requiring a user interaction. Video with audio cannot do this unless it satisfies the browsers MEI settings. See the MDN Autoplay Guide for further details.

Or:

```
Copycreate () {
  this.add.video(400, 300).loadURL('assets/aliens.mp4', true);
}

```

You can set the noAudio parameter to true even if the video does contain audio. It will still allow the video to play immediately, but the audio will not start.

Note that due to a bug in IE11 you cannot play a video texture to a Sprite in WebGL. For IE11 force Canvas mode.

More details about video playback and the supported media formats can be found on MDN:

* <https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement>
* <https://developer.mozilla.org/en-US/docs/Web/Media/Formats>

## Load video

```
Copythis.load.video(key, url, noAudio);

```

Reference: [load video](../loader.md)

!!! note "Cross-origin"
Can't load video cross-origin via `this.load.video(...)`.  
Using `this.add.video(x, y).loadURL(urls, noAudio, crossOrigin)` to load video cross-origin.

## Add video object

### Reference video from Video Cache

```
Copyvar video = this.add.video(x, y, key);

```

* `key` : Key of the Video this Game Object will play, as stored in the Video Cache.

### Load video from URL

1. Add video object

   ```
   Copyvar video = this.add.video(x, y);

   ```
2. Play video from URL

   ```
   Copyvideo.loadURL(url);
   // video.loadURL(urls, noAudio, crossOrigin);

   ```

   * `noAudio` : Does the video have an audio track? If not you can enable auto-playing on it.
     + `false` : Has audio track. Default behavior.
   * `crossOrigin` : The value to use for the `crossOrigin` property in the video load request.
     + `undefined` : `crossorigin` will not be set in the request. Default behavior.
     + `'anonymous'`
     + `'use-credentials'`

### Load video from MediaStream

```
Copyvideo.loadMediaStream(stream);
// video.loadMediaStream(stream, noAudio, crossOrigin);

```

* `stream` : The MediaStream object.
* `noAudio` : Does the video have an audio track? If not you can enable auto-playing on it.
  + `false` : Has audio track. Default behavior.
* `crossOrigin` : The value to use for the `crossOrigin` property in the video load request.
  + `undefined` : `crossorigin` will not be set in the request. Default behavior.
  + `'anonymous'`
  + `'use-credentials'`

```
Copynavigator.mediaDevices.getUserMedia({ video: true, audio: false })
    .then(function(stream) {
        video.loadMediaStream(stream, true);
        video.play();
    })
    .catch(function(err) {

    })

```

* [navigator.mediaDevices.getUserMedia](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia)

### Size

* Initial size : 256x265 (`video.setSize(256, 256)`)
* Size after playing : Size of video from metadata

## Play

```
Copyvideo.play();
// video.play(loop, markerIn, markerOut);

```

* `loop` : Should the video loop automatically when it reaches the end? Please note that not all browsers support *seamless* video looping for all encoding formats.
* `markerIn`, `markerOut` : Optional in/out marker time, in seconds, for playback of a sequence of the video.

!!! note "Play video first time"
Call `video.play()` when playing video first time.

!!! note
If you need audio in your videos, then you'll have to consider the fact that
**the video cannot start playing until the user has interacted with the browser**, into your game flow.

## Pause

* Pause

  ```
  Copyvideo.setPaused();
  // video.setPaused(true);

  ```
* Resume

  ```
  Copyvideo.setPaused(false);

  ```

!!! note "Play video after paused"
Call `video.setPaused(false)` to resume playing.

## Stop

Stops the video playing and clears all internal event listeners.

```
Copyvideo.stop();

```

## Is playing

* Is playing

  ```
  Copyvar isPlaying = video.isPlaying();  // (not PAUSE) and (not not ENDED)

  ```
* Is paused

  ```
  Copyvar isPaused = video.isPaused();

  ```

## Playback time

* Get

  ```
  Copyvar playbackTime = video.getCurrentTime();

  ```

  or

  ```
  Copyvar t = video.getProgress(); // t: 0~1

  ```
* Set

  + Set to

    ```
    Copyvideo.setCurrentTime(playbackTime);  // time in seconds

    ```

    or

    ```
    Copyvideo.seekTo(t); // t: 0~1

    ```

    - Is seeking

      ```
      Copyvar isSeeking = video.isSeeking();

      ```
  + Forward

    ```
    Copyvideo.setCurrentTime('+' + time);  // time in seconds
    // video.setCurrentTime('+2');

    ```
  + Backeard

    ```
    Copyvideo.setCurrentTime('-' + time);  // time in seconds
    // video.setCurrentTime('-2');

    ```

## Playback rate

* Get

  ```
  Copyvar rate = video.getPlaybackRate();

  ```
* Set

  ```
  Copyvideo.setPlaybackRate(rate);

  ```

## Duration

```
Copyvar duration = video.getDuration();  // time in seconds

```

## Volume

* Get

  ```
  Copyvar volume = video.getVolume();  // volume: 0~1

  ```
* Set

  ```
  Copyvideo.setVolume(volume);  // volume: 0~1

  ```

## Mute

* Get

  ```
  Copyvar muted = video.isMuted();  // muted: true/false

  ```
* Set

  ```
  Copyvideo.setMute(muted);  // muted: true/false

  ```

## Loop

* Get

  ```
  Copyvar loop = video.getLoop();  // loop: true/false

  ```
* Set

  ```
  Copyvideo.setLoop(loop);  // loop: true/false

  ```

## Video key

* Get

  ```
  Copyvar key = video.getVideoKey();

  ```
* Change video key (video source)

  ```
  Copyvideo.changeSource(key);
  // video.changeSource(key, autoplay, loop, markerIn, markerOut);

  ```

  + `autoplay` : Should the video start playing immediately, once the swap is complete?
  + `loop` : Should the video loop automatically when it reaches the end? **Not all browsers support *seamless* video looping for all encoding formats**.
  + `markerIn`, `markerOut` : Optional in/out marker time, in *seconds*, for playback of a sequence of the video.

## Marks

* Add mark

  ```
  Copyvideo.addMarker(key, markerIn, markerOut);

  ```

  + `key` : A unique name to give this marker.
  + `markerIn`, `markerOut` : The time, in seconds, representing the start/end of this marker.
* Play mark

  ```
  Copyvideo.playMarker(key, loop);

  ```
* Remove mark

  ```
  Copyvideo.removeMarker(key);

  ```

## Snapshot

1. Allocate a canvas texrure

   ```
   Copyvideo.saveSnapshotTexture(key);

   ```

   * `key` : Texture key.
2. Take a snapshot

   ```
   Copyvar canvasTexture = video.video.snapshot();
   // var canvasTexture = video.snapshot(width, height);

   ```

   or

   ```
   Copyvar canvasTexture = video.snapshotArea(x, y, srcWidth, srcHeight);
   // var canvasTexture = video.snapshotArea(x, y, srcWidth, srcHeight, destWidth, destHeight);

   ```

   * `x`, `y` : The horizontal/vertical location of the top-left of the area to grab from.
   * `srcWidth`, `srcHeight` : The width/height of area to grab from the video.
   * `destWidth`, `destHeight` : The destination width/height of the grab, allowing you to resize it.
   * `canvasTexture` : Canvas texture object.
     + Get key of texture

       ```
       Copyvar key = canvasTexture.key;

       ```

## Save texture

The saved texture is automatically updated as the video plays. If you pause this video, or change its source, then the saved texture updates instantly.

```
Copyvar texture = video.saveTexture(key);
// var texture = video.saveTexture(key, flipY);

```

* `flipY` : Set to `true` if use it as the input for a Shader.

## Events

* The media source doesn't represent a supported media format.

  ```
  Copyvideo.on('unsupported', function(video, error){

  }, scope);

  ```
* A Video is unlocked by a user gesture.

  ```
  Copyvideo.on('unlocked', function(video, error){

  }, scope);

  ```
* A Video tries to play a source that does not exist, or is the wrong file type.

  ```
  Copyvideo.on('error', function(video, error){

  }, scope);

  ```
* A Video has access to the metadata.

  ```
  Copyvideo.on('metadata', function(video){

  }, scope);

  ```
* A Video has exhausted its allocated time while trying to connect to a video source to start playback.

  ```
  Copyvideo.on('timeout', function(video){

  }, scope);

  ```
* A Video begins playback.

  ```
  Copyvideo.on('play', function(video){

  }, scope);

  ```
* First started or restarted.

  ```
  Copyvideo.on('playing', function(video){

  }, scope);

  ```
* The video has finished loading enough data for its first frame.

  ```
  Copyvideo.on('textureready', function(video){

  }, scope);

  ```
* A Video finishes playback by reaching the end of its duration, or `markerOut`.

  ```
  Copyvideo.on('complete', function(video){

  }, scope);

  ```
* A Video that is currently playing has looped.

  ```
  Copyvideo.on('loop', function(video){

  }, scope);

  ```
* A Video *begins* seeking to a new point in its timeline.

  ```
  Copyvideo.on('seeking', function(video){

  }, scope);

  ```
* A Video completes seeking to a new point in its timeline.

  ```
  Copyvideo.on('seeked', function(video){

  }, scope);

  ```
* Enough of the video source has been loaded, that the browser is able to render a frame from it.

  ```
  Copyvideo.on('created', function(video, width, height){

  }, scope);

  ```
* Stalled by `stalled`, `suspend`, `waiting` DOM event.

  ```
  Copyvideo.on('stalled', function(video, width, height){

  }, scope);

  ```
* A Video is stopped from playback via a call to the `Video.stop` method,

  ```
  Copyvideo.on('stop', function(video){

  }, scope);

  ```

## Other properties

See [game object](../gameobjects.md)

## Create mask

```
Copyvar mask = video.createBitmapMask();

```

See [mask](../display.md)

## Shader effects

Support [preFX and postFX effects](shader.md)

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Tile Sprite](tile-sprite.md)

[Geometry](../geometry.md)

On this page

* [Video](#video)

  + [Load video](#load-video)
  + [Add video object](#add-video-object)

    - [Reference video from Video Cache](#reference-video-from-video-cache)
    - [Load video from URL](#load-video-from-url)
    - [Load video from MediaStream](#load-video-from-mediastream)
    - [Size](#size)
  + [Play](#play)
  + [Pause](#pause)
  + [Stop](#stop)
  + [Is playing](#is-playing)
  + [Playback time](#playback-time)
  + [Playback rate](#playback-rate)
  + [Duration](#duration)
  + [Volume](#volume)
  + [Mute](#mute)
  + [Loop](#loop)
  + [Video key](#video-key)
  + [Marks](#marks)
  + [Snapshot](#snapshot)
  + [Save texture](#save-texture)
  + [Events](#events)
  + [Other properties](#other-properties)
  + [Create mask](#create-mask)
  + [Shader effects](#shader-effects)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../../index.md)