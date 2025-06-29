# Audio

A Guide to Phaser Audio

Web Browsers offer the ability to play audio in two different ways. The first is known as the Audio Tag. This is an HTML tag you can put on a web page that offers UI controls to play and pause/resume audio files. The second is known as the Web Audio API. This is a JavaScript API that allows you to create and control audio files directly from your code. It's a much more powerful system than the Audio Tag, but is not supported by all browsers.

Phaser has a built-in Sound Manager that allows you to play audio files in your game. It will automatically detect if the browser supports the Web Audio API and if it does, it will use that. If not, it will fall back to the Audio Tag. This means that you can use the same API to play audio files in all browsers, regardless of their support for the Web Audio API.

As with WebGL vs. Canvas, there are things that only Web Audio can do. Such as positional audio, i.e. having sounds 'follow' a player across the game world. It's also much better suited to playing lots of short duration sound effects in quick succession, i.e. "gunshots" or "explosions".

You can pick which audio system you'd like to use via the Game Configuration, or even disable audio entirely. Not all games need audio, after all.

The Phaser Sound Manager is a global system. This means that it belongs to the Game instance, and if you start to play a sound in one Scene, it won't automatically stop just because you change to another Scene. This gives you a lot of control, but also means you need to be careful to stop looping sounds when you're done with them, or they'll keep playing.

## Autoplay

Most browsers won't play sound until the user clicks/taps on the game. You can check the sound manager's `locked` property for this.

Chrome gives a console warning if the game boots using Web Audio:

> The AudioContext was not allowed to start. It must be resumed (or created) after a user gesture on the page

That's normal. Phaser will try to resume the audio context after the first user gesture (click/tap). If you don't need sound in your game, disable audio and you won't see this warning.

You can also create the game from a click/tap to avoid this problem.

Some browsers give a console error when playing a locked sound fails, and some don't.

* [Autoplay guide for media and Web Audio APIs](https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide)

## Configuration

### Web audio

Web audio is the default audio context.

### Disable web audio

```
Copyvar config = {
  // ....
  audio: {
    disableWebAudio: true,
  },
  // ....
};
var game = new Phaser.Game(config);

```

### Disable all audio

```
Copyvar config = {
  // ....
  audio: {
    noAudio: true,
  },
  // ....
};
var game = new Phaser.Game(config);

```

## Loading audio files

See details in [Media container formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Containers) and [Web audio codec guide](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Audio_codecs). If you're publishing a game you should probably support at least [MP3](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Containers#mpegmpeg-2).

When loading audio, Phaser matches the media type (inferred from the URL or given by you) with the device's support for that type. If there's no match, **nothing** is downloaded and if you try to create or play a sound with that key it will fail with an error.

```
Copythis.load.audio(key, urls, config, xhrSettings);

```

* `key` : The key to use for this file, or a file configuration object, or array of them.
* `urls` : The absolute or relative URL to load the audio files from.
* `config` : An object containing an instances property for HTML5Audio. Defaults to 1.
* `xhrSettings` : An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings.

### Decode audio

Decode audio data into a format ready for playback via Web Audio. The audio data can be a base64 encoded string, an audio media-type data uri, or an ArrayBuffer instance.

```
Copythis.sound.decodeAudio(key, audioData);

```

* `audioData` : Audio data
  + A base64 encoded string
  + An audio media-type data uri
  + An ArrayBuffer instance

Or

```
Copythis.sound.decodeAudio(audioFiles);

```

* `audioFiles` : An array of `{key, data}`
  + `data` : Audio data
    - A base64 encoded string
    - An audio media-type data uri
    - An ArrayBuffer instance

### Decoded events

* Finished decoding an audio data

  ```
  Copythis.sound.on("decoded", key);

  ```
* Finished decoding all audio data

  ```
  Copythis.sound.on("decodedall");

  ```

## Unlock audio

Unlocks Web Audio API/HTML5 Audio loading on the initial input event.

```
Copythis.sound.unlock();

```

## Play sound

Sound instance will be destroyed when playback ends.

```
Copythis.sound.play(key);

```

or

```
Copythis.sound.play(key, config);
/*
var sound = this.sound.add(key);
sound.play(config);
*/

```

## Position of the Spatial Audio listener

Sets the `x` and `y` position of the Spatial Audio listener on this Web Audios context.

```
Copythis.sound.setListenerPosition(x, y);

```

