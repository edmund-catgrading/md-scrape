# FacebookInstantGamesPlugin

Phaser.FacebookInstantGamesPlugin

The Facebook Instant Games Plugin for Phaser 3 provides a seamless bridge between Phaser

and the Facebook Instant Games API version 6.2.

You can access this plugin via the `facebook` property in a Scene, i.e:

```
Copy
this.facebook.getPlatform();


```

If this is unavailable please check to make sure you're using a build of Phaser that has

this plugin within it. You can quickly check this by looking at the dev tools console

header - the Phaser version number will have `-FB` after it if this plugin is loaded.

If you are building your own version of Phaser then use this Webpack DefinePlugin flag:

`"typeof PLUGIN_FBINSTANT": JSON.stringify(true)`

You will find that every Instant Games API method has a mapping in this plugin.

For a full list please consult either the plugin documentation, or the 6.2 SDK documentation

at <https://developers.facebook.com/docs/games/instant-games/sdk/fbinstant6.2>

Internally this plugin uses its own Data Manager to handle seamless user data updates and provides

handy functions for advertisement displaying, opening share dialogs, logging, leaderboards, purchase API requests,

loader integration and more.

To get started with Facebook Instant Games you will need to register on Facebook and create a new Instant

Game app that has its own unique app ID. Facebook have also provided a dashboard interface for setting up

various features for your game, including leaderboards, ad requests and the payments API. There are lots

of guides on the Facebook Developers portal to assist with setting these

various systems up: <https://developers.facebook.com/docs/games/instant-games/guides>

For more details follow the Quick Start guide here: <https://developers.facebook.com/docs/games/instant-games>

**Constructor**

