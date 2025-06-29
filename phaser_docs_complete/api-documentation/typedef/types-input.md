# Types.Input

Phaser.Types.Input

## EventData

### <static> EventData

A Phaser Input Event Data object.

This object is passed to the registered event listeners and allows you to stop any further propagation.

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| cancelled | boolean | Yes | false | The cancelled state of this Event. |
| --- | --- | --- | --- | --- |
| stopPropagation | function | No |  | Call this method to stop this event from passing any further down the event chain. |

**Type**: object

**Member of**: Phaser.Types.Input

> Source: [src/input/typedefs/EventData.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/typedefs/EventData.js#L7)  
> Since: 3.15.1

---

## HitAreaCallback

### <static> HitAreaCallback

**Type**: function

**Member of**: Phaser.Types.Input

> Source: [src/input/typedefs/HitAreaCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/typedefs/HitAreaCallback.js#L1)  
> Since: 3.0.0

---

## InputConfiguration

### <static> InputConfiguration

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| hitArea | any | Yes |  | The object / shape to use as the Hit Area. If not given it will try to create a Rectangle based on the texture frame. |
| --- | --- | --- | --- | --- |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](types-input.md) | Yes |  | The callback that determines if the pointer is within the Hit Area shape or not. |
| draggable | boolean | Yes | false | If `true` the Interactive Object will be set to be draggable and emit drag events. |
| dropZone | boolean | Yes | false | If `true` the Interactive Object will be set to be a drop zone for draggable objects. |
| useHandCursor | boolean | Yes | false | If `true` the Interactive Object will set the `pointer` hand cursor when a pointer is over it. This is a short-cut for setting `cursor: 'pointer'`. |
| cursor | string | Yes |  | The CSS string to be used when the cursor is over this Interactive Object. |
| pixelPerfect | boolean | Yes | false | If `true` the a pixel perfect function will be set for the hit area callback. Only works with image texture based Game Objects, not Render Textures. |
| alphaTolerance | number | Yes | 1 | If `pixelPerfect` is set, this is the alpha tolerance threshold value used in the callback. A value of 255 will match only fully opaque pixels. |

**Type**: object

**Member of**: Phaser.Types.Input

> Source: [src/input/typedefs/InputConfiguration.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/typedefs/InputConfiguration.js#L1)  
> Since: 3.0.0

---

## InputPluginContainer

### <static> InputPluginContainer

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique name of this plugin in the input plugin cache. |
| --- | --- | --- | --- |
| plugin | function | No | The plugin to be stored. Should be the source object, not instantiated. |
| mapping | string | Yes | If this plugin is to be injected into the Input Plugin, this is the property key map used. |

**Type**: object

**Member of**: Phaser.Types.Input

> Source: [src/input/typedefs/InputPluginContainer.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/typedefs/InputPluginContainer.js#L1)  
> Since: 3.0.0

---

## InteractiveObject

### <static> InteractiveObject

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to which this Interactive Object is bound. |
| --- | --- | --- | --- |
| enabled | boolean | No | Is this Interactive Object currently enabled for input events? |
| draggable | boolean | No | Is this Interactive Object draggable? Enable with `InputPlugin.setDraggable`. |
| dropZone | boolean | No | Is this Interactive Object a drag-targets drop zone? Set when the object is created. |
| cursor | boolean | string | No | Should this Interactive Object change the cursor (via css) when over? (desktop only) |
| target | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | An optional drop target for a draggable Interactive Object. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The most recent Camera to be tested against this Interactive Object. |
| hitArea | any | No | The hit area for this Interactive Object. Typically a geometry shape, like a Rectangle or Circle. |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](types-input.md) | No | The 'contains' check callback that the hit area shape will use for all hit tests. |
| hitAreaDebug | [Phaser.GameObjects.Shape](../class/gameobjects-shape.md) | No | If this Interactive Object has been enabled for debug, via `InputPlugin.enableDebug` then this property holds its debug shape. |
| customHitArea | boolean | No | Was the hitArea for this Interactive Object created based on texture size (false), or a custom shape? (true) |
| localX | number | No | The x coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position. |
| localY | number | No | The y coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position. |
| dragState | 0 | 1 | 2 | No |
| dragStartX | number | No | The x coordinate of the Game Object that owns this Interactive Object when the drag started. |
| dragStartY | number | No | The y coordinate of the Game Object that owns this Interactive Object when the drag started. |
| dragStartXGlobal | number | No | The x coordinate that the Pointer started dragging this Interactive Object from. |
| dragStartYGlobal | number | No | The y coordinate that the Pointer started dragging this Interactive Object from. |
| dragX | number | No | The x coordinate that this Interactive Object is currently being dragged to. |
| dragY | number | No | The y coordinate that this Interactive Object is currently being dragged to. |

**Type**: object

**Member of**: Phaser.Types.Input

> Source: [src/input/typedefs/InteractiveObject.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/typedefs/InteractiveObject.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Input](#typesinput)

  + [EventData](#eventdata)

    - [<static> EventData](#static-eventdata)
  + [HitAreaCallback](#hitareacallback)

    - [<static> HitAreaCallback](#static-hitareacallback)
  + [InputConfiguration](#inputconfiguration)

    - [<static> InputConfiguration](#static-inputconfiguration)
  + [InputPluginContainer](#inputplugincontainer)

    - [<static> InputPluginContainer](#static-inputplugincontainer)
  + [InteractiveObject](#interactiveobject)

    - [<static> InteractiveObject](#static-interactiveobject)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Input