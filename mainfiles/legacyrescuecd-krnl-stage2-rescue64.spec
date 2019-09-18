subarch: amd64
version_stamp: krnl
target: livecd-stage2
rel_type: default
profile: default/linux/x86/17.1
snapshot: latest
source_subpath: default/livecd-stage1-amd64-mini
portage_confdir: /worksrc/legacyrescuecd-src/portage-etc-x86
portage_overlay: /worksrc/legacyrescuecd-src/portage-overlay

livecd/fstype: none
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-3.72-cdtar.tar.bz2
livecd/iso: /worksrc/isofiles/legacyrescuecd-amd64-current.iso
livecd/splash_type: 
livecd/splash_theme: 
livecd/bootargs: dokeymap
livecd/gk_mainargs: --makeopts="-j5" --integrated-initramfs
livecd/type: generic-livecd
livecd/readme:
livecd/motd: 
livecd/modblacklist:
livecd/overlay: /worksrc/legacyrescuecd-src/overlay-iso-x86
livecd/users:

boot/kernel: rescue64

boot/kernel/rescue64/sources: sys-kernel/std-sources
boot/kernel/rescue64/config: /worksrc/legacyrescuecd-src/kernelcfg/config-std-x86_64.cfg
boot/kernel/rescue64/use: pcmcia usb -X png truetype 
boot/kernel/rescue64/extraversion: amd64
boot/kernel/rescue64/packages:
	app-emulation/open-vm-tools
	sys-block/open-iscsi