`new FacebookInstantGamesPlugin(game)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](game.md) | No | A reference to the Phaser.Game instance. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](events-eventemitter.md)

> Source: [src/FacebookInstantGamesPlugin.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L17)  
> Since: 3.13.0

# Public Members

## ads

### ads: Array.<AdInstance>

**Description:**

Contains AdInstance objects, as created by the `preloadAds()` method.

> Source: [src/FacebookInstantGamesPlugin.js#L287](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L287)  
> Since: 3.13.0

---

## catalog

### catalog: Array.<Product>

**Description:**

The set of products that are registered to the game.

> Source: [src/FacebookInstantGamesPlugin.js#L258](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L258)  
> Since: 3.13.0

---

## contextID

### contextID: string

**Description:**

A unique identifier for the current game context. This represents a specific context

that the game is being played in (for example, a particular messenger conversation or facebook post).

The identifier will be null if game is being played in a solo context.

This value is populated automatically during boot.

> Source: [src/FacebookInstantGamesPlugin.js#L146](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L146)  
> Since: 3.13.0

---

## contextType

### contextType: string

**Description:**

The current context in which your game is running. This can be either `null` or

one of:

`POST` - The game is running inside of a Facebook post.

`THREAD` - The game is running inside a Facebook Messenger thread.

`GROUP` - The game is running inside a Facebook Group.

`SOLO` - This is the default context, the player is the only participant.

This value is populated automatically during boot.

> Source: [src/FacebookInstantGamesPlugin.js#L158](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L158)  
> Since: 3.13.0

---

## data

### data: [Phaser.Data.DataManager](data-datamanager.md)

**Description:**

A Data Manager instance.

It allows you to store, query and retrieve any key/value data you may need to store.

It's also used internally by the plugin to store FBIG API data.

> Source: [src/FacebookInstantGamesPlugin.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L80)  
> Since: 3.13.0

---

## dataLocked

### dataLocked: boolean

**Description:**

Is the Data Manager currently locked?

> Source: [src/FacebookInstantGamesPlugin.js#L104](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L104)  
> Since: 3.13.0

---

## entryPoint

### entryPoint: string

**Description:**

Holds the entry point that the game was launched from.

This value is populated automatically during boot.

> Source: [src/FacebookInstantGamesPlugin.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L124)  
> Since: 3.13.0

---

## entryPointData

### entryPointData: any

**Description:**

An object that contains any data associated with the entry point that the game was launched from.

The contents of the object are developer-defined, and can occur from entry points on different platforms.

This will return null for older mobile clients, as well as when there is no data associated with the particular entry point.

This value is populated automatically during boot.

> Source: [src/FacebookInstantGamesPlugin.js#L134](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L134)  
> Since: 3.13.0

---

## game

### game: [Phaser.Game](game.md)

**Description:**

A reference to the Phaser.Game instance.

> Source: [src/FacebookInstantGamesPlugin.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L70)  
> Since: 3.13.0

---

## hasLoaded

### hasLoaded: boolean

**Description:**

Has the Facebook Instant Games API loaded yet?

This is set automatically during the boot process.

> Source: [src/FacebookInstantGamesPlugin.js#L94](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L94)  
> Since: 3.13.0

---

## leaderboards

### leaderboards: Array.<[Phaser.FacebookInstantGamesLeaderboard](facebookinstantgamesleaderboard.md)>

**Description:**

Contains all of the leaderboard data, as populated by the `getLeaderboard()` method.

> Source: [src/FacebookInstantGamesPlugin.js#L278](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L278)  
> Since: 3.13.0

---

## locale

### locale: string

**Description:**

The current locale.

See <https://origincache.facebook.com/developers/resources/?id=FacebookLocales.xml> for a complete list of supported locale values.

Use this to determine what languages the current game should be localized with.

This value is populated automatically during boot.

> Source: [src/FacebookInstantGamesPlugin.js#L175](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L175)  
> Since: 3.13.0

---

## paymentsReady

### paymentsReady: boolean

**Description:**

Does the current platform and context allow for use of the payments API?

Currently this is only available on Facebook.com and Android 6+.

> Source: [src/FacebookInstantGamesPlugin.js#L248](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L248)  
> Since: 3.13.0

---

## platform

### platform: string

**Description:**

The platform on which the game is currently running, i.e. `IOS`.

This value is populated automatically during boot.

> Source: [src/FacebookInstantGamesPlugin.js#L187](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L187)  
> Since: 3.13.0

---

## playerCanSubscribeBot

### playerCanSubscribeBot: boolean

**Description:**

Whether a player can subscribe to the game bot or not.

> Source: [src/FacebookInstantGamesPlugin.js#L239](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L239)  
> Since: 3.13.0

---

## playerID

### playerID: string

**Description:**

Holds the id of the player. This is a string based ID, the same as `FBInstant.player.getID()`.

This value is populated automatically during boot if the API is supported.

> Source: [src/FacebookInstantGamesPlugin.js#L207](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L207)  
> Since: 3.13.0

---

## playerName

### playerName: string

**Description:**

The player's localized display name.

This value is populated automatically during boot if the API is supported.

> Source: [src/FacebookInstantGamesPlugin.js#L217](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L217)  
> Since: 3.13.0

---

## playerPhotoURL

### playerPhotoURL: string

**Description:**

A url to the player's public profile photo. The photo will always be a square, and with dimensions

of at least 200x200. When rendering it in the game, the exact dimensions should never be assumed to be constant.

It's recommended to always scale the image to a desired size before rendering.

This value is populated automatically during boot if the API is supported.

> Source: [src/FacebookInstantGamesPlugin.js#L227](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L227)  
> Since: 3.13.0

---

## purchases

### purchases: Array.<Purchase>

**Description:**

Contains all of the player's unconsumed purchases.

The game must fetch the current player's purchases as soon as the client indicates that it is ready to perform payments-related operations,

i.e. at game start. The game can then process and consume any purchases that are waiting to be consumed.

> Source: [src/FacebookInstantGamesPlugin.js#L267](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L267)  
> Since: 3.13.0

---

## supportedAPIs

### supportedAPIs: Array.<string>

**Description:**

A list of the Facebook Instant Games APIs that are available,

based on the given platform, context and user privacy settings.

This value is populated automatically during boot.

> Source: [src/FacebookInstantGamesPlugin.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L113)  
> Since: 3.13.0

---

## version

### version: string

**Description:**

The string representation of the Facebook Instant Games SDK version being used.

This value is populated automatically during boot.

> Source: [src/FacebookInstantGamesPlugin.js#L197](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L197)  
> Since: 3.13.0

---

# Public Methods

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

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## canSubscribeBot

### <instance> canSubscribeBot()

**Description:**

Checks if the current player can subscribe to the game bot.

It makes an async call to the API, so the result isn't available immediately.

If they can subscribe, the `playerCanSubscribeBot` property is set to `true`

and this plugin will emit the `cansubscribebot` event.

If they cannot, i.e. it's not in the list of supported APIs, or the request

was rejected, it will emit a `cansubscribebotfail` event instead.

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L723](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L723)  
> Since: 3.13.0

---

## checkAPI

### <instance> checkAPI(api)

**Description:**

Checks to see if a given Facebook Instant Games API is available or not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| api | string | No | The API to check for, i.e. `player.getID`. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the API is supported, otherwise `false`.

> Source: [src/FacebookInstantGamesPlugin.js#L494](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L494)  
> Since: 3.13.0

---

## chooseContext

### <instance> chooseContext([options])

**Description:**

Opens a context selection dialog for the player. If the player selects an available context,

the client will attempt to switch into that context, and emit the `choose` event if successful.

Otherwise, if the player exits the menu or the client fails to switch into the new context, the `choosefail` event will be emitted.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| options | ChooseContextConfig | Yes | An object specifying conditions on the contexts that should be offered. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1351](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1351)  
> Since: 3.13.0

---

## consumePurchase

### <instance> consumePurchase(purchaseToken)

**Description:**

Consumes a specific purchase belonging to the current player. Before provisioning a product's effects to the player,

the game should request the consumption of the purchased product. Once the purchase is successfully consumed,

the game should immediately provide the player with the effects of their purchase.

It makes an async call to the API, so the result isn't available immediately.

If they are successfully subscribed this plugin will emit the `consumepurchase` event along

with the purchase data.

If they cannot, i.e. it's not in the list of supported APIs, or the request

was rejected, it will emit a `consumepurchasefail` event instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| purchaseToken | string | No | The purchase token of the purchase that should be consumed. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1626](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1626)  
> Since: 3.17.0

---

## createContext

### <instance> createContext(playerID)

**Description:**

Attempts to create or switch into a context between a specified player and the current player.

This plugin will emit the `create` event once the context switch is completed.

If the API call fails, such as if the player listed is not a Connected Player of the current player or if the

player does not provide permission to enter the new context, then the plugin will emit a 'createfail' event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| playerID | string | No | ID of the player. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1385](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1385)  
> Since: 3.13.0

---

## createShortcut

### <instance> createShortcut()

**Description:**

Prompts the user to create a shortcut to the game if they are eligible to.

Can only be called once per session.

It makes an async call to the API, so the result isn't available immediately.

If the user choose to create a shortcut this plugin will emit the `shortcutcreated` event.

If they cannot, i.e. it's not in the list of supported APIs, or the request

was rejected, it will emit a `shortcutcreatedfail` event instead.

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1856](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1856)  
> Since: 3.13.0

---

## destroy

### <instance> destroy()

**Description:**

Quits the Facebook API and then destroys this plugin.

**Overrides:** Phaser.Events.EventEmitter#destroy

> Source: [src/FacebookInstantGamesPlugin.js#L2290](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L2290)  
> Since: 3.13.0

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

## flushData

### <instance> flushData()

**Description:**

Immediately flushes any changes to the player data to the designated cloud storage.

This function is expensive, and should primarily be used for critical changes where persistence needs to be immediate

and known by the game. Non-critical changes should rely on the platform to persist them in the background.

NOTE: Calls to player.setDataAsync will be rejected while this function's result is pending.

Data managed via this plugins Data Manager instance is automatically synced with Facebook. However, you can call this

method directly if you need to flush the data directly.

When the APIs `flushDataAsync` call resolves it will emit the `flushdata` event from this plugin. If the call fails for some

reason it will emit `flushdatafail` instead.

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L891](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L891)  
> Since: 3.13.0

---

## gameStarted

### <instance> gameStarted()

**Description:**

This method is called automatically when the game has finished loading,

if you used the `showLoadProgress` method. If your game doesn't need to

load any assets, or you're managing the load yourself, then call this

method directly to start the API running.

When the API has finished starting this plugin will emit a `startgame` event

which you should listen for.

> Source: [src/FacebookInstantGamesPlugin.js#L398](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L398)  
> Since: 3.13.0

---

## getCatalog

### <instance> getCatalog()

**Description:**

Fetches the game's product catalog.

It makes an async call to the API, so the result isn't available immediately.

If they are successfully subscribed this plugin will emit the `getcatalog` event along

with the catalog data.

If they cannot, i.e. it's not in the list of supported APIs, or the request

was rejected, it will emit a `getcatalogfail` event instead.

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1458](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1458)  
> Since: 3.13.0

---

## getData

### <instance> getData(keys)

**Description:**

Gets the associated data from the player based on the given key, or array of keys.

The data is requested in an async call, so the result isn't available immediately.

When the call completes the data is set into this plugins Data Manager and the

`getdata` event will be emitted.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| keys | string | Array.<string> | No | The key/s of the data to retrieve. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L802](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L802)  
> Since: 3.13.0

---

## getID

### <instance> getID()

**Description:**

Returns the unique identifier for the current game context. This represents a specific context

that the game is being played in (for example, a particular messenger conversation or facebook post).

The identifier will be null if game is being played in a solo context.

It is only populated if `contextGetID` is in the list of supported APIs.

**Returns:** string - The context ID.

> Source: [src/FacebookInstantGamesPlugin.js#L516](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L516)  
> Since: 3.13.0

---

## getLeaderboard

### <instance> getLeaderboard(name)

**Description:**

Fetch a specific leaderboard belonging to this Instant Game.

The data is requested in an async call, so the result isn't available immediately.

When the call completes the `getleaderboard` event will be emitted along with a Leaderboard object instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the leaderboard. Each leaderboard for an Instant Game must have its own distinct name. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L2251](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L2251)  
> Since: 3.13.0

---

## getLocale

### <instance> getLocale()

**Description:**

Returns the current locale.

See <https://origincache.facebook.com/developers/resources/?id=FacebookLocales.xml> for a complete list of supported locale values.

Use this to determine what languages the current game should be localized with.

It is only populated if `getLocale` is in the list of supported APIs.

**Returns:** string - The current locale.

> Source: [src/FacebookInstantGamesPlugin.js#L563](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L563)  
> Since: 3.13.0

---

## getPlatform

### <instance> getPlatform()

**Description:**

Returns the platform on which the game is currently running, i.e. `IOS`.

It is only populated if `getPlatform` is in the list of supported APIs.

**Returns:** string - The current platform.

> Source: [src/FacebookInstantGamesPlugin.js#L584](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L584)  
> Since: 3.13.0

---

## getPlayerID

### <instance> getPlayerID()

**Description:**

Returns the id of the player. This is a string based ID, the same as `FBInstant.player.getID()`.

It is only populated if `playerGetID` is in the list of supported APIs.

**Returns:** string - The player ID.

> Source: [src/FacebookInstantGamesPlugin.js#L622](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L622)  
> Since: 3.13.0

---

## getPlayerName

### <instance> getPlayerName()

**Description:**

Returns the player's localized display name.

It is only populated if `playerGetName` is in the list of supported APIs.

**Returns:** string - The player's localized display name.

> Source: [src/FacebookInstantGamesPlugin.js#L641](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L641)  
> Since: 3.13.0

---

## getPlayerPhotoURL

### <instance> getPlayerPhotoURL()

**Description:**

Returns the url to the player's public profile photo. The photo will always be a square, and with dimensions

of at least 200x200. When rendering it in the game, the exact dimensions should never be assumed to be constant.

It's recommended to always scale the image to a desired size before rendering.

It is only populated if `playerGetPhoto` is in the list of supported APIs.

**Returns:** string - The player's photo url.

> Source: [src/FacebookInstantGamesPlugin.js#L660](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L660)  
> Since: 3.13.0

---

## getPlayers

### <instance> getPlayers()

**Description:**

Fetches an array of ConnectedPlayer objects containing information about active players

(people who played the game in the last 90 days) that are connected to the current player.

It makes an async call to the API, so the result isn't available immediately.

If they are successfully subscribed this plugin will emit the `players` event along

with the player data.

If they cannot, i.e. it's not in the list of supported APIs, or the request

was rejected, it will emit a `playersfail` event instead.

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1420](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1420)  
> Since: 3.13.0

---

## getProduct

### <instance> getProduct(productID)

**Description:**

Fetches a single Product from the game's product catalog.

The product catalog must have been populated using `getCatalog` prior to calling this method.

Use this to look-up product details based on a purchase list.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| productID | string | No | The Product ID of the item to get from the catalog. |
| --- | --- | --- | --- |

**Returns:** Product - The Product from the catalog, or `null` if it couldn't be found or the catalog isn't populated.

> Source: [src/FacebookInstantGamesPlugin.js#L1503](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1503)  
> Since: 3.17.0

---

## getPurchases

### <instance> getPurchases()

**Description:**

Fetches all of the player's unconsumed purchases. The game must fetch the current player's purchases

as soon as the client indicates that it is ready to perform payments-related operations,

i.e. at game start. The game can then process and consume any purchases that are waiting to be consumed.

It makes an async call to the API, so the result isn't available immediately.

If they are successfully subscribed this plugin will emit the `getpurchases` event along

with the purchase data.

If they cannot, i.e. it's not in the list of supported APIs, or the request

was rejected, it will emit a `getpurchasesfail` event instead.

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1579](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1579)  
> Since: 3.13.0

---

## getSDKVersion

### <instance> getSDKVersion()

**Description:**

Returns the string representation of the Facebook Instant Games SDK version being used.

It is only populated if `getSDKVersion` is in the list of supported APIs.

**Returns:** string - The sdk version.

> Source: [src/FacebookInstantGamesPlugin.js#L603](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L603)  
> Since: 3.13.0

---

## getStats

### <instance> getStats([keys])

**Description:**

Retrieve stats from the designated cloud storage of the current player.

The data is requested in an async call, so the result isn't available immediately.

When the call completes the `getstats` event will be emitted along with the data object returned.

If the call fails, i.e. it's not in the list of supported APIs, or the request was rejected,

it will emit a `getstatsfail` event instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| keys | Array.<string> | Yes | An optional array of unique keys to retrieve stats for. If the function is called without it, it will fetch all stats. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L929](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L929)  
> Since: 3.13.0

---

## getType

### <instance> getType()

**Description:**

Returns the current context in which your game is running. This can be either `null` or one of:

`POST` - The game is running inside of a Facebook post.

`THREAD` - The game is running inside a Facebook Messenger thread.

`GROUP` - The game is running inside a Facebook Group.

`SOLO` - This is the default context, the player is the only participant.

It is only populated if `contextGetType` is in the list of supported APIs.

**Returns:** string - The context type.

> Source: [src/FacebookInstantGamesPlugin.js#L538](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L538)  
> Since: 3.13.0

---

## incStats

### <instance> incStats(data)

**Description:**

Increment the stats of the current player and save them to the designated cloud storage.

Stats in the Facebook Instant Games API are purely numerical values paired with a string-based key. Only numbers can be saved as stats,

all other data types will be ignored.

The data object provided for this call should contain offsets for how much to modify the stats by:

```
Copy
this.facebook.incStats({

    level: 1,

    zombiesSlain: 17,

    rank: -1

});


