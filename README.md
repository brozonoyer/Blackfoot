# A Morphological Analyzer for Blackfoot Nouns

This analyzer is implemented with the Helsinki Finite-State Transducer toolkit. Please refer to [their Download And Install page](https://github.com/hfst/hfst/wiki/Download-And-Install) to install it on your system.

Start up `hsft-xfst` from `blackfoot.script`, which encodes phonological and allomorphy rules, and composes them with the lexicon defined in `blackfoot.lexc`:

```<PATH>/<TO>/hfst/bin/hfst-xfst -l blackfoot.script```

To generate a surface form from an abstract representation (refer to `blackfoot.lexc` for the full list of multicharacter symbols):

`apply down natáyo+3S` –> `natáyowa`

To analyze a surface form:

`apply up kakkóíksi` –> `kakkóó+AN.P`
