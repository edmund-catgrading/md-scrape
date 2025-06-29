# WebAudioSound

Phaser.Sound.WebAudioSound

Web Audio API implementation of the sound.

**Constructor**

`new WebAudioSound(manager, key, [config])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| manager | [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md) | No |  | Reference to the WebAudio Sound Manager that owns this Sound instance. |
| --- | --- | --- | --- | --- |
| key | string | No |  | Asset key for the sound. |
| config | [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md) | Yes | "{}" | An optional config object containing default sound settings. |

---

**Scope**: static

**Extends**

> [Phaser.Sound.BaseSound](sound-basesound.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L13)  
> Since: 3.0.0

# Public Members

## audioBuffer

### audioBuffer: AudioBuffer

**Description:**

Audio buffer containing decoded data of the audio asset to be played.

> Source: [src/sound/webaudio/WebAudioSound.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L37)  
> Since: 3.0.0

---

## currentMarker

### currentMarker: [Phaser.Types.Sound.SoundMarker](../typedef/types-sound.md)

**Description:**

Currently playing marker.

'null' if whole sound is playing.

**Inherits:** [Phaser.Sound.BaseSound#currentMarker](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L159)  
> Since: 3.0.0

---

## detune

### detune: number

**Description:**

The detune value of this Sound, given in [cents](https://en.wikipedia.org/wiki/Cent_%28music%29).

The range of the value is -1200 to 1200, but we recommend setting it to [50](https://en.wikipedia.org/wiki/50_Cent).

**Fires:** [Phaser.Sound.Events#event:DETUNE](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L828](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L828)  
> Since: 3.0.0

---

## duration

### duration: number

**Description:**

A value representing the duration, in seconds.

It could be total sound duration or a marker duration.

**Inherits:** [Phaser.Sound.BaseSound#duration](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L92)  
> Since: 3.0.0

---

## hasEnded

### hasEnded: boolean

**Description:**

Used for keeping track when sound source playback has ended

so its state can be updated accordingly.

> Source: [src/sound/webaudio/WebAudioSound.js#L174](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L174)  
> Since: 3.0.0

---

## hasLooped

### hasLooped: boolean

**Description:**

Used for keeping track when sound source has looped

so its state can be updated accordingly.

> Source: [src/sound/webaudio/WebAudioSound.js#L186](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L186)  
> Since: 3.0.0

---

## isPaused

### isPaused: boolean

**Description:**

Flag indicating if sound is currently paused.

**Inherits:** [Phaser.Sound.BaseSound#isPaused](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L68)  
> Since: 3.0.0

---

## isPlaying

### isPlaying: boolean

**Description:**

Flag indicating if sound is currently playing.

**Inherits:** [Phaser.Sound.BaseSound#isPlaying](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L57](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L57)  
> Since: 3.0.0

---

## key

### key: string

**Description:**

Asset key for the sound.

**Inherits:** [Phaser.Sound.BaseSound#key](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L47)  
> Since: 3.0.0

---

## loop

### loop: boolean

**Description:**

Flag indicating whether or not the sound or current sound marker will loop.

**Fires:** [Phaser.Sound.Events#event:LOOP](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L1039](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L1039)  
> Since: 3.0.0

---

## loopSource

### loopSource: AudioBufferSourceNode

**Description:**

A reference to a second audio source used for gapless looped playback.

> Source: [src/sound/webaudio/WebAudioSound.js#L62](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L62)  
> Since: 3.0.0

---

## loopTime

### loopTime: number

**Description:**

The time at which the sound loop source should actually start playback.

Based on `BaseAudioContext.currentTime` value.

> Source: [src/sound/webaudio/WebAudioSound.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L148)  
> Since: 3.0.0

---

## manager

### manager: [Phaser.Sound.BaseSoundManager](sound-basesoundmanager.md)

**Description:**

Local reference to the sound manager.

**Inherits:** [Phaser.Sound.BaseSound#manager](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L38)  
> Since: 3.0.0

---

## markers

### markers: Object.<string, [Phaser.Types.Sound.SoundMarker](../typedef/types-sound.md)>

**Description:**

Object containing markers definitions.

**Inherits:** [Phaser.Sound.BaseSound#markers](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L148)  
> Since: 3.0.0

---

## mute

### mute: boolean

**Description:**

Boolean indicating whether the sound is muted or not.

Gets or sets the muted state of this sound.

**Fires:** [Phaser.Sound.Events#event:MUTE](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L875](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L875)  
> Since: 3.0.0

---

## muteNode

### muteNode: GainNode

**Description:**

Gain node responsible for controlling this sound's muting.

> Source: [src/sound/webaudio/WebAudioSound.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L72)  
> Since: 3.0.0

---

## pan

### pan: number

**Description:**

Gets or sets the pan of this sound, a value between -1 (full left pan) and 1 (full right pan).

Always returns zero on iOS / Safari as it doesn't support the stereo panner node.

**Fires:** [Phaser.Sound.Events#event:PAN](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L1091](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L1091)  
> Since: 3.50.0

---

## pannerNode

### pannerNode: StereoPannerNode

**Description:**

Panner node responsible for controlling this sound's pan.

Doesn't work on iOS / Safari.

> Source: [src/sound/webaudio/WebAudioSound.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L90)  
> Since: 3.50.0

---

## pendingRemove

### pendingRemove: boolean

**Description:**

Flag indicating if destroy method was called on this sound.

**Inherits:** [Phaser.Sound.BaseSound#pendingRemove](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L171](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L171)  
> Since: 3.0.0

---

## playTime

### playTime: number

**Description:**

The time at which the sound should have started playback from the beginning.

Treat this property as read-only.

Based on `BaseAudioContext.currentTime` value.

> Source: [src/sound/webaudio/WebAudioSound.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L120)  
> Since: 3.0.0

---

## rate

### rate: number

**Description:**

Rate at which this Sound will be played.

Value of 1.0 plays the audio at full speed, 0.5 plays the audio at half speed

and 2.0 doubles the audios playback speed.

**Fires:** [Phaser.Sound.Events#event:RATE](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L778](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L778)  
> Since: 3.0.0

---

## rateUpdates

### rateUpdates: array

**Description:**

An array where we keep track of all rate updates during playback.

Treat this property as read-only.

Array of object types: `{ time: number, rate: number }`

> Source: [src/sound/webaudio/WebAudioSound.js#L160](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L160)  
> Since: 3.0.0

---

## seek

### seek: number

**Description:**

Property representing the position of playback for this sound, in seconds.

Setting it to a specific value moves current playback to that position.

The value given is clamped to the range 0 to current marker duration.

Setting seek of a stopped sound has no effect.

**Fires:** [Phaser.Sound.Events#event:SEEK](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L963](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L963)  
> Since: 3.0.0

---

## source

### source: AudioBufferSourceNode

**Description:**

A reference to an audio source node used for playing back audio from

audio data stored in Phaser.Sound.WebAudioSound#audioBuffer.

> Source: [src/sound/webaudio/WebAudioSound.js#L51](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L51)  
> Since: 3.0.0

---

## spatialNode

### spatialNode: PannerNode

**Description:**

The Stereo Spatial Panner node.

> Source: [src/sound/webaudio/WebAudioSound.js#L101](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L101)  
> Since: 3.60.0

---

## spatialSource

### spatialSource: [Phaser.Types.Math.Vector2Like](../typedef/types-math.md)

**Description:**

If the Spatial Panner node has been set to track a vector or

Game Object, this retains a reference to it.

> Source: [src/sound/webaudio/WebAudioSound.js#L110](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L110)  
> Since: 3.60.0

---

## startTime

### startTime: number

**Description:**

The time at which the sound source should have actually started playback.

Treat this property as read-only.

Based on `BaseAudioContext.currentTime` value.

> Source: [src/sound/webaudio/WebAudioSound.js#L134](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L134)  
> Since: 3.0.0

---

## totalDuration

### totalDuration: number

**Description:**

The total duration of the sound in seconds.

**Inherits:** [Phaser.Sound.BaseSound#totalDuration](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L103)  
> Since: 3.0.0

---

## totalRate

### totalRate: number

**Description:**

A property that holds the value of sound's actual playback rate,

after its rate and detune values has been combined with global

rate and detune values.

**Inherits:** [Phaser.Sound.BaseSound#totalRate](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L79)  
> Since: 3.0.0

---

## volume

### volume: number

**Description:**

Gets or sets the volume of this sound, a value between 0 (silence) and 1 (full volume).

**Fires:** [Phaser.Sound.Events#event:VOLUME](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L920](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L920)  
> Since: 3.0.0

---

## volumeNode

### volumeNode: GainNode

**Description:**

Gain node responsible for controlling this sound's volume.

> Source: [src/sound/webaudio/WebAudioSound.js#L81](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L81)  
> Since: 3.0.0

---

## x

### x: number

**Description:**

Sets the x position of this Sound in Spatial Audio space.

This only has any effect if the sound was created with a SpatialSoundConfig object.

Also see the `WebAudioSoundManager.setListenerPosition` method.

If you find that the sound becomes too quiet, too quickly, as it moves away from

the listener, then try different `refDistance` property values when configuring

the spatial sound.

> Source: [src/sound/webaudio/WebAudioSound.js#L528](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L528)  
> Since: 3.60.0

---

## y

### y: number

**Description:**

Sets the y position of this Sound in Spatial Audio space.

This only has any effect if the sound was created with a SpatialSoundConfig object.

Also see the `WebAudioSoundManager.setListenerPosition` method.

If you find that the sound becomes too quiet, too quickly, as it moves away from

the listener, then try different `refDistance` property values when configuring

the spatial sound.

> Source: [src/sound/webaudio/WebAudioSound.js#L566](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L566)  
> Since: 3.60.0

---

# Private Members

## config

### config: [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md)

**Description:**

A config object used to store default sound settings' values.

Default values will be set by properties' setters.

**Access:** private

**Inherits:** [Phaser.Sound.BaseSound#config](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L113)  
> Since: 3.0.0

---

## currentConfig

### currentConfig: [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md)

**Description:**

Reference to the currently used config.

It could be default config or marker config.

**Access:** private

**Inherits:** [Phaser.Sound.BaseSound#currentConfig](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L135](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L135)  
> Since: 3.0.0

---

# Public Methods

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

**Returns:** [Phaser.Sound.WebAudioSound](sound-webaudiosound.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## addMarker

### <instance> addMarker(marker)

**Description:**

Adds a marker into the current sound. A marker is represented by name, start time, duration, and optionally config object.

This allows you to bundle multiple sounds together into a single audio file and use markers to jump between them for playback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| marker | [Phaser.Types.Sound.SoundMarker](../typedef/types-sound.md) | No | Marker object. |
| --- | --- | --- | --- |

**Returns:** boolean - Whether the marker was added successfully.

**Inherits:** [Phaser.Sound.BaseSound#addMarker](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L182](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L182)  
> Since: 3.0.0

---

## applyConfig

### <instance> applyConfig()

**Description:**

Method used internally for applying config values to some of the sound properties.

**Overrides:** Phaser.Sound.BaseSound#applyConfig

> Source: [src/sound/webaudio/WebAudioSound.js#L482](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L482)  
> Since: 3.0.0

---

## calculateRate

### <instance> calculateRate()

**Description:**

Method used internally to calculate total playback rate of the sound.

**Overrides:** Phaser.Sound.BaseSound#calculateRate

> Source: [src/sound/webaudio/WebAudioSound.js#L696](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L696)  
> Since: 3.0.0

---

## createAndStartLoopBufferSource

### <instance> createAndStartLoopBufferSource()

**Description:**

This method is only used internally and it creates a looping buffer source.

> Source: [src/sound/webaudio/WebAudioSound.js#L381](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L381)  
> Since: 3.0.0

---

## createBufferSource

### <instance> createBufferSource()

**Description:**

This method is only used internally and it creates a buffer source.

**Returns:** AudioBufferSourceNode - undefined

> Source: [src/sound/webaudio/WebAudioSound.js#L399](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L399)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Calls Phaser.Sound.BaseSound#destroy method

and cleans up all Web Audio API related stuff.

**Overrides:** Phaser.Sound.BaseSound#destroy

> Source: [src/sound/webaudio/WebAudioSound.js#L656](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L656)  
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

## getCurrentTime

### <instance> getCurrentTime()

**Description:**

Method used internally for calculating current playback time of a playing sound.

> Source: [src/sound/webaudio/WebAudioSound.js#L728](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L728)  
> Since: 3.0.0

---

## getLoopTime

### <instance> getLoopTime()

**Description:**

Method used internally for calculating the time

at witch the loop source should start playing.

> Source: [src/sound/webaudio/WebAudioSound.js#L757](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L757)  
> Since: 3.0.0

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

**Returns:** [Phaser.Sound.WebAudioSound](sound-webaudiosound.md) - `this`.

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

**Returns:** [Phaser.Sound.WebAudioSound](sound-webaudiosound.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#on](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L98)  
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

**Returns:** [Phaser.Sound.WebAudioSound](sound-webaudiosound.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## pause

### <instance> pause()

**Description:**

Pauses the sound.

**Overrides:** Phaser.Sound.BaseSound#pause

**Returns:** boolean - Whether the sound was paused successfully.

**Fires:** [Phaser.Sound.Events#event:PAUSE](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L272](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L272)  
> Since: 3.0.0

---

## play

### <instance> play([markerName], [config])

**Description:**

Play this sound, or a marked section of it.

It always plays the sound from the start. If you want to start playback from a specific time

you can set 'seek' setting of the config object, provided to this call, to that value.

If you want to play the same sound simultaneously, then you need to create another instance

of it and play that Sound.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| markerName | string | [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md) | Yes | "''" | If you want to play a marker then provide the marker name here. Alternatively, this parameter can be a SoundConfig object. |
| --- | --- | --- | --- | --- |
| config | [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md) | Yes |  | Optional sound config object to be applied to this marker or entire sound if no marker name is provided. It gets memorized for future plays of current section of the sound. |

**Overrides:** Phaser.Sound.BaseSound#play

**Returns:** boolean - Whether the sound started playing successfully.

**Fires:** [Phaser.Sound.Events#event:PLAY](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L238](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L238)  
> Since: 3.0.0

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

**Returns:** [Phaser.Sound.WebAudioSound](sound-webaudiosound.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
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

**Returns:** [Phaser.Sound.WebAudioSound](sound-webaudiosound.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## removeMarker

### <instance> removeMarker(markerName)

**Description:**

Removes a marker from the sound.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| markerName | string | No | The name of the marker to remove. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Sound.SoundMarker](../typedef/types-sound.md) - Removed marker object or 'null' if there was no marker with provided name.

**Inherits:** [Phaser.Sound.BaseSound#removeMarker](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L259](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L259)  
> Since: 3.0.0

---

## resetConfig

### <instance> resetConfig()

**Description:**

Method used internally for resetting values of some of the config properties.

**Inherits:** [Phaser.Sound.BaseSound#resetConfig](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L428](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L428)  
> Since: 3.0.0

---

## resume

### <instance> resume()

**Description:**

Resumes the sound.

**Overrides:** Phaser.Sound.BaseSound#resume

**Returns:** boolean - Whether the sound was resumed successfully.

**Fires:** [Phaser.Sound.Events#event:RESUME](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L302](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L302)  
> Since: 3.0.0

---

## setDetune

### <instance> setDetune(value)

**Description:**

Sets the detune value of this Sound, given in [cents](https://en.wikipedia.org/wiki/Cent_%28music%29).

The range of the value is -1200 to 1200, but we recommend setting it to [50](https://en.wikipedia.org/wiki/50_Cent).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The range of the value is -1200 to 1200, but we recommend setting it to [50](https://en.wikipedia.org/wiki/50_Cent). |
| --- | --- | --- | --- |

**Returns:** [Phaser.Sound.WebAudioSound](sound-webaudiosound.md) - This Sound instance.

**Fires:** [Phaser.Sound.Events#event:DETUNE](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L856](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L856)  
> Since: 3.3.0

---

## setLoop

### <instance> setLoop(value)

**Description:**

Sets the loop state of this Sound.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | `true` to loop this sound, `false` to not loop it. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Sound.WebAudioSound](sound-webaudiosound.md) - This Sound instance.

**Fires:** [Phaser.Sound.Events#event:LOOP](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L1073](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L1073)  
> Since: 3.4.0

---

## setMute

### <instance> setMute(value)

**Description:**

Sets the muted state of this Sound.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | `true` to mute this sound, `false` to unmute it. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Sound.WebAudioSound](sound-webaudiosound.md) - This Sound instance.

**Fires:** [Phaser.Sound.Events#event:MUTE](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L902](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L902)  
> Since: 3.4.0

---

## setPan

### <instance> setPan(value)

**Description:**

Sets the pan of this sound, a value between -1 (full left pan) and 1 (full right pan).

Note: iOS / Safari doesn't support the stereo panner node.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The pan of the sound. A value between -1 (full left pan) and 1 (full right pan). |
| --- | --- | --- | --- |

**Returns:** [Phaser.Sound.WebAudioSound](sound-webaudiosound.md) - This Sound instance.

**Fires:** [Phaser.Sound.Events#event:PAN](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L1129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L1129)  
> Since: 3.50.0

---

## setRate

### <instance> setRate(value)

**Description:**

Sets the playback rate of this Sound.

For example, a value of 1.0 plays the audio at full speed, 0.5 plays the audio at half speed

and 2.0 doubles the audios playback speed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The playback rate at of this Sound. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Sound.WebAudioSound](sound-webaudiosound.md) - This Sound instance.

**Fires:** [Phaser.Sound.Events#event:RATE](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L807](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L807)  
> Since: 3.3.0

---

## setSeek

### <instance> setSeek(value)

**Description:**

Seeks to a specific point in this sound.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The point in the sound to seek to. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Sound.WebAudioSound](sound-webaudiosound.md) - This Sound instance.

**Fires:** [Phaser.Sound.Events#event:SEEK](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L1021](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L1021)  
> Since: 3.4.0

---

## setVolume

### <instance> setVolume(value)

**Description:**

Sets the volume of this Sound.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The volume of the sound. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Sound.WebAudioSound](sound-webaudiosound.md) - This Sound instance.

**Fires:** [Phaser.Sound.Events#event:VOLUME](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L945](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L945)  
> Since: 3.4.0

---

## shutdown

### <instance> shutdown()

**Description:**

Removes all listeners.

**Inherits:** [Phaser.Events.EventEmitter#shutdown](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L31)  
> Since: 3.0.0

---

## stop

### <instance> stop()

**Description:**

Stop playing this sound.

**Overrides:** Phaser.Sound.BaseSound#stop

**Returns:** boolean - Whether the sound was stopped successfully.

**Fires:** [Phaser.Sound.Events#event:STOP](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L331](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L331)  
> Since: 3.0.0

---

## stopAndRemoveBufferSource

### <instance> stopAndRemoveBufferSource()

**Description:**

This method is only used internally and it stops and removes a buffer source.

> Source: [src/sound/webaudio/WebAudioSound.js#L439](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L439)  
> Since: 3.0.0

---

## stopAndRemoveLoopBufferSource

### <instance> stopAndRemoveLoopBufferSource()

**Description:**

This method is only used internally and it stops and removes a looping buffer source.

> Source: [src/sound/webaudio/WebAudioSound.js#L464](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L464)  
> Since: 3.0.0

---

## update

### <instance> update()

**Description:**

Update method called automatically by sound manager on every game step.

**Overrides:** Phaser.Sound.BaseSound#update

**Fires:** [Phaser.Sound.Events#event:COMPLETE](../event/sound-events.md), [Phaser.Sound.Events#event:LOOPED](../event/sound-events.md)

> Source: [src/sound/webaudio/WebAudioSound.js#L604](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L604)  
> Since: 3.0.0

---

## updateMarker

### <instance> updateMarker(marker)

**Description:**

Updates previously added marker.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| marker | [Phaser.Types.Sound.SoundMarker](../typedef/types-sound.md) | No | Marker object with updated values. |
| --- | --- | --- | --- |

**Returns:** boolean - Whether the marker was updated successfully.

**Inherits:** [Phaser.Sound.BaseSound#updateMarker](sound-basesound.md)

> Source: [src/sound/BaseSound.js#L229](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L229)  
> Since: 3.0.0

---

# Private Methods

## createAndStartBufferSource

### <instance> createAndStartBufferSource()

**Description:**

Used internally.

**Access:** private

> Source: [src/sound/webaudio/WebAudioSound.js#L355](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/webaudio/WebAudioSound.js#L355)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [audioBuffer](#audiobuffer)

    - [audioBuffer: AudioBuffer](#audiobuffer-audiobuffer)
  + [currentMarker](#currentmarker)

    - [currentMarker: Phaser.Types.Sound.SoundMarker](#currentmarker-phasertypessoundsoundmarker)
  + [detune](#detune)

    - [detune: number](#detune-number)
  + [duration](#duration)

    - [duration: number](#duration-number)
  + [hasEnded](#hasended)

    - [hasEnded: boolean](#hasended-boolean)
  + [hasLooped](#haslooped)

    - [hasLooped: boolean](#haslooped-boolean)
  + [isPaused](#ispaused)

    - [isPaused: boolean](#ispaused-boolean)
  + [isPlaying](#isplaying)

    - [isPlaying: boolean](#isplaying-boolean)
  + [key](#key)

    - [key: string](#key-string)
  + [loop](#loop)

    - [loop: boolean](#loop-boolean)
  + [loopSource](#loopsource)

    - [loopSource: AudioBufferSourceNode](#loopsource-audiobuffersourcenode)
  + [loopTime](#looptime)

    - [loopTime: number](#looptime-number)
  + [manager](#manager)

    - [manager: Phaser.Sound.BaseSoundManager](#manager-phasersoundbasesoundmanager)
  + [markers](#markers)

    - [markers: Object.<string, Phaser.Types.Sound.SoundMarker>](#markers-objectstring-phasertypessoundsoundmarker)
  + [mute](#mute)

    - [mute: boolean](#mute-boolean)
  + [muteNode](#mutenode)

    - [muteNode: GainNode](#mutenode-gainnode)
  + [pan](#pan)

    - [pan: number](#pan-number)
  + [pannerNode](#pannernode)

    - [pannerNode: StereoPannerNode](#pannernode-stereopannernode)
  + [pendingRemove](#pendingremove)

    - [pendingRemove: boolean](#pendingremove-boolean)
  + [playTime](#playtime)

    - [playTime: number](#playtime-number)
  + [rate](#rate)

    - [rate: number](#rate-number)
  + [rateUpdates](#rateupdates)

    - [rateUpdates: array](#rateupdates-array)
  + [seek](#seek)

    - [seek: number](#seek-number)
  + [source](#source)

    - [source: AudioBufferSourceNode](#source-audiobuffersourcenode)
  + [spatialNode](#spatialnode)

    - [spatialNode: PannerNode](#spatialnode-pannernode)
  + [spatialSource](#spatialsource)

    - [spatialSource: Phaser.Types.Math.Vector2Like](#spatialsource-phasertypesmathvector2like)
  + [startTime](#starttime)

    - [startTime: number](#starttime-number)
  + [totalDuration](#totalduration)

    - [totalDuration: number](#totalduration-number)
  + [totalRate](#totalrate)

    - [totalRate: number](#totalrate-number)
  + [volume](#volume)

    - [volume: number](#volume-number)
  + [volumeNode](#volumenode)

    - [volumeNode: GainNode](#volumenode-gainnode)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
* [Private Members](#private-members)

  + [config](#config)

    - [config: Phaser.Types.Sound.SoundConfig](#config-phasertypessoundsoundconfig)
  + [currentConfig](#currentconfig)

    - [currentConfig: Phaser.Types.Sound.SoundConfig](#currentconfig-phasertypessoundsoundconfig)
* [Public Methods](#public-methods)

  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addMarker](#addmarker)

    - [<instance> addMarker(marker)](#instance-addmarkermarker)
  + [applyConfig](#applyconfig)

    - [<instance> applyConfig()](#instance-applyconfig)
  + [calculateRate](#calculaterate)

    - [<instance> calculateRate()](#instance-calculaterate)
  + [createAndStartLoopBufferSource](#createandstartloopbuffersource)

    - [<instance> createAndStartLoopBufferSource()](#instance-createandstartloopbuffersource)
  + [createBufferSource](#createbuffersource)

    - [<instance> createBufferSource()](#instance-createbuffersource)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [getCurrentTime](#getcurrenttime)

    - [<instance> getCurrentTime()](#instance-getcurrenttime)
  + [getLoopTime](#getlooptime)

    - [<instance> getLoopTime()](#instance-getlooptime)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [pause](#pause)

    - [<instance> pause()](#instance-pause)
  + [play](#play)

    - [<instance> play([markerName], [config])](#instance-playmarkername-config)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [removeMarker](#removemarker)

    - [<instance> removeMarker(markerName)](#instance-removemarkermarkername)
  + [resetConfig](#resetconfig)

    - [<instance> resetConfig()](#instance-resetconfig)
  + [resume](#resume)

    - [<instance> resume()](#instance-resume)
  + [setDetune](#setdetune)

    - [<instance> setDetune(value)](#instance-setdetunevalue)
  + [setLoop](#setloop)

    - [<instance> setLoop(value)](#instance-setloopvalue)
  + [setMute](#setmute)

    - [<instance> setMute(value)](#instance-setmutevalue)
  + [setPan](#setpan)

    - [<instance> setPan(value)](#instance-setpanvalue)
  + [setRate](#setrate)

    - [<instance> setRate(value)](#instance-setratevalue)
  + [setSeek](#setseek)

    - [<instance> setSeek(value)](#instance-setseekvalue)
  + [setVolume](#setvolume)

    - [<instance> setVolume(value)](#instance-setvolumevalue)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [stop](#stop)

    - [<instance> stop()](#instance-stop)
  + [stopAndRemoveBufferSource](#stopandremovebuffersource)

    - [<instance> stopAndRemoveBufferSource()](#instance-stopandremovebuffersource)
  + [stopAndRemoveLoopBufferSource](#stopandremoveloopbuffersource)

    - [<instance> stopAndRemoveLoopBufferSource()](#instance-stopandremoveloopbuffersource)
  + [update](#update)

    - [<instance> update()](#instance-update)
  + [updateMarker](#updatemarker)

    - [<instance> updateMarker(marker)](#instance-updatemarkermarker)
* [Private Methods](#private-methods)

  + [createAndStartBufferSource](#createandstartbuffersource)

    - [<instance> createAndStartBufferSource()](#instance-createandstartbuffersource)

Back to top

©2025[Phaser](https://docs.phaser.io)