```

The data is requested in an async call, so the result isn't available immediately.

When the call completes the `incstats` event will be emitted along with the data object returned.

If the call fails, i.e. it's not in the list of supported APIs, or the request was rejected,

it will emit a `incstatsfail` event instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | object | No | An object containing a set of key-value pairs indicating how much to increment each stat in cloud storage. Note that only numerical values are processed. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1018](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1018)  
> Since: 3.13.0

---

## isSizeBetween

### <instance> isSizeBetween([min], [max])

**Description:**

This function determines whether the number of participants in the current game context is between a given minimum and maximum, inclusive.

If one of the bounds is null only the other bound will be checked against.

It will always return the original result for the first call made in a context in a given game play session.

Subsequent calls, regardless of arguments, will return the answer to the original query until a context change occurs and the query result is reset.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| min | integer | Yes | The minimum bound of the context size query. |
| --- | --- | --- | --- |
| max | integer | Yes | The maximum bound of the context size query. |

**Returns:** object - The Context Size Response object in the format: `{answer: boolean, minSize: number?, maxSize: number?}`.

> Source: [src/FacebookInstantGamesPlugin.js#L1269](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1269)  
> Since: 3.13.0

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

## loadPlayerPhoto

### <instance> loadPlayerPhoto(scene, key)

**Description:**

Load the player's photo and store it in the Texture Manager, ready for use in-game.

This method works by using a Scene Loader instance and then asking the Loader to

retrieve the image.

When complete the plugin will emit a `photocomplete` event, along with the key of the photo.

```
Copy
this.facebook.loadPlayerPhoto(this, 'player').once('photocomplete', function (key) {

  this.add.image(x, y, 'player');

}, this);


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene that will be responsible for loading this photo. |
| --- | --- | --- | --- |
| key | string | No | The key to use when storing the photo in the Texture Manager. |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L681](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L681)  
> Since: 3.13.0

