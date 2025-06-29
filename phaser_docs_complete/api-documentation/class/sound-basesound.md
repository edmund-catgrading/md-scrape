# BaseSound

Phaser.Sound.BaseSound

Class containing all the shared state and behavior of a sound object, independent of the implementation.

**Constructor**

`new BaseSound(manager, key, [config])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| manager | [Phaser.Sound.BaseSoundManager](sound-basesoundmanager.md) | No | Reference to the current sound manager instance. |
| --- | --- | --- | --- |
| key | string | No | Asset key for the sound. |
| config | [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md) | Yes | An optional config object containing default sound settings. |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](events-eventemitter.md)

> Source: [src/sound/BaseSound.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L14)  
> Since: 3.0.0

# Public Members

## currentMarker

### currentMarker: [Phaser.Types.Sound.SoundMarker](../typedef/types-sound.md)

**Description:**

Currently playing marker.

'null' if whole sound is playing.

> Source: [src/sound/BaseSound.js#L159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L159)  
> Since: 3.0.0

---

## duration

### duration: number

**Description:**

A value representing the duration, in seconds.

It could be total sound duration or a marker duration.

> Source: [src/sound/BaseSound.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L92)  
> Since: 3.0.0

---

## isPaused

### isPaused: boolean

**Description:**

Flag indicating if sound is currently paused.

> Source: [src/sound/BaseSound.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L68)  
> Since: 3.0.0

---

## isPlaying

### isPlaying: boolean

**Description:**

Flag indicating if sound is currently playing.

> Source: [src/sound/BaseSound.js#L57](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L57)  
> Since: 3.0.0

---

## key

### key: string

**Description:**

Asset key for the sound.

> Source: [src/sound/BaseSound.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L47)  
> Since: 3.0.0

---

## manager

### manager: [Phaser.Sound.BaseSoundManager](sound-basesoundmanager.md)

**Description:**

Local reference to the sound manager.

> Source: [src/sound/BaseSound.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L38)  
> Since: 3.0.0

---

## markers

### markers: Object.<string, [Phaser.Types.Sound.SoundMarker](../typedef/types-sound.md)>

**Description:**

Object containing markers definitions.

> Source: [src/sound/BaseSound.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L148)  
> Since: 3.0.0

---

## pendingRemove

### pendingRemove: boolean

**Description:**

Flag indicating if destroy method was called on this sound.

> Source: [src/sound/BaseSound.js#L171](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L171)  
> Since: 3.0.0

---

## totalDuration

### totalDuration: number

**Description:**

The total duration of the sound in seconds.

> Source: [src/sound/BaseSound.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L103)  
> Since: 3.0.0

---

## totalRate

### totalRate: number

**Description:**

A property that holds the value of sound's actual playback rate,

after its rate and detune values has been combined with global

rate and detune values.

> Source: [src/sound/BaseSound.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L79)  
> Since: 3.0.0

---

# Private Members

## config

### config: [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md)

**Description:**

A config object used to store default sound settings' values.

Default values will be set by properties' setters.

**Access:** private

> Source: [src/sound/BaseSound.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L113)  
> Since: 3.0.0

---

## currentConfig

### currentConfig: [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md)

**Description:**

Reference to the currently used config.

It could be default config or marker config.

**Access:** private

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

**Returns:** [Phaser.Sound.BaseSound](sound-basesound.md) - `this`.

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

> Source: [src/sound/BaseSound.js#L182](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L182)  
> Since: 3.0.0

---

## applyConfig

### <instance> applyConfig()

**Description:**

Method used internally for applying config values to some of the sound properties.

> Source: [src/sound/BaseSound.js#L412](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L412)  
> Since: 3.0.0

---

## calculateRate

### <instance> calculateRate()

**Description:**

Method used internally to calculate total playback rate of the sound.

> Source: [src/sound/BaseSound.js#L451](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L451)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this sound and all associated events and marks it for removal from the sound manager.

**Overrides:** Phaser.Events.EventEmitter#destroy

**Fires:** [Phaser.Sound.Events#event:DESTROY](../event/sound-events.md)

> Source: [src/sound/BaseSound.js#L466](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L466)  
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

**Returns:** [Phaser.Sound.BaseSound](sound-basesound.md) - `this`.

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

**Returns:** [Phaser.Sound.BaseSound](sound-basesound.md) - `this`.

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

**Returns:** [Phaser.Sound.BaseSound](sound-basesound.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## pause

### <instance> pause()

**Description:**

Pauses the sound. This only works if the sound is currently playing.

You can inspect the `isPlaying` and `isPaused` properties to check the state.

**Returns:** boolean - Whether the sound was paused successfully.

> Source: [src/sound/BaseSound.js#L343](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L343)  
> Since: 3.0.0

---

## play

### <instance> play([markerName], [config])

**Description:**

Play this sound, or a marked section of it.

It always plays the sound from the start. If you want to start playback from a specific time

you can set 'seek' setting of the config object, provided to this call, to that value.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| markerName | string | [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md) | Yes | "''" | If you want to play a marker then provide the marker name here. Alternatively, this parameter can be a SoundConfig object. |
| --- | --- | --- | --- | --- |
| config | [Phaser.Types.Sound.SoundConfig](../typedef/types-sound.md) | Yes |  | Optional sound config object to be applied to this marker or entire sound if no marker name is provided. It gets memorized for future plays of current section of the sound. |

**Returns:** boolean - Whether the sound started playing successfully.

> Source: [src/sound/BaseSound.js#L283](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L283)  
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

**Returns:** [Phaser.Sound.BaseSound](sound-basesound.md) - `this`.

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

**Returns:** [Phaser.Sound.BaseSound](sound-basesound.md) - `this`.

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

> Source: [src/sound/BaseSound.js#L259](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L259)  
> Since: 3.0.0

---

## resetConfig

### <instance> resetConfig()

**Description:**

Method used internally for resetting values of some of the config properties.

> Source: [src/sound/BaseSound.js#L428](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L428)  
> Since: 3.0.0

---

## resume

### <instance> resume()

**Description:**

Resumes the sound. This only works if the sound is paused and not already playing.

You can inspect the `isPlaying` and `isPaused` properties to check the state.

**Returns:** boolean - Whether the sound was resumed successfully.

> Source: [src/sound/BaseSound.js#L366](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L366)  
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

## stop

### <instance> stop()

**Description:**

Stop playing this sound.

**Returns:** boolean - Whether the sound was stopped successfully.

> Source: [src/sound/BaseSound.js#L389](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L389)  
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

> Source: [src/sound/BaseSound.js#L440](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L440)  
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

> Source: [src/sound/BaseSound.js#L229](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/BaseSound.js#L229)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [currentMarker](#currentmarker)

    - [currentMarker: Phaser.Types.Sound.SoundMarker](#currentmarker-phasertypessoundsoundmarker)
  + [duration](#duration)

    - [duration: number](#duration-number)
  + [isPaused](#ispaused)

    - [isPaused: boolean](#ispaused-boolean)
  + [isPlaying](#isplaying)

    - [isPlaying: boolean](#isplaying-boolean)
  + [key](#key)

    - [key: string](#key-string)
  + [manager](#manager)

    - [manager: Phaser.Sound.BaseSoundManager](#manager-phasersoundbasesoundmanager)
  + [markers](#markers)

    - [markers: Object.<string, Phaser.Types.Sound.SoundMarker>](#markers-objectstring-phasertypessoundsoundmarker)
  + [pendingRemove](#pendingremove)

    - [pendingRemove: boolean](#pendingremove-boolean)
  + [totalDuration](#totalduration)

    - [totalDuration: number](#totalduration-number)
  + [totalRate](#totalrate)

    - [totalRate: number](#totalrate-number)
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



BaseSound