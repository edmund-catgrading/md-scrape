# Container

Phaser.GameObjects.Container

A Container Game Object.

A Container, as the name implies, can 'contain' other types of Game Object.

When a Game Object is added to a Container, the Container becomes responsible for the rendering of it.

By default it will be removed from the Display List and instead added to the Containers own internal list.

The position of the Game Object automatically becomes relative to the position of the Container.

The transform point of a Container is 0x0 (in local space) and that cannot be changed. The children you add to the

Container should be positioned with this value in mind. I.e. you should treat 0x0 as being the center of

the Container, and position children positively and negative around it as required.

When the Container is rendered, all of its children are rendered as well, in the order in which they exist

within the Container. Container children can be repositioned using methods such as `MoveUp`, `MoveDown` and `SendToBack`.

If you modify a transform property of the Container, such as `Container.x` or `Container.rotation` then it will

automatically influence all children as well.

Containers can include other Containers for deeply nested transforms.

Containers can have masks set on them and can be used as a mask too. However, Container children cannot be masked.

The masks do not 'stack up'. Only a Container on the root of the display list will use its mask.

Containers can be enabled for input. Because they do not have a texture you need to provide a shape for them

to use as their hit area. Container children can also be enabled for input, independent of the Container.

If input enabling a *child* you should not set both the `origin` and a **negative** scale factor on the child,

or the input area will become misaligned.

Containers can be given a physics body for either Arcade Physics, Impact Physics or Matter Physics. However,

if Container *children* are enabled for physics you may get unexpected results, such as offset bodies,

if the Container itself, or any of its ancestors, is positioned anywhere other than at 0 x 0. Container children

with physics do not factor in the Container due to the excessive extra calculations needed. Please structure

your game to work around this.

It's important to understand the impact of using Containers. They add additional processing overhead into

every one of their children. The deeper you nest them, the more the cost escalates. This is especially true

for input events. You also lose the ability to set the display depth of Container children in the same

flexible manner as those not within them. In short, don't use them for the sake of it. You pay a small cost

every time you create one, try to structure your game around avoiding that where possible.

**Constructor**

