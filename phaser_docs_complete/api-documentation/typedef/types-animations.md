# Types.Animations

Phaser.Types.Animations

## Animation

### <static> Animation

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | Yes |  | The key that the animation will be associated with. i.e. sprite.animations.play(key) |
| --- | --- | --- | --- | --- |
| frames | string | Array.<[Phaser.Types.Animations.AnimationFrame](types-animations.md)> | Yes |  | Either a string, in which case it will use all frames from a texture with the matching key, or an array of Animation Frame configuration objects. |
| sortFrames | boolean | Yes | true | If you provide a string for `frames` you can optionally have the frame names numerically sorted. |
| defaultTextureKey | string | Yes | null | The key of the texture all frames of the animation will use. Can be overridden on a per frame basis. |
| frameRate | number | Yes |  | The frame rate of playback in frames per second (default 24 if duration is null) |
| duration | number | Yes |  | How long the animation should play for in milliseconds. If not given its derived from frameRate. |
| skipMissedFrames | boolean | Yes | true | Skip frames if the time lags, or always advanced anyway? |
| delay | number | Yes | 0 | Delay before starting playback. Value given in milliseconds. |
| repeat | number | Yes | 0 | Number of times to repeat the animation (-1 for infinity) |
| repeatDelay | number | Yes | 0 | Delay before the animation repeats. Value given in milliseconds. |
| yoyo | boolean | Yes | false | Should the animation yoyo? (reverse back down to the start) before repeating? |
| showBeforeDelay | boolean | Yes | false | If this animation has a delay, should it show the first frame immediately (true), or only after the delay (false) |
| showOnStart | boolean | Yes | false | Should sprite.visible = true when the animation starts to play? This happens *after* any delay, if set. |
| hideOnComplete | boolean | Yes | false | Should sprite.visible = false when the animation finishes? |
| randomFrame | boolean | Yes | false | Start playback of this animation from a randomly selected frame? |

**Type**: object

**Member of**: Phaser.Types.Animations

