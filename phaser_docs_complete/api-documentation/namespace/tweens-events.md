# Phaser.Tweens.Events

Scope:
static

> Source: [src/tweens/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/events/index.js#L7)

# Static functions

## TWEEN\_ACTIVE

### TWEEN\_ACTIVE

**Description:**

The Tween Active Event.

This event is dispatched by a Tween when it becomes active within the Tween Manager.

An 'active' Tween is one that is now progressing, although it may not yet be updating

any target properties, due to settings such as `delay`. If you need an event for when

the Tween starts actually updating its first property, see `TWEEN_START`.

Listen to it from a Tween instance using `Tween.on('active', listener)`, i.e.:

```
Copy
var tween = this.tweens.create({

    targets: image,

    x: 500,

    ease: 'Power1',

    duration: 3000

});

tween.on('active', listener);

this.tweens.existing(tween);


```

Note that this event is usually dispatched already by the time you call `this.tweens.add()`, and is

meant for use with `tweens.create()` and/or `tweens.existing()`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](../class/tweens-tween.md) | No | A reference to the Tween instance that emitted the event. |
| --- | --- | --- | --- |
| targets | any | Array.<any> | No | The targets of the Tween. If this Tween has multiple targets this will be an array of the targets. |

> Source: [src/tweens/events/TWEEN\_ACTIVE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/events/TWEEN_ACTIVE_EVENT.js#L7)  
> Since: 3.19.0

---

## TWEEN\_COMPLETE

### TWEEN\_COMPLETE

**Description:**

The Tween Complete Event.

This event is dispatched by a Tween when it completes playback entirely, factoring in repeats and loops.

If the Tween has been set to loop or repeat infinitely, this event will not be dispatched

unless the `Tween.stop` method is called.

If a Tween has a `completeDelay` set, this event will fire after that delay expires.

Listen to it from a Tween instance using `Tween.on('complete', listener)`, i.e.:

```
Copy
var tween = this.tweens.add({

    targets: image,

    x: 500,

    ease: 'Power1',

    duration: 3000

});

tween.on('complete', listener);


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](../class/tweens-tween.md) | No | A reference to the Tween instance that emitted the event. |
| --- | --- | --- | --- |
| targets | any | Array.<any> | No | The targets of the Tween. If this Tween has multiple targets this will be an array of the targets. |

> Source: [src/tweens/events/TWEEN\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/events/TWEEN_COMPLETE_EVENT.js#L7)  
> Since: 3.19.0

---

## TWEEN\_LOOP

### TWEEN\_LOOP

**Description:**

The Tween Loop Event.

This event is dispatched by a Tween when it loops.

This event will only be dispatched if the Tween has a loop count set.

If a Tween has a `loopDelay` set, this event will fire after that delay expires.

The difference between `loop` and `repeat` is that `repeat` is a property setting,

where-as `loop` applies to the entire Tween.

Listen to it from a Tween instance using `Tween.on('loop', listener)`, i.e.:

```
Copy
var tween = this.tweens.add({

    targets: image,

    x: 500,

    ease: 'Power1',

    duration: 3000,

    loop: 6

});

tween.on('loop', listener);


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](../class/tweens-tween.md) | No | A reference to the Tween instance that emitted the event. |
| --- | --- | --- | --- |
| targets | any | Array.<any> | No | The targets of the Tween. If this Tween has multiple targets this will be an array of the targets. |

