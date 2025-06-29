# CameraManager

Phaser.Cameras.Scene2D.CameraManager

The Camera Manager is a plugin that belongs to a Scene and is responsible for managing all of the Scene Cameras.

By default you can access the Camera Manager from within a Scene using `this.cameras`, although this can be changed

in your game config.

Create new Cameras using the `add` method. Or extend the Camera class with your own addition code and then add

the new Camera in using the `addExisting` method.

Cameras provide a view into your game world, and can be positioned, rotated, zoomed and scrolled accordingly.

A Camera consists of two elements: The viewport and the scroll values.

The viewport is the physical position and size of the Camera within your game. Cameras, by default, are

created the same size as your game, but their position and size can be set to anything. This means if you

wanted to create a camera that was 320x200 in size, positioned in the bottom-right corner of your game,

you'd adjust the viewport to do that (using methods like `setViewport` and `setSize`).

If you wish to change where the Camera is looking in your game, then you scroll it. You can do this

via the properties `scrollX` and `scrollY` or the method `setScroll`. Scrolling has no impact on the

viewport, and changing the viewport has no impact on the scrolling.

By default a Camera will render all Game Objects it can see. You can change this using the `ignore` method,

allowing you to filter Game Objects out on a per-Camera basis. The Camera Manager can manage up to 31 unique

'Game Object ignore capable' Cameras. Any Cameras beyond 31 that you create will all be given a Camera ID of

zero, meaning that they cannot be used for Game Object exclusion. This means if you need your Camera to ignore

Game Objects, make sure it's one of the first 31 created.

A Camera also has built-in special effects including Fade, Flash, Camera Shake, Pan and Zoom.

**Constructor**

`new CameraManager(scene)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene that owns the Camera Manager plugin. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/cameras/2d/CameraManager.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L15)  
> Since: 3.0.0

# Public Members

## cameras

### cameras: Array.<[Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md)>

**Description:**

An Array of the Camera objects being managed by this Camera Manager.

The Cameras are updated and rendered in the same order in which they appear in this array.

Do not directly add or remove entries to this array. However, you can move the contents

around the array should you wish to adjust the display order.

> Source: [src/cameras/2d/CameraManager.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L89)  
> Since: 3.0.0

---

## default

### default: [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md)

**Description:**

A default un-transformed Camera that doesn't exist on the camera list and doesn't

count towards the total number of cameras being managed. It exists for other

systems, as well as your own code, should they require a basic un-transformed

camera instance from which to calculate a view matrix.

> Source: [src/cameras/2d/CameraManager.js#L118](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L118)  
> Since: 3.17.0

---

## main

### main: [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md)

**Description:**

A handy reference to the 'main' camera. By default this is the first Camera the

Camera Manager creates. You can also set it directly, or use the `makeMain` argument

in the `add` and `addExisting` methods. It allows you to access it from your game:

```
Copy
var cam = this.cameras.main;