---

## log

### <instance> log(name, [value], [params])

**Description:**

Log an app event with FB Analytics.

See <https://developers.facebook.com/docs/javascript/reference/v2.8#app_events> for more details about FB Analytics.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | Name of the event. Must be 2 to 40 characters, and can only contain '\_', '-', ' ', and alphanumeric characters. |
| --- | --- | --- | --- |
| value | number | Yes | An optional numeric value that FB Analytics can calculate a sum with. |
| params | object | Yes | An optional object that can contain up to 25 key-value pairs to be logged with the event. Keys must be 2 to 40 characters, and can only contain '\_', '-', ' ', and alphanumeric characters. Values must be less than 100 characters in length. |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1905](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1905)  
> Since: 3.13.0

---

## matchPlayer

### <instance> matchPlayer([matchTag], [switchImmediately])

**Description:**

Attempts to match the current player with other users looking for people to play with.

If successful, a new Messenger group thread will be created containing the matched players and the player will

be context switched to that thread. This plugin will also dispatch the `matchplayer` event, containing the new context ID and Type.

The default minimum and maximum number of players in one matched thread are 2 and 20 respectively,

depending on how many players are trying to get matched around the same time.

The values can be changed in `fbapp-config.json`. See the Bundle Config documentation for documentation about `fbapp-config.json`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| matchTag | string | Yes |  | Optional extra information about the player used to group them with similar players. Players will only be grouped with other players with exactly the same tag. The tag must only include letters, numbers, and underscores and be 100 characters or less in length. |
| --- | --- | --- | --- | --- |
| switchImmediately | boolean | Yes | false | Optional extra parameter that specifies whether the player should be immediately switched to the new context when a match is found. By default this will be false which will mean the player needs explicitly press play after being matched to switch to the new context. |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L2210](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L2210)  
> Since: 3.13.0

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

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - `this`.

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

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - `this`.

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

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## openChallenge

### <instance> openChallenge(text, key, [frame], [sessionData])

**Description:**

This invokes a dialog to let the user share specified content, either as a message in Messenger or as a post on the user's timeline.

A blob of data can be attached to the share which every game session launched from the share will be able to access via the `this.entryPointData` property.

This data must be less than or equal to 1000 characters when stringified.

