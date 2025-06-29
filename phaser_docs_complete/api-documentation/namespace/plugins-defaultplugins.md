# Phaser.Plugins.DefaultPlugins

Scope:
static

> Source: [src/plugins/DefaultPlugins.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/DefaultPlugins.js#L7)  
> Since: 3.0.0

# Static functions

## CoreScene

### CoreScene: array

**Description:**

These are the core plugins that are installed into every Scene.Systems instance, no matter what.

They are optionally exposed in the Scene as well (see the InjectionMap for details)

They are created in the order in which they appear in this array and EventEmitter is always first.

> Source: [src/plugins/DefaultPlugins.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/DefaultPlugins.js#L39)  
> Since: 3.0.0

---

## DefaultScene

### DefaultScene: array

**Description:**

These plugins are created in Scene.Systems in addition to the CoreScenePlugins.

You can elect not to have these plugins by either creating a DefaultPlugins object as part

of the Game Config, by creating a Plugins object as part of a Scene Config, or by modifying this array

and building your own bundle.

They are optionally exposed in the Scene as well (see the InjectionMap for details)

They are always created in the order in which they appear in the array.

> Source: [src/plugins/DefaultPlugins.js#L62](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/DefaultPlugins.js#L62)  
> Since: 3.0.0

---

## Global

### Global: array

**Description:**

These are the Global Managers that are created by the Phaser.Game instance.

They are referenced from Scene.Systems so that plugins can use them.

> Source: [src/plugins/DefaultPlugins.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/DefaultPlugins.js#L17)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [CoreScene](#corescene)

    - [CoreScene: array](#corescene-array)
  + [DefaultScene](#defaultscene)

    - [DefaultScene: array](#defaultscene-array)
  + [Global](#global)

    - [Global: array](#global-array)

Back to top

©2025[Phaser](https://docs.phaser.io)