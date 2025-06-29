# Animations

Animations

The primary means of animation in Phaser is by using 'frame' based animations. As mentioned previously, Phaser maintains a Texture class, which contains as many Frames as may exist on that Texture. The Animation systen allows you to play a sequence of these Frames, one after the other, at a given frame rate. This is how you create the illusion of animation on Sprites in your game. To achieve this, you often see texture image files divided into a 'grid' of frames, where each frame is a different animation frame. This is known as a Sprite Sheet or Texture Atlas.

Animations are created via the Animation Manager. Each Scene has its own instance of the Animation Manager. You can create as many animations as you like, and each animation can have as many frames as you like. You can also create multiple animations that all use the same frames, if you wish. For example, you could have a 'walk' animation that uses frames 1 to 4, and a 'run' animation that uses frames 1 to 8. Both animations would use overlapping frames, but play them at different speeds.

Not all Game Objects can be animated. The main one you'll use is the Sprite Game Object. This carries its own Animation State component with it, allowing you to create and play animations directly on a Sprite instance.

Animations can be either global or local. A global animation is one that is created via the Animation Manager and is available to all Game Objects in your game. A local animation is one that is created directly on a Game Object, such as a Sprite. Local animations are only available to that Game Object and cannot be used by any other Game Object.

It's worth mentioning that animation can also be achieved by tweening objects, if you just need a blend of motion + subtle changes (like scale or alpha), and that Phaser 3 also has a plugin available for Spine animations, which is a bone-based animation software package published by Esoteric Software.

## Animation manager

### Add animation

```
Copyvar animationConfig = {
  key: "",

  frames: [],

  sortFrames: true,
  defaultTextureKey: null,
  skipMissedFrames: true,
  randomFrame: false,

  // time
  delay: 0,
  duration: null,
  frameRate: null,
  timeScale: 1,

  // repeat
  repeat: 0, // set to (-1) to repeat forever
  repeatDelay: 0,
  yoyo: false,

  // visible
  showBeforeDelay: false,
  showOnStart: false,
  hideOnComplete: false,
};

this.anims.create(animationConfig);

```

* `key` : Unique key of this animation data
* `frames` : An array of `{key, frame}`

  + Properties

    ```
    Copy{
        key: '',
        frame: '', // string, or number
        duration: 0
    }

    ```

    - `duration` : The duration, in ms, of this frame of the animation.
  + A string : Texture key.
  + Every frame in the atlas

    ```
    Copythis.anims.generateFrameNames(key);

    ```
  + Frame sequence indexing from start to end

    ```
    Copyvar config = ;
    this.anims.generateFrameNames(key,
    {
        prefix: '',
        start: 0,
        end: 0,
        suffix: '',
        zeroPad: 0,
        // outputArray: [], // Append frames into this array
    });

    ```

    - `prefix + Pad(i, zeroPad, '0', 1) + suffix`, i: start ~ end
  + Custom frame sequence

    ```
    Copyvar config = ;
    this.anims.generateFrameNames(key,
    {
        prefix: '',
        suffix: '',
        zeroPad: 0,
        frames: [ ... ]
        // outputArray: [], // Append frames into this array
    });

    ```

    - `prefix + Pad(frames[i], zeroPad, '0', 1) + suffix`
* `sortFrames` : Frame names numerically sorted. Default value is `true`.
* `defaultTextureKey` : The key of the texture all frames of the animation will use. Can be overridden on a per frame basis.
* `skipMissedFrames` : Skip frames if the time lags, or always advanced anyway? Default value is `true`.
* `randomFrame` : Start playback of this animation from a randomly selected frame? Default value is `false`.
* `delay` : Delay before starting playback. Value given in milliseconds.
* `duration` : How long the animation should play for in milliseconds. If not given its derived from `frameRate`.
* `frameRate` : The frame rate of playback in frames per second. Default value is `24`.
* `timeScale` : The time scale to be applied to playback of this animation. Default value is `1`.
* `repeat` : Number of times to repeat the animation. Default value is `0`.

  + `-1` : Infinity
