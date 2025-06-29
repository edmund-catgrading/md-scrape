# Tweens

Phaser.Tweens

## CREATED

### CREATED: number

**Description:**

TweenData state.

> Source: [src/tweens/tween/const.js#L25](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L25)  
> Since: 3.0.0

## DELAY

### DELAY: number

**Description:**

TweenData state.

> Source: [src/tweens/tween/const.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L37)  
> Since: 3.0.0

## PENDING\_RENDER

### PENDING\_RENDER: number

**Description:**

TweenData state.

> Source: [src/tweens/tween/const.js#L49](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L49)  
> Since: 3.0.0

## PLAYING\_FORWARD

### PLAYING\_FORWARD: number

**Description:**

TweenData state.

> Source: [src/tweens/tween/const.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L59)  
> Since: 3.0.0

## PLAYING\_BACKWARD

### PLAYING\_BACKWARD: number

**Description:**

TweenData state.

> Source: [src/tweens/tween/const.js#L69](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L69)  
> Since: 3.0.0

## HOLD\_DELAY

### HOLD\_DELAY: number

**Description:**

TweenData state.

> Source: [src/tweens/tween/const.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L79)  
> Since: 3.0.0

## REPEAT\_DELAY

### REPEAT\_DELAY: number

**Description:**

TweenData state.

> Source: [src/tweens/tween/const.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L89)  
> Since: 3.0.0

## COMPLETE

### COMPLETE: number

**Description:**

TweenData state.

> Source: [src/tweens/tween/const.js#L99](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L99)  
> Since: 3.0.0

## PENDING

### PENDING: number

**Description:**

Tween state. The Tween has been created but has not yet been added to the Tween Manager.

> Source: [src/tweens/tween/const.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L111)  
> Since: 3.0.0

## ACTIVE

### ACTIVE: number

**Description:**

Tween state. The Tween is active within the Tween Manager. This means it is either playing,

or was playing and is currently paused, but in both cases it's still being processed by

the Tween Manager, so is considered 'active'.

> Source: [src/tweens/tween/const.js#L121](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L121)  
> Since: 3.0.0

## LOOP\_DELAY

### LOOP\_DELAY: number

**Description:**

Tween state. The Tween is waiting for a loop countdown to elapse.

> Source: [src/tweens/tween/const.js#L133](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L133)  
> Since: 3.0.0

## COMPLETE\_DELAY

### COMPLETE\_DELAY: number

**Description:**

Tween state. The Tween is waiting for a complete delay to elapse.

> Source: [src/tweens/tween/const.js#L143](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L143)  
> Since: 3.0.0

## START\_DELAY

### START\_DELAY: number

**Description:**

Tween state. The Tween is waiting for a starting delay to elapse.

> Source: [src/tweens/tween/const.js#L153](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L153)  
> Since: 3.0.0

## PENDING\_REMOVE

### PENDING\_REMOVE: number

**Description:**

Tween state. The Tween has finished playback and is waiting to be removed from the Tween Manager.

> Source: [src/tweens/tween/const.js#L163](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L163)  
> Since: 3.0.0

## REMOVED

### REMOVED: number

**Description:**

Tween state. The Tween has been removed from the Tween Manager.

> Source: [src/tweens/tween/const.js#L173](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L173)  
> Since: 3.0.0

## FINISHED

### FINISHED: number

**Description:**

Tween state. The Tween has finished playback but was flagged as 'persistent' during creation,

so will not be automatically removed by the Tween Manager.

> Source: [src/tweens/tween/const.js#L183](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L183)  
> Since: 3.60.0

## DESTROYED

### DESTROYED: number

**Description:**

Tween state. The Tween has been destroyed and can no longer be played by a Tween Manager.

> Source: [src/tweens/tween/const.js#L194](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L194)  
> Since: 3.60.0

## MAX

### MAX: number

**Description:**

A large integer value used for 'infinite' style countdowns.

Similar use-case to Number.MAX\_SAFE\_INTEGER but we cannot use that because it's not

supported on IE.

> Source: [src/tweens/tween/const.js#L204](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/const.js#L204)  
> Since: 3.60.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Tweens](#tweens)

  + [CREATED](#created)

    - [CREATED: number](#created-number)
  + [DELAY](#delay)

    - [DELAY: number](#delay-number)
  + [PENDING\_RENDER](#pending_render)

    - [PENDING\_RENDER: number](#pending_render-number)
  + [PLAYING\_FORWARD](#playing_forward)

    - [PLAYING\_FORWARD: number](#playing_forward-number)
  + [PLAYING\_BACKWARD](#playing_backward)

    - [PLAYING\_BACKWARD: number](#playing_backward-number)
  + [HOLD\_DELAY](#hold_delay)

    - [HOLD\_DELAY: number](#hold_delay-number)
  + [REPEAT\_DELAY](#repeat_delay)

    - [REPEAT\_DELAY: number](#repeat_delay-number)
  + [COMPLETE](#complete)

    - [COMPLETE: number](#complete-number)
  + [PENDING](#pending)

    - [PENDING: number](#pending-number)
  + [ACTIVE](#active)

    - [ACTIVE: number](#active-number)
  + [LOOP\_DELAY](#loop_delay)

    - [LOOP\_DELAY: number](#loop_delay-number)
  + [COMPLETE\_DELAY](#complete_delay)

    - [COMPLETE\_DELAY: number](#complete_delay-number)
  + [START\_DELAY](#start_delay)

    - [START\_DELAY: number](#start_delay-number)
  + [PENDING\_REMOVE](#pending_remove)

    - [PENDING\_REMOVE: number](#pending_remove-number)
  + [REMOVED](#removed)

    - [REMOVED: number](#removed-number)
  + [FINISHED](#finished)

    - [FINISHED: number](#finished-number)
  + [DESTROYED](#destroyed)

    - [DESTROYED: number](#destroyed-number)
  + [MAX](#max)

    - [MAX: number](#max-number)

Back to top

©2025[Phaser](https://docs.phaser.io)