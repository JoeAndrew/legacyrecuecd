subarch: i686
version_stamp: default
target: livecd-stage1
rel_type: default
profile: default/linux/x86/10.0
snapshot: 20120507
source_subpath: default/stage4-i386-20120505-01
portage_confdir: /worksrc/sysresccd-src/portage-etc-x86
portage_overlay: /worksrc/sysresccd-src/portage-overlay

livecd/use: -svg -opengl -glx -berkdb -gdbm -minimal -introspection dri X bindist fbcon ipv6 livecd ncurses pam readline ssl unicode zlib nptl nptlonly multilib multislot jfs ntfs reiserfs xfs fat reiser4 samba gtk gtk2 png jpeg xorg usb pdf acl nologin atm bash-completion slang -kdrive vram loop-aes crypt device-mapper 7zip xattr bzip2 server lzo xpm bash-completion -fam -doc -hardened -spoof-source -static -tcpd -mailwrapper -milter -nls -selinux -ermt -pic -dar32 -dar64 -openct -pcsc-lite -smartcard -caps -qt3 -qt4 -aqua -cscope -gnome -gpm -motif -netbeans -nextaw -perl -python -ruby -xterm -emacs -justify -spell -vim-pager -vim-with-x -sqlite -afs -bashlogger -plugins -vanilla -examples -maildir pcre -accessibility -ithreads -perlsuid -php -pike -tcl -tk -nocxx -no-net2 -kerberos -sse2 -aio -cups -ldap -quotas -swat -syslog -winbind -socks5 -guile -X509 dbus -gnutls -gsm -cracklib -nousuid -skey -old-linux -pxeserial -multitarget -test -clvm -cman -gulm -gd -glibc-compat20 -glibc-omitfp -bidi -xinerama -qt3support -alsa -xcb nfsv4 -gallium

