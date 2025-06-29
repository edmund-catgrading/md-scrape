# TweenChain

Phaser.Tweens.TweenChain

A TweenChain is a special type of Tween that allows you to create a sequence of Tweens, chained to one-another,

and add them to the Tween Manager.

The tweens are played in order, from start to finish. You can optionally set the chain

to repeat as many times as you like. Once the chain has finished playing, or repeating if set,

all tweens in the chain will be destroyed automatically. To override this, set the 'persist'

argument to 'true'.

Playback will start immediately unless the *first* Tween has been configured to be paused.

Please note that Tweens will not manipulate any target property that begins with an underscore.

**Constructor**

`new TweenChain(parent)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| parent | [Phaser.Tweens.TweenManager](tweens-tweenmanager.md) | [Phaser.Tweens.TweenChain](tweens-tweenchain.md) | No | A reference to the Tween Manager, or TweenChain, that owns this TweenChain. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.Tweens.BaseTween](tweens-basetween.md)

> Source: [src/tweens/tween/TweenChain.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L15)  
> Since: 3.60.0

# Public Members

## callbacks

### callbacks: [Phaser.Types.Tweens.TweenCallbacks](../typedef/types-tweens.md)

**Description:**

An object containing the different Tween callback functions.

You can either set these in the Tween config, or by calling the `Tween.setCallback` method.

The types available are:

`onActive` - When the Tween is first created it moves to an 'active' state when added to the Tween Manager. 'Active' does not mean 'playing'.

`onStart` - When the Tween starts playing after a delayed or paused state. This will happen at the same time as `onActive` if the tween has no delay and isn't paused.

`onLoop` - When a Tween loops, if it has been set to do so. This happens *after* the `loopDelay` expires, if set.

`onComplete` - When the Tween finishes playback fully. Never invoked if the Tween is set to repeat infinitely.

`onStop` - Invoked only if the `Tween.stop` method is called.

`onPause` - Invoked only if the `Tween.pause` method is called. Not invoked if the Tween Manager is paused.

`onResume` - Invoked only if the `Tween.resume` method is called. Not invoked if the Tween Manager is resumed.

The following types are also available and are invoked on a `TweenData` level - that is per-object, per-property, being tweened.

`onYoyo` - When a TweenData starts a yoyo. This happens *after* the `hold` delay expires, if set.

`onRepeat` - When a TweenData repeats playback. This happens *after* the `repeatDelay` expires, if set.

`onUpdate` - When a TweenData updates a property on a source target during playback.

**Inherits:** [Phaser.Tweens.BaseTween#callbacks](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L195](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L195)  
> Since: 3.60.0

---

## callbackScope

### callbackScope: any

**Description:**

The scope (or context) in which all of the callbacks are invoked.

This defaults to be this Tween, but you can override this property

to set it to whatever object you require.

**Inherits:** [Phaser.Tweens.BaseTween#callbackScope](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L233](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L233)  
> Since: 3.60.0

---

## completeDelay

### completeDelay: number

**Description:**

The time in milliseconds before the 'onComplete' event fires.

This never fires if `loop = -1` as it never completes because it has been

set to loop forever.

**Inherits:** [Phaser.Tweens.BaseTween#completeDelay](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L149)  
> Since: 3.60.0

---

## countdown

### countdown: number

**Description:**

An internal countdown timer (used by loopDelay and completeDelay)

**Inherits:** [Phaser.Tweens.BaseTween#countdown](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L162](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L162)  
> Since: 3.60.0

---

## currentIndex

### currentIndex: number

**Description:**

A reference to the data array index of the currently playing tween.

> Source: [src/tweens/tween/TweenChain.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L56)  
> Since: 3.60.0

---

## currentTween

### currentTween: [Phaser.Tweens.Tween](tweens-tween.md)

**Description:**

A reference to the Tween that this TweenChain is currently playing.

> Source: [src/tweens/tween/TweenChain.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L47)  
> Since: 3.60.0

---

## data

### data: Array.<[Phaser.Tweens.TweenData](tweens-tweendata.md)>, Array.<[Phaser.Tweens.Tween](tweens-tween.md)>

**Description:**

The main data array. For a Tween, this contains all of the `TweenData` objects, each

containing a unique property and target that is being tweened.

For a TweenChain, this contains an array of `Tween` instances, which are being played

through in sequence.

**Inherits:** [Phaser.Tweens.BaseTween#data](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L47)  
> Since: 3.60.0

---

## hasStarted

### hasStarted: boolean

**Description:**

Has this Tween started playback yet?

This boolean is toggled when the Tween leaves the 'start delayed' state and begins running.

**Inherits:** [Phaser.Tweens.BaseTween#hasStarted](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L82](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L82)  
> Since: 3.60.0

---

## loop

### loop: number

**Description:**

The number of times this Tween will loop.

Can be -1 for an infinite loop, zero for none, or a positive integer.

Typically this is set in the configuration object, but can also be set directly

as long as this Tween is paused and hasn't started playback.

When enabled it will play through ALL Tweens again.

Use TweenData.repeat to loop a single element.

**Inherits:** [Phaser.Tweens.BaseTween#loop](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L108](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L108)  
> Since: 3.60.0

---

## loopCounter

### loopCounter: number

**Description:**

Internal counter recording how many loops are left to run.

**Inherits:** [Phaser.Tweens.BaseTween#loopCounter](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L139)  
> Since: 3.60.0

---

## loopDelay

### loopDelay: number

**Description:**

The time in milliseconds before the Tween loops.

Only used if `loop` is > 0.

**Inherits:** [Phaser.Tweens.BaseTween#loopDelay](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L127](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L127)  
> Since: 3.60.0

---

## parent

### parent: [Phaser.Tweens.TweenManager](tweens-tweenmanager.md), [Phaser.Tweens.TweenChain](tweens-tweenchain.md)

**Description:**

A reference to the Tween Manager, or Tween Chain, that owns this Tween.

**Inherits:** [Phaser.Tweens.BaseTween#parent](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L38)  
> Since: 3.60.0

---

## paused

### paused: boolean

**Description:**

Is the Tween currently paused?

A paused Tween needs to be started with the `play` method, or resumed with the `resume` method.

This property can be toggled at runtime if required.

**Inherits:** [Phaser.Tweens.BaseTween#paused](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L181](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L181)  
> Since: 3.60.0

---

## persist

### persist: boolean

**Description:**

Will this Tween persist after playback? A Tween that persists will *not* be destroyed by the

Tween Manager, or when calling `Tween.stop`, and can be re-played as required. You can either

set this property when creating the tween in the tween config, or set it *prior* to playback.

However, it's up to you to ensure you destroy persistent tweens when you are finished with them,

or they will retain references you may no longer require and waste memory.

By default, `Tweens` are set to *not* persist, so they are automatically cleaned-up by

the Tween Manager.

**Inherits:** [Phaser.Tweens.BaseTween#persist](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L245](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L245)  
> Since: 3.60.0

---

## startDelay

### startDelay: number

**Description:**

The time in milliseconds before the 'onStart' event fires.

For a Tween, this is the shortest `delay` value across all of the TweenDatas it owns.

For a TweenChain, it is whatever delay value was given in the configuration.

**Inherits:** [Phaser.Tweens.BaseTween#startDelay](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L69](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L69)  
> Since: 3.60.0

---

## state

### state: [Phaser.Tweens.StateType](../typedef/tweens.md)

**Description:**

The current state of the Tween.

**Inherits:** [Phaser.Tweens.BaseTween#state](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L172)  
> Since: 3.60.0

---

## timeScale

### timeScale: number

**Description:**

Scales the time applied to this Tween. A value of 1 runs in real-time. A value of 0.5 runs 50% slower, and so on.

The value isn't used when calculating total duration of the tween, it's a run-time delta adjustment only.

This value is multiplied by the `TweenManager.timeScale`.

**Inherits:** [Phaser.Tweens.BaseTween#timeScale](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L94](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L94)  
> Since: 3.60.0

---

## totalData

### totalData: number

**Description:**

The cached size of the data array.

**Inherits:** [Phaser.Tweens.BaseTween#totalData](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L60](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L60)  
> Since: 3.60.0

---

# Public Methods

## add

### <instance> add(tweens)

**Description:**

Create a sequence of Tweens, chained to one-another, and add them to this Tween Manager.

The tweens are played in order, from start to finish. You can optionally set the chain

to repeat as many times as you like. Once the chain has finished playing, or repeating if set,

all tweens in the chain will be destroyed automatically. To override this, set the 'persist'

argument to 'true'.

Playback will start immediately unless the *first* Tween has been configured to be paused.

Please note that Tweens will not manipulate any target property that begins with an underscore.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tweens | Array.<[Phaser.Types.Tweens.TweenBuilderConfig](../typedef/types-tweens.md)> | Array.<object> | No | An array of Tween configuration objects for the Tweens in this chain. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This TweenChain instance.

> Source: [src/tweens/tween/TweenChain.js#L95](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L95)  
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

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## complete

### <instance> complete([delay])

**Description:**

Flags the Tween as being complete, whatever stage of progress it is at.

If an `onComplete` callback has been defined it will automatically invoke it, unless a `delay`

argument is provided, in which case the Tween will delay for that period of time before calling the callback.

If you don't need a delay or don't have an `onComplete` callback then call `Tween.stop` instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| delay | number | Yes | 0 | The time to wait before invoking the complete callback. If zero it will fire immediately. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This Tween instance.

**Fires:** [Phaser.Tweens.Events#event:TWEEN\_COMPLETE](../event/tweens-events.md)

**Inherits:** [Phaser.Tweens.BaseTween#complete](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L404](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L404)  
> Since: 3.2.0

---

## completeAfterLoop

### <instance> completeAfterLoop([loops])

**Description:**

Flags the Tween as being complete only once the current loop has finished.

This is a useful way to stop an infinitely looping tween once a complete cycle is over,

rather than abruptly.

If you don't have a loop then call `Tween.stop` instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| loops | number | Yes | 0 | The number of loops that should finish before this tween completes. Zero means complete just the current loop. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This Tween instance.

**Fires:** [Phaser.Tweens.Events#event:TWEEN\_COMPLETE](../event/tweens-events.md)

**Inherits:** [Phaser.Tweens.BaseTween#completeAfterLoop](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L438](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L438)  
> Since: 3.60.0

---

## destroy

### <instance> destroy()

**Description:**

Immediately destroys this TweenChain, nulling of all its references.

**Overrides:** Phaser.Tweens.BaseTween#destroy

> Source: [src/tweens/tween/TweenChain.js#L514](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L514)  
> Since: 3.60.0

---

## dispatchEvent

### <instance> dispatchEvent(event, [callback])

**Description:**

Internal method that will emit a TweenChain based Event and invoke the given callback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Types.Tweens.Event](../typedef/types-tweens.md) | No | The Event to be dispatched. |
| --- | --- | --- | --- |
| callback | [Phaser.Types.Tweens.TweenCallbackTypes](../typedef/types-tweens.md) | Yes | The name of the callback to be invoked. Can be `null` or `undefined` to skip invocation. |

> Source: [src/tweens/tween/TweenChain.js#L493](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L493)  
> Since: 3.60.0

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

## getTimeScale

### <instance> getTimeScale()

**Description:**

Gets the value of the time scale applied to this Tween. A value of 1 runs in real-time.

A value of 0.5 runs 50% slower, and so on.

**Returns:** number - The value of the time scale applied to this Tween.

**Inherits:** [Phaser.Tweens.BaseTween#getTimeScale](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L285](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L285)  
> Since: 3.60.0

---

## hasTarget

### <instance> hasTarget(target)

**Description:**

See if any of the tweens in this Tween Chain is currently acting upon the given target.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | object | No | The target to check against this TweenChain. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the given target is a target of this TweenChain, otherwise `false`.

> Source: [src/tweens/tween/TweenChain.js#L172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L172)  
> Since: 3.60.0

---

## init

### <instance> init()

**Description:**

Prepares this TweenChain for playback.

Called automatically by the TweenManager. Should not be called directly.

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This TweenChain instance.

**Fires:** [Phaser.Tweens.Events#event:TWEEN\_ACTIVE](../event/tweens-events.md)

> Source: [src/tweens/tween/TweenChain.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L66)  
> Since: 3.60.0

---

## isActive

### <instance> isActive()

**Description:**

Returns `true` if this Tween has a *current* state of ACTIVE, otherwise `false`.

**Returns:** boolean - `true` if this Tween has a *current* state of ACTIVE, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTween#isActive](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L747](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L747)  
> Since: 3.60.0

---

## isCompleteDelayed

### <instance> isCompleteDelayed()

**Description:**

Returns `true` if this Tween has a *current* state of COMPLETE\_DELAY, otherwise `false`.

**Returns:** boolean - `true` if this Tween has a *current* state of COMPLETE\_DELAY, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTween#isCompleteDelayed](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L773](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L773)  
> Since: 3.60.0

---

## isDestroyed

### <instance> isDestroyed()

**Description:**

Returns `true` if this Tween has a *current* state of DESTROYED, otherwise `false`.

**Returns:** boolean - `true` if this Tween has a *current* state of DESTROYED, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTween#isDestroyed](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L838](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L838)  
> Since: 3.60.0

---

## isFinished

### <instance> isFinished()

**Description:**

Returns `true` if this Tween has a *current* state of FINISHED, otherwise `false`.

**Returns:** boolean - `true` if this Tween has a *current* state of FINISHED, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTween#isFinished](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L825](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L825)  
> Since: 3.60.0

---

## isLoopDelayed

### <instance> isLoopDelayed()

**Description:**

Returns `true` if this Tween has a *current* state of LOOP\_DELAY, otherwise `false`.

**Returns:** boolean - `true` if this Tween has a *current* state of LOOP\_DELAY, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTween#isLoopDelayed](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L760](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L760)  
> Since: 3.60.0

---

## isPaused

### <instance> isPaused()

**Description:**

Checks if the Tween is currently paused.

This is the same as inspecting the `BaseTween.paused` property directly.

**Returns:** boolean - `true` if the Tween is paused, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTween#isPaused](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L314](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L314)  
> Since: 3.60.0

---

## isPending

### <instance> isPending()

**Description:**

Returns `true` if this Tween has a *current* state of PENDING, otherwise `false`.

**Returns:** boolean - `true` if this Tween has a *current* state of PENDING, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTween#isPending](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L734](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L734)  
> Since: 3.60.0

---

## isPendingRemove

### <instance> isPendingRemove()

**Description:**

Returns `true` if this Tween has a *current* state of PENDING\_REMOVE, otherwise `false`.

**Returns:** boolean - `true` if this Tween has a *current* state of PENDING\_REMOVE, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTween#isPendingRemove](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L799](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L799)  
> Since: 3.60.0

---

## isPlaying

### <instance> isPlaying()

**Description:**

Checks if this Tween is currently playing.

If this Tween is paused, or not active, this method will return false.

**Returns:** boolean - `true` if the Tween is playing, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTween#isPlaying](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L299](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L299)  
> Since: 3.60.0

---

## isRemoved

### <instance> isRemoved()

**Description:**

Returns `true` if this Tween has a *current* state of REMOVED, otherwise `false`.

**Returns:** boolean - `true` if this Tween has a *current* state of REMOVED, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTween#isRemoved](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L812](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L812)  
> Since: 3.60.0

---

## isStartDelayed

### <instance> isStartDelayed()

**Description:**

Returns `true` if this Tween has a *current* state of START\_DELAY, otherwise `false`.

**Returns:** boolean - `true` if this Tween has a *current* state of START\_DELAY, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTween#isStartDelayed](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L786](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L786)  
> Since: 3.60.0

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

## makeActive

### <instance> makeActive(tween)

**Description:**

Re-initialises the given Tween and sets it to the Active state.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](tweens-tween.md) | No | The Tween to check. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This TweenChain instance.

> Source: [src/tweens/tween/TweenChain.js#L251](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L251)  
> Since: 3.60.0

---

## makeActive

### <instance> makeActive(tween)

**Description:**

Re-initialises the given Tween and sets it to the Active state.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](tweens-tween.md) | No | The Tween to check. |
| --- | --- | --- | --- |

**Overrides:** Phaser.Tweens.BaseTween#makeActive

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This TweenChain instance.

**Fires:** [Phaser.Tweens.Events#event:TWEEN\_ACTIVE](../event/tweens-events.md)

**Inherits:** [Phaser.Tweens.TweenChain#makeActive](tweens-tweenchain.md)

> Source: [src/tweens/tween/TweenChain.js#L251](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L251)  
> Since: 3.60.0

---

## nextState

### <instance> nextState()

**Description:**

Internal method that advances to the next state of the TweenChain playback.

**Returns:** boolean - `true` if this TweenChain has completed, otherwise `false`.

**Fires:** [Phaser.Tweens.Events#event:TWEEN\_COMPLETE](../event/tweens-events.md), [Phaser.Tweens.Events#event:TWEEN\_LOOP](../event/tweens-events.md)

> Source: [src/tweens/tween/TweenChain.js#L271](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L271)  
> Since: 3.60.0

---

## nextTween

### <instance> nextTween()

**Description:**

Immediately advances to the next Tween in the chain.

This is typically called internally, but can be used if you need to

advance playback for some reason.

**Returns:** boolean - `true` if there are no more Tweens in the chain, otherwise `false`.

> Source: [src/tweens/tween/TweenChain.js#L448](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L448)  
> Since: 3.60.0

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

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - `this`.

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

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - `this`.

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

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## onCompleteHandler

### <instance> onCompleteHandler()

**Description:**

Internal method that handles this tween completing and emitting the onComplete event

and callback.

**Inherits:** [Phaser.Tweens.BaseTween#onCompleteHandler](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L390](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L390)  
> Since: 3.60.0

---

## pause

### <instance> pause()

**Description:**

Pauses the Tween immediately. Use `resume` to continue playback.

You can also toggle the `Tween.paused` boolean property, but doing so will not trigger the PAUSE event.

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This Tween instance.

**Fires:** [Phaser.Tweens.Events#event:TWEEN\_PAUSE](../event/tweens-events.md)

**Inherits:** [Phaser.Tweens.BaseTween#pause](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L329](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L329)  
> Since: 3.60.0

---

## play

### <instance> play()

**Description:**

Starts this TweenChain playing.

You only need to call this method if you have configured this TweenChain to be paused on creation.

If the TweenChain is already playing, calling this method again will have no effect. If you wish to

restart the chain, use `TweenChain.restart` instead.

Calling this method after the TweenChain has completed will start the chain playing again from the beginning.

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This TweenChain instance.

> Source: [src/tweens/tween/TweenChain.js#L318](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L318)  
> Since: 3.60.0

---

## remove

### <instance> remove(tween)

**Description:**

Removes the given Tween from this Tween Chain.

The removed tween is *not* destroyed. It is just removed from this Tween Chain.

If the given Tween is currently playing then the chain will automatically move

to the next tween in the chain. If there are no more tweens, this chain will complete.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](tweens-tween.md) | No | The Tween to be removed. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This Tween Chain instance.

> Source: [src/tweens/tween/TweenChain.js#L139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L139)  
> Since: 3.60.0

---

## remove

### <instance> remove(tween)

**Description:**

Removes the given Tween from this Tween Chain.

The removed tween is *not* destroyed. It is just removed from this Tween Chain.

If the given Tween is currently playing then the chain will automatically move

to the next tween in the chain. If there are no more tweens, this chain will complete.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](tweens-tween.md) | No | The Tween to be removed. |
| --- | --- | --- | --- |

**Overrides:** Phaser.Tweens.BaseTween#remove

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This Tween Chain instance.

**Inherits:** [Phaser.Tweens.TweenChain#remove](tweens-tweenchain.md)

> Source: [src/tweens/tween/TweenChain.js#L139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L139)  
> Since: 3.60.0

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

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - `this`.

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

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## reset

### <instance> reset(tween)

**Description:**

Resets the given Tween.

It will seek to position 0 and playback will start on the next frame.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](tweens-tween.md) | No | The Tween to be reset. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This TweenChain instance.

> Source: [src/tweens/tween/TweenChain.js#L230](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L230)  
> Since: 3.60.0

---

## resetTweens

### <instance> resetTweens()

**Description:**

Internal method that resets all of the Tweens and the current index pointer.

> Source: [src/tweens/tween/TweenChain.js#L361](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L361)  
> Since: 3.60.0

---

## restart

### <instance> restart()

**Description:**

Restarts the TweenChain from the beginning.

If this TweenChain was configured to have a loop, or start delay, those

are reset to their initial values as well. It will also dispatch the

`onActive` callback and event again.

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This TweenChain instance.

> Source: [src/tweens/tween/TweenChain.js#L197](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L197)  
> Since: 3.60.0

---

## resume

### <instance> resume()

**Description:**

Resumes the playback of a previously paused Tween.

You can also toggle the `Tween.paused` boolean property, but doing so will not trigger the RESUME event.

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This Tween instance.

**Fires:** [Phaser.Tweens.Events#event:TWEEN\_RESUME](../event/tweens-events.md)

**Inherits:** [Phaser.Tweens.BaseTween#resume](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L352](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L352)  
> Since: 3.60.0

---

## setActiveState

### <instance> setActiveState()

**Description:**

Sets this Tween state to ACTIVE.

**Inherits:** [Phaser.Tweens.BaseTween#setActiveState](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L640](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L640)  
> Since: 3.60.0

---

## setCallback

### <instance> setCallback(type, callback, [params])

**Description:**

Sets an event based callback to be invoked during playback.

Calling this method will replace a previously set callback for the given type, if any exists.

The types available are:

`onActive` - When the Tween is first created it moves to an 'active' state when added to the Tween Manager. 'Active' does not mean 'playing'.

`onStart` - When the Tween starts playing after a delayed or paused state. This will happen at the same time as `onActive` if the tween has no delay and isn't paused.

`onLoop` - When a Tween loops, if it has been set to do so. This happens *after* the `loopDelay` expires, if set.

`onComplete` - When the Tween finishes playback fully. Never invoked if the Tween is set to repeat infinitely.

`onStop` - Invoked only if the `Tween.stop` method is called.

`onPause` - Invoked only if the `Tween.pause` method is called. Not invoked if the Tween Manager is paused.

`onResume` - Invoked only if the `Tween.resume` method is called. Not invoked if the Tween Manager is resumed.

The following types are also available and are invoked on a `TweenData` level - that is per-object, per-property, being tweened.

`onYoyo` - When a TweenData starts a yoyo. This happens *after* the `hold` delay expires, if set.

`onRepeat` - When a TweenData repeats playback. This happens *after* the `repeatDelay` expires, if set.

`onUpdate` - When a TweenData updates a property on a source target during playback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| type | [Phaser.Types.Tweens.TweenCallbackTypes](../typedef/types-tweens.md) | No | The type of callback to set. One of: `onActive`, `onComplete`, `onLoop`, `onPause`, `onRepeat`, `onResume`, `onStart`, `onStop`, `onUpdate` or `onYoyo`. |
| --- | --- | --- | --- |
| callback | function | No | Your callback that will be invoked. |
| params | array | Yes | The parameters to pass to the callback. Pass an empty array if you don't want to define any, but do wish to set the scope. |

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This Tween instance.

**Inherits:** [Phaser.Tweens.BaseTween#setCallback](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L587](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L587)  
> Since: 3.60.0

---

## setCompleteDelayState

### <instance> setCompleteDelayState()

**Description:**

Sets this Tween state to COMPLETE\_DELAY.

**Inherits:** [Phaser.Tweens.BaseTween#setCompleteDelayState](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L664](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L664)  
> Since: 3.60.0

---

## setCurrentTween

### <instance> setCurrentTween(index)

**Description:**

Sets the current active Tween to the given index, based on its

entry in the TweenChain data array.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| index | number | No | The index of the Tween to be made current. |
| --- | --- | --- | --- |

> Source: [src/tweens/tween/TweenChain.js#L475](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L475)  
> Since: 3.60.0

---

## setDestroyedState

### <instance> setDestroyedState()

**Description:**

Sets this Tween state to DESTROYED.

**Inherits:** [Phaser.Tweens.BaseTween#setDestroyedState](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L723](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L723)  
> Since: 3.60.0

---

## setFinishedState

### <instance> setFinishedState()

**Description:**

Sets this Tween state to FINISHED.

**Inherits:** [Phaser.Tweens.BaseTween#setFinishedState](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L712](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L712)  
> Since: 3.60.0

---

## setLoopDelayState

### <instance> setLoopDelayState()

**Description:**

Sets this Tween state to LOOP\_DELAY.

**Inherits:** [Phaser.Tweens.BaseTween#setLoopDelayState](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L653](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L653)  
> Since: 3.60.0

---

## setPendingRemoveState

### <instance> setPendingRemoveState()

**Description:**

Sets this Tween state to PENDING\_REMOVE.

**Inherits:** [Phaser.Tweens.BaseTween#setPendingRemoveState](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L690](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L690)  
> Since: 3.60.0

---

## setPendingState

### <instance> setPendingState()

**Description:**

Sets this Tween state to PENDING.

**Inherits:** [Phaser.Tweens.BaseTween#setPendingState](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L629](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L629)  
> Since: 3.60.0

---

## setRemovedState

### <instance> setRemovedState()

**Description:**

Sets this Tween state to REMOVED.

**Inherits:** [Phaser.Tweens.BaseTween#setRemovedState](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L701](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L701)  
> Since: 3.60.0

---

## setStartDelayState

### <instance> setStartDelayState()

**Description:**

Sets this Tween state to START\_DELAY.

**Inherits:** [Phaser.Tweens.BaseTween#setStartDelayState](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L675](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L675)  
> Since: 3.60.0

---

## setTimeScale

### <instance> setTimeScale(value)

**Description:**

Sets the value of the time scale applied to this Tween. A value of 1 runs in real-time.

A value of 0.5 runs 50% slower, and so on.

The value isn't used when calculating total duration of the tween, it's a run-time delta adjustment only.

This value is multiplied by the `TweenManager.timeScale`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The time scale value to set. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This Tween instance.

**Inherits:** [Phaser.Tweens.BaseTween#setTimeScale](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L263](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L263)  
> Since: 3.60.0

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

Stops the Tween immediately, whatever stage of progress it is at.

If not a part of a Tween Chain it is also flagged for removal by the Tween Manager.

If an `onStop` callback has been defined it will automatically invoke it.

The Tween will be removed during the next game frame, but should be considered 'destroyed' from this point on.

Typically, you cannot play a Tween that has been stopped. If you just wish to pause the tween, not destroy it,

then call the `pause` method instead and use `resume` to continue playback. If you wish to restart the Tween,

use the `restart` or `seek` methods.

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - This Tween instance.

**Fires:** [Phaser.Tweens.Events#event:TWEEN\_STOP](../event/tweens-events.md)

**Inherits:** [Phaser.Tweens.BaseTween#stop](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L488](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L488)  
> Since: 3.60.0

---

## update

### <instance> update(delta)

**Description:**

Internal method that advances the TweenChain based on the time values.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |
| --- | --- | --- | --- |

**Returns:** boolean - Returns `true` if this TweenChain has finished and should be removed from the Tween Manager, otherwise returns `false`.

**Fires:** [Phaser.Tweens.Events#event:TWEEN\_COMPLETE](../event/tweens-events.md), [Phaser.Tweens.Events#event:TWEEN\_LOOP](../event/tweens-events.md), [Phaser.Tweens.Events#event:TWEEN\_START](../event/tweens-events.md)

> Source: [src/tweens/tween/TweenChain.js#L380](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L380)  
> Since: 3.60.0

---

## updateCompleteDelay

### <instance> updateCompleteDelay(delta)

**Description:**

Internal method that handles the processing of the complete delay countdown timer and

the dispatch of related events. Called automatically by `Tween.update`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.Tweens.BaseTween#updateCompleteDelay](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L568](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L568)  
> Since: 3.60.0

---

## updateLoopCountdown

### <instance> updateLoopCountdown(delta)

**Description:**

Internal method that handles the processing of the loop delay countdown timer and

the dispatch of related events. Called automatically by `Tween.update`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.Tweens.BaseTween#updateLoopCountdown](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L519](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L519)  
> Since: 3.60.0

---

## updateStartCountdown

### <instance> updateStartCountdown(delta)

**Description:**

Internal method that handles the processing of the start delay countdown timer and

the dispatch of related events. Called automatically by `Tween.update`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.Tweens.BaseTween#updateStartCountdown](tweens-basetween.md)

> Source: [src/tweens/tween/BaseTween.js#L540](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTween.js#L540)  
> Since: 3.60.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [callbacks](#callbacks)

    - [callbacks: Phaser.Types.Tweens.TweenCallbacks](#callbacks-phasertypestweenstweencallbacks)
  + [callbackScope](#callbackscope)

    - [callbackScope: any](#callbackscope-any)
  + [completeDelay](#completedelay)

    - [completeDelay: number](#completedelay-number)
  + [countdown](#countdown)

    - [countdown: number](#countdown-number)
  + [currentIndex](#currentindex)

    - [currentIndex: number](#currentindex-number)
  + [currentTween](#currenttween)

    - [currentTween: Phaser.Tweens.Tween](#currenttween-phasertweenstween)
  + [data](#data)

    - [data: Array.<Phaser.Tweens.TweenData>, Array.<Phaser.Tweens.Tween>](#data-arrayphasertweenstweendata-arrayphasertweenstween)
  + [hasStarted](#hasstarted)

    - [hasStarted: boolean](#hasstarted-boolean)
  + [loop](#loop)

    - [loop: number](#loop-number)
  + [loopCounter](#loopcounter)

    - [loopCounter: number](#loopcounter-number)
  + [loopDelay](#loopdelay)

    - [loopDelay: number](#loopdelay-number)
  + [parent](#parent)

    - [parent: Phaser.Tweens.TweenManager, Phaser.Tweens.TweenChain](#parent-phasertweenstweenmanager-phasertweenstweenchain)
  + [paused](#paused)

    - [paused: boolean](#paused-boolean)
  + [persist](#persist)

    - [persist: boolean](#persist-boolean)
  + [startDelay](#startdelay)

    - [startDelay: number](#startdelay-number)
  + [state](#state)

    - [state: Phaser.Tweens.StateType](#state-phasertweensstatetype)
  + [timeScale](#timescale)

    - [timeScale: number](#timescale-number)
  + [totalData](#totaldata)

    - [totalData: number](#totaldata-number)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(tweens)](#instance-addtweens)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [complete](#complete)

    - [<instance> complete([delay])](#instance-completedelay)
  + [completeAfterLoop](#completeafterloop)

    - [<instance> completeAfterLoop([loops])](#instance-completeafterlooploops)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [dispatchEvent](#dispatchevent)

    - [<instance> dispatchEvent(event, [callback])](#instance-dispatcheventevent-callback)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [getTimeScale](#gettimescale)

    - [<instance> getTimeScale()](#instance-gettimescale)
  + [hasTarget](#hastarget)

    - [<instance> hasTarget(target)](#instance-hastargettarget)
  + [init](#init)

    - [<instance> init()](#instance-init)
  + [isActive](#isactive)

    - [<instance> isActive()](#instance-isactive)
  + [isCompleteDelayed](#iscompletedelayed)

    - [<instance> isCompleteDelayed()](#instance-iscompletedelayed)
  + [isDestroyed](#isdestroyed)

    - [<instance> isDestroyed()](#instance-isdestroyed)
  + [isFinished](#isfinished)

    - [<instance> isFinished()](#instance-isfinished)
  + [isLoopDelayed](#isloopdelayed)

    - [<instance> isLoopDelayed()](#instance-isloopdelayed)
  + [isPaused](#ispaused)

    - [<instance> isPaused()](#instance-ispaused)
  + [isPending](#ispending)

    - [<instance> isPending()](#instance-ispending)
  + [isPendingRemove](#ispendingremove)

    - [<instance> isPendingRemove()](#instance-ispendingremove)
  + [isPlaying](#isplaying)

    - [<instance> isPlaying()](#instance-isplaying)
  + [isRemoved](#isremoved)

    - [<instance> isRemoved()](#instance-isremoved)
  + [isStartDelayed](#isstartdelayed)

    - [<instance> isStartDelayed()](#instance-isstartdelayed)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [makeActive](#makeactive)

    - [<instance> makeActive(tween)](#instance-makeactivetween)
  + [makeActive](#makeactive-1)

    - [<instance> makeActive(tween)](#instance-makeactivetween-1)
  + [nextState](#nextstate)

    - [<instance> nextState()](#instance-nextstate)
  + [nextTween](#nexttween)

    - [<instance> nextTween()](#instance-nexttween)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [onCompleteHandler](#oncompletehandler)

    - [<instance> onCompleteHandler()](#instance-oncompletehandler)
  + [pause](#pause)

    - [<instance> pause()](#instance-pause)
  + [play](#play)

    - [<instance> play()](#instance-play)
  + [remove](#remove)

    - [<instance> remove(tween)](#instance-removetween)
  + [remove](#remove-1)

    - [<instance> remove(tween)](#instance-removetween-1)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [reset](#reset)

    - [<instance> reset(tween)](#instance-resettween)
  + [resetTweens](#resettweens)

    - [<instance> resetTweens()](#instance-resettweens)
  + [restart](#restart)

    - [<instance> restart()](#instance-restart)
  + [resume](#resume)

    - [<instance> resume()](#instance-resume)
  + [setActiveState](#setactivestate)

    - [<instance> setActiveState()](#instance-setactivestate)
  + [setCallback](#setcallback)

    - [<instance> setCallback(type, callback, [params])](#instance-setcallbacktype-callback-params)
  + [setCompleteDelayState](#setcompletedelaystate)

    - [<instance> setCompleteDelayState()](#instance-setcompletedelaystate)
  + [setCurrentTween](#setcurrenttween)

    - [<instance> setCurrentTween(index)](#instance-setcurrenttweenindex)
  + [setDestroyedState](#setdestroyedstate)

    - [<instance> setDestroyedState()](#instance-setdestroyedstate)
  + [setFinishedState](#setfinishedstate)

    - [<instance> setFinishedState()](#instance-setfinishedstate)
  + [setLoopDelayState](#setloopdelaystate)

    - [<instance> setLoopDelayState()](#instance-setloopdelaystate)
  + [setPendingRemoveState](#setpendingremovestate)

    - [<instance> setPendingRemoveState()](#instance-setpendingremovestate)
  + [setPendingState](#setpendingstate)

    - [<instance> setPendingState()](#instance-setpendingstate)
  + [setRemovedState](#setremovedstate)

    - [<instance> setRemovedState()](#instance-setremovedstate)
  + [setStartDelayState](#setstartdelaystate)

    - [<instance> setStartDelayState()](#instance-setstartdelaystate)
  + [setTimeScale](#settimescale)

    - [<instance> setTimeScale(value)](#instance-settimescalevalue)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [stop](#stop)

    - [<instance> stop()](#instance-stop)
  + [update](#update)

    - [<instance> update(delta)](#instance-updatedelta)
  + [updateCompleteDelay](#updatecompletedelay)

    - [<instance> updateCompleteDelay(delta)](#instance-updatecompletedelaydelta)
  + [updateLoopCountdown](#updateloopcountdown)

    - [<instance> updateLoopCountdown(delta)](#instance-updateloopcountdowndelta)
  + [updateStartCountdown](#updatestartcountdown)

    - [<instance> updateStartCountdown(delta)](#instance-updatestartcountdowndelta)

Back to top

©2025[Phaser](https://docs.phaser.io)



TweenChain