> Source: [src/animations/typedefs/Animation.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/typedefs/Animation.js#L1)  
> Since: 3.0.0

---

## AnimationFrame

### <static> AnimationFrame

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | Yes |  | The key of the texture within the Texture Manager to use for this Animation Frame. |
| --- | --- | --- | --- | --- |
| frame | string | number | Yes |  | The key, or index number, of the frame within the texture to use for this Animation Frame. |
| duration | number | Yes | 0 | The duration, in ms, of this frame of the animation. |
| visible | boolean | Yes |  | Should the parent Game Object be visible during this frame of the animation? |

**Type**: object

**Member of**: Phaser.Types.Animations

> Source: [src/animations/typedefs/AnimationFrame.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/typedefs/AnimationFrame.js#L1)  
> Since: 3.0.0

---

## GenerateFrameNames

### <static> GenerateFrameNames

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| prefix | string | Yes | "''" | The string to append to every resulting frame name if using a range or an array of `frames`. |
| --- | --- | --- | --- | --- |
| start | number | Yes | 0 | If `frames` is not provided, the number of the first frame to return. |
| end | number | Yes | 0 | If `frames` is not provided, the number of the last frame to return. |
| suffix | string | Yes | "''" | The string to append to every resulting frame name if using a range or an array of `frames`. |
| zeroPad | number | Yes | 0 | The minimum expected lengths of each resulting frame's number. Numbers will be left-padded with zeroes until they are this long, then prepended and appended to create the resulting frame name. |
| outputArray | Array.<[Phaser.Types.Animations.AnimationFrame](types-animations.md)> | Yes | "[]" | The array to append the created configuration objects to. |
| frames | boolean | Array.<number> | Yes | false | If provided as an array, the range defined by `start` and `end` will be ignored and these frame numbers will be used. |

**Type**: object

**Member of**: Phaser.Types.Animations

> Source: [src/animations/typedefs/GenerateFrameNames.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/typedefs/GenerateFrameNames.js#L1)  
> Since: 3.0.0

---

## GenerateFrameNumbers

### <static> GenerateFrameNumbers

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| start | number | Yes | 0 | The starting frame of the animation. |
| --- | --- | --- | --- | --- |
| end | number | Yes | -1 | The ending frame of the animation. |
| first | boolean | number | Yes | false | A frame to put at the beginning of the animation, before `start` or `outputArray` or `frames`. |
| outputArray | Array.<[Phaser.Types.Animations.AnimationFrame](types-animations.md)> | Yes | "[]" | An array to concatenate the output onto. |
| frames | boolean | Array.<number> | Yes | false | A custom sequence of frames. |

**Type**: object

**Member of**: Phaser.Types.Animations

> Source: [src/animations/typedefs/GenerateFrameNumbers.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/typedefs/GenerateFrameNumbers.js#L1)  
> Since: 3.0.0

---

## JSONAnimation

### <static> JSONAnimation

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key that the animation will be associated with. i.e. sprite.animations.play(key) |
| --- | --- | --- | --- |
| type | string | No | A frame based animation (as opposed to a bone based animation) |
| frames | Array.<[Phaser.Types.Animations.JSONAnimationFrame](types-animations.md)> | No | An array of the AnimationFrame objects inside this Animation. |
| frameRate | number | No | The frame rate of playback in frames per second (default 24 if duration is null) |
| duration | number | No | How long the animation should play for in milliseconds. If not given its derived from frameRate. |
| skipMissedFrames | boolean | No | Skip frames if the time lags, or always advanced anyway? |
| delay | number | No | Delay before starting playback. Value given in milliseconds. |
| repeat | number | No | Number of times to repeat the animation (-1 for infinity) |
| repeatDelay | number | No | Delay before the animation repeats. Value given in milliseconds. |
| yoyo | boolean | No | Should the animation yoyo? (reverse back down to the start) before repeating? |
| showBeforeDelay | boolean | No | If this animation has a delay, should it show the first frame immediately (true), or only after the delay (false) |
| showOnStart | boolean | No | Should sprite.visible = true when the animation starts to play? |
| hideOnComplete | boolean | No | Should sprite.visible = false when the animation finishes? |
| randomFrame | boolean | Yes | Start playback of this animation from a randomly selected frame? |

**Type**: object

**Member of**: Phaser.Types.Animations

> Source: [src/animations/typedefs/JSONAnimation.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/typedefs/JSONAnimation.js#L1)  
> Since: 3.0.0

---

## JSONAnimationFrame

### <static> JSONAnimationFrame

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the Texture this AnimationFrame uses. |
| --- | --- | --- | --- |
| frame | string | number | No | The key of the Frame within the Texture that this AnimationFrame uses. |
| duration | number | No | Additional time (in ms) that this frame should appear for during playback. |

**Type**: object

**Member of**: Phaser.Types.Animations

> Source: [src/animations/typedefs/JSONAnimationFrame.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/typedefs/JSONAnimationFrame.js#L1)  
> Since: 3.0.0

---

## JSONAnimations

### <static> JSONAnimations

| name | type | optional | description |
| --- | --- | --- | --- |
| anims | Array.<[Phaser.Types.Animations.JSONAnimation](types-animations.md)> | No | An array of all Animations added to the Animation Manager. |
| --- | --- | --- | --- |
| globalTimeScale | number | No | The global time scale of the Animation Manager. |

**Type**: object

**Member of**: Phaser.Types.Animations

> Source: [src/animations/typedefs/JSONAnimations.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/typedefs/JSONAnimations.js#L1)  
> Since: 3.0.0

---

## PlayAnimationConfig

### <static> PlayAnimationConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Animations.Animation](../class/animations-animation.md) | No | The string-based key of the animation to play, or an Animation instance. |
| --- | --- | --- | --- |
| frameRate | number | Yes | The frame rate of playback in frames per second (default 24 if duration is null) |
| duration | number | Yes | How long the animation should play for in milliseconds. If not given its derived from frameRate. |
| delay | number | Yes | Delay before starting playback. Value given in milliseconds. |
| repeat | number | Yes | Number of times to repeat the animation (-1 for infinity) |
| repeatDelay | number | Yes | Delay before the animation repeats. Value given in milliseconds. |
| yoyo | boolean | Yes | Should the animation yoyo? (reverse back down to the start) before repeating? |
| showBeforeDelay | boolean | Yes | If this animation has a delay, should it show the first frame immediately (true), or only after the delay (false) |
| showOnStart | boolean | Yes | Should sprite.visible = true when the animation starts to play? |
| hideOnComplete | boolean | Yes | Should sprite.visible = false when the animation finishes? |
| skipMissedFrames | boolean | Yes | Skip frames if the time lags, or always advanced anyway? |
| startFrame | number | Yes | The frame of the animation to start playback from. |
| timeScale | number | Yes | The time scale to be applied to playback of this animation. |
| randomFrame | boolean | Yes | Start playback of this animation from a randomly selected frame? |

**Type**: object

**Member of**: Phaser.Types.Animations

> Source: [src/animations/typedefs/PlayAnimationConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/typedefs/PlayAnimationConfig.js#L1)  
> Since: 3.50.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Animations](#typesanimations)

  + [Animation](#animation)

    - [<static> Animation](#static-animation)
  + [AnimationFrame](#animationframe)

    - [<static> AnimationFrame](#static-animationframe)
  + [GenerateFrameNames](#generateframenames)

    - [<static> GenerateFrameNames](#static-generateframenames)
  + [GenerateFrameNumbers](#generateframenumbers)

    - [<static> GenerateFrameNumbers](#static-generateframenumbers)
  + [JSONAnimation](#jsonanimation)

    - [<static> JSONAnimation](#static-jsonanimation)
  + [JSONAnimationFrame](#jsonanimationframe)

    - [<static> JSONAnimationFrame](#static-jsonanimationframe)
  + [JSONAnimations](#jsonanimations)

    - [<static> JSONAnimations](#static-jsonanimations)
  + [PlayAnimationConfig](#playanimationconfig)

    - [<static> PlayAnimationConfig](#static-playanimationconfig)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Animations