`new Container(scene, [x], [y], [children])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No |  | The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time. |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| children | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | Yes |  | An optional array of Game Objects to add to this Container. |

---

**Scope**: static

**Extends**

> [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)  
> [Phaser.GameObjects.Components.AlphaSingle](../namespace/gameobjects-components-alphasingle.md)  
> [Phaser.GameObjects.Components.BlendMode](../namespace/gameobjects-components-blendmode.md)  
> [Phaser.GameObjects.Components.ComputedSize](../namespace/gameobjects-components-computedsize.md)  
> [Phaser.GameObjects.Components.Depth](../namespace/gameobjects-components-depth.md)  
> [Phaser.GameObjects.Components.Mask](../namespace/gameobjects-components-mask.md)  
> [Phaser.GameObjects.Components.PostPipeline](../namespace/gameobjects-components-postpipeline.md)  
> [Phaser.GameObjects.Components.Transform](../namespace/gameobjects-components-transform.md)  
> [Phaser.GameObjects.Components.Visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/container/Container.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L21)  
> Since: 3.4.0

# Public Members

## active

### active: boolean

**Description:**

The active state of this Game Object.

A Game Object with an active state of `true` is processed by the Scenes UpdateList, if added to it.

An active object is one which is having its logic and internal systems updated.

**Inherits:** [Phaser.GameObjects.GameObject#active](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L113)  
> Since: 3.0.0

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

## angle

### angle: number

**Description:**

The angle of this Game Object as expressed in degrees.

Phaser uses a right-hand clockwise rotation system, where 0 is right, 90 is down, 180/-180 is left

and -90 is up.

If you prefer to work in radians, see the `rotation` property instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#angle](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L211](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L211)  
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

If this Game Object is enabled for Arcade or Matter Physics then this property will contain a reference to a Physics Body.

**Inherits:** [Phaser.GameObjects.GameObject#body](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L186](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L186)  
> Since: 3.0.0

---

## cameraFilter

### cameraFilter: number

**Description:**

A bitmask that controls if this Game Object is drawn by a Camera or not.

Not usually set directly, instead call `Camera.ignore`, however you can

set this property directly using the Camera.id property:

**Inherits:** [Phaser.GameObjects.GameObject#cameraFilter](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L160](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L160)  
> Since: 3.0.0

---

## data

### data: [Phaser.Data.DataManager](data-datamanager.md)

**Description:**

A Data Manager.

It allows you to store, query and get key/value paired information specific to this Game Object.

`null` by default. Automatically created if you use `getData` or `setData` or `setDataEnabled`.

**Inherits:** [Phaser.GameObjects.GameObject#data](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L136)  
> Since: 3.0.0

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

## displayHeight

### displayHeight: number

**Description:**

The displayed height of this Game Object.

This value takes into account the scale factor.

Setting this value will adjust the Game Object's scale property.

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#displayHeight](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L68)  
> Since: 3.0.0

---

## displayList

### displayList: [Phaser.GameObjects.DisplayList](gameobjects-displaylist.md), [Phaser.GameObjects.Layer](gameobjects-layer.md)

**Description:**

Holds a reference to the Display List that contains this Game Object.

This is set automatically when this Game Object is added to a Scene or Layer.

You should treat this property as being read-only.

**Inherits:** [Phaser.GameObjects.GameObject#displayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L53)  
> Since: 3.50.0

---

## displayOriginX

### displayOriginX: number

**Description:**

Internal value to allow Containers to be used for input and physics.

Do not change this value. It has no effect other than to break things.

> Source: [src/gameobjects/container/Container.js#L289](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L289)  
> Since: 3.4.0

---

## displayOriginY

### displayOriginY: number

**Description:**

Internal value to allow Containers to be used for input and physics.

Do not change this value. It has no effect other than to break things.

> Source: [src/gameobjects/container/Container.js#L308](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L308)  
> Since: 3.4.0

---

## displayWidth

### displayWidth: number

**Description:**

The displayed width of this Game Object.

This value takes into account the scale factor.

Setting this value will adjust the Game Object's scale property.

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#displayWidth](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L43)  
> Since: 3.0.0

---

## exclusive

### exclusive: boolean

**Description:**

Does this Container exclusively manage its children?

The default is `true` which means a child added to this Container cannot

belong in another Container, which includes the Scene display list.

If you disable this then this Container will no longer exclusively manage its children.

This allows you to create all kinds of interesting graphical effects, such as replicating

Game Objects without reparenting them all over the Scene.

However, doing so will prevent children from receiving any kind of input event or have

their physics bodies work by default, as they're no longer a single entity on the

display list, but are being replicated where-ever this Container is.

> Source: [src/gameobjects/container/Container.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L115)  
> Since: 3.4.0

---

## first

### first: [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)

**Description:**

Returns the first Game Object within the Container, or `null` if it is empty.

You can move the cursor by calling `Container.next` and `Container.previous`.

> Source: [src/gameobjects/container/Container.js#L1322](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1322)  
> Since: 3.4.0

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

## hasTransformComponent

### hasTransformComponent: boolean

**Description:**

A property indicating that a Game Object has this component.

**Inherits:** [Phaser.GameObjects.Components.Transform#hasTransformComponent](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L26](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L26)  
> Since: 3.60.0

---

## height

### height: number

**Description:**

The native (un-scaled) height of this Game Object.

Changing this value will not change the size that the Game Object is rendered in-game.

For that you need to either set the scale of the Game Object (`setScale`) or use

the `displayHeight` property.

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#height](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L30)  
> Since: 3.0.0

---

## ignoreDestroy

### ignoreDestroy: boolean

**Description:**

This Game Object will ignore all calls made to its destroy method if this flag is set to `true`.

This includes calls that may come from a Group, Container or the Scene itself.

While it allows you to persist a Game Object across Scenes, please understand you are entirely

responsible for managing references to and from this Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#ignoreDestroy](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L196](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L196)  
> Since: 3.5.0

---

## input

### input: [Phaser.Types.Input.InteractiveObject](../typedef/types-input.md)

**Description:**

If this Game Object is enabled for input then this property will contain an InteractiveObject instance.

Not usually set directly. Instead call `GameObject.setInteractive()`.

**Inherits:** [Phaser.GameObjects.GameObject#input](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L175](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L175)  
> Since: 3.0.0

---

## last

### last: [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)

**Description:**

Returns the last Game Object within the Container, or `null` if it is empty.

You can move the cursor by calling `Container.next` and `Container.previous`.

> Source: [src/gameobjects/container/Container.js#L1350](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1350)  
> Since: 3.4.0

---

## length

### length: number

**Description:**

The number of Game Objects inside this Container.

> Source: [src/gameobjects/container/Container.js#L1305](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1305)  
> Since: 3.4.0

---

## list

### list: Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)>

**Description:**

An array holding the children of this Container.

> Source: [src/gameobjects/container/Container.js#L106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L106)  
> Since: 3.4.0

---

## localTransform

### localTransform: [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md)

**Description:**

Internal Transform Matrix used for local space conversion.

> Source: [src/gameobjects/container/Container.js#L156](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L156)  
> Since: 3.4.0

---

## mask

### mask: [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md), [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md)

**Description:**

The Mask this Game Object is using during render.

**Inherits:** [Phaser.GameObjects.Components.Mask#mask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L19)  
> Since: 3.0.0

---

## maxSize

### maxSize: number

**Description:**

Containers can have an optional maximum size. If set to anything above 0 it

will constrict the addition of new Game Objects into the Container, capping off

the maximum limit the Container can grow in size to.

> Source: [src/gameobjects/container/Container.js#L135](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L135)  
> Since: 3.4.0

---

## name

### name: string

**Description:**

The name of this Game Object.

Empty by default and never populated by Phaser, this is left for developers to use.

**Inherits:** [Phaser.GameObjects.GameObject#name](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L102)  
> Since: 3.0.0

---

## next

### next: [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)

**Description:**

Returns the next Game Object within the Container, or `null` if it is empty.

You can move the cursor by calling `Container.next` and `Container.previous`.

> Source: [src/gameobjects/container/Container.js#L1378](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1378)  
> Since: 3.4.0

---

## originX

### originX: number

**Description:**

Internal value to allow Containers to be used for input and physics.

Do not change this value. It has no effect other than to break things.

> Source: [src/gameobjects/container/Container.js#L251](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L251)  
> Since: 3.4.0

---

## originY

### originY: number

**Description:**

Internal value to allow Containers to be used for input and physics.

Do not change this value. It has no effect other than to break things.

> Source: [src/gameobjects/container/Container.js#L270](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L270)  
> Since: 3.4.0

---

## parentContainer

### parentContainer: [Phaser.GameObjects.Container](gameobjects-container.md)

**Description:**

The parent Container of this Game Object, if it has one.

**Inherits:** [Phaser.GameObjects.GameObject#parentContainer](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L93)  
> Since: 3.4.0

---

## position

### position: number

**Description:**

The cursor position.

> Source: [src/gameobjects/container/Container.js#L147](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L147)  
> Since: 3.4.0

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

## previous

### previous: [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)

**Description:**

Returns the previous Game Object within the Container, or `null` if it is empty.

You can move the cursor by calling `Container.next` and `Container.previous`.

> Source: [src/gameobjects/container/Container.js#L1406](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1406)  
> Since: 3.4.0

---

## renderFlags

### renderFlags: number

**Description:**

The flags that are compared against `RENDER_MASK` to determine if this Game Object will render or not.

The bits are 0001 | 0010 | 0100 | 1000 set by the components Visible, Alpha, Transform and Texture respectively.

If those components are not used by your custom class then you can use this bitmask as you wish.

**Inherits:** [Phaser.GameObjects.GameObject#renderFlags](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L148)  
> Since: 3.0.0

---

## rotation

### rotation: number

**Description:**

The angle of this Game Object in radians.

Phaser uses a right-hand clockwise rotation system, where 0 is right, PI/2 is down, +-PI is left

and -PI/2 is up.

If you prefer to work in degrees, see the `angle` property instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#rotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L238](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L238)  
> Since: 3.0.0

---

## scale

### scale: number

**Description:**

This is a special setter that allows you to set both the horizontal and vertical scale of this Game Object

to the same value, at the same time. When reading this value the result returned is `(scaleX + scaleY) / 2`.

Use of this property implies you wish the horizontal and vertical scales to be equal to each other. If this

isn't the case, use the `scaleX` or `scaleY` properties instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#scale](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L113)  
> Since: 3.18.0

---

## scaleX

### scaleX: number

**Description:**

The horizontal scale of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#scaleX](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L149)  
> Since: 3.0.0

---

## scaleY

### scaleY: number

**Description:**

The vertical scale of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#scaleY](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L180](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L180)  
> Since: 3.0.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

A reference to the Scene to which this Game Object belongs.

Game Objects can only belong to one Scene.

You should consider this property as being read-only. You cannot move a

Game Object to another Scene by simply changing it.

**Inherits:** [Phaser.GameObjects.GameObject#scene](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L39)  
> Since: 3.0.0

---

## scrollFactorX

### scrollFactorX: number

**Description:**

The horizontal scroll factor of this Container.

The scroll factor controls the influence of the movement of a Camera upon this Container.

When a camera scrolls it will change the location at which this Container is rendered on-screen.

It does not change the Containers actual position values.

For a Container, setting this value will only update the Container itself, not its children.

If you wish to change the scrollFactor of the children as well, use the `setScrollFactor` method.

A value of 1 means it will move exactly in sync with a camera.

A value of 0 means it will not move at all, even if the camera moves.

Other values control the degree to which the camera movement is mapped to this Container.

Please be aware that scroll factor values other than 1 are not taken in to consideration when

calculating physics collisions. Bodies always collide based on their world position, but changing

the scroll factor is a visual adjustment to where the textures are rendered, which can offset

them from physics bodies if not accounted for in your code.

> Source: [src/gameobjects/container/Container.js#L185](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L185)  
> Since: 3.4.0

---

## scrollFactorY

### scrollFactorY: number

**Description:**

The vertical scroll factor of this Container.

The scroll factor controls the influence of the movement of a Camera upon this Container.

When a camera scrolls it will change the location at which this Container is rendered on-screen.

It does not change the Containers actual position values.

For a Container, setting this value will only update the Container itself, not its children.

If you wish to change the scrollFactor of the children as well, use the `setScrollFactor` method.

A value of 1 means it will move exactly in sync with a camera.

A value of 0 means it will not move at all, even if the camera moves.

Other values control the degree to which the camera movement is mapped to this Container.

Please be aware that scroll factor values other than 1 are not taken in to consideration when

calculating physics collisions. Bodies always collide based on their world position, but changing

the scroll factor is a visual adjustment to where the textures are rendered, which can offset

them from physics bodies if not accounted for in your code.

> Source: [src/gameobjects/container/Container.js#L212](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L212)  
> Since: 3.4.0

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

**Inherits:** [Phaser.GameObjects.GameObject#state](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L77)  
> Since: 3.16.0

---

## tabIndex

### tabIndex: number

**Description:**

The Tab Index of the Game Object.

Reserved for future use by plugins and the Input Manager.

**Inherits:** [Phaser.GameObjects.GameObject#tabIndex](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L125](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L125)  
> Since: 3.0.0

---

## type

### type: string

**Description:**

A textual representation of this Game Object, i.e. `sprite`.

Used internally by Phaser but is available for your own custom classes to populate.

**Inherits:** [Phaser.GameObjects.GameObject#type](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L67](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L67)  
> Since: 3.0.0

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

## w

### w: number

**Description:**

The w position of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#w](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L103)  
> Since: 3.0.0

---

## width

### width: number

**Description:**

The native (un-scaled) width of this Game Object.

Changing this value will not change the size that the Game Object is rendered in-game.

For that you need to either set the scale of the Game Object (`setScale`) or use

the `displayWidth` property.

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#width](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L17)  
> Since: 3.0.0

---

## x

### x: number

**Description:**

The x position of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#x](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L70)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y position of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#y](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L80)  
> Since: 3.0.0

---

## z

### z: number

**Description:**

The z position of this Game Object.

Note: The z position does not control the rendering order of 2D Game Objects. Use

[Phaser.GameObjects.Components.Depth#depth](../namespace/gameobjects-components-depth.md) instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#z](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L90)  
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

## \_rotation

### \_rotation: number

**Description:**

Private internal value. Holds the rotation value in radians.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Transform#\_rotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L59)  
> Since: 3.0.0

---

## \_scaleX

### \_scaleX: number

**Description:**

Private internal value. Holds the horizontal scale value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Transform#\_scaleX](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L37)  
> Since: 3.0.0

---

## \_scaleY

### \_scaleY: number

**Description:**

Private internal value. Holds the vertical scale value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Transform#\_scaleY](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L48)  
> Since: 3.0.0

---

## \_sortKey

### \_sortKey: string

**Description:**

The property key to sort by.

**Access:** private

> Source: [src/gameobjects/container/Container.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L165)  
> Since: 3.4.0

---

## \_sysEvents

### \_sysEvents: [Phaser.Events.EventEmitter](events-eventemitter.md)

**Description:**

A reference to the Scene Systems Event Emitter.

**Access:** private

> Source: [src/gameobjects/container/Container.js#L175](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L175)  
> Since: 3.9.0

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

## add

### <instance> add(child)

**Description:**

Adds the given Game Object, or array of Game Objects, to this Container.

Each Game Object must be unique within the Container.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No | The Game Object, or array of Game Objects, to add to the Container. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L526](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L526)  
> Since: 3.4.0

---

## addAt

### <instance> addAt(child, [index])

**Description:**

Adds the given Game Object, or array of Game Objects, to this Container at the specified position.

Existing Game Objects in the Container are shifted up.

Each Game Object must be unique within the Container.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No |  | The Game Object, or array of Game Objects, to add to the Container. |
| --- | --- | --- | --- | --- |
| index | number | Yes | 0 | The position to insert the Game Object/s at. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L548](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L548)  
> Since: 3.4.0

---

## addedToScene

### <instance> addedToScene()

**Description:**

This callback is invoked when this Game Object is added to a Scene.

Can be overriden by custom Game Objects, but be aware of some Game Objects that

will use this, such as Sprites, to add themselves into the Update List.

You can also listen for the `ADDED_TO_SCENE` event from this Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#addedToScene](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L562](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L562)  
> Since: 3.50.0

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## addToDisplayList

### <instance> addToDisplayList([displayList])

**Description:**

Adds this Game Object to the given Display List.

If no Display List is specified, it will default to the Display List owned by the Scene to which

this Game Object belongs.

A Game Object can only exist on one Display List at any given time, but may move freely between them.

If this Game Object is already on another Display List when this method is called, it will first

be removed from it, before being added to the new list.

You can query which list it is on by looking at the `Phaser.GameObjects.GameObject#displayList` property.

