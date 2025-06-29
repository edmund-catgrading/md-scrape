AnimationManager

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

# AnimationManager

Phaser.Animations.AnimationManager

The Animation Manager.

Animations are managed by the global Animation Manager. This is a singleton class that is

responsible for creating and delivering animations and their corresponding data to all Game Objects.

Unlike plugins it is owned by the Game instance, not the Scene.

Sprites and other Game Objects get the data they need from the AnimationManager.

**Constructor**

`new AnimationManager(game)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](/api-documentation/class/game) | No | A reference to the Phaser.Game instance. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](/api-documentation/class/events-eventemitter)

> Source: [src/animations/AnimationManager.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L19)  
> Since: 3.0.0

# Public Members

## anims

### anims: Phaser.Structs.Map.<string, [Phaser.Animations.Animation](/api-documentation/class/animations-animation)>

**Description:**

The Animations registered in the Animation Manager.

This map should be modified with the <#add> and <#create> methods of the Animation Manager.

**Access:** protected

> Source: [src/animations/AnimationManager.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L79)  
> Since: 3.0.0

---

## game

### game: [Phaser.Game](/api-documentation/class/game)

**Description:**

A reference to the Phaser.Game instance.

**Access:** protected

> Source: [src/animations/AnimationManager.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L47)  
> Since: 3.0.0

---

## globalTimeScale

### globalTimeScale: number

**Description:**

The global time scale of the Animation Manager.

This scales the time delta between two frames, thus influencing the speed of time for the Animation Manager.

> Source: [src/animations/AnimationManager.js#L67](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L67)  
> Since: 3.0.0

---

## mixes

### mixes: Phaser.Structs.Map.<string, [Phaser.Animations.Animation](/api-documentation/class/animations-animation)>

**Description:**

A list of animation mix times.

See the <#setMix> method for more details.

> Source: [src/animations/AnimationManager.js#L91](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L91)  
> Since: 3.50.0

---

## name

### name: string

**Description:**

The name of this Animation Manager.

> Source: [src/animations/AnimationManager.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L112)  
> Since: 3.0.0

---

## paused

### paused: boolean

**Description:**

Whether the Animation Manager is paused along with all of its Animations.

> Source: [src/animations/AnimationManager.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L102)  
> Since: 3.0.0

---

## textureManager

### textureManager: [Phaser.Textures.TextureManager](/api-documentation/class/textures-texturemanager)

**Description:**

A reference to the Texture Manager.

**Access:** protected

> Source: [src/animations/AnimationManager.js#L57](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L57)  
> Since: 3.0.0

---

# Public Methods

## add

### <instance> add(key, animation)

**Description:**

Adds an existing Animation to the Animation Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key under which the Animation should be added. The Animation will be updated with it. Must be unique. |
| --- | --- | --- | --- |
| animation | [Phaser.Animations.Animation](/api-documentation/class/animations-animation) | No | The Animation which should be added to the Animation Manager. |

**Returns:** [Phaser.Animations.AnimationManager](/api-documentation/class/animations-animationmanager) - This Animation Manager.

**Fires:** [Phaser.Animations.Events#event:ADD\_ANIMATION](/api-documentation/event/animations-events#add_animation)

> Source: [src/animations/AnimationManager.js#L276](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L276)  
> Since: 3.0.0

---

## addListener

### <instance> addListener(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Animations.AnimationManager](/api-documentation/class/animations-animationmanager) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](/api-documentation/class/events-eventemitter#addlistener)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## addMix

### <instance> addMix(animA, animB, delay)

**Description:**

Adds a mix between two animations.

Mixing allows you to specify a unique delay between a pairing of animations.

When playing Animation A on a Game Object, if you then play Animation B, and a

mix exists, it will wait for the specified delay to be over before playing Animation B.

This allows you to customise smoothing between different types of animation, such

as blending between an idle and a walk state, or a running and a firing state.

Note that mixing is only applied if you use the `Sprite.play` method. If you opt to use

`playAfterRepeat` or `playAfterDelay` instead, those will take priority and the mix

delay will not be used.

To update an existing mix, just call this method with the new delay.

To remove a mix pairing, see the `removeMix` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| animA | string | [Phaser.Animations.Animation](/api-documentation/class/animations-animation) | No | The string-based key, or instance of, Animation A. |
| --- | --- | --- | --- |
| animB | string | [Phaser.Animations.Animation](/api-documentation/class/animations-animation) | No | The string-based key, or instance of, Animation B. |
| delay | number | No | The delay, in milliseconds, to wait when transitioning from Animation A to B. |

**Returns:** [Phaser.Animations.AnimationManager](/api-documentation/class/animations-animationmanager) - This Animation Manager.

> Source: [src/animations/AnimationManager.js#L138](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L138)  
> Since: 3.50.0

---

## boot

### <instance> boot()

**Description:**

Registers event listeners after the Game boots.

> Source: [src/animations/AnimationManager.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L124)  
> Since: 3.0.0

---

## create

### <instance> create(config)

**Description:**

Creates a new Animation and adds it to the Animation Manager.

Animations are global. Once created, you can use them in any Scene in your game. They are not Scene specific.

If an invalid key is given this method will return `false`.

If you pass the key of an animation that already exists in the Animation Manager, that animation will be returned.

A brand new animation is only created if the key is valid and not already in use.

If you wish to re-use an existing key, call `AnimationManager.remove` first, then this method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Animations.Animation](/api-documentation/typedef/types-animations#animation) | No | The configuration settings for the Animation. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Animations.Animation](/api-documentation/class/animations-animation), false - The Animation that was created, or `false` if the key is already in use.

**Fires:** [Phaser.Animations.Events#event:ADD\_ANIMATION](/api-documentation/event/animations-events#add_animation)

> Source: [src/animations/AnimationManager.js#L492](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L492)  
> Since: 3.0.0

---

## createFromAseprite

### <instance> createFromAseprite(key, [tags], [target])

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

Once loaded, you can call this method from within a Scene with the 'atlas' key:

```
Copy
this.anims.createFromAseprite('paladin');


