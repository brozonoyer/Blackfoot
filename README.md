# A Morphological Analyzer for Blackfoot Nouns

This analyzer takes Frantz’s (2017) *Blackfoot Grammar* and *Blackfoot Dictionary* as a reference for Blackfoot phonology, morphology, and standardized orthography. It is a work in progress, with an end goal of accounting for every nominal inflection attested for in the *Grammar* and *Dictionary*. Refer especially to *Chapter 2* for basics of Blackfoot noun inflection, *Chapter 5* for phonological rules, *Chapter 14* for possessive nouns, *Chapter 15* for allomorphy, and *Appendix B* for an exhaustive list of Blackfoot phonological rules. 

I use [this spreadsheet](https://docs.google.com/spreadsheets/d/1ZUYgWPyn846HW9tN7N7_AP4OmyIuVX3Vj9wv7-DQWk8/edit#gid=0) (at present scarcely-populated) to keep track of progress in this effort.

The analyzer is implemented with the [Helsinki Finite-State Technology toolkit](https://github.com/hfst/hfst/wiki). Please refer to their [Download And Install](https://github.com/hfst/hfst/wiki/Download-And-Install) page to get the right version for your system (developed with the Mac OS X version).

Start up `hsft-xfst` from `blackfoot.script`, which encodes phonological and allomorphy rules, and composes them with the lexicon defined in `blackfoot.lexc`:

```<PATH>/<TO>/hfst/bin/hfst-xfst -l blackfoot.script```

To generate a surface form from an abstract representation (refer to `blackfoot.lexc` for the full list of multicharacter symbols/glosses):

```
hfst[1]: apply down natáyo+3S
natáyowa
```

To analyze a surface form:

```
hfst[1]: apply up kakkóíksi
kakkóó+AN.P
```

Please address any questions or suggestions to `brozonoyer@brandeis.edu`.

## References

Donald G. Frantz. 2017. *Blackfoot Grammar*, 3 edition. University of Toronto Press.

Donald G. Frantz and Norma Jean Russell. 2017. *Blackfoot Dictionary of Stems, Roots, and Affixes*, 3 edition. University of Toronto Press.

University of Helsinki. 2003-2008. Helsinki Finite State Technology (HFST).

Kenneth R. Beesley and Lauri Karttunen. 2003. *Finite State Morphology*. CSLI Publications.
