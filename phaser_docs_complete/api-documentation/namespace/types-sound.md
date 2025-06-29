# Phaser.Types.Sound

Scope:
static

> Source: [src/sound/typedefs/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/typedefs/index.js#L7)

# Static functions

## AudioSpriteSound

### AudioSpriteSound

**Description:**

Audio sprite sound type.

> Source: [src/sound/typedefs/AudioSpriteSound.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/typedefs/AudioSpriteSound.js#L1)  
> Since: 3.0.0

---

## DecodeAudioConfig

### DecodeAudioConfig

**Description:**

A Audio Data object.

You can pass an array of these objects to the WebAudioSoundManager `decodeAudio` method to have it decode

them all at once.

> Source: [src/sound/typedefs/DecodeAudioConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/typedefs/DecodeAudioConfig.js#L1)  
> Since: 3.18.0

---

## EachActiveSoundCallback

### EachActiveSoundCallback

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| manager | [Phaser.Sound.BaseSoundManager](../class/sound-basesoundmanager.md) | No | The SoundManager |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.BaseSound](../class/sound-basesound.md) | No | The current active Sound |
| index | number | No | The index of the current active Sound |
| sounds | Array.<[Phaser.Sound.BaseSound](../class/sound-basesound.md)> | No | All sounds |

> Source: [src/sound/typedefs/EachActiveSoundCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/typedefs/EachActiveSoundCallback.js#L1)  
> Since: 3.0.0

---

## SoundConfig

### SoundConfig

**Description:**

Config object containing various sound settings.

> Source: [src/sound/typedefs/SoundConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/typedefs/SoundConfig.js#L1)  
> Since: 3.0.0

---

## SoundMarker

### SoundMarker

**Description:**

Marked section of a sound represented by name, and optionally start time, duration, and config object.

> Source: [src/sound/typedefs/SoundMarker.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/typedefs/SoundMarker.js#L1)  
> Since: 3.0.0

---

## SpatialSoundConfig

### SpatialSoundConfig

**Description:**

Config object containing settings for the source of the spatial sound.

See <https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Web_audio_spatialization_basics>

> Source: [src/sound/typedefs/SpatialSoundConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/typedefs/SpatialSoundConfig.js#L1)  
> Since: 3.60.0

---

## WebAudioDecodeEntry

### WebAudioDecodeEntry

**Description:**

An entry in the Web Audio Decoding Queue.

> Source: [src/sound/typedefs/WebAudioDecodeEntry.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/typedefs/WebAudioDecodeEntry.js#L1)  
> Since: 3.60.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [AudioSpriteSound](#audiospritesound)

    - [AudioSpriteSound](#audiospritesound-1)
  + [DecodeAudioConfig](#decodeaudioconfig)

    - [DecodeAudioConfig](#decodeaudioconfig-1)
  + [EachActiveSoundCallback](#eachactivesoundcallback)

    - [EachActiveSoundCallback](#eachactivesoundcallback-1)
  + [SoundConfig](#soundconfig)

    - [SoundConfig](#soundconfig-1)
  + [SoundMarker](#soundmarker)

    - [SoundMarker](#soundmarker-1)
  + [SpatialSoundConfig](#spatialsoundconfig)

    - [SpatialSoundConfig](#spatialsoundconfig-1)
  + [WebAudioDecodeEntry](#webaudiodecodeentry)

    - [WebAudioDecodeEntry](#webaudiodecodeentry-1)

Back to top

©2025[Phaser](https://docs.phaser.io)