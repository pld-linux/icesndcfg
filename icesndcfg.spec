Summary:	IceSound Configurator
Summary(pl.UTF-8):   Konfigurator IceSounda
Name:		icesndcfg
Version:	0.8
Release:	3
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://www.selena.kherson.ua/xvadim/%{name}-%{version}.tar.bz2
# Source0-md5:	e636114a659b80bce22ae83d480a9a66
Source1:	%{name}.desktop
Patch0:		%{name}-ac.patch
URL:		http://www.selena.kherson.ua/xvadim/programse.html#icesndcfg
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
Requires:	icewm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small utility for configuration IceSound. It allows you to
set any .WAV file for IceWM guievnts very easy.

%description -l pl.UTF-8
Jest to małe narzędzie konfigurujące IceSound. Pozwala ono na bardzo
łatwe ustawienie dowolnych plików .WAV dla zdarzeń IceWM-a.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-esd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf ../icesndcfg/pixmaps/icon-ice.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/icesndcfg.xpm
ln -sf ../icesndcfg/pixmaps $RPM_BUILD_ROOT%{_pixmapsdir}/icesndcfg
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/icesndcfg
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
