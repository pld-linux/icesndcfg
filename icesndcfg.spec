Summary:	IceSound Configurator
Summary(pl):	Konfigurator IceSounda
Name:		icesndcfg
Version:	0.8
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://www.selena.kherson.ua/xvadim/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
URL:		http://www.selena.kherson.ua/xvadim/programse.html#icesndcfg
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
Requires:	icewm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is a small utility for configuration IceSound. It allows you to
set any wav-file for IceWM guievnts very easy.

%description -l pl
Jest to ma³e narzêdzie konfiguruj±ce IceSound. Pozwala ono na bardzo
³atwe ustawienie dowolnych plików .wav dla zdarzeñ IceWM-a.

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-esd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Settings/IceWM/,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf ../icesndcfg/pixmaps/icon-ice.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/icesndcfg.xpm
ln -sf ../icesndcfg/pixmaps $RPM_BUILD_ROOT%{_pixmapsdir}/icesndcfg
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/icesndcfg
%{_pixmapsdir}/*
%{_applnkdir}/Settings/IceWM/*
