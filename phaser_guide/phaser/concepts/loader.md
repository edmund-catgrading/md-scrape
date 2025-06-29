# Loader

Loader

The Loader, as the name implies, is responsible for loading any external assets that your game may require. Common asset types include images, texture atlases, sprite sheets, fonts, audio files and JSON data, but there are many more that Phaser can handle.

By default, every Scene has access to its own Loader instance. The Loader works on a queue-basis, which means you can add as many 'load requests' to it as you like and they all get added to an internal queue. You then tell the Loader to start and it will work through the queue, loading each asset in turn.

Scenes have a special method available to you called 'preload'. This method is called automatically by Phaser when the Scene starts. It's a good place to add all of your game assets to the Loader and you'll see this convention used heavily in our examples and third-party tutorials. However, you can also add assets to the Loader at any point in your game, not just from within the preload method.

When you add a file to the loader, you have to give it a string-based key. This is a unique identifier for that file and its related resource. For example, if you load an image and give it the key 'player', then you identify that image by the key 'player' from that point on. The keys are case-sensitive and their uniqueness is applied per file type. I.e. a sound file could have the key 'player' as well as an image file. String-based keys is a very important concept in Phaser and you'll see it used throughout the framework.

The files are loaded via built-in browser APIs, which often allows for many files to be downloaded in parallel, depending on the browser and server settings. The Loader is specialised in loading files based on network requests and across a network. It is not for loading files from the local file system, something that all modern web browsers prohibit for security reasons.

As with most systems in Phaser, there are lots of events you can listen for that come from the Loader. These events are naturally centered around the loading progress: such as which files have completed, or maybe failed, and how far along the process is. You can use these events to create loading bars and progress displays for your game.

## Strategy

* Load assets before using them
* Load shared assets in a "boot" or "preload" scene
* Load any non-shared assets in the scene they will be used in
* Use a scene payload to load small assets before the scene `preload()` callback, if needed
* For special cases, run the scene loader manually and access the newly loaded assets in event callbacks
* You can remove assets if they are no longer needed to save some memory

## Assets

There are many [types](../../docs/latest/Phaser.Loader.FileTypes.md), and you can read about all of them.

Assets need to be loaded before you can use them, but once loaded, they are available everywhere. It doesn't matter which loader or scene loaded them. Once loaded they are in the Texture Manager (`this.textures`) or the asset caches (`this.cache`).

Use unique keys (names) for assets.

### Where to load assets

In a single-scene game, you'll load assets in that scene, naturally.

In a multi-scene game, it's convenient to load shared assets in a "boot" or "preloader" scene and then start the other scenes afterwards. Any non-shared assets can be loaded in the scene that uses them, and removed if necessary when that scene shuts down.

### Asset types

#### Image

* Image

  ```
  Copythis.load.image(key, url);
  // this.load.image(key, url, xhrSettings);

  ```

  + `url` : Url of texture, or base64 string of Uri.
* Image and normal map

  ```
  Copythis.load.image(key, [url, normalMapUrl]);
  // this.load.image(key, [url, normalMapUrl], xhrSettings);

  ```

  + `url` : Url of texture, or base64 string of Uri.
  + `normalMapUrl` : Url of normal map.
* SVG

  ```
  Copythis.load.svg(key, url);
  // this.load.svg(key, url, svgConfig);
  // this.load.svg(key, url, svgConfig, xhrSettings);

  ```

  + `svgConfig` : `{width, height}`, or `{scale}`
* Html texture

  ```
  Copythis.load.htmlTexture(key, url, width, height);
  // this.load.htmlTexture(key, url, width, height, xhrSettings);

  ```

#### Sprite sheet

```
Copythis.load.spritesheet(key, url, {
  // frameWidth: frameWidth,
  // frameHeight: frameHeight,
  // startFrame: startFrame,
  // endFrame: endFrame,
  // margin: margin,
  // spacing: spacing
});
// this.load.spritesheet(key, url, frameConfig, xhrSettings);

```

#### Texture atlas

```
Copythis.load.atlas(key, textureURL, atlasURL);
// this.load.atlas(key, textureURL, atlasURL, textureXhrSettings, atlasXhrSettings);

```

#### Multi file texture atlas

```
Copythis.load.multiatlas(key, atlasURL);
// this.load.multiatlas(key, atlasURL, path, baseURL, atlasXhrSettings);

```

