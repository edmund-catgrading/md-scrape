# TweenManager

Phaser.Tweens.TweenManager

The Tween Manager is a default Scene Plugin which controls and updates Tweens.

A tween is a way to alter one or more properties of a target object over a defined period of time.

Tweens are created by calling the `add` method and passing in the configuration object.

```
Copy
const logo = this.add.image(100, 100, 'logo');



this.tweens.add({

  targets: logo,

  x: 600,

  ease: 'Power1',

  duration: 2000

});


```

See the `TweenBuilderConfig` for all of the options you have available.

Playback will start immediately unless the tween has been configured to be paused.

Please note that a Tween will not manipulate any target property that begins with an underscore.

Tweens are designed to be 'fire-and-forget'. They automatically destroy themselves once playback

is complete, to free-up memory and resources. If you wish to keep a tween after playback, i.e. to

play it again at a later time, then you should set the `persist` property to `true` in the config.

However, doing so means it's entirely up to *you* to destroy the tween when you're finished with it,

otherwise it will linger in memory forever.

If you wish to chain Tweens together for sequential playback, see the `TweenManager.chain` method.

**Constructor**

`new TweenManager(scene)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene which owns this Tween Manager. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/tweens/TweenManager.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L19)  
> Since: 3.0.0

# Public Members

## events

### events: [Phaser.Events.EventEmitter](events-eventemitter.md)

**Description:**

The Scene Systems Event Emitter.

> Source: [src/tweens/TweenManager.js#L74](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L74)  
> Since: 3.60.0

---

## gap

### gap: number

**Description:**

An internal value that holds the fps rate.

> Source: [src/tweens/TweenManager.js#L193](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L193)  
> Since: 3.60.0

---

## lagSkip

### lagSkip: number

**Description:**

The amount of time, in milliseconds, that is used to set the

delta when lag smoothing is applied.

See the `TweenManager.setLagSmooth` method for further details.

> Source: [src/tweens/TweenManager.js#L180](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L180)  
> Since: 3.60.0

---

## maxLag

### maxLag: number

**Description:**

The maximum amount of time, in milliseconds, the browser can

lag for, before lag smoothing is applied.

See the `TweenManager.setLagSmooth` method for further details.

> Source: [src/tweens/TweenManager.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L167)  
> Since: 3.60.0

---

## nextTime

### nextTime: number

**Description:**

The time the Tween Manager should next update.

> Source: [src/tweens/TweenManager.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L149)  
> Since: 3.60.0

---

## paused

### paused: boolean

**Description:**

This toggles the updating state of this Tween Manager.

Setting `paused` to `true` (or calling the `pauseAll` method) will

stop this Tween Manager from updating any of its tweens, including

newly created ones. Set back to `false` to resume playback.

> Source: [src/tweens/TweenManager.js#L95](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L95)  
> Since: 3.60.0

---

## prevTime

### prevTime: number

**Description:**

The time the Tween Manager previously updated.

> Source: [src/tweens/TweenManager.js#L158](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L158)  
> Since: 3.60.0

---

## processing

### processing: boolean

**Description:**

Is this Tween Manager currently processing the tweens as part of

its 'update' loop? This is set to 'true' at the start of 'update'

and reset to 'false' at the end of the function. Allows you to trap

Tween Manager status during tween callbacks.

> Source: [src/tweens/TweenManager.js#L109](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L109)  
> Since: 3.60.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

The Scene which owns this Tween Manager.

> Source: [src/tweens/TweenManager.js#L65](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L65)  
> Since: 3.0.0

---

## startTime

### startTime: number

**Description:**

The time the Tween Manager was started.

> Source: [src/tweens/TweenManager.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L140)  
> Since: 3.60.0

---

## time

### time: number

**Description:**

The time the Tween Manager was updated.

> Source: [src/tweens/TweenManager.js#L131](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L131)  
> Since: 3.60.0

---

## timeScale

### timeScale: number

**Description:**

The time scale of the Tween Manager.

This value scales the time delta between two frames, thus influencing the speed of time for all Tweens owned by this Tween Manager.

> Source: [src/tweens/TweenManager.js#L83](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L83)  
> Since: 3.0.0

---

## tweens

### tweens: Array.<[Phaser.Tweens.Tween](tweens-tween.md)>

**Description:**

An array of Tweens which are actively being processed by the Tween Manager.

> Source: [src/tweens/TweenManager.js#L122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L122)  
> Since: 3.60.0

---

# Public Methods

## add

### <instance> add(config)

**Description:**

Create a Tween and add it to this Tween Manager by passing a Tween Configuration object.

Example, run from within a Scene:

```
Copy
const logo = this.add.image(100, 100, 'logo');