When this method is called you should consider your game paused. Listen out for the `resume` event from this plugin to know when the dialog has been closed.

The user may choose to cancel the share action and close the dialog. The resulting `resume` event will be dispatched regardless if the user actually shared the content or not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| text | string | No | A text message to be shared. |
| --- | --- | --- | --- |
| key | string | No | The key of the texture to use as the share image. |
| frame | string | Yes | The frame of the texture to use as the share image. Set to `null` if you don't require a frame, but do need to set session data. |
| sessionData | object | Yes | A blob of data to attach to the share. |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1192](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1192)  
> Since: 3.13.0

---

## openInvite

### <instance> openInvite(text, key, [frame], [sessionData])

**Description:**

This invokes a dialog to let the user invite a friend to play this game, either as a message in Messenger or as a post on the user's timeline.

A blob of data can be attached to the share which every game session launched from the share will be able to access via the `this.entryPointData` property.

This data must be less than or equal to 1000 characters when stringified.

When this method is called you should consider your game paused. Listen out for the `resume` event from this plugin to know when the dialog has been closed.

The user may choose to cancel the share action and close the dialog. The resulting `resume` event will be dispatched regardless if the user actually shared the content or not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| text | string | No | A text message to be shared. |
| --- | --- | --- | --- |
| key | string | No | The key of the texture to use as the share image. |
| frame | string | Yes | The frame of the texture to use as the share image. Set to `null` if you don't require a frame, but do need to set session data. |
| sessionData | object | Yes | A blob of data to attach to the share. |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1140)  
> Since: 3.13.0

---

## openRequest

### <instance> openRequest(text, key, [frame], [sessionData])

**Description:**

This invokes a dialog to let the user share specified content, either as a message in Messenger or as a post on the user's timeline.

A blob of data can be attached to the share which every game session launched from the share will be able to access via the `this.entryPointData` property.

This data must be less than or equal to 1000 characters when stringified.

When this method is called you should consider your game paused. Listen out for the `resume` event from this plugin to know when the dialog has been closed.

The user may choose to cancel the share action and close the dialog. The resulting `resume` event will be dispatched regardless if the user actually shared the content or not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| text | string | No | A text message to be shared. |
| --- | --- | --- | --- |
| key | string | No | The key of the texture to use as the share image. |
| frame | string | Yes | The frame of the texture to use as the share image. Set to `null` if you don't require a frame, but do need to set session data. |
| sessionData | object | Yes | A blob of data to attach to the share. |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1166](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1166)  
> Since: 3.13.0

---

## openShare

### <instance> openShare(text, key, [frame], [sessionData])

**Description:**

This invokes a dialog to let the user share specified content, either as a message in Messenger or as a post on the user's timeline.

A blob of data can be attached to the share which every game session launched from the share will be able to access via the `this.entryPointData` property.

This data must be less than or equal to 1000 characters when stringified.

When this method is called you should consider your game paused. Listen out for the `resume` event from this plugin to know when the dialog has been closed.

The user may choose to cancel the share action and close the dialog. The resulting `resume` event will be dispatched regardless if the user actually shared the content or not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| text | string | No | A text message to be shared. |
| --- | --- | --- | --- |
| key | string | No | The key of the texture to use as the share image. |
| frame | string | Yes | The frame of the texture to use as the share image. Set to `null` if you don't require a frame, but do need to set session data. |
| sessionData | object | Yes | A blob of data to attach to the share. |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1114](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1114)  
> Since: 3.13.0

---

## preloadAds

### <instance> preloadAds(placementID)

**Description:**

Attempt to create an instance of an interstitial ad.

If the instance is created successfully then the ad is preloaded ready for display in-game via the method `showAd()`.

If the ad loads it will emit the `adloaded` event, passing the AdInstance as the only parameter.

If the ad cannot be displayed because there was no inventory to fill it, it will emit the `adsnofill` event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| placementID | string | Array.<string> | No | The ad placement ID, or an array of IDs, as created in your Audience Network settings within Facebook. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1936](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1936)  
> Since: 3.13.0

---

## preloadVideoAds

### <instance> preloadVideoAds(placementID)

**Description:**

Attempt to create an instance of an rewarded video ad.

If the instance is created successfully then the ad is preloaded ready for display in-game via the method `showVideo()`.

If the ad loads it will emit the `adloaded` event, passing the AdInstance as the only parameter.

If the ad cannot be displayed because there was no inventory to fill it, it will emit the `adsnofill` event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| placementID | string | Array.<string> | No | The ad placement ID, or an array of IDs, as created in your Audience Network settings within Facebook. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L2022](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L2022)  
> Since: 3.13.0

---

## purchase

### <instance> purchase(productID, [developerPayload])

**Description:**

Begins the purchase flow for a specific product.

It makes an async call to the API, so the result isn't available immediately.

If they are successfully subscribed this plugin will emit the `purchase` event along

with the purchase data.

If they cannot, i.e. it's not in the list of supported APIs, or the request

was rejected, it will emit a `purchasefail` event instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| productID | string | No | The identifier of the product to purchase. |
| --- | --- | --- | --- |
| developerPayload | string | Yes | An optional developer-specified payload, to be included in the returned purchase's signed request. |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1530](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1530)  
> Since: 3.13.0

---

## quit

### <instance> quit()

**Description:**

Quits the game.

> Source: [src/FacebookInstantGamesPlugin.js#L1894](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1894)  
> Since: 3.13.0

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

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - `this`.

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

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## saveData

### <instance> saveData(data)

**Description:**

Set data to be saved to the designated cloud storage of the current player. The game can store up to 1MB of data for each unique player.

The data save is requested in an async call, so the result isn't available immediately.

Data managed via this plugins Data Manager instance is automatically synced with Facebook. However, you can call this

method directly if you need to replace the data object directly.

When the APIs `setDataAsync` call resolves it will emit the `savedata` event from this plugin. If the call fails for some

reason it will emit `savedatafail` instead.

The call resolving does not necessarily mean that the input has already been persisted. Rather, it means that the data was valid and

has been scheduled to be saved. It also guarantees that all values that were set are now available in `getData`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | object | No | An object containing a set of key-value pairs that should be persisted to cloud storage. The object must contain only serializable values - any non-serializable values will cause the entire modification to be rejected. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L848](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L848)  
> Since: 3.13.0