> Source: [src/tweens/events/TWEEN\_LOOP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/events/TWEEN_LOOP_EVENT.js#L7)  
> Since: 3.19.0

---

## TWEEN\_PAUSE

### TWEEN\_PAUSE

**Description:**

The Tween Pause Event.

This event is dispatched by a Tween when it is paused.

Listen to it from a Tween instance using `Tween.on('pause', listener)`, i.e.:

```
Copy
var tween = this.tweens.add({

    targets: image,

    ease: 'Power1',

    duration: 3000,

    x: 600

});

tween.on('pause', listener);

// At some point later ...

tween.pause();


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](../class/tweens-tween.md) | No | A reference to the Tween instance that emitted the event. |
| --- | --- | --- | --- |

> Source: [src/tweens/events/TWEEN\_PAUSE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/events/TWEEN_PAUSE_EVENT.js#L7)  
> Since: 3.60.0

---

## TWEEN\_REPEAT

### TWEEN\_REPEAT

**Description:**

The Tween Repeat Event.

This event is dispatched by a Tween when one of the properties it is tweening repeats.

This event will only be dispatched if the Tween has a property with a repeat count set.

If a Tween has a `repeatDelay` set, this event will fire after that delay expires.

The difference between `loop` and `repeat` is that `repeat` is a property setting,

where-as `loop` applies to the entire Tween.

Listen to it from a Tween instance using `Tween.on('repeat', listener)`, i.e.:

```
Copy
var tween = this.tweens.add({

    targets: image,

    x: 500,

    ease: 'Power1',

    duration: 3000,

    repeat: 4

});

tween.on('repeat', listener);


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](../class/tweens-tween.md) | No | A reference to the Tween instance that emitted the event. |
| --- | --- | --- | --- |
| key | string | No | The property on the target that has just repeated, i.e. `x` or `scaleY`, or whatever property you are tweening. |
| target | any | No | The target object that was repeated. Usually a Game Object, but can be of any type. |
| current | number | No | The current value of the property being set on the target. |
| previous | number | No | The previous value of the property being set on the target. |

> Source: [src/tweens/events/TWEEN\_REPEAT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/events/TWEEN_REPEAT_EVENT.js#L7)  
> Since: 3.19.0

---

## TWEEN\_RESUME

### TWEEN\_RESUME

**Description:**

The Tween Resume Event.

This event is dispatched by a Tween when it is resumed from a paused state.

Listen to it from a Tween instance using `Tween.on('resume', listener)`, i.e.:

```
Copy
var tween = this.tweens.add({

    targets: image,

    ease: 'Power1',

    duration: 3000,

    x: 600

});

tween.on('resume', listener);

// At some point later ...

tween.resume();


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](../class/tweens-tween.md) | No | A reference to the Tween instance that emitted the event. |
| --- | --- | --- | --- |

> Source: [src/tweens/events/TWEEN\_RESUME\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/events/TWEEN_RESUME_EVENT.js#L7)  
> Since: 3.60.0

---

## TWEEN\_START

### TWEEN\_START

**Description:**

The Tween Start Event.

This event is dispatched by a Tween when it starts tweening its first property.

A Tween will only emit this event once, as it can only start once.

If a Tween has a `delay` set, this event will fire after that delay expires.

Listen to it from a Tween instance using `Tween.on('start', listener)`, i.e.:

```
Copy
var tween = this.tweens.add({

    targets: image,

    x: 500,

    ease: 'Power1',

    duration: 3000

});

tween.on('start', listener);


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](../class/tweens-tween.md) | No | A reference to the Tween instance that emitted the event. |
| --- | --- | --- | --- |
| targets | any | Array.<any> | No | The targets of the Tween. If this Tween has multiple targets this will be an array of the targets. |

