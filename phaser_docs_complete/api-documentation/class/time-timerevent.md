# TimerEvent

Phaser.Time.TimerEvent

A Timer Event represents a delayed function call. It's managed by a Scene's [Clock](Clock.md) and will call its function after a set amount of time has passed. The Timer Event can optionally repeat - i.e. call its function multiple times before finishing, or loop indefinitely.

Because it's managed by a Clock, a Timer Event is based on game time, will be affected by its Clock's time scale, and will pause if its Clock pauses.

**Constructor**

`new TimerEvent(config)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Time.TimerEventConfig](../typedef/types-time.md) | No | The configuration for the Timer Event, including its delay and callback. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/time/TimerEvent.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L10)  
> Since: 3.0.0

# Public Members

## args

### args: array

**Description:**

Additional arguments to be passed to the callback.

> Source: [src/time/TimerEvent.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L90)  
> Since: 3.0.0

---

## callback

### callback: function

**Description:**

The callback that will be called when the TimerEvent occurs.

> Source: [src/time/TimerEvent.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L72)  
> Since: 3.0.0

---

## callbackScope

### callbackScope: object

**Description:**

The scope in which the callback will be called.

> Source: [src/time/TimerEvent.js#L81](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L81)  
> Since: 3.0.0

---

## delay

### delay: number

**Description:**

The delay in ms at which this TimerEvent fires.

> Source: [src/time/TimerEvent.js#L29](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L29)  
> Since: 3.0.0

---

## elapsed

### elapsed: number

**Description:**

The time in milliseconds which has elapsed since the Timer Event's creation.

This value is local for the Timer Event and is relative to its Clock. As such, it's influenced by the Clock's time scale and paused state, the Timer Event's initial <#startAt> property, and the Timer Event's <#timeScale> and <#paused> state.

> Source: [src/time/TimerEvent.js#L119](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L119)  
> Since: 3.0.0

---

## hasDispatched

### hasDispatched: boolean

**Description:**

Whether the Timer Event's function has been called.

When the Timer Event fires, this property will be set to `true` before the callback function is invoked and will be reset immediately afterward if the Timer Event should repeat. The value of this property does not directly influence whether the Timer Event will be removed from its Clock, but can prevent it from firing.

> Source: [src/time/TimerEvent.js#L141](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L141)  
> Since: 3.0.0

---

## loop

### loop: boolean

**Description:**

True if this TimerEvent loops, otherwise false.

> Source: [src/time/TimerEvent.js#L61](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L61)  
> Since: 3.0.0

---

## paused

### paused: boolean

**Description:**

Whether or not this timer is paused.

> Source: [src/time/TimerEvent.js#L131](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L131)  
> Since: 3.0.0

---

## repeat

### repeat: number

**Description:**

The total number of times this TimerEvent will repeat before finishing.

> Source: [src/time/TimerEvent.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L40)  
> Since: 3.0.0

---

## repeatCount

### repeatCount: number

**Description:**

If repeating this contains the current repeat count.

> Source: [src/time/TimerEvent.js#L51](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L51)  
> Since: 3.0.0

---

## startAt

### startAt: number

**Description:**

Start this many MS into the elapsed (useful if you want a long duration with repeat, but for the first loop to fire quickly)

> Source: [src/time/TimerEvent.js#L109](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L109)  
> Since: 3.0.0

---

## timeScale

### timeScale: number

**Description:**

Scale the time causing this TimerEvent to update.

> Source: [src/time/TimerEvent.js#L99](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L99)  
> Since: 3.0.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Destroys all object references in the Timer Event, i.e. its callback, scope, and arguments.

Normally, this method is only called by the Clock when it shuts down. As such, it doesn't stop the Timer Event. If called manually, the Timer Event will still be updated by the Clock, but it won't do anything when it fires.

> Source: [src/time/TimerEvent.js#L347](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L347)  
> Since: 3.0.0

---

## getElapsed

### <instance> getElapsed()

**Description:**

Returns the local elapsed time for the current iteration of the Timer Event.

**Returns:** number - The local elapsed time in milliseconds.

> Source: [src/time/TimerEvent.js#L250](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L250)  
> Since: 3.0.0

---

## getElapsedSeconds

### <instance> getElapsedSeconds()

**Description:**

Returns the local elapsed time for the current iteration of the Timer Event in seconds.

**Returns:** number - The local elapsed time in seconds.

> Source: [src/time/TimerEvent.js#L263](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L263)  
> Since: 3.0.0

---

## getOverallProgress

### <instance> getOverallProgress()

**Description:**

Gets the progress of the timer overall, factoring in repeats.

**Returns:** number - The overall progress of the Timer Event, between 0 and 1.

> Source: [src/time/TimerEvent.js#L212](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L212)  
> Since: 3.0.0

---

## getOverallRemaining

### <instance> getOverallRemaining()

**Description:**

Returns the time interval until the last iteration of the Timer Event.

**Returns:** number - The time interval in milliseconds.

> Source: [src/time/TimerEvent.js#L302](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L302)  
> Since: 3.50.0

---

## getOverallRemainingSeconds

### <instance> getOverallRemainingSeconds()

**Description:**

Returns the time interval until the last iteration of the Timer Event in seconds.

**Returns:** number - The time interval in seconds.

> Source: [src/time/TimerEvent.js#L315](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L315)  
> Since: 3.50.0

---

## getProgress

### <instance> getProgress()

**Description:**

Gets the progress of the current iteration, not factoring in repeats.

**Returns:** number - A number between 0 and 1 representing the current progress.

> Source: [src/time/TimerEvent.js#L199](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L199)  
> Since: 3.0.0

---

## getRemaining

### <instance> getRemaining()

**Description:**

Returns the time interval until the next iteration of the Timer Event.

**Returns:** number - The time interval in milliseconds.

> Source: [src/time/TimerEvent.js#L276](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L276)  
> Since: 3.50.0

---

## getRemainingSeconds

### <instance> getRemainingSeconds()

**Description:**

Returns the time interval until the next iteration of the Timer Event in seconds.

**Returns:** number - The time interval in seconds.

> Source: [src/time/TimerEvent.js#L289](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L289)  
> Since: 3.50.0

---

## getRepeatCount

### <instance> getRepeatCount()

**Description:**

Returns the number of times this Timer Event will repeat before finishing.

This should not be confused with the number of times the Timer Event will fire before finishing. A return value of 0 doesn't indicate that the Timer Event has finished running - it indicates that it will not repeat after the next time it fires.

**Returns:** number - How many times the Timer Event will repeat.

> Source: [src/time/TimerEvent.js#L235](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L235)  
> Since: 3.0.0

---

## remove

### <instance> remove([dispatchCallback])

**Description:**

Forces the Timer Event to immediately expire, thus scheduling its removal in the next frame.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| dispatchCallback | boolean | Yes | false | If `true`, the function of the Timer Event will be called before its removal. |
| --- | --- | --- | --- | --- |

> Source: [src/time/TimerEvent.js#L328](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L328)  
> Since: 3.0.0

---

## reset

### <instance> reset(config)

**Description:**

Completely reinitializes the Timer Event, regardless of its current state, according to a configuration object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Time.TimerEventConfig](../typedef/types-time.md) | No | The new state for the Timer Event. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Time.TimerEvent](time-timerevent.md) - This TimerEvent object.

> Source: [src/time/TimerEvent.js#L156](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/TimerEvent.js#L156)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [args](#args)

    - [args: array](#args-array)
  + [callback](#callback)

    - [callback: function](#callback-function)
  + [callbackScope](#callbackscope)

    - [callbackScope: object](#callbackscope-object)
  + [delay](#delay)

    - [delay: number](#delay-number)
  + [elapsed](#elapsed)

    - [elapsed: number](#elapsed-number)
  + [hasDispatched](#hasdispatched)

    - [hasDispatched: boolean](#hasdispatched-boolean)
  + [loop](#loop)

    - [loop: boolean](#loop-boolean)
  + [paused](#paused)

    - [paused: boolean](#paused-boolean)
  + [repeat](#repeat)

    - [repeat: number](#repeat-number)
  + [repeatCount](#repeatcount)

    - [repeatCount: number](#repeatcount-number)
  + [startAt](#startat)

    - [startAt: number](#startat-number)
  + [timeScale](#timescale)

    - [timeScale: number](#timescale-number)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [getElapsed](#getelapsed)

    - [<instance> getElapsed()](#instance-getelapsed)
  + [getElapsedSeconds](#getelapsedseconds)

    - [<instance> getElapsedSeconds()](#instance-getelapsedseconds)
  + [getOverallProgress](#getoverallprogress)

    - [<instance> getOverallProgress()](#instance-getoverallprogress)
  + [getOverallRemaining](#getoverallremaining)

    - [<instance> getOverallRemaining()](#instance-getoverallremaining)
  + [getOverallRemainingSeconds](#getoverallremainingseconds)

    - [<instance> getOverallRemainingSeconds()](#instance-getoverallremainingseconds)
  + [getProgress](#getprogress)

    - [<instance> getProgress()](#instance-getprogress)
  + [getRemaining](#getremaining)

    - [<instance> getRemaining()](#instance-getremaining)
  + [getRemainingSeconds](#getremainingseconds)

    - [<instance> getRemainingSeconds()](#instance-getremainingseconds)
  + [getRepeatCount](#getrepeatcount)

    - [<instance> getRepeatCount()](#instance-getrepeatcount)
  + [remove](#remove)

    - [<instance> remove([dispatchCallback])](#instance-removedispatchcallback)
  + [reset](#reset)

    - [<instance> reset(config)](#instance-resetconfig)

Back to top

©2025[Phaser](https://docs.phaser.io)