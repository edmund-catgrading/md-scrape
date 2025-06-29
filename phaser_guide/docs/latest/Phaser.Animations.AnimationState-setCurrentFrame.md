AnimationState

[![Phaser](/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1729268756946%2Fc586ecd3-3d9b-4945-a751-7ebb30337dca.png%3Fw%3D500%26h%3D125%26auto%3Dcompress%2Cformat%26format%3Dwebp&w=3840&q=75)](../../index.md)

Search

`⌘K`

Ask AI

Search

`⌘K`

Ask AI

38.1k stars

Phaser

API Documentation

Phaser Editor

Examples

Game of the Week

* [Phaser](../../index.md)
* [API Documentation](/api-documentation/api-documentation)
* [Phaser Editor](/phaser-editor/intro/welcome)
* [Examples](https://phaser.io/examples)
* [Game of the Week](https://phaser.io/news/2025/01/the-wildfires)

Collapse

Phaser API Documentation

* [Phaser 3.87.0 API Documentation](/api-documentation/api-documentation)
* [Namespaces](/api-documentation/namespace)
* [Game Objects](/api-documentation/gameobjects)
* [Physics](/api-documentation/physics)
* [Events](/api-documentation/event)
* [Class](/api-documentation/class)
* [Functions](/api-documentation/function)
* [Constants](/api-documentation/constant)
* [Typedefs](/api-documentation/typedef)

Collapse

`⌘\`

# AnimationState

Phaser.Animations.AnimationState

The Animation State Component.

This component provides features to apply animations to Game Objects. It is responsible for

loading, queuing animations for later playback, mixing between animations and setting

the current animation frame to the Game Object that owns this component.

This component lives as an instance within any Game Object that has it defined, such as Sprites.

You can access its properties and methods via the `anims` property, i.e. `Sprite.anims`.

As well as playing animations stored in the global Animation Manager, this component

can also create animations that are stored locally within it. See the `create` method

for more details.

Prior to Phaser 3.50 this component was called just `Animation` and lived in the

`Phaser.GameObjects.Components` namespace. It was renamed to `AnimationState`

in 3.50 to help better identify its true purpose when browsing the documentation.

**Constructor**

`new AnimationState(parent)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| parent | [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) | No | The Game Object to which this animation component belongs. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/animations/AnimationState.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L14)  
> Since: 3.0.0

# Public Members

## accumulator

### accumulator: number

**Description:**

Internal time overflow accumulator.

This has the `delta` time added to it as part of the `update` step.

> Source: [src/animations/AnimationState.js#L376](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L376)  
> Since: 3.0.0

---

## animationManager

### animationManager: [Phaser.Animations.AnimationManager](/api-documentation/class/animations-animationmanager)

**Description:**

A reference to the global Animation Manager.

> Source: [src/animations/AnimationState.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L59)  
> Since: 3.0.0

---

## anims

### anims: Phaser.Structs.Map.<string, [Phaser.Animations.Animation](/api-documentation/class/animations-animation)>

**Description:**

The Animations stored locally in this Animation component.

Do not modify the contents of this Map directly, instead use the

`add`, `create` and `remove` methods of this class instead.

**Access:** protected

> Source: [src/animations/AnimationState.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L80)  
> Since: 3.50.0

---

## currentAnim

### currentAnim: [Phaser.Animations.Animation](/api-documentation/class/animations-animation)

**Description:**

The current Animation loaded into this Animation component.

Will by `null` if no animation is yet loaded.

> Source: [src/animations/AnimationState.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L113)  
> Since: 3.0.0

---

## currentFrame

### currentFrame: [Phaser.Animations.AnimationFrame](/api-documentation/class/animations-animationframe)

**Description:**

The current AnimationFrame being displayed by this Animation component.

Will by `null` if no animation is yet loaded.

> Source: [src/animations/AnimationState.js#L125](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L125)  
> Since: 3.0.0

---

## delay

### delay: number

**Description:**

The delay before starting playback of the current animation, in milliseconds.

This value is set when a new animation is loaded into this component and should

be treated as read-only, as changing it once playback has started will not alter

the animation. To change the delay, provide a new value in the `PlayAnimationConfig` object.

Prior to Phaser 3.50 this property was private and called `_delay`.

> Source: [src/animations/AnimationState.js#L241](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L241)  
> Since: 3.50.0

---

## delayCounter

### delayCounter: number

**Description:**

A counter keeping track of how much delay time, in milliseconds, is left before playback begins.

This is set via the `playAfterDelay` method, although it can be modified at run-time

if required, as long as the animation has not already started playing.

> Source: [src/animations/AnimationState.js#L400](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L400)  
> Since: 3.50.0

---

## duration

### duration: number

**Description:**

The duration of the current animation, in milliseconds.

This value is set when a new animation is loaded into this component and should

be treated as read-only, as changing it once playback has started will not alter

the animation. To change the duration, provide a new value in the `PlayAnimationConfig` object.

> Source: [src/animations/AnimationState.js#L193](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L193)  
> Since: 3.0.0

---

## forward

### forward: boolean

**Description:**

Is the playhead moving forwards (`true`) or in reverse (`false`) ?

> Source: [src/animations/AnimationState.js#L352](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L352)  
> Since: 3.0.0

---

## frameRate

### frameRate: number

**Description:**

The frame rate of playback, of the current animation, in frames per second.

This value is set when a new animation is loaded into this component and should

be treated as read-only, as changing it once playback has started will not alter

the animation. To change the frame rate, provide a new value in the `PlayAnimationConfig` object.

> Source: [src/animations/AnimationState.js#L179](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L179)  
> Since: 3.0.0

---

## hasStarted

### hasStarted: boolean

**Description:**

Has the current animation started playing, or is it waiting for a delay to expire?

> Source: [src/animations/AnimationState.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L103)  
> Since: 3.50.0

---

## hideOnComplete

### hideOnComplete: boolean

**Description:**

Should the GameObject's `visible` property be set to `false` when the animation completes?

This value is set when a new animation is loaded into this component, but can also be modified

at run-time, assuming the animation is still actively playing.

> Source: [src/animations/AnimationState.js#L340](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L340)  
> Since: 3.50.0

---

## inReverse

### inReverse: boolean

**Description:**

An internal trigger that tells the component if it should plays the animation

in reverse mode ('true') or not ('false'). This is used because `forward` can

be changed by the `yoyo` feature.

Prior to Phaser 3.50 this property was private and called `_reverse`.

> Source: [src/animations/AnimationState.js#L362](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L362)  
> Since: 3.50.0

---

## isPaused

### isPaused: boolean

**Description:**

`true` if the current animation is paused, otherwise `false`.

> Source: [src/animations/AnimationState.js#L1988](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1988)  
> Since: 3.4.0

---

## isPlaying

### isPlaying: boolean

**Description:**

Is an animation currently playing or not?

> Source: [src/animations/AnimationState.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L93)  
> Since: 3.0.0

---

## msPerFrame

### msPerFrame: number

**Description:**

The number of milliseconds per frame, not including frame specific modifiers that may be present in the

Animation data.

This value is calculated when a new animation is loaded into this component and should

be treated as read-only. Changing it will not alter playback speed.

> Source: [src/animations/AnimationState.js#L207](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L207)  
> Since: 3.0.0

---

## nextAnim

### nextAnim: string, [Phaser.Animations.Animation](/api-documentation/class/animations-animation), [Phaser.Types.Animations.PlayAnimationConfig](/api-documentation/typedef/types-animations#playanimationconfig)

**Description:**

The key, instance, or config of the next Animation to be loaded into this Animation component

when the current animation completes.

Will by `null` if no animation has been queued.

> Source: [src/animations/AnimationState.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L137)  
> Since: 3.16.0

---

## nextAnimsQueue

### nextAnimsQueue: array

**Description:**

A queue of Animations to be loaded into this Animation component when the current animation completes.

Populate this queue via the `chain` method.

> Source: [src/animations/AnimationState.js#L150](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L150)  
> Since: 3.24.0

---

## nextTick

### nextTick: number

**Description:**

The time point at which the next animation frame will change.

This value is compared against the `accumulator` as part of the `update` step.

> Source: [src/animations/AnimationState.js#L388](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L388)  
> Since: 3.0.0

---

## parent

### parent: [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject)

**Description:**

The Game Object to which this animation component belongs.

You can typically access this component from the Game Object

via the `this.anims` property.

> Source: [src/animations/AnimationState.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L47)  
> Since: 3.0.0

---

## pendingRepeat

### pendingRepeat: boolean

**Description:**

An internal flag keeping track of pending repeats.

> Source: [src/animations/AnimationState.js#L426](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L426)  
> Since: 3.0.0

---

## randomFrame

### randomFrame: boolean

**Description:**

Start playback of this animation from a random frame?

> Source: [src/animations/AnimationState.js#L231](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L231)  
> Since: 3.60.0

---

## repeat

### repeat: number

**Description:**

The number of times to repeat playback of the current animation.

If -1, it means the animation will repeat forever.

This value is set when a new animation is loaded into this component and should

be treated as read-only, as changing it once playback has started will not alter

the animation. To change the number of repeats, provide a new value in the `PlayAnimationConfig` object.

Prior to Phaser 3.50 this property was private and called `_repeat`.

> Source: [src/animations/AnimationState.js#L257](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L257)  
> Since: 3.50.0

---

## repeatCounter

### repeatCounter: number

**Description:**

A counter that keeps track of how many repeats are left to run.

This value is set when a new animation is loaded into this component, but can also be modified

at run-time.

> Source: [src/animations/AnimationState.js#L413](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L413)  
> Since: 3.0.0

---

## repeatDelay

### repeatDelay: number

**Description:**

The number of milliseconds to wait before starting the repeat playback of the current animation.

This value is set when a new animation is loaded into this component, but can also be modified

at run-time.

You can change the repeat delay by providing a new value in the `PlayAnimationConfig` object.

Prior to Phaser 3.50 this property was private and called `_repeatDelay`.

> Source: [src/animations/AnimationState.js#L275](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L275)  
> Since: 3.0.0

---

## showBeforeDelay

### showBeforeDelay: boolean

**Description:**

If the animation has a delay set, before playback will begin, this

controls when the first frame is set on the Sprite. If this property

is 'false' then the frame is set only after the delay has expired.

This is the default behavior.

If this property is 'true' then the first frame of this animation

is set immediately, and then when the delay expires, playback starts.

> Source: [src/animations/AnimationState.js#L311](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L311)  
> Since: 3.60.0

---

## showOnStart

### showOnStart: boolean

**Description:**

Should the GameObject's `visible` property be set to `true` when the animation starts to play?

This will happen *after* any delay that may have been set.

This value is set when a new animation is loaded into this component, but can also be modified

at run-time, assuming the animation is currently delayed.

> Source: [src/animations/AnimationState.js#L326](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L326)  
> Since: 3.50.0

---

## skipMissedFrames

### skipMissedFrames: boolean

**Description:**

Skip frames if the time lags, or always advanced anyway?

> Source: [src/animations/AnimationState.js#L221](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L221)  
> Since: 3.0.0

---

## textureManager

### textureManager: [Phaser.Textures.TextureManager](/api-documentation/class/textures-texturemanager)

**Description:**

A reference to the Texture Manager.

**Access:** protected

> Source: [src/animations/AnimationState.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L70)  
> Since: 3.50.0

---

## timeScale

### timeScale: number

**Description:**

The Time Scale factor.

You can adjust this value to modify the passage of time for the animation that is currently

playing. For example, setting it to 2 will make the animation play twice as fast. Or setting

it to 0.5 will slow the animation down.

You can change this value at run-time, or set it via the `PlayAnimationConfig`.

Prior to Phaser 3.50 this property was private and called `_timeScale`.

> Source: [src/animations/AnimationState.js#L161](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L161)  
> Since: 3.50.0

---

## yoyo

### yoyo: boolean

**Description:**

Should the current animation yoyo? An animation that yoyos will play in reverse, from the end

to the start, before then repeating or completing. An animation that does not yoyo will just

play from the start to the end.

This value is set when a new animation is loaded into this component, but can also be modified

at run-time.

You can change the yoyo by providing a new value in the `PlayAnimationConfig` object.

Prior to Phaser 3.50 this property was private and called `_yoyo`.

> Source: [src/animations/AnimationState.js#L292](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L292)  
> Since: 3.50.0

---

# Private Members

## \_paused

### \_paused: boolean

**Description:**

Is the Animation paused?

**Access:** private

> Source: [src/animations/AnimationState.js#L436](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L436)  
> Since: 3.0.0

---

## \_pendingStop

### \_pendingStop: number

**Description:**

Internal property tracking if this Animation is waiting to stop.

0 = No

1 = Waiting for ms to pass

2 = Waiting for repeat

3 = Waiting for specific frame

**Access:** private

> Source: [src/animations/AnimationState.js#L458](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L458)  
> Since: 3.4.0

---

## \_pendingStopValue

### \_pendingStopValue: any

**Description:**

Internal property used by \_pendingStop.

**Access:** private

> Source: [src/animations/AnimationState.js#L473](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L473)  
> Since: 3.4.0

---

## \_wasPlaying

### \_wasPlaying: boolean

**Description:**

Was the animation previously playing before being paused?

**Access:** private

> Source: [src/animations/AnimationState.js#L447](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L447)  
> Since: 3.0.0

---

# Public Methods

## chain

### <instance> chain([key])

**Description:**

Sets an animation, or an array of animations, to be played in the future, after the current one completes or stops.

The current animation must enter a 'completed' state for this to happen, i.e. finish all of its repeats, delays, etc,

or have one of the `stop` methods called.

An animation set to repeat forever will never enter a completed state unless stopped.

You can chain a new animation at any point, including before the current one starts playing, during it, or when it ends (via its `animationcomplete` event).

Chained animations are specific to a Game Object, meaning different Game Objects can have different chained animations without impacting the global animation they're playing.

Call this method with no arguments to reset all currently chained animations.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Animations.Animation](/api-documentation/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api-documentation/typedef/types-animations#playanimationconfig) | Array.<string> |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

> Source: [src/animations/AnimationState.js#L484](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L484)  
> Since: 3.16.0

---

## complete

### <instance> complete()

**Description:**

The current animation has completed. This dispatches the `ANIMATION_COMPLETE` event.

This method is called by the Animation instance and should not usually be invoked directly.

If no animation is loaded, no events will be dispatched.

If another animation has been queued for playback, it will be started after the events fire.

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_COMPLETE](/api-documentation/event/animations-events#animation_complete)

> Source: [src/animations/AnimationState.js#L1309](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1309)  
> Since: 3.50.0

---

## create

### <instance> create(config)

**Description:**

Creates a new Animation that is local specifically to this Sprite.

When a Sprite owns an animation, it is kept out of the global Animation Manager, which means

you're free to use keys that may be already defined there. Unless you specifically need a Sprite

to have a unique animation, you should favor using global animations instead, as they allow for

the same animation to be used across multiple Sprites, saving on memory. However, if this Sprite

is the only one to use this animation, it's sensible to create it here.

If an invalid key is given this method will return `false`.

If you pass the key of an animation that already exists locally, that animation will be returned.

A brand new animation is only created if the key is valid and not already in use by this Sprite.

If you wish to re-use an existing key, call the `remove` method first, then this method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Animations.Animation](/api-documentation/typedef/types-animations#animation) | No | The configuration settings for the Animation. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Animations.Animation](/api-documentation/class/animations-animation), false - The Animation that was created, or `false` if the key is already in use.

> Source: [src/animations/AnimationState.js#L1699](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1699)  
> Since: 3.50.0

---

## createFromAseprite

### <instance> createFromAseprite(key, [tags])

**Description:**

Create one, or more animations from a loaded Aseprite JSON file.

Aseprite is a powerful animated sprite editor and pixel art tool.

You can find more details at <https://www.aseprite.org/>

To export a compatible JSON file in Aseprite, please do the following:

1. Go to "File - Export Sprite Sheet"
2. On the **Layout** tab:

2a. Set the "Sheet type" to "Packed"

2b. Set the "Constraints" to "None"

2c. Check the "Merge Duplicates" checkbox

3. On the **Sprite** tab:

3a. Set "Layers" to "Visible layers"

3b. Set "Frames" to "All frames", unless you only wish to export a sub-set of tags

4. On the **Borders** tab:

4a. Check the "Trim Sprite" and "Trim Cells" options

4b. Ensure "Border Padding", "Spacing" and "Inner Padding" are all > 0 (1 is usually enough)

5. On the **Output** tab:

5a. Check "Output File", give your image a name and make sure you choose "png files" as the file type

5b. Check "JSON Data" and give your json file a name

5c. The JSON Data type can be either a Hash or Array, Phaser doesn't mind.

5d. Make sure "Tags" is checked in the Meta options

5e. In the "Item Filename" input box, make sure it says just "{frame}" and nothing more.

6. Click export

This was tested with Aseprite 1.2.25.

This will export a png and json file which you can load using the Aseprite Loader, i.e.:

```
Copy
function preload ()

{

    this.load.path = 'assets/animations/aseprite/';

    this.load.aseprite('paladin', 'paladin.png', 'paladin.json');

}


```

Once loaded, you can call this method on a Sprite with the 'atlas' key:

```
Copy
const sprite = this.add.sprite(400, 300);



sprite.anims.createFromAseprite('paladin');


```

Any animations defined in the JSON will now be available to use on this Sprite and you play them

via their Tag name. For example, if you have an animation called 'War Cry' on your Aseprite timeline,

you can play it on the Sprite using that Tag name:

```
Copy
const sprite = this.add.sprite(400, 300);



sprite.anims.createFromAseprite('paladin');



sprite.play('War Cry');


```

When calling this method you can optionally provide an array of tag names, and only those animations

will be created. For example:

```
Copy
sprite.anims.createFromAseprite('paladin', [ 'step', 'War Cry', 'Magnum Break' ]);


```

This will only create the 3 animations defined. Note that the tag names are case-sensitive.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the loaded Aseprite atlas. It must have been loaded prior to calling this method. |
| --- | --- | --- | --- |
| tags | Array.<string> | Yes | An array of Tag names. If provided, only animations found in this array will be created. |

**Returns:** Array.<[Phaser.Animations.Animation](/api-documentation/class/animations-animation)> - An array of Animation instances that were successfully created.

> Source: [src/animations/AnimationState.js#L1753](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1753)  
> Since: 3.60.0

---

## destroy

### <instance> destroy()

**Description:**

Destroy this Animation component.

Unregisters event listeners and cleans up its references.

> Source: [src/animations/AnimationState.js#L1962](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1962)  
> Since: 3.0.0

---

## exists

### <instance> exists(key)

**Description:**

Checks to see if the given key is already used locally within the animations stored on this Sprite.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the Animation to check. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the Animation exists locally, or `false` if the key is available, or there are no local animations.

> Source: [src/animations/AnimationState.js#L1684](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1684)  
> Since: 3.50.0

---

## generateFrameNames

### <instance> generateFrameNames(key, [config])

**Description:**

Generate an array of [Phaser.Types.Animations.AnimationFrame](/api-documentation/typedef/types-animations#animationframe) objects from a texture key and configuration object.

Generates objects with string based frame names, as configured by the given [Phaser.Types.Animations.GenerateFrameNames](/api-documentation/typedef/types-animations#generateframenames).

It's a helper method, designed to make it easier for you to extract all of the frame names from texture atlases.

If you're working with a sprite sheet, see the `generateFrameNumbers` method instead.

Example:

If you have a texture atlases loaded called `gems` and it contains 6 frames called `ruby_0001`, `ruby_0002`, and so on,

then you can call this method using: `this.anims.generateFrameNames('gems', { prefix: 'ruby_', end: 6, zeroPad: 4 })`.

The `end` value tells it to look for 6 frames, incrementally numbered, all starting with the prefix `ruby_`. The `zeroPad`

value tells it how many zeroes pad out the numbers. To create an animation using this method, you can do:

```
Copy
this.anims.create({

  key: 'ruby',

  repeat: -1,

  frames: this.anims.generateFrameNames('gems', {

    prefix: 'ruby_',

    end: 6,

    zeroPad: 4

  })

});


```

Please see the animation examples for further details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key for the texture containing the animation frames. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Animations.GenerateFrameNames](/api-documentation/typedef/types-animations#generateframenames) | Yes | The configuration object for the animation frame names. |

**Returns:** Array.<[Phaser.Types.Animations.AnimationFrame](/api-documentation/typedef/types-animations#animationframe)> - The array of {@link Phaser.Types.Animations.AnimationFrame} objects.

> Source: [src/animations/AnimationState.js#L1840](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1840)  
> Since: 3.50.0

---

## generateFrameNumbers

### <instance> generateFrameNumbers(key, [config])

**Description:**

Generate an array of [Phaser.Types.Animations.AnimationFrame](/api-documentation/typedef/types-animations#animationframe) objects from a texture key and configuration object.

Generates objects with numbered frame names, as configured by the given [Phaser.Types.Animations.GenerateFrameNumbers](/api-documentation/typedef/types-animations#generateframenumbers).

If you're working with a texture atlas, see the `generateFrameNames` method instead.

It's a helper method, designed to make it easier for you to extract frames from sprite sheets.

If you're working with a texture atlas, see the `generateFrameNames` method instead.

Example:

If you have a sprite sheet loaded called `explosion` and it contains 12 frames, then you can call this method using:

`this.anims.generateFrameNumbers('explosion', { start: 0, end: 11 })`.

The `end` value tells it to stop after 12 frames. To create an animation using this method, you can do:

```
Copy
this.anims.create({

  key: 'boom',

  frames: this.anims.generateFrameNumbers('explosion', {

    start: 0,

    end: 11

  })

});


```

Note that `start` is optional and you don't need to include it if the animation starts from frame 0.

To specify an animation in reverse, swap the `start` and `end` values.

If the frames are not sequential, you may pass an array of frame numbers instead, for example:

`this.anims.generateFrameNumbers('explosion', { frames: [ 0, 1, 2, 1, 2, 3, 4, 0, 1, 2 ] })`

Please see the animation examples and `GenerateFrameNumbers` config docs for further details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key for the texture containing the animation frames. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Animations.GenerateFrameNumbers](/api-documentation/typedef/types-animations#generateframenumbers) | Yes | The configuration object for the animation frames. |

**Returns:** Array.<[Phaser.Types.Animations.AnimationFrame](/api-documentation/typedef/types-animations#animationframe)> - The array of {@link Phaser.Types.Animations.AnimationFrame} objects.

> Source: [src/animations/AnimationState.js#L1883](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1883)  
> Since: 3.50.0

---

## get

### <instance> get(key)

**Description:**

Get an Animation instance that has been created locally on this Sprite.

See the `create` method for more details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the Animation to retrieve. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Animations.Animation](/api-documentation/class/animations-animation) - The Animation, or `null` if the key is invalid.

> Source: [src/animations/AnimationState.js#L1667](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1667)  
> Since: 3.50.0

---

## getFrameName

### <instance> getFrameName()

**Description:**

Returns the key of the animation frame currently displayed by this component.

**Returns:** string - The key of the Animation Frame currently displayed by this component, or an empty string if no animation has been loaded.

> Source: [src/animations/AnimationState.js#L554](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L554)  
> Since: 3.50.0

---

## getName

### <instance> getName()

**Description:**

Returns the key of the animation currently loaded into this component.

Prior to Phaser 3.50 this method was called `getCurrentKey`.

**Returns:** string - The key of the Animation currently loaded into this component, or an empty string if none loaded.

> Source: [src/animations/AnimationState.js#L539](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L539)  
> Since: 3.50.0

---

## getProgress

### <instance> getProgress()

**Description:**

Returns a value between 0 and 1 indicating how far this animation is through, ignoring repeats and yoyos.

The value is based on the current frame and how far that is in the animation, it is not based on

the duration of the animation.

**Returns:** number - The progress of the current animation in frames, between 0 and 1.

> Source: [src/animations/AnimationState.js#L1150](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1150)  
> Since: 3.4.0

---

## getTotalFrames

### <instance> getTotalFrames()

**Description:**

Returns the total number of frames in this animation, or returns zero if no

animation has been loaded.

**Returns:** number - The total number of frames in the current animation, or zero if no animation has been loaded.

> Source: [src/animations/AnimationState.js#L1473](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1473)  
> Since: 3.4.0

---

## globalRemove

### <instance> globalRemove([key], [animation])

**Description:**

Handle the removal of an animation from the Animation Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | Yes | The key of the removed Animation. |
| --- | --- | --- | --- |
| animation | [Phaser.Animations.Animation](/api-documentation/class/animations-animation) | Yes | The removed Animation. |

> Source: [src/animations/AnimationState.js#L1232](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1232)  
> Since: 3.50.0

---

## load

### <instance> load(key)

**Description:**

Internal method used to load an animation into this component.

**Access:** protected

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Animations.PlayAnimationConfig](/api-documentation/typedef/types-animations#playanimationconfig) | No | The string-based key of the animation to play, or a `PlayAnimationConfig` object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

> Source: [src/animations/AnimationState.js#L567](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L567)  
> Since: 3.0.0

---

## nextFrame

### <instance> nextFrame()

**Description:**

Advances the animation to the next frame, regardless of the time or animation state.

If the animation is set to repeat, or yoyo, this will still take effect.

Calling this does not change the direction of the animation. I.e. if it was currently

playing in reverse, calling this method doesn't then change the direction to forwards.

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object this Animation Component belongs to.

> Source: [src/animations/AnimationState.js#L1623](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1623)  
> Since: 3.16.0

---

## pause

### <instance> pause([atFrame])

**Description:**

Pause the current animation and set the `isPlaying` property to `false`.

You can optionally pause it at a specific frame.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| atFrame | [Phaser.Animations.AnimationFrame](/api-documentation/class/animations-animationframe) | Yes | An optional frame to set after pausing the animation. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

> Source: [src/animations/AnimationState.js#L644](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L644)  
> Since: 3.0.0

---

## play

### <instance> play(key, [ignoreIfPlaying])

**Description:**

Start playing the given animation on this Sprite.

Animations in Phaser can either belong to the global Animation Manager, or specifically to this Sprite.

The benefit of a global animation is that multiple Sprites can all play the same animation, without

having to duplicate the data. You can just create it once and then play it on any Sprite.

The following code shows how to create a global repeating animation. The animation will be created

from all of the frames within the sprite sheet that was loaded with the key 'muybridge':

```
Copy
var config = {

    key: 'run',

    frames: 'muybridge',

    frameRate: 15,

    repeat: -1

};



//  This code should be run from within a Scene:

this.anims.create(config);


```

However, if you wish to create an animation that is unique to this Sprite, and this Sprite alone,

you can call the `Animation.create` method instead. It accepts the exact same parameters as when

creating a global animation, however the resulting data is kept locally in this Sprite.

With the animation created, either globally or locally, you can now play it on this Sprite:

```
Copy
this.add.sprite(x, y).play('run');


```

Alternatively, if you wish to run it at a different frame rate, for example, you can pass a config

object instead:

```
Copy
this.add.sprite(x, y).play({ key: 'run', frameRate: 24 });


```

When playing an animation on a Sprite it will first check to see if it can find a matching key

locally within the Sprite. If it can, it will play the local animation. If not, it will then

search the global Animation Manager and look for it there.

If you need a Sprite to be able to play both local and global animations, make sure they don't

have conflicting keys.

See the documentation for the `PlayAnimationConfig` config object for more details about this.

Also, see the documentation in the Animation Manager for further details on creating animations.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Animations.Animation](/api-documentation/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api-documentation/typedef/types-animations#playanimationconfig) | No |  |
| --- | --- | --- | --- | --- |
| ignoreIfPlaying | boolean | Yes | false | If this animation is already playing then ignore this call. |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_START](/api-documentation/event/animations-events#animation_start)

> Source: [src/animations/AnimationState.js#L799](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L799)  
> Since: 3.0.0

---

## playAfterDelay

### <instance> playAfterDelay(key, delay)

**Description:**

Waits for the specified delay, in milliseconds, then starts playback of the given animation.

If the animation *also* has a delay value set in its config, it will be **added** to the delay given here.

If an animation is already running and a new animation is given to this method, it will wait for

the given delay before starting the new animation.

If no animation is currently running, the given one begins after the delay.

Prior to Phaser 3.50 this method was called 'delayedPlay' and the parameters were in the reverse order.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Animations.Animation](/api-documentation/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api-documentation/typedef/types-animations#playanimationconfig) | No |
| --- | --- | --- | --- |
| delay | number | No | The delay, in milliseconds, to wait before starting the animation playing. |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_START](/api-documentation/event/animations-events#animation_start)

> Source: [src/animations/AnimationState.js#L699](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L699)  
> Since: 3.50.0

---

## playAfterRepeat

### <instance> playAfterRepeat(key, [repeatCount])

**Description:**

Waits for the current animation to complete the `repeatCount` number of repeat cycles, then starts playback

of the given animation.

You can use this to ensure there are no harsh jumps between two sets of animations, i.e. going from an

idle animation to a walking animation, by making them blend smoothly into each other.

If no animation is currently running, the given one will start immediately.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Animations.Animation](/api-documentation/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api-documentation/typedef/types-animations#playanimationconfig) | No |  |
| --- | --- | --- | --- | --- |
| repeatCount | number | Yes | 1 | How many times should the animation repeat before the next one starts? |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_START](/api-documentation/event/animations-events#animation_start)

> Source: [src/animations/AnimationState.js#L748](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L748)  
> Since: 3.50.0

---

## playReverse

### <instance> playReverse(key, [ignoreIfPlaying])

**Description:**

Start playing the given animation on this Sprite, in reverse.

Animations in Phaser can either belong to the global Animation Manager, or specifically to this Sprite.

The benefit of a global animation is that multiple Sprites can all play the same animation, without

having to duplicate the data. You can just create it once and then play it on any Sprite.

The following code shows how to create a global repeating animation. The animation will be created

from all of the frames within the sprite sheet that was loaded with the key 'muybridge':

```
Copy
var config = {

    key: 'run',

    frames: 'muybridge',

    frameRate: 15,

    repeat: -1

};



//  This code should be run from within a Scene:

this.anims.create(config);


```

However, if you wish to create an animation that is unique to this Sprite, and this Sprite alone,

you can call the `Animation.create` method instead. It accepts the exact same parameters as when

creating a global animation, however the resulting data is kept locally in this Sprite.

With the animation created, either globally or locally, you can now play it on this Sprite:

```
Copy
this.add.sprite(x, y).playReverse('run');


```

Alternatively, if you wish to run it at a different frame rate, for example, you can pass a config

object instead:

```
Copy
this.add.sprite(x, y).playReverse({ key: 'run', frameRate: 24 });


```

When playing an animation on a Sprite it will first check to see if it can find a matching key

locally within the Sprite. If it can, it will play the local animation. If not, it will then

search the global Animation Manager and look for it there.

If you need a Sprite to be able to play both local and global animations, make sure they don't

have conflicting keys.

See the documentation for the `PlayAnimationConfig` config object for more details about this.

Also, see the documentation in the Animation Manager for further details on creating animations.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Animations.Animation](/api-documentation/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api-documentation/typedef/types-animations#playanimationconfig) | No |  |
| --- | --- | --- | --- | --- |
| ignoreIfPlaying | boolean | Yes | false | If an animation is already playing then ignore this call. |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_START](/api-documentation/event/animations-events#animation_start)

> Source: [src/animations/AnimationState.js#L894](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L894)  
> Since: 3.12.0

---

## previousFrame

### <instance> previousFrame()

**Description:**

Advances the animation to the previous frame, regardless of the time or animation state.

If the animation is set to repeat, or yoyo, this will still take effect.

Calling this does not change the direction of the animation. I.e. if it was currently

playing in forwards, calling this method doesn't then change the direction to backwards.

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object this Animation Component belongs to.

> Source: [src/animations/AnimationState.js#L1645](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1645)  
> Since: 3.16.0

---

## remove

### <instance> remove(key)

**Description:**

Removes a locally created Animation from this Sprite, based on the given key.

Once an Animation has been removed, this Sprite cannot play it again without re-creating it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the animation to remove. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Animations.Animation](/api-documentation/class/animations-animation) - The Animation instance that was removed from this Sprite, if the key was valid.

> Source: [src/animations/AnimationState.js#L1933](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1933)  
> Since: 3.50.0

---

## restart

### <instance> restart([includeDelay], [resetRepeats])

**Description:**

Restarts the current animation from its beginning.

You can optionally reset the delay and repeat counters as well.

Calling this will fire the `ANIMATION_RESTART` event immediately.

If you `includeDelay` then it will also fire the `ANIMATION_START` event once

the delay has expired, otherwise, playback will just begin immediately.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| includeDelay | boolean | Yes | false | Whether to include the delay value of the animation when restarting. |
| --- | --- | --- | --- | --- |
| resetRepeats | boolean | Yes | false | Whether to reset the repeat counter or not? |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_RESTART](/api-documentation/event/animations-events#animation_restart)

> Source: [src/animations/AnimationState.js#L1253](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1253)  
> Since: 3.0.0

---

## resume

### <instance> resume([fromFrame])

**Description:**

Resumes playback of a paused animation and sets the `isPlaying` property to `true`.

You can optionally tell it to start playback from a specific frame.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| fromFrame | [Phaser.Animations.AnimationFrame](/api-documentation/class/animations-animationframe) | Yes | An optional frame to set before restarting playback. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

> Source: [src/animations/AnimationState.js#L672](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L672)  
> Since: 3.0.0

---

## reverse

### <instance> reverse()

**Description:**

Reverse the Animation that is already playing on the Game Object.

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

> Source: [src/animations/AnimationState.js#L1130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1130)  
> Since: 3.12.0

---

## setCurrentFrame

### <instance> setCurrentFrame(animationFrame)

**Description:**

Sets the given Animation Frame as being the current frame

and applies it to the parent Game Object, adjusting size and origin as needed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| animationFrame | [Phaser.Animations.AnimationFrame](/api-documentation/class/animations-animationframe) | No | The animation frame to change to. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object this Animation Component belongs to.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_UPDATE](/api-documentation/event/animations-events#animation_update), [Phaser.Animations.Events#event:ANIMATION\_STOP](/api-documentation/event/animations-events#animation_stop)

> Source: [src/animations/AnimationState.js#L1564](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1564)  
> Since: 3.4.0

---

## setProgress

### <instance> setProgress([value])

**Description:**

Takes a value between 0 and 1 and uses it to set how far this animation is through playback.

Does not factor in repeats or yoyos, but does handle playing forwards or backwards.

The value is based on the current frame and how far that is in the animation, it is not based on

the duration of the animation.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The progress value, between 0 and 1. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

> Source: [src/animations/AnimationState.js#L1180](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1180)  
> Since: 3.4.0

---

## setRepeat

### <instance> setRepeat(value)

**Description:**

Sets the number of times that the animation should repeat after its first play through.

For example, if repeat is 1, the animation will play a total of twice: the initial play plus 1 repeat.

To repeat indefinitely, use -1.

The value should always be an integer.

Calling this method only works if the animation is already running. Otherwise, any

value specified here will be overwritten when the next animation loads in. To avoid this,

use the `repeat` property of the `PlayAnimationConfig` object instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The number of times that the animation should repeat. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

> Source: [src/animations/AnimationState.js#L1207](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1207)  
> Since: 3.4.0

---

## startAnimation

### <instance> startAnimation(key)

**Description:**

Load the animation based on the key and set-up all of the internal values

needed for playback to start. If there is no delay, it will also fire the start events.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Animations.PlayAnimationConfig](/api-documentation/typedef/types-animations#playanimationconfig) | No | The string-based key of the animation to play, or a `PlayAnimationConfig` object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_START](/api-documentation/event/animations-events#animation_start)

> Source: [src/animations/AnimationState.js#L975](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L975)  
> Since: 3.50.0

---

## stop

### <instance> stop()

**Description:**

Immediately stops the current animation from playing and dispatches the `ANIMATION_STOP` event.

If no animation is running, no events will be dispatched.

If there is another animation in the queue (set via the `chain` method) then it will start playing.

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_STOP](/api-documentation/event/animations-events#animation_stop)

> Source: [src/animations/AnimationState.js#L1347](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1347)  
> Since: 3.0.0

---

## stopAfterDelay

### <instance> stopAfterDelay(delay)

**Description:**

Stops the current animation from playing after the specified time delay, given in milliseconds.

It then dispatches the `ANIMATION_STOP` event.

If no animation is running, no events will be dispatched.

If there is another animation in the queue (set via the `chain` method) then it will start playing,

when the current one stops.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| delay | number | No | The number of milliseconds to wait before stopping this animation. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_STOP](/api-documentation/event/animations-events#animation_stop)

> Source: [src/animations/AnimationState.js#L1385](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1385)  
> Since: 3.4.0

---

## stopAfterRepeat

### <instance> stopAfterRepeat([repeatCount])

**Description:**

Stops the current animation from playing when it next repeats.

It then dispatches the `ANIMATION_STOP` event.

If no animation is running, no events will be dispatched.

If there is another animation in the queue (set via the `chain` method) then it will start playing,

when the current one stops.

Prior to Phaser 3.50 this method was called `stopOnRepeat` and had no parameters.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| repeatCount | number | Yes | 1 | How many times should the animation repeat before stopping? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_STOP](/api-documentation/event/animations-events#animation_stop)

> Source: [src/animations/AnimationState.js#L1411](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1411)  
> Since: 3.50.0

---

## stopOnFrame

### <instance> stopOnFrame(frame)

**Description:**

Stops the current animation from playing when it next sets the given frame.

If this frame doesn't exist within the animation it will not stop it from playing.

It then dispatches the `ANIMATION_STOP` event.

If no animation is running, no events will be dispatched.

If there is another animation in the queue (set via the `chain` method) then it will start playing,

when the current one stops.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| frame | [Phaser.Animations.AnimationFrame](/api-documentation/class/animations-animationframe) | No | The frame to check before stopping this animation. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) - The Game Object that owns this Animation Component.

**Fires:** [Phaser.Animations.Events#event:ANIMATION\_STOP](/api-documentation/event/animations-events#animation_stop)

> Source: [src/animations/AnimationState.js#L1446](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1446)  
> Since: 3.4.0

---

## update

### <instance> update(time, delta)

**Description:**

The internal update loop for the AnimationState Component.

This is called automatically by the `Sprite.preUpdate` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current timestamp. |
| --- | --- | --- | --- |
| delta | number | No | The delta time, in ms, elapsed since the last frame. |

> Source: [src/animations/AnimationState.js#L1487](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1487)  
> Since: 3.0.0

---

# Private Methods

## emitEvents

### <instance> emitEvents(event)

**Description:**

Fires the given animation event.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | No | The Animation Event to dispatch. |
| --- | --- | --- | --- |

> Source: [src/animations/AnimationState.js#L1100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1100)  
> Since: 3.50.0

---

## handleComplete

### <instance> handleComplete()

**Description:**

Handles the completion of an animation playback.

**Access:** private

> Source: [src/animations/AnimationState.js#L1079](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1079)  
> Since: 3.50.0

---

## handleRepeat

### <instance> handleRepeat()

**Description:**

Handles the repeat of an animation.

**Access:** private

> Source: [src/animations/AnimationState.js#L1049](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1049)  
> Since: 3.50.0

---

## handleStart

### <instance> handleStart()

**Description:**

Handles the start of an animation playback.

**Access:** private

> Source: [src/animations/AnimationState.js#L1028](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1028)  
> Since: 3.50.0

---

## handleStop

### <instance> handleStop()

**Description:**

Handles the stop of an animation playback.

**Access:** private

> Source: [src/animations/AnimationState.js#L1063](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationState.js#L1063)  
> Since: 3.50.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](/api-documentation/api-documentation)

On this page

* [Public Members](#public-members)

  + [accumulator](#accumulator)

    - [accumulator: number](#accumulator-number)
  + [animationManager](#animationmanager)

    - [animationManager: Phaser.Animations.AnimationManager](#animationmanager-phaseranimationsanimationmanager)
  + [anims](#anims)

    - [anims: Phaser.Structs.Map.<string, Phaser.Animations.Animation>](#anims-phaserstructsmapstring-phaseranimationsanimation)
  + [currentAnim](#currentanim)

    - [currentAnim: Phaser.Animations.Animation](#currentanim-phaseranimationsanimation)
  + [currentFrame](#currentframe)

    - [currentFrame: Phaser.Animations.AnimationFrame](#currentframe-phaseranimationsanimationframe)
  + [delay](#delay)

    - [delay: number](#delay-number)
  + [delayCounter](#delaycounter)

    - [delayCounter: number](#delaycounter-number)
  + [duration](#duration)

    - [duration: number](#duration-number)
  + [forward](#forward)

    - [forward: boolean](#forward-boolean)
  + [frameRate](#framerate)

    - [frameRate: number](#framerate-number)
  + [hasStarted](#hasstarted)

    - [hasStarted: boolean](#hasstarted-boolean)
  + [hideOnComplete](#hideoncomplete)

    - [hideOnComplete: boolean](#hideoncomplete-boolean)
  + [inReverse](#inreverse)

    - [inReverse: boolean](#inreverse-boolean)
  + [isPaused](#ispaused)

    - [isPaused: boolean](#ispaused-boolean)
  + [isPlaying](#isplaying)

    - [isPlaying: boolean](#isplaying-boolean)
  + [msPerFrame](#msperframe)

    - [msPerFrame: number](#msperframe-number)
  + [nextAnim](#nextanim)

    - [nextAnim: string, Phaser.Animations.Animation, Phaser.Types.Animations.PlayAnimationConfig](#nextanim-string-phaseranimationsanimation-phasertypesanimationsplayanimationconfig)
  + [nextAnimsQueue](#nextanimsqueue)

    - [nextAnimsQueue: array](#nextanimsqueue-array)
  + [nextTick](#nexttick)

    - [nextTick: number](#nexttick-number)
  + [parent](#parent)

    - [parent: Phaser.GameObjects.GameObject](#parent-phasergameobjectsgameobject)
  + [pendingRepeat](#pendingrepeat)

    - [pendingRepeat: boolean](#pendingrepeat-boolean)
  + [randomFrame](#randomframe)

    - [randomFrame: boolean](#randomframe-boolean)
  + [repeat](#repeat)

    - [repeat: number](#repeat-number)
  + [repeatCounter](#repeatcounter)

    - [repeatCounter: number](#repeatcounter-number)
  + [repeatDelay](#repeatdelay)

    - [repeatDelay: number](#repeatdelay-number)
  + [showBeforeDelay](#showbeforedelay)

    - [showBeforeDelay: boolean](#showbeforedelay-boolean)
  + [showOnStart](#showonstart)

    - [showOnStart: boolean](#showonstart-boolean)
  + [skipMissedFrames](#skipmissedframes)

    - [skipMissedFrames: boolean](#skipmissedframes-boolean)
  + [textureManager](#texturemanager)

    - [textureManager: Phaser.Textures.TextureManager](#texturemanager-phasertexturestexturemanager)
  + [timeScale](#timescale)

    - [timeScale: number](#timescale-number)
  + [yoyo](#yoyo)

    - [yoyo: boolean](#yoyo-boolean)
* [Private Members](#private-members)

  + [\_paused](#_paused)

    - [\_paused: boolean](#_paused-boolean)
  + [\_pendingStop](#_pendingstop)

    - [\_pendingStop: number](#_pendingstop-number)
  + [\_pendingStopValue](#_pendingstopvalue)

    - [\_pendingStopValue: any](#_pendingstopvalue-any)
  + [\_wasPlaying](#_wasplaying)

    - [\_wasPlaying: boolean](#_wasplaying-boolean)
* [Public Methods](#public-methods)

  + [chain](#chain)

    - [<instance> chain([key])](#instance-chainkey)
  + [complete](#complete)

    - [<instance> complete()](#instance-complete)
  + [create](#create)

    - [<instance> create(config)](#instance-createconfig)
  + [createFromAseprite](#createfromaseprite)

    - [<instance> createFromAseprite(key, [tags])](#instance-createfromasepritekey-tags)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [exists](#exists)

    - [<instance> exists(key)](#instance-existskey)
  + [generateFrameNames](#generateframenames)

    - [<instance> generateFrameNames(key, [config])](#instance-generateframenameskey-config)
  + [generateFrameNumbers](#generateframenumbers)

    - [<instance> generateFrameNumbers(key, [config])](#instance-generateframenumberskey-config)
  + [get](#get)

    - [<instance> get(key)](#instance-getkey)
  + [getFrameName](#getframename)

    - [<instance> getFrameName()](#instance-getframename)
  + [getName](#getname)

    - [<instance> getName()](#instance-getname)
  + [getProgress](#getprogress)

    - [<instance> getProgress()](#instance-getprogress)
  + [getTotalFrames](#gettotalframes)

    - [<instance> getTotalFrames()](#instance-gettotalframes)
  + [globalRemove](#globalremove)

    - [<instance> globalRemove([key], [animation])](#instance-globalremovekey-animation)
  + [load](#load)

    - [<instance> load(key)](#instance-loadkey)
  + [nextFrame](#nextframe)

    - [<instance> nextFrame()](#instance-nextframe)
  + [pause](#pause)

    - [<instance> pause([atFrame])](#instance-pauseatframe)
  + [play](#play)

    - [<instance> play(key, [ignoreIfPlaying])](#instance-playkey-ignoreifplaying)
  + [playAfterDelay](#playafterdelay)

    - [<instance> playAfterDelay(key, delay)](#instance-playafterdelaykey-delay)
  + [playAfterRepeat](#playafterrepeat)

    - [<instance> playAfterRepeat(key, [repeatCount])](#instance-playafterrepeatkey-repeatcount)
  + [playReverse](#playreverse)

    - [<instance> playReverse(key, [ignoreIfPlaying])](#instance-playreversekey-ignoreifplaying)
  + [previousFrame](#previousframe)

    - [<instance> previousFrame()](#instance-previousframe)
  + [remove](#remove)

    - [<instance> remove(key)](#instance-removekey)
  + [restart](#restart)

    - [<instance> restart([includeDelay], [resetRepeats])](#instance-restartincludedelay-resetrepeats)
  + [resume](#resume)

    - [<instance> resume([fromFrame])](#instance-resumefromframe)
  + [reverse](#reverse)

    - [<instance> reverse()](#instance-reverse)
  + [setCurrentFrame](#setcurrentframe)

    - [<instance> setCurrentFrame(animationFrame)](#instance-setcurrentframeanimationframe)
  + [setProgress](#setprogress)

    - [<instance> setProgress([value])](#instance-setprogressvalue)
  + [setRepeat](#setrepeat)

    - [<instance> setRepeat(value)](#instance-setrepeatvalue)
  + [startAnimation](#startanimation)

    - [<instance> startAnimation(key)](#instance-startanimationkey)
  + [stop](#stop)

    - [<instance> stop()](#instance-stop)
  + [stopAfterDelay](#stopafterdelay)

    - [<instance> stopAfterDelay(delay)](#instance-stopafterdelaydelay)
  + [stopAfterRepeat](#stopafterrepeat)

    - [<instance> stopAfterRepeat([repeatCount])](#instance-stopafterrepeatrepeatcount)
  + [stopOnFrame](#stoponframe)

    - [<instance> stopOnFrame(frame)](#instance-stoponframeframe)
  + [update](#update)

    - [<instance> update(time, delta)](#instance-updatetime-delta)
* [Private Methods](#private-methods)

  + [emitEvents](#emitevents)

    - [<instance> emitEvents(event)](#instance-emiteventsevent)
  + [handleComplete](#handlecomplete)

    - [<instance> handleComplete()](#instance-handlecomplete)
  + [handleRepeat](#handlerepeat)

    - [<instance> handleRepeat()](#instance-handlerepeat)
  + [handleStart](#handlestart)

    - [<instance> handleStart()](#instance-handlestart)
  + [handleStop](#handlestop)

    - [<instance> handleStop()](#instance-handlestop)

Back to top

©2025[Phaser](../../index.md)



AnimationState