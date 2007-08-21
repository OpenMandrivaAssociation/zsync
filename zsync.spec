%define name zsync
%define version 0.5
%define release %mkrel 2

Summary: An rsync like transfer software over http
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: Artistic
Group: Networking/File transfer
Url: http://zsync.moria.org.uk/
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
zsync is a file transfer program. It allows you to download a file from a
remote web server, where you have a copy of an older version of the file on
your computer already. zsync downloads only the new parts of the file. It uses
the same algorithm as rsync.

zsync does not require any special server software or a shell account on the
remote system (rsync, in comparison, requires that you have an rsh or ssh
account, or that the remote system runs rsyncd). Instead, it uses a control
file - a .zsync file - that describes the file to be downloaded and enables
zsync to work out which blocks it needs. This file can be created by the admin
of the web server hosting the download, and placed alongside the file to
download - it is generated once, then any downloaders with zsync can use it.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%__rm -fr %buildroot%_datadir/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS README
%_bindir/*
%_mandir/man?/*