livecd/packages:
	app-admin/hddtemp
	app-admin/hwreport
	app-admin/ide-smart
	app-admin/mcelog
	app-admin/passook
	app-admin/procinfo-ng
	app-admin/pwgen
	app-admin/sudo
	app-admin/syslog-ng
	app-admin/sysstat
	app-admin/testdisk
	app-antivirus/clamav
	app-arch/afio
	app-arch/arj
	app-arch/bzip2
	app-arch/cabextract
	app-arch/cfv
	app-arch/cpio
	app-arch/dpkg
	app-arch/dump
	app-arch/gzip
	app-arch/lzip
	app-arch/lzop
	app-arch/mscompress
	app-arch/mt-st
	app-arch/ncompress
	app-arch/p7zip
	app-arch/par2cmdline
	app-arch/pbzip2
	app-arch/pigz
	app-arch/pxz
	app-arch/rar
	app-arch/rpm
	app-arch/rpm2targz
	app-arch/rzip
	app-arch/sharutils
	app-arch/tar
	app-arch/unace
	app-arch/unrar
	app-arch/unshield
	app-arch/unzip
	app-arch/xarchiver
	app-arch/xz-utils
	app-arch/zip
	app-backup/bacula
	app-backup/dar
	app-backup/duplicity
	app-backup/fsarchiver
	app-backup/rdiff-backup
	app-backup/rsnapshot
	app-backup/tob
	app-benchmarks/bonnie++
	app-benchmarks/cpuburn
	app-benchmarks/iozone
	app-benchmarks/stress
	app-benchmarks/systester
	app-cdr/cdw
	app-cdr/dvd+rw-tools
	app-cdr/isomaster
	app-cdr/xfburn
	app-crypt/chntpw
	app-crypt/md5deep
	app-crypt/truecrypt
	app-editors/gvim
	app-editors/hexcurse
	app-editors/hexedit
	app-editors/joe
	app-editors/nano
	app-editors/qemacs
	app-editors/vim
	app-editors/vim-core
	app-editors/zile
	app-forensics/afflib
	app-forensics/chkrootkit
	app-forensics/cmospwd
	app-forensics/foremost
	app-forensics/magicrescue
	app-forensics/sleuthkit
	app-misc/beep
	app-misc/ckermit
	app-misc/colordiff
	app-misc/emelfm2
	app-misc/fdupes
	app-misc/livecd-tools
	app-misc/mc
	app-misc/screen
	app-misc/scrub
	app-misc/secure-delete
	app-misc/symlinks
	app-misc/tmux
	app-misc/vlock
	app-misc/wipe
	app-portage/eix
	app-portage/gentoolkit
	app-portage/mirrorselect
	app-shells/bash
	app-shells/ksh
	app-shells/tcsh
	app-shells/zsh
	app-text/dos2unix
	app-text/epdfview
	app-text/tree
	app-text/wgetpaste
	app-vim/gentoo-syntax
	dev-lang/perl
	dev-lang/ruby
	dev-libs/expat
	dev-libs/icu
	dev-libs/libconfig
	dev-libs/libisoburn
	dev-libs/lzo
	dev-libs/openssl
	dev-libs/pkcs11-helper
	dev-libs/popt
	dev-util/cmake
	dev-util/debootstrap
	dev-util/geany
	dev-util/intltool
	dev-util/ltrace
	dev-util/pkgconfig
	dev-util/strace
	dev-vcs/git
	gnome-extra/nm-applet
	lxde-base/lxrandr
	media-fonts/font-bh-ttf
	media-fonts/font-bh-type1
	media-fonts/font-util
	media-fonts/terminus-font
	media-fonts/unifont
	net-analyzer/arping
	net-analyzer/dnstracer
	net-analyzer/httping
	net-analyzer/ifstat
	net-analyzer/iftop
	net-analyzer/iptraf-ng
	net-analyzer/macchanger
	net-analyzer/netcat
	net-analyzer/ngrep
	net-analyzer/nmap
	net-analyzer/tcpdump
	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-analyzer/vnstat
	net-dialup/globespan-adsl
	net-dialup/gtkterm
	net-dialup/hcfpcimodem
	net-dialup/hsfmodem
	net-dialup/linux-atm
	net-dialup/mingetty
	net-dialup/minicom
	net-dialup/ppp
	net-dialup/pppconfig
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-dialup/speedtouch-usb
	net-dns/bind-tools
	net-firewall/ipsec-tools
	net-firewall/iptables
	net-fs/mount-cifs
	net-fs/nfs-utils
	net-fs/samba
	net-ftp/ftp
	net-ftp/lftp
	net-ftp/ncftp
	net-ftp/tftp-hpa
	net-irc/irssi
	net-misc/autossh
	net-misc/bridge-utils
	net-misc/dhcp
	net-misc/dhcpcd
	net-misc/ethercard-diag
	net-misc/ifenslave
	net-misc/iperf
	net-misc/iputils
	net-misc/netkit-rsh
	net-misc/networkmanager
	net-misc/networkmanager-openvpn
	net-misc/networkmanager-vpnc
	net-misc/ntp
	net-misc/openssh
	net-misc/openswan
	net-misc/openvpn
	net-misc/rdate
	net-misc/rdesktop
	net-misc/rsync
	net-misc/telnet-bsd
	net-misc/tigervnc
	net-misc/udpcast
	net-misc/vconfig
	net-misc/vpnc
	net-misc/wget
	net-misc/whois
	net-misc/wput
	net-wireless/acx-firmware
	net-wireless/atmel-firmware
	net-wireless/b43-fwcutter
	net-wireless/bcm43xx-fwcutter
	net-wireless/ipw2100-firmware
	net-wireless/ipw2200-firmware
	net-wireless/iw
	net-wireless/linux-wlan-ng-firmware
	net-wireless/madwifi-ng-tools
	net-wireless/prism54-firmware
	net-wireless/rtl8192su-firmware
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	net-wireless/zd1201-firmware
	net-wireless/zd1211-firmware
	perl-core/Encode
	sys-apps/acl
	sys-apps/attr
	sys-apps/cciss_vol_status
	sys-apps/coreutils
	sys-apps/dcfldd
	sys-apps/debianutils
	sys-apps/diffutils
	sys-apps/dmapi
	sys-apps/dmidecode
	sys-apps/dstat
	sys-apps/dumpdisklayout
	sys-apps/ed
	sys-apps/ethtool
	sys-apps/fbset
	sys-apps/file
	sys-apps/findutils
	sys-apps/flashrom
	sys-apps/fxload
	sys-apps/gawk
	sys-apps/gptfdisk
	sys-apps/groff
	sys-apps/hdparm
	sys-apps/hwsetup
	sys-apps/ipmitool
	sys-apps/iproute2
	sys-apps/kbd
	sys-apps/lm_sensors
	sys-apps/lshw
	sys-apps/man-pages
	sys-apps/memtester
	sys-apps/miscfiles
	sys-apps/mlocate
	sys-apps/netplug
	sys-apps/net-tools
	sys-apps/openrc
	sys-apps/pcmciautils
	sys-apps/pv
	sys-apps/rename
	sys-apps/rescan-scsi-bus
	sys-apps/sdparm
	sys-apps/sed
	sys-apps/setserial
	sys-apps/sg3_utils
	sys-apps/shadow
	sys-apps/smartmontools
	sys-apps/tcp-wrappers
	sys-apps/usb_modeswitch
	sys-apps/usbutils
	sys-apps/util-linux
	sys-apps/which
	sys-apps/x86info
	sys-auth/pambase
	sys-block/aic94xx-firmware
	sys-block/eject
	sys-block/gpart
	sys-block/gparted
	sys-block/lsiutil
	sys-block/mbuffer
	sys-block/megacli
	sys-block/megarc
	sys-block/mpt-status
	sys-block/ms-sys
	sys-block/mtx
	sys-block/nbd
	sys-block/partclone
	sys-block/parted
	sys-block/partimage
	sys-block/scsiadd
	sys-block/tw_cli
	sys-boot/efibootmgr
	=sys-boot/grub-0.97-r10
	sys-boot/lilo
	sys-boot/mbr
	sys-boot/os-prober
	sys-boot/syslinux
	sys-cluster/drbd
	sys-devel/autogen
	sys-devel/bc
	sys-devel/crossdev
	sys-devel/gettext
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/ddrescue
	sys-fs/dd-rescue
	sys-fs/diskdev_cmds
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/ext3grep
	sys-fs/extundelete
	sys-fs/hfsplusutils
	sys-fs/hfsutils
	sys-fs/jfsutils
	sys-fs/lde
	sys-fs/lsscsi
	sys-fs/lufis
	sys-fs/lufs
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/mtd-utils
	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/ntfsreloc
	sys-fs/reiser4progs
	sys-fs/reiserfsprogs
	sys-fs/scrounge-ntfs
	sys-fs/squashfs-tools
	sys-fs/sshfs-fuse
	sys-fs/udev
	sys-fs/udftools
	sys-fs/xfsdump
	sys-fs/xfsprogs
	sys-kernel/gentoo-sources
	sys-kernel/linux-firmware
	sys-libs/libstdc++-v3
	sys-libs/openipmi
	sys-libs/pam
	sys-libs/pwdb
	sys-libs/readline
	sys-libs/zlib
	sys-process/atop
	sys-process/cronbase
	sys-process/htop
	sys-process/iotop
	sys-process/lsof
	sys-process/nmon
	sys-process/procps
	sys-process/psmisc
	sys-process/vixie-cron
	www-client/elinks
	www-client/midori
	www-servers/thttpd
	x11-apps/setxkbmap
	x11-apps/xcalc
	x11-apps/xdpyinfo
	x11-apps/xgamma
	x11-apps/xhost
	x11-apps/xinit
	x11-apps/xkbcomp
	x11-apps/xmodmap
	x11-apps/xrandr
	x11-apps/xset
	x11-apps/xwd
	x11-base/xorg-server
	x11-drivers/xf86-input-evdev
	x11-drivers/xf86-input-keyboard
	x11-drivers/xf86-input-mouse
	x11-drivers/xf86-input-vmmouse
	x11-libs/wxGTK
	x11-misc/mkxf86config
	x11-misc/read-edid
	x11-misc/util-macros
	x11-misc/xkeyboard-config
	x11-proto/dri2proto
	x11-proto/glproto
	x11-proto/inputproto
	x11-proto/xextproto
	x11-proto/xf86driproto
	x11-proto/xf86miscproto
	x11-proto/xineramaproto
	x11-terms/terminal
	x11-themes/gnome-icon-theme
	x11-wm/jwm
	xfce-base/xfce4-meta
	xfce-extra/xfce4-battery-plugin
	xfce-extra/xfce4-datetime-plugin
	xfce-extra/xfce4-notifyd
	xfce-extra/xfce4-taskmanager
	xfce-extra/xfce4-wavelan-plugin

