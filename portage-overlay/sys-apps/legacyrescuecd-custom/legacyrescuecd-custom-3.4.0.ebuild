DESCRIPTION="LegacyRescueCd customization package (forked from System Recue CD 5.x)"
LICENSE="GPL-2"
SLOT="0"
KEYWORDS="amd64 x86"
IUSE="full-build"

inherit eutils

src_install()
{
	use full-build && cdtype="full" || cdtype="mini"
	echo "${cdtype}" >| legacyrescuecd-type.txt
	insinto /usr/share/legacyrescuecd
	doins legacyrescuecd-type.txt
}
