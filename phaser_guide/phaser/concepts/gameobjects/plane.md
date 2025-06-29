# Plane

A Guide to the Phaser Plane Game Object

The Plane Game Object is a helper class that takes the Mesh Game Object and extends it, allowing for fast and easy creation of Planes. A Plane is a one-sided grid of cells, where you specify the number of cells in each dimension. The Plane can have a texture that is either repeated (tiled) across each cell, or applied to the full Plane.

The Plane can then be manipulated in 3D space, with rotation across all 3 axis.

This allows you to create effects not possible with regular Sprites, such as perspective distortion. You can also adjust the vertices on a per-vertex basis. Plane data becomes part of the WebGL batch, just like standard Sprites, so doesn't introduce any additional shader overhead. Because the Plane just generates vertices into the WebGL batch, like any other Sprite, you can use all of the common Game Object components on a Plane too, such as a custom pipeline, mask, blend mode or texture.

You can use the `uvScroll` and `uvScale` methods to adjust the placement and scaling of the texture if this Plane is using a single texture, and not a frame from a texture atlas or sprite sheet.

The Plane Game Object also has the Animation component, allowing you to play animations across the Plane just as you would with a Sprite. The animation frame size must be fixed as the first frame will be the size of the entire animation, for example use a `SpriteSheet`.

Note that the Plane object is WebGL only and does not have a Canvas counterpart.

The Plane origin is always 0.5 x 0.5 and *cannot be changed*.

## Load texture

```
Copythis.load.image(key, url);

```

Reference: [load image](../loader.md)

## Add plane object

```
Copyvar plane = this.add.plane(x, y, key);
// var plane = this.add.plane(x, y, key, frame);
// var plane = this.add.plane(x, y, texture, frame, width, height, tile);

```

* `x`, `y` : Position
* `key`, `frame` : Texture key of
* `width`, `height` : The width/height of this Plane, **in cells**, not pixels.
* `tile` : Is the texture tiled? I.e. repeated across each cell.

Add plane from JSON

```
Copyvar plane = this.make.plane({
    x: 0,
    y: 0,
    key: '',
    // frame: '',
    // width: 8,
    // height: 8,
    // tile: false,
    // checkerboard: null,
    // checkerboard: { color1, color2, alpha1, alpha2, height }

    // angle: 0,
    // alpha: 1,
    // scale : {
    //    x: 1,
    //    y: 1
    //},
    // origin: {x: 0.5, y: 0.5},

    add: true
});

```

## Custom class

* Define class

  ```
  Copyclass MyPlane extends Phaser.GameObjects.Plane {
      constructor(scene, x, y, texture, frame, width, height, tile) {
          super(scene, x, y, texture, frame, width, height, tile);
          // ...
          this.add.existing(this);
      }
      // ...

      // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar plane = new MyPlane(scene, x, y, texture, frame, width, height, tile);

  ```

## Texture

See [game object - texture](../gameobjects.md)

## Animation

See [Sprite's animation section](sprite.md).

### Play animation

* Play

  ```
  Copyplane.play(key);
  // plane.play(key, ignoreIfPlaying);

  ```

  + `key` : Animation key string, or animation config
    - String key of animation
    - Animation config, to override default config

      ```
      Copy{
          key,
          frameRate,
          duration,
          delay,
          repeat,
          repeatDelay,
          yoyo,
          showOnStart,
          hideOnComplete,
          startFrame,
          timeScale
      }

      ```
* Play in reverse

  ```
  Copyplane.playReverse(key);
  // plane.playReverse(key, ignoreIfPlaying);

  ```

  + `key` : Animation key string, or animation config
* Play after delay

  ```
  Copyplane.playAfterDelay(key, delay);

  ```

  + `key` : Animation key string, or animation config
* Play after repeat

  ```
  Copyplane.playAfterRepeat(key, repeatCount);

  ```

  + `key` : Animation key string, or animation config

### Stop

* Immediately stop

  ```
  Copyplane.stop();

  ```
* Stop after delay

  ```
  Copyplane.stopAfterDelay(delay);

  ```
* Stop at frame

  ```
  Copyplane.stopOnFrame(frame);

  ```

  + `frame` : Frame object in current animation.

    ```
    Copyvar currentAnim = plane.anims.currentAnim;
    var frame = currentAnim.getFrameAt(index);

    ```
* Stop after repeat

  ```
  Copyplane.stopAfterRepeat(repeatCount);

  ```

### Properties

* Has started

  ```
  Copyvar hasStarted = plane.anims.hasStarted;

  ```
* Is playing

  ```
  Copyvar isPlaying = plane.anims.isPlaying;

  ```
* Is paused

  ```
  Copyvar isPaused = plane.anims.isPaused;

  ```
* Total frames count

  ```
  Copyvar frameCount = plane.anims.getTotalFrames();

  ```
* Delay

  ```
  Copyvar delay = plane.anims.delay;

  ```
* Repeat

  + Total repeat count

    ```
    Copyvar repeatCount = plane.anims.repeat;

    ```
  + Repeat counter

    ```
    Copyvar repeatCount = plane.anims.repeatCounter;

    ```
  + Repeat delay

    ```
    Copyvar repeatDelay = plane.anims.repeatDelay;

    ```
  + Yoyo

    ```
    Copyvar repeatDelay = plane.anims.yoyo;

    ```
* Current animation key

  ```
  Copyvar key = plane.anims.getName();

  ```

  + `key` : Return `''` if not playing any animation.
* Current frame name

  ```
  Copyvar frameName = plane.anims.getFrameName();

  ```

  + `frameName` : Return `''` if not playing any animation.
* Current animation

  ```
  Copyvar currentAnim = plane.anims.currentAnim;

  ```
* Current frame

  ```
  Copyvar currentFrame = plane.anims.currentFrame;

  ```

## Interactive

To test if pointer is at any face of this mesh game object.

```
Copyplane.setInteractive();

```

## Checkerboard

Creates a checkerboard style texture,
based on the given colors and alpha values and applies it to this Plane,
replacing any current texture it may have.

* Create

  ```
  Copyplane.createCheckerboard(color1, color2, alpha1, alpha2, height)

  ```
* Remove

  ```
  Copyplane.removeCheckerboard();

  ```

## Other properties

See [Mesh game object](mesh.md), [game object](../gameobjects.md)

## Create mask

```
Copyvar mask = plane.createBitmapMask();

```

See [mask](../display.md)

## Shader effects

Support [postFX effects](shader.md)

!!! note
No preFX effect support

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Particles](particles.md)

[Render Texture](render-texture.md)

On this page

* [Plane](#plane)

  + [Load texture](#load-texture)
  + [Add plane object](#add-plane-object)
  + [Custom class](#custom-class)
  + [Texture](#texture)
  + [Animation](#animation)

    - [Play animation](#play-animation)
    - [Stop](#stop)
    - [Properties](#properties)
  + [Interactive](#interactive)
  + [Checkerboard](#checkerboard)
  + [Other properties](#other-properties)
  + [Create mask](#create-mask)
  + [Shader effects](#shader-effects)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../../index.md)