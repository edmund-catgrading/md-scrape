# Phaser.GameObjects.Components.PathFollower

Scope:
static

> Source: [src/gameobjects/components/PathFollower.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PathFollower.js#L13)  
> Since: 3.17.0

# Static functions

## path

### path: [Phaser.Curves.Path](../class/curves-path.md)

**Description:**

The Path this PathFollower is following. It can only follow one Path at a time.

> Source: [src/gameobjects/components/PathFollower.js#L23](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PathFollower.js#L23)  
> Since: 3.0.0

---

## rotateToPath

### rotateToPath: boolean

**Description:**

Should the PathFollower automatically rotate to point in the direction of the Path?

> Source: [src/gameobjects/components/PathFollower.js#L32](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PathFollower.js#L32)  
> Since: 3.0.0

---

# Static functions

## isFollowing

### <instance> isFollowing()

**Description:**

Is this PathFollower actively following a Path or not?

To be considered as `isFollowing` it must be currently moving on a Path, and not paused.

**Returns:** boolean - `true` is this PathFollower is actively following a Path, otherwise `false`.

> Source: [src/gameobjects/components/PathFollower.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PathFollower.js#L167)  
> Since: 3.0.0

---

## pathUpdate

### <instance> pathUpdate()

**Description:**

Internal update handler that advances this PathFollower along the path.

Called automatically by the Scene step, should not typically be called directly.

> Source: [src/gameobjects/components/PathFollower.js#L350](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PathFollower.js#L350)  
> Since: 3.17.0

---

## pauseFollow

### <instance> pauseFollow()

**Description:**

Pauses this PathFollower. It will still continue to render, but it will remain motionless at the

point on the Path at which you paused it.

**Returns:** [Phaser.GameObjects.Components.PathFollower](gameobjects-components-pathfollower.md) - This Game Object.

> Source: [src/gameobjects/components/PathFollower.js#L285](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PathFollower.js#L285)  
> Since: 3.3.0

---

## resumeFollow

### <instance> resumeFollow()

**Description:**

Resumes a previously paused PathFollower.

If the PathFollower was not paused this has no effect.

**Returns:** [Phaser.GameObjects.Components.PathFollower](gameobjects-components-pathfollower.md) - This Game Object.

> Source: [src/gameobjects/components/PathFollower.js#L306](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PathFollower.js#L306)  
> Since: 3.3.0

---

## setPath

### <instance> setPath(path, [config])

**Description:**

Set the Path that this PathFollower should follow.

Optionally accepts [Phaser.Types.GameObjects.PathFollower.PathConfig](../typedef/types-gameobjects-pathfollower.md) settings.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| path | [Phaser.Curves.Path](../class/curves-path.md) | No | The Path this PathFollower is following. It can only follow one Path at a time. |
| --- | --- | --- | --- |
| config | number | [Phaser.Types.GameObjects.PathFollower.PathConfig](../typedef/types-gameobjects-pathfollower.md) | [Phaser.Types.Tweens.NumberTweenBuilderConfig](../typedef/types-tweens.md) | Yes |

**Returns:** [Phaser.GameObjects.Components.PathFollower](gameobjects-components-pathfollower.md) - This Game Object.

> Source: [src/gameobjects/components/PathFollower.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PathFollower.js#L111)  
> Since: 3.0.0

---

## setRotateToPath

### <instance> setRotateToPath(value, [offset])

**Description:**

Set whether the PathFollower should automatically rotate to point in the direction of the Path.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | No |  | Whether the PathFollower should automatically rotate to point in the direction of the Path. |
| --- | --- | --- | --- | --- |
| offset | number | Yes | 0 | Rotation offset in degrees. |

**Returns:** [Phaser.GameObjects.Components.PathFollower](gameobjects-components-pathfollower.md) - This Game Object.

> Source: [src/gameobjects/components/PathFollower.js#L145](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PathFollower.js#L145)  
> Since: 3.0.0

---

## startFollow

### <instance> startFollow([config], [startAt])

**Description:**

Starts this PathFollower following its given Path.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| config | number | [Phaser.Types.GameObjects.PathFollower.PathConfig](../typedef/types-gameobjects-pathfollower.md) | [Phaser.Types.Tweens.NumberTweenBuilderConfig](../typedef/types-tweens.md) | Yes | "{}" |
| --- | --- | --- | --- | --- |
| startAt | number | Yes | 0 | Optional start position of the follow, between 0 and 1. |

**Returns:** [Phaser.GameObjects.Components.PathFollower](gameobjects-components-pathfollower.md) - This Game Object.

> Source: [src/gameobjects/components/PathFollower.js#L184](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PathFollower.js#L184)  
> Since: 3.3.0

---

## stopFollow

### <instance> stopFollow()

**Description:**

Stops this PathFollower from following the path any longer.

This will invoke any 'stop' conditions that may exist on the Path, or for the follower.

**Returns:** [Phaser.GameObjects.Components.PathFollower](gameobjects-components-pathfollower.md) - This Game Object.

> Source: [src/gameobjects/components/PathFollower.js#L328](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PathFollower.js#L328)  
> Since: 3.3.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [path](#path)

    - [path: Phaser.Curves.Path](#path-phasercurvespath)
  + [rotateToPath](#rotatetopath)

    - [rotateToPath: boolean](#rotatetopath-boolean)
* [Static functions](#static-functions-1)

  + [isFollowing](#isfollowing)

    - [<instance> isFollowing()](#instance-isfollowing)
  + [pathUpdate](#pathupdate)

    - [<instance> pathUpdate()](#instance-pathupdate)
  + [pauseFollow](#pausefollow)

    - [<instance> pauseFollow()](#instance-pausefollow)
  + [resumeFollow](#resumefollow)

    - [<instance> resumeFollow()](#instance-resumefollow)
  + [setPath](#setpath)

    - [<instance> setPath(path, [config])](#instance-setpathpath-config)
  + [setRotateToPath](#setrotatetopath)

    - [<instance> setRotateToPath(value, [offset])](#instance-setrotatetopathvalue-offset)
  + [startFollow](#startfollow)

    - [<instance> startFollow([config], [startAt])](#instance-startfollowconfig-startat)
  + [stopFollow](#stopfollow)

    - [<instance> stopFollow()](#instance-stopfollow)

Back to top

©2025[Phaser](https://docs.phaser.io)



Phaser.GameObjects.Components.PathFollower