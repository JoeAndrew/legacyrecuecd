subarch: i686
version_stamp: krnl
target: livecd-stage2
rel_type: default
profile: default/linux/x86/17.1
snapshot: latest
source_subpath: default/livecd-stage1-i686-mini
portage_confdir: /worksrc/legacyrescuecd-src/portage-etc-x86
portage_overlay: /worksrc/legacyrescuecd-src/portage-overlay

livecd/fstype: none
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-3.72-cdtar.tar.bz2
livecd/iso: /worksrc/isofiles/legacyrescuecd-x86-current.iso
livecd/splash_type: 
livecd/splash_theme: 
livecd/bootargs: dokeymap
livecd/gk_mainargs: --makeopts="-j13" --integrated-initramfs
livecd/type: generic-livecd
livecd/readme:
livecd/motd: 
livecd/modblacklist:
livecd/overlay: /worksrc/legacyrescuecd-src/overlay-iso-x86
livecd/users:

boot/kernel: rescue32

boot/kernel/rescue32/sources: sys-kernel/std-sources
boot/kernel/rescue32/config: /worksrc/legacyrescuecd-src/kernelcfg/config-std-i686.cfg
boot/kernel/rescue32/use: pcmcia usb -X png truetype 
boot/kernel/rescue32/extraversion: i686
boot/kernel/rescue32/packages:
	app-emulation/open-vm-tools
	sys-block/open-iscsi