If a Game Object isn't on any display list, it will not be rendered. If you just wish to temporarly

disable it from rendering, consider using the `setVisible` method, instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| displayList | [Phaser.GameObjects.DisplayList](gameobjects-displaylist.md) | [Phaser.GameObjects.Layer](gameobjects-layer.md) | Yes | The Display List to add to. Defaults to the Scene Display List. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object.

**Fires:** [Phaser.Scenes.Events#event:ADDED\_TO\_SCENE](../event/scenes-events.md), [Phaser.GameObjects.Events#event:ADDED\_TO\_SCENE](../event/gameobjects-events.md)

**Inherits:** [Phaser.GameObjects.GameObject#addToDisplayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L684](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L684)  
> Since: 3.53.0

---

## addToUpdateList

### <instance> addToUpdateList()

**Description:**

Adds this Game Object to the Update List belonging to the Scene.

When a Game Object is added to the Update List it will have its `preUpdate` method called

every game frame. This method is passed two parameters: `delta` and `time`.

If you wish to run your own logic within `preUpdate` then you should always call

`super.preUpdate(delta, time)` within it, or it may fail to process required operations,

such as Sprite animations.

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#addToUpdateList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L735](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L735)  
> Since: 3.53.0

---

## bringToTop

### <instance> bringToTop(child)

**Description:**

Brings the given Game Object to the top of this Container.

This will cause it to render on-top of any other objects in the Container.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to bring to the top of the Container. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L989](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L989)  
> Since: 3.4.0

---

## clearAlpha

### <instance> clearAlpha()

**Description:**

Clears all alpha values associated with this Game Object.

Immediately sets the alpha levels back to 1 (fully opaque).

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object.

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Mask#clearMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L56)  
> Since: 3.6.2

---

## copyPosition

### <instance> copyPosition(source)

**Description:**

Copies an object's coordinates to this Game Object's position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | [Phaser.Types.Math.Vector3Like](../typedef/types-math.md) | [Phaser.Types.Math.Vector4Like](../typedef/types-math.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#copyPosition](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L293](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L293)  
> Since: 3.50.0

---

## count

### <instance> count(property, value, [startIndex], [endIndex])

**Description:**

Returns the total number of Game Objects in this Container that have a property

matching the given value.

For example: `count('visible', true)` would count all the elements that have their visible property set.

You can optionally limit the operation to the `startIndex` - `endIndex` range.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| property | string | No |  | The property to check. |
| --- | --- | --- | --- | --- |
| value | any | No |  | The value to check. |
| startIndex | number | Yes | 0 | An optional start index to search from. |
| endIndex | number | Yes | "Container.length" | An optional end index to search up to (but not included) |

**Returns:** number - The total number of Game Objects in this Container with a property matching the given value.

> Source: [src/gameobjects/container/Container.js#L740](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L740)  
> Since: 3.4.0

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

## destroy

### <instance> destroy([fromScene])

**Description:**

Destroys this Game Object removing it from the Display List and Update List and

severing all ties to parent resources.

Also removes itself from the Input Manager and Physics Manager if previously enabled.

Use this to remove a Game Object from your game if you don't ever plan to use it again.

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

**Inherits:** [Phaser.GameObjects.GameObject#destroy](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L855](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L855)  
> Since: 3.0.0

---

## disableInteractive

### <instance> disableInteractive([resetCursor])

**Description:**

If this Game Object has previously been enabled for input, this will disable it.

An object that is disabled for input stops processing or being considered for

input events, but can be turned back on again at any time by simply calling

`setInteractive()` with no arguments provided.

If want to completely remove interaction from this Game Object then use `removeInteractive` instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetCursor | boolean | Yes | false | Should the currently active Input cursor, if any, be reset to the default cursor? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#disableInteractive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L494](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L494)  
> Since: 3.7.0

---

## each

### <instance> each(callback, [context], [args])

**Description:**

Passes all Game Objects in this Container to the given callback.

A copy of the Container is made before passing each entry to your callback.

This protects against the callback itself modifying the Container.

If you know for sure that the callback will not change the size of this Container

then you can use the more performant `Container.iterate` method instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | function | No | The function to call. |
| --- | --- | --- | --- |
| context | object | Yes | Value to use as `this` when executing callback. |
| args | \* | Yes | Additional arguments that will be passed to the callback, after the child. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L1187](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1187)  
> Since: 3.4.0

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

**Inherits:** [Phaser.Events.EventEmitter#emit](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L86)  
> Since: 3.0.0

---

## eventNames

### <instance> eventNames()

**Description:**

Return an array listing the events for which the emitter has registered listeners.

**Returns:** Array.<(string | symbol)> - undefined

**Inherits:** [Phaser.Events.EventEmitter#eventNames](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L55)  
> Since: 3.0.0

---

## exists

### <instance> exists(child)

**Description:**

Returns `true` if the given Game Object is a direct child of this Container.

This check does not scan nested Containers.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to check for within this Container. |
| --- | --- | --- | --- |

**Returns:** boolean - True if the Game Object is an immediate child of this Container, otherwise false.

> Source: [src/gameobjects/container/Container.js#L1135](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1135)  
> Since: 3.4.0

---

## getAll

### <instance> getAll([property], [value], [startIndex], [endIndex])

**Description:**

Returns all Game Objects in this Container.

You can optionally specify a matching criteria using the `property` and `value` arguments.

For example: `getAll('body')` would return only Game Objects that have a body property.

You can also specify a value to compare the property to:

`getAll('visible', true)` would return only Game Objects that have their visible property set to `true`.

Optionally you can specify a start and end index. For example if this Container had 100 Game Objects,

and you set `startIndex` to 0 and `endIndex` to 50, it would return matches from only

the first 50 Game Objects.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| property | string | Yes |  | The property to test on each Game Object in the Container. |
| --- | --- | --- | --- | --- |
| value | any | Yes |  | If property is set then the `property` must strictly equal this value to be included in the results. |
| startIndex | number | Yes | 0 | An optional start index to search from. |
| endIndex | number | Yes | "Container.length" | An optional end index to search up to (but not included) |

**Returns:** Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> - An array of matching Game Objects from this Container.

> Source: [src/gameobjects/container/Container.js#L707](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L707)  
> Since: 3.4.0

---

## getAt

### <instance> getAt(index)

**Description:**

Returns the Game Object at the given position in this Container.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| index | number | No | The position to get the Game Object from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) - The Game Object at the specified index, or `null` if none found.

> Source: [src/gameobjects/container/Container.js#L573](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L573)  
> Since: 3.4.0

---

## getBounds

### <instance> getBounds([output])

**Description:**

Gets the bounds of this Container. It works by iterating all children of the Container,

getting their respective bounds, and then working out a min-max rectangle from that.

It does not factor in if the children render or not, all are included.

Some children are unable to return their bounds, such as Graphics objects, in which case

they are skipped.

Depending on the quantity of children in this Container it could be a really expensive call,

so cache it and only poll it as needed.

The values are stored and returned in a Rectangle object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| output | [Phaser.Geom.Rectangle](geom-rectangle.md) | Yes | A Geom.Rectangle object to store the values in. If not provided a new Rectangle will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The values stored in the output object.

> Source: [src/gameobjects/container/Container.js#L356](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L356)  
> Since: 3.4.0

---

## getBoundsTransformMatrix

### <instance> getBoundsTransformMatrix()

**Description:**

Returns the world transform matrix as used for Bounds checks.

The returned matrix is temporal and shouldn't be stored.

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - The world transform matrix.

> Source: [src/gameobjects/container/Container.js#L511](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L511)  
> Since: 3.4.0

---

## getByName

### <instance> getByName(name)

**Description:**

Searches for the first instance of a child with its `name` property matching the given argument.

Should more than one child have the same name only the first is returned.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name to search for. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) - The first child with a matching name, or `null` if none were found.

> Source: [src/gameobjects/container/Container.js#L641](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L641)  
> Since: 3.4.0

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

**Inherits:** [Phaser.GameObjects.GameObject#getData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L416](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L416)  
> Since: 3.0.0

---

## getDisplayList

### <instance> getDisplayList()

**Description:**

Returns a reference to the underlying display list *array* that contains this Game Object,

which will be either the Scene's Display List or the internal list belonging

to its parent Container, if it has one.

If this Game Object is not on a display list or in a container, it will return `null`.

You should be very careful with this method, and understand that it returns a direct reference to the

internal array used by the Display List. Mutating this array directly can cause all kinds of subtle

and difficult to debug issues in your game.

**Returns:** Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> - The internal Display List array of Game Objects, or `null`.

**Inherits:** [Phaser.GameObjects.GameObject#getDisplayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L823](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L823)  
> Since: 3.85.0

---

## getFirst

### <instance> getFirst(property, value, [startIndex], [endIndex])

**Description:**

Gets the first Game Object in this Container.

You can also specify a property and value to search for, in which case it will return the first

Game Object in this Container with a matching property and / or value.

For example: `getFirst('visible', true)` would return the first Game Object that had its `visible` property set.

You can limit the search to the `startIndex` - `endIndex` range.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| property | string | No |  | The property to test on each Game Object in the Container. |
| --- | --- | --- | --- | --- |
| value | \* | No |  | The value to test the property against. Must pass a strict (`===`) comparison check. |
| startIndex | number | Yes | 0 | An optional start index to search from. |
| endIndex | number | Yes | "Container.length" | An optional end index to search up to (but not included) |

**Returns:** [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) - The first matching Game Object, or `null` if none was found.

> Source: [src/gameobjects/container/Container.js#L679](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L679)  
> Since: 3.4.0

---

## getIndex

### <instance> getIndex(child)

**Description:**

Returns the index of the given Game Object in this Container.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to search for in this Container. |
| --- | --- | --- | --- |

**Returns:** number - The index of the Game Object in this Container, or -1 if not found.

> Source: [src/gameobjects/container/Container.js#L591](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L591)  
> Since: 3.4.0

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

**Inherits:** [Phaser.GameObjects.GameObject#getIndexList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L635](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L635)  
> Since: 3.4.0

---

## getLocalPoint

### <instance> getLocalPoint(x, y, [point], [camera])

**Description:**

Takes the given `x` and `y` coordinates and converts them into local space for this

Game Object, taking into account parent and local transforms, and the Display Origin.

The returned Vector2 contains the translated point in its properties.

A Camera needs to be provided in order to handle modified scroll factors. If no

camera is specified, it will use the `main` camera from the Scene to which this

Game Object belongs.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position to translate. |
| --- | --- | --- | --- |
| y | number | No | The y position to translate. |
| point | [Phaser.Math.Vector2](math-vector2.md) | Yes | A Vector2, or point-like object, to store the results in. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera which is being tested against. If not given will use the Scene default camera. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The translated point.

**Inherits:** [Phaser.GameObjects.Components.Transform#getLocalPoint](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L542](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L542)  
> Since: 3.50.0

---

## getLocalTransformMatrix

### <instance> getLocalTransformMatrix([tempMatrix])

**Description:**

Gets the local transform matrix for this Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tempMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | Yes | The matrix to populate with the values from this Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - The populated Transform Matrix.

**Inherits:** [Phaser.GameObjects.Components.Transform#getLocalTransformMatrix](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L484](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L484)  
> Since: 3.4.0

---

## getParentRotation

### <instance> getParentRotation()

**Description:**

Gets the sum total rotation of all of this Game Objects parent Containers.

The returned value is in radians and will be zero if this Game Object has no parent container.

**Returns:** number - The sum total rotation, in radians, of all parent containers of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#getParentRotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L592](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L592)  
> Since: 3.18.0

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

## getRandom

### <instance> getRandom([startIndex], [length])

**Description:**

Returns a random Game Object from this Container.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| startIndex | number | Yes | 0 | An optional start index. |
| --- | --- | --- | --- | --- |
| length | number | Yes |  | An optional length, the total number of elements (from the startIndex) to choose from. |

**Returns:** [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) - A random child from the Container, or `null` if the Container is empty.

> Source: [src/gameobjects/container/Container.js#L660](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L660)  
> Since: 3.4.0

---

## getWorldTransformMatrix

### <instance> getWorldTransformMatrix([tempMatrix], [parentMatrix])

**Description:**

Gets the world transform matrix for this Game Object, factoring in any parent Containers.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tempMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | Yes | The matrix to populate with the values from this Game Object. |
| --- | --- | --- | --- |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | Yes | A temporary matrix to hold parent values during the calculations. |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - The populated Transform Matrix.

**Inherits:** [Phaser.GameObjects.Components.Transform#getWorldTransformMatrix](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L501](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L501)  
> Since: 3.4.0

---

## incData

### <instance> incData(key, [amount])

**Description:**

Increase a value for the given key within this Game Objects Data Manager. If the key doesn't already exist in the Data Manager then it is increased from 0.

If the Game Object has not been enabled for data (via `setDataEnabled`) then it will be enabled

before setting the value.

If the key doesn't already exist in the Data Manager then it is created.

When the value is first set, a `setdata` event is emitted from this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key to change the value for. |
| --- | --- | --- | --- | --- |
| amount | number | Yes | 1 | The amount to increase the given key by. Pass a negative value to decrease the key. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#incData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L357](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L357)  
> Since: 3.23.0

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

## iterate

### <instance> iterate(callback, [context], [args])

**Description:**

Passes all Game Objects in this Container to the given callback.

Only use this method when you absolutely know that the Container will not be modified during

the iteration, i.e. by removing or adding to its contents.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | function | No | The function to call. |
| --- | --- | --- | --- |
| context | object | Yes | Value to use as `this` when executing callback. |
| args | \* | Yes | Additional arguments that will be passed to the callback, after the child. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L1227](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1227)  
> Since: 3.4.0

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

**Inherits:** [Phaser.Events.EventEmitter#listenerCount](events-eventemitter.md)

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

**Inherits:** [Phaser.Events.EventEmitter#listeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L64)  
> Since: 3.0.0

---

## moveAbove

### <instance> moveAbove(child1, child2)

**Description:**

Moves a Game Object above another one within this Container.

If the Game Object is already above the other, it isn't moved.

These 2 Game Objects must already be children of this Container.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child1 | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to move above base Game Object. |
| --- | --- | --- | --- |
| child2 | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The base Game Object. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L811](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L811)  
> Since: 3.55.0

---

## moveBelow

### <instance> moveBelow(child1, child2)

**Description:**

Moves a Game Object below another one within this Container.

If the Game Object is already below the other, it isn't moved.

These 2 Game Objects must already be children of this Container.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child1 | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to move below base Game Object. |
| --- | --- | --- | --- |
| child2 | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The base Game Object. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L835](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L835)  
> Since: 3.55.0

---

## moveDown

### <instance> moveDown(child)

**Description:**

Moves the given Game Object down one place in this Container, unless it's already at the bottom.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to be moved in the Container. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L1051](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1051)  
> Since: 3.4.0

---

## moveTo

### <instance> moveTo(child, index)

**Description:**

Moves a Game Object to a new position within this Container.

The Game Object must already be a child of this Container.

The Game Object is removed from its old position and inserted into the new one.

Therefore the Container size does not change. Other children will change position accordingly.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to move. |
| --- | --- | --- | --- |
| index | number | No | The new position of the Game Object in this Container. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L785](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L785)  
> Since: 3.4.0

---

## moveUp

### <instance> moveUp(child)

**Description:**

Moves the given Game Object up one place in this Container, unless it's already at the top.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to be moved in the Container. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L1031](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1031)  
> Since: 3.4.0

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#off](events-eventemitter.md)

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#on](events-eventemitter.md)

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## onChildDestroyed

### <instance> onChildDestroyed()

**Description:**

Internal handler, called when a child is destroyed.

**Access:** protected

> Source: [src/gameobjects/container/Container.js#L1450](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1450)  
> Since: 3.80.0

---

## pointToContainer

### <instance> pointToContainer(source, [output])

**Description:**

Takes a Point-like object, such as a Vector2, Geom.Point or object with public x and y properties,

and transforms it into the space of this Container, then returns it in the output object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | The Source Point to be transformed. |
| --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes | A destination object to store the transformed point in. If none given a Vector2 will be created and returned. |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The transformed point.

> Source: [src/gameobjects/container/Container.js#L473](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L473)  
> Since: 3.4.0

---

## preDestroy

### <instance> preDestroy()

**Description:**

Internal destroy handler, called as part of the destroy process.

**Access:** protected

> Source: [src/gameobjects/container/Container.js#L1434](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1434)  
> Since: 3.9.0

---

## remove

### <instance> remove(child, [destroyChild])

**Description:**

Removes the given Game Object, or array of Game Objects, from this Container.

The Game Objects must already be children of this Container.

You can also optionally call `destroy` on each Game Object that is removed from the Container.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No |  | The Game Object, or array of Game Objects, to be removed from the Container. |
| --- | --- | --- | --- | --- |
| destroyChild | boolean | Yes | false | Optionally call `destroy` on each child successfully removed from this Container. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L859](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L859)  
> Since: 3.4.0

---

## removeAll

### <instance> removeAll([destroyChild])

**Description:**

Removes all Game Objects from this Container.

You can also optionally call `destroy` on each Game Object that is removed from the Container.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| destroyChild | boolean | Yes | false | Optionally call `destroy` on each Game Object successfully removed from this Container. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L951](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L951)  
> Since: 3.4.0

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeAt

### <instance> removeAt(index, [destroyChild])

**Description:**

Removes the Game Object at the given position in this Container.

You can also optionally call `destroy` on the Game Object, if one is found.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| index | number | No |  | The index of the Game Object to be removed. |
| --- | --- | --- | --- | --- |
| destroyChild | boolean | Yes | false | Optionally call `destroy` on the Game Object if successfully removed from this Container. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L897](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L897)  
> Since: 3.4.0

---

## removeBetween

### <instance> removeBetween([startIndex], [endIndex], [destroyChild])

**Description:**

Removes the Game Objects between the given positions in this Container.

You can also optionally call `destroy` on each Game Object that is removed from the Container.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| startIndex | number | Yes | 0 | An optional start index to search from. |
| --- | --- | --- | --- | --- |
| endIndex | number | Yes | "Container.length" | An optional end index to search up to (but not included) |
| destroyChild | boolean | Yes | false | Optionally call `destroy` on each Game Object successfully removed from this Container. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L922](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L922)  
> Since: 3.4.0

---

## removedFromScene

### <instance> removedFromScene()

**Description:**

This callback is invoked when this Game Object is removed from a Scene.

Can be overriden by custom Game Objects, but be aware of some Game Objects that

will use this, such as Sprites, to removed themselves from the Update List.

You can also listen for the `REMOVED_FROM_SCENE` event from this Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#removedFromScene](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L577](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L577)  
> Since: 3.50.0

---

## removeFromDisplayList

### <instance> removeFromDisplayList()

**Description:**

Removes this Game Object from the Display List it is currently on.

A Game Object can only exist on one Display List at any given time, but may move freely removed

and added back at a later stage.

You can query which list it is on by looking at the `Phaser.GameObjects.GameObject#displayList` property.

If a Game Object isn't on any Display List, it will not be rendered. If you just wish to temporarly

disable it from rendering, consider using the `setVisible` method, instead.

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object.

**Fires:** [Phaser.Scenes.Events#event:REMOVED\_FROM\_SCENE](../event/scenes-events.md), [Phaser.GameObjects.Events#event:REMOVED\_FROM\_SCENE](../event/gameobjects-events.md)

**Inherits:** [Phaser.GameObjects.GameObject#removeFromDisplayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L760](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L760)  
> Since: 3.53.0

---

## removeFromUpdateList

### <instance> removeFromUpdateList()

**Description:**

Removes this Game Object from the Scene's Update List.

When a Game Object is on the Update List, it will have its `preUpdate` method called

every game frame. Calling this method will remove it from the list, preventing this.

Removing a Game Object from the Update List will stop most internal functions working.

For example, removing a Sprite from the Update List will prevent it from being able to

run animations.

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#removeFromUpdateList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L798](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L798)  
> Since: 3.53.0

---

## removeInteractive

### <instance> removeInteractive([resetCursor])

**Description:**

If this Game Object has previously been enabled for input, this will queue it

for removal, causing it to no longer be interactive. The removal happens on

the next game step, it is not immediate.

The Interactive Object that was assigned to this Game Object will be destroyed,

removed from the Input Manager and cleared from this Game Object.

If you wish to re-enable this Game Object at a later date you will need to

re-create its InteractiveObject by calling `setInteractive` again.

If you wish to only temporarily stop an object from receiving input then use

`disableInteractive` instead, as that toggles the interactive state, where-as

this erases it completely.

If you wish to resize a hit area, don't remove and then set it as being

interactive. Instead, access the hitarea object directly and resize the shape

being used. I.e.: `sprite.input.hitArea.setSize(width, height)` (assuming the

shape is a Rectangle, which it is by default.)

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetCursor | boolean | Yes | false | Should the currently active Input cursor, if any, be reset to the default cursor? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#removeInteractive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L519](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L519)  
> Since: 3.7.0

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#removePostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L299](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L299)  
> Since: 3.60.0

---

## replace

### <instance> replace(oldChild, newChild, [destroyChild])

**Description:**

Replaces a Game Object in this Container with the new Game Object.

The new Game Object cannot already be a child of this Container.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| oldChild | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | The Game Object in this Container that will be replaced. |
| --- | --- | --- | --- | --- |
| newChild | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | The Game Object to be added to this Container. |
| destroyChild | boolean | Yes | false | Optionally call `destroy` on the Game Object if successfully removed from this Container. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L1101](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1101)  
> Since: 3.4.0

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

## reverse

### <instance> reverse()

**Description:**

Reverses the order of all Game Objects in this Container.

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L1071](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1071)  
> Since: 3.4.0

---

## sendToBack

### <instance> sendToBack(child)

**Description:**

Sends the given Game Object to the bottom of this Container.

This will cause it to render below any other objects in the Container.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to send to the bottom of the Container. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L1010](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1010)  
> Since: 3.4.0

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setActive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L216](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L216)  
> Since: 3.0.0

---

## setAll

### <instance> setAll(property, value, [startIndex], [endIndex])

**Description:**

Sets the property to the given value on all Game Objects in this Container.

Optionally you can specify a start and end index. For example if this Container had 100 Game Objects,

and you set `startIndex` to 0 and `endIndex` to 50, it would return matches from only

the first 50 Game Objects.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| property | string | No |  | The property that must exist on the Game Object. |
| --- | --- | --- | --- | --- |
| value | any | No |  | The value to get the property to. |
| startIndex | number | Yes | 0 | An optional start index to search from. |
| endIndex | number | Yes | "Container.length" | An optional end index to search up to (but not included) |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L1155](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1155)  
> Since: 3.4.0

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#setAlpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L48)  
> Since: 3.0.0

---

## setAngle

### <instance> setAngle([degrees])

**Description:**

Sets the angle of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| degrees | number | Yes | 0 | The rotation of this Game Object, in degrees. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setAngle](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L364](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L364)  
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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

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

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | object | No | The key to set the value for. Or an object of key value pairs. If an object the `data` argument is ignored. |
| --- | --- | --- | --- |
| data | \* | Yes | The value to set for the given key. If an object is provided as the key this argument is ignored. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L295](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L295)  
> Since: 3.0.0

---

## setDataEnabled

### <instance> setDataEnabled()

**Description:**

Adds a Data Manager component to this Game Object.

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setDataEnabled](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L276](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L276)  
> Since: 3.0.0

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setDepth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L64)  
> Since: 3.0.0

---

## setDisplaySize

### <instance> setDisplaySize(width, height)

**Description:**

Sets the display size of this Game Object.

Calling this will adjust the scale.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The width of this Game Object. |
| --- | --- | --- | --- |
| height | number | No | The height of this Game Object. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#setDisplaySize](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L120)  
> Since: 3.4.0

---

## setExclusive

### <instance> setExclusive([value])

**Description:**

Does this Container exclusively manage its children?

The default is `true` which means a child added to this Container cannot

belong in another Container, which includes the Scene display list.

If you disable this then this Container will no longer exclusively manage its children.

This allows you to create all kinds of interesting graphical effects, such as replicating

Game Objects without reparenting them all over the Scene.

However, doing so will prevent children from receiving any kind of input event or have

their physics bodies work by default, as they're no longer a single entity on the

display list, but are being replicated where-ever this Container is.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | The exclusive state of this Container. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container.

> Source: [src/gameobjects/container/Container.js#L327](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L327)  
> Since: 3.4.0

---

## setInteractive

### <instance> setInteractive([hitArea], [callback], [dropZone])

**Description:**

Pass this Game Object to the Input Manager to enable it for Input.

Input works by using hit areas, these are nearly always geometric shapes, such as rectangles or circles, that act as the hit area

for the Game Object. However, you can provide your own hit area shape and callback, should you wish to handle some more advanced

input detection.

If no arguments are provided it will try and create a rectangle hit area based on the texture frame the Game Object is using. If

this isn't a texture-bound object, such as a Graphics or BitmapText object, this will fail, and you'll need to provide a specific

shape for it to use.

You can also provide an Input Configuration Object as the only argument to this method.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| hitArea | [Phaser.Types.Input.InputConfiguration](../typedef/types-input.md) | any | Yes |  | Either an input configuration object, or a geometric shape that defines the hit area for the Game Object. If not given it will try to create a Rectangle based on the texture frame. |
| --- | --- | --- | --- | --- |
| callback | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | Yes |  | The callback that determines if the pointer is within the Hit Area shape or not. If you provide a shape you must also provide a callback. |
| dropZone | boolean | Yes | false | Should this Game Object be treated as a drop zone target? |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setInteractive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L456](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L456)  
> Since: 3.0.0

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setName](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L234](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L234)  
> Since: 3.0.0

---

## setPosition

### <instance> setPosition([x], [y], [z], [w])

**Description:**

Sets the position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x position of this Game Object. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The y position of this Game Object. If not set it will use the `x` value. |
| z | number | Yes | 0 | The z position of this Game Object. |
| w | number | Yes | 0 | The w position of this Game Object. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setPosition](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L265](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L265)  
> Since: 3.0.0

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#setPostPipelineData](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L205)  
> Since: 3.60.0

---

## setRandomPosition

### <instance> setRandomPosition([x], [y], [width], [height])

**Description:**

Sets the position of this Game Object to be a random position within the confines of

the given area.

If no area is specified a random position between 0 x 0 and the game width x height is used instead.

The position does not factor in the size of this Game Object, meaning that only the origin is

guaranteed to be within the area.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x position of the top-left of the random area. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y position of the top-left of the random area. |
| width | number | Yes |  | The width of the random area. |
| height | number | Yes |  | The height of the random area. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setRandomPosition](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L313](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L313)  
> Since: 3.8.0

---

## setRotation

### <instance> setRotation([radians])

**Description:**

Sets the rotation of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| radians | number | Yes | 0 | The rotation of this Game Object, in radians. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setRotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L345](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L345)  
> Since: 3.0.0

---

## setScale

### <instance> setScale([x], [y])

**Description:**

Sets the scale of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 1 | The horizontal scale of this Game Object. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical scale of this Game Object. If not set it will use the `x` value. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setScale](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L383](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L383)  
> Since: 3.0.0

---

## setScrollFactor

### <instance> setScrollFactor(x, [y], [updateChildren])

**Description:**

Sets the scroll factor of this Container and optionally all of its children.

The scroll factor controls the influence of the movement of a Camera upon this Game Object.

When a camera scrolls it will change the location at which this Game Object is rendered on-screen.

It does not change the Game Objects actual position values.

A value of 1 means it will move exactly in sync with a camera.

A value of 0 means it will not move at all, even if the camera moves.

Other values control the degree to which the camera movement is mapped to this Game Object.

Please be aware that scroll factor values other than 1 are not taken in to consideration when

calculating physics collisions. Bodies always collide based on their world position, but changing

the scroll factor is a visual adjustment to where the textures are rendered, which can offset

them from physics bodies if not accounted for in your code.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal scroll factor of this Game Object. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical scroll factor of this Game Object. If not set it will use the `x` value. |
| updateChildren | boolean | Yes | false | Apply this scrollFactor to all Container children as well? |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

> Source: [src/gameobjects/container/Container.js#L1262](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1262)  
> Since: 3.4.0

---

## setSize

### <instance> setSize(width, height)

**Description:**

Sets the internal size of this Game Object, as used for frame or physics body creation.

This will not change the size that the Game Object is rendered in-game.

For that you need to either set the scale of the Game Object (`setScale`) or call the

`setDisplaySize` method, which is the same thing as changing the scale but allows you

to do so by giving pixel values.

If you have enabled this Game Object for input, changing the size will *not* change the

size of the hit area. To do this you should adjust the `input.hitArea` object directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The width of this Game Object. |
| --- | --- | --- | --- |
| height | number | No | The height of this Game Object. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#setSize](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L93)  
> Since: 3.4.0

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setState](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L252](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L252)  
> Since: 3.16.0

---

## setToBack

### <instance> setToBack()

**Description:**

Sets this Game Object to the back of the display list, or the back of its parent container.

Being at the back means it will render below everything else.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Visible#setVisible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L63)  
> Since: 3.0.0

---

## setW

### <instance> setW([value])

**Description:**

Sets the w position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The w position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setW](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L465](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L465)  
> Since: 3.0.0

---

## setX

### <instance> setX([value])

**Description:**

Sets the x position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The x position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setX](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L405](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L405)  
> Since: 3.0.0

---

## setY

### <instance> setY([value])

**Description:**

Sets the y position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The y position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setY](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L424](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L424)  
> Since: 3.0.0