---

## saveSession

### <instance> saveSession(data)

**Description:**

Sets the data associated with the individual gameplay session for the current context.

This function should be called whenever the game would like to update the current session data.

This session data may be used to populate a variety of payloads, such as game play webhooks.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | object | No | An arbitrary data object, which must be less than or equal to 1000 characters when stringified. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1079](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1079)  
> Since: 3.13.0

---

## saveStats

### <instance> saveStats(data)

**Description:**

Save the stats of the current player to the designated cloud storage.

Stats in the Facebook Instant Games API are purely numerical values paired with a string-based key. Only numbers can be saved as stats,

all other data types will be ignored.

The data is requested in an async call, so the result isn't available immediately.

When the call completes the `savestats` event will be emitted along with the data object returned.

If the call fails, i.e. it's not in the list of supported APIs, or the request was rejected,

it will emit a `savestatsfail` event instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | object | No | An object containing a set of key-value pairs that should be persisted to cloud storage as stats. Note that only numerical values are stored. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L967](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L967)  
> Since: 3.13.0

---

## showAd

### <instance> showAd(placementID)

**Description:**

Displays a previously loaded interstitial ad.

If the ad is successfully displayed this plugin will emit the `adfinished` event, with the AdInstance object as its parameter.

If the ad cannot be displayed, it will emit the `adsnotloaded` event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| placementID | string | No | The ad placement ID to display. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L2108](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L2108)  
> Since: 3.13.0

---

## showLoadProgress

### <instance> showLoadProgress(scene)

**Description:**

Call this method from your `Scene.preload` in order to sync the load progress

of the Phaser Loader with the Facebook Instant Games loader display, i.e.:

```
Copy
this.facebook.showLoadProgress(this);

this.facebook.once('startgame', this.startGame, this);


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene for which you want to show loader progress for. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L357](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L357)  
> Since: 3.13.0

---

## showVideo

### <instance> showVideo(placementID)

**Description:**

Displays a previously loaded interstitial video ad.

If the ad is successfully displayed this plugin will emit the `adfinished` event, with the AdInstance object as its parameter.

If the ad cannot be displayed, it will emit the `adsnotloaded` event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| placementID | string | No | The ad placement ID to display. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L2159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L2159)  
> Since: 3.13.0

---

## shutdown

### <instance> shutdown()

**Description:**

Removes all listeners.

**Inherits:** [Phaser.Events.EventEmitter#shutdown](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L31)  
> Since: 3.0.0

---

## subscribeBot

### <instance> subscribeBot()

**Description:**

Subscribes the current player to the game bot.

It makes an async call to the API, so the result isn't available immediately.

If they are successfully subscribed this plugin will emit the `subscribebot` event.

If they cannot, i.e. it's not in the list of supported APIs, or the request

was rejected, it will emit a `subscribebotfail` event instead.

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L764](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L764)  
> Since: 3.13.0

---

## switchContext

### <instance> switchContext(contextID)

**Description:**

Request a switch into a specific context. If the player does not have permission to enter that context,

or if the player does not provide permission for the game to enter that context, this will emit a `switchfail` event.

Otherwise, the plugin will emit the `switch` event when the game has switched into the specified context.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| contextID | string | No | The ID of the desired context. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1293](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1293)  
> Since: 3.13.0

---

## switchGame

### <instance> switchGame(appID, [data])

**Description:**

Request that the client switch to a different Instant Game.

It makes an async call to the API, so the result isn't available immediately.

If the game switches successfully this plugin will emit the `switchgame` event and the client will load the new game.

If they cannot, i.e. it's not in the list of supported APIs, or the request

was rejected, it will emit a `switchgamefail` event instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| appID | string | No | The Application ID of the Instant Game to switch to. The application must be an Instant Game, and must belong to the same business as the current game. |
| --- | --- | --- | --- |
| data | object | Yes | An optional data payload. This will be set as the entrypoint data for the game being switched to. Must be less than or equal to 1000 characters when stringified. |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1806](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1806)  
> Since: 3.13.0

---

## update

### <instance> update(cta, text, key, frame, template, updateData)

**Description:**

Informs Facebook of a custom update that occurred in the game.

This will temporarily yield control to Facebook and Facebook will decide what to do based on what the update is.

Once Facebook returns control to the game the plugin will emit an `update` or `updatefail` event.

It makes an async call to the API, so the result isn't available immediately.

The `text` parameter is an update payload with the following structure:

```
Copy
text: {

    default: 'X just invaded Y\'s village!',

    localizations: {

        ar_AR: 'X \u0641\u0642\u0637 \u063A\u0632\u062A ' +

        '\u0642\u0631\u064A\u0629 Y!',

        en_US: 'X just invaded Y\'s village!',

        es_LA: '\u00A1X acaba de invadir el pueblo de Y!',

    }

}


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| cta | string | No | The call to action text. |
| --- | --- | --- | --- |
| text | object | No | The text object. |
| key | string | No | The key of the texture to use as the share image. |
| frame | string | integer | No | The frame of the texture to use as the share image. Set to `null` if you don't require a frame, but do need to set session data. |
| template | string | No | The update template key. |
| updateData | object | No | The update data object payload. |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1667](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1667)  
> Since: 3.13.0

---

## updateLeaderboard

### <instance> updateLeaderboard(cta, text, key, frame, template, updateData)

**Description:**

Informs Facebook of a leaderboard update that occurred in the game.

This will temporarily yield control to Facebook and Facebook will decide what to do based on what the update is.

Once Facebook returns control to the game the plugin will emit an `update` or `updatefail` event.

It makes an async call to the API, so the result isn't available immediately.

