Summary:	IceSound Configurator
Summary(pl):	Konfigurator IceSound'a
Name:		icesndcfg
Version:	0.8
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://www.selena.kherson.ua/xvadim/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
URL:		http://www.selena.kherson.ua/xvadim/programise.html#icesndcfg
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	esound-devel
Requires:	icewm
Requires:	gtk+ >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is a small utility for configuration IceSound. It allows you to
set any wav-file for IceWM guievnts very easy.

%description -l pl
Jest to ma³e narzêdzie konfiguruj±ce IceSound. Pozwala ono na bardzo
³atwe ustawienie dowolnych plików .wav dla zdarzeñ IceWM'a.

%prep
%setup -q

%build
%configure2_13 --enable-esd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Settings/IceWM/,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

ln -sf ../icesndcfg/pixmaps/icon-ice.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/icesndcfg.xpm
ln -sf ../icesndcfg/pixmaps $RPM_BUILD_ROOT%{_pixmapsdir}/icesndcfg
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/

gzip -9nf AUTHORS ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/icesndcfg/
%{_pixmapsdir}/*
%{_applnkdir}/Settings/IceWM/*