---

## setZ

### <instance> setZ([value])

**Description:**

Sets the z position of this Game Object.

Note: The z position does not control the rendering order of 2D Game Objects. Use

[Phaser.GameObjects.Components.Depth#setDepth](../namespace/gameobjects-components-depth.md) instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The z position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setZ](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L443](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L443)  
> Since: 3.0.0

---

## shuffle

### <instance> shuffle()

**Description:**

Shuffles the all Game Objects in this Container using the Fisher-Yates implementation.

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L1086](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L1086)  
> Since: 3.4.0

---

## shutdown

### <instance> shutdown()

**Description:**

Removes all listeners.

**Inherits:** [Phaser.Events.EventEmitter#shutdown](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L31)  
> Since: 3.0.0

---

## sort

### <instance> sort(property, [handler])

**Description:**

Sort the contents of this Container so the items are in order based on the given property.

For example: `sort('alpha')` would sort the elements based on the value of their `alpha` property.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| property | string | No | The property to lexically sort by. |
| --- | --- | --- | --- |
| handler | function | Yes | Provide your own custom handler function. Will receive 2 children which it should compare and return a boolean. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L609](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L609)  
> Since: 3.4.0

---

## swap

### <instance> swap(child1, child2)

**Description:**

Swaps the position of two Game Objects in this Container.

