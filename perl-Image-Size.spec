%define module	Image-Size
%define name	perl-%{module}
%define version 3.2
%define release %mkrel 1
%define epoch	1

Name: 		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		%{epoch}
Summary:	Read the dimensions of an image in several popular formats
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Image/%{module}-%{version}.tar.bz2
BuildRequires:	perl(Compress::Zlib)
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
%make

%check
make test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%{_mandir}/*/*
%{perl_vendorlib}/Image
%{perl_vendorlib}/auto/Image