* `x`, `y` : The x/y position of the Spatial Audio listener. Default value is center of the game canvas.

!!! note
Web audio only

## Sound instance

### Create sound instance

Adds a new sound into the sound manager.

```
Copyvar music = this.sound.add(key);

```

```
Copyvar music = this.sound.add(key, config);

```

* `config` : An optional config object containing default sound settings.

#### Sound instance configuration

```
Copy{
    mute: false,
    volume: 1,
    rate: 1,
    detune: 0,
    seek: 0,
    loop: false,
    delay: 0,

    // source of the spatial sound
    source: {
        x: 0,
        y: 0,
        z: 0,
        panningModel: 'equalpower',
        distanceModel: 'inverse',
        orientationX: 0,
        orientationY: 0,
        orientationZ: -1,
        refDistance: 1,
        maxDistance: 10000,
        rolloffFactor: 1,
        coneInnerAngle: 360,
        coneOuterAngle: 0,
        coneOuterGain: 0,
        follow: undefined
    }
}

```

* `source` : Source of the spatial sound
  + `x`, `y` : The horizontal/vertical position of the audio in a right-hand Cartesian coordinate system.
  + `z` : Represents the longitudinal (back and forth) position of the audio in a right-hand Cartesian coordinate system.
  + `panningModel` : An enumerated value determining which spatialization algorithm to use to position the audio in 3D space.
    - `'equalpower'`
    - `'HRTF'`
  + `orientationX`, `orientationY` : The horizontal/vertical position of the audio source's vector in a right-hand Cartesian coordinate system.
  + `orientationZ` : Represents the longitudinal (back and forth) position of the audio source's vector in a right-hand Cartesian coordinate system.
  + `refDistance` : A double value representing the reference distance for reducing volume as the audio source moves further from the listener. For distances greater than this the volume will be reduced based on `rolloffFactor` and `distanceModel`.
  + `maxDistance` : The maximum distance between the audio source and the listener, after which the volume is not reduced any further.
  + `rolloffFactor` : A double value describing how quickly the volume is reduced as the source moves away from the listener. This value is used by all distance models.
  + `coneInnerAngle` : The angle, in degrees, of a cone inside of which there will be no volume reduction.
  + `coneOuterAngle` : The angle, in degrees, of a cone outside of which the volume will be reduced by a constant value, defined by the `coneOuterGain` property.
  + `coneOuterGain` : The amount of volume reduction outside the cone defined by the `coneOuterAngle` attribute. Its default value is `0`, meaning that no sound can be heard. A value between `0` and `1`.
  + `follow` : Set this Sound object to automatically track the x/y position of this object. Can be a Phaser Game Object, Vec2 or anything that exposes public x/y properties.

### Play sound instance

* Start playing

  ```
  Copymusic.play();

  ```
