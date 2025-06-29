# Cache

A Guide to the Phaser Cache to manage game assets and resources

When a file is downloaded by the Loader it nearly always ends up stored in an internal Phaser Cache. There are different caches for different file types. For example, JSON files are stored in the JSON cache, Binary files in the Binary Cache, and so on. These caches are created automatically when the Phaser Game instance first starts up. Files are stored in them using unique string-based keys. If the file has come from the Loader, it will use the same key you used there, to store it in the Cache with.

The Phaser Cache is different to any cache that the browser itself may maintain, in that it only persists for the duration of your game. Once your game has been destroyed, either directly by you, or via a page navigation, the Phaser Cache is cleared. Unlike the browser cache, you are free to add to, and remove items from, any of the Phaser caches at will.

Items stored in a Phaser Cache are global, which means they can be accessed from any Scene in your game. Scene's do not maintain their own set of caches. Instead, they all share the same global set. This is important to understand, because it means that if you load a file in one Scene, it will be available in all other Scenes too.

Mostly, you don't need to worry about interacting with the Phaser Cache. It's primarily an internal system that is used by other systems, such as the Loader, to store and retrieve data. However, there are times when you may want to interact with it directly, and it has a public API for doing exactly this.

## Usage

* Getting cache data

  ```
  Copyvar cache = scene.cache.text;
  var data = cache.get(key);

  ```
* Adding cache data

  ```
  Copyvar cache = scene.cache.text;
  var data = cache.add(key);

  ```
* Removing cache data

  ```
  Copyvar cache = scene.cache.text;
  cache.remove(key);

  ```
* Verifying cache data

  ```
  Copyvar cache = scene.cache.text;
  var hasData = cache.exists(key);
  // var hasData = cache.has(key);

  ```

## Events

* Adding an item

  ```
  Copycache.events.on("add", function (cache, key, item) {});

  ```
* Removing an item

  ```
  Copycache.events.on("remove", function (cache, key, item) {});

  ```

Updated on June 4, 2025, 1:16 PM UTC

---

[Loader](../loader.md)

[Math](../math.md)

On this page

* [Cache](#cache)

  + [Usage](#usage)
  + [Events](#events)

Back to top

©2025[Phaser](../../../index.md)