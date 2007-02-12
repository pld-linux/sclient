Summary:	Simple X MUD client
Summary(pl.UTF-8):	Prosty klient MUDa pod Xy
Name:		sclient
Version:	0.7.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://sclient.linux.se/%{name}-%{version}.tar.gz
# Source0-md5:	e399bad04fb5837c5be1d9874fbfac32
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Simple X MUD client.

%description -l pl.UTF-8
Prosty klient MUDa pod Xy.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--%{?debug:en}%{!?debug:dis}able-more-warnings
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/sclient $RPM_BUILD_ROOT%{_bindir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS BUGS NEWS TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
