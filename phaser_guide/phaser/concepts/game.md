# Game

Game

If you look at any Phaser example you'll see they all create an instance of the Phaser.Game class. Indeed, without it, nothing will actually happen. This one class can be considered as the heart of your game, for without it, nothing will run.

Typically, you only ever have one instance of a Phaser game at any given time. The Game class itself doesn't do a great deal, and beyond creating it, you rarely ever interact with it. Yet it's responsible for creating and updating all of the internal systems that your game needs while it is executing.

Even if you're creating the type of game that consists of lots of smaller games (think Mario Party, or Wario Ware), you'll still only ever have one instance of the Phaser Game class itself.

## Creating a basic Phaser Game instance

```
Copynew Phaser.Game({
  scene: {
    create: function () {
      this.add.text(0, 0, 'Hello world');
    }
  }
});

```

It's not necessary to wait for [DOMContentLoaded](https://developer.mozilla.org/en-US/docs/Web/API/Window/DOMContentLoaded_event) or [window.onload](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event) before creating the game.

But if you have external stylesheets or images that affect page layout and you're using the Scale Manager, you may need to use [window.onload](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event).

The game is available on all scenes as `this.game` and is passed as an argument to relevant callbacks and event listeners, so you usually don't need to save a reference to the game unless you need to reach it from outside Phaser.

## Game configuration

* Basic game configuration object:

  ```
  Copyconst config = {
      type: Phaser.AUTO, // automatically detect browser WebGL support
      width: 800, // canvas width
      height: 600, // canvas height
      backgroundColor: '#2d2d2d', // canvas background color
      parent: 'phaser-example', // parent DOM element
      scene: Example // 
  };

  ```
