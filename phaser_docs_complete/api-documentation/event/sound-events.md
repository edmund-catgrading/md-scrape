# Sound.Events

Phaser.Sound.Events

## COMPLETE

**Description:** The Sound Complete Event.

This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they complete playback.

Listen to it from a Sound instance using `Sound.on('complete', listener)`, i.e.:

```
Copy
var music = this.sound.add('key');

music.on('complete', listener);

music.play();


```

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.WebAudioSound](../class/sound-webaudiosound.md) | [Phaser.Sound.HTML5AudioSound](../class/sound-html5audiosound.md) | No | A reference to the Sound that emitted the event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/COMPLETE_EVENT.js#L7)  
> Since: 3.16.1

## DECODED\_ALL

**Description:** The Audio Data Decoded All Event.

This event is dispatched by the Web Audio Sound Manager as a result of calling the `decodeAudio` method,

once all files passed to the method have been decoded (or errored).

Use `Phaser.Sound.Events#DECODED` to listen for single sounds being decoded, and `DECODED_ALL` to

listen for them all completing.

Listen to it from the Sound Manager in a Scene using `this.sound.on('decodedall', listener)`, i.e.:

```
Copy
this.sound.once('decodedall', handler);

this.sound.decodeAudio([ audioFiles ]);


```

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/DECODED\_ALL\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/DECODED_ALL_EVENT.js#L7)  
> Since: 3.18.0

## DECODED

**Description:** The Audio Data Decoded Event.

This event is dispatched by the Web Audio Sound Manager as a result of calling the `decodeAudio` method.

Listen to it from the Sound Manager in a Scene using `this.sound.on('decoded', listener)`, i.e.:

```
Copy
this.sound.on('decoded', handler);

this.sound.decodeAudio(key, audioData);


```

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the audio file that was decoded and added to the audio cache. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/DECODED\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/DECODED_EVENT.js#L7)  
> Since: 3.18.0

## DESTROY

**Description:** The Sound Destroy Event.

This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they are destroyed, either

directly or via a Sound Manager.

Listen to it from a Sound instance using `Sound.on('destroy', listener)`, i.e.:

```
Copy
var music = this.sound.add('key');

music.on('destroy', listener);

music.destroy();


```

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.WebAudioSound](../class/sound-webaudiosound.md) | [Phaser.Sound.HTML5AudioSound](../class/sound-html5audiosound.md) | No | A reference to the Sound that emitted the event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/DESTROY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/DESTROY_EVENT.js#L7)  
> Since: 3.0.0

## DETUNE

**Description:** The Sound Detune Event.

This event is dispatched by both Web Audio and HTML5 Audio Sound objects when their detune value changes.

Listen to it from a Sound instance using `Sound.on('detune', listener)`, i.e.:

```
Copy
var music = this.sound.add('key');

music.on('detune', listener);

music.play();

music.setDetune(200);


```

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.WebAudioSound](../class/sound-webaudiosound.md) | [Phaser.Sound.HTML5AudioSound](../class/sound-html5audiosound.md) | No | A reference to the Sound that emitted the event. |
| --- | --- | --- | --- |
| detune | number | No | The new detune value of the Sound. |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/DETUNE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/DETUNE_EVENT.js#L7)  
> Since: 3.0.0

## GLOBAL\_DETUNE

**Description:** The Sound Manager Global Detune Event.

This event is dispatched by the Base Sound Manager, or more typically, an instance of the Web Audio Sound Manager,

or the HTML5 Audio Manager. It is dispatched when the `detune` property of the Sound Manager is changed, which globally

adjusts the detuning of all active sounds.

