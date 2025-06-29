# FX

FX

As of Phaser v3.60, the framework includes a new FX Pipeline system with lots of built-in effects. This is a powerful and flexible way to apply both pre and post-processing effects to your game. It's a WebGL only feature and is not available in Canvas mode as it relies on shaders.

The built-in FX include: Barrel, Bloom, Blur, Bokeh, Circle, ColorMatrix, Displacement, Glow, Gradient, Pixelate, Shadow, Shine, Vignette and Wipe.

The FX can be enabled on all of the common types of Game Objects and you can stack effects and control the stacking order. For example, you can apply both a glow and vignette effect to a Sprite. Cameras can also have FX applied to them, which impacts everything they render and lets you create effects such as a 'zoom blur' or pixelate.

* [Barrel Distortion](#barrel) : A nice pinch / bulge distortion effect.
* [Bloom](#bloom) : Add bloom to any Game Object, with custom offset, blur strength, steps and color.
* [Blur](#blur) : 3 different levels of gaussian blur (low, medium and high) and custom distance and color.
* [Bokeh](#bokeh) / [Tilt Shift](#tilt-shift) : A bokeh and tiltshift effect, with intensity, contrast and distance settings.
* [Circle Outline](#circle-outline) : Add a circular ring around any Game Object, useful for masking / avatar frames, with custom color, width and background color.
* [Color Matrix](#colormatrix) : Add a ColorMatrix to any Game Object with access to all of its methods, such as `sepia`, `greyscale`, `lsd` and lots more.
* [Glow](#glow) : Add a smooth inner or outer glow, with custom distance, strength and color.
* [Displacement](#displacement) : Use a displacement texture, such as a noise texture, to drastically (or subtly!) alter the appearance of a Game Object.
* [Gradient](#gradient) : Draw a gradient between two colors across any Game Object, with optional 'chunky' mode for classic retro style games.
* [Pixelate](#pixelate) : Make any Game Object appear pixelated, to a varying degree.
* [Shine](#shine) : Run a 'shine' effect across a Game Object, either additively or as part of a reveal.
* [Shadow](#shadow) : Add a drop shadow behind a Game Object, with custom depth and color.
* [Vignette](#vignette) : Apply a vignette around a Game Object, with custom offset position, radius and color.
* [Wipe](#wipe) / [Reveal](#reveal) : Set a Game Object to 'wipe' or 'reveal' with custom line width, direction and axis of the effect.

Texture-based Game Objects also support Pre FX, including: Image, Sprite, TileSprite, Text, RenderTexture, Video.

All Game Objects and camera support Post FX. These are effects applied after the Game Object has been rendered.

* Author: Richard Davey
* Pre-fx, and Post-fx shader effects

!!! warning "WebGL only"
Only work in WebGL render mode.

## Live demos

* [Official demos](https://labs.phaser.io/index.html?dir=3.60/fx/&q=)

## Barrel

* Add pre-fx to game object

  ```
  Copy// gameObject.preFX.setPadding(padding);
  var effect = gameObject.preFX.addBarrel(amount);

  ```

  + `padding` : The amount of padding to add to this Game Object, in pixels.
    - Used when `amount` is larger than `1`.
  + `amount` : The amount of distortion applied to the barrel effect.
    - `1` : No distortion
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addBarrel(amount);

  ```

  ```
  Copyvar effect = camera.postFX.addBarrel(amount);

  ```
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Properties

  ```
  Copyeffect.amount = amount;

  ```

## Bloom

* Add pre-fx to game object

  ```
  Copyvar effect = gameObject.preFX.addBloom(color, offsetX, offsetY, blurStrength, strength, steps);

  ```

  + `color` : The color of the Bloom, as a hex value.
  + `offsetX`, `offsetY` : The horizontal/vertical offset of the bloom effect. Default value is `1`.
  + `blurStrength` , `strength` : The strength of the blur/blend process of the bloom effect. Default value is `1`.
  + `steps` : The number of steps to run the Bloom effect for. This value should always be an integer. Default value is `4`.
    - The higher the value, the smoother the Bloom, but at the cost of exponentially more gl operations.
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addBloom(color, offsetX, offsetY, blurStrength, strength, steps);

  ```

  ```
  Copyvar effect = camera.postFX.addBloom(color, offsetX, offsetY, blurStrength, strength, steps);

  ```
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Properties

  ```
  Copyeffect.color = color;  // hex value
  effect.offsetX = offsetX;
  effect.offsetY = offsetY;
  effect.blurStrength = blurStrength;
  effect.strength = strength;
  effect.steps = steps; // integer

  ```

## Blur

* Add pre-fx to game object

  ```
  Copyvar effect = gameObject.preFX.addBlur(quality, x, y, strength, color, steps);

  ```

  + `quality` : The quality of the blur effect. Default value is `0`.
    - `0` : Low Quality
    - `1` : Medium Quality
    - `2` : High Quality
  + `x`, `y` : The horizontal/vertical offset of the blur effect. Default value is `2`
  + `strength` : The strength of the blur effect. Default value is `1`.
  + `color` : The color of the blur, as a hex value. Default value is `0xffffff`.
  + `steps` : The number of steps to run the blur effect for. This value should always be an integer.
    - The higher the value, the smoother the blur, but at the cost of exponentially more gl operations.
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addBlur(quality, x, y, strength, color, steps);

  ```

  ```
  Copyvar effect = camera.postFX.addBlur(quality, x, y, strength, color, steps);

  ```
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Properties

  ```
  Copyeffect.quality = quality;
  effect.x = x;
  effect.y = y;
  effect.strength = strength;
  effect.color = color;
  effect.steps = steps;

  ```

## Bokeh

* Add pre-fx to game object

  ```
  Copyvar effect = gameObject.preFX.addBokeh(radius, amount, contrast);

  ```

  + `radius` : The radius of the bokeh effect. Default value is `0.5`.
  + `amount` : The amount of the bokeh effect. Default value is `1`.
  + `contrast` : The color contrast of the bokeh effect. Default value is `0.2`.
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addBlur(quality, x, y, strength, color, steps);

  ```

  ```
  Copyvar effect = camera.postFX.addBokeh(radius, amount, contrast);

  ```
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Properties

  ```
  Copyeffect.radius = radius;
  effect.amount = amount;
  effect.contrast = contrast;

  ```

## Tilt Shift

* Add pre-fx to game object

  ```
  Copyvar effect = gameObject.preFX.addTiltShift(radius, amount, contrast, blurX, blurY, strength);

  ```

  + `radius` : The radius of the bokeh effect. Default value is `0.5`.
  + `amount` : The amount of the bokeh effect. Default value is `1`.
  + `contrast` : The color contrast of the bokeh effect. Default value is `0.2`.
  + `blurX`, `blurY` : The amount of horizontal/vertical blur.
  + `strength` : The strength of the blur.
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addTiltShift(radius, amount, contrast, blurX, blurY, strength);

  ```

  ```
  Copyvar effect = camera.postFX.addTiltShift(radius, amount, contrast, blurX, blurY, strength);

  ```
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Properties

  ```
  Copyeffect.radius = radius;
  effect.amount = amount;
  effect.contrast = contrast;
  effect.blurX = blurX;
  effect.blurY = blurY;
  effect.strength = strength;

  ```

## Circle Outline

* Add pre-fx to game object

  ```
  Copyvar effect = gameObject.preFX.addCircle(thickness, color, backgroundColor, scale, feather);

  ```

  + `thickness` : The width of the circle around the texture, in pixels. Default value is `8`.
  + `color` : The color of the circular ring, given as a number value. Default value is `0xfeedb6`.
  + `backgroundColor` : The color of the background, behind the texture, given as a number value. Default value is `0xff0000`.
  + `scale` : The scale of the circle. Default value is `1`.
    - `1` : Full size of the underlying texture.
  + `feather` : The amount of feathering to apply to the circle from the ring. Default value is `0.005`.
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addCircle(thickness, color, backgroundColor, scale, feather);

  ```

  ```
  Copyvar effect = camera.postFX.addCircle(thickness, color, backgroundColor, scale, feather);

  ```
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Properties

  ```
  Copyeffect.thickness = thickness;
  effect.color = color;
  effect.backgroundColor = backgroundColor;
  effect.backgroundAlpha = backgroundAlpha;
  effect.scale = scale;
  effect.feather = feather;

  ```

## ColorMatrix

* Add pre-fx to game object

  ```
  Copyvar effect = gameObject.preFX.addColorMatrix();

  ```
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addColorMatrix();

  ```

  ```
  Copyvar effect = camera.postFX.addColorMatrix();

  ```
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Methods

  + Brightness : Changes the brightness of this ColorMatrix by the given amount.

    ```
    Copyeffect.brightness(value, multiply);

    ```

    - `value` : The amount of brightness to apply to this ColorMatrix. `0`(black)~`1`. Default value is `0`.
    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + Saturate : Changes the saturation of this ColorMatrix by the given amount.

    ```
    Copyeffect.saturate(value, multiply);

    ```

    - `value` : The amount of saturation to apply to this ColorMatrix. Default value is `0`.
    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + Desaturate : Desaturates this ColorMatrix (removes color from it).

    ```
    Copyeffect.desaturate(value, multiply);

    ```

    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + Hue : Rotates the hues of this ColorMatrix by the value given.

    ```
    Copyeffect.hue(rotation, multiply);

    ```

    - `rotation` : The amount of hue rotation to apply to this ColorMatrix, in degrees. Default value is `0`.
    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + Grayscale : Sets this ColorMatrix to be grayscale.

    ```
    Copyeffect.grayscale(value, multiply);

    ```

    - `value` : The grayscale scale `0`(black)~`1`. Default value is `1`.
    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + BlackWhite : Sets this ColorMatrix to be black and white.

    ```
    Copyeffect.blackWhite(multiply);

    ```

    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + Contrast : Change the contrast of this ColorMatrix by the amount given.

    ```
    Copyeffect.contrast(value, multiply);

    ```

    - `value` : The amount of contrast to apply to this ColorMatrix. Default value is `0`.
    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + Negative : Converts this ColorMatrix to have negative values.

    ```
    Copyeffect.negative(multiply);

    ```

    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + DesaturateLuminance : Apply a desaturated luminance to this ColorMatrix.

    ```
    Copyeffect.desaturateLuminance(multiply);

    ```

    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + Sepia : Applies a sepia tone to this ColorMatrix.

    ```
    Copyeffect.sepia(multiply);

    ```

    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + Night : Applies a night vision tone to this ColorMatrix.

    ```
    Copyeffect.night(intensity, multiply);

    ```

    - `intensity` : The intensity of this effect. Default value is `0.1`.
    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + LSD : Applies a trippy color tone to this ColorMatrix.

    ```
    Copyeffect.lsd(multiply);

    ```

    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + Brown : Applies a brown tone to this ColorMatrix.

    ```
    Copyeffect.brown(multiply);

    ```

    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + VintagePinhole : Applies a vintage pinhole color effect to this ColorMatrix.

    ```
    Copyeffect.vintagePinhole(multiply);

    ```

    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + Kodachrome : Applies a kodachrome color effect to this ColorMatrix.

    ```
    Copyeffect.kodachrome(multiply);

    ```

    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + Technicolor : Applies a technicolor color effect to this ColorMatrix.

    ```
    Copyeffect.technicolor(multiply);

    ```

    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + Polaroid : Applies a polaroid color effect to this ColorMatrix.

    ```
    Copyeffect.polaroid(multiply);

    ```

    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.
  + ShiftToBGR : Shifts the values of this ColorMatrix into BGR order.

    ```
    Copyeffect.shiftToBGR(multiply);

    ```

    - `multiply` : Multiply the resulting ColorMatrix (`true`), or set it (`false`) ?
      * `true` : Multiply the resulting.
      * `false` : Set the resulting. Default behavior.

## Displacement

* Add pre-fx to game object

  ```
  Copyvar effect = gameObject.preFX.addDisplacement(texture, x, y);

  ```

  + `texture` : The unique string-based key of the texture to use for displacement, which must exist in the Texture Manager. Default value is `'__WHITE'`.
    - You can only use a whole texture, not a frame from a texture atlas or sprite sheet.
  + `x`, `y` : The amount of horizontal/vertical displacement to apply. Default value is `0.005`.
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addDisplacement(texture, x, y);

  ```

  ```
  Copyvar effect = camera.postFX.addDisplacement(texture, x, y);

  ```
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Properties

  ```
  Copyeffect.x = x;
  effect.y = y;    

  ```
* Methods

  + Set texture

    ```
    Copyeffect.setTexture(key);

    ```

## Glow

* Add pre-fx to game object

  ```
  Copy// gameObject.preFX.setPadding(padding);
  var effect = gameObject.preFX.addGlow(color, outerStrength, innerStrength, knockout);

  ```

  + `padding` : The amount of padding to add to this Game Object, in pixels.
    - Used when `amount` is larger than `1`.
  + `color` : The color of the glow effect as a number value. Default value is `0xffffff`.
  + `outerStrength`, `innerStrength` : The strength of the glow outward/inward from the edge of the Sprite. Default value is `4`/`0`.
  + `knockout` :
    - `true` : Only the glow is drawn
    - `false` : Draw glow and texture. Default behavior.
  + `quality` : Only available for PostFX. Sets the quality of this Glow effect. Default is 0.1. Cannot be changed post-creation.
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addGlow(color, outerStrength, innerStrength, knockout, quality, distance);

  ```

  ```
  Copyvar effect = camera.postFX.addGlow(color, outerStrength, innerStrength, knockout, quality, distance);

  ```

  + `quality` : Sets the quality of this Glow effect. Default is `0.1`. Cannot be changed post-creation.
  + `distance` : Sets the distance of this Glow effect. Default is `10`. Cannot be changed post-creation.
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Properties

  ```
  Copyeffect.color = color;
  effect.outerStrength = outerStrength;
  effect.innerStrength = innerStrength;
  effect.knockout = knockout;

  ```

## Gradient

* Add pre-fx to game object

  ```
  Copyvar effect = gameObject.preFX.addGradient(color1, color2, alpha, fromX, fromY, toX, toY, size);

  ```

  + `color1`, `color2` : The first/second gradient color, given as a number value. Default values are `0xff0000`/`0x00ff00`.
  + `alpha` : The alpha value of the gradient effect.
  + `fromX`, `fromY` : The horizontal/vertical position the gradient will start from. Value between `0` and `1`.
  + `toX`, `toY` : The horizontal/vertical position the gradient will end at. Value between `0` and `1`.
  + `size` : How many 'chunks' the gradient is divided in to, as spread over the entire height of the texture.
    - `0` : Smooth gradient. Default behavior.
    - Others : Retro chunky effect.
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addGradient(color1, color2, alpha, fromX, fromY, toX, toY, size);

  ```

  ```
  Copyvar effect = camera.postFX.addGradient(color1, color2, alpha, fromX, fromY, toX, toY, size);

  ```
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Properties

  ```
  Copyeffect.color1 = color1;
  effect.color2 = color2;
  effect.alpha = alpha;
  effect.fromX = fromX;
  effect.fromY = fromY;
  effect.toX = toX;
  effect.toY = toY;
  effect.size = size;

  ```

## Pixelate

* Add pre-fx to game object

  ```
  Copyvar effect = gameObject.preFX.addPixelate(amount);

  ```

  + `amount` : The amount of pixelation to apply, in pixels.
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addPixelate(amount);

  ```

  ```
  Copyvar effect = camera.postFX.addPixelate(amount);

  ```
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Properties

  ```
  Copyeffect.amount = amount;

  ```

## Shadow

* Add pre-fx to game object

  ```
  Copy// gameObject.preFX.setPadding(padding);
  var effect = gameObject.preFX.addShadow(x, y, decay, power, color, samples, intensity);

  ```

  + `padding` : The amount of padding to add to this Game Object, in pixels.
    - Used when `amount` is larger than `1`.
  + `x`, `y` : The horizontal/vertical offset of the shadow effect. Default value is `0`.
  + `decay` : The amount of decay for shadow effect. Default value is `0.1`.
  + `power` : The power of the shadow effect. Default value is `1`.
  + `color` : The color of the shadow. Default value is `0x000000`.
  + `samples` : The number of samples that the shadow effect will run for. An integer between `1` and `12`.
  + `intensity` : The intensity of the shadow effect. Default value is `1`.
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addShadow(x, y, decay, power, color, samples, intensity);

  ```

  ```
  Copyvar effect = camera.postFX.addShadow(x, y, decay, power, color, samples, intensity);

  ```
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Properties

  ```
  Copyeffect.x = x;
  effect.y = y;
  effect.decay = decay;
  effect.power = power;
  effect.color = color;
  effect.samples = samples;
  effect.intensity = intensity;

  ```

## Shine

* Add pre-fx to game object

  ```
  Copyvar effect = gameObject.preFX.addShine(speed, lineWidth, gradient, reveal);

  ```

  + `speed` : The speed of the Shine effect. Default value is `0.5`.
  + `lineWidth` : The line width of the Shine effect. Default value is `0.5`.
  + `gradient` : The gradient of the Shine effect. Default value is `3`.
  + `reveal` : Does this Shine effect reveal or get added to its target?
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addShine(speed, lineWidth, gradient, reveal);

  ```

  ```
  Copyvar effect = camera.postFX.addShine(speed, lineWidth, gradient, reveal);

  ```
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Properties

  ```
  Copyeffect.speed = speed;
  effect.lineWidth = lineWidth;
  effect.gradient = gradient;
  effect.reveal = reveal;

  ```

## Vignette

* Add pre-fx to game object

  ```
  Copyvar effect = gameObject.preFX.addVignette(x, y, radius, strength);

  ```

  + `x`, `y` : The horizontal/vertical offset of the vignette effect. Value is between `0` and `1`. Default value is `0.5`.
  + `radius` : The radius of the vignette effect. Value is between `0` and `1`. Default value is `0.5`.
  + `strength` : The strength of the vignette effect. Default value is `0.5`.
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addVignette(x, y, radius, strength);

  ```

  ```
  Copyvar effect = camera.postFX.addVignette(x, y, radius, strength);

  ```
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Properties

  ```
  Copyeffect.x = x;
  effect.y = y;
  effect.radius = radius;
  effect.strength = strength;

  ```

## Wipe

* Add pre-fx to game object

  ```
  Copyvar effect = gameObject.preFX.addWipe(wipeWidth, direction, axis);

  ```

  + `wipeWidth` : The width of the wipe effect. Value is between `0` and `1`. Default value is `0.1`.
  + `direction` : The direction of the wipe effect.
    - `0` : Left to right, or top to bottom
    - `1` : Right to left, or bottom to top
  + `axis` : The axis of the wipe effect.
    - `0` : Left to right, or right to left
    - `1` : Bottom to top, or top to bottom
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addWipe(wipeWidth, direction, axis);

  ```

  ```
  Copyvar effect = camera.postFX.addWipe(wipeWidth, direction, axis);

  ```
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Properties

  ```
  Copyeffect.progress = t; // 0~1
  effect.wipeWidth = wipeWidth;
  effect.direction = direction;  // 0, 1
  effect.axis = axis;  // 0, 1    

  ```

## Reveal

* Add pre-fx to game object

  ```
  Copyvar effect = gameObject.preFX.addReveal(wipeWidth, direction, axis);

  ```

  + `wipeWidth` : The width of the wipe effect. Value is between `0` and `1`. Default value is `0.1`.
  + `direction` : The direction of the wipe effect.
    - `0` : Left to right, or top to bottom
    - `1` : Right to left, or bottom to top
  + `axis` : The axis of the wipe effect.
    - `0` : Left to right, or right to left
    - `1` : Bottom to top, or top to bottom
* Add post-fx to game object, or camera

  ```
  Copyvar effect = gameObject.postFX.addReveal(wipeWidth, direction, axis);

  ```

  ```
  Copyvar effect = camera.postFX.addReveal(wipeWidth, direction, axis);

  ```
* Disable effect

  ```
  Copyeffect.setActive(false);
  // effect.active = false;

  ```
* Remove effect

  ```
  CopygameObject.preFX.remove(effect);

  ```

  ```
  Copycamera.postFX.remove(effect);

  ```
* Properties

  ```
  Copyeffect.progress = t; // 0~1
  effect.wipeWidth = wipeWidth;
  effect.direction = direction;  // 0, 1
  effect.axis = axis;  // 0, 1

  ```

## Remove all effects

```
CopygameObject.preFX.clear();

```

```
CopygameObject.postFX.clear();

```

```
Copycamera.postFX.clear();

```

## Disable all effects

```
CopygameObject.preFX.disable();
// gameObject.preFX.disable(true);  // Also remove all effects

```

```
CopygameObject.postFX.disable();
// gameObject.postFX.disable(true);  // Also remove all effects

```

```
Copycamera.postFX.disable();
// camera.postFX.disable(true);  // Also remove all effects

```

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Events](events.md)

[Game](game.md)

On this page

* [FX](#fx)

  + [Live demos](#live-demos)
  + [Barrel](#barrel)
  + [Bloom](#bloom)
  + [Blur](#blur)
  + [Bokeh](#bokeh)
  + [Tilt Shift](#tilt-shift)
  + [Circle Outline](#circle-outline)
  + [ColorMatrix](#colormatrix)
  + [Displacement](#displacement)
  + [Glow](#glow)
  + [Gradient](#gradient)
  + [Pixelate](#pixelate)
  + [Shadow](#shadow)
  + [Shine](#shine)
  + [Vignette](#vignette)
  + [Wipe](#wipe)
  + [Reveal](#reveal)
  + [Remove all effects](#remove-all-effects)
  + [Disable all effects](#disable-all-effects)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../index.md)