Name:       grilo-plugins
Summary:    Grilo plugins
Version:    0.2.14
Release:    1
Group:      Development/Libraries
License:    LGPLv2.1
URL:        https://live.gnome.org/Grilo
Source0:    http://ftp.gnome.org/pub/GNOME/sources/grilo-plugins/0.2/%{name}-%{version}.tar.xz
Patch0:     disable-doc.patch
BuildRequires:  pkgconfig(grilo-0.2)
BuildRequires:  pkgconfig(grilo-net-0.2)
BuildRequires:  pkgconfig(grilo-pls-0.2)
BuildRequires:  pkgconfig(tracker-sparql-1.0)
BuildRequires:  pkgconfig(libgdata)
BuildRequires:  pkgconfig(oauth)
BuildRequires:  pkgconfig(libquvi-0.9)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(gmime-2.6)
BuildRequires:  pkgconfig(libgcrypt)
#BuildRequires:  pkgconfig(libmediaart-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(totem-plparser) >= 3.4.1
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  intltool
BuildRequires:  gnome-common

%description
Grilo is a framework focused on making media discovery and browsing
easy for application developers.
More precisely, Grilo provides:
* A single, high-level API that abstracts the differences among
  various media content providers, allowing application developers
  to integrate content from various services and sources easily.
* A collection of plugins for accessing content from various media
  providers. Developers can share efforts and code by writing
  plugins for the framework that are application agnostic.
* A flexible API that allows plugin developers to write plugins of
  various kinds.
This package contains the set of plugins officially distributed with
Grilo.

%package    -n grilo-plugin-youtube
Group:      Multimedia
Summary:    Grilo plugin - youtube

%description -n grilo-plugin-youtube
Grilo plugin - youtube


%package    -n grilo-plugin-filesystem
Group:      Multimedia
Summary:    Grilo plugin - filesystem

%description -n grilo-plugin-filesystem
Grilo plugin - filesystem


%package    -n grilo-plugin-jamendo
Group:      Multimedia
Summary:    Grilo plugin - jamendo

%description -n grilo-plugin-jamendo
Grilo plugin - jamendo


%package    -n grilo-plugin-lastfm-albumart
Group:      Multimedia
Summary:    Grilo plugin - lastfm-albumart

%description -n grilo-plugin-lastfm-albumart
Grilo plugin - lastfm-albumart


%package    -n grilo-plugin-flickr
Group:      Multimedia
Summary:    Grilo plugin - flickr

%description -n grilo-plugin-flickr
Grilo plugin - flickr


%package    -n grilo-plugin-podcasts
Group:      Multimedia
Summary:    Grilo plugin - podcasts

%description -n grilo-plugin-podcasts
Grilo plugin - podcasts


# %package    -n grilo-plugin-bookmarks
# Group:      Multimedia
# Summary:    Grilo plugin - bookmarks

# %description -n grilo-plugin-bookmarks
# Grilo plugin - bookmarks


%package    -n grilo-plugin-shoutcast
Group:      Multimedia
Summary:    Grilo plugin - shoutcast

%description -n grilo-plugin-shoutcast
Grilo plugin - shoutcast


%package    -n grilo-plugin-apple-trailers
Group:      Multimedia
Summary:    Grilo plugin - apple-trailers

%description -n grilo-plugin-apple-trailers
Grilo plugin - apple-trailers


%package    -n grilo-plugin-metadata-store
Group:      Multimedia
Summary:    Grilo plugin - metadata-store

%description -n grilo-plugin-metadata-store
Grilo plugin - metadata-store


%package    -n grilo-plugin-vimeo
Group:      Multimedia
Summary:    Grilo plugin - vimeo

%description -n grilo-plugin-vimeo
Grilo plugin - vimeo


%package    -n grilo-plugin-gravatar
Group:      Multimedia
Summary:    Grilo plugin - gravatar

%description -n grilo-plugin-gravatar
Grilo plugin - gravatar


%package    -n grilo-plugin-tracker
Group:      Multimedia
Summary:    Grilo plugin - tracker

%description -n grilo-plugin-tracker
Grilo plugin - tracker


%package    -n grilo-plugin-bliptv
Group:      Multimedia
Summary:    Grilo plugin - bliptv

%description -n grilo-plugin-bliptv
Grilo plugin - bliptv


# %package    -n grilo-plugin-localmetadata
# Group:      Multimedia
# Summary:    Grilo plugin - localmetadata

# %description -n grilo-plugin-localmetadata
# Grilo plugin - localmetadata


%package    -n grilo-plugin-raitv
Group:      Multimedia
Summary:    Grilo plugin - Rai.tv

%description -n grilo-plugin-raitv
Grilo plugin - Rai.tv


