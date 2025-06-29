# LoaderPlugin

Phaser.Loader.LoaderPlugin

The Loader handles loading all external content such as Images, Sounds, Texture Atlases and data files.

You typically interact with it via `this.load` in your Scene. Scenes can have a `preload` method, which is always

called before the Scenes `create` method, allowing you to preload assets that the Scene may need.

If you call any `this.load` methods from outside of `Scene.preload` then you need to start the Loader going

yourself by calling `Loader.start()`. It's only automatically started during the Scene preload.

The Loader uses a combination of tag loading (eg. Audio elements) and XHR and provides progress and completion events.

Files are loaded in parallel by default. The amount of concurrent connections can be controlled in your Game Configuration.

Once the Loader has started loading you are still able to add files to it. These can be injected as a result of a loader

event, the type of file being loaded (such as a pack file) or other external events. As long as the Loader hasn't finished

simply adding a new file to it, while running, will ensure it's added into the current queue.

Every Scene has its own instance of the Loader and they are bound to the Scene in which they are created. However,

assets loaded by the Loader are placed into global game-level caches. For example, loading an XML file will place that

file inside `Game.cache.xml`, which is accessible from every Scene in your game, no matter who was responsible

for loading it. The same is true of Textures. A texture loaded in one Scene is instantly available to all other Scenes

in your game.

The Loader works by using custom File Types. These are stored in the FileTypesManager, which injects them into the Loader

when it's instantiated. You can create your own custom file types by extending either the File or MultiFile classes.

See those files for more details.

**Constructor**

`new LoaderPlugin(scene)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene which owns this Loader instance. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](events-eventemitter.md)

> Source: [src/loader/LoaderPlugin.js#L20](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L20)  
> Since: 3.0.0

# Public Methods

## addFile

### <instance> addFile(file)

**Description:**

Adds a file, or array of files, into the load queue.

The file must be an instance of `Phaser.Loader.File`, or a class that extends it. The Loader will check that the key

used by the file won't conflict with any other key either in the loader, the inflight queue or the target cache.

If allowed it will then add the file into the pending list, read for the load to start. Or, if the load has already

started, ready for the next batch of files to be pulled from the list to the inflight queue.

You should not normally call this method directly, but rather use one of the Loader methods like `image` or `atlas`,

however you can call this as long as the file given to it is well formed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| file | [Phaser.Loader.File](loader-file.md) | Array.<[Phaser.Loader.File](loader-file.md)> | No | The file, or array of files, to be added to the load queue. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/LoaderPlugin.js#L516](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L516)  
> Since: 3.0.0

---

## addListener

### <instance> addListener(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## addPack

### <instance> addPack(pack, [packKey])

**Description:**

Takes a well formed, fully parsed pack file object and adds its entries into the load queue. Usually you do not call

this method directly, but instead use `Loader.pack` and supply a path to a JSON file that holds the

pack data. However, if you've got the data prepared you can pass it to this method.

You can also provide an optional key. If you do then it will only add the entries from that part of the pack into

to the load queue. If not specified it will add all entries it finds. For more details about the pack file format

see the `LoaderPlugin.pack` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pack | any | No | The Pack File data to be parsed and each entry of it to added to the load queue. |
| --- | --- | --- | --- |
| packKey | string | Yes | An optional key to use from the pack file data. |

**Returns:** boolean - `true` if any files were added to the queue, otherwise `false`.

> Source: [src/loader/LoaderPlugin.js#L618](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L618)  
> Since: 3.7.0

---

## animation

### <instance> animation(key, [url], [dataKey], [xhrSettings])

**Description:**

Adds an Animation JSON Data file, or array of Animation JSON files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.animation('baddieAnims', 'files/BaddieAnims.json');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

If you call this from outside of `preload` then you are responsible for starting the Loader afterwards and monitoring

its events to know when it's safe to use the asset. Please see the Phaser.Loader.LoaderPlugin class for more details.

The key must be a unique String. It is used to add the file to the global JSON Cache upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the JSON Cache.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the JSON Cache first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.animation({

    key: 'baddieAnims',

    url: 'files/BaddieAnims.json'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.JSONFileConfig` for more details.

Once the file has finished loading it will automatically be passed to the global Animation Managers `fromJSON` method.

This will parse all of the JSON data and create animation data from it. This process happens at the very end

of the Loader, once every other file in the load queue has finished. The reason for this is to allow you to load

both animation data and the images it relies upon in the same load call.

Once the animation data has been parsed you will be able to play animations using that data.

Please see the Animation Manager `fromJSON` method for more details about the format and playback.

You can also access the raw animation data from its Cache using its key:

```
Copy
this.load.animation('baddieAnims', 'files/BaddieAnims.json');

// and later in your game ...

var data = this.cache.json.get('baddieAnims');


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `LEVEL1.` and the key was `Waves` the final key will be `LEVEL1.Waves` and

this is what you would use to retrieve the text from the JSON Cache.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "data"

and no URL is given then the Loader will set the URL to be "data.json". It will always add `.json` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

You can also optionally provide a `dataKey` to use. This allows you to extract only a part of the JSON and store it in the Cache,

rather than the whole file. For example, if your JSON data had a structure like this:

```
Copy
{

    "level1": {

        "baddies": {

            "aliens": {},

            "boss": {}

        }

    },

    "level2": {},

    "level3": {}

}


```

And if you only wanted to create animations from the `boss` data, then you could pass `level1.baddies.boss`as the `dataKey`.

Note: The ability to load this type of file will only be available if the JSON File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.JSONFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.JSONFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | string | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.json`, i.e. if `key` was "alien" then the URL will be "alien.json". |
| dataKey | string | Yes | When the Animation JSON file loads only this property will be stored in the Cache and used to create animation data. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/AnimationJSONFile.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/AnimationJSONFile.js#L77)  
> Since: 3.0.0

---

## aseprite

### <instance> aseprite(key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings])

**Description:**

Aseprite is a powerful animated sprite editor and pixel art tool.

You can find more details at <https://www.aseprite.org/>

Adds a JSON based Aseprite Animation, or array of animations, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.aseprite('gladiator', 'images/Gladiator.png', 'images/Gladiator.json');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

If you call this from outside of `preload` then you are responsible for starting the Loader afterwards and monitoring

its events to know when it's safe to use the asset. Please see the Phaser.Loader.LoaderPlugin class for more details.

To export a compatible JSON file in Aseprite, please do the following:

1. Go to "File - Export Sprite Sheet"
2. On the **Layout** tab:

2a. Set the "Sheet type" to "Packed"

2b. Set the "Constraints" to "None"

2c. Check the "Merge Duplicates" checkbox

3. On the **Sprite** tab:

3a. Set "Layers" to "Visible layers"

3b. Set "Frames" to "All frames", unless you only wish to export a sub-set of tags

4. On the **Borders** tab:

4a. Check the "Trim Sprite" and "Trim Cells" options

4b. Ensure "Border Padding", "Spacing" and "Inner Padding" are all > 0 (1 is usually enough)

5. On the **Output** tab:

5a. Check "Output File", give your image a name and make sure you choose "png files" as the file type

5b. Check "JSON Data" and give your json file a name

5c. The JSON Data type can be either a Hash or Array, Phaser doesn't mind.

5d. Make sure "Tags" is checked in the Meta options

5e. In the "Item Filename" input box, make sure it says just "{frame}" and nothing more.

6. Click export

This was tested with Aseprite 1.2.25.

This will export a png and json file which you can load using the Aseprite Loader, i.e.:

Phaser can load all common image types: png, jpg, gif and any other format the browser can natively handle.

