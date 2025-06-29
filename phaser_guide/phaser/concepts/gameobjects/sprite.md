# Sprite

A Guide to the Phaser Sprite Game Object

A Sprite Game Object is used for the display of both static and animated images in your game. Sprites can have input events and physics bodies. They can also be tweened, tinted, scrolled and animated.

The main difference between a Sprite and an Image Game Object is that you cannot animate Images. As such, Sprites take a fraction longer to process and have a larger API footprint due to the Animation Component. If you do not require animation then you can safely use Images to replace Sprites in all cases.

## Load texture

Texture for static image

```
Copythis.load.image(key, url);

```

Reference: [load image](../loader.md)

## Load atlas

Atlas for animation images

```
Copythis.load.atlas(key, textureURL, atlasURL);

```

Reference: [load atlas](../loader.md)

## Add sprite object

```
Copyvar sprite = this.add.sprite(x, y, key);
// var sprite = this.add.sprite(x, y, key, frame);

```

Add sprite from JSON

```
Copyvar sprite = this.make.sprite({
    x: 0,
    y: 0,
    key: '',
    // frame: '',

    // angle: 0,
    // alpha: 1
    // flipX: true,
    // flipY: true,
    // scale : {
    //    x: 1,
    //    y: 1
    //},

    // anims: {
        // key: ,
        // repeat: ,
        // ...
    // },
    // origin: {x: 0.5, y: 0.5},
    
    add: true
});

```

* `key` :
  + A string
  + An array of string to pick one element at random
* `x`, `y`, `scale.x`, `scale.y` :
  + A number
  + A callback to get return value

    ```
    Copyfunction() { return 0; }

    ```
  + Random integer between min and max

    ```
    Copy{ randInt: [min, max] }

    ```
  + Random float between min and max

    ```
    Copy{ randFloat: [min, max] }

    ```

## Custom class

* Define class

  ```
  Copyclass MySprite extends Phaser.GameObjects.Sprite {
      constructor(scene, x, y, texture, frame) {
          super(scene, x, y, texture, frame);
          // ...
          this.add.existing(this);
      }
      // ...

      // preUpdate(time, delta) {
      //     super.preUpdate(time, delta);
      // }
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar sprite = new MySprite(scene, x, y, key);

  ```

## Texture

See [game object - texture](../gameobjects.md)

## Other properties

See [game object](../gameobjects.md)

## Create mask

```
Copyvar mask = sprite.createBitmapMask();

```

See [mask](../display.md)

## Shader effects

Support [preFX and postFX effects](shader.md)

## Animation

### Create animation

* Global animation for all sprites

  ```
  Copythis.anims.create(config);

  ```
* Private animation for this sprite

  ```
  Copysprite.anims.create(config);

  ```

`config` : See [Add animation section](../animations.md).

### Create Aseprite animation

* Global Aseprite animation for all sprites

  ```
  Copythis.anims.createFromAseprite(key, tags);

  ```
* Private Aseprite animation for this sprite

  ```
  Copysprite.anims.createFromAseprite(key, tags);

  ```

#### Remove animation

* Remove from global animation manager

  ```
  Copythis.anims.remove(key);

  ```

  or

  ```
  Copysprite.anims.globalRemove(key);

  ```
* Remove from private animation state

  ```
  Copysprite.anims.remove(key);

  ```

#### Get animation

* Get global [animation object](../animations.md)

  ```
  Copyvar anim = this.anims.get(key);

  ```
* Get private [animation object](../animations.md)

  ```
  Copyvar anim = sprite.anims.get(key);

  ```

#### Has animation

* Has global animation object

  ```
  Copyvar hasAnim = this.anims.exists(key);

  ```
* Get private animation object

  ```
  Copyvar hasAnim = sprite.anims.exists(key);

  ```

### Play animation

* Play

  ```
  Copysprite.play(key);
  // sprite.play(key, ignoreIfPlaying);

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
  Copysprite.playReverse(key);
  // sprite.playReverse(key, ignoreIfPlaying);

  ```

  + `key` : Animation key string, or animation config
* Play after delay

  ```
  Copysprite.playAfterDelay(key, delay);

  ```

  + `key` : Animation key string, or animation config
* Play after repeat

  ```
  Copysprite.playAfterRepeat(key, repeatCount);

  ```

  + `key` : Animation key string, or animation config

### Chain

* Chain next animation

  ```
  Copysprite.chain(key);

  ```

  + `key` : Animation key string, or animation config
* Chain next and next animation

  ```
  Copysprite.chain(key0).chain(key1);

  ```

  + `key0`, `key1` : Animation key string, or animation config

