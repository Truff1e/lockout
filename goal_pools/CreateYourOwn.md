# Goal Pools

You can create your own goal pools to draw from when generating a random board. The syntax is relatively simple.

The basic format is:

```json
{
    "meta": {
        "version": VERSION,
        "dp_version": [DPVERSION],
        "name": "NAME",
        "description": "DESCRIPTION",
        "author": "AUTHOR",
        "last_updated": "CREATIONDATE"
    },
    "pools": [
        {
            "type": "POOLTYPE",
            "goals": [GOALS]
        },
        {
            "type": "POOLTYPE",
            "goals": [GOALS]
        }
    ]
}
```


### Pools
You can add as many pools as you want. Pools can be any of the following types:

**all**

Adds all goals in "goals" to the pool.

**pick**

Picks an "amount" (integer) of goals from the list of "goals". You will need to specify an amount.

More pool types will be added in the future to allow for more customizability.


### Goals
This is a list of goal id numbers (the full list can be found in index.py).


### Meta
These fields specify various details about the goal pool. None of them are mandatory, but can be helpful to differentiate between different pool files. Some fields may become required in the future.