Listen to it from a Scene using: `this.sound.on('rate', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| soundManager | [Phaser.Sound.BaseSoundManager](../class/sound-basesoundmanager.md) | No | A reference to the sound manager that emitted the event. |
| --- | --- | --- | --- |
| detune | number | No | The updated detune value. |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/GLOBAL\_DETUNE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/GLOBAL_DETUNE_EVENT.js#L7)  
> Since: 3.0.0

## GLOBAL\_MUTE

**Description:** The Sound Manager Global Mute Event.

This event is dispatched by the Sound Manager when its `mute` property is changed, either directly

or via the `setMute` method. This changes the mute state of all active sounds.

Listen to it from a Scene using: `this.sound.on('mute', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| soundManager | [Phaser.Sound.WebAudioSoundManager](../class/sound-webaudiosoundmanager.md) | [Phaser.Sound.HTML5AudioSoundManager](../class/sound-html5audiosoundmanager.md) | No | A reference to the Sound Manager that emitted the event. |
| --- | --- | --- | --- |
| mute | boolean | No | The mute value. `true` if the Sound Manager is now muted, otherwise `false`. |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/GLOBAL\_MUTE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/GLOBAL_MUTE_EVENT.js#L7)  
> Since: 3.0.0

## GLOBAL\_RATE

**Description:** The Sound Manager Global Rate Event.

This event is dispatched by the Base Sound Manager, or more typically, an instance of the Web Audio Sound Manager,

or the HTML5 Audio Manager. It is dispatched when the `rate` property of the Sound Manager is changed, which globally

adjusts the playback rate of all active sounds.

Listen to it from a Scene using: `this.sound.on('rate', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| soundManager | [Phaser.Sound.BaseSoundManager](../class/sound-basesoundmanager.md) | No | A reference to the sound manager that emitted the event. |
| --- | --- | --- | --- |
| rate | number | No | The updated rate value. |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/GLOBAL\_RATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/GLOBAL_RATE_EVENT.js#L7)  
> Since: 3.0.0

## GLOBAL\_VOLUME

**Description:** The Sound Manager Global Volume Event.

This event is dispatched by the Sound Manager when its `volume` property is changed, either directly

or via the `setVolume` method. This changes the volume of all active sounds.

Listen to it from a Scene using: `this.sound.on('volume', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| soundManager | [Phaser.Sound.WebAudioSoundManager](../class/sound-webaudiosoundmanager.md) | [Phaser.Sound.HTML5AudioSoundManager](../class/sound-html5audiosoundmanager.md) | No | A reference to the sound manager that emitted the event. |
| --- | --- | --- | --- |
| volume | number | No | The new global volume of the Sound Manager. |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/GLOBAL\_VOLUME\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/GLOBAL_VOLUME_EVENT.js#L7)  
> Since: 3.0.0

## LOOPED

**Description:** The Sound Looped Event.

This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they loop during playback.

Listen to it from a Sound instance using `Sound.on('looped', listener)`, i.e.:

```
Copy
var music = this.sound.add('key');

music.on('looped', listener);

music.setLoop(true);

music.play();


```

This is not to be confused with the [LOOP]{@linkcode Phaser.Sound.Events#event:LOOP} event, which only emits when the loop state of a Sound is changed.

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.WebAudioSound](../class/sound-webaudiosound.md) | [Phaser.Sound.HTML5AudioSound](../class/sound-html5audiosound.md) | No | A reference to the Sound that emitted the event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/LOOPED\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/LOOPED_EVENT.js#L7)  
> Since: 3.0.0

## LOOP

**Description:** The Sound Loop Event.

This event is dispatched by both Web Audio and HTML5 Audio Sound objects when their loop state is changed.

Listen to it from a Sound instance using `Sound.on('loop', listener)`, i.e.:

```
Copy
var music = this.sound.add('key');

music.on('loop', listener);

music.setLoop(true);


```

This is not to be confused with the [LOOPED]{@linkcode Phaser.Sound.Events#event:LOOPED} event, which emits each time a Sound loops during playback.

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.WebAudioSound](../class/sound-webaudiosound.md) | [Phaser.Sound.HTML5AudioSound](../class/sound-html5audiosound.md) | No | A reference to the Sound that emitted the event. |
| --- | --- | --- | --- |
| loop | boolean | No | The new loop value. `true` if the Sound will loop, otherwise `false`. |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/LOOP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/LOOP_EVENT.js#L7)  
> Since: 3.0.0

## MUTE

**Description:** The Sound Mute Event.

This event is dispatched by both Web Audio and HTML5 Audio Sound objects when their mute state changes.

Listen to it from a Sound instance using `Sound.on('mute', listener)`, i.e.:

```
Copy
var music = this.sound.add('key');

music.on('mute', listener);

music.play();

music.setMute(true);


```

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.WebAudioSound](../class/sound-webaudiosound.md) | [Phaser.Sound.HTML5AudioSound](../class/sound-html5audiosound.md) | No | A reference to the Sound that emitted the event. |
| --- | --- | --- | --- |
| mute | boolean | No | The mute value. `true` if the Sound is now muted, otherwise `false`. |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/MUTE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/MUTE_EVENT.js#L7)  
> Since: 3.0.0

## PAN

**Description:** The Sound Pan Event.

This event is dispatched by both Web Audio and HTML5 Audio Sound objects when their pan changes.

Listen to it from a Sound instance using `Sound.on('pan', listener)`, i.e.:

```
Copy
var sound = this.sound.add('key');

sound.on('pan', listener);

sound.play();

sound.setPan(0.5);


```

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.WebAudioSound](../class/sound-webaudiosound.md) | [Phaser.Sound.HTML5AudioSound](../class/sound-html5audiosound.md) | No | A reference to the Sound that emitted the event. |
| --- | --- | --- | --- |
| pan | number | No | The new pan of the Sound. |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/PAN\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/PAN_EVENT.js#L7)  
> Since: 3.50.0