this.tweens.add({

  targets: logo,

  x: 600,

  ease: 'Power1',

  duration: 2000

});


```

See the `TweenBuilderConfig` for all of the options you have available.

Playback will start immediately unless the tween has been configured to be paused.

Please note that a Tween will not manipulate any target property that begins with an underscore.

Tweens are designed to be 'fire-and-forget'. They automatically destroy themselves once playback

is complete, to free-up memory and resources. If you wish to keep a tween after playback, i.e. to

play it again at a later time, then you should set the `persist` property to `true` in the config.

However, doing so means it's entirely up to *you* to destroy the tween when you're finished with it,

otherwise it will linger in memory forever.

If you wish to chain Tweens together for sequential playback, see the `TweenManager.chain` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Tweens.TweenBuilderConfig](../typedef/types-tweens.md) | [Phaser.Types.Tweens.TweenChainBuilderConfig](../typedef/types-tweens.md) | [Phaser.Tweens.Tween](tweens-tween.md) | [Phaser.Tweens.TweenChain](tweens-tweenchain.md) |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.Tween](tweens-tween.md) - The created Tween.

> Source: [src/tweens/TweenManager.js#L290](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L290)  
> Since: 3.0.0

---

## addCounter

### <instance> addCounter(config)

**Description:**

Create a Number Tween and add it to the active Tween list.

A Number Tween is a special kind of tween that doesn't have a target. Instead,

it allows you to tween between 2 numeric values. The default values are

`0` and `1`, but you can change them via the `from` and `to` properties.

You can get the current tweened value via the `Tween.getValue()` method.

Playback will start immediately unless the tween has been configured to be paused.

Please note that a Tween will not manipulate any target property that begins with an underscore.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Tweens.NumberTweenBuilderConfig](../typedef/types-tweens.md) | No | The configuration object for the Number Tween. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.Tween](tweens-tween.md) - The created Number Tween.

> Source: [src/tweens/TweenManager.js#L498](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L498)  
> Since: 3.0.0

---

## addMultiple

### <instance> addMultiple(configs)

**Description:**

Create multiple Tweens and add them all to this Tween Manager, by passing an array of Tween Configuration objects.

See the `TweenBuilderConfig` for all of the options you have available.

Playback will start immediately unless the tweens have been configured to be paused.

Please note that a Tween will not manipulate any target property that begins with an underscore.

Tweens are designed to be 'fire-and-forget'. They automatically destroy themselves once playback

is complete, to free-up memory and resources. If you wish to keep a tween after playback, i.e. to

play it again at a later time, then you should set the `persist` property to `true` in the config.

However, doing so means it's entirely up to *you* to destroy the tween when you're finished with it,

otherwise it will linger in memory forever.

If you wish to chain Tweens together for sequential playback, see the `TweenManager.chain` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| configs | Array.<[Phaser.Types.Tweens.TweenBuilderConfig](../typedef/types-tweens.md)> | Array.<object> | No | An array of Tween Configuration objects. |
| --- | --- | --- | --- |

**Returns:** Array.<[Phaser.Tweens.Tween](tweens-tween.md)> - An array of created Tweens.

> Source: [src/tweens/TweenManager.js#L353](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L353)  
> Since: 3.60.0

---

## chain

### <instance> chain(tweens)

**Description:**

Create a sequence of Tweens, chained to one-another, and add them to this Tween Manager.

The tweens are played in order, from start to finish. You can optionally set the chain

to repeat as many times as you like. Once the chain has finished playing, or repeating if set,

all tweens in the chain will be destroyed automatically. To override this, set the `persist`

argument to 'true'.

Playback will start immediately unless the *first* Tween has been configured to be paused.

Please note that Tweens will not manipulate any target property that begins with an underscore.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tweens | [Phaser.Types.Tweens.TweenChainBuilderConfig](../typedef/types-tweens.md) | object | No | A Tween Chain configuration object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - The Tween Chain instance.

> Source: [src/tweens/TweenManager.js#L411](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L411)  
> Since: 3.60.0

---

## create

### <instance> create(config)

**Description:**

Create a Tween and return it, but does not add it to this Tween Manager.

Please note that a Tween will not manipulate any target property that begins with an underscore.

In order to play this tween, you'll need to add it to a Tween Manager via

the `TweenManager.existing` method.

You can optionally pass an **array** of Tween Configuration objects to this method and it will create

one Tween per entry in the array. If an array is given, an array of tweens is returned.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Tweens.TweenBuilderConfig](../typedef/types-tweens.md) | Array.<[Phaser.Types.Tweens.TweenBuilderConfig](../typedef/types-tweens.md)> | object | Array.<object> |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.Tween](tweens-tween.md), Array.<[Phaser.Tweens.Tween](tweens-tween.md)> - The created Tween, or an array of Tweens if an array of tween configs was provided.

> Source: [src/tweens/TweenManager.js#L241](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L241)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

The Scene that owns this plugin is being destroyed.

We need to shutdown and then kill off all external references.

> Source: [src/tweens/TweenManager.js#L1134](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L1134)  
> Since: 3.0.0

---

## each

### <instance> each(callback, [scope], [args])

**Description:**

Passes all Tweens to the given callback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | function | No | The function to call. |
| --- | --- | --- | --- |
| scope | object | Yes | The scope (`this` object) to call the function with. |
| args | \* | Yes | The arguments to pass into the function. Its first argument will always be the Tween currently being iterated. |

**Returns:** [Phaser.Tweens.TweenManager](tweens-tweenmanager.md) - This Tween Manager instance.

> Source: [src/tweens/TweenManager.js#L852](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L852)  
> Since: 3.0.0

---

## existing

### <instance> existing(tween)

**Description:**

Add an existing Tween to this Tween Manager.

Playback will start immediately unless the tween has been configured to be paused.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](tweens-tween.md) | No | The Tween to add. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenManager](tweens-tweenmanager.md) - This Tween Manager instance.

> Source: [src/tweens/TweenManager.js#L476](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L476)  
> Since: 3.0.0

---

## getChainedTweens

### <instance> getChainedTweens(tween)

**Description:**

Returns an array containing this Tween and all Tweens chained to it,

in the order in which they will be played.

If there are no chained Tweens an empty array is returned.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](tweens-tween.md) | No | The Tween to return the chain from. |
| --- | --- | --- | --- |

**Returns:** Array.<[Phaser.Tweens.Tween](tweens-tween.md)> - An array of the chained tweens, or an empty array if there aren't any.

> Source: [src/tweens/TweenManager.js#L439](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L439)  
> Since: 3.60.0

---

## getDelta

### <instance> getDelta([tick])

**Description:**

Internal method that calculates the delta value, along with the other timing values,

and returns the new delta.

You should not typically call this method directly.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| tick | boolean | Yes | false | Is this a manual tick, or an automated tick? |
| --- | --- | --- | --- | --- |

**Returns:** number - The new delta value.

> Source: [src/tweens/TweenManager.js#L630](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L630)  
> Since: 3.60.0

---

## getGlobalTimeScale

### <instance> getGlobalTimeScale()

**Description:**

Returns the scale of the time delta for all Tweens owned by this Tween Manager.

**Returns:** number - The scale of the time delta, usually 1.

> Source: [src/tweens/TweenManager.js#L949](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L949)  
> Since: 3.0.0

---

## getTweens

### <instance> getTweens()

**Description:**

Returns an array containing references to all Tweens in this Tween Manager.

It is safe to mutate the returned array. However, acting upon any of the Tweens

within it, will adjust those stored in this Tween Manager, as they are passed

by reference and not cloned.

If you wish to get tweens for a specific target, see `getTweensOf`.

**Returns:** Array.<[Phaser.Tweens.Tween](tweens-tween.md)> - A new array containing references to all Tweens.

> Source: [src/tweens/TweenManager.js#L884](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L884)  
> Since: 3.0.0

---

## getTweensOf

### <instance> getTweensOf(target)

**Description:**

Returns an array of all Tweens in the Tween Manager which affect the given target, or array of targets.

It's possible for this method to return tweens that are about to be removed from

the Tween Manager. You should check the state of the returned tween before acting

upon it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | object | Array.<object> | No | The target to look for. Provide an array to look for multiple targets. |
| --- | --- | --- | --- |

**Returns:** Array.<[Phaser.Tweens.Tween](tweens-tween.md)> - A new array containing all Tweens which affect the given target(s).

> Source: [src/tweens/TweenManager.js#L903](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L903)  
> Since: 3.0.0

---

## has

### <instance> has(tween)

**Description:**

Check to see if the given Tween instance exists within this Tween Manager.

Will return `true` as long as the Tween is being processed by this Tween Manager.

Will return `false` if not present, or has a state of `REMOVED` or `DESTROYED`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](tweens-tween.md) | No | The Tween instance to check. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the Tween exists within this Tween Manager, otherwise `false`.

> Source: [src/tweens/TweenManager.js#L457](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L457)  
> Since: 3.60.0

---

## isTweening

### <instance> isTweening(target)

**Description:**

Checks if the given object is being affected by a *playing* Tween.

If the Tween is paused, this method will return false.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | object | No | The object to check if a tween is active for it, or not. |
| --- | --- | --- | --- |

**Returns:** boolean - Returns `true` if a tween is active on the given target, otherwise `false`.

> Source: [src/tweens/TweenManager.js#L981](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L981)  
> Since: 3.0.0

---

## killAll

### <instance> killAll()

**Description:**

Destroys all Tweens in this Tween Manager.

The tweens will erase all references to any targets they hold

and be stopped immediately.

If this method is called while the Tween Manager is running its

update process, then the tweens will be removed at the start of

the next frame. Outside of this, they are removed immediately.

**Returns:** [Phaser.Tweens.TweenManager](tweens-tweenmanager.md) - This Tween Manager instance.

> Source: [src/tweens/TweenManager.js#L1011](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L1011)  
> Since: 3.0.0

---

## killTweensOf

### <instance> killTweensOf(target)

**Description:**

Stops all Tweens which affect the given target or array of targets.

The tweens will erase all references to any targets they hold

and be stopped immediately.

If this method is called while the Tween Manager is running its

update process, then the tweens will be removed at the start of

the next frame. Outside of this, they are removed immediately.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | object | array | No | The target to kill the tweens of. Provide an array to use multiple targets. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenManager](tweens-tweenmanager.md) - This Tween Manager instance.

> Source: [src/tweens/TweenManager.js#L1043](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L1043)  
> Since: 3.0.0

---

## makeActive

### <instance> makeActive(tween)

**Description:**

Checks if a Tween is active and adds it to the Tween Manager at the start of the frame if it isn't.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](tweens-tween.md) | No | The Tween to check. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenManager](tweens-tweenmanager.md) - This Tween Manager instance.

> Source: [src/tweens/TweenManager.js#L833](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L833)  
> Since: 3.0.0

---

## pauseAll

### <instance> pauseAll()

**Description:**

Pauses this Tween Manager. No Tweens will update while paused.

This includes tweens created after this method was called.

See `TweenManager#resumeAll` to resume the playback.