```

Also see the properties `camera1`, `camera2` and so on.

> Source: [src/cameras/2d/CameraManager.js#L101](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L101)  
> Since: 3.0.0

---

## roundPixels

### roundPixels: boolean

**Description:**

All Cameras created by, or added to, this Camera Manager, will have their `roundPixels`

property set to match this value. By default it is set to match the value set in the

game configuration, but can be changed at any point. Equally, individual cameras can

also be changed as needed.

> Source: [src/cameras/2d/CameraManager.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L77)  
> Since: 3.11.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

The Scene that owns the Camera Manager plugin.

> Source: [src/cameras/2d/CameraManager.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L59)  
> Since: 3.0.0

---

## systems

### systems: [Phaser.Scenes.Systems](scenes-systems.md)

**Description:**

A reference to the Scene.Systems handler for the Scene that owns the Camera Manager.

> Source: [src/cameras/2d/CameraManager.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L68)  
> Since: 3.0.0

---

# Public Methods

## add

### <instance> add([x], [y], [width], [height], [makeMain], [name])

**Description:**

Adds a new Camera into the Camera Manager. The Camera Manager can support up to 31 different Cameras.

Each Camera has its own viewport, which controls the size of the Camera and its position within the canvas.

Use the `Camera.scrollX` and `Camera.scrollY` properties to change where the Camera is looking, or the

Camera methods such as `centerOn`. Cameras also have built in special effects, such as fade, flash, shake,

pan and zoom.

By default Cameras are transparent and will render anything that they can see based on their `scrollX`

and `scrollY` values. Game Objects can be set to be ignored by a Camera by using the `Camera.ignore` method.

The Camera will have its `roundPixels` property set to whatever `CameraManager.roundPixels` is. You can change

it after creation if required.

See the Camera class documentation for more details.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of the Camera viewport. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of the Camera viewport. |
| width | number | Yes |  | The width of the Camera viewport. If not given it'll be the game config size. |
| height | number | Yes |  | The height of the Camera viewport. If not given it'll be the game config size. |
| makeMain | boolean | Yes | false | Set this Camera as being the 'main' camera. This just makes the property `main` a reference to it. |
| name | string | Yes | "''" | The name of the Camera. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - The newly created Camera.

> Source: [src/cameras/2d/CameraManager.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L205)  
> Since: 3.0.0

---

## addExisting

### <instance> addExisting(camera, [makeMain])

**Description:**

Adds an existing Camera into the Camera Manager.

The Camera should either be a `Phaser.Cameras.Scene2D.Camera` instance, or a class that extends from it.

The Camera will have its `roundPixels` property set to whatever `CameraManager.roundPixels` is. You can change

it after addition if required.

The Camera will be assigned an ID, which is used for Game Object exclusion and then added to the

manager. As long as it doesn't already exist in the manager it will be added then returned.

If this method returns `null` then the Camera already exists in this Camera Manager.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No |  | The Camera to be added to the Camera Manager. |
| --- | --- | --- | --- | --- |
| makeMain | boolean | Yes | false | Set this Camera as being the 'main' camera. This just makes the property `main` a reference to it. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - The Camera that was added to the Camera Manager, or `null` if it couldn't be added.

> Source: [src/cameras/2d/CameraManager.js#L261](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L261)  
> Since: 3.0.0

---

## fromJSON

### <instance> fromJSON(config)

**Description:**

Populates this Camera Manager based on the given configuration object, or an array of config objects.

See the `Phaser.Types.Cameras.Scene2D.CameraConfig` documentation for details of the object structure.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Cameras.Scene2D.CameraConfig](../typedef/types-cameras-scene2d.md) | Array.<[Phaser.Types.Cameras.Scene2D.CameraConfig](../typedef/types-cameras-scene2d.md)> | No | A Camera configuration object, or an array of them, to be added to this Camera Manager. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Cameras.Scene2D.CameraManager](cameras-scene2d-cameramanager.md) - This Camera Manager instance.

> Source: [src/cameras/2d/CameraManager.js#L388](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L388)  
> Since: 3.0.0

---

## getCamera

### <instance> getCamera(name)

**Description:**

Gets a Camera based on its name.

Camera names are optional and don't have to be set, so this method is only of any use if you

have given your Cameras unique names.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the Camera. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - The first Camera with a name matching the given string, otherwise `null`.

> Source: [src/cameras/2d/CameraManager.js#L457](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L457)  
> Since: 3.0.0

---

## getCamerasBelowPointer

### <instance> getCamerasBelowPointer(pointer)

**Description:**

Returns an array of all cameras below the given Pointer.

The first camera in the array is the top-most camera in the camera list.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The Pointer to check against. |
| --- | --- | --- | --- |

**Returns:** Array.<[Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md)> - An array of cameras below the Pointer.

> Source: [src/cameras/2d/CameraManager.js#L485](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L485)  
> Since: 3.10.0

---

## getTotal

### <instance> getTotal([isVisible])

**Description:**

Gets the total number of Cameras in this Camera Manager.

If the optional `isVisible` argument is set it will only count Cameras that are currently visible.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| isVisible | boolean | Yes | false | Set the `true` to only include visible Cameras in the total. |
| --- | --- | --- | --- | --- |

**Returns:** number - The total number of Cameras in this Camera Manager.

> Source: [src/cameras/2d/CameraManager.js#L355](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L355)  
> Since: 3.11.0

---

## getVisibleChildren

### <instance> getVisibleChildren(children, camera)

**Description:**

Takes an array of Game Objects and a Camera and returns a new array

containing only those Game Objects that pass the `willRender` test

against the given Camera.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| children | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No | An array of Game Objects to be checked against the camera. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The camera to filter the Game Objects against. |

**Returns:** Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> - A filtered list of only Game Objects within the Scene that will render against the given Camera.

> Source: [src/cameras/2d/CameraManager.js#L612](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L612)  
> Since: 3.50.0

---

## onResize

### <instance> onResize(gameSize, baseSize)

**Description:**

The event handler that manages the `resize` event dispatched by the Scale Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameSize | [Phaser.Structs.Size](structs-size.md) | No | The default Game Size object. This is the un-modified game dimensions. |
| --- | --- | --- | --- |
| baseSize | [Phaser.Structs.Size](structs-size.md) | No | The base Size object. The game dimensions. The canvas width / height values match this. |

> Source: [src/cameras/2d/CameraManager.js#L676](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L676)  
> Since: 3.18.0

---

## remove

### <instance> remove(camera, [runDestroy])

**Description:**

Removes the given Camera, or an array of Cameras, from this Camera Manager.

If found in the Camera Manager it will be immediately removed from the local cameras array.

If also currently the 'main' camera, 'main' will be reset to be camera 0.

The removed Cameras are automatically destroyed if the `runDestroy` argument is `true`, which is the default.

If you wish to re-use the cameras then set this to `false`, but know that they will retain their references

and internal data until destroyed or re-added to a Camera Manager.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Array.<[Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md)> | No |  | The Camera, or an array of Cameras, to be removed from this Camera Manager. |
| --- | --- | --- | --- | --- |
| runDestroy | boolean | Yes | true | Automatically call `Camera.destroy` on each Camera removed from this Camera Manager. |

**Returns:** number - The total number of Cameras removed.

> Source: [src/cameras/2d/CameraManager.js#L520](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L520)  
> Since: 3.0.0

---

## render

### <instance> render(renderer, displayList)

**Description:**

The internal render method. This is called automatically by the Scene and should not be invoked directly.

It will iterate through all local cameras and render them in turn, as long as they're visible and have

an alpha level > 0.

**Access:** protected

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) | [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) | No | The Renderer that will render the children to this camera. |
| --- | --- | --- | --- |
| displayList | [Phaser.GameObjects.DisplayList](gameobjects-displaylist.md) | No | The Display List for the Scene. |

> Source: [src/cameras/2d/CameraManager.js#L579](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L579)  
> Since: 3.0.0

---

## resetAll

### <instance> resetAll()

**Description:**

Resets this Camera Manager.

This will iterate through all current Cameras, destroying them all, then it will reset the

cameras array, reset the ID counter and create 1 new single camera using the default values.

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - The freshly created main Camera.

> Source: [src/cameras/2d/CameraManager.js#L633](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L633)  
> Since: 3.0.0

---

## resize

### <instance> resize(width, height)

**Description:**

Resizes all cameras to the given dimensions.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The new width of the camera. |
| --- | --- | --- | --- |
| height | number | No | The new height of the camera. |

> Source: [src/cameras/2d/CameraManager.js#L701](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L701)  
> Since: 3.2.0

---

## update

### <instance> update(time, delta)

**Description:**

The main update loop. Called automatically when the Scene steps.

**Access:** protected

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current timestamp as generated by the Request Animation Frame or SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time, in ms, elapsed since the last frame. |

> Source: [src/cameras/2d/CameraManager.js#L658](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L658)  
> Since: 3.0.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

This method is called automatically, only once, when the Scene is first created.

Do not invoke it directly.

**Access:** private

> Source: [src/cameras/2d/CameraManager.js#L134](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L134)  
> Since: 3.5.1

---

## destroy

### <instance> destroy()

**Description:**

The Scene that owns this plugin is being destroyed.

We need to shutdown and then kill off all external references.

**Access:** private

> Source: [src/cameras/2d/CameraManager.js#L743](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L743)  
> Since: 3.0.0

---

## getNextID

### <instance> getNextID()

**Description:**

Gets the next available Camera ID number.

The Camera Manager supports up to 31 unique cameras, after which the ID returned will always be zero.

You can create additional cameras beyond 31, but they cannot be used for Game Object exclusion.

**Access:** private

**Returns:** number - The next available Camera ID, or 0 if they're all already in use.

> Source: [src/cameras/2d/CameraManager.js#L307](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L307)  
> Since: 3.11.0

---

## shutdown

### <instance> shutdown()

**Description:**

The Scene that owns this plugin is shutting down.

We need to kill and reset all internal properties as well as stop listening to Scene events.

**Access:** private

> Source: [src/cameras/2d/CameraManager.js#L718](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L718)  
> Since: 3.0.0

---

## start

### <instance> start()

**Description:**

This method is called automatically by the Scene when it is starting up.

It is responsible for creating local systems, properties and listening for Scene events.

Do not invoke it directly.

**Access:** private

> Source: [src/cameras/2d/CameraManager.js#L168](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/CameraManager.js#L168)  
> Since: 3.5.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [cameras](#cameras)

    - [cameras: Array.<Phaser.Cameras.Scene2D.Camera>](#cameras-arrayphasercamerasscene2dcamera)
  + [default](#default)

    - [default: Phaser.Cameras.Scene2D.Camera](#default-phasercamerasscene2dcamera)
  + [main](#main)

    - [main: Phaser.Cameras.Scene2D.Camera](#main-phasercamerasscene2dcamera)
  + [roundPixels](#roundpixels)

    - [roundPixels: boolean](#roundpixels-boolean)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [systems](#systems)

    - [systems: Phaser.Scenes.Systems](#systems-phaserscenessystems)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add([x], [y], [width], [height], [makeMain], [name])](#instance-addx-y-width-height-makemain-name)
  + [addExisting](#addexisting)

    - [<instance> addExisting(camera, [makeMain])](#instance-addexistingcamera-makemain)
  + [fromJSON](#fromjson)

    - [<instance> fromJSON(config)](#instance-fromjsonconfig)
  + [getCamera](#getcamera)

    - [<instance> getCamera(name)](#instance-getcameraname)
  + [getCamerasBelowPointer](#getcamerasbelowpointer)

    - [<instance> getCamerasBelowPointer(pointer)](#instance-getcamerasbelowpointerpointer)
  + [getTotal](#gettotal)

    - [<instance> getTotal([isVisible])](#instance-gettotalisvisible)
  + [getVisibleChildren](#getvisiblechildren)

    - [<instance> getVisibleChildren(children, camera)](#instance-getvisiblechildrenchildren-camera)
  + [onResize](#onresize)

    - [<instance> onResize(gameSize, baseSize)](#instance-onresizegamesize-basesize)
  + [remove](#remove)

    - [<instance> remove(camera, [runDestroy])](#instance-removecamera-rundestroy)
  + [render](#render)

    - [<instance> render(renderer, displayList)](#instance-renderrenderer-displaylist)
  + [resetAll](#resetall)

    - [<instance> resetAll()](#instance-resetall)
  + [resize](#resize)

    - [<instance> resize(width, height)](#instance-resizewidth-height)
  + [update](#update)

    - [<instance> update(time, delta)](#instance-updatetime-delta)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [getNextID](#getnextid)

    - [<instance> getNextID()](#instance-getnextid)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [start](#start)

    - [<instance> start()](#instance-start)

Back to top

©2025[Phaser](https://docs.phaser.io)