* `repeatDelay` : Delay before the animation repeats. Value given in milliseconds.
* `yoyo` : Should the animation yoyo? (reverse back down to the start) before repeating? Default value is `false`.
* `showBeforeDelay` : If this animation has a delay, should it show the first frame immediately (`true`), or only after the delay (`false`)
* `showOnStart` : Should `sprite.visible = true` when the animation starts to play? This happens *after* any delay, if set. Default value is `false`.
* `hideOnComplete` : Should sprite.visible = false when the animation finishes? Default value is `false`.

#### Use every frame in a texture

```
Copy// Create animation 'mummyWalk' from every frame in texture 'mummy':
this.anims.create({
  key: "mummyWalk",
  frames: "mummy",
});

```

#### Choosing texture frames

You will usually need to know the texture frame names. To get the frame names:

```
Copyconsole.assert(this.texture.exists("mummy"));
console.log(this.textures.get("mummy").getFrameNames());

```

```
Copy// Create animation 'mummyWalk' from frames 0, 1, 2 of texture 'mummy':
this.anims.create({
  key: "mummyWalk",
  frames: [
    { key: "mummy", frame: 0 },
    { key: "mummy", frame: 1 },
    { key: "mummy", frame: 2 },
  ],
});

```

You can of course create animations using any technique.

```
Copy// We have 3 textures with identical frame patterns.
const textureKeys = ["giant", "elf", "goblin"];

// We will create 9 animations from 3 sequences.
const anims = {
  idle: [0],
  walk: [1, 2],
  attack: [3, 4],
};

for (const textureKey of textureKeys) {
  for (const animName of anims) {
    this.anims.create({
      // 'giant:idle', 'giant:walk', etc.
      key: `${textureKey}:${animName}`,
      frames: anims[animName],
    });
  }
}

```

#### Frame timing

You can give either `frameRate` (default 24 fps) or a `duration` for the whole animation. The frame duration is calculated as `1000 / frameRate` or `duration / frames.length`.

If you set per-frame durations, these are **added** to the calculated frame durations. So if you want to set only frame durations, use an animation duration of 1ms.

```
Copythis.anims.create({
  key: "spikes",
  repeat: -1,
  defaultTextureKey: "spikes",
  duration: 1, // 1 ms, close enough to 0
  frames: [
    { frame: 0, duration: 3000 },
    { frame: 1, duration: 250 },
    { frame: 2, duration: 250 },
    { frame: 3, duration: 3000 },
    { frame: 2, duration: 250 },
    { frame: 1, duration: 250 },
  ],
});

```

#### generateFrameNumbers() and generateFrameNames()

The helper methods [generateFrameNumbers()](../../docs/latest/Phaser.Animations.AnimationManager-generateFrameNumbers.md) and [generateFrameNames()](../../docs/latest/Phaser.Animations.AnimationManager-generateFrameNames.md) both **select** frame names from a texture according to a pattern and then **generate** an array of [AnimationFrame](../../docs/latest/Phaser.Types.Animations.AnimationFrame.md) objects that can be passed as the `frames` property. `generateFrameNumbers()` selects spritesheet-style frame names (indexes) and `generateFrameNames()` selects atlas-style frame names. They never select frame names that don't exist in the texture.

For example,

```
Copythis.anims.generateFrameNumbers("mummy", { frames: [0, 1, 2] });

```

or

```
Copythis.anims.generateFrameNumbers("mummy", { start: 0, end: 2 });

```

would produce an array of the 3 frame configs that we wrote above.

The `generateFrameNames()` config has all the options of `generateFrameNumbers()`, plus `prefix`, `suffix`, and `zeroPad`.

Log the output of these methods if you run into trouble.

#### Add from Aseprite