* [Game config examples](https://labs.phaser.io/index.html?dir=game%20config/&q=)

You can read about the full list of [config options here](../../docs/latest/Phaser.Types.Core.GameConfig.md). For historical reasons, some config values can be set in two places: e.g., `width` and `height` are the same as `scale.width` and `scale.height`.

For most cases, you should add scenes and any plugins directly to the game config, as that's the simplest method.

Any special startup work should usually be done in the `preBoot` or `postBoot` callbacks.

`preBoot` runs only after [DOMContentLoaded](https://developer.mozilla.org/en-US/docs/Web/API/Window/DOMContentLoaded_event). `game.config` and `game.device` are available. **Some** `game.config` values can still be modified here. Most game systems have not been set up yet. You can add scenes to the game here. The game's [BOOT](../../docs/latest/Phaser.Core.Events.BOOT.md) event happens around the same time.

`postBoot` runs after all the game systems are ready. The game's [READY](../../docs/latest/Phaser.Core.Events.READY.md) event happens around the same time. Any scenes added before this are available (not pending) and have started if set to do so.

The game loop starts immediately after `postBoot`.

```
Copyconst config = {
    preBoot: function (game) {
      // Config (including defaults) has been created.
      console.log('game config' game.config);
    },
    postBoot: function (game) {
      // Game canvas has been created.
      console.log('game canvas', game.canvas);
    }
};

const game = new Phaser.Game(config);

```

## Global members

### Scene manager

Global [scene manager](scenes.md) in `game.scene`, or `scene.scene` in each scene.

### Data manager

Instance of [data manager](data-manager.md) in `game.registry`, or `scene.registry` in each scene.

* Get the data manager:

  ```
  Copyvar value = scene.registry.get(key);
  // var value = game.registry.get(key);

  ```
* Add / update data in the data manager:

  ```
  Copyscene.registry.set(key, value);
  // game.registry.set(key, value);

  ```
* Events

  + Set data events:

    ```
    Copyscene.registry.events.on('setdata', function(parent, key, value){ /* ... */ });
    // game.registry.events.on('setdata', function(parent, key, value){ /* ... */ })

    ```
  + Change data events:

    ```
    Copyscene.registry.events.on('changedata', function(parent, key, value, previousValue){ /* ... */ });
    // game.registry.events.on('changedata', function(parent, key, value, previousValue){ /* ... */ })

    ```

    ```
    Copyscene.registry.events.on('changedata-' + key, function(parent, value, previousValue){ /* ... */ });
    // game.registry.events.on('changedata-' + key, function(parent, value, previousValue){ /* ... */ });

    ```

### Game time

* The time that the current game step started at.

  ```
  Copyvar time = game.getTime();
  // var time = scene.game.getTime();

  ```
* The current game frame.

  ```
  Copyvar frameCount = game.getFrame();
  // var frameCount = scene.game.getFrame();

  ```
* The delta time, since the last game step. This is a clamped and smoothed average value.

  ```
  Copyvar delta = game.loop.delta;
  // var delta = scene.game.loop.delta;

  ```

### Game config

```
Copyvar config = game.config;
// var config = scene.game.config;

```

### Window size

* Window width:

  ```
  Copyvar width = game.config.width;
  // var width = scene.game.config.width;

  ```
* Window height:

  ```
  Copyvar height = game.config.height;
  // var height = scene.game.config.height;

  ```

## Pause and resume

You can pause or resume the entire game with its `pause()` and `resume()` methods. You won't be able to resume the game from Phaser's input events, though, since they're also paused.

* Pause the entire game and emit a `PAUSE` event.

  ```
  Copygame.pause();

  ```
* Resume the entire game and emit a `RESUME` event.

  ```
  Copygame.resume();


  ```
* Is paused

  ```
  Copyvar isPaused = game.isPaused;

  ```

## Events

[Game events](../../docs/latest/Phaser.Core.Events.md) are emitted from the game's `events`.

`FOCUS` and `BLUR` happen when the game window or frame gains or loses focus by the user's mouse clicks or key presses.

`HIDDEN` and `VISIBLE` happen when the game tab or window is hidden, switched away from, minimized, or restored, per the [Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API). Operating systems can differ here. `PAUSE` and `RESUME` events usually occur at the same time.

You can emit and listen to your own events on this emitter as long you avoid Phaser's event names.

* Pause (window is invisible) / Resume (window is visible) events

  ```
  Copygame.events.on('pause', function() {});

  ```

  ```
  Copygame.events.on('resume', function() {});

  ```
* Destroy event, triggered by `game.destroy()`

  ```
  Copygame.events.on('destroy', function() {})

  ```
* On window focused/blurred events

  ```
  Copygame.events.on('focus', function() {})

  ```

  ```
  Copygame.events.on('blur', function(){ })

  ```

## Registry

The registry is the game's [data store](https://github.com/samme/phaser3-faq/wiki/Data).

There's no way to pass registry data directly through the game config, but you can do it in a callback:

```
Copyconst config = {
    callbacks: {
    preBoot: function (game) {
      game.registry.merge({
        highScore: 0
      });
    }
  }
};

const game = new Phaser.Game(config);

```

## Systems

| Game | Scene | Description | Notes |
| --- | --- | --- | --- |
| `anims` | `anims` | Animation Manager |  |
| --- | --- | --- | --- |
| `cache` | `cache` | Cache Manager |  |
| `device` | `game.device` | Device record |  |
| `events` | `game.events` | Global events emitter | The scene's `events` is its own emitter. |
| `input` | `input.manager` | Input Manager | Use the scene's Input Plugin `input` instead. |
| `loop` | `game.loop` | The game loop |  |
| `plugins` | `plugins` | Plugins Manager |  |
| `registry` | `registry` | Global registry |  |
| `renderer` | `renderer` | Renderer |  |
| `scale` | `scale` | Scale Manager |  |
| `scene` | `scene.manager` | Scene Manager | Use the scene's Scene Plugin `scene` instead. |
| `sound` | `sound` | Sound Manager |  |
| `textures` | `textures` | Texture Manager |  |

## Destroying the game instance

```
Copygame.destroy();
// game.destroy(removeCanvas, noReturn);

```

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)
* [samme](https://github.com/samme)

Updated on June 4, 2025, 1:16 PM UTC

---

[FX](fx.md)

[Game Objects](gameobjects.md)

On this page

* [Game](#game)

  + [Creating a basic Phaser Game instance](#creating-a-basic-phaser-game-instance)
  + [Game configuration](#game-configuration)
  + [Global members](#global-members)

    - [Scene manager](#scene-manager)
    - [Data manager](#data-manager)
    - [Game time](#game-time)
    - [Game config](#game-config)
    - [Window size](#window-size)
  + [Pause and resume](#pause-and-resume)
  + [Events](#events)
  + [Registry](#registry)
  + [Systems](#systems)
  + [Destroying the game instance](#destroying-the-game-instance)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../index.md)