## PAUSE\_ALL

**Description:** The Pause All Sounds Event.

This event is dispatched by the Base Sound Manager, or more typically, an instance of the Web Audio Sound Manager,

or the HTML5 Audio Manager. It is dispatched when the `pauseAll` method is invoked and after all current Sounds

have been paused.

Listen to it from a Scene using: `this.sound.on('pauseall', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| soundManager | [Phaser.Sound.BaseSoundManager](../class/sound-basesoundmanager.md) | No | A reference to the sound manager that emitted the event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/PAUSE\_ALL\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/PAUSE_ALL_EVENT.js#L7)  
> Since: 3.0.0

## PAUSE

**Description:** The Sound Pause Event.

This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they are paused.

Listen to it from a Sound instance using `Sound.on('pause', listener)`, i.e.:

```
Copy
var music = this.sound.add('key');

music.on('pause', listener);

music.play();

music.pause();


```

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.WebAudioSound](../class/sound-webaudiosound.md) | [Phaser.Sound.HTML5AudioSound](../class/sound-html5audiosound.md) | No | A reference to the Sound that emitted the event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/PAUSE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/PAUSE_EVENT.js#L7)  
> Since: 3.0.0

## PLAY

**Description:** The Sound Play Event.

This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they are played.

Listen to it from a Sound instance using `Sound.on('play', listener)`, i.e.:

```
Copy
var music = this.sound.add('key');

music.on('play', listener);

music.play();


```

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.WebAudioSound](../class/sound-webaudiosound.md) | [Phaser.Sound.HTML5AudioSound](../class/sound-html5audiosound.md) | No | A reference to the Sound that emitted the event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/PLAY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/PLAY_EVENT.js#L7)  
> Since: 3.0.0

## RATE

**Description:** The Sound Rate Change Event.

This event is dispatched by both Web Audio and HTML5 Audio Sound objects when their rate changes.

Listen to it from a Sound instance using `Sound.on('rate', listener)`, i.e.:

```
Copy
var music = this.sound.add('key');

music.on('rate', listener);

music.play();

music.setRate(0.5);


```

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.WebAudioSound](../class/sound-webaudiosound.md) | [Phaser.Sound.HTML5AudioSound](../class/sound-html5audiosound.md) | No | A reference to the Sound that emitted the event. |
| --- | --- | --- | --- |
| rate | number | No | The new rate of the Sound. |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/RATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/RATE_EVENT.js#L7)  
> Since: 3.0.0

## RESUME\_ALL

**Description:** The Resume All Sounds Event.

This event is dispatched by the Base Sound Manager, or more typically, an instance of the Web Audio Sound Manager,

or the HTML5 Audio Manager. It is dispatched when the `resumeAll` method is invoked and after all current Sounds

have been resumed.

Listen to it from a Scene using: `this.sound.on('resumeall', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| soundManager | [Phaser.Sound.BaseSoundManager](../class/sound-basesoundmanager.md) | No | A reference to the sound manager that emitted the event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/RESUME\_ALL\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/RESUME_ALL_EVENT.js#L7)  
> Since: 3.0.0

## RESUME

**Description:** The Sound Resume Event.

This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they are resumed from a paused state.

Listen to it from a Sound instance using `Sound.on('resume', listener)`, i.e.:

```
Copy
var music = this.sound.add('key');

music.on('resume', listener);

music.play();

music.pause();

music.resume();


```

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.WebAudioSound](../class/sound-webaudiosound.md) | [Phaser.Sound.HTML5AudioSound](../class/sound-html5audiosound.md) | No | A reference to the Sound that emitted the event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/RESUME\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/RESUME_EVENT.js#L7)  
> Since: 3.0.0

## SEEK

**Description:** The Sound Seek Event.

This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they are seeked to a new position.

