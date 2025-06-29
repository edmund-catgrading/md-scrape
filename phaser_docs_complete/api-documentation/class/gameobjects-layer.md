# Layer

Phaser.GameObjects.Layer

A Layer Game Object.

A Layer is a special type of Game Object that acts as a Display List. You can add any type of Game Object

to a Layer, just as you would to a Scene. Layers can be used to visually group together 'layers' of Game

Objects:

```
Copy
const spaceman = this.add.sprite(150, 300, 'spaceman');

const bunny = this.add.sprite(400, 300, 'bunny');

const elephant = this.add.sprite(650, 300, 'elephant');



const layer = this.add.layer();



layer.add([ spaceman, bunny, elephant ]);


```

The 3 sprites in the example above will now be managed by the Layer they were added to. Therefore,

if you then set `layer.setVisible(false)` they would all vanish from the display.

You can also control the depth of the Game Objects within the Layer. For example, calling the

`setDepth` method of a child of a Layer will allow you to adjust the depth of that child \_within the

Layer itself\_, rather than the whole Scene. The Layer, too, can have its depth set as well.

The Layer class also offers many different methods for manipulating the list, such as the

methods `moveUp`, `moveDown`, `sendToBack`, `bringToTop` and so on. These allow you to change the

display list position of the Layers children, causing it to adjust the order in which they are

rendered. Using `setDepth` on a child allows you to override this.

Layers can have Post FX Pipelines set, which allows you to easily enable a post pipeline across

a whole range of children, which, depending on the effect, can often be far more efficient that doing so

on a per-child basis.

Layers have no position or size within the Scene. This means you cannot enable a Layer for

physics or input, or change the position, rotation or scale of a Layer. They also have no scroll

factor, texture, tint, origin, crop or bounds.

If you need those kind of features then you should use a Container instead. Containers can be added

to Layers, but Layers cannot be added to Containers.

However, you can set the Alpha, Blend Mode, Depth, Mask and Visible state of a Layer. These settings

will impact all children being rendered by the Layer.

**Constructor**

`new Layer(scene, [children])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time. |
| --- | --- | --- | --- |
| children | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | Yes | An optional array of Game Objects to add to this Layer. |

---

**Scope**: static

**Extends**

> Phaser.Structs.List.<Phaser.GameObjects.GameObject>  
> [Phaser.GameObjects.Components.AlphaSingle](../namespace/gameobjects-components-alphasingle.md)  
> [Phaser.GameObjects.Components.BlendMode](../namespace/gameobjects-components-blendmode.md)  
> [Phaser.GameObjects.Components.Depth](../namespace/gameobjects-components-depth.md)  
> [Phaser.GameObjects.Components.Mask](../namespace/gameobjects-components-mask.md)  
> [Phaser.GameObjects.Components.PostPipeline](../namespace/gameobjects-components-postpipeline.md)  
> [Phaser.GameObjects.Components.Visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/layer/Layer.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L19)  
> Since: 3.50.0

# Public Members

## active

### active: boolean

**Description:**

The active state of this Game Object.

A Game Object with an active state of `true` is processed by the Scenes UpdateList, if added to it.

An active object is one which is having its logic and internal systems updated.

> Source: [src/gameobjects/layer/Layer.js#L178](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L178)  
> Since: 3.50.0

---

## alpha

### alpha: number

**Description:**

The alpha value of the Game Object.

This is a global value, impacting the entire Game Object, not just a region of it.

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#alpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L68)  
> Since: 3.0.0

---

## blendMode

### blendMode: [Phaser.BlendModes](../namespace/blendmodes.md), string, number

**Description:**

Sets the Blend Mode being used by this Game Object.

This can be a const, such as `Phaser.BlendModes.SCREEN`, or an integer, such as 4 (for Overlay)

Under WebGL only the following Blend Modes are available:

* NORMAL
* ADD
* MULTIPLY
* SCREEN
* ERASE

Canvas has more available depending on browser support.

You can also create your own custom Blend Modes in WebGL.

Blend modes have different effects under Canvas and WebGL, and from browser to browser, depending

on support. Blend Modes also cause a WebGL batch flush should it encounter a new blend mode. For these

reasons try to be careful about the construction of your Scene and the frequency of which blend modes

are used.

**Inherits:** [Phaser.GameObjects.Components.BlendMode#blendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L30)  
> Since: 3.0.0

---

## body

### body: [Phaser.Physics.Arcade.Body](physics-arcade-body.md), [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md), MatterJS.BodyType

**Description:**

This property is kept purely so a Layer has the same

shape as a Game Object. You cannot give a Layer a physics body.

> Source: [src/gameobjects/layer/Layer.js#L251](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L251)  
> Since: 3.51.0

---

## cameraFilter

### cameraFilter: number

**Description:**

A bitmask that controls if this Game Object is drawn by a Camera or not.

Not usually set directly, instead call `Camera.ignore`, however you can

set this property directly using the Camera.id property:

> Source: [src/gameobjects/layer/Layer.js#L225](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L225)  
> Since: 3.50.0

---

## data

### data: [Phaser.Data.DataManager](data-datamanager.md)

**Description:**

A Data Manager.

It allows you to store, query and get key/value paired information specific to this Game Object.

`null` by default. Automatically created if you use `getData` or `setData` or `setDataEnabled`.

> Source: [src/gameobjects/layer/Layer.js#L201](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L201)  
> Since: 3.50.0

---

## depth

### depth: number

**Description:**

The depth of this Game Object within the Scene. Ensure this value is only ever set to a number data-type.

The depth is also known as the 'z-index' in some environments, and allows you to change the rendering order

of Game Objects, without actually moving their position in the display list.

The default depth is zero. A Game Object with a higher depth

value will always render in front of one with a lower value.

Setting the depth will queue a depth sort event within the Scene.

**Inherits:** [Phaser.GameObjects.Components.Depth#depth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L30)  
> Since: 3.0.0

---

## displayList

### displayList: [Phaser.GameObjects.DisplayList](gameobjects-displaylist.md), [Phaser.GameObjects.Layer](gameobjects-layer.md)

**Description:**

Holds a reference to the Display List that contains this Game Object.

This is set automatically when this Game Object is added to a Scene or Layer.

You should treat this property as being read-only.

> Source: [src/gameobjects/layer/Layer.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L115)  
> Since: 3.50.0

---

## events

### events: [Phaser.Events.EventEmitter](events-eventemitter.md)

**Description:**

A reference to the Scene Event Emitter.

> Source: [src/gameobjects/layer/Layer.js#L284](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L284)  
> Since: 3.50.0

---

## hasPostPipeline

### hasPostPipeline: boolean

**Description:**

Does this Game Object have any Post Pipelines set?

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#hasPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L21)  
> Since: 3.60.0

---

## ignoreDestroy

### ignoreDestroy: boolean

**Description:**

This Game Object will ignore all calls made to its destroy method if this flag is set to `true`.

This includes calls that may come from a Group, Container or the Scene itself.

While it allows you to persist a Game Object across Scenes, please understand you are entirely

responsible for managing references to and from this Game Object.

> Source: [src/gameobjects/layer/Layer.js#L262](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L262)  
> Since: 3.50.0

---

## input

### input: [Phaser.Types.Input.InteractiveObject](../typedef/types-input.md)

**Description:**

This property is kept purely so a Layer has the same

shape as a Game Object. You cannot input enable a Layer.

> Source: [src/gameobjects/layer/Layer.js#L240](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L240)  
> Since: 3.51.0

---

## mask

### mask: [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md), [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md)

**Description:**

The Mask this Game Object is using during render.

**Inherits:** [Phaser.GameObjects.Components.Mask#mask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L19)  
> Since: 3.0.0

---

## name

### name: string

**Description:**

The name of this Game Object.

Empty by default and never populated by Phaser, this is left for developers to use.

> Source: [src/gameobjects/layer/Layer.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L167)  
> Since: 3.50.0

---

## parentContainer

### parentContainer: [Phaser.GameObjects.Container](gameobjects-container.md)

**Description:**

A Layer cannot be placed inside a Container.

This property is kept purely so a Layer has the same

shape as a Game Object.

> Source: [src/gameobjects/layer/Layer.js#L155](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L155)  
> Since: 3.51.0

---

## postFX

### postFX: [Phaser.GameObjects.Components.FX](gameobjects-components-fx.md)

**Description:**

The Post FX component of this Game Object.

This component allows you to apply a variety of built-in effects to this Game Object, such

as glow, blur, bloom, displacements, vignettes and more. You access them via this property,

for example:

```
Copy
const player = this.add.sprite();

