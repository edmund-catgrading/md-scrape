# Animations.Events

Phaser.Animations.Events

## ADD\_ANIMATION

**Description:** The Add Animation Event.

This event is dispatched when a new animation is added to the global Animation Manager.

This can happen either as a result of an animation instance being added to the Animation Manager,

or the Animation Manager creating a new animation directly.

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the Animation that was added to the global Animation Manager. |
| --- | --- | --- | --- |
| animation | [Phaser.Animations.Animation](../class/animations-animation.md) | No | An instance of the newly created Animation. |

**Member of:** [Phaser.Animations.Events](../namespace/animations-events.md)

> Source: [src/animations/events/ADD\_ANIMATION\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/events/ADD_ANIMATION_EVENT.js#L7)  
> Since: 3.0.0

## ANIMATION\_COMPLETE

**Description:** The Animation Complete Event.

This event is dispatched by a Sprite when an animation playing on it completes playback.

This happens when the animation gets to the end of its sequence, factoring in any delays

or repeats it may have to process.

An animation that is set to loop, or repeat forever, will never fire this event, because

it never actually completes. If you need to handle this, listen for the `ANIMATION_STOP`

event instead, as this is emitted when the animation is stopped directly.

Listen for it on the Sprite using `sprite.on('animationcomplete', listener)`

The animation event flow is as follows:

1. `ANIMATION_START`
2. `ANIMATION_UPDATE` (repeated for however many frames the animation has)
3. `ANIMATION_REPEAT` (only if the animation is set to repeat, it then emits more update events after this)
4. `ANIMATION_COMPLETE` (only if there is a finite, or zero, repeat count)
5. `ANIMATION_COMPLETE_KEY` (only if there is a finite, or zero, repeat count)

If the animation is stopped directly, the `ANIMATION_STOP` event is dispatched instead of `ANIMATION_COMPLETE`.

If the animation is restarted while it is already playing, `ANIMATION_RESTART` is emitted.

| name | type | optional | description |
| --- | --- | --- | --- |
| animation | [Phaser.Animations.Animation](../class/animations-animation.md) | No | A reference to the Animation that completed. |
| --- | --- | --- | --- |
| frame | [Phaser.Animations.AnimationFrame](../class/animations-animationframe.md) | No | The current Animation Frame of the Animation. |
| gameObject | [Phaser.GameObjects.Sprite](../class/gameobjects-sprite.md) | No | A reference to the Game Object on which the animation updated. |
| frameKey | string | No | The unique key of the Animation Frame within the Animation. |

**Member of:** [Phaser.Animations.Events](../namespace/animations-events.md)

> Source: [src/animations/events/ANIMATION\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/events/ANIMATION_COMPLETE_EVENT.js#L7)  
> Since: 3.50.0

## ANIMATION\_COMPLETE\_KEY

**Description:** The Animation Complete Dynamic Key Event.

This event is dispatched by a Sprite when an animation playing on it completes playback.

This happens when the animation gets to the end of its sequence, factoring in any delays

or repeats it may have to process.

An animation that is set to loop, or repeat forever, will never fire this event, because

it never actually completes. If you need to handle this, listen for the `ANIMATION_STOP`

event instead, as this is emitted when the animation is stopped directly.

The difference between this and the `ANIMATION_COMPLETE` event is that this one has a

dynamic event name that contains the name of the animation within it. For example,

if you had an animation called `explode` you could listen for the completion of that

specific animation by using: `sprite.on('animationcomplete-explode', listener)`. Or, if you

wish to use types: `sprite.on(Phaser.Animations.Events.ANIMATION_COMPLETE_KEY + 'explode', listener)`.

The animation event flow is as follows:

1. `ANIMATION_START`
2. `ANIMATION_UPDATE` (repeated for however many frames the animation has)
3. `ANIMATION_REPEAT` (only if the animation is set to repeat, it then emits more update events after this)
4. `ANIMATION_COMPLETE` (only if there is a finite, or zero, repeat count)
5. `ANIMATION_COMPLETE_KEY` (only if there is a finite, or zero, repeat count)

If the animation is stopped directly, the `ANIMATION_STOP` event is dispatched instead of `ANIMATION_COMPLETE`.

If the animation is restarted while it is already playing, `ANIMATION_RESTART` is emitted.

| name | type | optional | description |
| --- | --- | --- | --- |
| animation | [Phaser.Animations.Animation](../class/animations-animation.md) | No | A reference to the Animation that completed. |
| --- | --- | --- | --- |
| frame | [Phaser.Animations.AnimationFrame](../class/animations-animationframe.md) | No | The current Animation Frame of the Animation. |
| gameObject | [Phaser.GameObjects.Sprite](../class/gameobjects-sprite.md) | No | A reference to the Game Object on which the animation updated. |
| frameKey | string | No | The unique key of the Animation Frame within the Animation. |

**Member of:** [Phaser.Animations.Events](../namespace/animations-events.md)

> Source: [src/animations/events/ANIMATION\_COMPLETE\_KEY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/events/ANIMATION_COMPLETE_KEY_EVENT.js#L7)  
> Since: 3.50.0

## ANIMATION\_REPEAT

**Description:** The Animation Repeat Event.

This event is dispatched by a Sprite when an animation repeats playing on it.

This happens if the animation was created, or played, with a `repeat` value specified.

An animation will repeat when it reaches the end of its sequence.

Listen for it on the Sprite using `sprite.on('animationrepeat', listener)`

The animation event flow is as follows:

1. `ANIMATION_START`
2. `ANIMATION_UPDATE` (repeated for however many frames the animation has)
3. `ANIMATION_REPEAT` (only if the animation is set to repeat, it then emits more update events after this)
4. `ANIMATION_COMPLETE` (only if there is a finite, or zero, repeat count)
5. `ANIMATION_COMPLETE_KEY` (only if there is a finite, or zero, repeat count)

If the animation is stopped directly, the `ANIMATION_STOP` event is dispatched instead of `ANIMATION_COMPLETE`.

If the animation is restarted while it is already playing, `ANIMATION_RESTART` is emitted.

| name | type | optional | description |
| --- | --- | --- | --- |
| animation | [Phaser.Animations.Animation](../class/animations-animation.md) | No | A reference to the Animation that has repeated. |
| --- | --- | --- | --- |
| frame | [Phaser.Animations.AnimationFrame](../class/animations-animationframe.md) | No | The current Animation Frame of the Animation. |
| gameObject | [Phaser.GameObjects.Sprite](../class/gameobjects-sprite.md) | No | A reference to the Game Object on which the animation repeated. |
| frameKey | string | No | The unique key of the Animation Frame within the Animation. |

**Member of:** [Phaser.Animations.Events](../namespace/animations-events.md)

> Source: [src/animations/events/ANIMATION\_REPEAT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/events/ANIMATION_REPEAT_EVENT.js#L7)  
> Since: 3.50.0

## ANIMATION\_RESTART

**Description:** The Animation Restart Event.

This event is dispatched by a Sprite when an animation restarts playing on it.

This only happens when the `Sprite.anims.restart` method is called.

Listen for it on the Sprite using `sprite.on('animationrestart', listener)`

The animation event flow is as follows:

1. `ANIMATION_START`
2. `ANIMATION_UPDATE` (repeated for however many frames the animation has)
3. `ANIMATION_REPEAT` (only if the animation is set to repeat, it then emits more update events after this)
4. `ANIMATION_COMPLETE` (only if there is a finite, or zero, repeat count)
5. `ANIMATION_COMPLETE_KEY` (only if there is a finite, or zero, repeat count)

If the animation is stopped directly, the `ANIMATION_STOP` event is dispatched instead of `ANIMATION_COMPLETE`.

If the animation is restarted while it is already playing, `ANIMATION_RESTART` is emitted.

| name | type | optional | description |
| --- | --- | --- | --- |
| animation | [Phaser.Animations.Animation](../class/animations-animation.md) | No | A reference to the Animation that has restarted. |
| --- | --- | --- | --- |
| frame | [Phaser.Animations.AnimationFrame](../class/animations-animationframe.md) | No | The current Animation Frame of the Animation. |
| gameObject | [Phaser.GameObjects.Sprite](../class/gameobjects-sprite.md) | No | A reference to the Game Object on which the animation restarted. |
| frameKey | string | No | The unique key of the Animation Frame within the Animation. |

**Member of:** [Phaser.Animations.Events](../namespace/animations-events.md)

> Source: [src/animations/events/ANIMATION\_RESTART\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/events/ANIMATION_RESTART_EVENT.js#L7)  
> Since: 3.50.0

## ANIMATION\_START

**Description:** The Animation Start Event.

This event is dispatched by a Sprite when an animation starts playing on it.

This happens when the animation is played, factoring in any delay that may have been specified.

This event happens after the delay has expired and prior to the first update event.

Listen for it on the Sprite using `sprite.on('animationstart', listener)`

The animation event flow is as follows:

1. `ANIMATION_START`
2. `ANIMATION_UPDATE` (repeated for however many frames the animation has)
3. `ANIMATION_REPEAT` (only if the animation is set to repeat, it then emits more update events after this)
4. `ANIMATION_COMPLETE` (only if there is a finite, or zero, repeat count)
5. `ANIMATION_COMPLETE_KEY` (only if there is a finite, or zero, repeat count)

If the animation is stopped directly, the `ANIMATION_STOP` event is dispatched instead of `ANIMATION_COMPLETE`.

If the animation is restarted while it is already playing, `ANIMATION_RESTART` is emitted.

| name | type | optional | description |
| --- | --- | --- | --- |
| animation | [Phaser.Animations.Animation](../class/animations-animation.md) | No | A reference to the Animation that has started. |
| --- | --- | --- | --- |
| frame | [Phaser.Animations.AnimationFrame](../class/animations-animationframe.md) | No | The current Animation Frame of the Animation. |
| gameObject | [Phaser.GameObjects.Sprite](../class/gameobjects-sprite.md) | No | A reference to the Game Object on which the animation started. |
| frameKey | string | No | The unique key of the Animation Frame within the Animation. |

**Member of:** [Phaser.Animations.Events](../namespace/animations-events.md)

> Source: [src/animations/events/ANIMATION\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/events/ANIMATION_START_EVENT.js#L7)  
> Since: 3.50.0

## ANIMATION\_STOP

**Description:** The Animation Stop Event.

This event is dispatched by a Sprite when an animation is stopped on it. An animation

will only be stopeed if a method such as `Sprite.stop` or `Sprite.anims.stopAfterDelay`

is called. It can also be emitted if a new animation is started before the current one completes.

Listen for it on the Sprite using `sprite.on('animationstop', listener)`

The animation event flow is as follows:

1. `ANIMATION_START`
2. `ANIMATION_UPDATE` (repeated for however many frames the animation has)
3. `ANIMATION_REPEAT` (only if the animation is set to repeat, it then emits more update events after this)
4. `ANIMATION_COMPLETE` (only if there is a finite, or zero, repeat count)
5. `ANIMATION_COMPLETE_KEY` (only if there is a finite, or zero, repeat count)

If the animation is stopped directly, the `ANIMATION_STOP` event is dispatched instead of `ANIMATION_COMPLETE`.

If the animation is restarted while it is already playing, `ANIMATION_RESTART` is emitted.

| name | type | optional | description |
| --- | --- | --- | --- |
| animation | [Phaser.Animations.Animation](../class/animations-animation.md) | No | A reference to the Animation that has stopped. |
| --- | --- | --- | --- |
| frame | [Phaser.Animations.AnimationFrame](../class/animations-animationframe.md) | No | The current Animation Frame of the Animation. |
| gameObject | [Phaser.GameObjects.Sprite](../class/gameobjects-sprite.md) | No | A reference to the Game Object on which the animation stopped. |
| frameKey | string | No | The unique key of the Animation Frame within the Animation. |

**Member of:** [Phaser.Animations.Events](../namespace/animations-events.md)

> Source: [src/animations/events/ANIMATION\_STOP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/events/ANIMATION_STOP_EVENT.js#L7)  
> Since: 3.50.0

## ANIMATION\_UPDATE

**Description:** The Animation Update Event.

This event is dispatched by a Sprite when an animation playing on it updates. This happens when the animation changes frame.

An animation will change frame based on the frame rate and other factors like `timeScale` and `delay`. It can also change

frame when stopped or restarted.

Listen for it on the Sprite using `sprite.on('animationupdate', listener)`

If an animation is playing faster than the game frame-rate can handle, it's entirely possible for it to emit several

update events in a single game frame, so please be aware of this in your code. The **final** event received that frame

is the one that is rendered to the game.

The animation event flow is as follows:

1. `ANIMATION_START`
2. `ANIMATION_UPDATE` (repeated for however many frames the animation has)
3. `ANIMATION_REPEAT` (only if the animation is set to repeat, it then emits more update events after this)
4. `ANIMATION_COMPLETE` (only if there is a finite, or zero, repeat count)
5. `ANIMATION_COMPLETE_KEY` (only if there is a finite, or zero, repeat count)

If the animation is stopped directly, the `ANIMATION_STOP` event is dispatched instead of `ANIMATION_COMPLETE`.

If the animation is restarted while it is already playing, `ANIMATION_RESTART` is emitted.

| name | type | optional | description |
| --- | --- | --- | --- |
| animation | [Phaser.Animations.Animation](../class/animations-animation.md) | No | A reference to the Animation that has updated. |
| --- | --- | --- | --- |
| frame | [Phaser.Animations.AnimationFrame](../class/animations-animationframe.md) | No | The current Animation Frame of the Animation. |
| gameObject | [Phaser.GameObjects.Sprite](../class/gameobjects-sprite.md) | No | A reference to the Game Object on which the animation updated. |
| frameKey | string | No | The unique key of the Animation Frame within the Animation. |

**Member of:** [Phaser.Animations.Events](../namespace/animations-events.md)

> Source: [src/animations/events/ANIMATION\_UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/events/ANIMATION_UPDATE_EVENT.js#L7)  
> Since: 3.50.0

## PAUSE\_ALL

**Description:** The Pause All Animations Event.

This event is dispatched when the global Animation Manager is told to pause.

When this happens all current animations will stop updating, although it doesn't necessarily mean

that the game has paused as well.

**Member of:** [Phaser.Animations.Events](../namespace/animations-events.md)

> Source: [src/animations/events/PAUSE\_ALL\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/events/PAUSE_ALL_EVENT.js#L7)  
> Since: 3.0.0

## REMOVE\_ANIMATION

**Description:** The Remove Animation Event.

This event is dispatched when an animation is removed from the global Animation Manager.

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the Animation that was removed from the global Animation Manager. |
| --- | --- | --- | --- |
| animation | [Phaser.Animations.Animation](../class/animations-animation.md) | No | An instance of the removed Animation. |

**Member of:** [Phaser.Animations.Events](../namespace/animations-events.md)

> Source: [src/animations/events/REMOVE\_ANIMATION\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/events/REMOVE_ANIMATION_EVENT.js#L7)  
> Since: 3.0.0

## RESUME\_ALL

**Description:** The Resume All Animations Event.

This event is dispatched when the global Animation Manager resumes, having been previously paused.

When this happens all current animations will continue updating again.

**Member of:** [Phaser.Animations.Events](../namespace/animations-events.md)

> Source: [src/animations/events/RESUME\_ALL\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/events/RESUME_ALL_EVENT.js#L7)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Animations.Events](#animationsevents)

  + [ADD\_ANIMATION](#add_animation)
  + [ANIMATION\_COMPLETE](#animation_complete)
  + [ANIMATION\_COMPLETE\_KEY](#animation_complete_key)
  + [ANIMATION\_REPEAT](#animation_repeat)
  + [ANIMATION\_RESTART](#animation_restart)
  + [ANIMATION\_START](#animation_start)
  + [ANIMATION\_STOP](#animation_stop)
  + [ANIMATION\_UPDATE](#animation_update)
  + [PAUSE\_ALL](#pause_all)
  + [REMOVE\_ANIMATION](#remove_animation)
  + [RESUME\_ALL](#resume_all)

Back to top

©2025[Phaser](https://docs.phaser.io)



Animations.Events