The key must be a unique String. It is used to add the file to the global Texture Manager upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Texture Manager.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Texture Manager first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.aseprite({

    key: 'gladiator',

    textureURL: 'images/Gladiator.png',

    atlasURL: 'images/Gladiator.json'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.AsepriteFileConfig` for more details.

Instead of passing a URL for the JSON data you can also pass in a well formed JSON object instead.

Once loaded, you can call this method from within a Scene with the 'atlas' key:

```
Copy
this.anims.createFromAseprite('paladin');


```

Any animations defined in the JSON will now be available to use in Phaser and you play them

via their Tag name. For example, if you have an animation called 'War Cry' on your Aseprite timeline,

you can play it in Phaser using that Tag name:

```
Copy
this.add.sprite(400, 300).play('War Cry');


```

When calling this method you can optionally provide an array of tag names, and only those animations

will be created. For example:

```
Copy
this.anims.createFromAseprite('paladin', [ 'step', 'War Cry', 'Magnum Break' ]);


```

This will only create the 3 animations defined. Note that the tag names are case-sensitive.

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `MENU.` and the key was `Background` the final key will be `MENU.Background` and

this is what you would use to retrieve the image from the Texture Manager.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "alien"

and no URL is given then the Loader will set the URL to be "alien.png". It will always add `.png` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the Aseprite File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.AsepriteFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.AsepriteFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| textureURL | string | Array.<string> | Yes | The absolute or relative URL to load the texture image file from. If undefined or `null` it will be set to `<key>.png`, i.e. if `key` was "alien" then the URL will be "alien.png". |
| atlasURL | object | string | Yes | The absolute or relative URL to load the texture atlas json data file from. If undefined or `null` it will be set to `<key>.json`, i.e. if `key` was "alien" then the URL will be "alien.json". Or, a well formed JSON object. |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object for the atlas image file. Used in replacement of the Loaders default XHR Settings. |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object for the atlas json file. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/AsepriteFile.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/AsepriteFile.js#L111)  
> Since: 3.50.0

---

## atlas

### <instance> atlas(key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings])

**Description:**

Adds a JSON based Texture Atlas, or array of atlases, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.atlas('mainmenu', 'images/MainMenu.png', 'images/MainMenu.json');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

If you call this from outside of `preload` then you are responsible for starting the Loader afterwards and monitoring

its events to know when it's safe to use the asset. Please see the Phaser.Loader.LoaderPlugin class for more details.

Phaser expects the atlas data to be provided in a JSON file, using either the JSON Hash or JSON Array format.

These files are created by software such as:

* [Texture Packer](https://www.codeandweb.com/texturepacker/tutorials/how-to-create-sprite-sheets-for-phaser3?source=photonstorm)
* [Shoebox](https://renderhjs.net/shoebox/)
* [Gamma Texture Packer](https://gammafp.com/tool/atlas-packer/)
* [Adobe Flash / Animate](https://www.adobe.com/uk/products/animate.html)
* [Free Texture Packer](http://free-tex-packer.com/)
* [Leshy SpriteSheet Tool](https://www.leshylabs.com/apps/sstool/)

If you are using Texture Packer and have enabled multi-atlas support, then please use the Phaser Multi Atlas loader

instead of this one.

Phaser can load all common image types: png, jpg, gif and any other format the browser can natively handle.

The key must be a unique String. It is used to add the file to the global Texture Manager upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Texture Manager.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Texture Manager first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.atlas({

    key: 'mainmenu',

    textureURL: 'images/MainMenu.png',

    atlasURL: 'images/MainMenu.json'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.AtlasJSONFileConfig` for more details.

Instead of passing a URL for the atlas JSON data you can also pass in a well formed JSON object instead.

Once the atlas has finished loading you can use frames from it as textures for a Game Object by referencing its key:

```
Copy
this.load.atlas('mainmenu', 'images/MainMenu.png', 'images/MainMenu.json');

// and later in your game ...

this.add.image(x, y, 'mainmenu', 'background');


```

To get a list of all available frames within an atlas please consult your Texture Atlas software.

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `MENU.` and the key was `Background` the final key will be `MENU.Background` and

this is what you would use to retrieve the image from the Texture Manager.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "alien"

and no URL is given then the Loader will set the URL to be "alien.png". It will always add `.png` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Phaser also supports the automatic loading of associated normal maps. If you have a normal map to go with this image,

then you can specify it by providing an array as the `url` where the second element is the normal map:

```
Copy
this.load.atlas('mainmenu', [ 'images/MainMenu.png', 'images/MainMenu-n.png' ], 'images/MainMenu.json');


```

Or, if you are using a config object use the `normalMap` property:

```
Copy
this.load.atlas({

    key: 'mainmenu',

    textureURL: 'images/MainMenu.png',

    normalMap: 'images/MainMenu-n.png',

    atlasURL: 'images/MainMenu.json'

});


```

The normal map file is subject to the same conditions as the image file with regard to the path, baseURL, CORs and XHR Settings.

Normal maps are a WebGL only feature.

Note: The ability to load this type of file will only be available if the Atlas JSON File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.AtlasJSONFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.AtlasJSONFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| textureURL | string | Array.<string> | Yes | The absolute or relative URL to load the texture image file from. If undefined or `null` it will be set to `<key>.png`, i.e. if `key` was "alien" then the URL will be "alien.png". |
| atlasURL | object | string | Yes | The absolute or relative URL to load the texture atlas json data file from. If undefined or `null` it will be set to `<key>.json`, i.e. if `key` was "alien" then the URL will be "alien.json". Or, a well formed JSON object. |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object for the atlas image file. Used in replacement of the Loaders default XHR Settings. |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object for the atlas json file. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/AtlasJSONFile.js#L109](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/AtlasJSONFile.js#L109)  
> Since: 3.0.0

---

## atlasXML

### <instance> atlasXML(key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings])

**Description:**

Adds an XML based Texture Atlas, or array of atlases, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.atlasXML('mainmenu', 'images/MainMenu.png', 'images/MainMenu.xml');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

If you call this from outside of `preload` then you are responsible for starting the Loader afterwards and monitoring

its events to know when it's safe to use the asset. Please see the Phaser.Loader.LoaderPlugin class for more details.

Phaser expects the atlas data to be provided in an XML file format.

These files are created by software such as Shoebox and Adobe Flash / Animate.

Phaser can load all common image types: png, jpg, gif and any other format the browser can natively handle.

The key must be a unique String. It is used to add the file to the global Texture Manager upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Texture Manager.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Texture Manager first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.atlasXML({

    key: 'mainmenu',

    textureURL: 'images/MainMenu.png',

    atlasURL: 'images/MainMenu.xml'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.AtlasXMLFileConfig` for more details.

Once the atlas has finished loading you can use frames from it as textures for a Game Object by referencing its key:

```
Copy
this.load.atlasXML('mainmenu', 'images/MainMenu.png', 'images/MainMenu.xml');

// and later in your game ...

this.add.image(x, y, 'mainmenu', 'background');


```

To get a list of all available frames within an atlas please consult your Texture Atlas software.

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `MENU.` and the key was `Background` the final key will be `MENU.Background` and

this is what you would use to retrieve the image from the Texture Manager.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "alien"

and no URL is given then the Loader will set the URL to be "alien.png". It will always add `.png` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Phaser also supports the automatic loading of associated normal maps. If you have a normal map to go with this image,

then you can specify it by providing an array as the `url` where the second element is the normal map:

```
Copy
this.load.atlasXML('mainmenu', [ 'images/MainMenu.png', 'images/MainMenu-n.png' ], 'images/MainMenu.xml');


```

Or, if you are using a config object use the `normalMap` property:

```
Copy
this.load.atlasXML({

    key: 'mainmenu',

    textureURL: 'images/MainMenu.png',

    normalMap: 'images/MainMenu-n.png',

    atlasURL: 'images/MainMenu.xml'

});


```

The normal map file is subject to the same conditions as the image file with regard to the path, baseURL, CORs and XHR Settings.

Normal maps are a WebGL only feature.

Note: The ability to load this type of file will only be available if the Atlas XML File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.AtlasXMLFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.AtlasXMLFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| textureURL | string | Array.<string> | Yes | The absolute or relative URL to load the texture image file from. If undefined or `null` it will be set to `<key>.png`, i.e. if `key` was "alien" then the URL will be "alien.png". |
| atlasURL | string | Yes | The absolute or relative URL to load the texture atlas xml data file from. If undefined or `null` it will be set to `<key>.xml`, i.e. if `key` was "alien" then the URL will be "alien.xml". |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object for the atlas image file. Used in replacement of the Loaders default XHR Settings. |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object for the atlas xml file. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/AtlasXMLFile.js#L107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/AtlasXMLFile.js#L107)  
> Since: 3.7.0

---

## audio

### <instance> audio(key, [urls], [config], [xhrSettings])

**Description:**

Adds an Audio or HTML5Audio file, or array of audio files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.audio('title', [ 'music/Title.ogg', 'music/Title.mp3', 'music/Title.m4a' ]);

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global Audio Cache upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Audio Cache.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Audio Cache first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.audio({

    key: 'title',

    url: [ 'music/Title.ogg', 'music/Title.mp3', 'music/Title.m4a' ]

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.AudioFileConfig` for more details.

The URLs can be relative or absolute. If the URLs are relative the `Loader.baseURL` and `Loader.path` values will be prepended to them.

Due to different browsers supporting different audio file types you should usually provide your audio files in a variety of formats.

ogg, mp3 and m4a are the most common. If you provide an array of URLs then the Loader will determine which *one* file to load based on

browser support.

If audio has been disabled in your game, either via the game config, or lack of support from the device, then no audio will be loaded.

Note: The ability to load this type of file will only be available if the Audio File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.AudioFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.AudioFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| urls | string | Array.<string> | [Phaser.Types.Loader.FileTypes.AudioFileURLConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.AudioFileURLConfig](../typedef/types-loader-filetypes.md)> |
| config | any | Yes | An object containing an `instances` property for HTML5Audio. Defaults to 1. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/AudioFile.js#L172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/AudioFile.js#L172)  
> Since: 3.0.0

---

## audioSprite

### <instance> audioSprite(key, jsonURL, [audioURL], [audioConfig], [audioXhrSettings], [jsonXhrSettings])

**Description:**

Adds a JSON based Audio Sprite, or array of audio sprites, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.audioSprite('kyobi', 'kyobi.json', [

        'kyobi.ogg',

        'kyobi.mp3',

        'kyobi.m4a'

    ]);

}


```

Audio Sprites are a combination of audio files and a JSON configuration.

The JSON follows the format of that created by <https://github.com/tonistiigi/audiosprite>

If the JSON file includes a 'resource' object then you can let Phaser parse it and load the audio

files automatically based on its content. To do this exclude the audio URLs from the load:

```
Copy
function preload ()

{

    this.load.audioSprite('kyobi', 'kyobi.json');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

If you call this from outside of `preload` then you are responsible for starting the Loader afterwards and monitoring

its events to know when it's safe to use the asset. Please see the Phaser.Loader.LoaderPlugin class for more details.

The key must be a unique String. It is used to add the file to the global Audio Cache upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Audio Cache.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Audio Cache first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.audioSprite({

    key: 'kyobi',

    jsonURL: 'audio/Kyobi.json',

    audioURL: [

        'audio/Kyobi.ogg',

        'audio/Kyobi.mp3',

        'audio/Kyobi.m4a'

    ]

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.AudioSpriteFileConfig` for more details.

Instead of passing a URL for the audio JSON data you can also pass in a well formed JSON object instead.

Once the audio has finished loading you can use it create an Audio Sprite by referencing its key:

```
Copy
this.load.audioSprite('kyobi', 'kyobi.json');

// and later in your game ...

var music = this.sound.addAudioSprite('kyobi');

music.play('title');


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `MENU.` and the key was `Background` the final key will be `MENU.Background` and

this is what you would use to retrieve the image from the Texture Manager.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

Due to different browsers supporting different audio file types you should usually provide your audio files in a variety of formats.

ogg, mp3 and m4a are the most common. If you provide an array of URLs then the Loader will determine which *one* file to load based on

browser support.

If audio has been disabled in your game, either via the game config, or lack of support from the device, then no audio will be loaded.

Note: The ability to load this type of file will only be available if the Audio Sprite File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.AudioSpriteFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.AudioSpriteFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| jsonURL | string | No | The absolute or relative URL to load the json file from. Or a well formed JSON object to use instead. |
| audioURL | string | Array.<string> | Yes | The absolute or relative URL to load the audio file from. If empty it will be obtained by parsing the JSON file. |
| audioConfig | any | Yes | The audio configuration options. |
| audioXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object for the audio file. Used in replacement of the Loaders default XHR Settings. |
| jsonXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object for the json file. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/AudioSpriteFile.js#L143](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/AudioSpriteFile.js#L143)  
> Since: 3.0.0

---

## binary

### <instance> binary(key, [url], [dataType], [xhrSettings])

**Description:**

Adds a Binary file, or array of Binary files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.binary('doom', 'files/Doom.wad');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global Binary Cache upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Binary Cache.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Binary Cache first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.binary({

    key: 'doom',

    url: 'files/Doom.wad',

    dataType: Uint8Array

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.BinaryFileConfig` for more details.

Once the file has finished loading you can access it from its Cache using its key:

```
Copy
this.load.binary('doom', 'files/Doom.wad');

// and later in your game ...

var data = this.cache.binary.get('doom');


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `LEVEL1.` and the key was `Data` the final key will be `LEVEL1.Data` and

this is what you would use to retrieve the text from the Binary Cache.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "doom"

and no URL is given then the Loader will set the URL to be "doom.bin". It will always add `.bin` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the Binary File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.BinaryFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.BinaryFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | string | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.bin`, i.e. if `key` was "alien" then the URL will be "alien.bin". |
| dataType | any | Yes | Optional type to cast the binary file to once loaded. For example, `Uint8Array`. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/BinaryFile.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/BinaryFile.js#L89)  
> Since: 3.0.0

---

## bitmapFont

### <instance> bitmapFont(key, [textureURL], [fontDataURL], [textureXhrSettings], [fontDataXhrSettings])

**Description:**

Adds an XML based Bitmap Font, or array of fonts, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.bitmapFont('goldenFont', 'images/GoldFont.png', 'images/GoldFont.xml');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

If you call this from outside of `preload` then you are responsible for starting the Loader afterwards and monitoring

its events to know when it's safe to use the asset. Please see the Phaser.Loader.LoaderPlugin class for more details.

Phaser expects the font data to be provided in an XML file format.

These files are created by software such as the [Angelcode Bitmap Font Generator](http://www.angelcode.com/products/bmfont/),

[Littera](http://kvazars.com/littera/) or [Glyph Designer](https://71squared.com/glyphdesigner)

Phaser can load all common image types: png, jpg, gif and any other format the browser can natively handle.

The key must be a unique String. It is used to add the file to the global Texture Manager upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Texture Manager.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Texture Manager first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.bitmapFont({

    key: 'goldenFont',

    textureURL: 'images/GoldFont.png',

    fontDataURL: 'images/GoldFont.xml'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.BitmapFontFileConfig` for more details.

Once the atlas has finished loading you can use key of it when creating a Bitmap Text Game Object:

```
Copy
this.load.bitmapFont('goldenFont', 'images/GoldFont.png', 'images/GoldFont.xml');

// and later in your game ...

this.add.bitmapText(x, y, 'goldenFont', 'Hello World');


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `MENU.` and the key was `Background` the final key will be `MENU.Background` and

this is what you would use when creating a Bitmap Text object.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "alien"

and no URL is given then the Loader will set the URL to be "alien.png". It will always add `.png` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Phaser also supports the automatic loading of associated normal maps. If you have a normal map to go with this image,

then you can specify it by providing an array as the `url` where the second element is the normal map:

```
Copy
this.load.bitmapFont('goldenFont', [ 'images/GoldFont.png', 'images/GoldFont-n.png' ], 'images/GoldFont.xml');


```

Or, if you are using a config object use the `normalMap` property:

```
Copy
this.load.bitmapFont({

    key: 'goldenFont',

    textureURL: 'images/GoldFont.png',

    normalMap: 'images/GoldFont-n.png',

    fontDataURL: 'images/GoldFont.xml'

});


```

The normal map file is subject to the same conditions as the image file with regard to the path, baseURL, CORs and XHR Settings.

Normal maps are a WebGL only feature.

Note: The ability to load this type of file will only be available if the Bitmap Font File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.BitmapFontFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.BitmapFontFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| textureURL | string | Array.<string> | Yes | The absolute or relative URL to load the font image file from. If undefined or `null` it will be set to `<key>.png`, i.e. if `key` was "alien" then the URL will be "alien.png". |
| fontDataURL | string | Yes | The absolute or relative URL to load the font xml data file from. If undefined or `null` it will be set to `<key>.xml`, i.e. if `key` was "alien" then the URL will be "alien.xml". |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object for the font image file. Used in replacement of the Loaders default XHR Settings. |
| fontDataXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object for the font data xml file. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/BitmapFontFile.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/BitmapFontFile.js#L113)  
> Since: 3.0.0

---

## css

### <instance> css(key, [url], [xhrSettings])

**Description:**

Adds a CSS file, or array of CSS files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.css('headers', 'styles/headers.css');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String and not already in-use by another file in the Loader.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.css({

    key: 'headers',

    url: 'styles/headers.css'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.CSSFileConfig` for more details.

Once the file has finished loading it will automatically be converted into a style DOM element

via `document.createElement('style')`. It will have its `defer` property set to false and then the

resulting element will be appended to `document.head`. The CSS styles are then applied to the current document.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "alien"

and no URL is given then the Loader will set the URL to be "alien.css". It will always add `.css` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the CSS File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.CSSFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.CSSFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | string | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.css`, i.e. if `key` was "alien" then the URL will be "alien.css". |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/CSSFile.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/CSSFile.js#L88)  
> Since: 3.17.0

---

## emit

### <instance> emit(event, [args])

**Description:**

Calls each of the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| args | \* | Yes | Additional arguments that will be passed to the event handler. |

**Returns:** boolean - `true` if the event had listeners, else `false`.

**Inherits:** [Phaser.Events.EventEmitter#emit](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L86)  
> Since: 3.0.0

---

## eventNames

### <instance> eventNames()

**Description:**

Return an array listing the events for which the emitter has registered listeners.

**Returns:** Array.<(string | symbol)> - undefined

**Inherits:** [Phaser.Events.EventEmitter#eventNames](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L55)  
> Since: 3.0.0

---

## fileProcessComplete

### <instance> fileProcessComplete(file)

**Description:**

An internal method that is called automatically by the File when it has finished processing.

If the process was successful, and the File isn't part of a MultiFile, its `addToCache` method is called.

It this then removed from the queue. If there are no more files to load `loadComplete` is called.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| file | [Phaser.Loader.File](loader-file.md) | No | The file that has finished processing. |
| --- | --- | --- | --- |

> Source: [src/loader/LoaderPlugin.js#L1067](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L1067)  
> Since: 3.7.0

---

## flagForRemoval

### <instance> flagForRemoval(file)

**Description:**

Adds a File into the pending-deletion queue.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| file | [Phaser.Loader.File](loader-file.md) | No | The File to be queued for deletion when the Loader completes. |
| --- | --- | --- | --- |

> Source: [src/loader/LoaderPlugin.js#L1158](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L1158)  
> Since: 3.7.0

---

## font

### <instance> font(key, [url], [format], [descriptors], [xhrSettings])

**Description:**

Adds a Font file, or array of Font files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.font('Nokia', 'assets/nokia.ttf', 'truetype');

}


```

If the font file is open type, you can specify the format:

```
Copy
function preload ()

{

    this.load.font('Nokia', 'assets/nokia.otf', 'opentype');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String and not already in-use by another file in the Loader.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.font({

    key: 'Nokia',

    url: 'assets/nokia.ttf',

    format: 'truetype',

    descriptors: { style: 'normal', weight: '400' }

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.FontFileConfig` for more details.

See the MDN documentation at <https://developer.mozilla.org/en-US/docs/Web/API/FontFace/FontFace#descriptors> for details about the descriptors.

When this file is handled by the Loader, it will create a new Font Face DOM element for it and add it to the document.

You should use the same key given for the font in your Text objects, such as:

```
Copy
this.add.text(x, y, 'Hello World', { fontFamily: 'Nokia', fontSize: 48 });


```

See <https://developer.mozilla.org/en-US/docs/Web/API/FontFace> for more details.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "alien"

and no URL is given then the Loader will set the URL to be "alien.ttf". It will always add `.ttf` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the Font File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.FontFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.FontFileConfig](../typedef/types-loader-filetypes.md)> | No |  |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.ttf`, i.e. if `key` was "alien" then the URL will be "alien.ttf". |
| format | string | Yes | "'truetype'" | The font type. Should be a string, like 'truetype' or 'opentype'. |
| descriptors | object | Yes |  | An optional object containing font descriptors for the Font Face. See <https://developer.mozilla.org/en-US/docs/Web/API/FontFace/FontFace#descriptors> for more details. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes |  | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/FontFile.js#L127](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/FontFile.js#L127)  
> Since: 3.87.0

---

## glsl

### <instance> glsl(key, [url], [shaderType], [xhrSettings])

**Description:**

Adds a GLSL file, or array of GLSL files, to the current load queue.

In Phaser 3 GLSL files are just plain Text files at the current moment in time.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.glsl('plasma', 'shaders/Plasma.glsl');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global Shader Cache upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Shader Cache.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Shader Cache first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.glsl({

    key: 'plasma',

    shaderType: 'fragment',

    url: 'shaders/Plasma.glsl'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.GLSLFileConfig` for more details.

Once the file has finished loading you can access it from its Cache using its key:

```
Copy
this.load.glsl('plasma', 'shaders/Plasma.glsl');

// and later in your game ...

var data = this.cache.shader.get('plasma');


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `FX.` and the key was `Plasma` the final key will be `FX.Plasma` and

this is what you would use to retrieve the text from the Shader Cache.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "plasma"

and no URL is given then the Loader will set the URL to be "plasma.glsl". It will always add `.glsl` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the GLSL File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.GLSLFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.GLSLFileConfig](../typedef/types-loader-filetypes.md)> | No |  |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.glsl`, i.e. if `key` was "alien" then the URL will be "alien.glsl". |
| shaderType | string | Yes | "'fragment'" | The type of shader. Either `fragment` for a fragment shader, or `vertex` for a vertex shader. This is ignored if you load a shader bundle. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes |  | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/GLSLFile.js#L315](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/GLSLFile.js#L315)  
> Since: 3.0.0

---

## html

### <instance> html(key, [url], [xhrSettings])

**Description:**

Adds an HTML file, or array of HTML files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.html('story', 'files/LoginForm.html');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global HTML Cache upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the HTML Cache.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the HTML Cache first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.html({

    key: 'login',

    url: 'files/LoginForm.html'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.HTMLFileConfig` for more details.

Once the file has finished loading you can access it from its Cache using its key:

```
Copy
this.load.html('login', 'files/LoginForm.html');

// and later in your game ...

var data = this.cache.html.get('login');


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `LEVEL1.` and the key was `Story` the final key will be `LEVEL1.Story` and

this is what you would use to retrieve the html from the HTML Cache.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "story"

and no URL is given then the Loader will set the URL to be "story.html". It will always add `.html` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the HTML File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.HTMLFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.HTMLFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | string | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.html`, i.e. if `key` was "alien" then the URL will be "alien.html". |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/HTMLFile.js#L84](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/HTMLFile.js#L84)  
> Since: 3.12.0

---

## htmlTexture

### <instance> htmlTexture(key, [url], [width], [height], [xhrSettings])

**Description:**

Adds an HTML File, or array of HTML Files, to the current load queue. When the files are loaded they

will be rendered to textures and stored in the Texture Manager.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.htmlTexture('instructions', 'content/intro.html', 256, 512);

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global Texture Manager upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Texture Manager.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Texture Manager first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.htmlTexture({

    key: 'instructions',

    url: 'content/intro.html',

    width: 256,

    height: 512

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.HTMLTextureFileConfig` for more details.

Once the file has finished loading you can use it as a texture for a Game Object by referencing its key:

```
Copy
this.load.htmlTexture('instructions', 'content/intro.html', 256, 512);

// and later in your game ...

this.add.image(x, y, 'instructions');


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `MENU.` and the key was `Background` the final key will be `MENU.Background` and

this is what you would use to retrieve the image from the Texture Manager.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "alien"

and no URL is given then the Loader will set the URL to be "alien.html". It will always add `.html` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

The width and height are the size of the texture to which the HTML will be rendered. It's not possible to determine these

automatically, so you will need to provide them, either as arguments or in the file config object.

When the HTML file has loaded a new SVG element is created with a size and viewbox set to the width and height given.

The SVG file has a body tag added to it, with the HTML file contents included. It then calls `window.Blob` on the SVG,

and if successful is added to the Texture Manager, otherwise it fails processing. The overall quality of the rendered

HTML depends on your browser, and some of them may not even support the svg / blob process used. Be aware that there are

limitations on what HTML can be inside an SVG. You can find out more details in this

[Mozilla MDN entry](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Drawing_DOM_objects_into_a_canvas).

Note: The ability to load this type of file will only be available if the HTMLTextureFile File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.HTMLTextureFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.HTMLTextureFileConfig](../typedef/types-loader-filetypes.md)> | No |  |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.html`, i.e. if `key` was "alien" then the URL will be "alien.html". |
| width | number | Yes | 512 | The width of the texture the HTML will be rendered to. |
| height | number | Yes | 512 | The height of the texture the HTML will be rendered to. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes |  | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/HTMLTextureFile.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/HTMLTextureFile.js#L151)  
> Since: 3.12.0

---

## image

### <instance> image(key, [url], [xhrSettings])

**Description:**

Adds an Image, or array of Images, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.image('logo', 'images/phaserLogo.png');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

Phaser can load all common image types: png, jpg, gif and any other format the browser can natively handle.

If you try to load an animated gif only the first frame will be rendered. Browsers do not natively support playback

of animated gifs to Canvas elements.

The key must be a unique String. It is used to add the file to the global Texture Manager upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Texture Manager.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Texture Manager first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.image({

    key: 'logo',

    url: 'images/AtariLogo.png'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.ImageFileConfig` for more details.

Once the file has finished loading you can use it as a texture for a Game Object by referencing its key:

```
Copy
this.load.image('logo', 'images/AtariLogo.png');

// and later in your game ...

this.add.image(x, y, 'logo');


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `MENU.` and the key was `Background` the final key will be `MENU.Background` and

this is what you would use to retrieve the image from the Texture Manager.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "alien"

and no URL is given then the Loader will set the URL to be "alien.png". It will always add `.png` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Phaser also supports the automatic loading of associated normal maps. If you have a normal map to go with this image,

then you can specify it by providing an array as the `url` where the second element is the normal map:

```
Copy
this.load.image('logo', [ 'images/AtariLogo.png', 'images/AtariLogo-n.png' ]);


```

Or, if you are using a config object use the `normalMap` property:

```
Copy
this.load.image({

    key: 'logo',

    url: 'images/AtariLogo.png',

    normalMap: 'images/AtariLogo-n.png'

});


```

The normal map file is subject to the same conditions as the image file with regard to the path, baseURL, CORs and XHR Settings.

Normal maps are a WebGL only feature.

In Phaser 3.60 a new property was added that allows you to control how images are loaded. By default, images are loaded via XHR as Blobs.

However, you can set `loader.imageLoadType: "HTMLImageElement"` in the Game Configuration and instead, the Loader will load all images

via the Image tag instead.

Note: The ability to load this type of file will only be available if the Image File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.ImageFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.ImageFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | string | Array.<string> | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.png`, i.e. if `key` was "alien" then the URL will be "alien.png". |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/ImageFile.js#L234](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/ImageFile.js#L234)  
> Since: 3.0.0

---

## isLoading

### <instance> isLoading()

**Description:**

Is the Loader actively loading, or processing loaded files?

**Returns:** boolean - `true` if the Loader is busy loading or processing, otherwise `false`.

> Source: [src/loader/LoaderPlugin.js#L874](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L874)  
> Since: 3.0.0

---

## isReady

### <instance> isReady()

**Description:**

Is the Loader ready to start a new load?

**Returns:** boolean - `true` if the Loader is ready to start a new load, otherwise `false`.

> Source: [src/loader/LoaderPlugin.js#L887](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L887)  
> Since: 3.0.0

---

## json

### <instance> json(key, [url], [dataKey], [xhrSettings])

**Description:**

Adds a JSON file, or array of JSON files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.json('wavedata', 'files/AlienWaveData.json');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global JSON Cache upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the JSON Cache.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the JSON Cache first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.json({

    key: 'wavedata',

    url: 'files/AlienWaveData.json'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.JSONFileConfig` for more details.

Once the file has finished loading you can access it from its Cache using its key:

```
Copy
this.load.json('wavedata', 'files/AlienWaveData.json');

// and later in your game ...

var data = this.cache.json.get('wavedata');


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `LEVEL1.` and the key was `Waves` the final key will be `LEVEL1.Waves` and

this is what you would use to retrieve the text from the JSON Cache.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "data"

and no URL is given then the Loader will set the URL to be "data.json". It will always add `.json` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

You can also optionally provide a `dataKey` to use. This allows you to extract only a part of the JSON and store it in the Cache,

rather than the whole file. For example, if your JSON data had a structure like this:

```
Copy
{

    "level1": {

        "baddies": {

            "aliens": {},

            "boss": {}

        }

    },

    "level2": {},

    "level3": {}

}


```

And you only wanted to store the `boss` data in the Cache, then you could pass `level1.baddies.boss`as the `dataKey`.

Note: The ability to load this type of file will only be available if the JSON File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.JSONFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.JSONFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | object | string | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.json`, i.e. if `key` was "alien" then the URL will be "alien.json". Or, can be a fully formed JSON Object. |
| dataKey | string | Yes | When the JSON file loads only this property will be stored in the Cache. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/JSONFile.js#L129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/JSONFile.js#L129)  
> Since: 3.0.0

---

## keyExists

### <instance> keyExists(file)

**Description:**

Checks the key and type of the given file to see if it will conflict with anything already

in a Cache, the Texture Manager, or the list or inflight queues.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| file | [Phaser.Loader.File](loader-file.md) | No | The file to check the key of. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if adding this file will cause a cache or queue conflict, otherwise `false`.

> Source: [src/loader/LoaderPlugin.js#L561](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L561)  
> Since: 3.7.0

---

## listenerCount

### <instance> listenerCount(event)

**Description:**

Return the number of listeners listening to a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** number - The number of listeners.

**Inherits:** [Phaser.Events.EventEmitter#listenerCount](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L75)  
> Since: 3.0.0

---

## listeners

### <instance> listeners(event)

**Description:**

Return the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** Array.<function()> - The registered listeners.

**Inherits:** [Phaser.Events.EventEmitter#listeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L64)  
> Since: 3.0.0

---

## loadComplete

### <instance> loadComplete()

**Description:**

Called at the end when the load queue is exhausted and all files have either loaded or errored.

By this point every loaded file will now be in its associated cache and ready for use.

Also clears down the Sets, puts progress to 1 and clears the deletion queue.

**Fires:** [Phaser.Loader.Events#event:COMPLETE](../event/loader-events.md), [Phaser.Loader.Events#event:POST\_PROCESS](../event/loader-events.md)

> Source: [src/loader/LoaderPlugin.js#L1125](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L1125)  
> Since: 3.7.0

---

## multiatlas

### <instance> multiatlas(key, [atlasURL], [path], [baseURL], [atlasXhrSettings])

**Description:**

Adds a Multi Texture Atlas, or array of multi atlases, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.multiatlas('level1', 'images/Level1.json');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

If you call this from outside of `preload` then you are responsible for starting the Loader afterwards and monitoring

its events to know when it's safe to use the asset. Please see the Phaser.Loader.LoaderPlugin class for more details.

Phaser expects the atlas data to be provided in a JSON file as exported from the application Texture Packer,

version 4.6.3 or above, where you have made sure to use the Phaser 3 Export option.

The way it works internally is that you provide a URL to the JSON file. Phaser then loads this JSON, parses it and

extracts which texture files it also needs to load to complete the process. If the JSON also defines normal maps,

Phaser will load those as well.

The key must be a unique String. It is used to add the file to the global Texture Manager upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Texture Manager.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Texture Manager first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.multiatlas({

    key: 'level1',

    atlasURL: 'images/Level1.json'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.MultiAtlasFileConfig` for more details.

Instead of passing a URL for the atlas JSON data you can also pass in a well formed JSON object instead.

Once the atlas has finished loading you can use frames from it as textures for a Game Object by referencing its key:

```
Copy
this.load.multiatlas('level1', 'images/Level1.json');

// and later in your game ...

this.add.image(x, y, 'level1', 'background');


```

To get a list of all available frames within an atlas please consult your Texture Atlas software.

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `MENU.` and the key was `Background` the final key will be `MENU.Background` and

this is what you would use to retrieve the image from the Texture Manager.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "alien"

and no URL is given then the Loader will set the URL to be "alien.png". It will always add `.png` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the Multi Atlas File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.MultiAtlasFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.MultiAtlasFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| atlasURL | string | Yes | The absolute or relative URL to load the texture atlas json data file from. If undefined or `null` it will be set to `<key>.json`, i.e. if `key` was "alien" then the URL will be "alien.json". |
| path | string | Yes | Optional path to use when loading the textures defined in the atlas data. |
| baseURL | string | Yes | Optional Base URL to use when loading the textures defined in the atlas data. |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object for the atlas json file. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/MultiAtlasFile.js#L212](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/MultiAtlasFile.js#L212)  
> Since: 3.7.0

---

## nextFile

### <instance> nextFile(file, success)

**Description:**

An internal method called automatically by the XHRLoader belonging to a File.

This method will remove the given file from the inflight Set and update the load progress.

If the file was successful its `onProcess` method is called, otherwise it is added to the delete queue.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| file | [Phaser.Loader.File](loader-file.md) | No | The File that just finished loading, or errored during load. |
| --- | --- | --- | --- |
| success | boolean | No | `true` if the file loaded successfully, otherwise `false`. |

**Fires:** [Phaser.Loader.Events#event:FILE\_LOAD](../event/loader-events.md), [Phaser.Loader.Events#event:FILE\_LOAD\_ERROR](../event/loader-events.md)

> Source: [src/loader/LoaderPlugin.js#L1019](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L1019)  
> Since: 3.0.0

---

## obj

### <instance> obj(key, [objURL], [matURL], [flipUV], [xhrSettings])

**Description:**

Adds a Wavefront OBJ file, or array of OBJ files, to the current load queue.

Note: You should ensure your 3D package has triangulated the OBJ file prior to export.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.obj('ufo', 'files/spaceship.obj');

}


```

You can optionally also load a Wavefront Material file as well, by providing the 3rd parameter:

```
Copy
function preload ()

{

    this.load.obj('ufo', 'files/spaceship.obj', 'files/spaceship.mtl');

}


```

If given, the material will be parsed and stored along with the obj data in the cache.

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global OBJ Cache upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the OBJ Cache.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the OBJ Cache first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.obj({

    key: 'ufo',

    url: 'files/spaceship.obj',

    matURL: 'files/spaceship.mtl',

    flipUV: true

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.OBJFileConfig` for more details.

Once the file has finished loading you can access it from its Cache using its key:

```
Copy
this.load.obj('ufo', 'files/spaceship.obj');

// and later in your game ...

var data = this.cache.obj.get('ufo');


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `LEVEL1.` and the key was `Story` the final key will be `LEVEL1.Story` and

this is what you would use to retrieve the obj from the OBJ Cache.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "story"

and no URL is given then the Loader will set the URL to be "story.obj". It will always add `.obj` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the OBJ File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.OBJFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.OBJFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| objURL | string | Yes | The absolute or relative URL to load the obj file from. If undefined or `null` it will be set to `<key>.obj`, i.e. if `key` was "alien" then the URL will be "alien.obj". |
| matURL | string | Yes | Optional absolute or relative URL to load the obj material file from. |
| flipUV | boolean | Yes | Flip the UV coordinates stored in the model data? |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/OBJFile.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/OBJFile.js#L140)  
> Since: 3.50.0

---

## off

### <instance> off(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#off](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L151)  
> Since: 3.0.0

---

## on

### <instance> on(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#on](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L98)  
> Since: 3.0.0

---

## once

### <instance> once(event, fn, [context])

**Description:**

Add a one-time listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## pack

### <instance> pack(key, [url], [dataKey], [xhrSettings])

**Description:**

Adds a JSON File Pack, or array of packs, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.pack('level1', 'data/Level1Files.json');

}


```

A File Pack is a JSON file (or object) that contains details about other files that should be added into the Loader.

Here is a small example:

```
Copy
{

   "test1": {

       "files": [

           {

               "type": "image",

               "key": "taikodrummaster",

               "url": "assets/pics/taikodrummaster.jpg"

           },

           {

               "type": "image",

               "key": "sukasuka-chtholly",

               "url": "assets/pics/sukasuka-chtholly.png"

           }

       ]

   },

   "meta": {

       "generated": "1401380327373",

       "app": "Phaser 3 Asset Packer",

       "url": "[https://phaser.io](https://phaser.io)",

       "version": "1.0",

       "copyright": "Photon Storm Ltd. 2018"

   }

}


```

The pack can be split into sections. In the example above you'll see a section called `test1`. You can tell

the `load.pack` method to parse only a particular section of a pack. The pack is stored in the JSON Cache,

so you can pass it to the Loader to process additional sections as needed in your game, or you can just load

them all at once without specifying anything.

The pack file can contain an entry for any type of file that Phaser can load. The object structures exactly

match that of the file type configs, and all properties available within the file type configs can be used

in the pack file too. An entry's `type` is the name of the Loader method that will load it, e.g., 'image'.

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

If you call this from outside of `preload` then you are responsible for starting the Loader afterwards and monitoring

its events to know when it's safe to use the asset. Please see the Phaser.Loader.LoaderPlugin class for more details.

The key must be a unique String. It is used to add the file to the global JSON Cache upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the JSON Cache.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the JSON Cache first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.pack({

    key: 'level1',

    url: 'data/Level1Files.json'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.PackFileConfig` for more details.

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `LEVEL1.` and the key was `Waves` the final key will be `LEVEL1.Waves` and

this is what you would use to retrieve the text from the JSON Cache.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "data"

and no URL is given then the Loader will set the URL to be "data.json". It will always add `.json` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

You can also optionally provide a `dataKey` to use. This allows you to extract only a part of the JSON and store it in the Cache,

rather than the whole file. For example, if your JSON data had a structure like this:

```
Copy
{

    "level1": {

        "baddies": {

            "aliens": {},

            "boss": {}

        }

    },

    "level2": {},

    "level3": {}

}


```

And you only wanted to store the `boss` data in the Cache, then you could pass `level1.baddies.boss`as the `dataKey`.

Note: The ability to load this type of file will only be available if the Pack File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.PackFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.PackFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | string | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.json`, i.e. if `key` was "alien" then the URL will be "alien.json". |
| dataKey | string | Yes | When the JSON file loads only this property will be stored in the Cache. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/PackFile.js#L81](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/PackFile.js#L81)  
> Since: 3.7.0

---

## plugin

### <instance> plugin(key, [url], [start], [mapping], [xhrSettings])

**Description:**

Adds a Plugin Script file, or array of plugin files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.plugin('modplayer', 'plugins/ModPlayer.js');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String and not already in-use by another file in the Loader.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.plugin({

    key: 'modplayer',

    url: 'plugins/ModPlayer.js'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.PluginFileConfig` for more details.

Once the file has finished loading it will automatically be converted into a script element

via `document.createElement('script')`. It will have its language set to JavaScript, `defer` set to

false and then the resulting element will be appended to `document.head`. Any code then in the

script will be executed. It will then be passed to the Phaser PluginCache.register method.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "alien"

and no URL is given then the Loader will set the URL to be "alien.js". It will always add `.js` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the Plugin File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.PluginFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.PluginFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | string | function | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.js`, i.e. if `key` was "alien" then the URL will be "alien.js". Or, a plugin function. |
| start | boolean | Yes | Automatically start the plugin after loading? |
| mapping | string | Yes | If this plugin is to be injected into the Scene, this is the property key used. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/PluginFile.js#L129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/PluginFile.js#L129)  
> Since: 3.0.0

---

## removeAllListeners

### <instance> removeAllListeners([event])

**Description:**

Remove all listeners, or those of the specified event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | Yes | The event name. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeListener

### <instance> removeListener(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## removePack

### <instance> removePack(packKey, [dataKey])

**Description:**

Remove the resources listed in an Asset Pack.

This removes Animations from the Animation Manager, Textures from the Texture Manager, and all other assets from their respective caches.

It doesn't remove the Pack itself from the JSON cache, if it exists there.

If the Pack includes another Pack, its resources will be removed too.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| packKey | string | object | No | The key of an Asset Pack in the JSON cache, or a Pack File data. |
| --- | --- | --- | --- |
| dataKey | string | Yes | A key in the Pack data, if you want to process only a section of it. |

> Source: [src/loader/LoaderPlugin.js#L700](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L700)  
> Since: 3.85.0

---

## reset

### <instance> reset()

**Description:**

Resets the Loader.

This will clear all lists and reset the base URL, path and prefix.

Warning: If the Loader is currently downloading files, or has files in its queue, they will be aborted.

> Source: [src/loader/LoaderPlugin.js#L1223](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L1223)  
> Since: 3.0.0

---

## save

### <instance> save(data, [filename], [filetype])

**Description:**

Causes the browser to save the given data as a file to its default Downloads folder.

Creates a DOM level anchor link, assigns it as being a `download` anchor, sets the href

to be an ObjectURL based on the given data, and then invokes a click event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| data | \* | No |  | The data to be saved. Will be passed through URL.createObjectURL. |
| --- | --- | --- | --- | --- |
| filename | string | Yes | "file.json" | The filename to save the file as. |
| filetype | string | Yes | "application/json" | The file type to use when saving the file. Defaults to JSON. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - This Loader plugin.

> Source: [src/loader/LoaderPlugin.js#L1189](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L1189)  
> Since: 3.0.0

---

## saveJSON

### <instance> saveJSON(data, [filename])

**Description:**

Converts the given JSON data into a file that the browser then prompts you to download so you can save it locally.

The data must be well formed JSON and ready-parsed, not a JavaScript object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| data | \* | No |  | The JSON data, ready parsed. |
| --- | --- | --- | --- | --- |
| filename | string | Yes | "file.json" | The name to save the JSON file as. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - This Loader plugin.

> Source: [src/loader/LoaderPlugin.js#L1171](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L1171)  
> Since: 3.0.0

---

## sceneFile

### <instance> sceneFile(key, [url], [xhrSettings])

**Description:**

Adds an external Scene file, or array of Scene files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.sceneFile('Level1', 'src/Level1.js');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global Scene Manager upon a successful load.

For a Scene File it's vitally important that the key matches the class name in the JavaScript file.

For example here is the source file:

```
Copy
class ExternalScene extends Phaser.Scene {



    constructor ()

    {

        super('myScene');

    }



}


```

Because the class is called `ExternalScene` that is the exact same key you must use when loading it:

```
Copy
function preload ()

{

    this.load.sceneFile('ExternalScene', 'src/yourScene.js');

}


```

The key that is used within the Scene Manager can either be set to the same, or you can override it in the Scene

constructor, as we've done in the example above, where the Scene key was changed to `myScene`.

The key should be unique both in terms of files being loaded and Scenes already present in the Scene Manager.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Scene Manager first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.sceneFile({

    key: 'Level1',

    url: 'src/Level1.js'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.SceneFileConfig` for more details.

Once the file has finished loading it will be added to the Scene Manager.

```
Copy
this.load.sceneFile('Level1', 'src/Level1.js');

// and later in your game ...

this.scene.start('Level1');


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `WORLD1.` and the key was `Story` the final key will be `WORLD1.Story` and

this is what you would use to retrieve the text from the Scene Manager.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "story"

and no URL is given then the Loader will set the URL to be "story.js". It will always add `.js` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the Scene File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.SceneFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.SceneFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | string | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.js`, i.e. if `key` was "alien" then the URL will be "alien.js". |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/SceneFile.js#L101](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/SceneFile.js#L101)  
> Since: 3.16.0

---

## scenePlugin

### <instance> scenePlugin(key, [url], [systemKey], [sceneKey], [xhrSettings])

**Description:**

Adds a Scene Plugin Script file, or array of plugin files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.scenePlugin('ModPlayer', 'plugins/ModPlayer.js', 'modPlayer', 'mods');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String and not already in-use by another file in the Loader.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.scenePlugin({

    key: 'modplayer',

    url: 'plugins/ModPlayer.js'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.ScenePluginFileConfig` for more details.

Once the file has finished loading it will automatically be converted into a script element

via `document.createElement('script')`. It will have its language set to JavaScript, `defer` set to

false and then the resulting element will be appended to `document.head`. Any code then in the

script will be executed. It will then be passed to the Phaser PluginCache.register method.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "alien"

and no URL is given then the Loader will set the URL to be "alien.js". It will always add `.js` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the Script File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.ScenePluginFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.ScenePluginFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | string | function | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.js`, i.e. if `key` was "alien" then the URL will be "alien.js". Or, set to a plugin function. |
| systemKey | string | Yes | If this plugin is to be added to Scene.Systems, this is the property key for it. |
| sceneKey | string | Yes | If this plugin is to be added to the Scene, this is the property key for it. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/ScenePluginFile.js#L123](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/ScenePluginFile.js#L123)  
> Since: 3.8.0

---

## script

### <instance> script(key, [url], [type], [xhrSettings])

**Description:**

Adds a Script file, or array of Script files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.script('aliens', 'lib/aliens.js');

}


```

If the script file contains a module, then you should specify that using the 'type' parameter:

```
Copy
function preload ()

{

    this.load.script('aliens', 'lib/aliens.js', 'module');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String and not already in-use by another file in the Loader.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.script({

    key: 'aliens',

    url: 'lib/aliens.js',

    type: 'script' // or 'module'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.ScriptFileConfig` for more details.

Once the file has finished loading it will automatically be converted into a script element

via `document.createElement('script')`. It will have its language set to JavaScript, `defer` set to

false and then the resulting element will be appended to `document.head`. Any code then in the

script will be executed.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "alien"

and no URL is given then the Loader will set the URL to be "alien.js". It will always add `.js` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the Script File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.ScriptFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.ScriptFileConfig](../typedef/types-loader-filetypes.md)> | No |  |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.js`, i.e. if `key` was "alien" then the URL will be "alien.js". |
| type | string | Yes | "'script'" | The script type. Should be either 'script' for classic JavaScript, or 'module' if the file contains an exported module. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes |  | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/ScriptFile.js#L96](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/ScriptFile.js#L96)  
> Since: 3.0.0

---

## scripts

### <instance> scripts(key, [url], [extension], [xhrSettings])

**Description:**

Adds an array of Script files to the current load queue.

The difference between this and the `ScriptFile` file type is that you give an array of scripts to this method,

and the scripts are then processed *exactly* in that order. This allows you to load a bunch of scripts that

may have dependencies on each other without worrying about the async nature of traditional script loading.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.scripts('PostProcess', [

        'libs/shaders/CopyShader.js',

        'libs/postprocessing/EffectComposer.js',

        'libs/postprocessing/RenderPass.js',

        'libs/postprocessing/MaskPass.js',

        'libs/postprocessing/ShaderPass.js',

        'libs/postprocessing/AfterimagePass.js'

   ]);

}


```

In the code above the script files will all be loaded in parallel but only processed (i.e. invoked) in the exact

order given in the array.

The files are **not** loaded right away. They are added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the files are queued

it means you cannot use the files immediately after calling this method, but must wait for the files to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String and not already in-use by another file in the Loader.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.scripts({

    key: 'PostProcess',

    url: [

        'libs/shaders/CopyShader.js',

        'libs/postprocessing/EffectComposer.js',

        'libs/postprocessing/RenderPass.js',

        'libs/postprocessing/MaskPass.js',

        'libs/postprocessing/ShaderPass.js',

        'libs/postprocessing/AfterimagePass.js'

       ]

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.MultiScriptFileConfig` for more details.

Once all the files have finished loading they will automatically be converted into a script element

via `document.createElement('script')`. They will have their language set to JavaScript, `defer` set to

false and then the resulting element will be appended to `document.head`. Any code then in the

script will be executed. This is done in the exact order the files are specified in the url array.

The URLs can be relative or absolute. If the URLs are relative the `Loader.baseURL` and `Loader.path` values will be prepended to them.

Note: The ability to load this type of file will only be available if the MultiScript File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.MultiScriptFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.MultiScriptFileConfig](../typedef/types-loader-filetypes.md)> | No |  |
| --- | --- | --- | --- | --- |
| url | Array.<string> | Yes |  | An array of absolute or relative URLs to load the script files from. They are processed in the order given in the array. |
| extension | string | Yes | "'js'" | The default file extension to use if no url is provided. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes |  | Extra XHR Settings specifically for these files. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/MultiScriptFile.js#L109](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/MultiScriptFile.js#L109)  
> Since: 3.17.0

---

## setBaseURL

### <instance> setBaseURL([url])

**Description:**

If you want to append a URL before the path of any asset you can set this here.

Useful if allowing the asset base url to be configured outside of the game code.

Once a base URL is set it will affect every file loaded by the Loader from that point on. It does *not* change any

file *already* being loaded. To reset it, call this method with no arguments.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| url | string | Yes | The URL to use. Leave empty to reset. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - This Loader object.

> Source: [src/loader/LoaderPlugin.js#L399](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L399)  
> Since: 3.0.0

---

## setCORS

### <instance> setCORS([crossOrigin])

**Description:**

Sets the Cross Origin Resource Sharing value used when loading files.

Files can override this value on a per-file basis by specifying an alternative `crossOrigin` value in their file config.

Once CORs is set it will then affect every file loaded by the Loader from that point on, as long as they don't have

their own CORs setting. To reset it, call this method with no arguments.

For more details about CORs see <https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS>

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| crossOrigin | string | Yes | The value to use for the `crossOrigin` property in the load request. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - This Loader object.

> Source: [src/loader/LoaderPlugin.js#L492](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L492)  
> Since: 3.0.0

---

## setPath

### <instance> setPath([path])

**Description:**

The value of `path`, if set, is placed before any *relative* file path given. For example:

```
Copy
this.load.setPath("images/sprites/");

this.load.image("ball", "ball.png");

this.load.image("tree", "level1/oaktree.png");

this.load.image("boom", "[http://server.com/explode.png](http://server.com/explode.png)");


```

Would load the `ball` file from `images/sprites/ball.png` and the tree from

`images/sprites/level1/oaktree.png` but the file `boom` would load from the URL

given as it's an absolute URL.

Please note that the path is added before the filename but *after* the baseURL (if set.)

Once a path is set it will then affect every file added to the Loader from that point on. It does *not* change any

file *already* in the load queue. To reset it, call this method with no arguments.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| path | string | Yes | The path to use. Leave empty to reset. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - This Loader object.

> Source: [src/loader/LoaderPlugin.js#L428](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L428)  
> Since: 3.0.0

---

## setPrefix

### <instance> setPrefix([prefix])

**Description:**

An optional prefix that is automatically prepended to the start of every file key.

If prefix was `MENU.` and you load an image with the key 'Background' the resulting key would be `MENU.Background`.

Once a prefix is set it will then affect every file added to the Loader from that point on. It does *not* change any

file *already* in the load queue. To reset it, call this method with no arguments.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| prefix | string | Yes | The prefix to use. Leave empty to reset. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - This Loader object.

> Source: [src/loader/LoaderPlugin.js#L468](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L468)  
> Since: 3.7.0

---

## spritesheet

### <instance> spritesheet(key, [url], [frameConfig], [xhrSettings])

**Description:**

Adds a Sprite Sheet Image, or array of Sprite Sheet Images, to the current load queue.

The term 'Sprite Sheet' in Phaser means a fixed-size sheet. Where every frame in the sheet is the exact same size,

and you reference those frames using numbers, not frame names. This is not the same thing as a Texture Atlas, where

the frames are packed in a way where they take up the least amount of space, and are referenced by their names,

not numbers. Some articles and software use the term 'Sprite Sheet' to mean Texture Atlas, so please be aware of

what sort of file you're actually trying to load.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.spritesheet('bot', 'images/robot.png', { frameWidth: 32, frameHeight: 38 });

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

Phaser can load all common image types: png, jpg, gif and any other format the browser can natively handle.

If you try to load an animated gif only the first frame will be rendered. Browsers do not natively support playback

of animated gifs to Canvas elements.

The key must be a unique String. It is used to add the file to the global Texture Manager upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Texture Manager.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Texture Manager first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.spritesheet({

    key: 'bot',

    url: 'images/robot.png',

    frameConfig: {

        frameWidth: 32,

        frameHeight: 38,

        startFrame: 0,

        endFrame: 8

    }

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.SpriteSheetFileConfig` for more details.

Once the file has finished loading you can use it as a texture for a Game Object by referencing its key:

```
Copy
this.load.spritesheet('bot', 'images/robot.png', { frameWidth: 32, frameHeight: 38 });

// and later in your game ...

this.add.image(x, y, 'bot', 0);


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `PLAYER.` and the key was `Running` the final key will be `PLAYER.Running` and

this is what you would use to retrieve the image from the Texture Manager.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "alien"

and no URL is given then the Loader will set the URL to be "alien.png". It will always add `.png` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Phaser also supports the automatic loading of associated normal maps. If you have a normal map to go with this image,

then you can specify it by providing an array as the `url` where the second element is the normal map:

```
Copy
this.load.spritesheet('logo', [ 'images/AtariLogo.png', 'images/AtariLogo-n.png' ], { frameWidth: 256, frameHeight: 80 });


```

Or, if you are using a config object use the `normalMap` property:

```
Copy
this.load.spritesheet({

    key: 'logo',

    url: 'images/AtariLogo.png',

    normalMap: 'images/AtariLogo-n.png',

    frameConfig: {

        frameWidth: 256,

        frameHeight: 80

    }

});


```

The normal map file is subject to the same conditions as the image file with regard to the path, baseURL, CORs and XHR Settings.

Normal maps are a WebGL only feature.

Note: The ability to load this type of file will only be available if the Sprite Sheet File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.SpriteSheetFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.SpriteSheetFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | string | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.png`, i.e. if `key` was "alien" then the URL will be "alien.png". |
| frameConfig | [Phaser.Types.Loader.FileTypes.ImageFrameConfig](../typedef/types-loader-filetypes.md) | Yes | The frame configuration object. At a minimum it should have a `frameWidth` property. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/SpriteSheetFile.js#L87](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/SpriteSheetFile.js#L87)  
> Since: 3.0.0

---

## start

### <instance> start()

**Description:**

Starts the Loader running. This will reset the progress and totals and then emit a `start` event.

If there is nothing in the queue the Loader will immediately complete, otherwise it will start

loading the first batch of files.

The Loader is started automatically if the queue is populated within your Scenes `preload` method.

However, outside of this, you need to call this method to start it.

If the Loader is already running this method will simply return.

**Fires:** [Phaser.Loader.Events#event:START](../event/loader-events.md)

> Source: [src/loader/LoaderPlugin.js#L900](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L900)  
> Since: 3.0.0

---

## svg

### <instance> svg(key, [url], [svgConfig], [xhrSettings])

**Description:**

Adds an SVG File, or array of SVG Files, to the current load queue. When the files are loaded they

will be rendered to bitmap textures and stored in the Texture Manager.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.svg('morty', 'images/Morty.svg');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global Texture Manager upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Texture Manager.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Texture Manager first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.svg({

    key: 'morty',

    url: 'images/Morty.svg'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.SVGFileConfig` for more details.

Once the file has finished loading you can use it as a texture for a Game Object by referencing its key:

```
Copy
this.load.svg('morty', 'images/Morty.svg');

// and later in your game ...

this.add.image(x, y, 'morty');


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `MENU.` and the key was `Background` the final key will be `MENU.Background` and

this is what you would use to retrieve the image from the Texture Manager.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "alien"

and no URL is given then the Loader will set the URL to be "alien.html". It will always add `.html` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

You can optionally pass an SVG Resize Configuration object when you load an SVG file. By default the SVG will be rendered to a texture

at the same size defined in the SVG file attributes. However, this isn't always desirable. You may wish to resize the SVG (either down

or up) to improve texture clarity, or reduce texture memory consumption. You can either specify an exact width and height to resize

the SVG to:

```
Copy
function preload ()

{

    this.load.svg('morty', 'images/Morty.svg', { width: 300, height: 600 });

}


```

Or when using a configuration object:

```
Copy
this.load.svg({

    key: 'morty',

    url: 'images/Morty.svg',

    svgConfig: {

        width: 300,

        height: 600

    }

});


```

Alternatively, you can just provide a scale factor instead:

```
Copy
function preload ()

{

    this.load.svg('morty', 'images/Morty.svg', { scale: 2.5 });

}


```

Or when using a configuration object:

```
Copy
this.load.svg({

    key: 'morty',

    url: 'images/Morty.svg',

    svgConfig: {

        scale: 2.5

    }

});


```

If scale, width and height values are all given, the scale has priority and the width and height values are ignored.

Note: The ability to load this type of file will only be available if the SVG File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.SVGFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.SVGFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | string | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.svg`, i.e. if `key` was "alien" then the URL will be "alien.svg". |
| svgConfig | [Phaser.Types.Loader.FileTypes.SVGSizeConfig](../typedef/types-loader-filetypes.md) | Yes | The svg size configuration object. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/SVGFile.js#L195](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/SVGFile.js#L195)  
> Since: 3.0.0

---

## text

### <instance> text(key, [url], [xhrSettings])

**Description:**

Adds a Text file, or array of Text files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.text('story', 'files/IntroStory.txt');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global Text Cache upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Text Cache.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Text Cache first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.text({

    key: 'story',

    url: 'files/IntroStory.txt'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.TextFileConfig` for more details.

Once the file has finished loading you can access it from its Cache using its key:

```
Copy
this.load.text('story', 'files/IntroStory.txt');

// and later in your game ...

var data = this.cache.text.get('story');


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `LEVEL1.` and the key was `Story` the final key will be `LEVEL1.Story` and

this is what you would use to retrieve the text from the Text Cache.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "story"

and no URL is given then the Loader will set the URL to be "story.txt". It will always add `.txt` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the Text File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.TextFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.TextFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | string | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.txt`, i.e. if `key` was "alien" then the URL will be "alien.txt". |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/TextFile.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/TextFile.js#L88)  
> Since: 3.0.0

---

## texture

### <instance> texture(key, [url], [xhrSettings])

**Description:**

Adds a Compressed Texture file to the current load queue. This feature is WebGL only.

This method takes a key and a configuration object, which lists the different formats

and files associated with them.

The texture format object should be ordered in GPU priority order, with IMG as the last entry.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
preload ()

{

    this.load.texture('yourPic', {

        ASTC: { type: 'PVR', textureURL: 'pic-astc-4x4.pvr' },

        PVRTC: { type: 'PVR', textureURL: 'pic-pvrtc-4bpp-rgba.pvr' },

        S3TC: { type: 'PVR', textureURL: 'pic-dxt5.pvr' },

        IMG: { textureURL: 'pic.png' }

    });


```

If you wish to load a texture atlas, provide the `atlasURL` property:

```
Copy
preload ()

{

    const path = 'assets/compressed';



    this.load.texture('yourAtlas', {

        'ASTC': { type: 'PVR', textureURL: `${path}/textures-astc-4x4.pvr`, atlasURL: `${path}/textures.json` },

        'PVRTC': { type: 'PVR', textureURL: `${path}/textures-pvrtc-4bpp-rgba.pvr`, atlasURL: `${path}/textures-pvrtc-4bpp-rgba.json` },

        'S3TC': { type: 'PVR', textureURL: `${path}/textures-dxt5.pvr`, atlasURL: `${path}/textures-dxt5.json` },

        'IMG': { textureURL: `${path}/textures.png`, atlasURL: `${path}/textures.json` }

    });

}


```

If you wish to load a Multi Atlas, as exported from Texture Packer Pro, use the `multiAtlasURL` property instead:

```
Copy
preload ()

{

    const path = 'assets/compressed';



    this.load.texture('yourAtlas', {

        'ASTC': { type: 'PVR', atlasURL: `${path}/textures.json` },

        'PVRTC': { type: 'PVR', atlasURL: `${path}/textures-pvrtc-4bpp-rgba.json` },

        'S3TC': { type: 'PVR', atlasURL: `${path}/textures-dxt5.json` },

        'IMG': { atlasURL: `${path}/textures.json` }

    });

}


```

When loading a Multi Atlas you do not need to specify the `textureURL` property as it will be read from the JSON file.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.texture({

    key: 'yourPic',

    url: {

        ASTC: { type: 'PVR', textureURL: 'pic-astc-4x4.pvr' },

        PVRTC: { type: 'PVR', textureURL: 'pic-pvrtc-4bpp-rgba.pvr' },

        S3TC: { type: 'PVR', textureURL: 'pic-dxt5.pvr' },

        IMG: { textureURL: 'pic.png' }

   }

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.CompressedTextureFileConfig` for more details.

The number of formats you provide to this function is up to you, but you should ensure you

cover the primary platforms where appropriate.

The 'IMG' entry is a fallback to a JPG or PNG, should the browser be unable to load any of the other

formats presented to this function. You should really always include this, although it is optional.

Phaser supports loading both the PVR and KTX container formats. Within those, it can parse

the following texture compression formats:

ETC

ETC1

ATC

ASTC

BPTC

RGTC

PVRTC

S3TC

S3TCSRGB

For more information about the benefits of compressed textures please see the

following articles:

Texture Compression in 2020 (<https://aras-p.info/blog/2020/12/08/Texture-Compression-in-2020/>)

Compressed GPU Texture Formats (<https://themaister.net/blog/2020/08/12/compressed-gpu-texture-formats-a-review-and-compute-shader-decoders-part-1/>)

To create compressed texture files use a 3rd party application such as:

Texture Packer (<https://www.codeandweb.com/texturepacker/tutorials/how-to-create-sprite-sheets-for-phaser3?utm_source=ad&utm_medium=banner&utm_campaign=phaser-2018-10-16>)

PVRTexTool (<https://developer.imaginationtech.com/pvrtextool/>) - available for Windows, macOS and Linux.

Mali Texture Compression Tool (<https://developer.arm.com/tools-and-software/graphics-and-gaming/mali-texture-compression-tool>)

ASTC Encoder (<https://github.com/ARM-software/astc-encoder>)

ASTCs must have a Channel Type of Unsigned Normalized Bytes (UNorm).

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global Texture Manager upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Texture Manager.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Texture Manager first, before loading a new one.

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `LEVEL1.` and the key was `Data` the final key will be `LEVEL1.Data` and

this is what you would use to retrieve the text from the Texture Manager.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

Unlike other file loaders in Phaser, the URLs must include the file extension.

Note: The ability to load this type of file will only be available if the Compressed Texture File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.CompressedTextureFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.CompressedTextureFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | [Phaser.Types.Loader.FileTypes.CompressedTextureFileConfig](../typedef/types-loader-filetypes.md) | Yes | The compressed texture configuration object. Not required if passing a config object as the `key` parameter. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/CompressedTextureFile.js#L337](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/CompressedTextureFile.js#L337)  
> Since: 3.60.0

---

## tilemapCSV

### <instance> tilemapCSV(key, [url], [xhrSettings])

**Description:**

Adds a CSV Tilemap file, or array of CSV files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.tilemapCSV('level1', 'maps/Level1.csv');

}


```

Tilemap CSV data can be created in a text editor, or a 3rd party app that exports as CSV.

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global Tilemap Cache upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Tilemap Cache.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Text Cache first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.tilemapCSV({

    key: 'level1',

    url: 'maps/Level1.csv'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.TilemapCSVFileConfig` for more details.

Once the file has finished loading you can access it from its Cache using its key:

```
Copy
this.load.tilemapCSV('level1', 'maps/Level1.csv');

// and later in your game ...

var map = this.make.tilemap({ key: 'level1' });


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `LEVEL1.` and the key was `Story` the final key will be `LEVEL1.Story` and

this is what you would use to retrieve the text from the Tilemap Cache.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "level"

and no URL is given then the Loader will set the URL to be "level.csv". It will always add `.csv` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the Tilemap CSV File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.TilemapCSVFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.TilemapCSVFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | string | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.csv`, i.e. if `key` was "alien" then the URL will be "alien.csv". |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/TilemapCSVFile.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/TilemapCSVFile.js#L100)  
> Since: 3.0.0

---

## tilemapImpact

### <instance> tilemapImpact(key, [url], [xhrSettings])

**Description:**

Adds an Impact.js Tilemap file, or array of map files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.tilemapImpact('level1', 'maps/Level1.json');

}


```

Impact Tilemap data is created the Impact.js Map Editor called Weltmeister.

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global Tilemap Cache upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Tilemap Cache.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Text Cache first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.tilemapImpact({

    key: 'level1',

    url: 'maps/Level1.json'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.TilemapImpactFileConfig` for more details.

Once the file has finished loading you can access it from its Cache using its key:

```
Copy
this.load.tilemapImpact('level1', 'maps/Level1.json');

// and later in your game ...

var map = this.make.tilemap({ key: 'level1' });


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `LEVEL1.` and the key was `Story` the final key will be `LEVEL1.Story` and

this is what you would use to retrieve the text from the Tilemap Cache.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "level"

and no URL is given then the Loader will set the URL to be "level.json". It will always add `.json` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the Tilemap Impact File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.TilemapImpactFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.TilemapImpactFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | string | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.json`, i.e. if `key` was "alien" then the URL will be "alien.json". |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/TilemapImpactFile.js#L61](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/TilemapImpactFile.js#L61)  
> Since: 3.7.0

---

## tilemapTiledJSON

### <instance> tilemapTiledJSON(key, [url], [xhrSettings])

**Description:**

Adds a Tiled JSON Tilemap file, or array of map files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.tilemapTiledJSON('level1', 'maps/Level1.json');

}


```

The Tilemap data is created using the Tiled Map Editor and selecting JSON as the export format.

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global Tilemap Cache upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Tilemap Cache.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Text Cache first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.tilemapTiledJSON({

    key: 'level1',

    url: 'maps/Level1.json'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.TilemapJSONFileConfig` for more details.

Once the file has finished loading you can access it from its Cache using its key:

```
Copy
this.load.tilemapTiledJSON('level1', 'maps/Level1.json');

// and later in your game ...

var map = this.make.tilemap({ key: 'level1' });


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `LEVEL1.` and the key was `Story` the final key will be `LEVEL1.Story` and

this is what you would use to retrieve the text from the Tilemap Cache.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "level"

and no URL is given then the Loader will set the URL to be "level.json". It will always add `.json` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the Tilemap JSON File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.TilemapJSONFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.TilemapJSONFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | object | string | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.json`, i.e. if `key` was "alien" then the URL will be "alien.json". Or, a well formed JSON object. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/TilemapJSONFile.js#L61](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/TilemapJSONFile.js#L61)  
> Since: 3.0.0

---

## unityAtlas

### <instance> unityAtlas(key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings])

**Description:**

Adds a Unity YAML based Texture Atlas, or array of atlases, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.unityAtlas('mainmenu', 'images/MainMenu.png', 'images/MainMenu.txt');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

If you call this from outside of `preload` then you are responsible for starting the Loader afterwards and monitoring

its events to know when it's safe to use the asset. Please see the Phaser.Loader.LoaderPlugin class for more details.

Phaser expects the atlas data to be provided in a YAML formatted text file as exported from Unity.

Phaser can load all common image types: png, jpg, gif and any other format the browser can natively handle.

The key must be a unique String. It is used to add the file to the global Texture Manager upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Texture Manager.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Texture Manager first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.unityAtlas({

    key: 'mainmenu',

    textureURL: 'images/MainMenu.png',

    atlasURL: 'images/MainMenu.txt'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.UnityAtlasFileConfig` for more details.

Once the atlas has finished loading you can use frames from it as textures for a Game Object by referencing its key:

```
Copy
this.load.unityAtlas('mainmenu', 'images/MainMenu.png', 'images/MainMenu.json');

// and later in your game ...

this.add.image(x, y, 'mainmenu', 'background');


```

To get a list of all available frames within an atlas please consult your Texture Atlas software.

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `MENU.` and the key was `Background` the final key will be `MENU.Background` and

this is what you would use to retrieve the image from the Texture Manager.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "alien"

and no URL is given then the Loader will set the URL to be "alien.png". It will always add `.png` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Phaser also supports the automatic loading of associated normal maps. If you have a normal map to go with this image,

then you can specify it by providing an array as the `url` where the second element is the normal map:

```
Copy
this.load.unityAtlas('mainmenu', [ 'images/MainMenu.png', 'images/MainMenu-n.png' ], 'images/MainMenu.txt');


```

Or, if you are using a config object use the `normalMap` property:

```
Copy
this.load.unityAtlas({

    key: 'mainmenu',

    textureURL: 'images/MainMenu.png',

    normalMap: 'images/MainMenu-n.png',

    atlasURL: 'images/MainMenu.txt'

});


```

The normal map file is subject to the same conditions as the image file with regard to the path, baseURL, CORs and XHR Settings.

Normal maps are a WebGL only feature.

Note: The ability to load this type of file will only be available if the Unity Atlas File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.UnityAtlasFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.UnityAtlasFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| textureURL | string | Array.<string> | Yes | The absolute or relative URL to load the texture image file from. If undefined or `null` it will be set to `<key>.png`, i.e. if `key` was "alien" then the URL will be "alien.png". |
| atlasURL | string | Yes | The absolute or relative URL to load the texture atlas data file from. If undefined or `null` it will be set to `<key>.txt`, i.e. if `key` was "alien" then the URL will be "alien.txt". |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object for the atlas image file. Used in replacement of the Loaders default XHR Settings. |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object for the atlas data file. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/UnityAtlasFile.js#L107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/UnityAtlasFile.js#L107)  
> Since: 3.0.0

---

## update

### <instance> update()

**Description:**

Called automatically during the load process.

> Source: [src/loader/LoaderPlugin.js#L965](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L965)  
> Since: 3.10.0

---

## updateProgress

### <instance> updateProgress()

**Description:**

Called automatically during the load process.

It updates the `progress` value and then emits a progress event, which you can use to

display a loading bar in your game.

**Fires:** [Phaser.Loader.Events#event:PROGRESS](../event/loader-events.md)

> Source: [src/loader/LoaderPlugin.js#L949](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L949)  
> Since: 3.0.0

---

## video

### <instance> video(key, [urls], [noAudio])

**Description:**

Adds a Video file, or array of video files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.video('intro', [ 'video/level1.mp4', 'video/level1.webm', 'video/level1.mov' ]);

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global Video Cache upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the Video Cache.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the Video Cache first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.video({

    key: 'intro',

    url: [ 'video/level1.mp4', 'video/level1.webm', 'video/level1.mov' ],

    noAudio: true

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.VideoFileConfig` for more details.

The URLs can be relative or absolute. If the URLs are relative the `Loader.baseURL` and `Loader.path` values will be prepended to them.

Due to different browsers supporting different video file types you should usually provide your video files in a variety of formats.

mp4, mov and webm are the most common. If you provide an array of URLs then the Loader will determine which *one* file to load based on

browser support, starting with the first in the array and progressing to the end.

Unlike most asset-types, videos do not *need* to be preloaded. You can create a Video Game Object and then call its `loadURL` method,

to load a video at run-time, rather than in advance.

Note: The ability to load this type of file will only be available if the Video File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.VideoFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.VideoFileConfig](../typedef/types-loader-filetypes.md)> | No |  |
| --- | --- | --- | --- | --- |
| urls | string | Array.<string> | [Phaser.Types.Loader.FileTypes.VideoFileURLConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.VideoFileURLConfig](../typedef/types-loader-filetypes.md)> | Yes |
| noAudio | boolean | Yes | false | Does the video have an audio track? If not you can enable auto-playing on it. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/VideoFile.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/VideoFile.js#L113)  
> Since: 3.20.0

---

## xml

### <instance> xml(key, [url], [xhrSettings])

**Description:**

Adds an XML file, or array of XML files, to the current load queue.

You can call this method from within your Scene's `preload`, along with any other files you wish to load:

```
Copy
function preload ()

{

    this.load.xml('wavedata', 'files/AlienWaveData.xml');

}


```

The file is **not** loaded right away. It is added to a queue ready to be loaded either when the loader starts,

or if it's already running, when the next free load slot becomes available. This happens automatically if you

are calling this from within the Scene's `preload` method, or a related callback. Because the file is queued

it means you cannot use the file immediately after calling this method, but must wait for the file to complete.

The typical flow for a Phaser Scene is that you load assets in the Scene's `preload` method and then when the

Scene's `create` method is called you are guaranteed that all of those assets are ready for use and have been

loaded.

The key must be a unique String. It is used to add the file to the global XML Cache upon a successful load.

The key should be unique both in terms of files being loaded and files already present in the XML Cache.

Loading a file using a key that is already taken will result in a warning. If you wish to replace an existing file

then remove it from the XML Cache first, before loading a new one.

Instead of passing arguments you can pass a configuration object, such as:

```
Copy
this.load.xml({

    key: 'wavedata',

    url: 'files/AlienWaveData.xml'

});


```

See the documentation for `Phaser.Types.Loader.FileTypes.XMLFileConfig` for more details.

Once the file has finished loading you can access it from its Cache using its key:

```
Copy
this.load.xml('wavedata', 'files/AlienWaveData.xml');

// and later in your game ...

var data = this.cache.xml.get('wavedata');


```

If you have specified a prefix in the loader, via `Loader.setPrefix` then this value will be prepended to this files

key. For example, if the prefix was `LEVEL1.` and the key was `Waves` the final key will be `LEVEL1.Waves` and

this is what you would use to retrieve the text from the XML Cache.

The URL can be relative or absolute. If the URL is relative the `Loader.baseURL` and `Loader.path` values will be prepended to it.

If the URL isn't specified the Loader will take the key and create a filename from that. For example if the key is "data"

and no URL is given then the Loader will set the URL to be "data.xml". It will always add `.xml` as the extension, although

this can be overridden if using an object instead of method arguments. If you do not desire this action then provide a URL.

Note: The ability to load this type of file will only be available if the XML File type has been built into Phaser.

It is available in the default build but can be excluded from custom builds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.XMLFileConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.XMLFileConfig](../typedef/types-loader-filetypes.md)> | No |
| --- | --- | --- | --- |
| url | string | Yes | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.xml`, i.e. if `key` was "alien" then the URL will be "alien.xml". |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md) | Yes | An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings. |

**Returns:** [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) - The Loader instance.

**Fires:** [Phaser.Loader.Events#event:ADD](../event/loader-events.md)

> Source: [src/loader/filetypes/XMLFile.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/XMLFile.js#L92)  
> Since: 3.0.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

This method is called automatically, only once, when the Scene is first created.

Do not invoke it directly.

**Access:** private

> Source: [src/loader/LoaderPlugin.js#L372](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L372)  
> Since: 3.5.1

---

## checkLoadQueue

### <instance> checkLoadQueue()

**Description:**

An internal method called by the Loader.

It will check to see if there are any more files in the pending list that need loading, and if so it will move

them from the list Set into the inflight Set, set their CORs flag and start them loading.

It will carrying on doing this for each file in the pending list until it runs out, or hits the max allowed parallel downloads.

**Access:** private

> Source: [src/loader/LoaderPlugin.js#L979](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L979)  
> Since: 3.7.0

---

## destroy

### <instance> destroy()

**Description:**

The Scene that owns this plugin is being destroyed.

We need to shutdown and then kill off all external references.

**Access:** private

**Overrides:** Phaser.Events.EventEmitter#destroy

> Source: [src/loader/LoaderPlugin.js#L1269](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L1269)  
> Since: 3.0.0

---

## pluginStart

### <instance> pluginStart()

**Description:**

This method is called automatically by the Scene when it is starting up.

It is responsible for creating local systems, properties and listening for Scene events.

Do not invoke it directly.

**Access:** private

> Source: [src/loader/LoaderPlugin.js#L385](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L385)  
> Since: 3.5.1

---

## shutdown

### <instance> shutdown()

**Description:**

The Scene that owns this plugin is shutting down.

We need to kill and reset all internal properties as well as stop listening to Scene events.

**Access:** private

**Overrides:** Phaser.Events.EventEmitter#shutdown

> Source: [src/loader/LoaderPlugin.js#L1249](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L1249)  
> Since: 3.0.0

---

# Public Members

## baseURL

### baseURL: string

**Description:**

If you want to append a URL before the path of any asset you can set this here.

Useful if allowing the asset base url to be configured outside of the game code.

If you set this property directly then it *must* end with a "/". Alternatively, call `setBaseURL()` and it'll do it for you.

> Source: [src/loader/LoaderPlugin.js#L154](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L154)  
> Since: 3.0.0

---

## cacheManager

### cacheManager: [Phaser.Cache.CacheManager](cache-cachemanager.md)

**Description:**

A reference to the global Cache Manager.

> Source: [src/loader/LoaderPlugin.js#L85](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L85)  
> Since: 3.7.0

---

## crossOrigin

### crossOrigin: string

**Description:**

The crossOrigin value applied to loaded images. Very often this needs to be set to 'anonymous'.

> Source: [src/loader/LoaderPlugin.js#L203](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L203)  
> Since: 3.0.0

---

## imageLoadType

### imageLoadType: string

**Description:**

Optional load type for image files. `XHR` is the default. Set to `HTMLImageElement` to load images using the Image tag instead.

> Source: [src/loader/LoaderPlugin.js#L212](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L212)  
> Since: 3.60.0

---

## inflight

### inflight: Phaser.Structs.Set.<Phaser.Loader.File>

**Description:**

Files are stored in this Set while they're in the process of being loaded.

Upon a successful load they are moved to the `queue` Set.

By the end of the load process this Set will be empty.

> Source: [src/loader/LoaderPlugin.js#L270](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L270)  
> Since: 3.0.0

---

## list

### list: Phaser.Structs.Set.<Phaser.Loader.File>

**Description:**

Files are placed in this Set when they're added to the Loader via `addFile`.

They are moved to the `inflight` Set when they start loading, and assuming a successful

load, to the `queue` Set for further processing.

By the end of the load process this Set will be empty.

> Source: [src/loader/LoaderPlugin.js#L256](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L256)  
> Since: 3.0.0

---

## localSchemes

### localSchemes: Array.<string>

**Description:**

An array of all schemes that the Loader considers as being 'local'.

This is populated by the `Phaser.Core.Config#loaderLocalScheme` game configuration setting and defaults to

`[ 'file://', 'capacitor://' ]`. Additional local schemes can be added to this array as needed.

> Source: [src/loader/LoaderPlugin.js#L221](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L221)  
> Since: 3.60.0

---

## maxParallelDownloads

### maxParallelDownloads: number

**Description:**

The number of concurrent / parallel resources to try and fetch at once.

Old browsers limit 6 requests per domain; modern ones, especially those with HTTP/2 don't limit it at all.

The default is 32 but you can change this in your Game Config, or by changing this property before the Loader starts.

> Source: [src/loader/LoaderPlugin.js#L174](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L174)  
> Since: 3.0.0

---

## maxRetries

### maxRetries: number

**Description:**

The number of times to retry loading a single file before it fails.

This property is read by the `File` object when it is created and set to

the internal property of the same name. It's not used by the Loader itself.

You can set this value via the Game Config, or you can adjust this property

at any point after the Loader has started. However, it will not apply to files

that have already been added to the Loader, only those added after this value

is changed.

> Source: [src/loader/LoaderPlugin.js#L350](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L350)  
> Since: 3.85.0

---

## path

### path: string

**Description:**

The value of `path`, if set, is placed before any *relative* file path given. For example:

```
Copy
this.load.path = "images/sprites/";

this.load.image("ball", "ball.png");

this.load.image("tree", "level1/oaktree.png");

this.load.image("boom", "[http://server.com/explode.png](http://server.com/explode.png)");


```

Would load the `ball` file from `images/sprites/ball.png` and the tree from

`images/sprites/level1/oaktree.png` but the file `boom` would load from the URL

given as it's an absolute URL.

Please note that the path is added before the filename but *after* the baseURL (if set.)

If you set this property directly then it *must* end with a "/". Alternatively, call `setPath()` and it'll do it for you.

> Source: [src/loader/LoaderPlugin.js#L129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L129)  
> Since: 3.0.0

---

## prefix

### prefix: string

**Description:**

An optional prefix that is automatically prepended to the start of every file key.

If prefix was `MENU.` and you load an image with the key 'Background' the resulting key would be `MENU.Background`.

You can set this directly, or call `Loader.setPrefix()`. It will then affect every file added to the Loader

from that point on. It does *not* change any file already in the load queue.

> Source: [src/loader/LoaderPlugin.js#L116](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L116)  
> Since: 3.7.0

---

## progress

### progress: number

**Description:**

The progress of the current load queue, as a float value between 0 and 1.

This is updated automatically as files complete loading.

Note that it is possible for this value to go down again if you add content to the current load queue during a load.

> Source: [src/loader/LoaderPlugin.js#L244](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L244)  
> Since: 3.0.0

---

## queue

### queue: Phaser.Structs.Set.<Phaser.Loader.File>

**Description:**

Files are stored in this Set while they're being processed.

If the process is successful they are moved to their final destination, which could be

a Cache or the Texture Manager.

At the end of the load process this Set will be empty.

> Source: [src/loader/LoaderPlugin.js#L283](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L283)  
> Since: 3.0.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

The Scene which owns this Loader instance.

> Source: [src/loader/LoaderPlugin.js#L67](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L67)  
> Since: 3.0.0

---

## sceneManager

### sceneManager: [Phaser.Scenes.SceneManager](scenes-scenemanager.md)

**Description:**

A reference to the global Scene Manager.

**Access:** protected

> Source: [src/loader/LoaderPlugin.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L103)  
> Since: 3.16.0

---

## state

### state: number

**Description:**

The current state of the Loader.

> Source: [src/loader/LoaderPlugin.js#L330](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L330)  
> Since: 3.0.0

---

## systems

### systems: [Phaser.Scenes.Systems](scenes-systems.md)

**Description:**

A reference to the Scene Systems.

> Source: [src/loader/LoaderPlugin.js#L76](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L76)  
> Since: 3.0.0

---

## textureManager

### textureManager: [Phaser.Textures.TextureManager](textures-texturemanager.md)

**Description:**

A reference to the global Texture Manager.

> Source: [src/loader/LoaderPlugin.js#L94](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L94)  
> Since: 3.7.0

---

## totalComplete

### totalComplete: number

**Description:**

The total number of files that successfully loaded during the most recent load.

This value is reset when you call `Loader.start`.

> Source: [src/loader/LoaderPlugin.js#L319](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L319)  
> Since: 3.7.0

---

## totalFailed

### totalFailed: number

**Description:**

The total number of files that failed to load during the most recent load.

This value is reset when you call `Loader.start`.

> Source: [src/loader/LoaderPlugin.js#L308](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L308)  
> Since: 3.7.0

---

## totalToLoad

### totalToLoad: number

**Description:**

The total number of files to load. It may not always be accurate because you may add to the Loader during the process

of loading, especially if you load a Pack File. Therefore this value can change, but in most cases remains static.

> Source: [src/loader/LoaderPlugin.js#L233](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L233)  
> Since: 3.0.0

---

## xhr

### xhr: [Phaser.Types.Loader.XHRSettingsObject](../typedef/types-loader.md)

**Description:**

xhr specific global settings (can be overridden on a per-file basis)

> Source: [src/loader/LoaderPlugin.js#L187](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L187)  
> Since: 3.0.0

---

# Private Members

## \_deleteQueue

### \_deleteQueue: Phaser.Structs.Set.<Phaser.Loader.File>

**Description:**

A temporary Set in which files are stored after processing,

awaiting destruction at the end of the load process.

**Access:** private

> Source: [src/loader/LoaderPlugin.js#L297](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L297)  
> Since: 3.7.0

---

## multiKeyIndex

### multiKeyIndex: number

**Description:**

The current index being used by multi-file loaders to avoid key clashes.

**Access:** private

> Source: [src/loader/LoaderPlugin.js#L340](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/LoaderPlugin.js#L340)  
> Since: 3.20.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Methods](#public-methods)

  + [addFile](#addfile)

    - [<instance> addFile(file)](#instance-addfilefile)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addPack](#addpack)

    - [<instance> addPack(pack, [packKey])](#instance-addpackpack-packkey)
  + [animation](#animation)

    - [<instance> animation(key, [url], [dataKey], [xhrSettings])](#instance-animationkey-url-datakey-xhrsettings)
  + [aseprite](#aseprite)

    - [<instance> aseprite(key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings])](#instance-asepritekey-textureurl-atlasurl-texturexhrsettings-atlasxhrsettings)
  + [atlas](#atlas)

    - [<instance> atlas(key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings])](#instance-atlaskey-textureurl-atlasurl-texturexhrsettings-atlasxhrsettings)
  + [atlasXML](#atlasxml)

    - [<instance> atlasXML(key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings])](#instance-atlasxmlkey-textureurl-atlasurl-texturexhrsettings-atlasxhrsettings)
  + [audio](#audio)

    - [<instance> audio(key, [urls], [config], [xhrSettings])](#instance-audiokey-urls-config-xhrsettings)
  + [audioSprite](#audiosprite)

    - [<instance> audioSprite(key, jsonURL, [audioURL], [audioConfig], [audioXhrSettings], [jsonXhrSettings])](#instance-audiospritekey-jsonurl-audiourl-audioconfig-audioxhrsettings-jsonxhrsettings)
  + [binary](#binary)

    - [<instance> binary(key, [url], [dataType], [xhrSettings])](#instance-binarykey-url-datatype-xhrsettings)
  + [bitmapFont](#bitmapfont)

    - [<instance> bitmapFont(key, [textureURL], [fontDataURL], [textureXhrSettings], [fontDataXhrSettings])](#instance-bitmapfontkey-textureurl-fontdataurl-texturexhrsettings-fontdataxhrsettings)
  + [css](#css)

    - [<instance> css(key, [url], [xhrSettings])](#instance-csskey-url-xhrsettings)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [fileProcessComplete](#fileprocesscomplete)

    - [<instance> fileProcessComplete(file)](#instance-fileprocesscompletefile)
  + [flagForRemoval](#flagforremoval)

    - [<instance> flagForRemoval(file)](#instance-flagforremovalfile)
  + [font](#font)

    - [<instance> font(key, [url], [format], [descriptors], [xhrSettings])](#instance-fontkey-url-format-descriptors-xhrsettings)
  + [glsl](#glsl)

    - [<instance> glsl(key, [url], [shaderType], [xhrSettings])](#instance-glslkey-url-shadertype-xhrsettings)
  + [html](#html)

    - [<instance> html(key, [url], [xhrSettings])](#instance-htmlkey-url-xhrsettings)
  + [htmlTexture](#htmltexture)

    - [<instance> htmlTexture(key, [url], [width], [height], [xhrSettings])](#instance-htmltexturekey-url-width-height-xhrsettings)
  + [image](#image)

    - [<instance> image(key, [url], [xhrSettings])](#instance-imagekey-url-xhrsettings)
  + [isLoading](#isloading)

    - [<instance> isLoading()](#instance-isloading)
  + [isReady](#isready)

    - [<instance> isReady()](#instance-isready)
  + [json](#json)

    - [<instance> json(key, [url], [dataKey], [xhrSettings])](#instance-jsonkey-url-datakey-xhrsettings)
  + [keyExists](#keyexists)

    - [<instance> keyExists(file)](#instance-keyexistsfile)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [loadComplete](#loadcomplete)

    - [<instance> loadComplete()](#instance-loadcomplete)
  + [multiatlas](#multiatlas)

    - [<instance> multiatlas(key, [atlasURL], [path], [baseURL], [atlasXhrSettings])](#instance-multiatlaskey-atlasurl-path-baseurl-atlasxhrsettings)
  + [nextFile](#nextfile)

    - [<instance> nextFile(file, success)](#instance-nextfilefile-success)
  + [obj](#obj)

    - [<instance> obj(key, [objURL], [matURL], [flipUV], [xhrSettings])](#instance-objkey-objurl-maturl-flipuv-xhrsettings)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [pack](#pack)

    - [<instance> pack(key, [url], [dataKey], [xhrSettings])](#instance-packkey-url-datakey-xhrsettings)
  + [plugin](#plugin)

    - [<instance> plugin(key, [url], [start], [mapping], [xhrSettings])](#instance-pluginkey-url-start-mapping-xhrsettings)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [removePack](#removepack)

    - [<instance> removePack(packKey, [dataKey])](#instance-removepackpackkey-datakey)
  + [reset](#reset)

    - [<instance> reset()](#instance-reset)
  + [save](#save)

    - [<instance> save(data, [filename], [filetype])](#instance-savedata-filename-filetype)
  + [saveJSON](#savejson)

    - [<instance> saveJSON(data, [filename])](#instance-savejsondata-filename)
  + [sceneFile](#scenefile)

    - [<instance> sceneFile(key, [url], [xhrSettings])](#instance-scenefilekey-url-xhrsettings)
  + [scenePlugin](#sceneplugin)

    - [<instance> scenePlugin(key, [url], [systemKey], [sceneKey], [xhrSettings])](#instance-scenepluginkey-url-systemkey-scenekey-xhrsettings)
  + [script](#script)

    - [<instance> script(key, [url], [type], [xhrSettings])](#instance-scriptkey-url-type-xhrsettings)
  + [scripts](#scripts)

    - [<instance> scripts(key, [url], [extension], [xhrSettings])](#instance-scriptskey-url-extension-xhrsettings)
  + [setBaseURL](#setbaseurl)

    - [<instance> setBaseURL([url])](#instance-setbaseurlurl)
  + [setCORS](#setcors)

    - [<instance> setCORS([crossOrigin])](#instance-setcorscrossorigin)
  + [setPath](#setpath)

    - [<instance> setPath([path])](#instance-setpathpath)
  + [setPrefix](#setprefix)

    - [<instance> setPrefix([prefix])](#instance-setprefixprefix)
  + [spritesheet](#spritesheet)

    - [<instance> spritesheet(key, [url], [frameConfig], [xhrSettings])](#instance-spritesheetkey-url-frameconfig-xhrsettings)
  + [start](#start)

    - [<instance> start()](#instance-start)
  + [svg](#svg)

    - [<instance> svg(key, [url], [svgConfig], [xhrSettings])](#instance-svgkey-url-svgconfig-xhrsettings)
  + [text](#text)

    - [<instance> text(key, [url], [xhrSettings])](#instance-textkey-url-xhrsettings)
  + [texture](#texture)

    - [<instance> texture(key, [url], [xhrSettings])](#instance-texturekey-url-xhrsettings)
  + [tilemapCSV](#tilemapcsv)

    - [<instance> tilemapCSV(key, [url], [xhrSettings])](#instance-tilemapcsvkey-url-xhrsettings)
  + [tilemapImpact](#tilemapimpact)

    - [<instance> tilemapImpact(key, [url], [xhrSettings])](#instance-tilemapimpactkey-url-xhrsettings)
  + [tilemapTiledJSON](#tilemaptiledjson)

    - [<instance> tilemapTiledJSON(key, [url], [xhrSettings])](#instance-tilemaptiledjsonkey-url-xhrsettings)
  + [unityAtlas](#unityatlas)

    - [<instance> unityAtlas(key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings])](#instance-unityatlaskey-textureurl-atlasurl-texturexhrsettings-atlasxhrsettings)
  + [update](#update)

    - [<instance> update()](#instance-update)
  + [updateProgress](#updateprogress)

    - [<instance> updateProgress()](#instance-updateprogress)
  + [video](#video)

    - [<instance> video(key, [urls], [noAudio])](#instance-videokey-urls-noaudio)
  + [xml](#xml)

    - [<instance> xml(key, [url], [xhrSettings])](#instance-xmlkey-url-xhrsettings)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [checkLoadQueue](#checkloadqueue)

    - [<instance> checkLoadQueue()](#instance-checkloadqueue)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [pluginStart](#pluginstart)

    - [<instance> pluginStart()](#instance-pluginstart)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
* [Public Members](#public-members)

  + [baseURL](#baseurl)

    - [baseURL: string](#baseurl-string)
  + [cacheManager](#cachemanager)

    - [cacheManager: Phaser.Cache.CacheManager](#cachemanager-phasercachecachemanager)
  + [crossOrigin](#crossorigin)

    - [crossOrigin: string](#crossorigin-string)
  + [imageLoadType](#imageloadtype)

    - [imageLoadType: string](#imageloadtype-string)
  + [inflight](#inflight)

    - [inflight: Phaser.Structs.Set.<Phaser.Loader.File>](#inflight-phaserstructssetphaserloaderfile)
  + [list](#list)

    - [list: Phaser.Structs.Set.<Phaser.Loader.File>](#list-phaserstructssetphaserloaderfile)
  + [localSchemes](#localschemes)

    - [localSchemes: Array.<string>](#localschemes-arraystring)
  + [maxParallelDownloads](#maxparalleldownloads)

    - [maxParallelDownloads: number](#maxparalleldownloads-number)
  + [maxRetries](#maxretries)

    - [maxRetries: number](#maxretries-number)
  + [path](#path)

    - [path: string](#path-string)
  + [prefix](#prefix)

    - [prefix: string](#prefix-string)
  + [progress](#progress)

    - [progress: number](#progress-number)
  + [queue](#queue)

    - [queue: Phaser.Structs.Set.<Phaser.Loader.File>](#queue-phaserstructssetphaserloaderfile)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [sceneManager](#scenemanager)

    - [sceneManager: Phaser.Scenes.SceneManager](#scenemanager-phaserscenesscenemanager)
  + [state](#state)

    - [state: number](#state-number)
  + [systems](#systems)

    - [systems: Phaser.Scenes.Systems](#systems-phaserscenessystems)
  + [textureManager](#texturemanager)

    - [textureManager: Phaser.Textures.TextureManager](#texturemanager-phasertexturestexturemanager)
  + [totalComplete](#totalcomplete)

    - [totalComplete: number](#totalcomplete-number)
  + [totalFailed](#totalfailed)

    - [totalFailed: number](#totalfailed-number)
  + [totalToLoad](#totaltoload)

    - [totalToLoad: number](#totaltoload-number)
  + [xhr](#xhr)

    - [xhr: Phaser.Types.Loader.XHRSettingsObject](#xhr-phasertypesloaderxhrsettingsobject)
* [Private Members](#private-members)

  + [\_deleteQueue](#_deletequeue)

    - [\_deleteQueue: Phaser.Structs.Set.<Phaser.Loader.File>](#_deletequeue-phaserstructssetphaserloaderfile)
  + [multiKeyIndex](#multikeyindex)

    - [multiKeyIndex: number](#multikeyindex-number)

Back to top

©2025[Phaser](https://docs.phaser.io)