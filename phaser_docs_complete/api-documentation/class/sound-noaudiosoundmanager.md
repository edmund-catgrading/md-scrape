# NoAudioSoundManager

Phaser.Sound.NoAudioSoundManager

No-audio implementation of the Sound Manager. It is used if audio has been

disabled in the game config or the device doesn't support any audio.

It represents a graceful degradation of Sound Manager logic that provides

minimal functionality and prevents Phaser projects that use audio from

breaking on devices that don't support any audio playback technologies.

**Constructor**

`new NoAudioSoundManager(game)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](game.md) | No | Reference to the current game instance. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.Sound.BaseSoundManager](sound-basesoundmanager.md)

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L14)  
> Since: 3.0.0

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

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md) - The new sound instance.

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L51](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L51)  
> Since: 3.60.0

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

**Overrides:** Phaser.Sound.BaseSoundManager#addAudioSprite

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md) - The new audio sprite sound instance.

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L71](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L71)  
> Since: 3.60.0

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

**Returns:** [Phaser.Sound.NoAudioSoundManager](sound-noaudiosoundmanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys all the sounds in the game and all associated events.

**Overrides:** Phaser.Sound.BaseSoundManager#destroy

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L347](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L347)  
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

Gets the first sound in the manager matching the given key, if any.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | Sound asset key. |
| --- | --- | --- | --- |

**Overrides:** Phaser.Sound.BaseSoundManager#get

**Returns:** [Phaser.Sound.BaseSound](sound-basesound.md) - - The sound, or null.

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L93)  
> Since: 3.23.0

---

## getAll

### <instance> getAll(key)

**Description:**

Gets any sounds in the manager matching the given key.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | Sound asset key. |
| --- | --- | --- | --- |

**Overrides:** Phaser.Sound.BaseSoundManager#getAll

**Returns:** Array.<[Phaser.Sound.BaseSound](sound-basesound.md)> - - The sounds, or an empty array.

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L111)  
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

**Returns:** [Phaser.Sound.NoAudioSoundManager](sound-noaudiosoundmanager.md) - `this`.

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

**Returns:** [Phaser.Sound.NoAudioSoundManager](sound-noaudiosoundmanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#on](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L98)  
> Since: 3.0.0

---

## onBlur

### <instance> onBlur()

**Description:**

Empty function for the No Audio Sound Manager.

**Overrides:** Phaser.Sound.BaseSoundManager#onBlur

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L224](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L224)  
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

**Returns:** [Phaser.Sound.NoAudioSoundManager](sound-noaudiosoundmanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## onFocus

### <instance> onFocus()

**Description:**

Empty function for the No Audio Sound Manager.

**Overrides:** Phaser.Sound.BaseSoundManager#onFocus

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L232](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L232)  
> Since: 3.0.0

---

## onGameBlur

### <instance> onGameBlur()

**Description:**

Empty function for the No Audio Sound Manager.

**Overrides:** Phaser.Sound.BaseSoundManager#onGameBlur

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L240](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L240)  
> Since: 3.0.0

---

## onGameFocus

### <instance> onGameFocus()

**Description:**

Empty function for the No Audio Sound Manager.

**Overrides:** Phaser.Sound.BaseSoundManager#onGameFocus

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L248](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L248)  
> Since: 3.0.0

---

## pauseAll

### <instance> pauseAll()

**Description:**

Empty function for the No Audio Sound Manager.

**Overrides:** Phaser.Sound.BaseSoundManager#pauseAll

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L256](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L256)  
> Since: 3.0.0

---

## play

### <instance> play(key, [extra])

**Description:**

This method does nothing but return 'false' for the No Audio Sound Manager, to maintain

compatibility with the other Sound Managers.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | Asset key for the sound. |
| --- | --- | --- | --- |
| extra | [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md) | [Phaser.Types.Sound.SoundMarker](../typedef/types-sound.md) | Yes | An optional additional object containing settings to be applied to the sound. It could be either config or marker object. |

**Overrides:** Phaser.Sound.BaseSoundManager#play

**Returns:** boolean - Always 'false' for the No Audio Sound Manager.

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L129)  
> Since: 3.0.0

---

## playAudioSprite

### <instance> playAudioSprite(key, spriteName, [config])

**Description:**

This method does nothing but return 'false' for the No Audio Sound Manager, to maintain

compatibility with the other Sound Managers.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | Asset key for the sound. |
| --- | --- | --- | --- |
| spriteName | string | No | The name of the sound sprite to play. |
| config | [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md) | Yes | An optional config object containing default sound settings. |

**Overrides:** Phaser.Sound.BaseSoundManager#playAudioSprite

**Returns:** boolean - Always 'false' for the No Audio Sound Manager.

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L147](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L147)  
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

**Overrides:** Phaser.Sound.BaseSoundManager#remove

**Returns:** boolean - True if the sound was removed successfully, otherwise false.

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L166](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L166)  
> Since: 3.0.0

---

## removeAll

### <instance> removeAll()

**Description:**

Removes all sounds from the manager, destroying the sounds.

**Overrides:** Phaser.Sound.BaseSoundManager#removeAll

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L182](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L182)  
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

**Returns:** [Phaser.Sound.NoAudioSoundManager](sound-noaudiosoundmanager.md) - `this`.

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

**Overrides:** Phaser.Sound.BaseSoundManager#removeByKey

**Returns:** number - The number of matching sound objects that were removed.

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L193](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L193)  
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

**Returns:** [Phaser.Sound.NoAudioSoundManager](sound-noaudiosoundmanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## resumeAll

### <instance> resumeAll()

**Description:**

Empty function for the No Audio Sound Manager.

**Overrides:** Phaser.Sound.BaseSoundManager#resumeAll

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L264](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L264)  
> Since: 3.0.0

---

## setDetune

### <instance> setDetune()

**Description:**

Empty function for the No Audio Sound Manager.

**Overrides:** Phaser.Sound.BaseSoundManager#setDetune

**Returns:** [Phaser.Sound.NoAudioSoundManager](sound-noaudiosoundmanager.md) - This Sound Manager.

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L298](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L298)  
> Since: 3.0.0

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

### <instance> setMute()

**Description:**

Empty function for the No Audio Sound Manager.

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L308](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L308)  
> Since: 3.0.0

---

## setRate

### <instance> setRate()

**Description:**

Empty function for the No Audio Sound Manager.

**Overrides:** Phaser.Sound.BaseSoundManager#setRate

**Returns:** [Phaser.Sound.NoAudioSoundManager](sound-noaudiosoundmanager.md) - This Sound Manager.

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L288](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L288)  
> Since: 3.0.0

---

## setVolume

### <instance> setVolume()

**Description:**

Empty function for the No Audio Sound Manager.

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L316](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L316)  
> Since: 3.0.0

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

Empty function for the No Audio Sound Manager.

**Overrides:** Phaser.Sound.BaseSoundManager#stopAll

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L272](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L272)  
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

**Overrides:** Phaser.Sound.BaseSoundManager#stopByKey

**Returns:** number - - How many sounds were stopped.

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L209](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L209)  
> Since: 3.23.0

---

## unlock

### <instance> unlock()

**Description:**

Empty function for the No Audio Sound Manager.

**Overrides:** Phaser.Sound.BaseSoundManager#unlock

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L324](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L324)  
> Since: 3.0.0

---

## update

### <instance> update()

**Description:**

Empty function for the No Audio Sound Manager.

**Overrides:** Phaser.Sound.BaseSoundManager#update

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L280](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L280)  
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

**Overrides:** Phaser.Sound.BaseSoundManager#forEachActiveSound

> Source: [src/sound/noaudio/NoAudioSoundManager.js#L332](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSoundManager.js#L332)  
> Since: 3.0.0

---

# Public Members

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

## mute

### mute: boolean

**Description:**

Global mute setting.

**Inherits:** [Phaser.Sound.BaseSoundManager#mute](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L75)  
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

**Description:**

Global volume setting.

**Inherits:** [Phaser.Sound.BaseSoundManager#volume](sound-basesoundmanager.md)

> Source: [src/sound/BaseSoundManager.js#L85](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSoundManager.js#L85)  
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

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

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

    - [<instance> getAll(key)](#instance-getallkey)
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
  + [onGameBlur](#ongameblur)

    - [<instance> onGameBlur()](#instance-ongameblur)
  + [onGameFocus](#ongamefocus)

    - [<instance> onGameFocus()](#instance-ongamefocus)
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

    - [<instance> setDetune()](#instance-setdetune)
  + [setListenerPosition](#setlistenerposition)

    - [<instance> setListenerPosition([x], [y])](#instance-setlistenerpositionx-y)
  + [setMute](#setmute)

    - [<instance> setMute()](#instance-setmute)
  + [setRate](#setrate)

    - [<instance> setRate()](#instance-setrate)
  + [setVolume](#setvolume)

    - [<instance> setVolume()](#instance-setvolume)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [stopAll](#stopall)

    - [<instance> stopAll()](#instance-stopall)
  + [stopByKey](#stopbykey)

    - [<instance> stopByKey(key)](#instance-stopbykeykey)
  + [unlock](#unlock)

    - [<instance> unlock()](#instance-unlock)
  + [update](#update)

    - [<instance> update()](#instance-update)
* [Private Methods](#private-methods)

  + [forEachActiveSound](#foreachactivesound)

    - [<instance> forEachActiveSound(callback, [scope])](#instance-foreachactivesoundcallback-scope)
* [Public Members](#public-members)

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

Back to top

©2025[Phaser](https://docs.phaser.io)