* Start playing with configuration

  ```
  Copymusic.play(config);

  ```

  + [config](#sound-instance-configuration)
* Stop

  ```
  Copymusic.stop();

  ```
* Pause

  ```
  Copymusic.pause();

  ```
* Resume

  ```
  Copymusic.resume();

  ```

### Methods

#### Mute

* Set

  ```
  Copymusic.setMute(mute); // mute: true/false
  // music.mute = mute;

  ```
* Get

  ```
  Copyvar mute = music.mute;

  ```

#### Volume

* Set

  ```
  Copymusic.setVolume(volume); // volume: 0 to 1
  // music.volume = volume;

  ```
* Get

  ```
  Copyvar volume = music.volume;

  ```

#### Detune

Sets global detuning of all sounds in [cents](https://en.wikipedia.org/wiki/Cent_%28music%29). The range of the value is -1200 to 1200, but we recommend setting it to 50.

* Set

  ```
  Copymusic.setDetune(detune); // detune: -1200 to 1200
  // music.detune = detune;

  ```
* Get

  ```
  Copyvar detune = music.detune;

  ```

#### Playback rate

* Set

  ```
  Copymusic.setRate(rate); // rate: 1.0(normal speed), 0.5(half speed), 2.0(double speed)
  // music.rate = rate;

  ```
* Get

  ```
  Copyvar rate = music.rate;

  ```

#### Seek to

* Seek to

  ```
  Copymusic.setSeek(time); // seek: playback time
  // music.seek = seek;

  ```
* Get current playback time

  ```
  Copyvar time = music.seek; // return 0 when playback ends

  ```

#### Loop

* Set

  ```
  Copymusic.setLoop(loop); // loop: true/false
  // music.loop = loop;

  ```
* Get

  ```
  Copyvar loop = music.loop;

  ```

### Properties

* Duration : duration of this sound

  ```
  Copyvar duration = music.duration;

  ```
* Is playing

  ```
  Copyvar isPlaying = music.isPlaying;

  ```
* Is paused

  ```
  Copyvar isPaused = music.isPaused;

  ```
* Asset key

  ```
  Copyvar key = music.key;

  ```

### Events

* Start playing

  ```
  Copymusic.once("play", function (music) {});

  ```
* Playback end

  ```
  Copymusic.once("complete", function (music) {});

  ```
* Looping

  ```
  Copymusic.once("looped", function (music) {});

  ```
* Pause

  ```
  Copymusic.once("pause", function (music) {});

  ```
* Resume

  ```
  Copymusic.once("resume", function (music) {});

  ```
* Stop

  ```
  Copymusic.once("stop", function (music) {});

  ```
* Set mute

  ```
  Copymusic.once("mute", function (music, mute) {});

  ```
* Set volume

  ```
  Copymusic.once("volume", function (music, volume) {});

  ```
* Set detune

  ```
  Copymusic.once("detune", function (music, detune) {});

  ```
* Set play-rate

  ```
  Copymusic.once("rate", function (music, rate) {});

  ```
* Seek to

  ```
  Copymusic.once("seek", function (music, time) {});

  ```
* set loop

  ```
  Copymusic.once("loop", function (music, loop) {});

  ```

## Play marked sound

Sound instance will be destroyed when playback ends.

```
Copythis.sound.play(key, marker);

```

* `marker` : Marked section of a sound represented by name, and optionally start time, duration, and config object.

### Marker

```
Copy{
    name: '',
    start: 0,
    duration: music.duration,
    config: {
        mute: false,
        volume: 1,
        rate: 1,
        detune: 0,
        seek: 0,
        loop: false,
        delay: 0
    }
}

```

## Markers in sound instance

### Add marker

```
Copymusic.addMarker(marker);

```

[Marker](#marker)

### Play marked sound

```
Copymusic.play(markerName);

```

```
Copymusic.play(markerName, config);

```

[config](#sound-instance-configuration)

## Audio sprite

### Load audio sprite

```
Copyscene.load.audioSprite(key, urls, markersConfig, config);

```

See [loader](loader.md)

Format of markersConfig

```
Copy{
    resources: urls, // an array of audio files
    spritemap: {
        markerName0: {
            start: 0,
            end: 0
        },
        markerName1: {
            start: 0,
            end: 0
        }
        // ...
    }
}

```

### Play sound

Create a sound instance then play the marked section, this sound instance will be destroyed when playback ends.

```
Copythis.sound.playAudioSprite(key, markerName, config);

```

[config](#sound-instance-configuration)

### Sound instance

Create a sound instance with markers.

```
Copyvar music = this.sound.addAudioSprite(key, config);

```

[config](#sound-instance-configuration)

### Play sound instance

```
Copymusic.play(markerName);

```

```
Copymusic.play(markerName, config);

```

[config](#sound-instance-configuration)

## Sound manager

### Mute

* Set

  ```
  Copythis.sound.setMute(mute); // mute: true/false
  // this.sound.mute = mute;

  ```
* Get

  ```
  Copyvar mute = this.sound.mute;

  ```

### Volume

* Set

  ```
  Copythis.sound.setVolume(volume); // volume: 0 to 1
  // this.sound.volume = volume;

  ```
* Get

  ```
  Copyvar volume = this.sound.volume;

  ```

### Detune

* Set

  ```
  Copythis.sound.setDetune(detune); // detune: -1200 to 1200
  // this.sound.detune = detune;

  ```
* Get

  ```
  Copyvar detune = this.sound.detune;

  ```

### Playback rate

* Set

  ```
  Copythis.sound.setRate(rate); // rate: 1.0(normal speed), 0.5(half speed), 2.0(double speed)
  // this.sound.rate = rate;

  ```
* Get

  ```
  Copyvar rate = this.sound.rate;

  ```

### Get music instance

* Get first by key

  ```
  Copyvar music = this.sound.get(key); // music instance, or null

  ```
* Get all by key

  ```
  Copyvar musicArray = this.sound.getAll(key); // music instance, or null

  ```
* Get all

  ```
  Copyvar musicArray = this.sound.getAll();

  ```
* Get all playing

  ```
  Copyvar musicArray = this.sound.getAllPlaying();

  ```

### Remove music instance

* Remove by key

  ```
  Copyvar removed = this.sound.removeByKey(key);

  ```

  + `removed` : The number of matching sound objects that were removed.
* Remove all

  ```
  Copythis.sound.removeAll();

  ```

### Stop music instance

* Stop by key

  ```
  Copyvar stopped = this.sound.stopByKey(key);

  ```

  + `stopped` : How many sounds were stopped.
* Stop all

  ```
  Copythis.sound.stopAll();

  ```

## Analyser

Web Audio API has the ability to extract frequency, waveform, and other data from your audio source, which can then be used to create [visualizations](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Visualizations_with_Web_Audio_API).

1. Create analyser node

   ```
   Copyvar analyser = this.sound.context.createAnalyser();

   ```
2. Configure analyser node

   ```
   Copyanalyser.smoothingTimeConstant = 1;
   analyser.fftSize = 8192;
   analyser.minDecibels = -90;
   analyser.maxDecibels = -10;

   ```

   * `smoothingTimeConstant` : Averaging constant with the last analysis frame.
     + `0`(no time averaging) ~ `1`. Default value is `0.8`.
   * `fftSize` : Window size.
     + `32`, `64`, `128`, `256`, `512`, `1024`, `2048`, `4096`, `8192`, `16384`, and `32768`. Defaults to `2048`.
   * `minDecibels` : Minimum *decibel* value for scaling the FFT analysis data.
     + `0` dB is the loudest possible sound, `-10` dB is a 10th of that, etc. The default value is `-100` dB
   * `maxDecibels` : Maximum *decibel* value for scaling the FFT analysis data.
     + The default value is `-30` dB.
3. Set source of analyser node

   * Global volume nodee -> analyser node

     ```
     Copythis.sound.masterVolumeNode.connect(analyser);

     ```
   * A sound instance -> analyser node

     ```
     Copymusic.volumeNode.connect(analyser);

     ```
4. Ouput analyser node to audio context

   ```
   Copyanalyser.connect(this.sound.context.destination);

   ```
5. Create output data array

   ```
   Copyvar dataArrayLength = analyser.frequencyBinCount;
   var dataArray = new Uint8Array(dataArrayLength);

   ```
6. Get output data

   ```
   Copyanalyser.getByteTimeDomainData(dataArray);

   ```

   * Retrieve output data

     ```
     Copyfor (var i = 0; i < dataArrayLength; i++) {
       var data = dataArray[i];
     }

     ```

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)
* [samme](https://github.com/samme)

Updated on June 4, 2025, 1:16 PM UTC

---

[Animations](animations.md)

[Cameras](cameras.md)

On this page

* [Audio](#audio)

  + [Autoplay](#autoplay)
  + [Configuration](#configuration)

    - [Web audio](#web-audio)
    - [Disable web audio](#disable-web-audio)
    - [Disable all audio](#disable-all-audio)
  + [Loading audio files](#loading-audio-files)

    - [Decode audio](#decode-audio)
    - [Decoded events](#decoded-events)
  + [Unlock audio](#unlock-audio)
  + [Play sound](#play-sound)
  + [Position of the Spatial Audio listener](#position-of-the-spatial-audio-listener)
  + [Sound instance](#sound-instance)

    - [Create sound instance](#create-sound-instance)
    - [Play sound instance](#play-sound-instance)
    - [Methods](#methods)
    - [Properties](#properties)
    - [Events](#events)
  + [Play marked sound](#play-marked-sound)

    - [Marker](#marker)
  + [Markers in sound instance](#markers-in-sound-instance)

    - [Add marker](#add-marker)
    - [Play marked sound](#play-marked-sound-1)
  + [Audio sprite](#audio-sprite)

    - [Load audio sprite](#load-audio-sprite)
    - [Play sound](#play-sound-1)
    - [Sound instance](#sound-instance-1)
    - [Play sound instance](#play-sound-instance-1)
  + [Sound manager](#sound-manager)

    - [Mute](#mute-1)
    - [Volume](#volume-1)
    - [Detune](#detune-1)
    - [Playback rate](#playback-rate-1)
    - [Get music instance](#get-music-instance)
    - [Remove music instance](#remove-music-instance)
    - [Stop music instance](#stop-music-instance)
  + [Analyser](#analyser)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../index.md)



Audio