```

Any animations defined in the JSON will now be available to use in Phaser and you play them

via their Tag name. For example, if you have an animation called 'War Cry' on your Aseprite timeline,

you can play it in Phaser using that Tag name:

```
Copy
this.add.sprite(400, 300).play('War Cry');


```

When calling this method you can optionally provide an array of tag names, and only those animations

will be created. For example:

```
Copy
this.anims.createFromAseprite('paladin', [ 'step', 'War Cry', 'Magnum Break' ]);


```

This will only create the 3 animations defined. Note that the tag names are case-sensitive.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the loaded Aseprite atlas. It must have been loaded prior to calling this method. |
| --- | --- | --- | --- |
| tags | Array.<string> | Yes | An array of Tag names. If provided, only animations found in this array will be created. |
| target | [Phaser.Animations.AnimationManager](/api-documentation/class/animations-animationmanager) | [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) | Yes | Create the animations on this target Sprite. If not given, they will be created globally in this Animation Manager. |

**Returns:** Array.<[Phaser.Animations.Animation](/api-documentation/class/animations-animation)> - An array of Animation instances that were successfully created.

> Source: [src/animations/AnimationManager.js#L323](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L323)  
> Since: 3.50.0

---

## destroy

### <instance> destroy()

**Description:**

Destroy this Animation Manager and clean up animation definitions and references to other objects.

This method should not be called directly. It will be called automatically as a response to a `destroy` event from the Phaser.Game instance.

**Overrides:** Phaser.Events.EventEmitter#destroy

> Source: [src/animations/AnimationManager.js#L1045](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L1045)  
> Since: 3.0.0

---

## emit

### <instance> emit(event, [args])

**Description:**

Calls each of the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| args | \* | Yes | Additional arguments that will be passed to the event handler. |

**Returns:** boolean - `true` if the event had listeners, else `false`.

**Inherits:** [Phaser.Events.EventEmitter#emit](/api-documentation/class/events-eventemitter#emit)

> Source: [src/events/EventEmitter.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L86)  
> Since: 3.0.0

---

## eventNames

### <instance> eventNames()

**Description:**

Return an array listing the events for which the emitter has registered listeners.

**Returns:** Array.<(string | symbol)> - undefined

**Inherits:** [Phaser.Events.EventEmitter#eventNames](/api-documentation/class/events-eventemitter#eventnames)

> Source: [src/events/EventEmitter.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L55)  
> Since: 3.0.0

---

## exists

### <instance> exists(key)

**Description:**

Checks to see if the given key is already in use within the Animation Manager or not.

Animations are global. Keys created in one scene can be used from any other Scene in your game. They are not Scene specific.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the Animation to check. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the Animation already exists in the Animation Manager, or `false` if the key is available.

> Source: [src/animations/AnimationManager.js#L306](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L306)  
> Since: 3.16.0

---

## fromJSON

### <instance> fromJSON(data, [clearCurrentAnimations])

**Description:**

Loads this Animation Manager's Animations and settings from a JSON object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| data | string | [Phaser.Types.Animations.JSONAnimations](/api-documentation/typedef/types-animations#jsonanimations) | [Phaser.Types.Animations.JSONAnimation](/api-documentation/typedef/types-animations#jsonanimation) | No |  |
| --- | --- | --- | --- | --- |
| clearCurrentAnimations | boolean | Yes | false | If set to `true`, the current animations will be removed (`anims.clear()`). If set to `false` (default), the animations in `data` will be added. |

**Returns:** Array.<[Phaser.Animations.Animation](/api-documentation/class/animations-animation)> - An array containing all of the Animation objects that were created as a result of this call.

> Source: [src/animations/AnimationManager.js#L540](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L540)  
> Since: 3.0.0

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

then you can call this method using: `this.anims.generateFrameNames('gems', { prefix: 'ruby_', start: 1, end: 6, zeroPad: 4 })`.

The `end` value tells it to select frames 1 through 6, incrementally numbered, all starting with the prefix `ruby_`. The `zeroPad`

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

> Source: [src/animations/AnimationManager.js#L589](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L589)  
> Since: 3.0.0

---

## generateFrameNumbers

### <instance> generateFrameNumbers(key, [config])

**Description:**

Generate an array of [Phaser.Types.Animations.AnimationFrame](/api-documentation/typedef/types-animations#animationframe) objects from a texture key and configuration object.

Generates objects with numbered frame names, as configured by the given [Phaser.Types.Animations.GenerateFrameNumbers](/api-documentation/typedef/types-animations#generateframenumbers).

If you're working with a texture atlas, see the `generateFrameNames` method instead.

It's a helper method, designed to make it easier for you to extract frames from sprite sheets.

Example:

If you have a sprite sheet loaded called `explosion` and it contains 12 frames, then you can call this method using:

`this.anims.generateFrameNumbers('explosion', { start: 0, end: 11 })`.

The `end` value of 11 tells it to stop after the 12th frame has been added, because it started at zero.

To create an animation using this method, you can do:

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

> Source: [src/animations/AnimationManager.js#L689](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L689)  
> Since: 3.0.0

---

## get

### <instance> get(key)

**Description:**

Get an Animation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the Animation to retrieve. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Animations.Animation](/api-documentation/class/animations-animation) - The Animation.

> Source: [src/animations/AnimationManager.js#L793](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L793)  
> Since: 3.0.0

---

## getAnimsFromTexture

### <instance> getAnimsFromTexture(key)

**Description:**

Returns an array of all Animation keys that are using the given

Texture. Only Animations that have at least one AnimationFrame

entry using this texture will be included in the result.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Textures.Texture](/api-documentation/class/textures-texture) | [Phaser.Textures.Frame](/api-documentation/class/textures-frame) | No |
| --- | --- | --- | --- |

**Returns:** Array.<string> - An array of Animation keys that feature the given Texture.

> Source: [src/animations/AnimationManager.js#L808](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L808)  
> Since: 3.60.0

---

## getMix

### <instance> getMix(animA, animB)

**Description:**

Returns the mix delay between two animations.

If no mix has been set-up, this method will return zero.

If you wish to create, or update, a new mix, call the `addMix` method.

If you wish to remove a mix, call the `removeMix` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| animA | string | [Phaser.Animations.Animation](/api-documentation/class/animations-animation) | No | The string-based key, or instance of, Animation A. |
| --- | --- | --- | --- |
| animB | string | [Phaser.Animations.Animation](/api-documentation/class/animations-animation) | No | The string-based key, or instance of, Animation B. |

**Returns:** number - The mix duration, or zero if no mix exists.

> Source: [src/animations/AnimationManager.js#L241](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L241)  
> Since: 3.50.0

---

## listenerCount

### <instance> listenerCount(event)

**Description:**

Return the number of listeners listening to a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** number - The number of listeners.

**Inherits:** [Phaser.Events.EventEmitter#listenerCount](/api-documentation/class/events-eventemitter#listenercount)

> Source: [src/events/EventEmitter.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L75)  
> Since: 3.0.0

---

## listeners

### <instance> listeners(event)

**Description:**

Return the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** Array.<function()> - The registered listeners.

**Inherits:** [Phaser.Events.EventEmitter#listeners](/api-documentation/class/events-eventemitter#listeners)

> Source: [src/events/EventEmitter.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L64)  
> Since: 3.0.0

---

## off

### <instance> off(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.Animations.AnimationManager](/api-documentation/class/animations-animationmanager) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#off](/api-documentation/class/events-eventemitter#off)

> Source: [src/events/EventEmitter.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L151)  
> Since: 3.0.0

---

## on

### <instance> on(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Animations.AnimationManager](/api-documentation/class/animations-animationmanager) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#on](/api-documentation/class/events-eventemitter#on)

> Source: [src/events/EventEmitter.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L98)  
> Since: 3.0.0

---

## once

### <instance> once(event, fn, [context])

**Description:**

Add a one-time listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Animations.AnimationManager](/api-documentation/class/animations-animationmanager) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](/api-documentation/class/events-eventemitter#once)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## pauseAll

### <instance> pauseAll()

**Description:**

Pause all animations.

**Returns:** [Phaser.Animations.AnimationManager](/api-documentation/class/animations-animationmanager) - This Animation Manager.

**Fires:** [Phaser.Animations.Events#event:PAUSE\_ALL](/api-documentation/event/animations-events#pause_all)

> Source: [src/animations/AnimationManager.js#L848](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L848)  
> Since: 3.0.0

---

## play

### <instance> play(key, children)

**Description:**

Play an animation on the given Game Objects that have an Animation Component.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Animations.Animation](/api-documentation/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api-documentation/typedef/types-animations#playanimationconfig) | No |
| --- | --- | --- | --- |
| children | [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) | Array.<[Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject)> | No | An array of Game Objects to play the animation on. They must have an Animation Component. |

**Returns:** [Phaser.Animations.AnimationManager](/api-documentation/class/animations-animationmanager) - This Animation Manager.

> Source: [src/animations/AnimationManager.js#L869](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L869)  
> Since: 3.0.0

---

## remove

### <instance> remove(key)

**Description:**

Removes an Animation from this Animation Manager, based on the given key.

This is a global action. Once an Animation has been removed, no Game Objects

can carry on using it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the animation to remove. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Animations.Animation](/api-documentation/class/animations-animation) - The Animation instance that was removed from the Animation Manager.

**Fires:** [Phaser.Animations.Events#event:REMOVE\_ANIMATION](/api-documentation/event/animations-events#remove_animation)

> Source: [src/animations/AnimationManager.js#L961](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L961)  
> Since: 3.0.0

---

## removeAllListeners

### <instance> removeAllListeners([event])

**Description:**

Remove all listeners, or those of the specified event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | Yes | The event name. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Animations.AnimationManager](/api-documentation/class/animations-animationmanager) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](/api-documentation/class/events-eventemitter#removealllisteners)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeListener

### <instance> removeListener(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.Animations.AnimationManager](/api-documentation/class/animations-animationmanager) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](/api-documentation/class/events-eventemitter#removelistener)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## removeMix

### <instance> removeMix(animA, [animB])

**Description:**

Removes a mix between two animations.

Mixing allows you to specify a unique delay between a pairing of animations.

Calling this method lets you remove those pairings. You can either remove

it between `animA` and `animB`, or if you do not provide the `animB` parameter,

it will remove all `animA` mixes.

If you wish to update an existing mix instead, call the `addMix` method with the

new delay.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| animA | string | [Phaser.Animations.Animation](/api-documentation/class/animations-animation) | No | The string-based key, or instance of, Animation A. |
| --- | --- | --- | --- |
| animB | string | [Phaser.Animations.Animation](/api-documentation/class/animations-animation) | Yes | The string-based key, or instance of, Animation B. If not given, all mixes for Animation A will be removed. |

**Returns:** [Phaser.Animations.AnimationManager](/api-documentation/class/animations-animationmanager) - This Animation Manager.

> Source: [src/animations/AnimationManager.js#L191](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L191)  
> Since: 3.50.0

---

## resumeAll

### <instance> resumeAll()

**Description:**

Resume all paused animations.

**Returns:** [Phaser.Animations.AnimationManager](/api-documentation/class/animations-animationmanager) - This Animation Manager.

**Fires:** [Phaser.Animations.Events#event:RESUME\_ALL](/api-documentation/event/animations-events#resume_all)

> Source: [src/animations/AnimationManager.js#L991](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L991)  
> Since: 3.0.0

---

## shutdown

### <instance> shutdown()

**Description:**

Removes all listeners.

**Inherits:** [Phaser.Events.EventEmitter#shutdown](/api-documentation/class/events-eventemitter#shutdown)

> Source: [src/events/EventEmitter.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L31)  
> Since: 3.0.0

---

## staggerPlay

### <instance> staggerPlay(key, children, stagger, [staggerFirst])

**Description:**

Takes an array of Game Objects that have an Animation Component and then

starts the given animation playing on them. The start time of each Game Object

is offset, incrementally, by the `stagger` amount.

For example, if you pass an array with 4 children and a stagger time of 1000,

the delays will be:

child 1: 1000ms delay

child 2: 2000ms delay

child 3: 3000ms delay

child 4: 4000ms delay

If you set the `staggerFirst` parameter to `false` they would be:

child 1: 0ms delay

child 2: 1000ms delay

child 3: 2000ms delay

child 4: 3000ms delay

You can also set `stagger` to be a negative value. If it was -1000, the above would be:

child 1: 3000ms delay

child 2: 2000ms delay

child 3: 1000ms delay

child 4: 0ms delay

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Animations.Animation](/api-documentation/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api-documentation/typedef/types-animations#playanimationconfig) | No |  |
| --- | --- | --- | --- | --- |
| children | [Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject) | Array.<[Phaser.GameObjects.GameObject](/api-documentation/class/gameobjects-gameobject)> | No |  | An array of Game Objects to play the animation on. They must have an Animation Component. |
| stagger | number | No |  | The amount of time, in milliseconds, to offset each play time by. If a negative value is given, it's applied to the children in reverse order. |
| staggerFirst | boolean | Yes | true | Should the first child be staggered as well? |

**Returns:** [Phaser.Animations.AnimationManager](/api-documentation/class/animations-animationmanager) - This Animation Manager.

> Source: [src/animations/AnimationManager.js#L895](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L895)  
> Since: 3.0.0

---

## toJSON

### <instance> toJSON([key])

**Description:**

Returns the Animation data as JavaScript object based on the given key.

Or, if not key is defined, it will return the data of all animations as array of objects.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | Yes | The animation to get the JSONAnimation data from. If not provided, all animations are returned as an array. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Animations.JSONAnimations](/api-documentation/typedef/types-animations#jsonanimations) - The resulting JSONAnimations formatted object.

> Source: [src/animations/AnimationManager.js#L1012](https://github.com/phaserjs/phaser/blob/v3.87.0/src/animations/AnimationManager.js#L1012)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](/api-documentation/api-documentation)

On this page

* [Public Members](#public-members)

  + [anims](#anims)

    - [anims: Phaser.Structs.Map.<string, Phaser.Animations.Animation>](#anims-phaserstructsmapstring-phaseranimationsanimation)
  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [globalTimeScale](#globaltimescale)

    - [globalTimeScale: number](#globaltimescale-number)
  + [mixes](#mixes)

    - [mixes: Phaser.Structs.Map.<string, Phaser.Animations.Animation>](#mixes-phaserstructsmapstring-phaseranimationsanimation)
  + [name](#name)

    - [name: string](#name-string)
  + [paused](#paused)

    - [paused: boolean](#paused-boolean)
  + [textureManager](#texturemanager)

    - [textureManager: Phaser.Textures.TextureManager](#texturemanager-phasertexturestexturemanager)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(key, animation)](#instance-addkey-animation)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addMix](#addmix)

    - [<instance> addMix(animA, animB, delay)](#instance-addmixanima-animb-delay)
  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [create](#create)

    - [<instance> create(config)](#instance-createconfig)
  + [createFromAseprite](#createfromaseprite)

    - [<instance> createFromAseprite(key, [tags], [target])](#instance-createfromasepritekey-tags-target)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [exists](#exists)

    - [<instance> exists(key)](#instance-existskey)
  + [fromJSON](#fromjson)

    - [<instance> fromJSON(data, [clearCurrentAnimations])](#instance-fromjsondata-clearcurrentanimations)
  + [generateFrameNames](#generateframenames)

    - [<instance> generateFrameNames(key, [config])](#instance-generateframenameskey-config)
  + [generateFrameNumbers](#generateframenumbers)

    - [<instance> generateFrameNumbers(key, [config])](#instance-generateframenumberskey-config)
  + [get](#get)

    - [<instance> get(key)](#instance-getkey)
  + [getAnimsFromTexture](#getanimsfromtexture)

    - [<instance> getAnimsFromTexture(key)](#instance-getanimsfromtexturekey)
  + [getMix](#getmix)

    - [<instance> getMix(animA, animB)](#instance-getmixanima-animb)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [pauseAll](#pauseall)

    - [<instance> pauseAll()](#instance-pauseall)
  + [play](#play)

    - [<instance> play(key, children)](#instance-playkey-children)
  + [remove](#remove)

    - [<instance> remove(key)](#instance-removekey)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [removeMix](#removemix)

    - [<instance> removeMix(animA, [animB])](#instance-removemixanima-animb)
  + [resumeAll](#resumeall)

    - [<instance> resumeAll()](#instance-resumeall)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [staggerPlay](#staggerplay)

    - [<instance> staggerPlay(key, children, stagger, [staggerFirst])](#instance-staggerplaykey-children-stagger-staggerfirst)
  + [toJSON](#tojson)

    - [<instance> toJSON([key])](#instance-tojsonkey)

Back to top

©2025[Phaser](../../index.md)



AnimationManager