### Stop

* Immediately stop

  ```
  Copysprite.stop();

  ```
* Stop after delay

  ```
  Copysprite.stopAfterDelay(delay);

  ```
* Stop at frame

  ```
  Copysprite.stopOnFrame(frame);

  ```

  + `frame` : Frame object in current animation.

    ```
    Copyvar currentAnim = sprite.anims.currentAnim;
    var frame = currentAnim.getFrameAt(index);

    ```
* Stop after repeat

  ```
  Copysprite.stopAfterRepeat(repeatCount);

  ```

### Restart

```
Copysprite.anims.restart();
// sprite.anims.restart(includeDelay, resetRepeats);

```

### Time scale

* Get

  ```
  Copyvar timeScale = sprite.anims.globalTimeScale;

  ```
* Set

  ```
  Copysprite.anims.globalTimeScale = timeScale;

  ```

See also [Global time scale](../animations.md)

### Properties

* Has started

  ```
  Copyvar hasStarted = sprite.anims.hasStarted;

  ```
* Is playing

  ```
  Copyvar isPlaying = sprite.anims.isPlaying;

  ```
* Is paused

  ```
  Copyvar isPaused = sprite.anims.isPaused;

  ```
* Total frames count

  ```
  Copyvar frameCount = sprite.anims.getTotalFrames();

  ```
* Delay

  ```
  Copyvar delay = sprite.anims.delay;

  ```
* Repeat

  + Total repeat count

    ```
    Copyvar repeatCount = sprite.anims.repeat;

    ```
  + Repeat counter

    ```
    Copyvar repeatCount = sprite.anims.repeatCounter;

    ```
  + Repeat delay

    ```
    Copyvar repeatDelay = sprite.anims.repeatDelay;

    ```
  + Yoyo

    ```
    Copyvar repeatDelay = sprite.anims.yoyo;

    ```
* Current animation key

  ```
  Copyvar key = sprite.anims.getName();

  ```

  + `key` : Return `''` if not playing any animation.
* Current frame name

  ```
  Copyvar frameName = sprite.anims.getFrameName();

  ```

  + `frameName` : Return `''` if not playing any animation.
* Current animation

  ```
  Copyvar currentAnim = sprite.anims.currentAnim;

  ```
* Current frame

  ```
  Copyvar currentFrame = sprite.anims.currentFrame;

  ```

### Events

* On start

  ```
  Copysprite.on('animationstart', function(currentAnim, currentFrame, sprite){});

  ```

  ```
  Copysprite.on('animationstart-' + key, function(currentAnim, currentFrame, sprite){});

  ```
* On restart

  ```
  Copysprite.on('animationrestart', function(currentAnim, currentFrame, sprite){});

  ```

  ```
  Copysprite.on('animationrestart-' + key, function(currentAnim, currentFrame, sprite){});

  ```
* On complete

  ```
  Copysprite.on('animationcomplete', function(currentAnim, currentFramee, sprite){});

  ```

  ```
  Copysprite.on('animationcomplete-' + key, function(currentAnim, currentFramee, sprite){});

  ```
* On stop

  ```
  Copysprite.on('animationstop', function(currentAnim, currentFrame, sprite){});

  ```

  ```
  Copysprite.on('animationstop-' + key, function(currentAnim, currentFrame, sprite){});

  ```
* On update

  ```
  Copysprite.on('animationupdate', function(currentAnim, currentFrame, sprite){});

  ```

  ```
  Copysprite.on('animationupdate-' + key, function(currentAnim, currentFrame, sprite){});

  ```
* On repeat

  ```
  Copysprite.on('animationrepeat', function(currentAnim, currentFrame, sprite){});

  ```

  ```
  Copysprite.on('animationrepeat-' + key, function(currentAnim, currentFrame, sprite){});

  ```

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Shader](shader.md)

[Text](text.md)

On this page

* [Sprite](#sprite)

  + [Load texture](#load-texture)
  + [Load atlas](#load-atlas)
  + [Add sprite object](#add-sprite-object)
  + [Custom class](#custom-class)
  + [Texture](#texture)
  + [Other properties](#other-properties)
  + [Create mask](#create-mask)
  + [Shader effects](#shader-effects)
  + [Animation](#animation)

    - [Create animation](#create-animation)
    - [Create Aseprite animation](#create-aseprite-animation)
    - [Play animation](#play-animation)
    - [Chain](#chain)
    - [Stop](#stop)
    - [Restart](#restart)
    - [Time scale](#time-scale)
    - [Properties](#properties)
    - [Events](#events)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../../index.md)