* `atlasURL` : The absolute or relative URL to load the texture atlas json data file from.
* `path` : Optional path to use when loading the textures defined in the atlas data.
* `baseURL` : Optional Base URL to use when loading the textures defined in the atlas data.

#### Unity texture atlas

```
Copythis.load.unityAtlas(key, textureURL, atlasURL);
// this.load.unityAtlas(key, textureURL, atlasURL, textureXhrSettings, atlasXhrSettings);

```

#### Animation

```
Copythis.load.animation(key, url);
// this.load.animation(key, url, dataKey, xhrSettings);

```

#### Audio

```
Copythis.load.audio(key, urls);
// this.load.audio(key, urls, {instances: 1}, xhrSettings);

```

* `urls` : The absolute or relative URL to load the audio files from, or a blob, or a base64 string of Uri.
* `config.instances` : Number of audio instances for HTML5Audio. Defaults to `1`.

#### Audio sprite

```
Copythis.load.audioSprite(key, jsonURL, audioURL, audioConfig);
// this.load.audioSprite(key, jsonURL, audioURL, audioConfig, audioXhrSettings, jsonXhrSettings);

```

* `jsonURL` : The absolute or relative URL to load the json file from.
* `audioURL` : The absolute or relative URL to load the audio file from.
* `audioConfig` : An object containing an `instances` property for HTML5Audio. Defaults to `1`.

#### Video

```
Copythis.load.video(key, url, noAudio);
// this.load.video(key, url, noAudio, xhrSettings);

```

* `url` : The absolute or relative URL to load the video files from, or a blob.
* `loadEvent` : The load event to listen for when *not* loading as a blob.
  + `'loadeddata'` : Data for the current frame is available. Default value.
  + `'canplay'` : The video is ready to start playing.
  + `'canplaythrough'` : The video can be played all the way through, without stopping.
* `asBlob` : Load the video as a data blob, or via the Video element? Default value is `false`.
* `noAudio` : Does the video have an audio track? If not you can enable auto-playing on it.
  + `false` : Has audio track, default behavior.

#### Bitmap font

```
Copythis.load.bitmapFont(key, textureURL, fontDataURL);
// this.load.bitmapFont(key, textureURL, fontDataURL, textureXhrSettings, fontDataXhrSettings);

```

