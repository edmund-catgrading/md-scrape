# LightsPlugin

Phaser.GameObjects.LightsPlugin

A Scene plugin that provides a [Phaser.GameObjects.LightsManager](Phaser.GameObjects.LightsManager.md) for the Light2D pipeline.

Available from within a Scene via `this.lights`.

Add Lights using the [Phaser.GameObjects.LightsManager#addLight](gameobjects-lightsmanager.md) method:

```
Copy
// Enable the Lights Manager because it is disabled by default

this.lights.enable();



// Create a Light at [400, 300] with a radius of 200

this.lights.addLight(400, 300, 200);


```

For Game Objects to be affected by the Lights when rendered, you will need to set them to use the `Light2D` pipeline like so:

```
Copy
sprite.setPipeline('Light2D');


```

Note that you cannot use this pipeline on Graphics Game Objects or Shape Game Objects.

**Constructor**

`new LightsPlugin(scene)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene that this Lights Plugin belongs to. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.GameObjects.LightsManager](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsPlugin.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsPlugin.js#L12)  
> Since: 3.0.0

# Public Members

## active

### active: boolean

**Description:**

Whether the Lights Manager is enabled.

**Inherits:** [Phaser.GameObjects.LightsManager#active](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsManager.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsManager.js#L59)  
> Since: 3.0.0

---

## ambientColor

### ambientColor: [Phaser.Display.RGB](display-rgb.md)

**Description:**

The ambient color.

**Inherits:** [Phaser.GameObjects.LightsManager#ambientColor](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsManager.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsManager.js#L50)  
> Since: 3.50.0

---

## lights

### lights: Array.<[Phaser.GameObjects.Light](gameobjects-light.md)>

**Description:**

The Lights in the Scene.

**Inherits:** [Phaser.GameObjects.LightsManager#lights](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsManager.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsManager.js#L40)  
> Since: 3.0.0

---

## maxLights

### maxLights: number

**Description:**

The maximum number of lights that a single Camera and the lights shader can process.

Change this via the `maxLights` property in your game config, as it cannot be changed at runtime.

**Inherits:** [Phaser.GameObjects.LightsManager#maxLights](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsManager.js#L69](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsManager.js#L69)  
> Since: 3.15.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

A reference to the Scene that this Lights Plugin belongs to.

> Source: [src/gameobjects/lights/LightsPlugin.js#L52](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsPlugin.js#L52)  
> Since: 3.0.0

---

## systems

### systems: [Phaser.Scenes.Systems](scenes-systems.md)

**Description:**

A reference to the Scene's systems.

> Source: [src/gameobjects/lights/LightsPlugin.js#L61](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsPlugin.js#L61)  
> Since: 3.0.0

---

## visibleLights

### visibleLights: number

**Description:**

The number of lights that the LightPipeline processed in the *previous* frame.

**Inherits:** [Phaser.GameObjects.LightsManager#visibleLights](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsManager.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsManager.js#L80)  
> Since: 3.50.0

---

# Public Methods

## addLight

### <instance> addLight([x], [y], [radius], [rgb], [intensity])

**Description:**

Add a Light.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of the Light. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of the Light. |
| radius | number | Yes | 128 | The radius of the Light. |
| rgb | number | Yes | "0xffffff" | The integer RGB color of the light. |
| intensity | number | Yes | 1 | The intensity of the Light. |

**Returns:** [Phaser.GameObjects.Light](gameobjects-light.md) - The Light that was added.

**Inherits:** [Phaser.GameObjects.LightsManager#addLight](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsManager.js#L273](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsManager.js#L273)  
> Since: 3.0.0

---

## addPointLight

### <instance> addPointLight(x, y, [color], [radius], [intensity], [attenuation])

**Description:**

Creates a new Point Light Game Object and adds it to the Scene.

Note: This method will only be available if the Point Light Game Object has been built into Phaser.

The Point Light Game Object provides a way to add a point light effect into your game,

without the expensive shader processing requirements of the traditional Light Game Object.

The difference is that the Point Light renders using a custom shader, designed to give the

impression of a point light source, of variable radius, intensity and color, in your game.

However, unlike the Light Game Object, it does not impact any other Game Objects, or use their

normal maps for calcuations. This makes them extremely fast to render compared to Lights

and perfect for special effects, such as flickering torches or muzzle flashes.

For maximum performance you should batch Point Light Game Objects together. This means

ensuring they follow each other consecutively on the display list. Ideally, use a Layer

Game Object and then add just Point Lights to it, so that it can batch together the rendering

of the lights. You don't *have* to do this, and if you've only a handful of Point Lights in

your game then it's perfectly safe to mix them into the dislay list as normal. However, if

you're using a large number of them, please consider how they are mixed into the display list.

The renderer will automatically cull Point Lights. Those with a radius that does not intersect

with the Camera will be skipped in the rendering list. This happens automatically and the

culled state is refreshed every frame, for every camera.

The origin of a Point Light is always 0.5 and it cannot be changed.

Point Lights are a WebGL only feature and do not have a Canvas counterpart.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal position of this Point Light in the world. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The vertical position of this Point Light in the world. |
| color | number | Yes | "0xffffff" | The color of the Point Light, given as a hex value. |
| radius | number | Yes | 128 | The radius of the Point Light. |
| intensity | number | Yes | 1 | The intensity, or color blend, of the Point Light. |
| attenuation | number | Yes | 0.1 | The attenuation of the Point Light. This is the reduction of light from the center point. |

**Returns:** [Phaser.GameObjects.PointLight](gameobjects-pointlight.md) - The Game Object that was created.

**Inherits:** [Phaser.GameObjects.LightsManager#addPointLight](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsManager.js#L91](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsManager.js#L91)  
> Since: 3.50.0

---

## boot

### <instance> boot()

**Description:**

Boot the Lights Plugin.

> Source: [src/gameobjects/lights/LightsPlugin.js#L78](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsPlugin.js#L78)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroy the Lights Plugin.

Cleans up all references.

**Overrides:** Phaser.GameObjects.LightsManager#destroy

> Source: [src/gameobjects/lights/LightsPlugin.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsPlugin.js#L92)  
> Since: 3.0.0

---

## disable

### <instance> disable()

**Description:**

Disable the Lights Manager.

**Returns:** [Phaser.GameObjects.LightsPlugin](gameobjects-lightsplugin.md) - This Lights Manager instance.

**Inherits:** [Phaser.GameObjects.LightsManager#disable](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsManager.js#L157](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsManager.js#L157)  
> Since: 3.0.0

---

## enable

### <instance> enable()

**Description:**

Enable the Lights Manager.

**Returns:** [Phaser.GameObjects.LightsPlugin](gameobjects-lightsplugin.md) - This Lights Manager instance.

**Inherits:** [Phaser.GameObjects.LightsManager#enable](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsManager.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsManager.js#L137)  
> Since: 3.0.0

---

## getLightCount

### <instance> getLightCount()

**Description:**

Get the number of Lights managed by this Lights Manager.

**Returns:** number - The number of Lights managed by this Lights Manager.

**Inherits:** [Phaser.GameObjects.LightsManager#getLightCount](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsManager.js#L260](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsManager.js#L260)  
> Since: 3.0.0

---

## getLights

### <instance> getLights(camera)

**Description:**

Get all lights that can be seen by the given Camera.

It will automatically cull lights that are outside the world view of the Camera.

If more lights are returned than supported by the pipeline, the lights are then culled

based on the distance from the center of the camera. Only those closest are rendered.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera to cull Lights for. |
| --- | --- | --- | --- |

**Returns:** Array.<[Phaser.GameObjects.Light](gameobjects-light.md)> - The culled Lights.

**Inherits:** [Phaser.GameObjects.LightsManager#getLights](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsManager.js#L172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsManager.js#L172)  
> Since: 3.50.0

---

## getMaxVisibleLights

### <instance> getMaxVisibleLights()

**Description:**

Returns the maximum number of Lights allowed to appear at once.

**Returns:** number - The maximum number of Lights allowed to appear at once.

**Inherits:** [Phaser.GameObjects.LightsManager#getMaxVisibleLights](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsManager.js#L247](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsManager.js#L247)  
> Since: 3.0.0

---

## removeLight

### <instance> removeLight(light)

**Description:**

Remove a Light.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| light | [Phaser.GameObjects.Light](gameobjects-light.md) | No | The Light to remove. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.LightsPlugin](gameobjects-lightsplugin.md) - This Lights Manager instance.

**Inherits:** [Phaser.GameObjects.LightsManager#removeLight](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsManager.js#L304](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsManager.js#L304)  
> Since: 3.0.0

---

## setAmbientColor

### <instance> setAmbientColor(rgb)

**Description:**

Set the ambient light color.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rgb | number | No | The integer RGB color of the ambient light. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.LightsPlugin](gameobjects-lightsplugin.md) - This Lights Manager instance.

**Inherits:** [Phaser.GameObjects.LightsManager#setAmbientColor](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsManager.js#L228](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsManager.js#L228)  
> Since: 3.0.0

---

## shutdown

### <instance> shutdown()

**Description:**

Shut down the Lights Manager.

Recycles all active Lights into the Light pool, resets ambient light color and clears the lists of Lights and

culled Lights.

**Inherits:** [Phaser.GameObjects.LightsManager#shutdown](gameobjects-lightsmanager.md)

> Source: [src/gameobjects/lights/LightsManager.js#L326](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/LightsManager.js#L326)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [active](#active)

    - [active: boolean](#active-boolean)
  + [ambientColor](#ambientcolor)

    - [ambientColor: Phaser.Display.RGB](#ambientcolor-phaserdisplayrgb)
  + [lights](#lights)

    - [lights: Array.<Phaser.GameObjects.Light>](#lights-arrayphasergameobjectslight)
  + [maxLights](#maxlights)

    - [maxLights: number](#maxlights-number)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [systems](#systems)

    - [systems: Phaser.Scenes.Systems](#systems-phaserscenessystems)
  + [visibleLights](#visiblelights)

    - [visibleLights: number](#visiblelights-number)
* [Public Methods](#public-methods)

  + [addLight](#addlight)

    - [<instance> addLight([x], [y], [radius], [rgb], [intensity])](#instance-addlightx-y-radius-rgb-intensity)
  + [addPointLight](#addpointlight)

    - [<instance> addPointLight(x, y, [color], [radius], [intensity], [attenuation])](#instance-addpointlightx-y-color-radius-intensity-attenuation)
  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [disable](#disable)

    - [<instance> disable()](#instance-disable)
  + [enable](#enable)

    - [<instance> enable()](#instance-enable)
  + [getLightCount](#getlightcount)

    - [<instance> getLightCount()](#instance-getlightcount)
  + [getLights](#getlights)

    - [<instance> getLights(camera)](#instance-getlightscamera)
  + [getMaxVisibleLights](#getmaxvisiblelights)

    - [<instance> getMaxVisibleLights()](#instance-getmaxvisiblelights)
  + [removeLight](#removelight)

    - [<instance> removeLight(light)](#instance-removelightlight)
  + [setAmbientColor](#setambientcolor)

    - [<instance> setAmbientColor(rgb)](#instance-setambientcolorrgb)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)

Back to top

©2025[Phaser](https://docs.phaser.io)