Listen to it from a Sound instance using `Sound.on('seek', listener)`, i.e.:

```
Copy
var music = this.sound.add('key');

music.on('seek', listener);

music.play();

music.setSeek(5000);


```

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.WebAudioSound](../class/sound-webaudiosound.md) | [Phaser.Sound.HTML5AudioSound](../class/sound-html5audiosound.md) | No | A reference to the Sound that emitted the event. |
| --- | --- | --- | --- |
| detune | number | No | The new detune value of the Sound. |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/SEEK\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/SEEK_EVENT.js#L7)  
> Since: 3.0.0

## STOP\_ALL

**Description:** The Stop All Sounds Event.

This event is dispatched by the Base Sound Manager, or more typically, an instance of the Web Audio Sound Manager,

or the HTML5 Audio Manager. It is dispatched when the `stopAll` method is invoked and after all current Sounds

have been stopped.

Listen to it from a Scene using: `this.sound.on('stopall', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| soundManager | [Phaser.Sound.BaseSoundManager](../class/sound-basesoundmanager.md) | No | A reference to the sound manager that emitted the event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/STOP\_ALL\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/STOP_ALL_EVENT.js#L7)  
> Since: 3.0.0

## STOP

**Description:** The Sound Stop Event.

This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they are stopped.

Listen to it from a Sound instance using `Sound.on('stop', listener)`, i.e.:

```
Copy
var music = this.sound.add('key');

music.on('stop', listener);

music.play();

music.stop();


```

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.WebAudioSound](../class/sound-webaudiosound.md) | [Phaser.Sound.HTML5AudioSound](../class/sound-html5audiosound.md) | No | A reference to the Sound that emitted the event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/STOP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/STOP_EVENT.js#L7)  
> Since: 3.0.0

## UNLOCKED

**Description:** The Sound Manager Unlocked Event.

This event is dispatched by the Base Sound Manager, or more typically, an instance of the Web Audio Sound Manager,

or the HTML5 Audio Manager. It is dispatched during the update loop when the Sound Manager becomes unlocked. For

Web Audio this is on the first user gesture on the page.

Listen to it from a Scene using: `this.sound.on('unlocked', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| soundManager | [Phaser.Sound.BaseSoundManager](../class/sound-basesoundmanager.md) | No | A reference to the sound manager that emitted the event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/UNLOCKED\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/UNLOCKED_EVENT.js#L7)  
> Since: 3.0.0

## VOLUME

**Description:** The Sound Volume Event.

This event is dispatched by both Web Audio and HTML5 Audio Sound objects when their volume changes.

Listen to it from a Sound instance using `Sound.on('volume', listener)`, i.e.:

```
Copy
var music = this.sound.add('key');

music.on('volume', listener);

music.play();

music.setVolume(0.5);


```

| name | type | optional | description |
| --- | --- | --- | --- |
| sound | [Phaser.Sound.WebAudioSound](../class/sound-webaudiosound.md) | [Phaser.Sound.HTML5AudioSound](../class/sound-html5audiosound.md) | No | A reference to the Sound that emitted the event. |
| --- | --- | --- | --- |
| volume | number | No | The new volume of the Sound. |

**Member of:** [Phaser.Sound.Events](../namespace/sound-events.md)

> Source: [src/sound/events/VOLUME\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/events/VOLUME_EVENT.js#L7)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Sound.Events](#soundevents)

  + [COMPLETE](#complete)
  + [DECODED\_ALL](#decoded_all)
  + [DECODED](#decoded)
  + [DESTROY](#destroy)
  + [DETUNE](#detune)
  + [GLOBAL\_DETUNE](#global_detune)
  + [GLOBAL\_MUTE](#global_mute)
  + [GLOBAL\_RATE](#global_rate)
  + [GLOBAL\_VOLUME](#global_volume)
  + [LOOPED](#looped)
  + [LOOP](#loop)
  + [MUTE](#mute)
  + [PAN](#pan)
  + [PAUSE\_ALL](#pause_all)
  + [PAUSE](#pause)
  + [PLAY](#play)
  + [RATE](#rate)
  + [RESUME\_ALL](#resume_all)
  + [RESUME](#resume)
  + [SEEK](#seek)
  + [STOP\_ALL](#stop_all)
  + [STOP](#stop)
  + [UNLOCKED](#unlocked)
  + [VOLUME](#volume)

Back to top

©2025[Phaser](https://docs.phaser.io)



Sound.Events