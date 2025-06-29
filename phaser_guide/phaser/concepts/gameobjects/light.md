# Light

A Guide to the Phaser Light Game Object and Lights Manager

A 2D Light created by the `Phaser.GameObjects.LightsManager`, available from within a scene via `this.lights`.

Any Game Objects using the Light2D pipeline will then be affected by these Lights as long as they have a normal map.

They can also simply be used to represent a point light for your own purposes.

!!! warning "WebGL only"
Lights cannot be added to Containers. They are designed to exist in the root of a Scene.

!!! warning "WebGL only"
It only works in WebGL render mode.

## Lights Manager

### Enable Lights Manager

* Enable

  ```
  Copythis.lights.enable();

  ```
* Disable

  ```
  Copythis.lights.disable();

  ```

  or

  ```
  Copythis.lights.active = false;

  ```

### Ambient color

```
Copythis.lights.setAmbientColor(color);

```

* `color` : Integer color value.

### Get all lights managed by this Lights Manager

```
Copy    var lightsCount = this.lights.getLightCount();

```

### Get all lights seen by the given Camera

```
Copy    var visibleLights = this.lights.getLights(camera);

```

* `camera` : The Camera to cull Lights for.

### Get maximum number of Lights allowed to appear

```
Copy    var maxVisibleLights = this.lights.getMaxVisibleLights();

```

### Shut down the Lights Manager

Recycles all active Lights into the Light pool, resets ambient light color and clears the lists of Lights and culled Lights.

```
Copy    this.lights.shutdown();

```

## Light Game Object

* Add

  ```
  Copyvar light = this.lights.addLight(x, y, radius);
  // var light = this.lights.addLight(x, y, radius, color, intensity);

  ```

  + `x`, `y` : The horizontal/vertical position of the Light. Default is 0.
  + `radius` : The radius of the Light. Default is 128. Default is 0.
  + `color` : The integer RGB color of the light. Default is `0xffffff`.
  + `intensity` : The intensity of the Light. Default is 1.
* Add Point Light

  + The Point Light Game Object provides a way to add a point light effect into your game, without the expensive shader processing requirements of the traditional Light Game Object. It renders using a custom shader, designed to give the impression of a point light source, of variable radius, intensity and color, in your game. However, unlike the Light Game Object, it does not impact any other Game Objects, or use their normal maps for calcuations. This makes them extremely fast to render compared to Lights and perfect for special effects, such as flickering torches or muzzle flashes.

    ```
    Copyvar light = this.lights.addPointLight(x, y, color, radius, intensity, attenuation);

    ```
  + `x`, `y` : The horizontal/vertical position of the Light.
  + `color` : The integer RGB color of the light. Default is `0xffffff`.
  + `radius` : The radius of the Light. Default is 128.
  + `intensity` : The intensity of the Light. Default is 1.
  + `attenuation` : The attenuation of the Point Light. This is the reduction of light from the center point. Default is 0.1.
* Remove

  ```
  Copythis.lights.removeLight(light);

  ```
* Destroy

  ```
  Copythis.lights.destroy();

  ```

### Position

* Set

  ```
  Copylight.setPosition(x, y);

  ```

  or

  ```
  Copylight.x = x;
  light.y = y;

  ```
* Get

  ```
  Copyvar x = light.x;
  var y = light.y;

  ```

### Color

* Set

  + Red, green, blue

    ```
    Copylight.color.set(red, green, blue);

    ```

    or

    ```
    Copylight.color.r = red;
    light.color.g = green;
    light.color.b = blue;

    ```
  + Integer value

    ```
    Copylight.setColor(colorInteger);

    ```
* Get

  + Red, green, blue

    ```
    Copyvar red = light.color.r;
    var green = light.color.g;
    var blue = light.color.b;

    ```

### Size

* Set

  ```
  Copylight.setRadius(radius);
  // light.radius = radius;

  ```

  or

  ```
  Copylight.diameter = diameter;
  // light.width = diameter;
  // light.height = diameter;
  // light.displayWidth = diameter;
  // light.displayHeight = diameter;

  ```
* Get

  ```
  Copyvar radius = light.radius;

  ```

  or

  ```
  Copyvar diameter = light.diameter;
  // var diameter = light.displayWidth;
  // var diameter = light.displayHeight;
  // var diameter = light.width;
  // var diameter = light.height;

  ```

### Intensity

* Set

  ```
  Copylight.setIntensity(intensity);

  ```

  or

  ```
  Copylight.intensity = intensity;

  ```
* Get

  ```
  Copyvar intensity = light.intensity;

  ```

## Game object

### Load texture with normal map

```
Copythis.load.image(key, [url, normalMapUrl]);

```

* `url` : Url of texture.
* `url` : Url of texture.
* `normalMapUrl` : Url of normal map.

### Apply light pipeline

```
CopygameObject.setPipeline('Light2D');

```

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Layer](layer.md)

[Mesh](mesh.md)

On this page

* [Light](#light)

  + [Lights Manager](#lights-manager)

    - [Enable Lights Manager](#enable-lights-manager)
    - [Ambient color](#ambient-color)
    - [Get all lights managed by this Lights Manager](#get-all-lights-managed-by-this-lights-manager)
    - [Get all lights seen by the given Camera](#get-all-lights-seen-by-the-given-camera)
    - [Get maximum number of Lights allowed to appear](#get-maximum-number-of-lights-allowed-to-appear)
    - [Shut down the Lights Manager](#shut-down-the-lights-manager)
  + [Light Game Object](#light-game-object)

    - [Position](#position)
    - [Color](#color)
    - [Size](#size)
    - [Intensity](#intensity)
  + [Game object](#game-object)

    - [Load texture with normal map](#load-texture-with-normal-map)
    - [Apply light pipeline](#apply-light-pipeline)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../../index.md)