As of Phaser 3.60 you can also toggle the boolean property `TweenManager.paused`.

**Returns:** [Phaser.Tweens.TweenManager](tweens-tweenmanager.md) - This Tween Manager instance.

> Source: [src/tweens/TweenManager.js#L1074](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L1074)  
> Since: 3.0.0

---

## remove

### <instance> remove(tween)

**Description:**

Removes the given Tween from this Tween Manager, even if it hasn't started

playback yet. If this method is called while the Tween Manager is processing

an update loop, then the tween will be flagged for removal at the start of

the next frame. Otherwise, it is removed immediately.

The removed tween is *not* destroyed. It is just removed from this Tween Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](tweens-tween.md) | No | The Tween to be removed. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenManager](tweens-tweenmanager.md) - This Tween Manager instance.

> Source: [src/tweens/TweenManager.js#L775](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L775)  
> Since: 3.17.0

---

## reset

### <instance> reset(tween)

**Description:**

Resets the given Tween.

If the Tween does not belong to this Tween Manager, it will first be added.

Then it will seek to position 0 and playback will start on the next frame.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](tweens-tween.md) | No | The Tween to be reset. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenManager](tweens-tweenmanager.md) - This Tween Manager instance.

> Source: [src/tweens/TweenManager.js#L808](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L808)  
> Since: 3.60.0

---

## resumeAll

### <instance> resumeAll()

**Description:**

Resumes playback of this Tween Manager.

All active Tweens will continue updating.

See `TweenManager#pauseAll` to pause the playback.

As of Phaser 3.60 you can also toggle the boolean property `TweenManager.paused`.

**Returns:** [Phaser.Tweens.TweenManager](tweens-tweenmanager.md) - This Tween Manager instance.

> Source: [src/tweens/TweenManager.js#L1095](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L1095)  
> Since: 3.0.0

---

## setFps

### <instance> setFps([fps])

**Description:**

Limits the Tween system to run at a particular frame rate.

You should not set this *above* the frequency of the browser,

but instead can use it to throttle the frame rate lower, should

you need to in certain situations.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| fps | number | Yes | 240 | The frame rate to tick at. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenManager](tweens-tweenmanager.md) - This Tween Manager instance.

> Source: [src/tweens/TweenManager.js#L606](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L606)  
> Since: 3.60.0

---

## setGlobalTimeScale

### <instance> setGlobalTimeScale(value)

**Description:**

Sets a new scale of the time delta for this Tween Manager.

The time delta is the time elapsed between two consecutive frames and influences the speed of time for this Tween Manager and all Tweens it owns. Values higher than 1 increase the speed of time, while values smaller than 1 decrease it. A value of 0 freezes time and is effectively equivalent to pausing all Tweens.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The new scale of the time delta, where 1 is the normal speed. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenManager](tweens-tweenmanager.md) - This Tween Manager instance.

> Source: [src/tweens/TweenManager.js#L962](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L962)  
> Since: 3.0.0

---

## setLagSmooth

### <instance> setLagSmooth([limit], [skip])

**Description:**

Set the limits that are used when a browser encounters lag, or delays that cause the elapsed

time between two frames to exceed the expected amount. If this occurs, the Tween Manager will

act as if the 'skip' amount of times has passed, in order to maintain strict tween sequencing.

This is enabled by default with the values 500ms for the lag limit and 33ms for the skip.

You should not set these to low values, as it won't give time for the browser to ever

catch-up with itself and reclaim sync.

Call this method with no arguments to disable smoothing.

Call it with the arguments `500` and `33` to reset to the defaults.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| limit | number | Yes | 0 | If the browser exceeds this amount, in milliseconds, it will act as if the 'skip' amount has elapsed instead. |
| --- | --- | --- | --- | --- |
| skip | number | Yes | 0 | The amount, in milliseconds, to use as the step delta should the browser lag beyond the 'limit'. |

**Returns:** [Phaser.Tweens.TweenManager](tweens-tweenmanager.md) - This Tween Manager instance.

> Source: [src/tweens/TweenManager.js#L573](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L573)  
> Since: 3.60.0

---

## shutdown

### <instance> shutdown()

**Description:**

The Scene that owns this plugin is shutting down.

We need to kill and reset all internal properties as well as stop listening to Scene events.

> Source: [src/tweens/TweenManager.js#L1116](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L1116)  
> Since: 3.0.0

---

## stagger

### <instance> stagger(value, config)

**Description:**

Creates a Stagger function to be used by a Tween property.

The stagger function will allow you to stagger changes to the value of the property across all targets of the tween.

This is only worth using if the tween has multiple targets.

The following will stagger the delay by 100ms across all targets of the tween, causing them to scale down to 0.2

over the duration specified:

```
Copy
this.tweens.add({

    targets: [ ... ],

    scale: 0.2,

    ease: 'linear',

    duration: 1000,

    delay: this.tweens.stagger(100)

});


```

The following will stagger the delay by 500ms across all targets of the tween using a 10 x 6 grid, staggering

from the center out, using a cubic ease.

```
Copy
this.tweens.add({

    targets: [ ... ],

    scale: 0.2,

    ease: 'linear',

    duration: 1000,

    delay: this.tweens.stagger(500, { grid: [ 10, 6 ], from: 'center', ease: 'cubic.out' })

});


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | Array.<number> | No | The amount to stagger by, or an array containing two elements representing the min and max values to stagger between. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Tweens.StaggerConfig](../typedef/types-tweens.md) | No | The configuration object for the Stagger function. |

**Returns:** function - The stagger function.

> Source: [src/tweens/TweenManager.js#L527](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L527)  
> Since: 3.19.0

---

## step

### <instance> step([tick])

**Description:**

Updates all Tweens belonging to this Tween Manager.

Called automatically by `update` and `tick`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| tick | boolean | Yes | false | Is this a manual tick, or an automated tick? |
| --- | --- | --- | --- | --- |

> Source: [src/tweens/TweenManager.js#L707](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L707)  
> Since: 3.60.0

---

## tick

### <instance> tick()

**Description:**

Manually advance the Tween system by one step.

This will update all Tweens even if the Tween Manager is currently

paused.

**Returns:** [Phaser.Tweens.TweenManager](tweens-tweenmanager.md) - This Tween Manager instance.

> Source: [src/tweens/TweenManager.js#L672](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L672)  
> Since: 3.60.0

---

## update

### <instance> update()

**Description:**

Internal update handler.

Calls `TweenManager.step` as long as the Tween Manager has not

been paused.

> Source: [src/tweens/TweenManager.js#L690](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L690)  
> Since: 3.0.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

This method is called automatically, only once, when the Scene is first created.

Do not invoke it directly.

**Access:** private

> Source: [src/tweens/TweenManager.js#L206](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L206)  
> Since: 3.5.1

---

## start

### <instance> start()

**Description:**

This method is called automatically by the Scene when it is starting up.

It is responsible for creating local systems, properties and listening for Scene events.

Do not invoke it directly.

**Access:** private

> Source: [src/tweens/TweenManager.js#L219](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/TweenManager.js#L219)  
> Since: 3.5.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [events](#events)

    - [events: Phaser.Events.EventEmitter](#events-phasereventseventemitter)
  + [gap](#gap)

    - [gap: number](#gap-number)
  + [lagSkip](#lagskip)

    - [lagSkip: number](#lagskip-number)
  + [maxLag](#maxlag)

    - [maxLag: number](#maxlag-number)
  + [nextTime](#nexttime)

    - [nextTime: number](#nexttime-number)
  + [paused](#paused)

    - [paused: boolean](#paused-boolean)
  + [prevTime](#prevtime)

    - [prevTime: number](#prevtime-number)
  + [processing](#processing)

    - [processing: boolean](#processing-boolean)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [startTime](#starttime)

    - [startTime: number](#starttime-number)
  + [time](#time)

    - [time: number](#time-number)
  + [timeScale](#timescale)

    - [timeScale: number](#timescale-number)
  + [tweens](#tweens)

    - [tweens: Array.<Phaser.Tweens.Tween>](#tweens-arrayphasertweenstween)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(config)](#instance-addconfig)
  + [addCounter](#addcounter)

    - [<instance> addCounter(config)](#instance-addcounterconfig)
  + [addMultiple](#addmultiple)

    - [<instance> addMultiple(configs)](#instance-addmultipleconfigs)
  + [chain](#chain)

    - [<instance> chain(tweens)](#instance-chaintweens)
  + [create](#create)

    - [<instance> create(config)](#instance-createconfig)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [each](#each)

    - [<instance> each(callback, [scope], [args])](#instance-eachcallback-scope-args)
  + [existing](#existing)

    - [<instance> existing(tween)](#instance-existingtween)
  + [getChainedTweens](#getchainedtweens)

    - [<instance> getChainedTweens(tween)](#instance-getchainedtweenstween)
  + [getDelta](#getdelta)

    - [<instance> getDelta([tick])](#instance-getdeltatick)
  + [getGlobalTimeScale](#getglobaltimescale)

    - [<instance> getGlobalTimeScale()](#instance-getglobaltimescale)
  + [getTweens](#gettweens)

    - [<instance> getTweens()](#instance-gettweens)
  + [getTweensOf](#gettweensof)

    - [<instance> getTweensOf(target)](#instance-gettweensoftarget)
  + [has](#has)

    - [<instance> has(tween)](#instance-hastween)
  + [isTweening](#istweening)

    - [<instance> isTweening(target)](#instance-istweeningtarget)
  + [killAll](#killall)

    - [<instance> killAll()](#instance-killall)
  + [killTweensOf](#killtweensof)

    - [<instance> killTweensOf(target)](#instance-killtweensoftarget)
  + [makeActive](#makeactive)

    - [<instance> makeActive(tween)](#instance-makeactivetween)
  + [pauseAll](#pauseall)

    - [<instance> pauseAll()](#instance-pauseall)
  + [remove](#remove)

    - [<instance> remove(tween)](#instance-removetween)
  + [reset](#reset)

    - [<instance> reset(tween)](#instance-resettween)
  + [resumeAll](#resumeall)

    - [<instance> resumeAll()](#instance-resumeall)
  + [setFps](#setfps)

    - [<instance> setFps([fps])](#instance-setfpsfps)
  + [setGlobalTimeScale](#setglobaltimescale)

    - [<instance> setGlobalTimeScale(value)](#instance-setglobaltimescalevalue)
  + [setLagSmooth](#setlagsmooth)

    - [<instance> setLagSmooth([limit], [skip])](#instance-setlagsmoothlimit-skip)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [stagger](#stagger)

    - [<instance> stagger(value, config)](#instance-staggervalue-config)
  + [step](#step)

    - [<instance> step([tick])](#instance-steptick)
  + [tick](#tick)

    - [<instance> tick()](#instance-tick)
  + [update](#update)

    - [<instance> update()](#instance-update)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [start](#start)

    - [<instance> start()](#instance-start)

Back to top

©2025[Phaser](https://docs.phaser.io)