The `text` parameter is an update payload with the following structure:

```
Copy
text: {

    default: 'X just invaded Y\'s village!',

    localizations: {

        ar_AR: 'X \u0641\u0642\u0637 \u063A\u0632\u062A ' +

        '\u0642\u0631\u064A\u0629 Y!',

        en_US: 'X just invaded Y\'s village!',

        es_LA: '\u00A1X acaba de invadir el pueblo de Y!',

    }

}


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| cta | string | No | The call to action text. |
| --- | --- | --- | --- |
| text | object | No | The text object. |
| key | string | No | The key of the texture to use as the share image. |
| frame | string | integer | No | The frame of the texture to use as the share image. Set to `null` if you don't require a frame, but do need to set session data. |
| template | string | No | The update template key. |
| updateData | object | No | The update data object payload. |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1705](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1705)  
> Since: 3.13.0

---

# Private Methods

## \_share

### <instance> \_share(intent, text, key, [frame], [sessionData])

**Description:**

Internal share handler.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| intent | string | No | ("INVITE" | "REQUEST" |
| --- | --- | --- | --- |
| text | string | No | A text message to be shared. |
| key | string | No | The key of the texture to use as the share image. |
| frame | string | Yes | The frame of the texture to use as the share image. Set to `null` if you don't require a frame, but do need to set session data. |
| sessionData | object | Yes | A blob of data to attach to the share. |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1218](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1218)  
> Since: 3.13.0

---

## \_update

### <instance> \_update(action, cta, text, key, frame, template, updateData)

**Description:**

Internal update handler.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| action | string | No | The update action. |
| --- | --- | --- | --- |
| cta | string | No | The call to action text. |
| text | object | No | The text object. |
| key | string | No | The key of the texture to use as the share image. |
| frame | string | integer | No | The frame of the texture to use as the share image. Set to `null` if you don't require a frame, but do need to set session data. |
| template | string | No | The update template key. |
| updateData | object | No | The update data object payload. |

**Returns:** [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) - This Facebook Instant Games Plugin instance.

> Source: [src/FacebookInstantGamesPlugin.js#L1743](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L1743)  
> Since: 3.13.0

---

## changeDataHandler

### <instance> changeDataHandler(parent, key, value)

**Description:**

Internal change data handler.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| parent | [Phaser.Data.DataManager](data-datamanager.md) | No | The parent Data Manager instance. |
| --- | --- | --- | --- |
| key | string | No | The key of the data. |
| value | any | No | The value of the data. |

> Source: [src/FacebookInstantGamesPlugin.js#L327](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L327)  
> Since: 3.13.0

---

## gameStartedHandler

### <instance> gameStartedHandler()

**Description:**

The internal gameStarted handler.

**Access:** private

> Source: [src/FacebookInstantGamesPlugin.js#L424](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L424)  
> Since: 3.20.0

---

## setDataHandler

### <instance> setDataHandler(parent, key, value)

**Description:**

Internal set data handler.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| parent | [Phaser.Data.DataManager](data-datamanager.md) | No | The parent Data Manager instance. |
| --- | --- | --- | --- |
| key | string | No | The key of the data. |
| value | any | No | The value of the data. |

> Source: [src/FacebookInstantGamesPlugin.js#L297](https://github.com/phaserjs/phaser/blob/v3.87.0/src/FacebookInstantGamesPlugin.js#L297)  
> Since: 3.13.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [ads](#ads)

    - [ads: Array.<AdInstance>](#ads-arrayadinstance)
  + [catalog](#catalog)

    - [catalog: Array.<Product>](#catalog-arrayproduct)
  + [contextID](#contextid)

    - [contextID: string](#contextid-string)
  + [contextType](#contexttype)

    - [contextType: string](#contexttype-string)
  + [data](#data)

    - [data: Phaser.Data.DataManager](#data-phaserdatadatamanager)
  + [dataLocked](#datalocked)

    - [dataLocked: boolean](#datalocked-boolean)
  + [entryPoint](#entrypoint)

    - [entryPoint: string](#entrypoint-string)
  + [entryPointData](#entrypointdata)

    - [entryPointData: any](#entrypointdata-any)
  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [hasLoaded](#hasloaded)

    - [hasLoaded: boolean](#hasloaded-boolean)
  + [leaderboards](#leaderboards)

    - [leaderboards: Array.<Phaser.FacebookInstantGamesLeaderboard>](#leaderboards-arrayphaserfacebookinstantgamesleaderboard)
  + [locale](#locale)

    - [locale: string](#locale-string)
  + [paymentsReady](#paymentsready)

    - [paymentsReady: boolean](#paymentsready-boolean)
  + [platform](#platform)

    - [platform: string](#platform-string)
  + [playerCanSubscribeBot](#playercansubscribebot)

    - [playerCanSubscribeBot: boolean](#playercansubscribebot-boolean)
  + [playerID](#playerid)

    - [playerID: string](#playerid-string)
  + [playerName](#playername)

    - [playerName: string](#playername-string)
  + [playerPhotoURL](#playerphotourl)

    - [playerPhotoURL: string](#playerphotourl-string)
  + [purchases](#purchases)

    - [purchases: Array.<Purchase>](#purchases-arraypurchase)
  + [supportedAPIs](#supportedapis)

    - [supportedAPIs: Array.<string>](#supportedapis-arraystring)
  + [version](#version)

    - [version: string](#version-string)
* [Public Methods](#public-methods)

  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [canSubscribeBot](#cansubscribebot)

    - [<instance> canSubscribeBot()](#instance-cansubscribebot)
  + [checkAPI](#checkapi)

    - [<instance> checkAPI(api)](#instance-checkapiapi)
  + [chooseContext](#choosecontext)

    - [<instance> chooseContext([options])](#instance-choosecontextoptions)
  + [consumePurchase](#consumepurchase)

    - [<instance> consumePurchase(purchaseToken)](#instance-consumepurchasepurchasetoken)
  + [createContext](#createcontext)

    - [<instance> createContext(playerID)](#instance-createcontextplayerid)
  + [createShortcut](#createshortcut)

    - [<instance> createShortcut()](#instance-createshortcut)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [flushData](#flushdata)

    - [<instance> flushData()](#instance-flushdata)
  + [gameStarted](#gamestarted)

    - [<instance> gameStarted()](#instance-gamestarted)
  + [getCatalog](#getcatalog)

    - [<instance> getCatalog()](#instance-getcatalog)
  + [getData](#getdata)

    - [<instance> getData(keys)](#instance-getdatakeys)
  + [getID](#getid)

    - [<instance> getID()](#instance-getid)
  + [getLeaderboard](#getleaderboard)

    - [<instance> getLeaderboard(name)](#instance-getleaderboardname)
  + [getLocale](#getlocale)

    - [<instance> getLocale()](#instance-getlocale)
  + [getPlatform](#getplatform)

    - [<instance> getPlatform()](#instance-getplatform)
  + [getPlayerID](#getplayerid)

    - [<instance> getPlayerID()](#instance-getplayerid)
  + [getPlayerName](#getplayername)

    - [<instance> getPlayerName()](#instance-getplayername)
  + [getPlayerPhotoURL](#getplayerphotourl)

    - [<instance> getPlayerPhotoURL()](#instance-getplayerphotourl)
  + [getPlayers](#getplayers)

    - [<instance> getPlayers()](#instance-getplayers)
  + [getProduct](#getproduct)

    - [<instance> getProduct(productID)](#instance-getproductproductid)
  + [getPurchases](#getpurchases)

    - [<instance> getPurchases()](#instance-getpurchases)
  + [getSDKVersion](#getsdkversion)

    - [<instance> getSDKVersion()](#instance-getsdkversion)
  + [getStats](#getstats)

    - [<instance> getStats([keys])](#instance-getstatskeys)
  + [getType](#gettype)

    - [<instance> getType()](#instance-gettype)
  + [incStats](#incstats)

    - [<instance> incStats(data)](#instance-incstatsdata)
  + [isSizeBetween](#issizebetween)

    - [<instance> isSizeBetween([min], [max])](#instance-issizebetweenmin-max)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [loadPlayerPhoto](#loadplayerphoto)

    - [<instance> loadPlayerPhoto(scene, key)](#instance-loadplayerphotoscene-key)
  + [log](#log)

    - [<instance> log(name, [value], [params])](#instance-logname-value-params)
  + [matchPlayer](#matchplayer)

    - [<instance> matchPlayer([matchTag], [switchImmediately])](#instance-matchplayermatchtag-switchimmediately)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [openChallenge](#openchallenge)

    - [<instance> openChallenge(text, key, [frame], [sessionData])](#instance-openchallengetext-key-frame-sessiondata)
  + [openInvite](#openinvite)

    - [<instance> openInvite(text, key, [frame], [sessionData])](#instance-openinvitetext-key-frame-sessiondata)
  + [openRequest](#openrequest)

    - [<instance> openRequest(text, key, [frame], [sessionData])](#instance-openrequesttext-key-frame-sessiondata)
  + [openShare](#openshare)

    - [<instance> openShare(text, key, [frame], [sessionData])](#instance-opensharetext-key-frame-sessiondata)
  + [preloadAds](#preloadads)

    - [<instance> preloadAds(placementID)](#instance-preloadadsplacementid)
  + [preloadVideoAds](#preloadvideoads)

    - [<instance> preloadVideoAds(placementID)](#instance-preloadvideoadsplacementid)
  + [purchase](#purchase)

    - [<instance> purchase(productID, [developerPayload])](#instance-purchaseproductid-developerpayload)
  + [quit](#quit)

    - [<instance> quit()](#instance-quit)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [saveData](#savedata)

    - [<instance> saveData(data)](#instance-savedatadata)
  + [saveSession](#savesession)

    - [<instance> saveSession(data)](#instance-savesessiondata)
  + [saveStats](#savestats)

    - [<instance> saveStats(data)](#instance-savestatsdata)
  + [showAd](#showad)

    - [<instance> showAd(placementID)](#instance-showadplacementid)
  + [showLoadProgress](#showloadprogress)

    - [<instance> showLoadProgress(scene)](#instance-showloadprogressscene)
  + [showVideo](#showvideo)

    - [<instance> showVideo(placementID)](#instance-showvideoplacementid)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [subscribeBot](#subscribebot)

    - [<instance> subscribeBot()](#instance-subscribebot)
  + [switchContext](#switchcontext)

    - [<instance> switchContext(contextID)](#instance-switchcontextcontextid)
  + [switchGame](#switchgame)

    - [<instance> switchGame(appID, [data])](#instance-switchgameappid-data)
  + [update](#update)

    - [<instance> update(cta, text, key, frame, template, updateData)](#instance-updatecta-text-key-frame-template-updatedata)
  + [updateLeaderboard](#updateleaderboard)

    - [<instance> updateLeaderboard(cta, text, key, frame, template, updateData)](#instance-updateleaderboardcta-text-key-frame-template-updatedata)
* [Private Methods](#private-methods)

  + [\_share](#_share)

    - [<instance> \_share(intent, text, key, [frame], [sessionData])](#instance-_shareintent-text-key-frame-sessiondata)
  + [\_update](#_update)

    - [<instance> \_update(action, cta, text, key, frame, template, updateData)](#instance-_updateaction-cta-text-key-frame-template-updatedata)
  + [changeDataHandler](#changedatahandler)

    - [<instance> changeDataHandler(parent, key, value)](#instance-changedatahandlerparent-key-value)
  + [gameStartedHandler](#gamestartedhandler)

    - [<instance> gameStartedHandler()](#instance-gamestartedhandler)
  + [setDataHandler](#setdatahandler)

    - [<instance> setDataHandler(parent, key, value)](#instance-setdatahandlerparent-key-value)

Back to top

©2025[Phaser](https://docs.phaser.io)