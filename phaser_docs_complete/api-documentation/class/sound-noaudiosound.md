# NoAudioSound

Phaser.Sound.NoAudioSound

No audio implementation of the sound. It is used if audio has been

disabled in the game config or the device doesn't support any audio.

It represents a graceful degradation of sound logic that provides

minimal functionality and prevents Phaser projects that use audio from

breaking on devices that don't support any audio playback technologies.

**Constructor**

`new NoAudioSound(manager, key, [config])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| manager | [Phaser.Sound.NoAudioSoundManager](sound-noaudiosoundmanager.md) | No |  | Reference to the current sound manager instance. |
| --- | --- | --- | --- | --- |
| key | string | No |  | Asset key for the sound. |
| config | [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md) | Yes | "{}" | An optional config object containing default sound settings. |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](events-eventemitter.md)

> Source: [src/sound/noaudio/NoAudioSound.js#L29](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L29)  
> Since: 3.0.0

# Public Members

## config

### config: [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md)

**Description:**

A config object used to store default sound settings' values.

Default values will be set by properties' setters.

> Source: [src/sound/noaudio/NoAudioSound.js#L135](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L135)  
> Since: 3.0.0

---

## currentConfig

### currentConfig: [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md)

**Description:**

Reference to the currently used config.

It could be default config or marker config.

> Source: [src/sound/noaudio/NoAudioSound.js#L154](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L154)  
> Since: 3.0.0

---

## currentMarker

### currentMarker: [Phaser.Types.Sound.SoundMarker](../typedef/types-sound.md)

**Description:**

Currently playing marker.

'null' if whole sound is playing.

> Source: [src/sound/noaudio/NoAudioSound.js#L260](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L260)  
> Since: 3.0.0

---

## detune

### detune: number

**Description:**

The detune value of this Sound, given in [cents](https://en.wikipedia.org/wiki/Cent_%28music%29).

The range of the value is -1200 to 1200, but we recommend setting it to [50](https://en.wikipedia.org/wiki/50_Cent).

**Fires:** [Phaser.Sound.Events#event:DETUNE](../event/sound-events.md)

> Source: [src/sound/noaudio/NoAudioSound.js#L200](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L200)  
> Since: 3.0.0

---

## duration

### duration: number

**Description:**

A value representing the duration, in seconds.

It could be total sound duration or a marker duration.

> Source: [src/sound/noaudio/NoAudioSound.js#L114](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L114)  
> Since: 3.0.0

---

## isPaused

### isPaused: boolean

**Description:**

Flag indicating if sound is currently paused.

> Source: [src/sound/noaudio/NoAudioSound.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L90)  
> Since: 3.0.0

---

## isPlaying

### isPlaying: boolean

**Description:**

Flag indicating if sound is currently playing.

> Source: [src/sound/noaudio/NoAudioSound.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L79)  
> Since: 3.0.0

---

## key

### key: string

**Description:**

Asset key for the sound.

> Source: [src/sound/noaudio/NoAudioSound.js#L69](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L69)  
> Since: 3.0.0

---

## loop

### loop: boolean

**Description:**

Flag indicating whether or not the sound or current sound marker will loop.

**Fires:** [Phaser.Sound.Events#event:LOOP](../event/sound-events.md)

> Source: [src/sound/noaudio/NoAudioSound.js#L225](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L225)  
> Since: 3.0.0

---

## manager

### manager: [Phaser.Sound.BaseSoundManager](sound-basesoundmanager.md)

**Description:**

Local reference to the sound manager.

> Source: [src/sound/noaudio/NoAudioSound.js#L60](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L60)  
> Since: 3.0.0

---

## markers

### markers: Object.<string, [Phaser.Types.Sound.SoundMarker](../typedef/types-sound.md)>

**Description:**

Object containing markers definitions.

> Source: [src/sound/noaudio/NoAudioSound.js#L249](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L249)  
> Since: 3.0.0

---

## mute

### mute: boolean

**Description:**

Boolean indicating whether the sound is muted or not.

Gets or sets the muted state of this sound.

**Fires:** [Phaser.Sound.Events#event:MUTE](../event/sound-events.md)

> Source: [src/sound/noaudio/NoAudioSound.js#L164](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L164)  
> Since: 3.0.0

---

## pan

### pan: number

**Description:**

Gets or sets the pan of this sound, a value between -1 (full left pan) and 1 (full right pan).

Always returns zero on iOS / Safari as it doesn't support the stereo panner node.

**Fires:** [Phaser.Sound.Events#event:PAN](../event/sound-events.md)

> Source: [src/sound/noaudio/NoAudioSound.js#L236](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L236)  
> Since: 3.50.0

---

## pendingRemove

### pendingRemove: boolean

**Description:**

Flag indicating if destroy method was called on this sound.

> Source: [src/sound/noaudio/NoAudioSound.js#L272](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L272)  
> Since: 3.0.0

---

## rate

### rate: number

**Description:**

Rate at which this Sound will be played.

Value of 1.0 plays the audio at full speed, 0.5 plays the audio at half speed

and 2.0 doubles the audios playback speed.

**Fires:** [Phaser.Sound.Events#event:RATE](../event/sound-events.md)

> Source: [src/sound/noaudio/NoAudioSound.js#L187](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L187)  
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

> Source: [src/sound/noaudio/NoAudioSound.js#L212](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L212)  
> Since: 3.0.0

---

## totalDuration

### totalDuration: number

**Description:**

The total duration of the sound in seconds.

> Source: [src/sound/noaudio/NoAudioSound.js#L125](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L125)  
> Since: 3.0.0

---

## totalRate

### totalRate: number

**Description:**

A property that holds the value of sound's actual playback rate,

after its rate and detune values has been combined with global

rate and detune values.

> Source: [src/sound/noaudio/NoAudioSound.js#L101](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L101)  
> Since: 3.0.0

---

## volume

### volume: number

**Description:**

Gets or sets the volume of this sound, a value between 0 (silence) and 1 (full volume).

**Fires:** [Phaser.Sound.Events#event:VOLUME](../event/sound-events.md)

> Source: [src/sound/noaudio/NoAudioSound.js#L176](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L176)  
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

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## addMarker

### <instance> addMarker(marker)

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| marker | [Phaser.Types.Sound.SoundMarker](../typedef/types-sound.md) | No | Marker object. |
| --- | --- | --- | --- |

**Returns:** boolean - false

> Source: [src/sound/noaudio/NoAudioSound.js#L283](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L283)  
> Since: 3.0.0

---

## applyConfig

### <instance> applyConfig()

**Description:**

Method used internally for applying config values to some of the sound properties.

> Source: [src/sound/noaudio/NoAudioSound.js#L442](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L442)  
> Since: 3.0.0

---

## calculateRate

### <instance> calculateRate()

**Description:**

Method used internally to calculate total playback rate of the sound.

> Source: [src/sound/noaudio/NoAudioSound.js#L470](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L470)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this sound and all associated events and marks it for removal from the sound manager.

**Overrides:** Phaser.Events.EventEmitter#destroy

**Fires:** [Phaser.Sound.Events#event:DESTROY](../event/sound-events.md)

> Source: [src/sound/noaudio/NoAudioSound.js#L478](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L478)  
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

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md) - `this`.

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

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md) - `this`.

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

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## pause

### <instance> pause()

**Returns:** boolean - false

> Source: [src/sound/noaudio/NoAudioSound.js#L324](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L324)  
> Since: 3.0.0

---

## play

### <instance> play([markerName], [config])

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| markerName | string | [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md) | Yes | "''" | If you want to play a marker then provide the marker name here. Alternatively, this parameter can be a SoundConfig object. |
| --- | --- | --- | --- | --- |
| config | [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md) | Yes |  | Optional sound config object to be applied to this marker or entire sound if no marker name is provided. It gets memorized for future plays of current section of the sound. |

**Returns:** boolean - false

> Source: [src/sound/noaudio/NoAudioSound.js#L313](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L313)  
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

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md) - `this`.

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

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## removeMarker

### <instance> removeMarker(markerName)

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| markerName | string | No | The name of the marker to remove. |
| --- | --- | --- | --- |

**Returns:** null - null

> Source: [src/sound/noaudio/NoAudioSound.js#L303](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L303)  
> Since: 3.0.0

---

## resetConfig

### <instance> resetConfig()

**Description:**

Method used internally for resetting values of some of the config properties.

> Source: [src/sound/noaudio/NoAudioSound.js#L450](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L450)  
> Since: 3.0.0

---

## resume

### <instance> resume()

**Description:**

Resumes the sound.

**Returns:** boolean - false

> Source: [src/sound/noaudio/NoAudioSound.js#L332](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L332)  
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

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md) - This Sound instance.

> Source: [src/sound/noaudio/NoAudioSound.js#L391](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L391)  
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

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md) - This Sound instance.

> Source: [src/sound/noaudio/NoAudioSound.js#L416](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L416)  
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

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md) - This Sound instance.

> Source: [src/sound/noaudio/NoAudioSound.js#L352](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L352)  
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

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md) - This Sound instance.

> Source: [src/sound/noaudio/NoAudioSound.js#L428](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L428)  
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

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md) - This Sound instance.

> Source: [src/sound/noaudio/NoAudioSound.js#L376](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L376)  
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

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md) - This Sound instance.

> Source: [src/sound/noaudio/NoAudioSound.js#L404](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L404)  
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

**Returns:** [Phaser.Sound.NoAudioSound](sound-noaudiosound.md) - This Sound instance.

> Source: [src/sound/noaudio/NoAudioSound.js#L364](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L364)  
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

**Returns:** boolean - false

> Source: [src/sound/noaudio/NoAudioSound.js#L342](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L342)  
> Since: 3.0.0

---

## update

### <instance> update(time, delta)

**Description:**

Update method called automatically by sound manager on every game step.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current timestamp as generated by the Request Animation Frame or SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time elapsed since the last frame. |

> Source: [src/sound/noaudio/NoAudioSound.js#L458](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L458)  
> Since: 3.0.0

---

## updateMarker

### <instance> updateMarker(marker)

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| marker | [Phaser.Types.Sound.SoundMarker](../typedef/types-sound.md) | No | Marker object with updated values. |
| --- | --- | --- | --- |

**Returns:** boolean - false

> Source: [src/sound/noaudio/NoAudioSound.js#L293](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/noaudio/NoAudioSound.js#L293)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [config](#config)

    - [config: Phaser.Types.Sound.SoundConfig](#config-phasertypessoundsoundconfig)
  + [currentConfig](#currentconfig)

    - [currentConfig: Phaser.Types.Sound.SoundConfig](#currentconfig-phasertypessoundsoundconfig)
  + [currentMarker](#currentmarker)

    - [currentMarker: Phaser.Types.Sound.SoundMarker](#currentmarker-phasertypessoundsoundmarker)
  + [detune](#detune)

    - [detune: number](#detune-number)
  + [duration](#duration)

    - [duration: number](#duration-number)
  + [isPaused](#ispaused)

    - [isPaused: boolean](#ispaused-boolean)
  + [isPlaying](#isplaying)

    - [isPlaying: boolean](#isplaying-boolean)
  + [key](#key)

    - [key: string](#key-string)
  + [loop](#loop)

    - [loop: boolean](#loop-boolean)
  + [manager](#manager)

    - [manager: Phaser.Sound.BaseSoundManager](#manager-phasersoundbasesoundmanager)
  + [markers](#markers)

    - [markers: Object.<string, Phaser.Types.Sound.SoundMarker>](#markers-objectstring-phasertypessoundsoundmarker)
  + [mute](#mute)

    - [mute: boolean](#mute-boolean)
  + [pan](#pan)

    - [pan: number](#pan-number)
  + [pendingRemove](#pendingremove)

    - [pendingRemove: boolean](#pendingremove-boolean)
  + [rate](#rate)

    - [rate: number](#rate-number)
  + [seek](#seek)

    - [seek: number](#seek-number)
  + [totalDuration](#totalduration)

    - [totalDuration: number](#totalduration-number)
  + [totalRate](#totalrate)

    - [totalRate: number](#totalrate-number)
  + [volume](#volume)

    - [volume: number](#volume-number)
* [Public Methods](#public-methods)

  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addMarker](#addmarker)

    - [<instance> addMarker(marker)](#instance-addmarkermarker)
  + [applyConfig](#applyconfig)

    - [<instance> applyConfig()](#instance-applyconfig)
  + [calculateRate](#calculaterate)

    - [<instance> calculateRate()](#instance-calculaterate)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
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
  + [update](#update)

    - [<instance> update(time, delta)](#instance-updatetime-delta)
  + [updateMarker](#updatemarker)

    - [<instance> updateMarker(marker)](#instance-updatemarkermarker)

Back to top

©2025[Phaser](https://docs.phaser.io)