player.postFX.addBloom();


```

All FX are WebGL only and do not have Canvas counterparts.

Please see the FX Class for more details and available methods.

This property is always `null` until the `initPostPipeline` method is called.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#postFX](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L88)  
> Since: 3.60.0

---

## postPipelineData

### postPipelineData: object

**Description:**

An object to store pipeline specific data in, to be read by the pipelines this Game Object uses.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#postPipelineData](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L46)  
> Since: 3.60.0

---

## postPipelines

### postPipelines: Array.<[Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md)>

**Description:**

The WebGL Post FX Pipelines this Game Object uses for post-render effects.

The pipelines are processed in the order in which they appear in this array.

If you modify this array directly, be sure to set the

`hasPostPipeline` property accordingly.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#postPipelines](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L31)  
> Since: 3.60.0

---

## preFX

### preFX: [Phaser.GameObjects.Components.FX](gameobjects-components-fx.md)

**Description:**

The Pre FX component of this Game Object.

This component allows you to apply a variety of built-in effects to this Game Object, such

as glow, blur, bloom, displacements, vignettes and more. You access them via this property,

for example:

```
Copy
const player = this.add.sprite();

player.preFX.addBloom();


```

Only the following Game Objects support Pre FX:

* Image
* Sprite
* TileSprite
* Text
* RenderTexture
* Video

All FX are WebGL only and do not have Canvas counterparts.

Please see the FX Class for more details and available methods.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#preFX](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L56)  
> Since: 3.60.0

---

## renderFlags

### renderFlags: number

**Description:**

The flags that are compared against `RENDER_MASK` to determine if this Game Object will render or not.

The bits are 0001 | 0010 | 0100 | 1000 set by the components Visible, Alpha, Transform and Texture respectively.

If those components are not used by your custom class then you can use this bitmask as you wish.

> Source: [src/gameobjects/layer/Layer.js#L213](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L213)  
> Since: 3.50.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

A reference to the Scene to which this Game Object belongs.

Game Objects can only belong to one Scene.

You should consider this property as being read-only. You cannot move a

Game Object to another Scene by simply changing it.

> Source: [src/gameobjects/layer/Layer.js#L101](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L101)  
> Since: 3.50.0

---

## sortChildrenFlag

### sortChildrenFlag: boolean

**Description:**

The flag the determines whether Game Objects should be sorted when `depthSort()` is called.

> Source: [src/gameobjects/layer/Layer.js#L293](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L293)  
> Since: 3.50.0

---

## state

### state: number, string

**Description:**

The current state of this Game Object.

Phaser itself will never modify this value, although plugins may do so.

Use this property to track the state of a Game Object during its lifetime. For example, it could change from

a state of 'moving', to 'attacking', to 'dead'. The state value should be an integer (ideally mapped to a constant

in your game code), or a string. These are recommended to keep it light and simple, with fast comparisons.

If you need to store complex data about your Game Object, look at using the Data Component instead.

> Source: [src/gameobjects/layer/Layer.js#L139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L139)  
> Since: 3.50.0

---

## systems

### systems: [Phaser.Scenes.Systems](scenes-systems.md)

**Description:**

A reference to the Scene Systems.

> Source: [src/gameobjects/layer/Layer.js#L275](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L275)  
> Since: 3.50.0

---

## tabIndex

### tabIndex: number

**Description:**

The Tab Index of the Game Object.

Reserved for future use by plugins and the Input Manager.

> Source: [src/gameobjects/layer/Layer.js#L190](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L190)  
> Since: 3.51.0

---

## type

### type: string

**Description:**

A textual representation of this Game Object, i.e. `sprite`.

Used internally by Phaser but is available for your own custom classes to populate.

> Source: [src/gameobjects/layer/Layer.js#L129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L129)  
> Since: 3.50.0

---

## visible

### visible: boolean

**Description:**

The visible state of the Game Object.

An invisible Game Object will skip rendering, but will still process update logic.

**Inherits:** [Phaser.GameObjects.Components.Visible#visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L31)  
> Since: 3.0.0

---

# Private Members

## \_alpha

### \_alpha: number

**Description:**

Private internal value. Holds the global alpha value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#\_alpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L22](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L22)  
> Since: 3.0.0

---

## \_blendMode

### \_blendMode: number

**Description:**

Private internal value. Holds the current blend mode.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.BlendMode#\_blendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L19)  
> Since: 3.0.0

---

## \_depth

### \_depth: number

**Description:**

Private internal value. Holds the depth of the Game Object.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Depth#\_depth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L19)  
> Since: 3.0.0

---

## \_visible

### \_visible: boolean

**Description:**

Private internal value. Holds the visible value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Visible#\_visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L20](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L20)  
> Since: 3.0.0

---

# Public Methods

## addedToScene

### <instance> addedToScene()

**Description:**

This callback is invoked when this Game Object is added to a Scene.

Can be overriden by custom Game Objects, but be aware of some Game Objects that

will use this, such as Sprites, to add themselves into the Update List.

You can also listen for the `ADDED_TO_SCENE` event from this Game Object.

> Source: [src/gameobjects/layer/Layer.js#L607](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L607)  
> Since: 3.50.0

---

## addToDisplayList

### <instance> addToDisplayList([displayList])

**Description:**

Adds this Layer to the given Display List.

If no Display List is specified, it will default to the Display List owned by the Scene to which

this Layer belongs.

A Layer can only exist on one Display List at any given time, but may move freely between them.

If this Layer is already on another Display List when this method is called, it will first

be removed from it, before being added to the new list.

You can query which list it is on by looking at the `Phaser.GameObjects.Layer#displayList` property.

