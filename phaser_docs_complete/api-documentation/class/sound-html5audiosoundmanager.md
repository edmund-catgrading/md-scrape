# HTML5AudioSoundManager

Phaser.Sound.HTML5AudioSoundManager

HTML5AudioSoundManager

**Constructor**

`new HTML5AudioSoundManager(game)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](game.md) | No | Reference to the current game instance. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.Sound.BaseSoundManager](sound-basesoundmanager.md)

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L37)  
> Since: 3.0.0

# Public Members

## audioPlayDelay

### audioPlayDelay: number

**Description:**

Value representing time difference, in seconds, between calling

play method on an audio tag and when it actually starts playing.

It is used to achieve more accurate delayed sound playback.

You might need to tweak this value to get the desired results

since audio play delay varies depending on the browser/platform.

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L58](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L58)  
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

## loopEndOffset

### loopEndOffset: number

**Description:**

A value by which we should offset the loop end marker of the

looping sound to compensate for lag, caused by changing audio

tag playback position, in order to achieve gapless looping.

You might need to tweak this value to get the desired results

since loop lag varies depending on the browser/platform.

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L73](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L73)  
> Since: 3.0.0

---

## mute

### mute: boolean

**Overrides:** Phaser.Sound.BaseSoundManager#mute

**Fires:** [Phaser.Sound.Events#event:GLOBAL\_MUTE](../event/sound-events.md)

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L389](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L389)  
> Since: 3.0.0

---

## override

### override: boolean

**Description:**

Flag indicating whether if there are no idle instances of HTML5 Audio tag,

for any particular sound, if one of the used tags should be hijacked and used

for succeeding playback or if succeeding Phaser.Sound.HTML5AudioSound#play

call should be ignored.

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L45)  
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

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L434](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L434)  
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

## \_mute

### \_mute: boolean

**Description:**

Property that actually holds the value of global mute

for HTML5 Audio sound manager implementation.

**Access:** private

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L115)  
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

## \_volume

### \_volume: boolean

**Description:**

Property that actually holds the value of global volume

for HTML5 Audio sound manager implementation.

**Access:** private

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L127](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L127)  
> Since: 3.0.0

---

## lockedActionsQueue

### lockedActionsQueue: array

**Description:**

A queue of all actions performed on sound objects while audio was locked.

Once the audio gets unlocked, after an explicit user interaction,

all actions will be performed in chronological order.

Array of object types: { sound: Phaser.Sound.HTML5AudioSound, name: string, value?: \* }

**Access:** private

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L102)  
> Since: 3.0.0

---

## onBlurPausedSounds

### onBlurPausedSounds: Array.<[Phaser.Sound.HTML5AudioSound](sound-html5audiosound.md)>

**Description:**

An array for keeping track of all the sounds

that were paused when game lost focus.

**Access:** private

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L88)  
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

**Returns:** [Phaser.Sound.HTML5AudioSound](sound-html5audiosound.md) - The new sound instance.

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L142](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L142)  
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

**Returns:** [Phaser.Sound.HTML5AudioSoundManager](sound-html5audiosoundmanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Calls Phaser.Sound.BaseSoundManager#destroy method

and cleans up all HTML5 Audio related stuff.

**Overrides:** Phaser.Sound.BaseSoundManager#destroy

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L325](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L325)  
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

## isLocked

### <instance> isLocked(sound, prop, [value])

**Description:**

Method used internally by Phaser.Sound.HTML5AudioSound class methods and property setters

to check if sound manager is locked and then either perform action immediately or queue it

to be performed once the sound manager gets unlocked.

**Access:** protected

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.HTML5AudioSound](sound-html5audiosound.md) | No | Sound object on which to perform queued action. |
| --- | --- | --- | --- |
| prop | string | No | Name of the method to be called or property to be assigned a value to. |
| value | \* | Yes | An optional parameter that either holds an array of arguments to be passed to the method call or value to be set to the property. |

**Returns:** boolean - Whether the sound manager is locked.

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L340](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L340)  
> Since: 3.0.0

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

**Returns:** [Phaser.Sound.HTML5AudioSoundManager](sound-html5audiosoundmanager.md) - `this`.

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

**Returns:** [Phaser.Sound.HTML5AudioSoundManager](sound-html5audiosoundmanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#on](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L98)  
> Since: 3.0.0

---

## onBlur

### <instance> onBlur()

**Description:**

Method used internally for pausing sound manager if

Phaser.Sound.HTML5AudioSoundManager#pauseOnBlur is set to true.

**Access:** protected

**Overrides:** Phaser.Sound.BaseSoundManager#onBlur

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L287](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L287)  
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

**Returns:** [Phaser.Sound.HTML5AudioSoundManager](sound-html5audiosoundmanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## onFocus

### <instance> onFocus()

**Description:**

Method used internally for resuming sound manager if

Phaser.Sound.HTML5AudioSoundManager#pauseOnBlur is set to true.

**Access:** protected

**Overrides:** Phaser.Sound.BaseSoundManager#onFocus

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L307](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L307)  
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

**Returns:** [Phaser.Sound.HTML5AudioSoundManager](sound-html5audiosoundmanager.md) - `this`.

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

**Returns:** [Phaser.Sound.HTML5AudioSoundManager](sound-html5audiosoundmanager.md) - `this`.

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

**Returns:** [Phaser.Sound.HTML5AudioSoundManager](sound-html5audiosoundmanager.md) - This Sound Manager.

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

**Inherits:** [Phaser.Sound.BaseSoundManager#setListenerPosition](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L480](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L480)  
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

**Returns:** [Phaser.Sound.HTML5AudioSoundManager](sound-html5audiosoundmanager.md) - This Sound Manager.

**Fires:** [Phaser.Sound.Events#event:GLOBAL\_MUTE](../event/sound-events.md)

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L371](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L371)  
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

**Returns:** [Phaser.Sound.HTML5AudioSoundManager](sound-html5audiosoundmanager.md) - This Sound Manager.

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

**Returns:** [Phaser.Sound.HTML5AudioSoundManager](sound-html5audiosoundmanager.md) - This Sound Manager.

**Fires:** [Phaser.Sound.Events#event:GLOBAL\_VOLUME](../event/sound-events.md)

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L416](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L416)  
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

Unlocks HTML5 Audio loading and playback on mobile

devices on the initial explicit user interaction.

**Overrides:** Phaser.Sound.BaseSoundManager#unlock

> Source: [src/sound/html5/HTML5AudioSoundManager.js#L162](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/html5/HTML5AudioSoundManager.js#L162)  
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

**Fires:** [Phaser.Sound.Events#event:UNLOCKED](../event/sound-events.md)

**Inherits:** [Phaser.Sound.BaseSoundManager#update](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L651](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L651)  
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

  + [audioPlayDelay](#audioplaydelay)

    - [audioPlayDelay: number](#audioplaydelay-number)
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
  + [loopEndOffset](#loopendoffset)

    - [loopEndOffset: number](#loopendoffset-number)
  + [mute](#mute)

    - [mute: boolean](#mute-boolean)
  + [override](#override)

    - [override: boolean](#override-boolean)
  + [pauseOnBlur](#pauseonblur)

    - [pauseOnBlur: boolean](#pauseonblur-boolean)
  + [rate](#rate)

    - [rate: number](#rate-number)
  + [volume](#volume)

    - [volume: number](#volume-number)
* [Private Members](#private-members)

  + [\_detune](#_detune)

    - [\_detune: number](#_detune-number)
  + [\_mute](#_mute)

    - [\_mute: boolean](#_mute-boolean)
  + [\_rate](#_rate)

    - [\_rate: number](#_rate-number)
  + [\_volume](#_volume)

    - [\_volume: boolean](#_volume-boolean)
  + [lockedActionsQueue](#lockedactionsqueue)

    - [lockedActionsQueue: array](#lockedactionsqueue-array)
  + [onBlurPausedSounds](#onblurpausedsounds)

    - [onBlurPausedSounds: Array.<Phaser.Sound.HTML5AudioSound>](#onblurpausedsounds-arrayphasersoundhtml5audiosound)
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
  + [isLocked](#islocked)

    - [<instance> isLocked(sound, prop, [value])](#instance-islockedsound-prop-value)
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