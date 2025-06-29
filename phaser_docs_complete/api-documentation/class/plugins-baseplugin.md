# BasePlugin

Phaser.Plugins.BasePlugin

A Global Plugin is installed just once into the Game owned Plugin Manager.

It can listen for Game events and respond to them.

**Constructor**

`new BasePlugin(pluginManager)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| pluginManager | [Phaser.Plugins.PluginManager](plugins-pluginmanager.md) | No | A reference to the Plugin Manager. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/plugins/BasePlugin.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/BasePlugin.js#L9)  
> Since: 3.8.0

# Public Members

## game

### game: [Phaser.Game](game.md)

**Description:**

A reference to the Game instance this plugin is running under.

**Access:** protected

> Source: [src/plugins/BasePlugin.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/BasePlugin.js#L38)  
> Since: 3.8.0

---

## pluginManager

### pluginManager: [Phaser.Plugins.PluginManager](plugins-pluginmanager.md)

**Description:**

A handy reference to the Plugin Manager that is responsible for this plugin.

Can be used as a route to gain access to game systems and events.

**Access:** protected

> Source: [src/plugins/BasePlugin.js#L27](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/BasePlugin.js#L27)  
> Since: 3.8.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Game instance has been destroyed.

You must release everything in here, all references, all objects, free it all up.

> Source: [src/plugins/BasePlugin.js#L107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/plugins/BasePlugin.js#L107)  
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
  + [pluginManager](#pluginmanager)

    - [pluginManager: Phaser.Plugins.PluginManager](#pluginmanager-phaserpluginspluginmanager)
* [Public Methods](#public-methods)

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



BasePlugin