Summary:	Rockin' asteroids game - 1980 theme
Summary(pl):	Gra, w której strzelasz do asteroidów - temat 1980
Name:		Maelstrom-1980
Version:	1
Release:	1
License:	dunno
Group:		X11/Application/Games
Source0:	http://www.devolution.com/~slouken/Maelstrom/add-ons/Maelstrom_1980.tar.gz
URL:		http://www.devolution.com/~slouken/Maelstrom/add-ons/
Requires:	Maelstrom
Obsoletes:	Maelstrom-Star_Trek
Obsoletes:	Maelstrom-Star_Wars
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_gamedir	%{_datadir}/Maelstrom

%description
1980 theme for Maelstrom.

%description -l pl
Temat 1980 dla Maelstroma.

%prep
%setup -q -n Maelstrom_1980

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gamedir}

install %* $RPM_BUILD_ROOT%{_gamedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{_gamedir}/*