Both Game Objects must belong to this Container.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child1 | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The first Game Object to swap. |
| --- | --- | --- | --- |
| child2 | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The second Game Object to swap. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This Container instance.

> Source: [src/gameobjects/container/Container.js#L763](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L763)  
> Since: 3.4.0

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
| key | string | No | The key to toggle the value for. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#toggleData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L387](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L387)  
> Since: 3.23.0

---

## toJSON

### <instance> toJSON()

**Description:**

Returns a JSON representation of the Game Object.

**Returns:** [Phaser.Types.GameObjects.JSONGameObject](../typedef/types-gameobjects.md) - A JSON representation of the Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#toJSON](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L604](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L604)  
> Since: 3.0.0

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

**Inherits:** [Phaser.GameObjects.GameObject#update](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L592](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L592)  
> Since: 3.0.0

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

**Inherits:** [Phaser.GameObjects.GameObject#willRender](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L617](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L617)  
> Since: 3.0.0

---

# Private Methods

## addHandler

### <instance> addHandler(gameObject)

**Description:**

Internal add handler.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object that was just added to this Container. |
| --- | --- | --- | --- |

> Source: [src/gameobjects/container/Container.js#L422](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L422)  
> Since: 3.4.0

---

## removeHandler

### <instance> removeHandler(gameObject)

**Description:**

Internal remove handler.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object that was just removed from this Container. |
| --- | --- | --- | --- |

> Source: [src/gameobjects/container/Container.js#L450](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/Container.js#L450)  
> Since: 3.4.0

---

## renderCanvas

### <instance> renderCanvas(renderer, container, camera, parentMatrix)

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
| container | [Phaser.GameObjects.Container](gameobjects-container.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | No | This transform matrix is defined if the game object is nested |

> Source: [src/gameobjects/container/ContainerCanvasRenderer.js#L8](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/ContainerCanvasRenderer.js#L8)  
> Since: 3.4.0

---

## renderWebGL

### <instance> renderWebGL(renderer, container, camera, parentMatrix)

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
| container | [Phaser.GameObjects.Container](gameobjects-container.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | No | This transform matrix is defined if the game object is nested |

> Source: [src/gameobjects/container/ContainerWebGLRenderer.js#L8](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/ContainerWebGLRenderer.js#L8)  
> Since: 3.4.0

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
  + [angle](#angle)

    - [angle: number](#angle-number)
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
  + [displayHeight](#displayheight)

    - [displayHeight: number](#displayheight-number)
  + [displayList](#displaylist)

    - [displayList: Phaser.GameObjects.DisplayList, Phaser.GameObjects.Layer](#displaylist-phasergameobjectsdisplaylist-phasergameobjectslayer)
  + [displayOriginX](#displayoriginx)

    - [displayOriginX: number](#displayoriginx-number)
  + [displayOriginY](#displayoriginy)

    - [displayOriginY: number](#displayoriginy-number)
  + [displayWidth](#displaywidth)

    - [displayWidth: number](#displaywidth-number)
  + [exclusive](#exclusive)

    - [exclusive: boolean](#exclusive-boolean)
  + [first](#first)

    - [first: Phaser.GameObjects.GameObject](#first-phasergameobjectsgameobject)
  + [hasPostPipeline](#haspostpipeline)

    - [hasPostPipeline: boolean](#haspostpipeline-boolean)
  + [hasTransformComponent](#hastransformcomponent)

    - [hasTransformComponent: boolean](#hastransformcomponent-boolean)
  + [height](#height)

    - [height: number](#height-number)
  + [ignoreDestroy](#ignoredestroy)

    - [ignoreDestroy: boolean](#ignoredestroy-boolean)
  + [input](#input)

    - [input: Phaser.Types.Input.InteractiveObject](#input-phasertypesinputinteractiveobject)
  + [last](#last)

    - [last: Phaser.GameObjects.GameObject](#last-phasergameobjectsgameobject)
  + [length](#length)

    - [length: number](#length-number)
  + [list](#list)

    - [list: Array.<Phaser.GameObjects.GameObject>](#list-arrayphasergameobjectsgameobject)
  + [localTransform](#localtransform)

    - [localTransform: Phaser.GameObjects.Components.TransformMatrix](#localtransform-phasergameobjectscomponentstransformmatrix)
  + [mask](#mask)

    - [mask: Phaser.Display.Masks.BitmapMask, Phaser.Display.Masks.GeometryMask](#mask-phaserdisplaymasksbitmapmask-phaserdisplaymasksgeometrymask)
  + [maxSize](#maxsize)

    - [maxSize: number](#maxsize-number)
  + [name](#name)

    - [name: string](#name-string)
  + [next](#next)

    - [next: Phaser.GameObjects.GameObject](#next-phasergameobjectsgameobject)
  + [originX](#originx)

    - [originX: number](#originx-number)
  + [originY](#originy)

    - [originY: number](#originy-number)
  + [parentContainer](#parentcontainer)

    - [parentContainer: Phaser.GameObjects.Container](#parentcontainer-phasergameobjectscontainer)
  + [position](#position)

    - [position: number](#position-number)
  + [postFX](#postfx)

    - [postFX: Phaser.GameObjects.Components.FX](#postfx-phasergameobjectscomponentsfx)
  + [postPipelineData](#postpipelinedata)

    - [postPipelineData: object](#postpipelinedata-object)
  + [postPipelines](#postpipelines)

    - [postPipelines: Array.<Phaser.Renderer.WebGL.Pipelines.PostFXPipeline>](#postpipelines-arrayphaserrendererwebglpipelinespostfxpipeline)
  + [preFX](#prefx)

    - [preFX: Phaser.GameObjects.Components.FX](#prefx-phasergameobjectscomponentsfx)
  + [previous](#previous)

    - [previous: Phaser.GameObjects.GameObject](#previous-phasergameobjectsgameobject)
  + [renderFlags](#renderflags)

    - [renderFlags: number](#renderflags-number)
  + [rotation](#rotation)

    - [rotation: number](#rotation-number)
  + [scale](#scale)

    - [scale: number](#scale-number)
  + [scaleX](#scalex)

    - [scaleX: number](#scalex-number)
  + [scaleY](#scaley)

    - [scaleY: number](#scaley-number)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [scrollFactorX](#scrollfactorx)

    - [scrollFactorX: number](#scrollfactorx-number)
  + [scrollFactorY](#scrollfactory)

    - [scrollFactorY: number](#scrollfactory-number)
  + [state](#state)

    - [state: number, string](#state-number-string)
  + [tabIndex](#tabindex)

    - [tabIndex: number](#tabindex-number)
  + [type](#type)

    - [type: string](#type-string)
  + [visible](#visible)

    - [visible: boolean](#visible-boolean)
  + [w](#w)

    - [w: number](#w-number)
  + [width](#width)

    - [width: number](#width-number)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
  + [z](#z)

    - [z: number](#z-number)
* [Private Members](#private-members)

  + [\_alpha](#_alpha)

    - [\_alpha: number](#_alpha-number)
  + [\_blendMode](#_blendmode)

    - [\_blendMode: number](#_blendmode-number)
  + [\_depth](#_depth)

    - [\_depth: number](#_depth-number)
  + [\_rotation](#_rotation)

    - [\_rotation: number](#_rotation-number)
  + [\_scaleX](#_scalex)

    - [\_scaleX: number](#_scalex-number)
  + [\_scaleY](#_scaley)

    - [\_scaleY: number](#_scaley-number)
  + [\_sortKey](#_sortkey)

    - [\_sortKey: string](#_sortkey-string)
  + [\_sysEvents](#_sysevents)

    - [\_sysEvents: Phaser.Events.EventEmitter](#_sysevents-phasereventseventemitter)
  + [\_visible](#_visible)

    - [\_visible: boolean](#_visible-boolean)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(child)](#instance-addchild)
  + [addAt](#addat)

    - [<instance> addAt(child, [index])](#instance-addatchild-index)
  + [addedToScene](#addedtoscene)

    - [<instance> addedToScene()](#instance-addedtoscene)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addToDisplayList](#addtodisplaylist)

    - [<instance> addToDisplayList([displayList])](#instance-addtodisplaylistdisplaylist)
  + [addToUpdateList](#addtoupdatelist)

    - [<instance> addToUpdateList()](#instance-addtoupdatelist)
  + [bringToTop](#bringtotop)

    - [<instance> bringToTop(child)](#instance-bringtotopchild)
  + [clearAlpha](#clearalpha)

    - [<instance> clearAlpha()](#instance-clearalpha)
  + [clearFX](#clearfx)

    - [<instance> clearFX()](#instance-clearfx)
  + [clearMask](#clearmask)

    - [<instance> clearMask([destroyMask])](#instance-clearmaskdestroymask)
  + [copyPosition](#copyposition)

    - [<instance> copyPosition(source)](#instance-copypositionsource)
  + [count](#count)

    - [<instance> count(property, value, [startIndex], [endIndex])](#instance-countproperty-value-startindex-endindex)
  + [createBitmapMask](#createbitmapmask)

    - [<instance> createBitmapMask([maskObject], [x], [y], [texture], [frame])](#instance-createbitmapmaskmaskobject-x-y-texture-frame)
  + [createGeometryMask](#creategeometrymask)

    - [<instance> createGeometryMask([graphics])](#instance-creategeometrymaskgraphics)
  + [destroy](#destroy)

    - [<instance> destroy([fromScene])](#instance-destroyfromscene)
  + [disableInteractive](#disableinteractive)

    - [<instance> disableInteractive([resetCursor])](#instance-disableinteractiveresetcursor)
  + [each](#each)

    - [<instance> each(callback, [context], [args])](#instance-eachcallback-context-args)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [exists](#exists)

    - [<instance> exists(child)](#instance-existschild)
  + [getAll](#getall)

    - [<instance> getAll([property], [value], [startIndex], [endIndex])](#instance-getallproperty-value-startindex-endindex)
  + [getAt](#getat)

    - [<instance> getAt(index)](#instance-getatindex)
  + [getBounds](#getbounds)

    - [<instance> getBounds([output])](#instance-getboundsoutput)
  + [getBoundsTransformMatrix](#getboundstransformmatrix)

    - [<instance> getBoundsTransformMatrix()](#instance-getboundstransformmatrix)
  + [getByName](#getbyname)

    - [<instance> getByName(name)](#instance-getbynamename)
  + [getData](#getdata)

    - [<instance> getData(key)](#instance-getdatakey)
  + [getDisplayList](#getdisplaylist)

    - [<instance> getDisplayList()](#instance-getdisplaylist)
  + [getFirst](#getfirst)

    - [<instance> getFirst(property, value, [startIndex], [endIndex])](#instance-getfirstproperty-value-startindex-endindex)
  + [getIndex](#getindex)

    - [<instance> getIndex(child)](#instance-getindexchild)
  + [getIndexList](#getindexlist)

    - [<instance> getIndexList()](#instance-getindexlist)
  + [getLocalPoint](#getlocalpoint)

    - [<instance> getLocalPoint(x, y, [point], [camera])](#instance-getlocalpointx-y-point-camera)
  + [getLocalTransformMatrix](#getlocaltransformmatrix)

    - [<instance> getLocalTransformMatrix([tempMatrix])](#instance-getlocaltransformmatrixtempmatrix)
  + [getParentRotation](#getparentrotation)

    - [<instance> getParentRotation()](#instance-getparentrotation)
  + [getPostPipeline](#getpostpipeline)

    - [<instance> getPostPipeline(pipeline)](#instance-getpostpipelinepipeline)
  + [getRandom](#getrandom)

    - [<instance> getRandom([startIndex], [length])](#instance-getrandomstartindex-length)
  + [getWorldTransformMatrix](#getworldtransformmatrix)

    - [<instance> getWorldTransformMatrix([tempMatrix], [parentMatrix])](#instance-getworldtransformmatrixtempmatrix-parentmatrix)
  + [incData](#incdata)

    - [<instance> incData(key, [amount])](#instance-incdatakey-amount)
  + [initPostPipeline](#initpostpipeline)

    - [<instance> initPostPipeline([preFX])](#instance-initpostpipelineprefx)
  + [iterate](#iterate)

    - [<instance> iterate(callback, [context], [args])](#instance-iteratecallback-context-args)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [moveAbove](#moveabove)

    - [<instance> moveAbove(child1, child2)](#instance-moveabovechild1-child2)
  + [moveBelow](#movebelow)

    - [<instance> moveBelow(child1, child2)](#instance-movebelowchild1-child2)
  + [moveDown](#movedown)

    - [<instance> moveDown(child)](#instance-movedownchild)
  + [moveTo](#moveto)

    - [<instance> moveTo(child, index)](#instance-movetochild-index)
  + [moveUp](#moveup)

    - [<instance> moveUp(child)](#instance-moveupchild)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [onChildDestroyed](#onchilddestroyed)

    - [<instance> onChildDestroyed()](#instance-onchilddestroyed)
  + [pointToContainer](#pointtocontainer)

    - [<instance> pointToContainer(source, [output])](#instance-pointtocontainersource-output)
  + [preDestroy](#predestroy)

    - [<instance> preDestroy()](#instance-predestroy)
  + [remove](#remove)

    - [<instance> remove(child, [destroyChild])](#instance-removechild-destroychild)
  + [removeAll](#removeall)

    - [<instance> removeAll([destroyChild])](#instance-removealldestroychild)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeAt](#removeat)

    - [<instance> removeAt(index, [destroyChild])](#instance-removeatindex-destroychild)
  + [removeBetween](#removebetween)

    - [<instance> removeBetween([startIndex], [endIndex], [destroyChild])](#instance-removebetweenstartindex-endindex-destroychild)
  + [removedFromScene](#removedfromscene)

    - [<instance> removedFromScene()](#instance-removedfromscene)
  + [removeFromDisplayList](#removefromdisplaylist)

    - [<instance> removeFromDisplayList()](#instance-removefromdisplaylist)
  + [removeFromUpdateList](#removefromupdatelist)

    - [<instance> removeFromUpdateList()](#instance-removefromupdatelist)
  + [removeInteractive](#removeinteractive)

    - [<instance> removeInteractive([resetCursor])](#instance-removeinteractiveresetcursor)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [removePostPipeline](#removepostpipeline)

    - [<instance> removePostPipeline(pipeline)](#instance-removepostpipelinepipeline)
  + [replace](#replace)

    - [<instance> replace(oldChild, newChild, [destroyChild])](#instance-replaceoldchild-newchild-destroychild)
  + [resetPostPipeline](#resetpostpipeline)

    - [<instance> resetPostPipeline([resetData])](#instance-resetpostpipelineresetdata)
  + [reverse](#reverse)

    - [<instance> reverse()](#instance-reverse)
  + [sendToBack](#sendtoback)

    - [<instance> sendToBack(child)](#instance-sendtobackchild)
  + [setAbove](#setabove)

    - [<instance> setAbove(gameObject)](#instance-setabovegameobject)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)
  + [setAll](#setall)

    - [<instance> setAll(property, value, [startIndex], [endIndex])](#instance-setallproperty-value-startindex-endindex)
  + [setAlpha](#setalpha)

    - [<instance> setAlpha([value])](#instance-setalphavalue)
  + [setAngle](#setangle)

    - [<instance> setAngle([degrees])](#instance-setangledegrees)
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
  + [setDisplaySize](#setdisplaysize)

    - [<instance> setDisplaySize(width, height)](#instance-setdisplaysizewidth-height)
  + [setExclusive](#setexclusive)

    - [<instance> setExclusive([value])](#instance-setexclusivevalue)
  + [setInteractive](#setinteractive)

    - [<instance> setInteractive([hitArea], [callback], [dropZone])](#instance-setinteractivehitarea-callback-dropzone)
  + [setMask](#setmask)

    - [<instance> setMask(mask)](#instance-setmaskmask)
  + [setName](#setname)

    - [<instance> setName(value)](#instance-setnamevalue)
  + [setPosition](#setposition)

    - [<instance> setPosition([x], [y], [z], [w])](#instance-setpositionx-y-z-w)
  + [setPostPipeline](#setpostpipeline)

    - [<instance> setPostPipeline(pipelines, [pipelineData], [copyData])](#instance-setpostpipelinepipelines-pipelinedata-copydata)
  + [setPostPipelineData](#setpostpipelinedata)

    - [<instance> setPostPipelineData(key, [value])](#instance-setpostpipelinedatakey-value)
  + [setRandomPosition](#setrandomposition)

    - [<instance> setRandomPosition([x], [y], [width], [height])](#instance-setrandompositionx-y-width-height)
  + [setRotation](#setrotation)

    - [<instance> setRotation([radians])](#instance-setrotationradians)
  + [setScale](#setscale)

    - [<instance> setScale([x], [y])](#instance-setscalex-y)
  + [setScrollFactor](#setscrollfactor)

    - [<instance> setScrollFactor(x, [y], [updateChildren])](#instance-setscrollfactorx-y-updatechildren)
  + [setSize](#setsize)

    - [<instance> setSize(width, height)](#instance-setsizewidth-height)
  + [setState](#setstate)

    - [<instance> setState(value)](#instance-setstatevalue)
  + [setToBack](#settoback)

    - [<instance> setToBack()](#instance-settoback)
  + [setToTop](#settotop)

    - [<instance> setToTop()](#instance-settotop)
  + [setVisible](#setvisible)

    - [<instance> setVisible(value)](#instance-setvisiblevalue)
  + [setW](#setw)

    - [<instance> setW([value])](#instance-setwvalue)
  + [setX](#setx)

    - [<instance> setX([value])](#instance-setxvalue)
  + [setY](#sety)

    - [<instance> setY([value])](#instance-setyvalue)
  + [setZ](#setz)

    - [<instance> setZ([value])](#instance-setzvalue)
  + [shuffle](#shuffle)

    - [<instance> shuffle()](#instance-shuffle)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [sort](#sort)

    - [<instance> sort(property, [handler])](#instance-sortproperty-handler)
  + [swap](#swap)

    - [<instance> swap(child1, child2)](#instance-swapchild1-child2)
  + [toggleData](#toggledata)

    - [<instance> toggleData(key)](#instance-toggledatakey)
  + [toJSON](#tojson)

    - [<instance> toJSON()](#instance-tojson)
  + [update](#update)

    - [<instance> update([args])](#instance-updateargs)
  + [willRender](#willrender)

    - [<instance> willRender(camera)](#instance-willrendercamera)
* [Private Methods](#private-methods)

  + [addHandler](#addhandler)

    - [<instance> addHandler(gameObject)](#instance-addhandlergameobject)
  + [removeHandler](#removehandler)

    - [<instance> removeHandler(gameObject)](#instance-removehandlergameobject)
  + [renderCanvas](#rendercanvas)

    - [<instance> renderCanvas(renderer, container, camera, parentMatrix)](#instance-rendercanvasrenderer-container-camera-parentmatrix)
  + [renderWebGL](#renderwebgl)

    - [<instance> renderWebGL(renderer, container, camera, parentMatrix)](#instance-renderwebglrenderer-container-camera-parentmatrix)

Back to top

©2025[Phaser](https://docs.phaser.io)