# rescue-cd-legacy

This is a fork of the 5.3.2 branch of System Rescue CD, with the intent (currently unrealized) of bringing it up to date.

Differences from upstream (intended, not yet realized):
* rebranded to legacyrescuecd
* trying to follow gentoo-upstable as closely as possible
* default to BASH 
* remove support for:
** sparc
** really old processors (minimum Core2 or similar-age processor, or more recent Atom)
** some more obscure hardware (fewer video cards,
** reiserfs

Things I'm considering:
* default to docache
* add support for more hypervisors natively
* gentoo-sources based kernel