%package    -n grilo-plugin-magnatune
Group:      Multimedia
Summary:    Grilo plugin - Magnatune

%description -n grilo-plugin-magnatune
Grilo plugin - Mangnatune

%package    -n grilo-plugin-dleyna
Group:      Multimedia
Summary:    Grilo plugin - dLeyna

%description -n grilo-plugin-dleyna
A Grilo plugin for browsing DLNA servers

%package    -n grilo-plugin-opensubtitles
Group:      Multimedia
Summary:    Grilo plugin - OpenSubtitles Provider

%description -n grilo-plugin-opensubtitles
A Grilo plugin that gets a list of subtitles for a video

%prep
%setup -q -n %{name}-%{version}/%{name}
%patch0 -p1

%build
echo "EXTRA_DIST = missing-gtk-doc" > gtk-doc.make
echo "EXTRA_DIST = missing-gnome-doc" > gnome-doc-utils.make
REQUIRED_AUTOMAKE_VERSION=1.8 USE_GNOME2_MACROS=1 USE_COMMON_DOC_BUILD=no NOCONFIGURE=1 \
. gnome-autogen.sh

%configure --disable-static --disable-goa --disable-gcov --enable-filesystem --disable-optical-media --enable-jamendo --enable-lastfm-albumart --enable-youtube --enable-flickr --disable-pocket --enable-podcasts --disable-bookmarks --enable-shoutcast --enable-apple-trailers --enable-magnatune --disable-lua-factory --enable-metadata-store --enable-vimeo --enable-gravatar --enable-tracker --enable-bliptv --enable-raitv --disable-localmetadata --enable-dleyna --disable-dmap --disable-thetvdb --disable-tmdb --disable-freebox --enable-opensubtitles

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
rm -rf $RPM_BUILD_ROOT/%{_datadir}/gnome/help/
rm -rf $RPM_BUILD_ROOT/%{_datadir}/locale

%files -n grilo-plugin-youtube
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrlyoutube.so
%{_libdir}/grilo-0.2/grl-youtube.xml

%files -n grilo-plugin-filesystem
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrlfilesystem.so
%{_libdir}/grilo-0.2/grl-filesystem.xml

%files -n grilo-plugin-jamendo
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrljamendo.so
%{_libdir}/grilo-0.2/grl-jamendo.xml

%files -n grilo-plugin-lastfm-albumart
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrllastfm-albumart.so
%{_libdir}/grilo-0.2/grl-lastfm-albumart.xml

%files -n grilo-plugin-flickr
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrlflickr.so
%{_libdir}/grilo-0.2/grl-flickr.xml

%files -n grilo-plugin-podcasts
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrlpodcasts.so
%{_libdir}/grilo-0.2/grl-podcasts.xml

# %files -n grilo-plugin-bookmarks
# %defattr(-,root,root,-)
# %{_libdir}/grilo-0.2/libgrlbookmarks.so
# %{_libdir}/grilo-0.2/grl-bookmarks.xml

%files -n grilo-plugin-shoutcast
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrlshoutcast.so
%{_libdir}/grilo-0.2/grl-shoutcast.xml

%files -n grilo-plugin-apple-trailers
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrlappletrailers.so
%{_libdir}/grilo-0.2/grl-apple-trailers.xml

%files -n grilo-plugin-metadata-store
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrlmetadatastore.so
%{_libdir}/grilo-0.2/grl-metadata-store.xml

%files -n grilo-plugin-vimeo
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrlvimeo.so
%{_libdir}/grilo-0.2/grl-vimeo.xml

%files -n grilo-plugin-gravatar
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrlgravatar.so
%{_libdir}/grilo-0.2/grl-gravatar.xml

%files -n grilo-plugin-tracker
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrltracker.so
%{_libdir}/grilo-0.2/grl-tracker.xml

%files -n grilo-plugin-bliptv
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrlbliptv.so
%{_libdir}/grilo-0.2/grl-bliptv.xml

# %files -n grilo-plugin-localmetadata
# %defattr(-,root,root,-)
# %{_libdir}/grilo-0.2/libgrllocalmetadata.so
# %{_libdir}/grilo-0.2/grl-local-metadata.xml

%files -n grilo-plugin-raitv
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrlraitv.so
%{_libdir}/grilo-0.2/grl-raitv.xml

%files -n grilo-plugin-magnatune
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrlmagnatune.so
%{_libdir}/grilo-0.2/grl-magnatune.xml

%files -n grilo-plugin-dleyna
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrldleyna.so
%{_libdir}/grilo-0.2/grl-dleyna.xml

%files -n grilo-plugin-opensubtitles
%defattr(-,root,root,-)
%{_libdir}/grilo-0.2/libgrlopensubtitles.so
%{_libdir}/grilo-0.2/grl-opensubtitles.xml
