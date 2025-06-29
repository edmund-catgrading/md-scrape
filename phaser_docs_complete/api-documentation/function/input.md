# Phaser.Input

## CreateInteractiveObject

### <static> CreateInteractiveObject(gameObject, hitArea, hitAreaCallback)

**Description:**

Creates a new Interactive Object.

This is called automatically by the Input Manager when you enable a Game Object for input.

The resulting Interactive Object is mapped to the Game Object's `input` property.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to which this Interactive Object is bound. |
| --- | --- | --- | --- |
| hitArea | any | No | The hit area for this Interactive Object. Typically a geometry shape, like a Rectangle or Circle. |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | No | The 'contains' check callback that the hit area shape will use for all hit tests. |

**Returns:** [Phaser.Types.Input.InteractiveObject](../typedef/types-input.md) - The new Interactive Object.

> Source: [src/input/CreateInteractiveObject.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/CreateInteractiveObject.js#L7)  
> Since: 3.0.0

## CreatePixelPerfectHandler

### <static> CreatePixelPerfectHandler(textureManager, alphaTolerance)

**Description:**

Creates a new Pixel Perfect Handler function.

Access via `InputPlugin.makePixelPerfect` rather than calling it directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| textureManager | [Phaser.Textures.TextureManager](../class/textures-texturemanager.md) | No | A reference to the Texture Manager. |
| --- | --- | --- | --- |
| alphaTolerance | number | No | The alpha level that the pixel should be above to be included as a successful interaction. |

**Returns:** function - The new Pixel Perfect Handler function.

> Source: [src/input/CreatePixelPerfectHandler.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/CreatePixelPerfectHandler.js#L7)  
> Since: 3.10.0

# Phaser.Input.InputPluginCache

## register

### <static> register(key, plugin, mapping, settingsKey, configKey)

**Description:**

Static method called directly by the Core internal Plugins.

Key is a reference used to get the plugin from the plugins object (i.e. InputPlugin)

Plugin is the object to instantiate to create the plugin

Mapping is what the plugin is injected into the Scene.Systems as (i.e. input)

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | A reference used to get this plugin from the plugin cache. |
| --- | --- | --- | --- |
| plugin | function | No | The plugin to be stored. Should be the core object, not instantiated. |
| mapping | string | No | If this plugin is to be injected into the Input Plugin, this is the property key used. |
| settingsKey | string | No | The key in the Scene Settings to check to see if this plugin should install or not. |
| configKey | string | No | The key in the Game Config to check to see if this plugin should install or not. |

> Source: [src/input/InputPluginCache.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPluginCache.js#L19)  
> Since: 3.10.0

## getPlugin

### <static> getPlugin(key)

**Description:**

Returns the input plugin object from the cache based on the given key.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the input plugin to get. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Input.InputPluginContainer](../typedef/types-input.md) - The input plugin object.

> Source: [src/input/InputPluginCache.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPluginCache.js#L40)  
> Since: 3.10.0

## install

### <static> install(target)

**Description:**

Installs all of the registered Input Plugins into the given target.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | [Phaser.Input.InputPlugin](../class/input-inputplugin.md) | No | The target InputPlugin to install the plugins into. |
| --- | --- | --- | --- |

> Source: [src/input/InputPluginCache.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPluginCache.js#L56)  
> Since: 3.10.0

## remove

### <static> remove(key)

**Description:**

Removes an input plugin based on the given key.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the input plugin to remove. |
| --- | --- | --- | --- |

> Source: [src/input/InputPluginCache.js#L85](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPluginCache.js#L85)  
> Since: 3.10.0

# Phaser.Input.Keyboard

## AdvanceKeyCombo

### <static> AdvanceKeyCombo(event, combo)

**Description:**

Used internally by the KeyCombo class.

Return `true` if it reached the end of the combo, `false` if not.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | KeyboardEvent | No | The native Keyboard Event. |
| --- | --- | --- | --- |
| combo | [Phaser.Input.Keyboard.KeyCombo](../class/input-keyboard-keycombo.md) | No | The KeyCombo object to advance. |

**Returns:** boolean - `true` if it reached the end of the combo, `false` if not.

> Source: [src/input/keyboard/combo/AdvanceKeyCombo.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/combo/AdvanceKeyCombo.js#L7)  
> Since: 3.0.0

## ProcessKeyCombo

### <static> ProcessKeyCombo(event, combo)

**Description:**

Used internally by the KeyCombo class.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | KeyboardEvent | No | The native Keyboard Event. |
| --- | --- | --- | --- |
| combo | [Phaser.Input.Keyboard.KeyCombo](../class/input-keyboard-keycombo.md) | No | The KeyCombo object to be processed. |

**Returns:** boolean - `true` if the combo was matched, otherwise `false`.

> Source: [src/input/keyboard/combo/ProcessKeyCombo.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/combo/ProcessKeyCombo.js#L9)  
> Since: 3.0.0

## ResetKeyCombo

### <static> ResetKeyCombo(combo)

**Description:**

Used internally by the KeyCombo class.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| combo | [Phaser.Input.Keyboard.KeyCombo](../class/input-keyboard-keycombo.md) | No | The KeyCombo to reset. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Input.Keyboard.KeyCombo](../class/input-keyboard-keycombo.md) - The KeyCombo.

> Source: [src/input/keyboard/combo/ResetKeyCombo.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/combo/ResetKeyCombo.js#L7)  
> Since: 3.0.0

## DownDuration

### <static> DownDuration(key, [duration])

**Description:**

Returns `true` if the Key was pressed down within the `duration` value given, based on the current

game clock time. Or `false` if it either isn't down, or was pressed down longer ago than the given duration.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | No |  | The Key object to test. |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 50 | The duration, in ms, within which the key must have been pressed down. |

**Returns:** boolean - `true` if the Key was pressed down within `duration` ms ago, otherwise `false`.

> Source: [src/input/keyboard/keys/DownDuration.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/DownDuration.js#L7)  
> Since: 3.0.0

## JustDown

### <static> JustDown(key)

**Description:**

The justDown value allows you to test if this Key has just been pressed down or not.

When you check this value it will return `true` if the Key is down, otherwise `false`.

You can only call justDown once per key press. It will only return `true` once, until the Key is released and pressed down again.

This allows you to use it in situations where you want to check if this key is down without using an event, such as in a core game loop.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | No | The Key to check to see if it's just down or not. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the Key was just pressed, otherwise `false`.

> Source: [src/input/keyboard/keys/JustDown.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/JustDown.js#L7)  
> Since: 3.0.0

## JustUp

### <static> JustUp(key)

**Description:**

The justUp value allows you to test if this Key has just been released or not.

When you check this value it will return `true` if the Key is up, otherwise `false`.

You can only call JustUp once per key release. It will only return `true` once, until the Key is pressed down and released again.

This allows you to use it in situations where you want to check if this key is up without using an event, such as in a core game loop.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | No | The Key to check to see if it's just up or not. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the Key was just released, otherwise `false`.

> Source: [src/input/keyboard/keys/JustUp.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/JustUp.js#L7)  
> Since: 3.0.0

## UpDuration

### <static> UpDuration(key, [duration])

**Description:**

Returns `true` if the Key was released within the `duration` value given, based on the current

game clock time. Or returns `false` if it either isn't up, or was released longer ago than the given duration.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | No |  | The Key object to test. |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 50 | The duration, in ms, within which the key must have been released. |

**Returns:** boolean - `true` if the Key was released within `duration` ms ago, otherwise `false`.

> Source: [src/input/keyboard/keys/UpDuration.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/UpDuration.js#L7)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [CreateInteractiveObject](#createinteractiveobject)

  + [<static> CreateInteractiveObject(gameObject, hitArea, hitAreaCallback)](#static-createinteractiveobjectgameobject-hitarea-hitareacallback)
* [CreatePixelPerfectHandler](#createpixelperfecthandler)

  + [<static> CreatePixelPerfectHandler(textureManager, alphaTolerance)](#static-createpixelperfecthandlertexturemanager-alphatolerance)
* [Phaser.Input.InputPluginCache](#phaserinputinputplugincache)

  + [register](#register)

    - [<static> register(key, plugin, mapping, settingsKey, configKey)](#static-registerkey-plugin-mapping-settingskey-configkey)
  + [getPlugin](#getplugin)

    - [<static> getPlugin(key)](#static-getpluginkey)
  + [install](#install)

    - [<static> install(target)](#static-installtarget)
  + [remove](#remove)

    - [<static> remove(key)](#static-removekey)
* [Phaser.Input.Keyboard](#phaserinputkeyboard)

  + [AdvanceKeyCombo](#advancekeycombo)

    - [<static> AdvanceKeyCombo(event, combo)](#static-advancekeycomboevent-combo)
  + [ProcessKeyCombo](#processkeycombo)

    - [<static> ProcessKeyCombo(event, combo)](#static-processkeycomboevent-combo)
  + [ResetKeyCombo](#resetkeycombo)

    - [<static> ResetKeyCombo(combo)](#static-resetkeycombocombo)
  + [DownDuration](#downduration)

    - [<static> DownDuration(key, [duration])](#static-downdurationkey-duration)
  + [JustDown](#justdown)

    - [<static> JustDown(key)](#static-justdownkey)
  + [JustUp](#justup)

    - [<static> JustUp(key)](#static-justupkey)
  + [UpDuration](#upduration)

    - [<static> UpDuration(key, [duration])](#static-updurationkey-duration)

Back to top

©2025[Phaser](https://docs.phaser.io)