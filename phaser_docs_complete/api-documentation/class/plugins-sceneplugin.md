# ScenePlugin

Phaser.Plugins.ScenePlugin

A Scene Level Plugin is installed into every Scene and belongs to that Scene.

It can listen for Scene events and respond to them.

It can map itself to a Scene property, or into the Scene Systems, or both.

**Constructor**

`new ScenePlugin(scene, pluginManager, pluginKey)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | A reference to the Scene that has installed this plugin. |
| --- | --- | --- | --- |
| pluginManager | [Phaser.Plugins.PluginManager](plugins-pluginmanager.md) | No | A reference to the Plugin Manager. |
| pluginKey | string | No | The key under which this plugin has been installed into the Scene Systems. |

---

**Scope**: static

**Extends**

> [Phaser.Plugins.BasePlugin](plugins-baseplugin.md)

> Source: [src/plugins/ScenePlugin.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/ScenePlugin.js#L11)  
> Since: 3.8.0

# Public Members

## game

### game: [Phaser.Game](game.md)

**Description:**

A reference to the Game instance this plugin is running under.

**Access:** protected

**Inherits:** [Phaser.Plugins.BasePlugin#game](plugins-baseplugin.md)

> Source: [src/plugins/BasePlugin.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/BasePlugin.js#L38)  
> Since: 3.8.0

---

## pluginKey

### pluginKey: string

**Description:**

The key under which this plugin was installed into the Scene Systems.

This property is only set when the plugin is instantiated and added to the Scene, not before.

You can use it during the `boot` method.

> Source: [src/plugins/ScenePlugin.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/ScenePlugin.js#L63)  
> Since: 3.54.0

---

## pluginManager

### pluginManager: [Phaser.Plugins.PluginManager](plugins-pluginmanager.md)

**Description:**

A handy reference to the Plugin Manager that is responsible for this plugin.

Can be used as a route to gain access to game systems and events.

**Access:** protected

**Inherits:** [Phaser.Plugins.BasePlugin#pluginManager](plugins-baseplugin.md)

> Source: [src/plugins/BasePlugin.js#L27](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/BasePlugin.js#L27)  
> Since: 3.8.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

A reference to the Scene that has installed this plugin.

Only set if it's a Scene Plugin, otherwise `null`.

This property is only set when the plugin is instantiated and added to the Scene, not before.

You can use it during the `boot` method.

**Access:** protected

> Source: [src/plugins/ScenePlugin.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/ScenePlugin.js#L37)  
> Since: 3.8.0

---

## systems

### systems: [Phaser.Scenes.Systems](scenes-systems.md)

**Description:**

A reference to the Scene Systems of the Scene that has installed this plugin.

Only set if it's a Scene Plugin, otherwise `null`.

This property is only set when the plugin is instantiated and added to the Scene, not before.

You can use it during the `boot` method.

**Access:** protected

> Source: [src/plugins/ScenePlugin.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/ScenePlugin.js#L50)  
> Since: 3.8.0

---

# Public Methods

## boot

### <instance> boot()

**Description:**

This method is called when the Scene boots. It is only ever called once.

By this point the plugin properties `scene` and `systems` will have already been set.

In here you can listen for [Scene](../namespace/Phaser.Scenes.Events.md) and set-up whatever you need for this plugin to run.

Here are the Scene events you can listen to:

* start
* ready
* preupdate
* update
* postupdate
* resize
* pause
* resume
* sleep
* wake
* transitioninit
* transitionstart
* transitioncomplete
* transitionout
* shutdown
* destroy

At the very least you should offer a destroy handler for when the Scene closes down, i.e:

```
Copy
var eventEmitter = this.systems.events;

eventEmitter.once('destroy', this.sceneDestroy, this);


```

> Source: [src/plugins/ScenePlugin.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/ScenePlugin.js#L79)  
> Since: 3.8.0

---

## destroy

### <instance> destroy()

**Description:**

Game instance has been destroyed.

You must release everything in here, all references, all objects, free it all up.

**Overrides:** Phaser.Plugins.BasePlugin#destroy

> Source: [src/plugins/ScenePlugin.js#L118](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/ScenePlugin.js#L118)  
> Since: 3.8.0

---

## init

### <instance> init([data])

**Description:**

The PluginManager calls this method on a Global Plugin when the plugin is first instantiated.

It will never be called again on this instance.

In here you can set-up whatever you need for this plugin to run.

If a plugin is set to automatically start then `BasePlugin.start` will be called immediately after this.

On a Scene Plugin, this method is never called. Use [Phaser.Plugins.ScenePlugin#boot](plugins-sceneplugin.md) instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | any | Yes | A value specified by the user, if any, from the `data` property of the plugin's configuration object (if started at game boot) or passed in the PluginManager's `install` method (if started manually). |
| --- | --- | --- | --- |

**Inherits:** [Phaser.Plugins.BasePlugin#init](plugins-baseplugin.md)

> Source: [src/plugins/BasePlugin.js#L49](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/BasePlugin.js#L49)  
> Since: 3.8.0

---

## start

### <instance> start()

**Description:**

The PluginManager calls this method on a Global Plugin when the plugin is started.

If a plugin is stopped, and then started again, this will get called again.

Typically called immediately after `BasePlugin.init`.

On a Scene Plugin, this method is never called.

**Inherits:** [Phaser.Plugins.BasePlugin#start](plugins-baseplugin.md)

> Source: [src/plugins/BasePlugin.js#L65](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/BasePlugin.js#L65)  
> Since: 3.8.0

---

## stop

### <instance> stop()

**Description:**

The PluginManager calls this method on a Global Plugin when the plugin is stopped.

The game code has requested that your plugin stop doing whatever it does.

It is now considered as 'inactive' by the PluginManager.

Handle that process here (i.e. stop listening for events, etc)

If the plugin is started again then `BasePlugin.start` will be called again.

On a Scene Plugin, this method is never called.

**Inherits:** [Phaser.Plugins.BasePlugin#stop](plugins-baseplugin.md)

> Source: [src/plugins/BasePlugin.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/BasePlugin.js#L92)  
> Since: 3.8.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [pluginKey](#pluginkey)

    - [pluginKey: string](#pluginkey-string)
  + [pluginManager](#pluginmanager)

    - [pluginManager: Phaser.Plugins.PluginManager](#pluginmanager-phaserpluginspluginmanager)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [systems](#systems)

    - [systems: Phaser.Scenes.Systems](#systems-phaserscenessystems)
* [Public Methods](#public-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [init](#init)

    - [<instance> init([data])](#instance-initdata)
  + [start](#start)

    - [<instance> start()](#instance-start)
  + [stop](#stop)

    - [<instance> stop()](#instance-stop)

Back to top

©2025[Phaser](https://docs.phaser.io)