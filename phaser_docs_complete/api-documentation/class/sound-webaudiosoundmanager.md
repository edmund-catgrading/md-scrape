# WebAudioSoundManager

Phaser.Sound.WebAudioSoundManager

Web Audio API implementation of the Sound Manager.

Not all browsers can play all audio formats.

There is a good guide to what's supported: [Cross-browser audio basics: Audio codec support](https://developer.mozilla.org/en-US/Apps/Fundamentals/Audio_and_video_delivery/Cross-browser_audio_basics#Audio_Codec_Support).

**Constructor**

`new WebAudioSoundManager(game)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](game.md) | No | Reference to the current game instance. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.Sound.BaseSoundManager](sound-basesoundmanager.md)

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L16)  
> Since: 3.0.0

# Public Members

## context

### context: AudioContext

**Description:**

The AudioContext being used for playback.

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L40)  
> Since: 3.0.0

---

## destination

### destination: AudioNode

**Description:**

Destination node for connecting individual sounds to.

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L71](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L71)  
> Since: 3.0.0

---

## detune

### detune: number

**Description:**

Global detuning of all sounds in [cents](https://en.wikipedia.org/wiki/Cent_%28music%29).

The range of the value is -1200 to 1200, but we recommend setting it to [50](https://en.wikipedia.org/wiki/50_Cent).

**Inherits:** [Phaser.Sound.BaseSoundManager#detune](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L803](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L803)  
> Since: 3.0.0

---

## game

### game: [Phaser.Game](game.md)

**Description:**

Local reference to game.

**Inherits:** [Phaser.Sound.BaseSoundManager#game](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L44](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L44)  
> Since: 3.0.0

---

## gameLostFocus

### gameLostFocus: boolean

**Description:**

Flag used to track if the game has lost focus.

**Inherits:** [Phaser.Sound.BaseSoundManager#gameLostFocus](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L152](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L152)  
> Since: 3.60.0

---

## jsonCache

### jsonCache: [Phaser.Cache.BaseCache](cache-basecache.md)

**Description:**

Local reference to the JSON Cache, as used by Audio Sprites.

**Inherits:** [Phaser.Sound.BaseSoundManager#jsonCache](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L54)  
> Since: 3.7.0

---

## listenerPosition

### listenerPosition: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The Spatial Audio listener position.

Only available with WebAudio.

You can modify the x/y properties of this Vec2 directly to

adjust the listener position within the game world.

**Inherits:** [Phaser.Sound.BaseSoundManager#listenerPosition](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L162](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L162)  
> Since: 3.60.0

---

## locked

### locked: boolean

**Description:**

Mobile devices require sounds to be triggered from an explicit user action,

such as a tap, before any sound can be loaded/played on a web page.

Set to true if the audio system is currently locked awaiting user interaction.

**Inherits:** [Phaser.Sound.BaseSoundManager#locked](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L128](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L128)  
> Since: 3.0.0

---

## masterMuteNode

### masterMuteNode: GainNode

**Description:**

Gain node responsible for controlling global muting.

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L49](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L49)  
> Since: 3.0.0

---

## masterVolumeNode

### masterVolumeNode: GainNode

**Description:**

Gain node responsible for controlling global volume.

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L58](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L58)  
> Since: 3.0.0

---

## mute

### mute: boolean

**Overrides:** Phaser.Sound.BaseSoundManager#mute

**Fires:** [Phaser.Sound.Events#event:GLOBAL\_MUTE](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L471](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L471)  
> Since: 3.0.0

---

## pauseOnBlur

### pauseOnBlur: boolean

**Description:**

Flag indicating if sounds should be paused when game looses focus,

for instance when user switches to another tab/program/app.

**Inherits:** [Phaser.Sound.BaseSoundManager#pauseOnBlur](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L95](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L95)  
> Since: 3.0.0

---

## rate

### rate: number

**Description:**

Global playback rate at which all the sounds will be played.

Value of 1.0 plays the audio at full speed, 0.5 plays the audio at half speed

and 2.0 doubles the audio's playback speed.

**Inherits:** [Phaser.Sound.BaseSoundManager#rate](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L753](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L753)  
> Since: 3.0.0

---

## volume

### volume: number

**Overrides:** Phaser.Sound.BaseSoundManager#volume

**Fires:** [Phaser.Sound.Events#event:GLOBAL\_VOLUME](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L511](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L511)  
> Since: 3.0.0

---

# Private Members

## \_detune

### \_detune: number

**Description:**

Property that actually holds the value of global detune.

**Access:** private

**Inherits:** [Phaser.Sound.BaseSoundManager#\_detune](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L117](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L117)  
> Since: 3.0.0

---

## \_rate

### \_rate: number

**Description:**

Property that actually holds the value of global playback rate.

**Access:** private

**Inherits:** [Phaser.Sound.BaseSoundManager#\_rate](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L106)  
> Since: 3.0.0

---

## sounds

### sounds: Array.<[Phaser.Sound.BaseSound](sound-basesound.md)>

**Description:**

An array containing all added sounds.

**Access:** private

**Inherits:** [Phaser.Sound.BaseSoundManager#sounds](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L64)  
> Since: 3.0.0

---

## unlocked

### unlocked: boolean

**Description:**

Flag used internally for handling when the audio system

has been unlocked, if there ever was a need for it.

**Access:** private

**Inherits:** [Phaser.Sound.BaseSoundManager#unlocked](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L140)  
> Since: 3.0.0

---

# Public Methods

## add

### <instance> add(key, [config])

**Description:**

Adds a new sound into the sound manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | Asset key for the sound. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md) | Yes | An optional config object containing default sound settings. |

**Overrides:** Phaser.Sound.BaseSoundManager#add

**Returns:** [Phaser.Sound.WebAudioSound](sound-webaudiosound.md) - The new sound instance.

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L173](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L173)  
> Since: 3.0.0

---

## addAudioSprite

### <instance> addAudioSprite(key, [config])

**Description:**

Adds a new audio sprite sound into the sound manager.

Audio Sprites are a combination of audio files and a JSON configuration.

The JSON follows the format of that created by <https://github.com/tonistiigi/audiosprite>

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | Asset key for the sound. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md) | Yes | An optional config object containing default sound settings. |

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md), [Phaser.Sound.HTML5AudioSound](sound-html5audiosound.md), [Phaser.Sound.WebAudioSound](sound-webaudiosound.md) - The new audio sprite sound instance.

**Inherits:** [Phaser.Sound.BaseSoundManager#addAudioSprite](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L196](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L196)  
> Since: 3.0.0

---

## addListener

### <instance> addListener(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## createAudioContext

### <instance> createAudioContext(game)

**Description:**

Method responsible for instantiating and returning AudioContext instance.

If an instance of an AudioContext class was provided through the game config,

that instance will be returned instead. This can come in handy if you are reloading

a Phaser game on a page that never properly refreshes (such as in an SPA project)

and you want to reuse already instantiated AudioContext.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](game.md) | No | Reference to the current game instance. |
| --- | --- | --- | --- |

**Returns:** AudioContext - The AudioContext instance to be used for playback.

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L94](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L94)  
> Since: 3.0.0

---

## decodeAudio

### <instance> decodeAudio([audioKey], [audioData])

**Description:**

Decode audio data into a format ready for playback via Web Audio.

The audio data can be a base64 encoded string, an audio media-type data uri, or an ArrayBuffer instance.

The `audioKey` is the key that will be used to save the decoded audio to the audio cache.

Instead of passing a single entry you can instead pass an array of `Phaser.Types.Sound.DecodeAudioConfig`

objects as the first and only argument.

Decoding is an async process, so be sure to listen for the events to know when decoding has completed.

Once the audio has decoded it can be added to the Sound Manager or played via its key.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| audioKey | Array.<[Phaser.Types.Sound.DecodeAudioConfig](../typedef/types-sound.md)> | string | Yes | The string-based key to be used to reference the decoded audio in the audio cache, or an array of audio config objects. |
| --- | --- | --- | --- |
| audioData | ArrayBuffer | string | Yes | The audio data, either a base64 encoded string, an audio media-type data uri, or an ArrayBuffer instance. |

**Fires:** [Phaser.Sound.Events#event:DECODED](../event/sound-events.md), [Phaser.Sound.Events#event:DECODED\_ALL](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L193](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L193)  
> Since: 3.18.0

---

## destroy

### <instance> destroy()

**Description:**

Calls Phaser.Sound.BaseSoundManager#destroy method

and cleans up all Web Audio API related stuff.

**Overrides:** Phaser.Sound.BaseSoundManager#destroy

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L421](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L421)  
> Since: 3.0.0

---

## emit

### <instance> emit(event, [args])

**Description:**

Calls each of the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| args | \* | Yes | Additional arguments that will be passed to the event handler. |

**Returns:** boolean - `true` if the event had listeners, else `false`.

**Inherits:** [Phaser.Events.EventEmitter#emit](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L86)  
> Since: 3.0.0

---

## eventNames

### <instance> eventNames()

**Description:**

Return an array listing the events for which the emitter has registered listeners.

**Returns:** Array.<(string | symbol)> - undefined

**Inherits:** [Phaser.Events.EventEmitter#eventNames](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L55)  
> Since: 3.0.0

---

## get

### <instance> get(key)

**Description:**

Gets the first sound in this Sound Manager that matches the given key.

If none can be found it returns `null`.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | Sound asset key. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Sound.BaseSound](sound-basesound.md) - - The sound, or null.

**Inherits:** [Phaser.Sound.BaseSoundManager#get](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L241](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L241)  
> Since: 3.23.0

---

## getAll

### <instance> getAll([key])

**Description:**

Gets all sounds in this Sound Manager.

You can optionally specify a key, in which case only Sound instances that match the given key

will be returned.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | Yes | Optional asset key. If given, only Sound instances with this key will be returned. |
| --- | --- | --- | --- |

**Returns:** Array.<[Phaser.Sound.BaseSound](sound-basesound.md)> - - The sounds, or an empty array.

**Inherits:** [Phaser.Sound.BaseSoundManager#getAll](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L260](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L260)  
> Since: 3.23.0

---

## getAllPlaying

### <instance> getAllPlaying()

**Description:**

Returns all sounds from this Sound Manager that are currently

playing. That is, Sound instances that have their `isPlaying`

property set to `true`.

**Tags:**

* generic
* genericUse

**Returns:** Array.<[Phaser.Sound.BaseSound](sound-basesound.md)> - - All currently playing sounds, or an empty array.

**Inherits:** [Phaser.Sound.BaseSoundManager#getAllPlaying](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L288](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L288)  
> Since: 3.60.0

---

## isPlaying

### <instance> isPlaying(key)

**Description:**

When a key is given, returns true if any sound with that key is playing.

When no key is given, returns true if any sound is playing.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | Sound asset key. |
| --- | --- | --- | --- |

**Returns:** boolean - - Per the key argument, true if any matching sound is playing, otherwise false.

**Inherits:** [Phaser.Sound.BaseSoundManager#isPlaying](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L536](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L536)  
> Since: 3.85.0

---

## listenerCount

### <instance> listenerCount(event)

**Description:**

Return the number of listeners listening to a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** number - The number of listeners.

**Inherits:** [Phaser.Events.EventEmitter#listenerCount](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L75)  
> Since: 3.0.0

---

## listeners

### <instance> listeners(event)

**Description:**

Return the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** Array.<function()> - The registered listeners.

**Inherits:** [Phaser.Events.EventEmitter#listeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L64)  
> Since: 3.0.0

---

## off

### <instance> off(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#off](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L151)  
> Since: 3.0.0

---

## on

### <instance> on(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#on](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L98)  
> Since: 3.0.0

---

## onBlur

### <instance> onBlur()

**Description:**

Method used internally for pausing sound manager if

Phaser.Sound.WebAudioSoundManager#pauseOnBlur is set to true.

**Access:** protected

**Overrides:** Phaser.Sound.BaseSoundManager#onBlur

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L346](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L346)  
> Since: 3.0.0

---

## once

### <instance> once(event, fn, [context])

**Description:**

Add a one-time listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## onFocus

### <instance> onFocus()

**Description:**

Method used internally for resuming sound manager if

Phaser.Sound.WebAudioSoundManager#pauseOnBlur is set to true.

**Access:** protected

**Overrides:** Phaser.Sound.BaseSoundManager#onFocus

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L362](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L362)  
> Since: 3.0.0

---

## pauseAll

### <instance> pauseAll()

**Description:**

Pauses all the sounds in the game.

**Fires:** [Phaser.Sound.Events#event:PAUSE\_ALL](../event/sound-events.md)

**Inherits:** [Phaser.Sound.BaseSoundManager#pauseAll](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L446](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L446)  
> Since: 3.0.0

---

## play

### <instance> play(key, [extra])

**Description:**

Adds a new sound to the sound manager and plays it.

The sound will be automatically removed (destroyed) once playback ends.

This lets you play a new sound on the fly without the need to keep a reference to it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | Asset key for the sound. |
| --- | --- | --- | --- |
| extra | [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md) | [Phaser.Types.Sound.SoundMarker](../typedef/types-sound.md) | Yes | An optional additional object containing settings to be applied to the sound. It could be either config or marker object. |

**Returns:** boolean - Whether the sound started playing successfully.

**Inherits:** [Phaser.Sound.BaseSoundManager#play](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L306](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L306)  
> Since: 3.0.0

---

## playAudioSprite

### <instance> playAudioSprite(key, spriteName, [config])

**Description:**

Adds a new audio sprite sound to the sound manager and plays it.

The sprite will be automatically removed (destroyed) once playback ends.

This lets you play a new sound on the fly without the need to keep a reference to it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | Asset key for the sound. |
| --- | --- | --- | --- |
| spriteName | string | No | The name of the sound sprite to play. |
| config | [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md) | Yes | An optional config object containing default sound settings. |

**Returns:** boolean - Whether the audio sprite sound started playing successfully.

**Inherits:** [Phaser.Sound.BaseSoundManager#playAudioSprite](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L347](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L347)  
> Since: 3.0.0

---

## remove

### <instance> remove(sound)

**Description:**

Removes a sound from the sound manager.

The removed sound is destroyed before removal.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.BaseSound](sound-basesound.md) | No | The sound object to remove. |
| --- | --- | --- | --- |

**Returns:** boolean - True if the sound was removed successfully, otherwise false.

**Inherits:** [Phaser.Sound.BaseSoundManager#remove](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L371](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L371)  
> Since: 3.0.0

---

## removeAll

### <instance> removeAll()

**Description:**

Removes all sounds from the manager, destroying the sounds.

**Inherits:** [Phaser.Sound.BaseSoundManager#removeAll](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L398](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L398)  
> Since: 3.23.0

---

## removeAllListeners

### <instance> removeAllListeners([event])

**Description:**

Remove all listeners, or those of the specified event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | Yes | The event name. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeByKey

### <instance> removeByKey(key)

**Description:**

Removes all sounds from the sound manager that have an asset key matching the given value.

The removed sounds are destroyed before removal.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key to match when removing sound objects. |
| --- | --- | --- | --- |

**Returns:** number - The number of matching sound objects that were removed.

**Inherits:** [Phaser.Sound.BaseSoundManager#removeByKey](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L414](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L414)  
> Since: 3.0.0

---

## removeListener

### <instance> removeListener(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## resumeAll

### <instance> resumeAll()

**Description:**

Resumes all the sounds in the game.

**Fires:** [Phaser.Sound.Events#event:RESUME\_ALL](../event/sound-events.md)

**Inherits:** [Phaser.Sound.BaseSoundManager#resumeAll](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L463](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L463)  
> Since: 3.0.0

---

## setAudioContext

### <instance> setAudioContext(context)

**Description:**

This method takes a new AudioContext reference and then sets

this Sound Manager to use that context for all playback.

As part of this call it also disconnects the master mute and volume

nodes and then re-creates them on the new given context.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| context | AudioContext | No | Reference to an already created AudioContext instance. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md) - The WebAudioSoundManager instance.

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L129)  
> Since: 3.21.0

---

## setDetune

### <instance> setDetune(value)

**Description:**

Sets the global detuning of all sounds in [cents](https://en.wikipedia.org/wiki/Cent_%28music%29).

The range of the value is -1200 to 1200, but we recommend setting it to [50](https://en.wikipedia.org/wiki/50_Cent).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The range of the value is -1200 to 1200, but we recommend setting it to [50](https://en.wikipedia.org/wiki/50_Cent). |
| --- | --- | --- | --- |

**Returns:** [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md) - This Sound Manager.

**Fires:** [Phaser.Sound.Events#event:GLOBAL\_DETUNE](../event/sound-events.md)

**Inherits:** [Phaser.Sound.BaseSoundManager#setDetune](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L784](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L784)  
> Since: 3.3.0

---

## setListenerPosition

### <instance> setListenerPosition([x], [y])

**Description:**

Sets the X and Y position of the Spatial Audio listener on this Web Audios context.

If you call this method with no parameters it will default to the center-point of

the game canvas. Depending on the type of game you're making, you may need to call

this method constantly to reset the listener position as the camera scrolls.

Calling this method does nothing on HTML5Audio.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | Yes | The x position of the Spatial Audio listener. |
| --- | --- | --- | --- |
| y | number | Yes | The y position of the Spatial Audio listener. |

**Overrides:** Phaser.Sound.BaseSoundManager#setListenerPosition

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L274](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L274)  
> Since: 3.60.0

---

## setMute

### <instance> setMute(value)

**Description:**

Sets the muted state of all this Sound Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | `true` to mute all sounds, `false` to unmute them. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md) - This Sound Manager.

**Fires:** [Phaser.Sound.Events#event:GLOBAL\_MUTE](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L453](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L453)  
> Since: 3.3.0

---

## setRate

### <instance> setRate(value)

**Description:**

Sets the global playback rate at which all the sounds will be played.

For example, a value of 1.0 plays the audio at full speed, 0.5 plays the audio at half speed

and 2.0 doubles the audios playback speed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | Global playback rate at which all the sounds will be played. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md) - This Sound Manager.

**Fires:** [Phaser.Sound.Events#event:GLOBAL\_RATE](../event/sound-events.md)

**Inherits:** [Phaser.Sound.BaseSoundManager#setRate](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L732](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L732)  
> Since: 3.3.0

---

## setVolume

### <instance> setVolume(value)

**Description:**

Sets the volume of this Sound Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The global volume of this Sound Manager. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md) - This Sound Manager.

**Fires:** [Phaser.Sound.Events#event:GLOBAL\_VOLUME](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L493](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L493)  
> Since: 3.3.0

---

## shutdown

### <instance> shutdown()

**Description:**

Removes all listeners.

**Inherits:** [Phaser.Events.EventEmitter#shutdown](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L31)  
> Since: 3.0.0

---

## stopAll

### <instance> stopAll()

**Description:**

Stops all the sounds in the game.

**Fires:** [Phaser.Sound.Events#event:STOP\_ALL](../event/sound-events.md)

**Inherits:** [Phaser.Sound.BaseSoundManager#stopAll](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L497](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L497)  
> Since: 3.0.0

---

## stopByKey

### <instance> stopByKey(key)

**Description:**

Stops any sounds matching the given key.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | Sound asset key. |
| --- | --- | --- | --- |

**Returns:** number - - How many sounds were stopped.

**Inherits:** [Phaser.Sound.BaseSoundManager#stopByKey](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L514](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L514)  
> Since: 3.23.0

---

## unlock

### <instance> unlock()

**Description:**

Unlocks Web Audio API on the initial input event.

Read more about how this issue is handled here in [this article](https://medium.com/@pgoloskokovic/unlocking-web-audio-the-smarter-way-8858218c0e09).

**Overrides:** Phaser.Sound.BaseSoundManager#unlock

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L299](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L299)  
> Since: 3.0.0

---

## update

### <instance> update(time, delta)

**Description:**

Update method called on every game step.

Removes destroyed sounds and updates every active sound in the game.

**Access:** protected

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current timestamp as generated by the Request Animation Frame or SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time elapsed since the last frame. |

**Overrides:** Phaser.Sound.BaseSoundManager#update

**Fires:** [Phaser.Sound.Events#event:UNLOCKED](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSoundManager.js#L380](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSoundManager.js#L380)  
> Since: 3.0.0

---

# Private Methods

## forEachActiveSound

### <instance> forEachActiveSound(callback, [scope])

**Description:**

Method used internally for iterating only over active sounds and skipping sounds that are marked for removal.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | [Phaser.Types.Sound.EachActiveSoundCallback](../typedef/types-sound.md) | No | Callback function. (manager: Phaser.Sound.BaseSoundManager, sound: Phaser.Sound.BaseSound, index: number, sounds: Phaser.Manager.BaseSound[]) => void |
| --- | --- | --- | --- |
| scope | \* | Yes | Callback context. |

**Inherits:** [Phaser.Sound.BaseSoundManager#forEachActiveSound](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L709](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L709)  
> Since: 3.0.0

---

## onGameBlur

### <instance> onGameBlur()

**Description:**

Internal handler for Phaser.Core.Events#BLUR.

**Access:** private

**Inherits:** [Phaser.Sound.BaseSoundManager#onGameBlur](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L617](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L617)  
> Since: 3.23.0

---

## onGameFocus

### <instance> onGameFocus()

**Description:**

Internal handler for Phaser.Core.Events#FOCUS.

**Access:** private

**Inherits:** [Phaser.Sound.BaseSoundManager#onGameFocus](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L634](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L634)  
> Since: 3.23.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [context](#context)

    - [context: AudioContext](#context-audiocontext)
  + [destination](#destination)

    - [destination: AudioNode](#destination-audionode)
  + [detune](#detune)

    - [detune: number](#detune-number)
  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [gameLostFocus](#gamelostfocus)

    - [gameLostFocus: boolean](#gamelostfocus-boolean)
  + [jsonCache](#jsoncache)

    - [jsonCache: Phaser.Cache.BaseCache](#jsoncache-phasercachebasecache)
  + [listenerPosition](#listenerposition)

    - [listenerPosition: Phaser.Math.Vector2](#listenerposition-phasermathvector2)
  + [locked](#locked)

    - [locked: boolean](#locked-boolean)
  + [masterMuteNode](#mastermutenode)

    - [masterMuteNode: GainNode](#mastermutenode-gainnode)
  + [masterVolumeNode](#mastervolumenode)

    - [masterVolumeNode: GainNode](#mastervolumenode-gainnode)
  + [mute](#mute)

    - [mute: boolean](#mute-boolean)
  + [pauseOnBlur](#pauseonblur)

    - [pauseOnBlur: boolean](#pauseonblur-boolean)
  + [rate](#rate)

    - [rate: number](#rate-number)
  + [volume](#volume)

    - [volume: number](#volume-number)
* [Private Members](#private-members)

  + [\_detune](#_detune)

    - [\_detune: number](#_detune-number)
  + [\_rate](#_rate)

    - [\_rate: number](#_rate-number)
  + [sounds](#sounds)

    - [sounds: Array.<Phaser.Sound.BaseSound>](#sounds-arrayphasersoundbasesound)
  + [unlocked](#unlocked)

    - [unlocked: boolean](#unlocked-boolean)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(key, [config])](#instance-addkey-config)
  + [addAudioSprite](#addaudiosprite)

    - [<instance> addAudioSprite(key, [config])](#instance-addaudiospritekey-config)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [createAudioContext](#createaudiocontext)

    - [<instance> createAudioContext(game)](#instance-createaudiocontextgame)
  + [decodeAudio](#decodeaudio)

    - [<instance> decodeAudio([audioKey], [audioData])](#instance-decodeaudioaudiokey-audiodata)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [get](#get)

    - [<instance> get(key)](#instance-getkey)
  + [getAll](#getall)

    - [<instance> getAll([key])](#instance-getallkey)
  + [getAllPlaying](#getallplaying)

    - [<instance> getAllPlaying()](#instance-getallplaying)
  + [isPlaying](#isplaying)

    - [<instance> isPlaying(key)](#instance-isplayingkey)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [onBlur](#onblur)

    - [<instance> onBlur()](#instance-onblur)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [onFocus](#onfocus)

    - [<instance> onFocus()](#instance-onfocus)
  + [pauseAll](#pauseall)

    - [<instance> pauseAll()](#instance-pauseall)
  + [play](#play)

    - [<instance> play(key, [extra])](#instance-playkey-extra)
  + [playAudioSprite](#playaudiosprite)

    - [<instance> playAudioSprite(key, spriteName, [config])](#instance-playaudiospritekey-spritename-config)
  + [remove](#remove)

    - [<instance> remove(sound)](#instance-removesound)
  + [removeAll](#removeall)

    - [<instance> removeAll()](#instance-removeall)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeByKey](#removebykey)

    - [<instance> removeByKey(key)](#instance-removebykeykey)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [resumeAll](#resumeall)

    - [<instance> resumeAll()](#instance-resumeall)
  + [setAudioContext](#setaudiocontext)

    - [<instance> setAudioContext(context)](#instance-setaudiocontextcontext)
  + [setDetune](#setdetune)

    - [<instance> setDetune(value)](#instance-setdetunevalue)
  + [setListenerPosition](#setlistenerposition)

    - [<instance> setListenerPosition([x], [y])](#instance-setlistenerpositionx-y)
  + [setMute](#setmute)

    - [<instance> setMute(value)](#instance-setmutevalue)
  + [setRate](#setrate)

    - [<instance> setRate(value)](#instance-setratevalue)
  + [setVolume](#setvolume)

    - [<instance> setVolume(value)](#instance-setvolumevalue)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [stopAll](#stopall)

    - [<instance> stopAll()](#instance-stopall)
  + [stopByKey](#stopbykey)

    - [<instance> stopByKey(key)](#instance-stopbykeykey)
  + [unlock](#unlock)

    - [<instance> unlock()](#instance-unlock)
  + [update](#update)

    - [<instance> update(time, delta)](#instance-updatetime-delta)
* [Private Methods](#private-methods)

  + [forEachActiveSound](#foreachactivesound)

    - [<instance> forEachActiveSound(callback, [scope])](#instance-foreachactivesoundcallback-scope)
  + [onGameBlur](#ongameblur)

    - [<instance> onGameBlur()](#instance-ongameblur)
  + [onGameFocus](#ongamefocus)

    - [<instance> onGameFocus()](#instance-ongamefocus)

Back to top

©2025[Phaser](https://docs.phaser.io)