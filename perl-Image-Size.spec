%define upstream_name	 Image-Size
%define upstream_version 3.230

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6
Epoch:		1

Summary:	Read the dimensions of an image in several popular formats
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Image/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl-devel

BuildArch:	noarch

%description
Image::Size is a library based on the image-sizing code in the wwwimagesize
script, a tool that analyzes HTML files and adds HEIGHT and WIDTH tags to
IMG directives.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{_bindir}/imgsize
%{_mandir}/*/*
%{perl_vendorlib}/Image
%{perl_vendorlib}/auto/Image


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:3.230.0-4mdv2012.0
+ Revision: 765366
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1:3.230.0-3
+ Revision: 763868
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:3.230.0-2
+ Revision: 667218
- mass rebuild

* Thu Sep 02 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:3.230.0-1mdv2011.0
+ Revision: 575396
- update to 3.230

* Mon Apr 26 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:3.221.0-1mdv2010.1
+ Revision: 539085
- update to 3.221

* Tue Nov 10 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:3.220.0-1mdv2010.1
+ Revision: 463918
- update to 3.220

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:3.210.0-1mdv2010.1
+ Revision: 461322
- update to 3.210

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1:3.2-2mdv2010.0
+ Revision: 426514
- rebuild

* Tue Feb 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:3.2-1mdv2009.1
+ Revision: 344394
- new version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1:3.1.1-2mdv2009.0
+ Revision: 223794
- rebuild

* Wed Feb 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:3.1.1-1mdv2008.1
+ Revision: 173293
- update to new version 3.1.1

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:3.01-1mdv2008.0
+ Revision: 48726
- switch to Module::Build

  + Olivier Thauvin <nanardon@mandriva.org>
    - buildrequires
    - 3.01


* Mon Jul 17 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 1:3.0-2
- add BuildRequires: perl-Compress-Zlib

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1:3.0-1mdv2007.0
- new version
- rpmbuildupdate aware
- spec cleanup
- better summary

* Tue Jan 18 2005 Abel Cheung <deaddog@mandrake.org> 2.992-3mdk
- rebuild

* Tue Aug 12 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.992-2mdk
- rebuild for new perl
- use %%makeinstall_std macro

* Mon Jul 21 2003 François Pons <fpons@mandrakesoft.com> 2.992-1mdk
- 2.992.