If a Layer isn't on any display list, it will not be rendered. If you just wish to temporarily

disable it from rendering, consider using the `setVisible` method, instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| displayList | [Phaser.GameObjects.DisplayList](gameobjects-displaylist.md) | [Phaser.GameObjects.Layer](gameobjects-layer.md) | Yes | The Display List to add to. Defaults to the Scene Display List. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Layer instance.

**Fires:** [Phaser.Scenes.Events#event:ADDED\_TO\_SCENE](../event/scenes-events.md), [Phaser.GameObjects.Events#event:ADDED\_TO\_SCENE](../event/gameobjects-events.md)

> Source: [src/gameobjects/layer/Layer.js#L832](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L832)  
> Since: 3.60.0

---

## clearAlpha

### <instance> clearAlpha()

**Description:**

Clears all alpha values associated with this Game Object.

Immediately sets the alpha levels back to 1 (fully opaque).

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#clearAlpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L33](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L33)  
> Since: 3.0.0

---

## clearFX

### <instance> clearFX()

**Description:**

Removes all Pre and Post FX Controllers from this Game Object.

If you wish to remove a single controller, use the `preFX.remove(fx)` or `postFX.remove(fx)` methods instead.

If you wish to clear a single controller, use the `preFX.clear()` or `postFX.clear()` methods instead.

**Tags:**

* webglOnly

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#clearFX](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L337](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L337)  
> Since: 3.60.0

---

## clearMask

### <instance> clearMask([destroyMask])

**Description:**

Clears the mask that this Game Object was using.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| destroyMask | boolean | Yes | false | Destroy the mask before clearing it? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Mask#clearMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L56)  
> Since: 3.6.2

---

## createBitmapMask

### <instance> createBitmapMask([maskObject], [x], [y], [texture], [frame])

**Description:**

Creates and returns a Bitmap Mask. This mask can be used by any Game Object,

including this one, or a Dynamic Texture.

Note: Bitmap Masks only work on WebGL. Geometry Masks work on both WebGL and Canvas.

To create the mask you need to pass in a reference to a renderable Game Object.

A renderable Game Object is one that uses a texture to render with, such as an

Image, Sprite, Render Texture or BitmapText.

If you do not provide a renderable object, and this Game Object has a texture,

it will use itself as the object. This means you can call this method to create

a Bitmap Mask from any renderable texture-based Game Object.

**Tags:**

* generic
* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| maskObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | [Phaser.Textures.DynamicTexture](textures-dynamictexture.md) | Yes | The Game Object or Dynamic Texture that will be used as the mask. If `null` it will generate an Image Game Object using the rest of the arguments. |
| --- | --- | --- | --- |
| x | number | Yes | If creating a Game Object, the horizontal position in the world. |
| y | number | Yes | If creating a Game Object, the vertical position in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | Yes | If creating a Game Object, the key, or instance of the Texture it will use to render with, as stored in the Texture Manager. |
| frame | string | number | [Phaser.Textures.Frame](textures-frame.md) | Yes |

**Returns:** [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md) - This Bitmap Mask that was created.

**Inherits:** [Phaser.GameObjects.Components.Mask#createBitmapMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L80)  
> Since: 3.6.2

---

## createGeometryMask

### <instance> createGeometryMask([graphics])

**Description:**

Creates and returns a Geometry Mask. This mask can be used by any Game Object,

including this one.

To create the mask you need to pass in a reference to a Graphics Game Object.

If you do not provide a graphics object, and this Game Object is an instance

of a Graphics object, then it will use itself to create the mask.

This means you can call this method to create a Geometry Mask from any Graphics Game Object.

**Tags:**

* generic
* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | [Phaser.GameObjects.Shape](gameobjects-shape.md) | Yes | A Graphics Game Object, or any kind of Shape Game Object. The geometry within it will be used as the mask. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md) - This Geometry Mask that was created.

**Inherits:** [Phaser.GameObjects.Components.Mask#createGeometryMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L120)  
> Since: 3.6.2

---

## depthSort

### <instance> depthSort()

**Description:**

Immediately sorts the display list if the flag is set.

> Source: [src/gameobjects/layer/Layer.js#L785](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L785)  
> Since: 3.50.0

---

## destroy

### <instance> destroy([fromScene])

**Description:**

Destroys this Layer removing it from the Display List and Update List and

severing all ties to parent resources.

Also destroys all children of this Layer. If you do not wish for the

children to be destroyed, you should move them from this Layer first.

Use this to remove this Layer from your game if you don't ever plan to use it again.

As long as no reference to it exists within your own code it should become free for

garbage collection by the browser.

If you just want to temporarily disable an object then look at using the

Game Object Pool instead of destroying it, as destroyed objects cannot be resurrected.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| fromScene | boolean | Yes | false | `True` if this Game Object is being destroyed by the Scene, `false` if not. |
| --- | --- | --- | --- | --- |

**Fires:** [Phaser.GameObjects.Events#event:DESTROY](../event/gameobjects-events.md)

> Source: [src/gameobjects/layer/Layer.js#L921](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L921)  
> Since: 3.50.0

---

## disableInteractive

### <instance> disableInteractive()

**Description:**

A Layer cannot be enabled for input.

This method does nothing and is kept to ensure

the Layer has the same shape as a Game Object.

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This GameObject.

> Source: [src/gameobjects/layer/Layer.js#L575](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L575)  
> Since: 3.51.0

---

## getChildren

### <instance> getChildren()

**Description:**

Returns a reference to the array which contains all Game Objects in this Layer.

This is a reference, not a copy of it, so be very careful not to mutate it.

**Returns:** Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> - An array of Game Objects within this Layer.

> Source: [src/gameobjects/layer/Layer.js#L817](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L817)  
> Since: 3.50.0

---

## getData

### <instance> getData(key)

**Description:**

Retrieves the value for the given key in this Game Objects Data Manager, or undefined if it doesn't exist.

You can also access values via the `values` object. For example, if you had a key called `gold` you can do either:

```
Copy
sprite.getData('gold');


```

Or access the value directly:

```
Copy
sprite.data.values.gold;


```

You can also pass in an array of keys, in which case an array of values will be returned:

```
Copy
sprite.getData([ 'gold', 'armor', 'health' ]);


```

This approach is useful for destructuring arrays in ES6.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | Array.<string> | No | The key of the value to retrieve, or an array of keys. |
| --- | --- | --- | --- |

**Returns:** \* - The value belonging to the given key, or an array of values, the order of which will match the input array.

> Source: [src/gameobjects/layer/Layer.js#L519](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L519)  
> Since: 3.50.0

---

## getIndexList

### <instance> getIndexList()

**Description:**

Returns an array containing the display list index of either this Game Object, or if it has one,

its parent Container. It then iterates up through all of the parent containers until it hits the

root of the display list (which is index 0 in the returned array).

Used internally by the InputPlugin but also useful if you wish to find out the display depth of

this Game Object and all of its ancestors.

**Returns:** Array.<number> - An array of display list position indexes.

> Source: [src/gameobjects/layer/Layer.js#L678](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L678)  
> Since: 3.51.0

---

## getPostPipeline

### <instance> getPostPipeline(pipeline)

**Description:**

Gets a Post Pipeline instance from this Game Object, based on the given name, and returns it.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | string | function | [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md), Array.<[Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md)> - An array of all the Post Pipelines matching the name. This array will be empty if there was no match. If there was only one single match, that pipeline is returned directly, not in an array.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#getPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L237)  
> Since: 3.60.0

---

## incData

### <instance> incData(key, [data])

**Description:**

Increase a value for the given key within this Game Objects Data Manager. If the key doesn't already exist in the Data Manager then it is increased from 0.

If the Game Object has not been enabled for data (via `setDataEnabled`) then it will be enabled

before setting the value.

If the key doesn't already exist in the Data Manager then it is created.

When the value is first set, a `setdata` event is emitted from this Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | object | No | The key to increase the value for. |
| --- | --- | --- | --- |
| data | \* | Yes | The value to increase for the given key. |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This GameObject.

> Source: [src/gameobjects/layer/Layer.js#L460](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L460)  
> Since: 3.50.0

---

## initPostPipeline

### <instance> initPostPipeline([preFX])

**Description:**

This should only be called during the instantiation of the Game Object.

It is called by default by all core Game Objects and doesn't need

calling again.

After that, use `setPostPipeline`.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| preFX | boolean | Yes | false | Does this Game Object support Pre FX? |
| --- | --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#initPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L113)  
> Since: 3.60.0

---

## queueDepthSort

### <instance> queueDepthSort()

**Description:**

Force a sort of the display list on the next call to depthSort.

> Source: [src/gameobjects/layer/Layer.js#L774](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L774)  
> Since: 3.50.0

---

## removedFromScene

### <instance> removedFromScene()

**Description:**

This callback is invoked when this Game Object is removed from a Scene.

Can be overriden by custom Game Objects, but be aware of some Game Objects that

will use this, such as Sprites, to removed themselves from the Update List.

You can also listen for the `REMOVED_FROM_SCENE` event from this Game Object.

> Source: [src/gameobjects/layer/Layer.js#L622](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L622)  
> Since: 3.50.0

---

## removeFromDisplayList

### <instance> removeFromDisplayList()

**Description:**

Removes this Layer from the Display List it is currently on.

A Layer can only exist on one Display List at any given time, but may move freely removed

and added back at a later stage.

You can query which list it is on by looking at the `Phaser.GameObjects.GameObject#displayList` property.

If a Layer isn't on any Display List, it will not be rendered. If you just wish to temporarily

disable it from rendering, consider using the `setVisible` method, instead.

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Layer instance.

**Fires:** [Phaser.Scenes.Events#event:REMOVED\_FROM\_SCENE](../event/scenes-events.md), [Phaser.GameObjects.Events#event:REMOVED\_FROM\_SCENE](../event/gameobjects-events.md)

> Source: [src/gameobjects/layer/Layer.js#L883](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L883)  
> Since: 3.60.0

---

## removeInteractive

### <instance> removeInteractive()

**Description:**

A Layer cannot be enabled for input.

This method does nothing and is kept to ensure

the Layer has the same shape as a Game Object.

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This GameObject.

> Source: [src/gameobjects/layer/Layer.js#L591](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L591)  
> Since: 3.51.0

---

## removePostPipeline

### <instance> removePostPipeline(pipeline)

**Description:**

Removes a type of Post Pipeline instances from this Game Object, based on the given name, and destroys them.

If you wish to remove all Post Pipelines use the `resetPostPipeline` method instead.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | string | [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md) | No | The string-based name of the pipeline, or a pipeline class. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#removePostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L299](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L299)  
> Since: 3.60.0

---

## resetPostPipeline

### <instance> resetPostPipeline([resetData])

**Description:**

Resets the WebGL Post Pipelines of this Game Object. It does this by calling

the `destroy` method on each post pipeline and then clearing the local array.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetData | boolean | Yes | false | Reset the `postPipelineData` object to being an empty object? |
| --- | --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#resetPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L269](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L269)  
> Since: 3.60.0

---

## setAbove

### <instance> setAbove(gameObject)

**Description:**

Move this Game Object so that it appears above the given Game Object.

This means it will render immediately after the other object in the display list.

Both objects must belong to the same display list, or parent container.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object that this Game Object will be moved to be above. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setAbove](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L139)  
> Since: 3.85.0

---

## setActive

### <instance> setActive(value)

**Description:**

Sets the `active` property of this Game Object and returns this Game Object for further chaining.

A Game Object with its `active` property set to `true` will be updated by the Scenes UpdateList.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | True if this Game Object should be set as active, false if not. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This GameObject.

> Source: [src/gameobjects/layer/Layer.js#L322](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L322)  
> Since: 3.50.0

---

## setAlpha

### <instance> setAlpha([value])

**Description:**

Set the Alpha level of this Game Object. The alpha controls the opacity of the Game Object as it renders.

Alpha values are provided as a float between 0, fully transparent, and 1, fully opaque.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 1 | The alpha value applied across the whole Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#setAlpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L48)  
> Since: 3.0.0

---

## setBelow

### <instance> setBelow(gameObject)

**Description:**

Move this Game Object so that it appears below the given Game Object.

This means it will render immediately under the other object in the display list.

Both objects must belong to the same display list, or parent container.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object that this Game Object will be moved to be below. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setBelow](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L167)  
> Since: 3.85.0

---

## setBlendMode

### <instance> setBlendMode(value)

**Description:**

Sets the Blend Mode being used by this Game Object.

This can be a const, such as `Phaser.BlendModes.SCREEN`, or an integer, such as 4 (for Overlay)

Under WebGL only the following Blend Modes are available:

* NORMAL
* ADD
* MULTIPLY
* SCREEN
* ERASE (only works when rendering to a framebuffer, like a Render Texture)

Canvas has more available depending on browser support.

You can also create your own custom Blend Modes in WebGL.

Blend modes have different effects under Canvas and WebGL, and from browser to browser, depending

on support. Blend Modes also cause a WebGL batch flush should it encounter a new blend mode. For these

reasons try to be careful about the construction of your Scene and the frequency in which blend modes

are used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | string | [Phaser.BlendModes](../namespace/blendmodes.md) | number | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.BlendMode#setBlendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L80)  
> Since: 3.0.0

---

## setData

### <instance> setData(key, [data])

**Description:**

Allows you to store a key value pair within this Game Objects Data Manager.

If the Game Object has not been enabled for data (via `setDataEnabled`) then it will be enabled

before setting the value.

If the key doesn't already exist in the Data Manager then it is created.

```
Copy
sprite.setData('name', 'Red Gem Stone');


```

You can also pass in an object of key value pairs as the first argument:

```
Copy
sprite.setData({ name: 'Red Gem Stone', level: 2, owner: 'Link', gold: 50 });


```

To get a value back again you can call `getData`:

```
Copy
sprite.getData('gold');


```

Or you can access the value directly via the `values` property, where it works like any other variable:

```
Copy
sprite.data.values.gold += 50;


```

When the value is first set, a `setdata` event is emitted from this Game Object.

If the key already exists, a `changedata` event is emitted instead, along an event named after the key.

For example, if you updated an existing key called `PlayerLives` then it would emit the event `changedata-PlayerLives`.

These events will be emitted regardless if you use this method to set the value, or the direct `values` setter.

Please note that the data keys are case-sensitive and must be valid JavaScript Object property strings.

This means the keys `gold` and `Gold` are treated as two unique values within the Data Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | object | No | The key to set the value for. Or an object of key value pairs. If an object the `data` argument is ignored. |
| --- | --- | --- | --- |
| data | \* | Yes | The value to set for the given key. If an object is provided as the key this argument is ignored. |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This GameObject.

> Source: [src/gameobjects/layer/Layer.js#L401](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L401)  
> Since: 3.50.0

---

## setDataEnabled

### <instance> setDataEnabled()

**Description:**

Adds a Data Manager component to this Game Object.

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This GameObject.

> Source: [src/gameobjects/layer/Layer.js#L382](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L382)  
> Since: 3.50.0

---

## setDepth

### <instance> setDepth(value)

**Description:**

The depth of this Game Object within the Scene.

The depth is also known as the 'z-index' in some environments, and allows you to change the rendering order

of Game Objects, without actually moving their position in the display list.

The default depth is zero. A Game Object with a higher depth

value will always render in front of one with a lower value.

Setting the depth will queue a depth sort event within the Scene.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The depth of this Game Object. Ensure this value is only ever a number data-type. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setDepth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L64)  
> Since: 3.0.0

---

## setInteractive

### <instance> setInteractive()

**Description:**

A Layer cannot be enabled for input.

This method does nothing and is kept to ensure

the Layer has the same shape as a Game Object.

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This GameObject.

> Source: [src/gameobjects/layer/Layer.js#L559](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L559)  
> Since: 3.51.0

---

## setMask

### <instance> setMask(mask)

**Description:**

Sets the mask that this Game Object will use to render with.

The mask must have been previously created and can be either a GeometryMask or a BitmapMask.

Note: Bitmap Masks only work on WebGL. Geometry Masks work on both WebGL and Canvas.

If a mask is already set on this Game Object it will be immediately replaced.

Masks are positioned in global space and are not relative to the Game Object to which they

are applied. The reason for this is that multiple Game Objects can all share the same mask.

Masks have no impact on physics or input detection. They are purely a rendering component

that allows you to limit what is visible during the render pass.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mask | [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md) | [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md) | No | The mask this Game Object will use when rendering. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Mask#setMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L28](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L28)  
> Since: 3.6.2

---

## setName

### <instance> setName(value)

**Description:**

Sets the `name` property of this Game Object and returns this Game Object for further chaining.

The `name` property is not populated by Phaser and is presented for your own use.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | string | No | The name to be given to this Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This GameObject.

> Source: [src/gameobjects/layer/Layer.js#L340](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L340)  
> Since: 3.50.0

---

## setPostPipeline

### <instance> setPostPipeline(pipelines, [pipelineData], [copyData])

**Description:**

Sets one, or more, Post Pipelines on this Game Object.

Post Pipelines are invoked after this Game Object has rendered to its target and

are commonly used for post-fx.

The post pipelines are appended to the `postPipelines` array belonging to this

Game Object. When the renderer processes this Game Object, it iterates through the post

pipelines in the order in which they appear in the array. If you are stacking together

multiple effects, be aware that the order is important.

If you call this method multiple times, the new pipelines will be appended to any existing

post pipelines already set. Use the `resetPostPipeline` method to clear them first, if required.

You can optionally also set the `postPipelineData` property, if the parameter is given.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| pipelines | string | Array.<string> | function | Array.<function()> | [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md) |
| --- | --- | --- | --- | --- |
| pipelineData | object | Yes |  | Optional pipeline data object that is set in to the `postPipelineData` property of this Game Object. |
| copyData | boolean | Yes | true | Should the pipeline data object be *deep copied* into the `postPipelineData` property of this Game Object? If `false` it will be set by reference instead. |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#setPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L140)  
> Since: 3.60.0

---

## setPostPipelineData

### <instance> setPostPipelineData(key, [value])

**Description:**

Adds an entry to the `postPipelineData` object belonging to this Game Object.

If the 'key' already exists, its value is updated. If it doesn't exist, it is created.

If `value` is undefined, and `key` exists, `key` is removed from the data object.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the pipeline data to set, update, or delete. |
| --- | --- | --- | --- |
| value | any | Yes | The value to be set with the key. If `undefined` then `key` will be deleted from the object. |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#setPostPipelineData](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L205)  
> Since: 3.60.0

---

## setState

### <instance> setState(value)

**Description:**

Sets the current state of this Game Object.

Phaser itself will never modify the State of a Game Object, although plugins may do so.

For example, a Game Object could change from a state of 'moving', to 'attacking', to 'dead'.

The state value should typically be an integer (ideally mapped to a constant

in your game code), but could also be a string. It is recommended to keep it light and simple.

If you need to store complex data about your Game Object, look at using the Data Component instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | string | No | The state of the Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This GameObject.

> Source: [src/gameobjects/layer/Layer.js#L358](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L358)  
> Since: 3.50.0

---

## setToBack

### <instance> setToBack()

**Description:**

Sets this Game Object to the back of the display list, or the back of its parent container.

Being at the back means it will render below everything else.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setToBack](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L115)  
> Since: 3.85.0

---

## setToTop

### <instance> setToTop()

**Description:**

Sets this Game Object to be at the top of the display list, or the top of its parent container.

Being at the top means it will render on-top of everything else.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setToTop](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L91](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L91)  
> Since: 3.85.0

---

## setVisible

### <instance> setVisible(value)

**Description:**

Sets the visibility of this Game Object.

An invisible Game Object will skip rendering, but will still process update logic.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | The visible state of the Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Visible#setVisible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L63)  
> Since: 3.0.0

---

## sortByDepth

### <instance> sortByDepth(childA, childB)

**Description:**

Compare the depth of two Game Objects.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| childA | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The first Game Object. |
| --- | --- | --- | --- |
| childB | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The second Game Object. |

**Returns:** number - The difference between the depths of each Game Object.

> Source: [src/gameobjects/layer/Layer.js#L801](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L801)  
> Since: 3.50.0

---

## toggleData

### <instance> toggleData(key)

**Description:**

Toggle a boolean value for the given key within this Game Objects Data Manager. If the key doesn't already exist in the Data Manager then it is toggled from false.

If the Game Object has not been enabled for data (via `setDataEnabled`) then it will be enabled

before setting the value.

If the key doesn't already exist in the Data Manager then it is created.

When the value is first set, a `setdata` event is emitted from this Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | object | No | The key to toggle the value for. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - This GameObject.

> Source: [src/gameobjects/layer/Layer.js#L490](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L490)  
> Since: 3.50.0

---

## toJSON

### <instance> toJSON()

**Description:**

Returns a JSON representation of the Game Object.

**Returns:** [Phaser.Types.GameObjects.JSONGameObject](../typedef/types-gameobjects.md) - A JSON representation of the Game Object.

> Source: [src/gameobjects/layer/Layer.js#L649](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L649)  
> Since: 3.50.0

---

## update

### <instance> update([args])

**Description:**

To be overridden by custom GameObjects. Allows base objects to be used in a Pool.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| args | \* | Yes | args |
| --- | --- | --- | --- |

> Source: [src/gameobjects/layer/Layer.js#L637](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L637)  
> Since: 3.50.0

---

## willRender

### <instance> willRender(camera)

**Description:**

Compares the renderMask with the renderFlags to see if this Game Object will render or not.

Also checks the Game Object against the given Cameras exclusion list.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera to check against this Game Object. |
| --- | --- | --- | --- |

**Returns:** boolean - True if the Game Object should be rendered, otherwise false.

> Source: [src/gameobjects/layer/Layer.js#L662](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L662)  
> Since: 3.50.0

---

# Private Methods

## addChildCallback

### <instance> addChildCallback(gameObject)

**Description:**

Internal method called from `List.addCallback`.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object that was added to the list. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Scenes.Events#event:ADDED\_TO\_SCENE](../event/scenes-events.md), [Phaser.GameObjects.Events#event:ADDED\_TO\_SCENE](../event/gameobjects-events.md)

> Source: [src/gameobjects/layer/Layer.js#L720](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L720)  
> Since: 3.50.0

---

## removeChildCallback

### <instance> removeChildCallback(gameObject)

**Description:**

Internal method called from `List.removeCallback`.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object that was removed from the list. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Scenes.Events#event:REMOVED\_FROM\_SCENE](../event/scenes-events.md), [Phaser.GameObjects.Events#event:REMOVED\_FROM\_SCENE](../event/gameobjects-events.md)

> Source: [src/gameobjects/layer/Layer.js#L752](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/Layer.js#L752)  
> Since: 3.50.0

---

## renderCanvas

### <instance> renderCanvas(renderer, layer, camera)

**Description:**

Renders this Game Object with the Canvas Renderer to the given Camera.

The object will not render if any of its renderFlags are set or it is being actively filtered out by the Camera.

This method should not be called directly. It is a utility function of the Render module.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) | No | A reference to the current active Canvas renderer. |
| --- | --- | --- | --- |
| layer | [Phaser.GameObjects.Layer](gameobjects-layer.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |

> Source: [src/gameobjects/layer/LayerCanvasRenderer.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/LayerCanvasRenderer.js#L7)  
> Since: 3.50.0

---

## renderWebGL

### <instance> renderWebGL(renderer, layer, camera)

**Description:**

Renders this Game Object with the WebGL Renderer to the given Camera.

The object will not render if any of its renderFlags are set or it is being actively filtered out by the Camera.

This method should not be called directly. It is a utility function of the Render module.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) | No | A reference to the current active WebGL renderer. |
| --- | --- | --- | --- |
| layer | [Phaser.GameObjects.Layer](gameobjects-layer.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |

> Source: [src/gameobjects/layer/LayerWebGLRenderer.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/LayerWebGLRenderer.js#L7)  
> Since: 3.50.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [active](#active)

    - [active: boolean](#active-boolean)
  + [alpha](#alpha)

    - [alpha: number](#alpha-number)
  + [blendMode](#blendmode)

    - [blendMode: Phaser.BlendModes, string, number](#blendmode-phaserblendmodes-string-number)
  + [body](#body)

    - [body: Phaser.Physics.Arcade.Body, Phaser.Physics.Arcade.StaticBody, MatterJS.BodyType](#body-phaserphysicsarcadebody-phaserphysicsarcadestaticbody-matterjsbodytype)
  + [cameraFilter](#camerafilter)

    - [cameraFilter: number](#camerafilter-number)
  + [data](#data)

    - [data: Phaser.Data.DataManager](#data-phaserdatadatamanager)
  + [depth](#depth)

    - [depth: number](#depth-number)
  + [displayList](#displaylist)

    - [displayList: Phaser.GameObjects.DisplayList, Phaser.GameObjects.Layer](#displaylist-phasergameobjectsdisplaylist-phasergameobjectslayer)
  + [events](#events)

    - [events: Phaser.Events.EventEmitter](#events-phasereventseventemitter)
  + [hasPostPipeline](#haspostpipeline)

    - [hasPostPipeline: boolean](#haspostpipeline-boolean)
  + [ignoreDestroy](#ignoredestroy)

    - [ignoreDestroy: boolean](#ignoredestroy-boolean)
  + [input](#input)

    - [input: Phaser.Types.Input.InteractiveObject](#input-phasertypesinputinteractiveobject)
  + [mask](#mask)

    - [mask: Phaser.Display.Masks.BitmapMask, Phaser.Display.Masks.GeometryMask](#mask-phaserdisplaymasksbitmapmask-phaserdisplaymasksgeometrymask)
  + [name](#name)

    - [name: string](#name-string)
  + [parentContainer](#parentcontainer)

    - [parentContainer: Phaser.GameObjects.Container](#parentcontainer-phasergameobjectscontainer)
  + [postFX](#postfx)

    - [postFX: Phaser.GameObjects.Components.FX](#postfx-phasergameobjectscomponentsfx)
  + [postPipelineData](#postpipelinedata)

    - [postPipelineData: object](#postpipelinedata-object)
  + [postPipelines](#postpipelines)

    - [postPipelines: Array.<Phaser.Renderer.WebGL.Pipelines.PostFXPipeline>](#postpipelines-arrayphaserrendererwebglpipelinespostfxpipeline)
  + [preFX](#prefx)

    - [preFX: Phaser.GameObjects.Components.FX](#prefx-phasergameobjectscomponentsfx)
  + [renderFlags](#renderflags)

    - [renderFlags: number](#renderflags-number)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [sortChildrenFlag](#sortchildrenflag)

    - [sortChildrenFlag: boolean](#sortchildrenflag-boolean)
  + [state](#state)

    - [state: number, string](#state-number-string)
  + [systems](#systems)

    - [systems: Phaser.Scenes.Systems](#systems-phaserscenessystems)
  + [tabIndex](#tabindex)

    - [tabIndex: number](#tabindex-number)
  + [type](#type)

    - [type: string](#type-string)
  + [visible](#visible)

    - [visible: boolean](#visible-boolean)
* [Private Members](#private-members)

  + [\_alpha](#_alpha)

    - [\_alpha: number](#_alpha-number)
  + [\_blendMode](#_blendmode)

    - [\_blendMode: number](#_blendmode-number)
  + [\_depth](#_depth)

    - [\_depth: number](#_depth-number)
  + [\_visible](#_visible)

    - [\_visible: boolean](#_visible-boolean)
* [Public Methods](#public-methods)

  + [addedToScene](#addedtoscene)

    - [<instance> addedToScene()](#instance-addedtoscene)
  + [addToDisplayList](#addtodisplaylist)

    - [<instance> addToDisplayList([displayList])](#instance-addtodisplaylistdisplaylist)
  + [clearAlpha](#clearalpha)

    - [<instance> clearAlpha()](#instance-clearalpha)
  + [clearFX](#clearfx)

    - [<instance> clearFX()](#instance-clearfx)
  + [clearMask](#clearmask)

    - [<instance> clearMask([destroyMask])](#instance-clearmaskdestroymask)
  + [createBitmapMask](#createbitmapmask)

    - [<instance> createBitmapMask([maskObject], [x], [y], [texture], [frame])](#instance-createbitmapmaskmaskobject-x-y-texture-frame)
  + [createGeometryMask](#creategeometrymask)

    - [<instance> createGeometryMask([graphics])](#instance-creategeometrymaskgraphics)
  + [depthSort](#depthsort)

    - [<instance> depthSort()](#instance-depthsort)
  + [destroy](#destroy)

    - [<instance> destroy([fromScene])](#instance-destroyfromscene)
  + [disableInteractive](#disableinteractive)

    - [<instance> disableInteractive()](#instance-disableinteractive)
  + [getChildren](#getchildren)

    - [<instance> getChildren()](#instance-getchildren)
  + [getData](#getdata)

    - [<instance> getData(key)](#instance-getdatakey)
  + [getIndexList](#getindexlist)

    - [<instance> getIndexList()](#instance-getindexlist)
  + [getPostPipeline](#getpostpipeline)

    - [<instance> getPostPipeline(pipeline)](#instance-getpostpipelinepipeline)
  + [incData](#incdata)

    - [<instance> incData(key, [data])](#instance-incdatakey-data)
  + [initPostPipeline](#initpostpipeline)

    - [<instance> initPostPipeline([preFX])](#instance-initpostpipelineprefx)
  + [queueDepthSort](#queuedepthsort)

    - [<instance> queueDepthSort()](#instance-queuedepthsort)
  + [removedFromScene](#removedfromscene)

    - [<instance> removedFromScene()](#instance-removedfromscene)
  + [removeFromDisplayList](#removefromdisplaylist)

    - [<instance> removeFromDisplayList()](#instance-removefromdisplaylist)
  + [removeInteractive](#removeinteractive)

    - [<instance> removeInteractive()](#instance-removeinteractive)
  + [removePostPipeline](#removepostpipeline)

    - [<instance> removePostPipeline(pipeline)](#instance-removepostpipelinepipeline)
  + [resetPostPipeline](#resetpostpipeline)

    - [<instance> resetPostPipeline([resetData])](#instance-resetpostpipelineresetdata)
  + [setAbove](#setabove)

    - [<instance> setAbove(gameObject)](#instance-setabovegameobject)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)
  + [setAlpha](#setalpha)

    - [<instance> setAlpha([value])](#instance-setalphavalue)
  + [setBelow](#setbelow)

    - [<instance> setBelow(gameObject)](#instance-setbelowgameobject)
  + [setBlendMode](#setblendmode)

    - [<instance> setBlendMode(value)](#instance-setblendmodevalue)
  + [setData](#setdata)

    - [<instance> setData(key, [data])](#instance-setdatakey-data)
  + [setDataEnabled](#setdataenabled)

    - [<instance> setDataEnabled()](#instance-setdataenabled)
  + [setDepth](#setdepth)

    - [<instance> setDepth(value)](#instance-setdepthvalue)
  + [setInteractive](#setinteractive)

    - [<instance> setInteractive()](#instance-setinteractive)
  + [setMask](#setmask)

    - [<instance> setMask(mask)](#instance-setmaskmask)
  + [setName](#setname)

    - [<instance> setName(value)](#instance-setnamevalue)
  + [setPostPipeline](#setpostpipeline)

    - [<instance> setPostPipeline(pipelines, [pipelineData], [copyData])](#instance-setpostpipelinepipelines-pipelinedata-copydata)
  + [setPostPipelineData](#setpostpipelinedata)

    - [<instance> setPostPipelineData(key, [value])](#instance-setpostpipelinedatakey-value)
  + [setState](#setstate)

    - [<instance> setState(value)](#instance-setstatevalue)
  + [setToBack](#settoback)

    - [<instance> setToBack()](#instance-settoback)
  + [setToTop](#settotop)

    - [<instance> setToTop()](#instance-settotop)
  + [setVisible](#setvisible)

    - [<instance> setVisible(value)](#instance-setvisiblevalue)
  + [sortByDepth](#sortbydepth)

    - [<instance> sortByDepth(childA, childB)](#instance-sortbydepthchilda-childb)
  + [toggleData](#toggledata)

    - [<instance> toggleData(key)](#instance-toggledatakey)
  + [toJSON](#tojson)

    - [<instance> toJSON()](#instance-tojson)
  + [update](#update)

    - [<instance> update([args])](#instance-updateargs)
  + [willRender](#willrender)

    - [<instance> willRender(camera)](#instance-willrendercamera)
* [Private Methods](#private-methods)

  + [addChildCallback](#addchildcallback)

    - [<instance> addChildCallback(gameObject)](#instance-addchildcallbackgameobject)
  + [removeChildCallback](#removechildcallback)

    - [<instance> removeChildCallback(gameObject)](#instance-removechildcallbackgameobject)
  + [renderCanvas](#rendercanvas)

    - [<instance> renderCanvas(renderer, layer, camera)](#instance-rendercanvasrenderer-layer-camera)
  + [renderWebGL](#renderwebgl)

    - [<instance> renderWebGL(renderer, layer, camera)](#instance-renderwebglrenderer-layer-camera)

Back to top

©2025[Phaser](https://docs.phaser.io)