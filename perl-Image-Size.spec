%define module	Image-Size
%define name	perl-%{module}
%define version 3.0
%define release %mkrel 2
%define epoch	1

Name: 		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		%{epoch}
Summary:	Read the dimensions of an image in several popular formats
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Expect/%{module}-%{version}.tar.bz2
BuildRequires:	perl-Compress-Zlib
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Image::Size is a library based on the image-sizing code in the wwwimagesize
script, a tool that analyzes HTML files and adds HEIGHT and WIDTH tags to
IMG directives.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS='%{optflags} -DENGLISH'

%check
make test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/Image
%{perl_vendorlib}/auto/Image