[Aseprite](https://www.aseprite.org/) is a powerful animation sprite editor and pixel art tool. Create one, or more animations from a loaded Aseprite JSON file.

```
Copythis.anims.createFromAseprite(key);
// this.anims.createFromAseprite(key, tags, target);

```

* `key` : The key of the loaded Aseprite atlas.
* `tags` :
  + `undefined` : Load all tags.
  + Array of string tag : Load these tags.
* `target` : Create the animations on this target Sprite.
  + `undefined` : Created globally in this Animation Manager. Default behavior.

### Remove animation

```
Copythis.anims.remove(key);

```

### Mixing and delaying between two animations

* Add

  ```
  Copythis.anims.addMix(animA, animB, delay);

  ```

  + `animA`, `animB` : String key of an animation, or an instance of animation.
* Remove

  ```
  Copythis.anims.removeMix(animA, animB);
  // this.anims.removeMix(animA);

  ```
* Get

  ```
  Copyvar delay = this.anims.getMix(animA, animB);

  ```
* Example of an animation mix for transitioning from one animation to another.

  ```
  Copythis.anims.create({ key: "animA" /* etc. */ });
  this.anims.create({ key: "animB" /* etc. */ });

  this.anims.addMix("animA", "animB", 200);

  ```

  The delay is applied automatically if you play the second animation while the first is playing.

  ```
  Copysprite.play("animA");
  // Later:
  sprite.play("animB");

  ```

  It's very similar to

  ```
  Copyif (sprite.anims.isPlaying && sprite.anims.getName() === "animA") {
    sprite.anims.playAfterDelay("animB", 200);
  }

  ```

### Play animation

* Play

  ```
  Copythis.anims.play(key, children);

  ```
* Stagger play (delay play)

  ```
  Copythis.anims.staggerPlay(key, children, stagger, staggerFirst);

  ```

  + `children` : An array of Game Objects to play the animation on
  + `stagger` : The amount of time, in milliseconds, to offset each play time by
  + `staggerFirst` : Set `true` to apply delay on 1st child
* Playing an animation when an event is triggered

  ```
  Copysprite.on(event, function () {
    sprite.play(key);
  }


  ```

  Example:

  ```
  Copysprite.on('pointerdown', function () {
    sprite.play('smile');
  }

  ```
* Ignore playing an animation if it is already playing

  ```
  Copysprite.play(key, ignoreIfPlaying);

  ```

  + `ignoreIfPlaying` : Set to `true` to ignore restarting an animation.

  Example:

  ```
  Copysprite.play("run", true); // only plays the "run" animation if it is not already playing

  ```
* Chaining animation

`chain()` schedules an animation to play once the current one **completes** or **stops**. Repeated chaining adds to the **end** of the queue. If an animation is repeating, only `stop()` will advance the queue. If you want a final stop, do

```
Copysprite.chain().stop();

```

Be careful of chaining too many animations by mistake.

```
Copyfunction update() {
  // Choose a reasonable maximum.
  if (sprite.anims.nextAnimsQueue.length > 10) {
    throw new Error("Too many chained animations");
  }
}

```

Internally, the next chained animation is in `nextAnim` and any additional ones are in `nextAnimsQueue`.

* Play animation after delay or repeat count

  + `playAfterDelay()`

    ```
    Copysprite.playAfterDelay(key, delay);

    ```

    - `key` : The string-based key of the animation to play.
    - `delay` : The delay, in milliseconds, to wait before playing the animation.
  + `playAfterRepeat()`

    ```
    Copysprite.playAfterRepeat(key, repeatCount);

    ```

    - `key` : The string-based key of the animation to play.
    - `repeatCount` : Optional argument that defaults to 1. Number of current animation repeats before next animation plays.

### Pause all animations

```
Copythis.anims.pauseAll();

```

### Resume all animations

```
Copythis.anims.resumeAll();

```

### Global time scale

The global time scale of the Animation Manager. This scales the time delta between two frames, thus influencing the speed of time for the Animation Manager.

* Get

  ```
  Copyvar timeScale = this.anims.globalTimeScale;

  ```
* Set

  ```
  Copythis.anims.globalTimeScale = timeScale;

  ```

### Has animation

```
Copyvar hasAnim = this.anims.exists(key);

```

### Export/load

* Export JSON

  ```
  Copyvar json = this.anims.toJSON();

  ```
* Load from JSON

  ```
  Copythis.anims.fromJSON(json);
  // this.anims.fromJSON(json, clearCurrentAnimations);

  ```

  + Load JSON in preload stage

    ```
    Copyscene.load.json(key, url);

    ```
  + Load animation in preload stage

    ```
    Copyscene.load.animation(key, url);

    ```

### Events

* On add animation

  ```
  Copythis.anims.on("add", function (key, anim) {});

  ```
* On remove animation

  ```
  Copythis.anims.on("remove", function (key, anim) {});

  ```
* On pause all animations

  ```
  Copythis.anims.on("pauseall", function () {});

  ```
* On resume all animations

  ```
  Copythis.anims.on("resumeall", function () {});

  ```

## Animation object

```
Copyvar anim = this.anims.get(key);

```

Example:

```
Copyconst mummyWalkAnim = this.anims.get("mummyWalk");

```

### Add frame

* Append frames

  ```
  Copyanim.addFrame(frame);

  ```

  + `frame` : `this.anims.generateFrameNames(key, config)`
* Insert frames at index

  ```
  Copyanim.addFrameAt(index, frame);

  ```

  + `frame` : `this.anims.generateFrameNames(key, config)`

### Remove frame

* Remove frame at

  ```
  Copyanim.removeFrameAt(index);

  ```
* Remove frame

  ```
  Copyanim.removeFrame(frame);

  ```

### Get frame

* Has frame index

  ```
  Copyvar HasFrameAt = anim.checkFrame(index);

  ```
* Get frame at index

  ```
  Copyvar frame = anim.getFrameAt(index);

  ```

  Example:

  ```
  Copyconst mummyWalkFrame1 = this.anims.get("mummyWalk").getFrameAt(1);

  ```
* Get last frame

  ```
  Copyvar frame = anim.getLastFrame();

  ```

### Export

* Export JSON

  ```
  Copyvar json = anim.toJSON();

  ```

  or

  ```
  Copyvar jsonString = JSON.stringify(anim);

  ```

## Common errors

> TypeError: undefined is not an object (evaluating 'animationFrame.frame.texture')

in [setCurrentFrame()](../../docs/latest/Phaser.Animations.AnimationState-setCurrentFrame.md). Usually you created an animation with a bad texture key.

> TypeError: undefined is not an object (evaluating 'state.currentFrame.duration')

in [getFirstTick()](../../docs/latest/Phaser.Animations.Animation-getFirstTick.md). You're playing an empty animation (no frames), or you're playing a `startFrame` that's out of range. If the animation has no frames, this is usually because `generateFrameNames()` or `generateFrameNumbers()` couldn't select any; look for preceding warnings in the console.

> TypeError: undefined is not an object (evaluating 'this.anims.play')

You're playing on a destroyed Sprite or a non-Sprite game object (lacking `anims`).

> TypeError: sprite.play is not a function

You're playing on a non-Sprite game object.

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)
* [samme](https://github.com/samme)

Updated on June 4, 2025, 1:16 PM UTC

---

[Actions](actions.md)

[Audio](audio.md)

On this page

* [Animations](#animations)

  + [Animation manager](#animation-manager)

    - [Add animation](#add-animation)
    - [Remove animation](#remove-animation)
    - [Mixing and delaying between two animations](#mixing-and-delaying-between-two-animations)
    - [Play animation](#play-animation)
    - [Pause all animations](#pause-all-animations)
    - [Resume all animations](#resume-all-animations)
    - [Global time scale](#global-time-scale)
    - [Has animation](#has-animation)
    - [Export/load](#exportload)
    - [Events](#events)
  + [Animation object](#animation-object)

    - [Add frame](#add-frame)
    - [Remove frame](#remove-frame)
    - [Get frame](#get-frame)
    - [Export](#export)
  + [Common errors](#common-errors)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../index.md)



Animations