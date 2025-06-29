# AnimationFrame

Phaser.Animations.AnimationFrame

A single frame in an Animation sequence.

An AnimationFrame consists of a reference to the Texture it uses for rendering, references to other

frames in the animation, and index data. It also has the ability to modify the animation timing.

AnimationFrames are generated automatically by the Animation class.

**Constructor**

`new AnimationFrame(textureKey, textureFrame, index, frame, [isKeyFrame])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| textureKey | string | No |  | The key of the Texture this AnimationFrame uses. |
| --- | --- | --- | --- | --- |
| textureFrame | string | number | No |  | The key of the Frame within the Texture that this AnimationFrame uses. |
| index | number | No |  | The index of this AnimationFrame within the Animation sequence. |
| frame | [Phaser.Textures.Frame](textures-frame.md) | No |  | A reference to the Texture Frame this AnimationFrame uses for rendering. |
| isKeyFrame | boolean | Yes | false | Is this Frame a Keyframe within the Animation? |

---

**Scope**: static

> Source: [src/animations/AnimationFrame.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationFrame.js#L9)  
> Since: 3.0.0

# Public Members

## duration

### duration: number

**Description:**

The duration, in ms, of this frame of the animation.

> Source: [src/animations/AnimationFrame.js#L117](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationFrame.js#L117)  
> Since: 3.0.0

---

## frame

### frame: [Phaser.Textures.Frame](textures-frame.md)

**Description:**

A reference to the Texture Frame this AnimationFrame uses for rendering.

> Source: [src/animations/AnimationFrame.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationFrame.js#L64)  
> Since: 3.0.0

---

## index

### index: number

**Description:**

The index of this AnimationFrame within the Animation sequence.

> Source: [src/animations/AnimationFrame.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationFrame.js#L55)  
> Since: 3.0.0

---

## isFirst

### isFirst: boolean

**Description:**

Is this the first frame in an animation sequence?

> Source: [src/animations/AnimationFrame.js#L73](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationFrame.js#L73)  
> Since: 3.0.0

---

## isKeyFrame

### isKeyFrame: boolean

**Description:**

Is this Frame a KeyFrame within the Animation?

> Source: [src/animations/AnimationFrame.js#L139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationFrame.js#L139)  
> Since: 3.50.0

---

## isLast

### isLast: boolean

**Description:**

Is this the last frame in an animation sequence?

> Source: [src/animations/AnimationFrame.js#L84](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationFrame.js#L84)  
> Since: 3.0.0

---

## nextFrame

### nextFrame: [Phaser.Animations.AnimationFrame](animations-animationframe.md)

**Description:**

A reference to the AnimationFrame that comes after this one in the animation, if any.

> Source: [src/animations/AnimationFrame.js#L106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationFrame.js#L106)  
> Since: 3.0.0

---

## prevFrame

### prevFrame: [Phaser.Animations.AnimationFrame](animations-animationframe.md)

**Description:**

A reference to the AnimationFrame that comes before this one in the animation, if any.

> Source: [src/animations/AnimationFrame.js#L95](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationFrame.js#L95)  
> Since: 3.0.0

---

## progress

### progress: number

**Description:**

What % through the animation does this frame come?

This value is generated when the animation is created and cached here.

> Source: [src/animations/AnimationFrame.js#L127](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationFrame.js#L127)  
> Since: 3.0.0

---

## textureFrame

### textureFrame: string, number

**Description:**

The key of the Frame within the Texture that this AnimationFrame uses.

> Source: [src/animations/AnimationFrame.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationFrame.js#L46)  
> Since: 3.0.0

---

## textureKey

### textureKey: string

**Description:**

The key of the Texture this AnimationFrame uses.

> Source: [src/animations/AnimationFrame.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationFrame.js#L37)  
> Since: 3.0.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Destroys this object by removing references to external resources and callbacks.

> Source: [src/animations/AnimationFrame.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationFrame.js#L167)  
> Since: 3.0.0

---

## toJSON

### <instance> toJSON()

**Description:**

Generates a JavaScript object suitable for converting to JSON.

**Returns:** [Phaser.Types.Animations.JSONAnimationFrame](../typedef/types-animations.md) - The AnimationFrame data.

> Source: [src/animations/AnimationFrame.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationFrame.js#L149)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [duration](#duration)

    - [duration: number](#duration-number)
  + [frame](#frame)

    - [frame: Phaser.Textures.Frame](#frame-phasertexturesframe)
  + [index](#index)

    - [index: number](#index-number)
  + [isFirst](#isfirst)

    - [isFirst: boolean](#isfirst-boolean)
  + [isKeyFrame](#iskeyframe)

    - [isKeyFrame: boolean](#iskeyframe-boolean)
  + [isLast](#islast)

    - [isLast: boolean](#islast-boolean)
  + [nextFrame](#nextframe)

    - [nextFrame: Phaser.Animations.AnimationFrame](#nextframe-phaseranimationsanimationframe)
  + [prevFrame](#prevframe)

    - [prevFrame: Phaser.Animations.AnimationFrame](#prevframe-phaseranimationsanimationframe)
  + [progress](#progress)

    - [progress: number](#progress-number)
  + [textureFrame](#textureframe)

    - [textureFrame: string, number](#textureframe-string-number)
  + [textureKey](#texturekey)

    - [textureKey: string](#texturekey-string)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [toJSON](#tojson)

    - [<instance> toJSON()](#instance-tojson)

Back to top

©2025[Phaser](https://docs.phaser.io)