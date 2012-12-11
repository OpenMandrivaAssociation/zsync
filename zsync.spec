%define name zsync
%define version 0.6.2
%define release %mkrel 1

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
zsync is a file transfer program. It allows you to download a file
from a remote web server, where you have a copy of an older version of
the file on your computer already. zsync downloads only the new parts
of the file. It uses the same algorithm as rsync.

zsync does not require any special server software or a shell account
on the remote system (rsync, in comparison, requires that you have an
rsh or ssh account, or that the remote system runs rsyncd). Instead,
it uses a control file - a .zsync file - that describes the file to be
downloaded and enables zsync to work out which blocks it needs. This
file can be created by the admin of the web server hosting the
download, and placed alongside the file to download - it is generated
once, then any downloaders with zsync can use it.

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



%changelog
* Sun Oct 10 2010 Giuseppe Ghibò <ghibo@mandriva.com> 0.6.2-1mdv2011.0
+ Revision: 584627
- Update to release 0.6.2.

* Sun Nov 08 2009 Olivier Thauvin <nanardon@mandriva.org> 0.6.1-1mdv2010.1
+ Revision: 462918
- 0.6.1

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.6-2mdv2010.0
+ Revision: 446354
- rebuild

* Sun Jan 25 2009 Olivier Thauvin <nanardon@mandriva.org> 0.6-1mdv2009.1
+ Revision: 333342
- 0.6

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 0.5-5mdv2009.0
+ Revision: 263230
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 0.5-4mdv2009.0
+ Revision: 262913
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.5-2mdv2008.1
+ Revision: 136634
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Olivier Thauvin <nanardon@mandriva.org> 0.5-2mdv2008.0
+ Revision: 68565
- rebuild


* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 17:35:27 (53598)
- add source

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 17:35:04 (53597)
- 0.5

* Wed Jul 12 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 07/12/06 20:24:56 (41024)
- sync with last version

* Wed Jul 12 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 07/12/06 18:17:50 (40988)
Import zsync

* Wed Jul 12 2006 Lenny Cartier <lenny@mandriva.com> 0.4.3-1mdv2007.0
- 0.4.3

* Sat Dec 31 2005 Olivier Thauvin <nanardon@mandriva.org> 0.4.2-1mdk
- 0.4.2
- Happy new year, best wishes

* Sun Jul 17 2005 Olivier Thauvin <nanardon@mandriva.org> 0.4.1-1mdk
- 0.4.1

* Wed May 11 2005 Olivier Thauvin <nanardon@mandriva.org> 0.4.0-1mdk
- 0.4.0

* Tue Mar 29 2005 Olivier Thauvin <nanardon@mandrake.org> 0.3.3-1mdk
- 0.3.3

* Tue Mar 22 2005 Olivier Thauvin <nanardon@mandrake.org> 0.3.1-1mdk
- 0.3.1

* Sat Mar 12 2005 Olivier Thauvin <nanardon@mandrake.org> 0.3.0-3mdk
- really fix summary (re thanks Zero_Dogg)

* Sat Mar 12 2005 Olivier Thauvin <nanardon@mandrake.org> 0.3.0-2mdk
- <Zero_Dogg> Nanar: spelling error in zsync: "tranfert" == "transfer" i summary

* Sat Mar 12 2005 Olivier Thauvin <nanardon@mandrake.org> 0.3.0-1mdk
- 0.3.0

* Fri Feb 18 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.2.3-1mdk
- 0.2.3

* Sun Feb 13 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.2.2-1mdk
- 0.2.2

* Wed Feb 09 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.2.1-1mdk
- First mdk spec

