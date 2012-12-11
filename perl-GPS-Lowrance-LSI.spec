%define upstream_name    GPS-Lowrance-LSI
%define upstream_version 0.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Lowrance Serial Interface Protocol module in Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/GPS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp::Assert)
BuildRequires:	perl(Parse::Binary::FixedFormat)
BuildArch:	noarch

%description
This module provides _very_ low-level support for the LSI (Lowrance Serial
Interface) 100 protocol used to communicate with Lowrance and Eagle GPS
devices.

(Higher-level functions and wrappers for specific commands will be provided
in other modules. This module is intentionally kept simple.)

Functions
    * lsi_query

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.230.0-2mdv2011.0
+ Revision: 654965
- rebuild for updated spec-helper

* Mon Jun 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2011.0
+ Revision: 381783
- adding missing buildrequires:
- import perl-GPS-Lowrance-LSI


* Sun May 31 2009 cpan2dist 0.23-1mdv
- initial mdv release, generated with cpan2dist

