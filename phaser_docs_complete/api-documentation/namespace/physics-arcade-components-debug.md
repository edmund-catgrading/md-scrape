# Phaser.Physics.Arcade.Components.Debug

Scope:
static

> Source: [src/physics/arcade/components/Debug.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Debug.js#L7)  
> Since: 3.0.0

# Static functions

## setDebug

### <instance> setDebug(showBody, showVelocity, bodyColor)

**Description:**

Sets the debug values of this body.

Bodies will only draw their debug if debug has been enabled for Arcade Physics as a whole.

Note that there is a performance cost in drawing debug displays. It should never be used in production.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| showBody | boolean | No | Set to `true` to have this body render its outline to the debug display. |
| --- | --- | --- | --- |
| showVelocity | boolean | No | Set to `true` to have this body render a velocity marker to the debug display. |
| bodyColor | number | No | The color of the body outline when rendered to the debug display. |

**Returns:** [Phaser.Physics.Arcade.Components.Debug](physics-arcade-components-debug.md) - This Game Object.

> Source: [src/physics/arcade/components/Debug.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Debug.js#L15)  
> Since: 3.0.0

---

## setDebugBodyColor

### <instance> setDebugBodyColor(value)

**Description:**

Sets the color of the body outline when it renders to the debug display.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The color of the body outline when rendered to the debug display. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Components.Debug](physics-arcade-components-debug.md) - This Game Object.

> Source: [src/physics/arcade/components/Debug.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Debug.js#L39)  
> Since: 3.0.0

---

# Static functions

## debugBodyColor

### debugBodyColor: number

**Description:**

The color of the body outline when it renders to the debug display.

> Source: [src/physics/arcade/components/Debug.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Debug.js#L98)  
> Since: 3.0.0

---

## debugShowBody

### debugShowBody: boolean

**Description:**

Set to `true` to have this body render its outline to the debug display.

> Source: [src/physics/arcade/components/Debug.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Debug.js#L56)  
> Since: 3.0.0

---

## debugShowVelocity

### debugShowVelocity: boolean

**Description:**

Set to `true` to have this body render a velocity marker to the debug display.

> Source: [src/physics/arcade/components/Debug.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Debug.js#L77)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [setDebug](#setdebug)

    - [<instance> setDebug(showBody, showVelocity, bodyColor)](#instance-setdebugshowbody-showvelocity-bodycolor)
  + [setDebugBodyColor](#setdebugbodycolor)

    - [<instance> setDebugBodyColor(value)](#instance-setdebugbodycolorvalue)
* [Static functions](#static-functions-1)

  + [debugBodyColor](#debugbodycolor)

    - [debugBodyColor: number](#debugbodycolor-number)
  + [debugShowBody](#debugshowbody)

    - [debugShowBody: boolean](#debugshowbody-boolean)
  + [debugShowVelocity](#debugshowvelocity)

    - [debugShowVelocity: boolean](#debugshowvelocity-boolean)

Back to top

©2025[Phaser](https://docs.phaser.io)



Phaser.Physics.Arcade.Components.Debug