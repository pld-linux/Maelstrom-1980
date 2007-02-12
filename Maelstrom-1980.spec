Summary:	Rockin' asteroids game - 1980 theme
Summary(pl.UTF-8):   Gra, w której strzelasz do asteroidów - motyw 1980
Name:		Maelstrom-1980
Version:	1
Release:	3
License:	unknown
Group:		X11/Applications/Games
# Source0-md5:	9e56052936121b1a8b904d4b36253b0b
Source0:	http://www.devolution.com/~slouken/projects/Maelstrom/add-ons/Maelstrom_1980.zip
URL:		http://www.devolution.com/~slouken/projects/Maelstrom/add-ons.html
Requires:	Maelstrom
Obsoletes:	Maelstrom-Star_Trek
Obsoletes:	Maelstrom-Star_Wars
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamedir	%{_datadir}/Maelstrom

%description
1980 theme for Maelstrom.

%description -l pl.UTF-8
Motyw 1980 dla Maelstroma.

%prep
%setup -q -n Maelstrom_1980

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gamedir}

install "%Maelstrom Sounds" $RPM_BUILD_ROOT%{_gamedir}/Maelstrom_Sounds.bin
install "%Maelstrom Sprites" $RPM_BUILD_ROOT%{_gamedir}/Maelstrom_Sprites.bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{_gamedir}/*
