Summary:	Simple X MUD client
Summary(pl):	Prosty klient MUDa pod Xy
Name:		sclient
Version:	0.7.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://sclient.linux.se/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Simple X MUD client.

%description -l pl
Prosty klient MUDa pod Xy.

%prep
%setup -q

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%configure \
	--%{?debug:en}%{!?debug:dis}able-more-warnings
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/sclient $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README AUTHORS BUGS NEWS TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