> Source: [src/tweens/events/TWEEN\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/events/TWEEN_START_EVENT.js#L7)  
> Since: 3.19.0

---

## TWEEN\_STOP

### TWEEN\_STOP

**Description:**

The Tween Stop Event.

This event is dispatched by a Tween when it is stopped.

Listen to it from a Tween instance using `Tween.on('stop', listener)`, i.e.:

```
Copy
var tween = this.tweens.add({

    targets: image,

    x: 500,

    ease: 'Power1',

    duration: 3000

});

tween.on('stop', listener);


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](../class/tweens-tween.md) | No | A reference to the Tween instance that emitted the event. |
| --- | --- | --- | --- |
| targets | any | Array.<any> | No | The targets of the Tween. If this Tween has multiple targets this will be an array of the targets. |

> Source: [src/tweens/events/TWEEN\_STOP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/events/TWEEN_STOP_EVENT.js#L7)  
> Since: 3.24.0

---

## TWEEN\_UPDATE

### TWEEN\_UPDATE

**Description:**

The Tween Update Event.

This event is dispatched by a Tween every time it updates *any* of the properties it is tweening.

A Tween that is changing 3 properties of a target will emit this event 3 times per change, once per property.

**Note:** This is a very high frequency event and may be dispatched multiple times, every single frame.

Listen to it from a Tween instance using `Tween.on('update', listener)`, i.e.:

```
Copy
var tween = this.tweens.add({

    targets: image,

    x: 500,

    ease: 'Power1',

    duration: 3000,

});

tween.on('update', listener);


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](../class/tweens-tween.md) | No | A reference to the Tween instance that emitted the event. |
| --- | --- | --- | --- |
| key | string | No | The property on the target that has just updated, i.e. `x` or `scaleY`, or whatever property you are tweening. |
| target | any | No | The target object that was updated. Usually a Game Object, but can be of any type. |
| current | number | No | The current value of the property that was tweened. |
| previous | number | No | The previous value of the property that was tweened, prior to this update. |

> Source: [src/tweens/events/TWEEN\_UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/events/TWEEN_UPDATE_EVENT.js#L7)  
> Since: 3.19.0

---

## TWEEN\_YOYO

### TWEEN\_YOYO

**Description:**

The Tween Yoyo Event.

This event is dispatched by a Tween whenever a property it is tweening yoyos.

This event will only be dispatched if the Tween has a property with `yoyo` set.

If the Tween has a `hold` value, this event is dispatched when the hold expires.

This event is dispatched for every property, and for every target, that yoyos.

For example, if a Tween was updating 2 properties and had 10 targets, this event

would be dispatched 20 times (twice per target). So be careful how you use it!

Listen to it from a Tween instance using `Tween.on('yoyo', listener)`, i.e.:

```
Copy
var tween = this.tweens.add({

    targets: image,

    x: 500,

    ease: 'Power1',

    duration: 3000,

    yoyo: true

});

tween.on('yoyo', listener);


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tween | [Phaser.Tweens.Tween](../class/tweens-tween.md) | No | A reference to the Tween instance that emitted the event. |
| --- | --- | --- | --- |
| key | string | No | The property on the target that has just yoyo'd, i.e. `x` or `scaleY`, or whatever property you are tweening. |
| target | any | No | The target object that was yoyo'd. Usually a Game Object, but can be of any type. |
| current | number | No | The current value of the property being set on the target. |
| previous | number | No | The previous value of the property being set on the target. |

> Source: [src/tweens/events/TWEEN\_YOYO\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/events/TWEEN_YOYO_EVENT.js#L7)  
> Since: 3.19.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [TWEEN\_ACTIVE](#tween_active)

    - [TWEEN\_ACTIVE](#tween_active-1)
  + [TWEEN\_COMPLETE](#tween_complete)

    - [TWEEN\_COMPLETE](#tween_complete-1)
  + [TWEEN\_LOOP](#tween_loop)

    - [TWEEN\_LOOP](#tween_loop-1)
  + [TWEEN\_PAUSE](#tween_pause)

    - [TWEEN\_PAUSE](#tween_pause-1)
  + [TWEEN\_REPEAT](#tween_repeat)

    - [TWEEN\_REPEAT](#tween_repeat-1)
  + [TWEEN\_RESUME](#tween_resume)

    - [TWEEN\_RESUME](#tween_resume-1)
  + [TWEEN\_START](#tween_start)

    - [TWEEN\_START](#tween_start-1)
  + [TWEEN\_STOP](#tween_stop)

    - [TWEEN\_STOP](#tween_stop-1)
  + [TWEEN\_UPDATE](#tween_update)

    - [TWEEN\_UPDATE](#tween_update-1)
  + [TWEEN\_YOYO](#tween_yoyo)

    - [TWEEN\_YOYO](#tween_yoyo-1)

Back to top

©2025[Phaser](https://docs.phaser.io)