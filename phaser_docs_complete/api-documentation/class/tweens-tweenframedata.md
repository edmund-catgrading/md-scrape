# TweenFrameData

Phaser.Tweens.TweenFrameData

The TweenFrameData is a class that contains a single target that will change the texture frame

at the conclusion of the Tween.

TweenFrameData instances are typically created by the TweenBuilder automatically, when it

detects the presence of a 'texture' property as the key being tweened.

A Tween can own multiple TweenFrameData instances, but a TweenFrameData only

ever belongs to a single Tween.

You should not typically create these yourself, but rather use the TweenBuilder,

or the `Tween.addFrame` method.

**Constructor**

`new TweenFrameData(tween, targetIndex, texture, frame, delay, duration, hold, repeat, repeatDelay, flipX, flipY)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](tweens-tween.md) | No | The tween this TweenData instance belongs to. |
| --- | --- | --- | --- |
| targetIndex | number | No | The target index within the Tween targets array. |
| texture | string | No | The texture key to set at the end of this tween. |
| frame | string | number | No | The texture frame to set at the end of this tween. |
| delay | function | No | Function that returns the time in milliseconds before tween will start. |
| duration | number | No | The duration of the tween in milliseconds. |
| hold | number | No | Function that returns the time in milliseconds the tween will pause before repeating or returning to its starting value if yoyo is set to true. |
| repeat | number | No | Function that returns the number of times to repeat the tween. The tween will always run once regardless, so a repeat value of '1' will play the tween twice. |
| repeatDelay | number | No | Function that returns the time in milliseconds before the repeat will start. |
| flipX | boolean | No | Should toggleFlipX be called when yoyo or repeat happens? |
| flipY | boolean | No | Should toggleFlipY be called when yoyo or repeat happens? |

---

**Scope**: static

**Extends**

> [Phaser.Tweens.BaseTweenData](tweens-basetweendata.md)

> Source: [src/tweens/tween/TweenFrameData.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenFrameData.js#L12)  
> Since: 3.60.0

# Public Members

## delay

### delay: number

**Description:**

The time, in milliseconds, before this tween will start playing.

This value is generated by the `getDelay` function.

**Inherits:** [Phaser.Tweens.BaseTweenData#delay](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L87](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L87)  
> Since: 3.60.0

---

## duration

### duration: number

**Description:**

The duration of the tween in milliseconds, excluding any time required

for yoyo or repeats.

**Inherits:** [Phaser.Tweens.BaseTweenData#duration](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L67](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L67)  
> Since: 3.60.0

---

## elapsed

### elapsed: number

**Description:**

The amount of time, in milliseconds, that has elapsed since this

TweenData was made active.

**Inherits:** [Phaser.Tweens.BaseTweenData#elapsed](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L190](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L190)  
> Since: 3.60.0

---

## endFrame

### endFrame: string, number

**Description:**

The frame to be set at the end of the tween.

> Source: [src/tweens/tween/TweenFrameData.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenFrameData.js#L93)  
> Since: 3.60.0

---

## endTexture

### endTexture: string

**Description:**

The texture to be set at the end of the tween.

> Source: [src/tweens/tween/TweenFrameData.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenFrameData.js#L75)  
> Since: 3.60.0

---

## flipX

### flipX: boolean

**Description:**

If `true` this Tween will call `toggleFlipX` on the Tween target

whenever it yoyo's or repeats. It will only be called if the target

has a function matching this name, like most Phaser GameObjects do.

**Inherits:** [Phaser.Tweens.BaseTweenData#flipX](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L159)  
> Since: 3.60.0

---

## flipY

### flipY: boolean

**Description:**

If `true` this Tween will call `toggleFlipY` on the Tween target

whenever it yoyo's or repeats. It will only be called if the target

has a function matching this name, like most Phaser GameObjects do.

**Inherits:** [Phaser.Tweens.BaseTweenData#flipY](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L170](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L170)  
> Since: 3.60.0

---

## getDelay

### getDelay: function

**Description:**

This function returns the value to be used for `TweenData.delay`.

**Inherits:** [Phaser.Tweens.BaseTweenData#getDelay](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L98)  
> Since: 3.60.0

---

## hold

### hold: number

**Description:**

The time, in milliseconds, before this tween will start a yoyo to repeat.

**Inherits:** [Phaser.Tweens.BaseTweenData#hold](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L117](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L117)  
> Since: 3.60.0

---

## isCountdown

### isCountdown: boolean

**Description:**

Is this Tween Data currently waiting for a countdown to elapse, or not?

**Inherits:** [Phaser.Tweens.BaseTweenData#isCountdown](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L209](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L209)  
> Since: 3.60.0

---

## key

### key: string

**Description:**

The property of the target to be tweened.

Always 'texture' for a TweenFrameData object.

> Source: [src/tweens/tween/TweenFrameData.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenFrameData.js#L54)  
> Since: 3.60.0

---

## progress

### progress: number

**Description:**

A value between 0 and 1 holding the progress of this TweenData.

**Inherits:** [Phaser.Tweens.BaseTweenData#progress](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L181](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L181)  
> Since: 3.60.0

---

## repeat

### repeat: number

**Description:**

The number of times this tween will repeat.

The tween will always run once regardless of this value,

so a repeat value of '1' will play the tween twice: I.e. the original

play-through and then it repeats that once (1).

If this value is set to -1 this tween will repeat forever.

**Inherits:** [Phaser.Tweens.BaseTweenData#repeat](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L126)  
> Since: 3.60.0

---

## repeatCounter

### repeatCounter: number

**Description:**

How many repeats are left to run?

**Inherits:** [Phaser.Tweens.BaseTweenData#repeatCounter](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L150](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L150)  
> Since: 3.60.0

---

## repeatDelay

### repeatDelay: number

**Description:**

The time, in milliseconds, before the repeat will start.

**Inherits:** [Phaser.Tweens.BaseTweenData#repeatDelay](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L141](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L141)  
> Since: 3.60.0

---

## startFrame

### startFrame: string, number

**Description:**

The frame to be set at the start of the tween.

> Source: [src/tweens/tween/TweenFrameData.js#L84](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenFrameData.js#L84)  
> Since: 3.60.0

---

## startTexture

### startTexture: string

**Description:**

The texture to be set at the start of the tween.

> Source: [src/tweens/tween/TweenFrameData.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenFrameData.js#L66)  
> Since: 3.60.0

---

## state

### state: [Phaser.Tweens.StateType](../typedef/tweens.md)

**Description:**

The state of this TweenData.

**Inherits:** [Phaser.Tweens.BaseTweenData#state](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L200](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L200)  
> Since: 3.60.0

---

## targetIndex

### targetIndex: number

**Description:**

The index of the target within the Tween `targets` array.

**Inherits:** [Phaser.Tweens.BaseTweenData#targetIndex](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L58](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L58)  
> Since: 3.60.0

---

## totalDuration

### totalDuration: number

**Description:**

The total calculated duration, in milliseconds, of this TweenData.

Factoring in the duration, repeats, delays and yoyos.

**Inherits:** [Phaser.Tweens.BaseTweenData#totalDuration](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L77)  
> Since: 3.60.0

---

## tween

### tween: [Phaser.Tweens.Tween](tweens-tween.md)

**Description:**

A reference to the Tween that this TweenData instance belongs to.

**Inherits:** [Phaser.Tweens.BaseTweenData#tween](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L49](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L49)  
> Since: 3.60.0

---

## yoyo

### yoyo: boolean

**Description:**

Will the Tween ease back to its starting values, after reaching the end

and any `hold` value that may be set?

**Overrides:** Phaser.Tweens.BaseTweenData#yoyo

> Source: [src/tweens/tween/TweenFrameData.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenFrameData.js#L102)  
> Since: 3.60.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Immediately destroys this TweenData, nulling of all its references.

**Overrides:** Phaser.Tweens.BaseTweenData#destroy

> Source: [src/tweens/tween/TweenFrameData.js#L298](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenFrameData.js#L298)  
> Since: 3.60.0

---

## dispatchEvent

### <instance> dispatchEvent(event, [callback])

**Description:**

Internal method that will emit a TweenData based Event on the

parent Tween and also invoke the given callback, if provided.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Types.Tweens.Event](../typedef/types-tweens.md) | No | The Event to be dispatched. |
| --- | --- | --- | --- |
| callback | [Phaser.Types.Tweens.TweenCallbackTypes](../typedef/types-tweens.md) | Yes | The name of the callback to be invoked. Can be `null` or `undefined` to skip invocation. |

> Source: [src/tweens/tween/TweenFrameData.js#L268](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenFrameData.js#L268)  
> Since: 3.60.0

---

## getTarget

### <instance> getTarget()

**Description:**

Returns a reference to the target object belonging to this TweenData.

**Returns:** object - The target object. Can be any JavaScript object, but is typically a Game Object.

**Inherits:** [Phaser.Tweens.BaseTweenData#getTarget](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L219](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L219)  
> Since: 3.60.0

---

## isComplete

### <instance> isComplete()

**Description:**

Returns `true` if this TweenData has a *current* state of COMPLETE, otherwise `false`.

**Returns:** boolean - `true` if this TweenData has a *current* state of COMPLETE, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTweenData#isComplete](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L434](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L434)  
> Since: 3.60.0

---

## isCreated

### <instance> isCreated()

**Description:**

Returns `true` if this TweenData has a *current* state of CREATED, otherwise `false`.

**Returns:** boolean - `true` if this TweenData has a *current* state of CREATED, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTweenData#isCreated](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L343](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L343)  
> Since: 3.60.0

---

## isDelayed

### <instance> isDelayed()

**Description:**

Returns `true` if this TweenData has a *current* state of DELAY, otherwise `false`.

**Returns:** boolean - `true` if this TweenData has a *current* state of DELAY, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTweenData#isDelayed](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L356](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L356)  
> Since: 3.60.0

---

## isHolding

### <instance> isHolding()

**Description:**

Returns `true` if this TweenData has a *current* state of HOLD\_DELAY, otherwise `false`.

**Returns:** boolean - `true` if this TweenData has a *current* state of HOLD\_DELAY, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTweenData#isHolding](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L408](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L408)  
> Since: 3.60.0

---

## isPendingRender

### <instance> isPendingRender()

**Description:**

Returns `true` if this TweenData has a *current* state of PENDING\_RENDER, otherwise `false`.

**Returns:** boolean - `true` if this TweenData has a *current* state of PENDING\_RENDER, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTweenData#isPendingRender](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L369](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L369)  
> Since: 3.60.0

---

## isPlayingBackward

### <instance> isPlayingBackward()

**Description:**

Returns `true` if this TweenData has a *current* state of PLAYING\_BACKWARD, otherwise `false`.

**Returns:** boolean - `true` if this TweenData has a *current* state of PLAYING\_BACKWARD, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTweenData#isPlayingBackward](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L395](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L395)  
> Since: 3.60.0

---

## isPlayingForward

### <instance> isPlayingForward()

**Description:**

Returns `true` if this TweenData has a *current* state of PLAYING\_FORWARD, otherwise `false`.

**Returns:** boolean - `true` if this TweenData has a *current* state of PLAYING\_FORWARD, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTweenData#isPlayingForward](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L382](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L382)  
> Since: 3.60.0

---

## isRepeating

### <instance> isRepeating()

**Description:**

Returns `true` if this TweenData has a *current* state of REPEAT\_DELAY, otherwise `false`.

**Returns:** boolean - `true` if this TweenData has a *current* state of REPEAT\_DELAY, otherwise `false`.

**Inherits:** [Phaser.Tweens.BaseTweenData#isRepeating](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L421](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L421)  
> Since: 3.60.0

---

## onRepeat

### <instance> onRepeat(diff, setStart, isYoyo)

**Description:**

Internal method that handles repeating or yoyo'ing this TweenData.

Called automatically by `setStateFromStart` and `setStateFromEnd`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| diff | number | No | Any extra time that needs to be accounted for in the elapsed and progress values. |
| --- | --- | --- | --- |
| setStart | boolean | No | Set the TweenData start values? |
| isYoyo | boolean | No | Is this call a Yoyo check? |

**Fires:** [Phaser.Tweens.Events#event:TWEEN\_REPEAT](../event/tweens-events.md), [Phaser.Tweens.Events#event:TWEEN\_YOYO](../event/tweens-events.md)

**Inherits:** [Phaser.Tweens.BaseTweenData#onRepeat](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L569](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L569)  
> Since: 3.60.0

---

## reset

### <instance> reset([isSeeking])

**Description:**

Internal method that resets this Tween Data entirely, including the progress and elapsed values.

Called automatically by the parent Tween. Should not be called directly.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| isSeeking | boolean | Yes | false | Is the Tween Data being reset as part of a Tween seek? |
| --- | --- | --- | --- | --- |

**Overrides:** Phaser.Tweens.BaseTweenData#reset

> Source: [src/tweens/tween/TweenFrameData.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenFrameData.js#L113)  
> Since: 3.60.0

---

## setCompleteState

### <instance> setCompleteState()

**Description:**

Sets this TweenData state to COMPLETE.

**Inherits:** [Phaser.Tweens.BaseTweenData#setCompleteState](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L331](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L331)  
> Since: 3.60.0

---

## setCreatedState

### <instance> setCreatedState()

**Description:**

Sets this TweenData state to CREATED.

**Inherits:** [Phaser.Tweens.BaseTweenData#setCreatedState](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L247](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L247)  
> Since: 3.60.0

---

## setDelayState

### <instance> setDelayState()

**Description:**

Sets this TweenData state to DELAY.

**Inherits:** [Phaser.Tweens.BaseTweenData#setDelayState](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L259](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L259)  
> Since: 3.60.0

---

## setHoldState

### <instance> setHoldState()

**Description:**

Sets this TweenData state to HOLD\_DELAY.

**Inherits:** [Phaser.Tweens.BaseTweenData#setHoldState](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L307](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L307)  
> Since: 3.60.0

---

## setPendingRenderState

### <instance> setPendingRenderState()

**Description:**

Sets this TweenData state to PENDING\_RENDER.

**Inherits:** [Phaser.Tweens.BaseTweenData#setPendingRenderState](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L271](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L271)  
> Since: 3.60.0

---

## setPlayingBackwardState

### <instance> setPlayingBackwardState()

**Description:**

Sets this TweenData state to PLAYING\_BACKWARD.

**Inherits:** [Phaser.Tweens.BaseTweenData#setPlayingBackwardState](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L295](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L295)  
> Since: 3.60.0

---

## setPlayingForwardState

### <instance> setPlayingForwardState()

**Description:**

Sets this TweenData state to PLAYING\_FORWARD.

**Inherits:** [Phaser.Tweens.BaseTweenData#setPlayingForwardState](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L283](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L283)  
> Since: 3.60.0

---

## setRepeatState

### <instance> setRepeatState()

**Description:**

Sets this TweenData state to REPEAT\_DELAY.

**Inherits:** [Phaser.Tweens.BaseTweenData#setRepeatState](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L319](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L319)  
> Since: 3.60.0

---

## setStateFromEnd

### <instance> setStateFromEnd(diff)

**Description:**

Internal method used as part of the playback process that checks if this

TweenData should yoyo, repeat, or has completed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| diff | number | No | Any extra time that needs to be accounted for in the elapsed and progress values. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Tweens.Events#event:TWEEN\_REPEAT](../event/tweens-events.md), [Phaser.Tweens.Events#event:TWEEN\_YOYO](../event/tweens-events.md)

**Inherits:** [Phaser.Tweens.BaseTweenData#setStateFromEnd](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L447](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L447)  
> Since: 3.60.0

---

## setStateFromStart

### <instance> setStateFromStart(diff)

**Description:**

Internal method used as part of the playback process that checks if this

TweenData should repeat or has completed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| diff | number | No | Any extra time that needs to be accounted for in the elapsed and progress values. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Tweens.Events#event:TWEEN\_REPEAT](../event/tweens-events.md)

**Inherits:** [Phaser.Tweens.BaseTweenData#setStateFromStart](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L474](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L474)  
> Since: 3.60.0

---

## setTargetValue

### <instance> setTargetValue([value])

**Description:**

Sets this TweenData's target object property to be the given value.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | Yes | The value to set on the target. If not given, sets it to the last `current` value. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.Tweens.BaseTweenData#setTargetValue](tweens-basetweendata.md)

> Source: [src/tweens/tween/BaseTweenData.js#L232](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/BaseTweenData.js#L232)  
> Since: 3.60.0

---

## update

### <instance> update(delta)

**Description:**

Internal method that advances this TweenData based on the delta value given.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| delta | number | No | The elapsed delta time in ms. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if this TweenData is still playing, or `false` if it has finished entirely.

**Fires:** [Phaser.Tweens.Events#event:TWEEN\_UPDATE](../event/tweens-events.md), [Phaser.Tweens.Events#event:TWEEN\_REPEAT](../event/tweens-events.md)

> Source: [src/tweens/tween/TweenFrameData.js#L141](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenFrameData.js#L141)  
> Since: 3.60.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [delay](#delay)

    - [delay: number](#delay-number)
  + [duration](#duration)

    - [duration: number](#duration-number)
  + [elapsed](#elapsed)

    - [elapsed: number](#elapsed-number)
  + [endFrame](#endframe)

    - [endFrame: string, number](#endframe-string-number)
  + [endTexture](#endtexture)

    - [endTexture: string](#endtexture-string)
  + [flipX](#flipx)

    - [flipX: boolean](#flipx-boolean)
  + [flipY](#flipy)

    - [flipY: boolean](#flipy-boolean)
  + [getDelay](#getdelay)

    - [getDelay: function](#getdelay-function)
  + [hold](#hold)

    - [hold: number](#hold-number)
  + [isCountdown](#iscountdown)

    - [isCountdown: boolean](#iscountdown-boolean)
  + [key](#key)

    - [key: string](#key-string)
  + [progress](#progress)

    - [progress: number](#progress-number)
  + [repeat](#repeat)

    - [repeat: number](#repeat-number)
  + [repeatCounter](#repeatcounter)

    - [repeatCounter: number](#repeatcounter-number)
  + [repeatDelay](#repeatdelay)

    - [repeatDelay: number](#repeatdelay-number)
  + [startFrame](#startframe)

    - [startFrame: string, number](#startframe-string-number)
  + [startTexture](#starttexture)

    - [startTexture: string](#starttexture-string)
  + [state](#state)

    - [state: Phaser.Tweens.StateType](#state-phasertweensstatetype)
  + [targetIndex](#targetindex)

    - [targetIndex: number](#targetindex-number)
  + [totalDuration](#totalduration)

    - [totalDuration: number](#totalduration-number)
  + [tween](#tween)

    - [tween: Phaser.Tweens.Tween](#tween-phasertweenstween)
  + [yoyo](#yoyo)

    - [yoyo: boolean](#yoyo-boolean)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [dispatchEvent](#dispatchevent)

    - [<instance> dispatchEvent(event, [callback])](#instance-dispatcheventevent-callback)
  + [getTarget](#gettarget)

    - [<instance> getTarget()](#instance-gettarget)
  + [isComplete](#iscomplete)

    - [<instance> isComplete()](#instance-iscomplete)
  + [isCreated](#iscreated)

    - [<instance> isCreated()](#instance-iscreated)
  + [isDelayed](#isdelayed)

    - [<instance> isDelayed()](#instance-isdelayed)
  + [isHolding](#isholding)

    - [<instance> isHolding()](#instance-isholding)
  + [isPendingRender](#ispendingrender)

    - [<instance> isPendingRender()](#instance-ispendingrender)
  + [isPlayingBackward](#isplayingbackward)

    - [<instance> isPlayingBackward()](#instance-isplayingbackward)
  + [isPlayingForward](#isplayingforward)

    - [<instance> isPlayingForward()](#instance-isplayingforward)
  + [isRepeating](#isrepeating)

    - [<instance> isRepeating()](#instance-isrepeating)
  + [onRepeat](#onrepeat)

    - [<instance> onRepeat(diff, setStart, isYoyo)](#instance-onrepeatdiff-setstart-isyoyo)
  + [reset](#reset)

    - [<instance> reset([isSeeking])](#instance-resetisseeking)
  + [setCompleteState](#setcompletestate)

    - [<instance> setCompleteState()](#instance-setcompletestate)
  + [setCreatedState](#setcreatedstate)

    - [<instance> setCreatedState()](#instance-setcreatedstate)
  + [setDelayState](#setdelaystate)

    - [<instance> setDelayState()](#instance-setdelaystate)
  + [setHoldState](#setholdstate)

    - [<instance> setHoldState()](#instance-setholdstate)
  + [setPendingRenderState](#setpendingrenderstate)

    - [<instance> setPendingRenderState()](#instance-setpendingrenderstate)
  + [setPlayingBackwardState](#setplayingbackwardstate)

    - [<instance> setPlayingBackwardState()](#instance-setplayingbackwardstate)
  + [setPlayingForwardState](#setplayingforwardstate)

    - [<instance> setPlayingForwardState()](#instance-setplayingforwardstate)
  + [setRepeatState](#setrepeatstate)

    - [<instance> setRepeatState()](#instance-setrepeatstate)
  + [setStateFromEnd](#setstatefromend)

    - [<instance> setStateFromEnd(diff)](#instance-setstatefromenddiff)
  + [setStateFromStart](#setstatefromstart)

    - [<instance> setStateFromStart(diff)](#instance-setstatefromstartdiff)
  + [setTargetValue](#settargetvalue)

    - [<instance> setTargetValue([value])](#instance-settargetvaluevalue)
  + [update](#update)

    - [<instance> update(delta)](#instance-updatedelta)

Back to top

©2025[Phaser](https://docs.phaser.io)