* `textureURL` : The absolute or relative URL to load the font image file from.
* `fontDataURL` : The absolute or relative URL to load the font *xml* data file from, which created by software such as
  + [Angelcode Bitmap Font Generator](http://www.angelcode.com/products/bmfont/)
  + [Glyph Designer](https://71squared.com/glyphdesigner)
  + [Littera](http://kvazars.com/littera/) (Flash-based - yes, really, free)

#### Tile map

* JSON : Created using the Tiled Map Editor and selecting JSON as the export format

  ```
  Copythis.load.tilemapTiledJSON(key, url);
  // this.load.tilemapTiledJSON(key, url, xhrSettings);

  ```
* CSV : Created in a text editor, or a 3rd party app that exports as CSV.

  ```
  Copythis.load.tilemapCSV(key, url);
  // this.load.tilemapCSV(key, url, xhrSettings);

  ```

#### Text

```
Copythis.load.text(key, url);
// this.load.text(key, url, xhrSettings);

```

#### JSON

```
Copythis.load.json(key, url);
// this.load.json(key, url, dataKey, xhrSettings);

```

* `dataKey` : When the JSON file loads only this property will be stored in the Cache.

#### XML

```
Copythis.load.xml(key, url);
// this.load.xml(key, url, xhrSettings);

```

#### HTML

```
Copythis.load.html(key, url);
// this.load.html(key, url, xhrSettings);

```

#### CSS

```
Copythis.load.css(key, url);
// this.load.css(key, url, xhrSettings);

```

#### Scene

```
Copythis.load.sceneFile(key, url);
// this.load.sceneFile(key, url, xhrSettings);

```

The `key` matches the **class name** in the JavaScript file.

##### Script

```
Copythis.load.script(key, url);
// this.load.script(key, url, type, xhrSettings);

```

* `type` :　`'script'`, or `'module'`.

##### Scripts

```
Copythis.load.scripts(key, urlArray);
// this.load.scripts(key, urlArray, xhrSettings);

```

Add scripts in the exact order of `urlArray`.

##### GLSL

```
Copythis.load.glsl(key, url);
// this.load.glsl(key, url, shaderType, xhrSettings);

```

* `shaderType` : The type of shader.
  + `'fragment'` : Fragment shader. Default value.
  + `'vertex'` : Vertex shader.

Get data from cache

```
Copyvar cache = scene.cache.shader;
var data = cache.get(key);

```

A glsl file can contain multiple shaders, all separated by a frontmatter block.

```
Copy---
name:
type:
---

void main(void)
{
}

```

##### Binary

```
Copythis.load.binary(key, url, dataType); // dataType: Uint8Array
// this.load.binary(key, url, dataType, xhrSettings);

```

* `dataType` : Optional type to cast the binary file to once loaded.
  + `Uint8Array`, `Uint8ClampedArray`, `Uint16Array` `Uint32Array`
  + `Int8Array`, `Int16Array`, `Int32Array`
  + `Float32Array`, `Float64Array`
  + `BigInt64Array`, `BigUint64Array`

Get data from cache

```
Copyvar cache = scene.cache.binary;
var data = cache.get(key);

```

##### Plugin

```
Copythis.load.plugin(key, url, true); // start plugin when loaded
// this.load.plugin(key, url, true, undefined, xhrSettings);

```

* `url` : File url or class instance.

##### Scene plugin

```
Copythis.load.scenePlugin(key, url, systemKey, sceneKey);
// this.load.scenePlugin(key, url, systemKey, sceneKey, xhrSettings);

```

* `url` : File url or class instance.

##### File pack

Load files in JSON format.

```
Copythis.load.pack(key, url);
// this.load.pack(key, url, dataKey, xhrSettings);

```

or

```
Copythis.load.pack(key, json);
// this.load.pack(key, json, dataKey);

```

* `dataKey` : When the JSON file loads only this property will be stored in the Cache.

JSON pack file:

```
Copy{
    'dataKey': {
        // "prefix": "...",          // optional, extend key by prefix
        // "path": "...",            // optional, extend url by path
        // "defaultType": "image",   // optional, default file type
        'files': [
            {
                'type': 'image',
                'key': '...',
                'url': '...'
            },
            {
                'type': 'image',
                'key': '...',
                'url': '...'
            }
            // ...
        ]
    },

    'node0': {
        'node1': {
            'node2': {
                'files': [
                    // ....
                ]
            }
        }
    }
    // dataKey: 'node0.node1.node2'
}

```

File type:

* `audio`
* `binary`
* `glsl`
* `html`
* `htmlTexture`
* `image`
* `json`
* `script`
* `spritesheet`
* `svg`
* `text`
* `tilemapCSV`
* `tilemapJSON`
* `xml`

Get pack json data from cache

```
Copyvar cache = scene.cache.json; // pack json is stored in json cache
var data = cache.get(key);

```

Event name in `'filecomplete'` event : `'filecomplete-packfile-' + key`

## The loader

Each scene has a loader plugin, `this.load`, for loading assets.

### Set path

The `path` value is added before the filename but after the `baseURL` (if set). Once a path is set it will affect every file added to the Loader from that point on. It does not change any file already in the load queue. To reset it, call this method with no arguments.

#### Usage

```
Copythis.load.setPath(path);

```

* Example:

  ```
  Copythis.load.setPath("images/sprites/");
  this.load.image("ball", "ball.png"); // loads the ball.png file from images/sprites/ball.png

  ```

### Status of loader

* Ready to start loading

  ```
  Copyvar isReady = this.load.isReady();

  ```
* Is loading

  ```
  Copyvar isLoading = this.load.isLoading();

  ```

### Adding files to the loader

Each asset-loading method queues a resource by key and URL. You use the key to identify the asset later.

There is a `(key, url)` argument format:

```
Copythis.load.image("treasure", "treasure.png");

```

And an [object config format](../../docs/latest/Phaser.Loader.FileTypes.md):

```
Copythis.load.image({ key: "treasure", url: "treasure.png" });

```

And an array format:

```
Copythis.load.spritesheet([
  {
    key: "mermaid",
    url: "mermaid.png",
    frameConfig: { frameWidth: 16, frameHeight: 16 },
  },
  {
    key: "merman",
    url: "merman.png",
    frameConfig: { frameWidth: 16, frameHeight: 16 },
  },
]);

```

The loader will not add assets with duplicate keys (per asset type) at all:

```
Copythis.load.image("sky", "sky1.png");
// 'sky1.png' will be queued and (if loaded) stored as texture key 'sky'

// OOPS:
this.load.image("sky", "sky2.png");
// 'sky2.png' will not be queued at all

```

Some `key` exceptions:

* For some asset types (`script()`, sometimes `pack()`), you won't use the key again to retrieve anything, so it's not very important which key you choose.
* For `plugin()`, `sceneFile()`, and `scenePlugin()`, `key` must be the global class name of the plugin or scene.

Relative URLs are resolved to the [base URL of the document](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base), unless you configure the loader's `path` or `baseURL` values.

Each asset-loading method creates a temporary [File](../../docs/latest/Phaser.Loader.File.md) object for the loader which you can access through the load event handlers if you need. These last only for the duration of the load cycle.

You can write your own asset manifest pretty easily:

```
Copyconst files = {
  animation: [/* … */],
  audio: [/* … */],
  image: [/* … */],
  spritesheet: [/* … */],
};

this.load.animation(files.animation);
this.load.audio(files.audio);
this.load.image(files.images);
this.load.spritesheet(files.spritesheet};

```

A [File Pack](../../docs/latest/Phaser.Loader.LoaderPlugin-pack.md) could do as well:

```
Copythis.load.pack("pack1", {
  section1: {
    files: [
      { type: "image", key: "conch", url: "conch.png" },
      {
        type: "spritesheet",
        key: "mermaid",
        url: "mermaid.png",
        frameConfig: {
          /* … */
        },
      },
    ],
  },
});

```

A File Pack needs at least one named section (e.g., `section1` above). If you're loading all the pack assets at once, it doesn't really matter what the section names are. The docs describe a method for downloading pack sections separately, but if you want to do this it seems more practical to download the entire pack with `load.json()` then select sections from the JSON data and pass those into `load.pack()`.

You can add assets to the load queue while the loader is running:

```
Copythis.load.json("level1", "level1.json");
this.load.on("filecomplete-json-level1", (key, type, data) => {
  this.load.image(data.images);
  this.load.spritesheet(data.spritesheets);
});

```

`load.multiatlas()`, `load.pack()`, and `load.spine()` work this way.

### Load events

#### Events

* Load file complete event

  ```
  Copythis.load.on("filecomplete", function (key, type, data) {}, scope);

  ```

  or

  ```
  Copythis.load.on(
    "filecomplete-" + type + "-" + key,
    function (key, type, data) {},
    scope
  );

  ```
* Add loading file event

  ```
  Copythis.load.on("addfile", function (key, type, file) {}, scope);

  ```
* Start loading

  ```
  Copythis.load.once("start", function () {}, scope);

  ```
* Loading progressing

  ```
  Copythis.load.on("progress", function (progress) {}, scope);

  ```

  + `progress` value will increase when a file is loaded, and decrease when a new file loading request is added.

    ```
    Copyvar loader = this.load;
    var total = loader.totalToLoad;
    var remainder = loader.list.size + loader.inflight.size;
    var progress = 1 - remainder / total;

    ```
* Loading file progressing

  ```
  Copythis.load.on(
    "fileprogress",
    function (file, progress) {
      // var key = file.key;
    },
    scope
  );

  ```
* Loading a file object successful

  ```
  Copythis.load.once("load", function (fileObj) {}, scope);

  ```
* Loading a file object failed

  ```
  Copythis.load.once("loaderror", function (fileObj) {}, scope);

  ```
* All loading completed

  + Before releasing resources

    ```
    Copythis.load.once("postprocess", function (loader) {}, scope);

    ```
  + After releasing resources

    ```
    Copythis.load.once("complete", function (loader) {}, scope);

    ```
* Scene's `'preupdate'`, `'update'`, `'postupdate'`, `'render'` events will be triggered during preload stage.

#### Preload stage

Most of the time you will load assets in a scene `preload()` method.

When `preload()` returns, the loader starts automatically, then `create()` is called only after loading finishes. In the meantime the scene is in a `LOADING` state and still updates and renders any of its game objects, but doesn't call scene `update()`. You can show load progress this way.

##### Usage

```
Copythis.load.image(key, url);
// this.load.image(config); // config: {key, url}

```

Loader in preload stage will start loading automatically by scene.

#### Loading progress

It's best to create any game objects in the load `START` event and destroy them in the load `COMPLETE` event, so that restarting the loader doesn't cause any errors.

* [load progress event](https://labs.phaser.io/edit.html?src=src/loader/loader%20events/load%20progress.js)
* [file progress event](https://labs.phaser.io/edit.html?src=src/loader/loader%20events/file%20progress%20event.js)

#### Loading after preload stage

To load assets outside of `preload()`, you add files as usual, add listeners for the completion events, and then start the loader yourself.

##### Usage

```
Copythis.load.image(key, url); // add task
// this.load.image(config); // config: {key, url}
this.load.once("complete", callback, scope); // add callback of 'complete' event
this.load.start(); // start loading

```

```
Copythis.load
  .image(["conch", "treasure", "trident"])
  .once("complete", () => {
    // All files complete
  })
  .start();

```

It's fine if two processes call the loader's `start()` separately. If it's already loading, it won't restart or clear the queue.

Other scenes should listen for "add" events from the game caches or Texture Manager:

```
Copythis.cache.audio.on("add", (cache, key) => {
  if (key === "music") {
    this.sound.play("music");
  }
});

this.textures.on("addtexture-map", (texture) => {
  // The key is also in `texture.key`.
  this.add.image(0, 0, "map");
});

```

## Scene payload

A scene payload is alternative to `preload()` that lets you load assets right when the scene starts. It's often used when you need to load a few small assets to use **during** `preload()`, and you don't want the trouble of starting an extra scene (and its loader) before that. A scene downloading a payload is not in a `LOADING` state and can't update or render anything, so it's best to keep payloads small.

The pack object structure is the same as the `files` portion of a [pack file](../../docs/latest/Phaser.Loader.LoaderPlugin-pack.md) section.

```
Copyconst sceneConfig = {
  pack: {
    files: [
      { type: "json", key: "settings", url: "settings.json" },
      { type: "image", key: "bar", url: "bar.png" },
    ],
  },
  init: function () {
    // Pack has downloaded. 'settings' is in JSON cache.
    this.game.registry.merge(this.cache.json.get("settings"));
  },
  preload: function () {
    // 'bar' is in the Texture Manager.
    this.load.on("start", () => {
      const loadingBar = this.add.image(0, 0, "bar");
    });
  },
};

```

## Removing assets

You can remove assets to save memory. Remove any game objects or scene objects (e.g., Sounds) using these assets first!

Remove textures from the Texture Manager:

```
Copythis.textures.remove("conch");

```

and other assets from their respective caches:

```
Copythis.cache.audio.remove("chime");
this.cache.json.remove("settings");

```

Removing assets to reuse their keys for different assets is usually a bad idea.

## XHR Settings Object

You have a lot of control over the `xhrSettings` object used by every file loaded. This allows you to modify the timeout, request or credential headers. The object takes the following form:

```
Copy{
    async: true,
    user: '',
    password: '',
    timeout: 0,
    headers: undefined,
    header: undefined,
    headerValue: undefined,
    requestedWith: undefined,
    overrideMimeType: undefined,
    withCredentials: false
}

```

* `user` : Optional username for the XHR request.
* `password` : Optional password for the XHR request.
* `timeout` : Optional XHR timeout value.
* `headers`, `header`, `headerValue`, `requestedWith` : This value is used to populate the XHR `setRequestHeader`
* `overrideMimeType` : Provide a custom mime-type to use instead of the default.
* `withCredentials` : Whether or not cross-site Access-Control requests should be made using credentials such as cookies, authorization headers or TLS client certificates. *Setting `withCredentials` has no effect on same-site requests.*

## More configurations

More configurations in game config

```
Copyloader:{
    baseURL: '',
    path: '',
    enableParallel: true,
    maxParallelDownloads: 4,
    crossOrigin: undefined,
    responseType: '',
    async: true,
    user: '',
    password: '',
    timeout: 0,
    withCredentials: false,
    imageLoadType: 'XHR',    // 'HTMLImageElement'
    localScheme: [ 'file://', 'capacitor://' ]
},

```

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)
* [samme](https://github.com/samme)

Updated on June 4, 2025, 1:16 PM UTC

---

[Input](input.md)

[Cache](loader/cache.md)

On this page

* [Loader](#loader)

  + [Strategy](#strategy)
  + [Assets](#assets)

    - [Where to load assets](#where-to-load-assets)
    - [Asset types](#asset-types)
  + [The loader](#the-loader)

    - [Set path](#set-path)
    - [Status of loader](#status-of-loader)
    - [Adding files to the loader](#adding-files-to-the-loader)
    - [Load events](#load-events)
  + [Scene payload](#scene-payload)
  + [Removing assets](#removing-assets)
  + [XHR Settings Object](#xhr-settings-object)
  + [More configurations](#more-configurations)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../index.md)



Loader